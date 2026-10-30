---
name: web-search
description: 联网搜索并抓取正文。用于 ZCode 自带 WebSearch 报 "Current model does not support native WebSearch"、内置搜索返回无关内容、需要查官方文档尤其是PDF时。AnySearch 搜索 + Firecrawl 抓全文（含 PDF）。
---

# web-search

替代 ZCode 内置联网搜索。抓搜索引擎结果页在本机走不通（Bing 对相当比例查询返回完全无关的结果，百度/搜狗弹验证码，Google/DDG/Brave 等 网络不能直连），所以直接用搜索 API。

## 后端分工

按能力分工：

| 后端 | 用途 |
|---|---|
| **AnySearch** | 搜索 |
| **Firecrawl** | 抓正文 |
| Tavily | 抓正文备用 |

AnySearch 的 `content` 只有百余字符，不能用来读正文。

## 用法

```bash
PY="C:/Users/UserX/.conda/envs/opencv/python.exe"
SK="C:/Users/UserX/.zcode/skills/web-search/zsearch.py"

"$PY" "$SK" "查询" -n 6              # 搜索
"$PY" "$SK" "查询" -o                # 去掉中文功能词再搜，官方文档排前
"$PY" "$SK" "查询" --read 1,2        # 搜索 + 抓第 1、2 条正文
"$PY" "$SK" "URL" --scrape           # 直接抓正文（支持 PDF）
"$PY" "$SK" "查询" --json            # 结构化输出
```

## `-o` 的作用

中文功能词会压掉官方文档排名。`-o` 用去功能词的版本再搜一次并前置结果，查技术细节时加上。

## 注意

- snippet 只是摘要，要参数/代码/引脚定义就 `--read` 或 `--scrape`。
- 搜索接口对 PDF 只给标题和摘要，**正文必须 `--scrape`**。
- 登录墙站点（天眼查、知乎部分页）能搜到链接但抓不到正文。
- Key 在 skill 目录：`.anysearch_key` / `.firecrawl_key` / `.tavily_key`，也支持环境变量。
