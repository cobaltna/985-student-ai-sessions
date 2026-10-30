#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""zsearch - 联网搜索 + 正文抓取。

后端分工：
  AnySearch  搜索
  Firecrawl  抓正文（能解析 PDF）
  Tavily     抓正文备用

三家额度相同（每月 1000 次）。

用法:
    python zsearch.py "查询"                    # 搜索，8 条
    python zsearch.py "查询" --read 1            # 额外抓第 1 条的完整正文
    python zsearch.py "查询" --read 1,2 --save  # 正文存成 md
    python zsearch.py "URL" --scrape             # 直接抓某个 URL 的正文
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from urllib.parse import urlparse

import requests

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
TIMEOUT = 120


def _key(name: str, env: str) -> str:
    """key 查找：环境变量 -> skill 目录 .<name>_key -> ~/.<name>_key"""
    v = os.environ.get(env)
    if v:
        return v.strip()
    for p in (os.path.join(HERE, f".{name}_key"),
              os.path.join(os.path.expanduser("~"), ".zcode", "skills",
                           "web-search", f".{name}_key"),
              os.path.join(os.path.expanduser("~"), f".{name}_key")):
        try:
            with open(p, encoding="utf-8") as f:
                return f.read().strip()
        except Exception:
            continue
    return ""


# ------------------------------------------------------------------ 搜索

def anysearch(q, limit=8):
    key = _key("anysearch", "ANYSEARCH_API_KEY")
    if not key:
        return None
    r = requests.post("https://api.anysearch.com/v1/search",
                      headers={"Authorization": f"Bearer {key}"},
                      json={"query": q, "limit": limit}, timeout=TIMEOUT)
    if r.status_code != 200:
        raise RuntimeError(f"anysearch HTTP {r.status_code}: {r.text[:120]}")
    out = []
    for x in (r.json().get("data") or {}).get("results") or []:
        out.append({"title": x.get("title") or "",
                    "url": x.get("url") or "",
                    "snippet": (x.get("content") or x.get("snippet") or "")[:400],
                    "backend": "anysearch"})
    return out


def firecrawl_search(q, limit=8):
    key = _key("firecrawl", "FIRECRAWL_API_KEY")
    if not key:
        return None
    r = requests.post("https://api.firecrawl.dev/v1/search",
                      headers={"Authorization": f"Bearer {key}"},
                      json={"query": q, "limit": limit}, timeout=TIMEOUT)
    if r.status_code != 200:
        raise RuntimeError(f"firecrawl HTTP {r.status_code}: {r.text[:120]}")
    return [{"title": x.get("title") or "",
             "url": x.get("url") or "",
             "snippet": (x.get("description") or "")[:400],
             "backend": "firecrawl"}
            for x in r.json().get("data") or []]


def tavily_search(q, limit=8):
    key = _key("tavily", "TAVILY_API_KEY")
    if not key:
        return None
    r = requests.post("https://api.tavily.com/search",
                      headers={"Authorization": f"Bearer {key}"},
                      json={"query": q, "max_results": limit,
                            "search_depth": "advanced"}, timeout=TIMEOUT)
    if r.status_code != 200:
        raise RuntimeError(f"tavily HTTP {r.status_code}: {r.text[:120]}")
    return [{"title": x.get("title") or "", "url": x.get("url") or "",
             "snippet": (x.get("content") or "")[:400], "backend": "tavily"}
            for x in r.json().get("results") or []]


BACKENDS = (("anysearch", anysearch), ("firecrawl", firecrawl_search),
            ("tavily", tavily_search))


def _de_cjk(q):
    """去掉中文功能词，留下术语。中文功能词会压掉官方文档的排名。"""
    s = re.sub(r"[（(].*?[)）]", " ", q)
    s = re.sub(r"(怎么用|如何使用|使用方法?|用法|配置|教程|原理|详解|介绍|"
               r"是什么|的区别|官方文档|文档|示例|例子|模式|并发写|并发)", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def search(q, limit=8, official=False):
    """按优先级问；主后端成功就用它，失败才降级。不合并各后端结果。"""
    errors = []
    for name, fn in BACKENDS:
        try:
            res = fn(q, limit)
        except Exception as e:
            errors.append(f"{name}: {str(e)[:100]}")
            continue
        if res:
            for it in res:
                it["backend"] = name
            if official:
                # 用去功能词的术语版再搜一次。中文功能词会实打实压掉官方文档排名：
                # 'SQLite WAL mode concurrent writes' 官方第 1，加上"模式 并发写"就掉出前 5。
                # 术语版结果前置（更可能给官方源），原始结果去重后接在后面。
                try:
                    res2 = fn(_de_cjk(q) or q, limit)
                except Exception:
                    res2 = None
                if res2:
                    for it in res2:
                        it["backend"] = name
                    seen = {r["url"] for r in res2}
                    res = res2 + [r for r in res if r["url"] not in seen]
            return res, name, errors
        if res is None:
            errors.append(f"{name}: 未配置 key")
    return [], None, errors


# ------------------------------------------------------------------ 正文

def _read_anysearch(url):
    """AnySearch 的 content 只有百余字符，抓不了正文，跳过。"""
    return ""


def read_firecrawl(url):
    key = _key("firecrawl", "FIRECRAWL_API_KEY")
    if not key:
        return ""
    r = requests.post("https://api.firecrawl.dev/v1/scrape",
                      headers={"Authorization": f"Bearer {key}"},
                      json={"url": url, "formats": ["markdown"]},
                      timeout=180)
    if r.status_code != 200:
        return ""
    return (r.json().get("data") or {}).get("markdown") or ""


def read_tavily(url):
    key = _key("tavily", "TAVILY_API_KEY")
    if not key:
        return ""
    r = requests.post("https://api.tavily.com/extract",
                      headers={"Authorization": f"Bearer {key}"},
                      json={"urls": [url], "extract_depth": "advanced",
                            "format": "markdown"}, timeout=120)
    if r.status_code != 200:
        return ""
    for x in r.json().get("results") or []:
        return x.get("raw_content") or ""
    return ""


def read_trafilatura(url):
    try:
        import trafilatura
        html = trafilatura.fetch_url(url)
        if not html:
            return ""
        return trafilatura.extract(html, include_tables=True,
                                   favor_precision=True) or ""
    except Exception:
        return ""


def read_page(url):
    """抓正文：Firecrawl 优先（能解析 PDF），失败退 trafilatura。"""
    for fn in (read_firecrawl, read_tavily, read_trafilatura):
        try:
            txt = fn(url)
        except Exception:
            continue
        if txt and len(txt) > 200:
            return txt, fn.__name__.replace("read_", "")
    return "", ""


# ------------------------------------------------------------------ 输出

def host_of(u):
    try:
        return urlparse(u).netloc.replace("www.", "")
    except Exception:
        return ""


def render(q, results, backend, errors, bodies):
    lines = [f"## 搜索：{q}", ""]
    if backend:
        lines.append(f"> 后端：{backend}")
    if errors and not results:
        lines.append("> " + "; ".join(errors))
    lines.append("")
    if not results:
        lines.append("**没有结果。** 检查 key 或换个查询词。")
        return "\n".join(lines)
    for i, r in enumerate(results, 1):
        lines.append(f"{i}. **{r['title']}**")
        lines.append(f"   {r['url']}")
        if r["snippet"]:
            lines.append(f"   {re.sub(r'\s+', ' ', r['snippet'])[:220]}")
        body = bodies.get(r["url"])
        if body:
            body = re.sub(r"\n{3,}", "\n\n", body).strip()
            lines.append("")
            lines.append(f"   --- 正文（{len(body)} 字符）---")
            lines.append(body)
        lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", help="查询词，或配合 --scrape 时传 URL")
    ap.add_argument("-n", "--num", type=int, default=8)
    ap.add_argument("--read", default="",
                    help="抓第几条的完整正文，逗号分隔，如 1,2")
    ap.add_argument("--scrape", action="store_true", help="把 query 当 URL 直接抓正文")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--save", action="store_true", help="正文存到正文.md")
    ap.add_argument("--official", "-o", action="store_true",
                    help="额外用去掉中文功能词的查询再搜一次，把官方文档提上来")
    a = ap.parse_args()

    t0 = time.time()

    if a.scrape:
        body, via = read_page(a.query)
        if a.json:
            print(json.dumps({"url": a.query, "via": via,
                              "content": body}, ensure_ascii=False, indent=1))
        else:
            print(f"## {a.query}\n> 抓取器：{via or '失败'}  长度：{len(body)}\n")
            print(body or "**抓取失败。**")
        return

    results, backend, errors = search(a.query, a.num, a.official)

    bodies = {}
    if a.read and results:
        idx = [int(x) for x in a.read.split(",") if x.strip().isdigit()]
        for i in idx:
            if 1 <= i <= len(results):
                r = results[i - 1]
                body, _ = read_page(r["url"])
                if body:
                    bodies[r["url"]] = body

    if a.json:
        print(json.dumps({"query": a.query, "backend": backend, "errors": errors,
                          "elapsed": round(time.time() - t0, 1),
                          "results": [{**r, "content": bodies.get(r["url"], "")}
                                      for r in results]},
                         ensure_ascii=False, indent=1))
        return

    out = render(a.query, results, backend, errors, bodies)
    print(out)
    if a.save and bodies:
        path = "正文.md"
        with open(path, "w", encoding="utf-8") as f:
            f.write(out)
        print(f"\n已保存到 {path}")
    print(f"\n({time.time() - t0:.1f}s)")


if __name__ == "__main__":
    main()
