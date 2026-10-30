"""
Minecraft 基岩版模组开发文档深度爬取主程序（多站点版）

站点与模式见 config/crawler_config.py：
  - deep    模式：从入口页出发做 BestFirst 链接发现（适合链接密集的文档站）
  - url_list 模式：从 sitemap / llms.txt 生成显式清单逐页抓取（适合 SPA / 全站确定性抓取）

用法：
  python advanced_crawler.py                # 抓取全部站点
  python advanced_crawler.py bedrock_wiki   # 只抓指定站点（名字见 SITES[].name）
"""

import asyncio
import re
import signal
import sys
import json
import urllib.request
from datetime import datetime
from pathlib import Path

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode, BrowserConfig
from crawl4ai.deep_crawling import BestFirstCrawlingStrategy

from config.crawler_config import (
    SITES, SiteConfig,
    CONCURRENT_REQUESTS, DELAY_BETWEEN_REQUESTS, PAGE_TIMEOUT, OUTPUT_DIR, ENABLE_CACHE,
)
from filters.minecraft_filters import create_filter_chain, create_scorer, url_allowed
from scrapers.content_processor import MinecraftContentProcessor
from storage.data_saver import MinecraftDataSaver


class MinecraftCreatorCrawler:
    """
    Minecraft 文档爬虫主类

    功能：
    1. 多站点抓取（社区维基 / 官方文档镜像 / 微软 Script API）
    2. 智能过滤（域名/路径白名单 + 关键词评分），剔除广告与杂页
    3. URL 去重 + 内容级去重（正文指纹），跨站点重复只保留一份
    4. 断点续传（crawl4ai 缓存 + 索引查重）
    5. 分站点统计与日志
    """

    def __init__(self):
        self.processor = MinecraftContentProcessor()
        self.saver = MinecraftDataSaver(OUTPUT_DIR)

        # 分站点统计
        self.stats = {}

        # 优雅退出标志
        self.should_stop = False

        # 设置信号处理（Ctrl+C 优雅退出）
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

    def _signal_handler(self, signum, frame):
        """处理中断信号"""
        print("\n\n⚠️  收到中断信号，正在优雅退出...")
        print("   当前进度已保存，下次运行会自动续传")
        self.should_stop = True

    # ============ 总控 ============

    async def run(self, site_names=None):
        targets = [s for s in SITES if not site_names or s.name in site_names]
        if not targets:
            print(f"❌ 未找到站点，可选: {', '.join(s.name for s in SITES)}")
            return

        print("🚀 Minecraft 基岩版模组文档爬虫启动")
        print(f"   站点: {', '.join(s.name for s in targets)}")
        print(f"   输出目录: {OUTPUT_DIR}")
        print(f"   已有语料: {self.saver.existing_docs['total_count']} 篇（自动去重续传）")
        print("-" * 70)

        # 本机 playwright 未捆绑对应版本 chromium，改用系统 Edge（chromium 内核，零下载）
        browser_cfg = BrowserConfig(headless=True, chrome_channel="msedge", verbose=False)
        async with AsyncWebCrawler(config=browser_cfg) as crawler:
            for site in targets:
                if self.should_stop:
                    break
                await self.run_site(crawler, site)

        self._print_final_stats()

    async def run_site(self, crawler, site: SiteConfig):
        self.stats[site.name] = {
            "start_url": site.start_url,
            "mode": site.mode,
            "total_pages": 0, "successful": 0, "failed": 0,
            "skipped_seen": 0, "skipped_junk": 0, "skipped_duplicate_content": 0,
            "by_type": {},
            "started_at": datetime.now().isoformat(),
        }
        print(f"\n{'=' * 70}\n🌐 站点[{site.name}] 开始  模式={site.mode}  入口={site.start_url}\n{'=' * 70}")

        try:
            if site.mode == "url_list":
                urls = self._build_url_list(site)
                print(f"   清单共 {len(urls)} 个待抓 URL")
                await self._crawl_url_list(crawler, site, urls)
            else:
                await self._crawl_deep(crawler, site)
        except Exception as e:
            print(f"❌ 站点[{site.name}] 异常终止: {e!r}")

        self.stats[site.name]["finished_at"] = datetime.now().isoformat()
        self._save_stats()

    # ============ deep 模式 ============

    async def _crawl_deep(self, crawler, site: SiteConfig):
        """多入口深度爬取：start_url 与 extra_seeds 各自作为一次 BestFirst 爬取的入口"""
        entries = [site.start_url] + list(site.extra_seeds)

        for i, entry in enumerate(entries):
            if self.should_stop:
                return
            remaining = site.max_pages - self.stats[site.name]["total_pages"]
            if remaining <= 0:
                print(f"   ⏹ [{site.name}] 页数预算用尽，跳过入口 {i + 1}/{len(entries)}: {entry}")
                return

            filter_chain = create_filter_chain(site)
            scorer = create_scorer(site)

            deep_strategy = BestFirstCrawlingStrategy(
                max_depth=site.max_depth,
                max_pages=remaining,
                filter_chain=filter_chain,
                url_scorer=scorer,
                include_external=False
            )

            config = CrawlerRunConfig(
                deep_crawl_strategy=deep_strategy,
                cache_mode=CacheMode.ENABLED if ENABLE_CACHE else CacheMode.DISABLED,
                stream=True,
                verbose=False,
                page_timeout=PAGE_TIMEOUT,
            )

            print(f"   🔎 [{site.name}] 深度入口 {i + 1}/{len(entries)}: {entry}")
            try:
                crawl_generator = await crawler.arun(url=entry, config=config)
                async for result in crawl_generator:
                    if self.should_stop:
                        return
                    await self._handle_result(result, site)
            except Exception as e:
                print(f"❌ [{site.name}] 入口异常 {entry}: {e!r}")

    # ============ url_list 模式 ============

    MEDIA_EXT = re.compile(
        r"\.(png|jpe?g|gif|svg|webp|ico|bmp|tga|psd|pdf|zip|mp3|ogg|wav|mp4|"
        r"woff2?|ttf|json|xml|js|lang|txt|mcfunction|mcstructure|mcpack|mctemplate)$",
        re.IGNORECASE,
    )

    def _is_media_url(self, url: str) -> bool:
        """剔除图片/音频/原始样例文件等非文档 URL（wiki 的 /files/ 目录托管教程样例资产）"""
        path = url.split("?")[0]
        if self.MEDIA_EXT.search(path):
            return True
        return "/files/" in path

    def _build_url_list(self, site: SiteConfig):
        """按 url_source 抓取并过滤 URL 清单"""
        if site.url_source == "sitemap":
            raw = self._http_get(site.sitemap_url)
            urls = re.findall(r"<loc>\s*(.*?)\s*</loc>", raw)
        elif site.url_source == "llms_txt":
            raw = self._http_get(site.llms_txt_url)
            # 只取 “## Stable ...” 段，避免抓历史版本与预览版造成重复
            m = re.search(r"##\s*Stable[^\n]*\n(.*?)(?=\n##\s|\Z)", raw, re.DOTALL)
            section = m.group(1) if m else raw
            urls = re.findall(r"https://[^\s)\]]+", section)
        else:
            raise ValueError(f"未知 url_source: {site.url_source}")

        # 去重 + 过滤 + 续传过滤
        seen, result = set(), []
        for url in urls:
            if url in seen:
                continue
            seen.add(url)
            if self._is_media_url(url):
                continue
            if not url_allowed(site, url):
                continue
            if self.saver.is_duplicate(url):
                self.stats[site.name]["skipped_seen"] += 1
                continue
            result.append(url)

        return result[: site.max_pages]

    async def _crawl_url_list(self, crawler, site: SiteConfig, urls):
        """并发槽 + 请求间隔的礼貌抓取"""
        sem = asyncio.Semaphore(CONCURRENT_REQUESTS)

        config = CrawlerRunConfig(
            cache_mode=CacheMode.ENABLED if ENABLE_CACHE else CacheMode.DISABLED,
            stream=False,
            verbose=False,
            page_timeout=PAGE_TIMEOUT,
        )

        async def worker(url: str):
            if self.should_stop:
                return
            async with sem:
                if self.should_stop:
                    return
                try:
                    res = await crawler.arun(url=url, config=config)
                    if isinstance(res, list):  # 兼容 CrawlResultContainer
                        res = res[0] if res else None
                    await self._handle_result(res, site)
                except Exception as e:
                    self._bump(site.name, "failed")
                    print(f"❌ [{site.name}] {url} : {e!r}")
                finally:
                    await asyncio.sleep(DELAY_BETWEEN_REQUESTS)

        await asyncio.gather(*(worker(u) for u in urls))

    # ============ 结果处理 ============

    async def _handle_result(self, result, site: SiteConfig):
        if result is None:
            self._bump(site.name, "failed")
            return

        self._bump(site.name, "total_pages")

        if not result.success:
            self._bump(site.name, "failed")
            print(f"❌ [{site.name}] 失败 {result.url}: {result.error_message}")
            return

        if self.saver.is_duplicate(result.url):
            self._bump(site.name, "skipped_seen")
            return

        try:
            doc_page = self.processor.process(result, site)
        except ValueError as e:
            self._bump(site.name, "skipped_junk")
            return
        except Exception as e:
            self._bump(site.name, "failed")
            print(f"❌ [{site.name}] 处理失败 {result.url}: {e!r}")
            return

        # 内容级去重：不同 URL 的相同正文只保留一份
        if self.saver.is_duplicate_content(doc_page.content_hash):
            self._bump(site.name, "skipped_duplicate_content")
            print(f"♻️  [{site.name}] 内容重复: {doc_page.title[:40]}")
            return

        saved_files = await self.saver.save(doc_page)

        self._bump(site.name, "successful")
        content_type = doc_page.content_type
        st = self.stats[site.name]
        st["by_type"][content_type] = st["by_type"].get(content_type, 0) + 1

        depth = doc_page.metadata.get("depth", 0)
        score = doc_page.metadata.get("score", 0)
        print(f"✅ [{site.name}] 深度{depth} 评分{score:.2f} [{content_type}] {doc_page.title[:44]}")
        print(f"   💾 {Path(saved_files['markdown']).name}")

        if st["successful"] % 20 == 0:
            self._print_progress(site)

    # ============ 工具与统计 ============

    @staticmethod
    def _http_get(url: str) -> str:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research crawler)"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.read().decode("utf-8", errors="replace")

    def _bump(self, site_name: str, key: str, n: int = 1):
        self.stats[site_name][key] = self.stats[site_name].get(key, 0) + n

    def _print_progress(self, site: SiteConfig):
        st = self.stats[site.name]
        print(f"\n📊 [{site.name}] {st['successful']} 成功 / {st['failed']} 失败 / "
              f"{st['skipped_seen']} 已见 / {st['skipped_junk']} 无效 / "
              f"{st['skipped_duplicate_content']} 内容重复\n")

    def _save_stats(self):
        totals = {
            k: sum(s.get(k, 0) for s in self.stats.values())
            for k in ["total_pages", "successful", "failed", "skipped_seen",
                      "skipped_junk", "skipped_duplicate_content"]
        }
        payload = {
            "run_finished_at": datetime.now().isoformat(),
            "totals": totals,
            "sites": self.stats,
        }
        stats_file = Path(OUTPUT_DIR) / "crawl_stats.json"
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

    def _print_final_stats(self):
        print("\n" + "=" * 70)
        print("🏁 爬取完成统计")
        print("=" * 70)
        for name, st in self.stats.items():
            print(f"\n🌐 {name}  ({st['mode']})")
            print(f"   总处理 {st['total_pages']} | ✅ 成功 {st['successful']} | ❌ 失败 {st['failed']}")
            print(f"   ⏭️  已存在 {st['skipped_seen']} | 无效页 {st['skipped_junk']} | "
                  f"内容重复 {st['skipped_duplicate_content']}")
            if st["by_type"]:
                print(f"   类型分布: {st['by_type']}")

        self._save_stats()
        print(f"\n💾 索引: {Path(OUTPUT_DIR) / 'document_index.json'}")
        print(f"📁 输出目录: {Path(OUTPUT_DIR).absolute()}")


# 入口函数
async def main(site_names=None):
    crawler = MinecraftCreatorCrawler()
    await crawler.run(site_names)


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
        try:  # Windows 控制台中文/emoji 输出兜底
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

    sites = [a for a in sys.argv[1:] if not a.startswith("-")]
    asyncio.run(main(sites or None))
