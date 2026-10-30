"""
Crawl4AI 配置文件 - Minecraft 基岩版模组开发多站点文档抓取

现有语料：learn.microsoft.com/zh-cn/minecraft/creator/（148 页，见 document_index.json）
本次新增三个高价值源：
  1. wiki.bedrock.dev        —— Bedrock OSS 社区维基，最系统的基岩 add-on 教程（无广告）
  2. bedrock.dev             —— Mojang 官方 add-on 文档镜像（稳定版全量 schema/组件参考）
  3. learn.microsoft.com en  —— 英文 Script API 参考（@minecraft/server 等，中文语料缺口）
"""

from dataclasses import dataclass, field
from typing import List


# ============ 通用性能/输出设置 ============

CONCURRENT_REQUESTS = 3          # 并发请求数（对站点保持礼貌）
DELAY_BETWEEN_REQUESTS = 1.2     # 每个并发槽完成一次请求后的等待秒数
PAGE_TIMEOUT = 60000             # 单页超时（毫秒）
OUTPUT_DIR = "minecraft_docs"    # 输出目录（与已有中文语料共用，统一索引）
ENABLE_CACHE = True              # crawl4ai 缓存，中断续传


@dataclass
class SiteConfig:
    """单站点抓取配置"""

    name: str                                # 站点标识（统计/索引用）
    start_url: str                           # 入口 URL
    mode: str = "deep"                       # deep=链接发现 | url_list=显式清单
    url_source: str = ""                     # url_list 模式的清单来源: sitemap | llms_txt
    sitemap_url: str = ""                    # sitemap.xml 地址（url_source=sitemap）
    llms_txt_url: str = ""                   # llms.txt 地址（url_source=llms_txt，解析 Stable 段）
    extra_seeds: List[str] = field(default_factory=list)  # deep 模式补充种子页

    allowed_domains: List[str] = field(default_factory=list)
    allowed_patterns: List[str] = field(default_factory=list)   # URL 白名单（fnmatch）
    blocked_patterns: List[str] = field(default_factory=list)   # URL 黑名单（fnmatch）
    keywords: List[str] = field(default_factory=list)           # URL 评分关键词

    max_pages: int = 500
    max_depth: int = 4
    min_content_length: int = 300            # 正文低于该字符数视为垃圾页丢弃


# ============ 站点关键词集 ============

WIKI_KEYWORDS = [
    "behavior", "resource", "addon", "pack", "manifest", "json",
    "block", "item", "entity", "biome", "dimension", "structure", "feature",
    "loot", "recipe", "trade", "component", "animation", "animation-controller",
    "script", "scripting", "api", "molang", "particle", "sound", "effect",
    "enchantment", "ui", "world-generation", "jigsaw", "nbt", "mcstructure",
    "texture", "material", "fog", "camera", "command", "guide",
]

BEDROCK_DEV_KEYWORDS = [
    "addons", "entities", "blocks", "item", "biomes", "recipes",
    "molang", "particles", "animations", "features", "fogs",
    "schemas", "texture", "lighting", "water", "atmospherics",
]

SCRIPTAPI_KEYWORDS = [
    "minecraft-server", "server", "module", "class", "interface", "function",
    "event", "enum", "typealias", "block", "entity", "player", "world",
    "component", "system", "dimension", "container", "inventory", "item",
    "gametest", "server-ui", "server-admin", "server-net", "actionform",
]


# ============ 站点清单 ============

SITES: List[SiteConfig] = [

    # ---- 1. Bedrock Wiki：社区教程（467 个 sitemap URL，剔除杂页后约 455）----
    SiteConfig(
        name="bedrock_wiki",
        start_url="https://wiki.bedrock.dev/",
        mode="url_list",
        url_source="sitemap",
        sitemap_url="https://wiki.bedrock.dev/sitemap.xml",
        allowed_domains=["wiki.bedrock.dev"],
        allowed_patterns=["https://wiki.bedrock.dev/*"],
        blocked_patterns=[
            "*licenses*", "*privacy*", "*hacktoberfest*", "*discord*",
            "*contribute*", "*style-guide*", "*useful-links*",
            "*/test", "*/graph-test",
        ],
        keywords=WIKI_KEYWORDS,
        max_pages=600,
        min_content_length=200,
    ),

    # ---- 2. bedrock.dev：Mojang 官方文档镜像（稳定版 1.26.50.4，20 个 .md）----
    SiteConfig(
        name="bedrock_dev",
        start_url="https://bedrock.dev/",
        mode="url_list",
        url_source="llms_txt",
        llms_txt_url="https://bedrock.dev/llms.txt",
        allowed_domains=["bedrock.dev"],
        allowed_patterns=["https://bedrock.dev/docs/stable/*"],
        blocked_patterns=["*/static/*", "*algolia*", "*search*", "*packs.md*"],
        keywords=BEDROCK_DEV_KEYWORDS,
        max_pages=40,
        min_content_length=500,
    ),

    # ---- 3. Microsoft Learn 英文 Script API 参考（现有中文语料仅 4 页，最大缺口）----
    SiteConfig(
        name="ms_scriptapi_en",
        start_url="https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/",
        mode="deep",
        extra_seeds=[
            "https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server",
        ],
        allowed_domains=["learn.microsoft.com"],
        allowed_patterns=["*en-us/minecraft/creator/scriptapi/*"],
        blocked_patterns=[
            "*view=minecraft-bedrock-preview*",   # 预览/实验版 API 与稳定版重复
            "*view=minecraft-bedrock-experimental*",
            "*viewFallbackFrom=*",
            "*view=*preview*",
            "*toc.json*", "*search*", "*profile*",
        ],
        keywords=SCRIPTAPI_KEYWORDS,
        max_pages=800,
        max_depth=5,
        min_content_length=200,
    ),

    # ---- 3b. Script API 小模块补充（主模块 @minecraft/server 已抓 783 页，
    #         深度爬取预算耗尽未覆盖 server-ui/server-admin/server-net/mojang-gametest）----
    SiteConfig(
        name="ms_scriptapi_en_rest",
        start_url="https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server-ui/minecraft-server-ui",
        mode="deep",
        extra_seeds=[
            "https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server-admin/minecraft-server-admin",
            "https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server-net/minecraft-server-net",
            "https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/mojang-gametest/mojang-gametest",
        ],
        allowed_domains=["learn.microsoft.com"],
        allowed_patterns=["*en-us/minecraft/creator/scriptapi/*"],
        blocked_patterns=[
            "*view=minecraft-bedrock-preview*",
            "*view=minecraft-bedrock-experimental*",
            "*viewFallbackFrom=*",
            "*view=*preview*",
            "*scriptapi/minecraft/server/*",  # 主模块已入库，避免消耗预算
            "*toc.json*", "*search*", "*profile*",
        ],
        keywords=SCRIPTAPI_KEYWORDS,
        max_pages=200,
        max_depth=4,
        min_content_length=200,
    ),
]
