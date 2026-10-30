"""
Minecraft 基岩版模组开发文档爬虫 - 入口

用法：
  python main.py                # 抓取全部站点
  python main.py bedrock_wiki   # 只抓指定站点
"""

import asyncio
import sys

from advanced_crawler import main

if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

    asyncio.run(main([a for a in sys.argv[1:] if not a.startswith("-")] or None))
