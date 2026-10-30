# 子代理会话 sess_subagent_agent_fdf3d64e-9765-4264-a5ad-4c53fbac0831

模型: ?

## 👤 用户（2026-09-12 19:26）

请用 WebSearch/WebFetch 联网调研「京郊（北京郊区）现代农机服务及农机专业合作社」及「一条龙农机作业托管服务」新模式，用于撰写大学生《农工综合生产实习》报告。需要事实准确、可核实，并给出每条信息的来源 URL。

请重点收集：
1. 北京市农机化总体情况：农机总动力、主要农作物耕种收综合机械化率（北京最新数据，2023-2025）、京郊农机社会化服务组织数量、托管服务面积。
2. 「一条龙农机作业托管服务」模式：定义、具体环节（耕、种、管、收、秸秆处理、烘干等全程托管/半托管）、"保姆式""菜单式"服务、土地流转与生产托管区别、代表案例（北京或全国，如山东、黑龙江的农业生产托管案例数据）。
3. 京郊具体合作社案例：北京鑫利农机服务专业合作社（顺义？）、北京兴农天力农机服务专业合作社、北京绿谷汇德、大兴/顺义/房山/平谷的农机合作社。请查证其成立时间、所在地、服务面积、装备规模、经营模式、荣誉。
4. 北京市农机购置补贴、秸秆综合利用政策、深松整地补贴、小麦玉米秸秆禁烧与综合利用要求（北京最新政策口径）。
5. 农机合作社发展中的共性问题：机手老龄化、装备利用率低、维修能力弱、土地细碎化、服务价格竞争、融资难等（有公开调研数据更好）。

只输出要点清单（中文）+ 来源链接。找不到的明确写"未找到公开资料"，不要编造具体的合作社名称、数据或年份。

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

The user wants me to research online using WebSearch/WebFetch. However, I only have WebFetch and Bash available. There's no WebSearch tool listed. Let me check - I have Bash, Read, TodoWrite, WebFetch, RespondToCoordinator. No WebSearch tool.

Hmm, the task says use WebSearch/WebFetch. I don't have WebSearch. I could use WebFetch on search engine URLs? WebFetch fetches a URL and answers a prompt. I could try fetching a search engine like Bing or Baidu. But WebFetch says fails on authenticated/private URLs; cross-host redirects returned. Search engines might work or be blocked.

Also note I'm a subagent (Explore) with read-only. The system reminder mentions browser-use skill is main-agent-only and subagents must not use it.

Let me try WebFetch on search URLs. Let me attempt bing.com search, and maybe use curl via Bash? Bash is read-only allowed for read-only ops, and curl is read-only network access — but the guidelines say Bash only for read-only operations; curl fetching a page is read-only. However sandbox might block network. Let me try.

Actually the best approach: use WebFetch with search engine query URLs, then fetch the resulting pages.

Let me start with a few parallel WebFetch calls.

Let me try:
- https://www.bing.com/search?q=北京+农机总动力+2024+综合机械化率
- https://www.baidu.com/s?wd=... (Baidu may block)
- Maybe use cn.bing.com

Let me try WebFetch on Bing search.

I'll do parallel calls.

Actually, WebFetch converts page to markdown and answers prompt with a small model. For search engine results, it should extract links/text.

Let me try multiple queries.

Let me also consider known sources: 北京市农业农村局 (nyncj.beijing.gov.cn), 中国农业机械化信息网 (amic.agri.cn), 农业农村部 (moa.gov.cn), 北京市统计年鉴.

Let me start.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "Research Beijing agricultural mechanization overall data", "status": "in_progress", "priority": "high"}, {"content": "Research 'one-stop' farm machinery trusteeship model", "status": "pending", "priority": "high"}, {"content": "Research specific Beijing cooperative cases", "status": "pending", "priority": "high"}, {"content": "Research Beijing subsidies  …[截断,原长412]` → `{"oldTodos":[],"todos":[{"content":"Research Beijing agricultural mechanization overall data","status":"in_progress","priority":"high"},{"content":"Research 'one-stop' farm machinery trusteeship model","status":"pending","priority":"high"},{"content":"Research specific Beijing cooperative cases","status":"pending","pri …[截断,原长602]`

- 🔧 **WebFetch** `{"url": "https://www.bing.com/search?q=%E5%8C%97%E4%BA%AC%E5%86%9C%E6%9C%BA%E6%80%BB%E5%8A%A8%E5%8A%9B%20%E7%BB%BC%E5%90%88%E6%9C%BA%E6%A2%B0%E5%8C%96%E7%8E%87%202024", "prompt": "List any search results about Beijing agricultural machinery total power and comprehensive mechanization rate, with URLs and key data."}` → `REDIRECT DETECTED: The URL redirects to a different host. Original URL: https://www.bing.com/search?q=%E5%8C%97%E4%BA%AC%E5%86%9C%E6%9C%BA%E6%80%BB%E5%8A%A8%E5%8A%9B%20%E7%BB%BC%E5%90%88%E6%9C%BA%E6%A2%B0%E5%8C%96%E7%8E%87%202024 Redirect URL: https://cn.bing.com/search?q=%E5%8C%97%E4%BA%AC%E5%86%9C%E6%9C%BA%E6%80%BB%E …[截断,原长855]`

- 🔧 **WebFetch** `{"url": "https://www.bing.com/search?q=%E5%8C%97%E4%BA%AC%20%E5%86%9C%E4%B8%9A%E7%94%9F%E4%BA%A7%E6%89%98%E7%AE%A1%20%E4%B8%80%E6%9D%A1%E9%BE%99%20%E5%86%9C%E6%9C%BA%E4%BD%9C%E4%B8%9A", "prompt": "List search results about Beijing agricultural production trusteeship and one-stop farm machinery service, with URLs and key facts."}` → `REDIRECT DETECTED: The URL redirects to a different host. Original URL: https://www.bing.com/search?q=%E5%8C%97%E4%BA%AC%20%E5%86%9C%E4%B8%9A%E7%94%9F%E4%BA%A7%E6%89%98%E7%AE%A1%20%E4%B8%80%E6%9D%A1%E9%BE%99%20%E5%86%9C%E6%9C%BA%E4%BD%9C%E4%B8%9A Redirect URL: https://cn.bing.com/search?q=%E5%8C%97%E4%BA%AC%20%E5%86%9C …[截断,原长903]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:26）

I'll research this systematically. Let me start with searches on the key topics.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

Need to follow redirects to cn.bing.com. Let me do parallel calls.

</details>

- 🔧 **WebFetch** `{"prompt": "List any search results about Beijing agricultural machinery total power (农机总动力) and comprehensive mechanization rate (综合机械化率), with URLs and key data. Include the result titles.", "url": "https://cn.bing.com/search?q=%E5%8C%97%E4%BA%AC%E5%86%9C%E6%9C%BA%E6%80%BB%E5%8A%A8%E5%8A%9B%20%E7%BB%BC%E5%90%88%E6%9C%BA%E6%A2%B0%E5%8C%96%E7%8E%87%202024"}` → `未在提供的搜索结果中找到涉及北京“农机总动力”或“综合机械化率”的条目，也没有相关 URL 或关键数据。 页面虽显示“约 151,000 个结果”，但可见标题均为北京概况、政府门户或旅游内容，例如： - “北京市_百度百科” — https://baike.baidu.com/item/%e5%8c%97%e4%ba%ac%e5%b8%82/126069 - “Beijing - 北京市人民政府门户网站” — https://www.beijing.gov.cn/ - “北京旅游必去的20个景点，实用攻略赶紧收藏！ - 知乎” — https://zhuanlan.zhihu.com/p/623666920 这些结果摘要均未提供农机 …[截断,原长333]`

- 🔧 **WebFetch** `{"prompt": "List search results about Beijing agricultural production trusteeship (农业生产托管) and one-stop farm machinery service (一条龙农机作业), with URLs and key facts. Include result titles.", "url": "https://cn.bing.com/search?q=%E5%8C%97%E4%BA%AC%20%E5%86%9C%E4%B8%9A%E7%94%9F%E4%BA%A7%E6%89%98%E7%AE%A1%20%E4%B8%80%E6%9D%A1%E9%BE%99%20%E5%86%9C%E6%9C%BA%E4%BD%9C%E4%B8%9A"}` → `No relevant search results were found in the provided content. The query shown is “北京 农业生产托管 一条龙 农机作业”, and the page reports “约 151,000 个结果”, but the displayed results are general Beijing/tourism/government pages—not about agricultural production trusteeship or one-stop farm machinery service. Therefore, there are no m …[截断,原长370]`

- 🔧 **WebFetch** `{"prompt": "List search results about Beijing farm machinery cooperatives (农机合作社), including 北京鑫利农机服务专业合作社, 北京兴农天力农机服务专业合作社, with URLs and key facts. Include result titles.", "url": "https://cn.bing.com/search?q=%E5%8C%97%E4%BA%AC%E9%91%AB%E5%88%A9%E5%86%9C%E6%9C%BA%E6%9C%8D%E5%8A%A1%E4%B8%93%E4%B8%9A%E5%90%88%E4%BD%9C%E7%A4%BE"}` → `Based only on the provided page, I found **no search results about Beijing farm machinery cooperatives (农机合作社)**, and **no visible result for 北京兴农天力农机服务专业合作社**. The page title is “北京鑫利农机服务专业合作社 - 搜索自适应缩放”, but the listed results are general Beijing pages, not 农机合作社 pages. Visible result titles, URLs, and key facts: - “ …[截断,原长1570]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:26）

Following the redirects to cn.bing.com.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

Bing search results seem to be heavily cached/generic, likely Bing returning a generic page. Maybe the fetch is being served a "search adaptive" page. Let me try different search engines: Baidu, Sogou, or DuckDuckGo HTML. Also could try 360. Let me try:
- https://duckduckgo.com/html/?q=...
- https://www.baidu.com/s?wd=...
- https://search.cnki.com... no.

DuckDuckGo html might work. Let me try.

Also could fetch directly known authoritative pages. Let me try Bing with site: filters, and also try alternative engines.

Let me try multiple in parallel.

</details>

- 🔧 **WebFetch** `{"prompt": "List search result titles and URLs related to Beijing agricultural machinery (农机), mechanization rate, or farm machinery cooperatives.", "url": "https://duckduckgo.com/html/?q=%E5%8C%97%E4%BA%AC+%E5%86%9C%E6%9C%BA%E6%80%BB%E5%8A%A8%E5%8A%9B+%E7%BB%BC%E5%90%88%E6%9C%BA%E6%A2%B0%E5%8C%96%E7%8E%87"}` → ``

- 🔧 **WebFetch** `{"prompt": "List search result titles and URLs related to Beijing agricultural mechanization rate or farm machinery.", "url": "https://www.baidu.com/s?wd=%E5%8C%97%E4%BA%AC%E5%B8%82%E5%86%9C%E6%9C%BA%E6%80%BB%E5%8A%A8%E5%8A%9B%E7%BB%BC%E5%90%88%E6%9C%BA%E6%A2%B0%E5%8C%96%E7%8E%87"}` → `The provided web page content is blank, so there are no search result titles or URLs to list.`

- 🔧 **WebFetch** `{"prompt": "List search result titles and URLs about 农业生产托管 一条龙 农机作业托管服务模式.", "url": "https://www.sogou.com/web?query=%E5%86%9C%E4%B8%9A%E7%94%9F%E4%BA%A7%E6%89%98%E7%AE%A1%20%E4%B8%80%E6%9D%A1%E9%BE%99%20%E5%86%9C%E6%9C%BA%E4%BD%9C%E4%B8%9A%E6%89%98%E7%AE%A1"}` → `REDIRECT DETECTED: The URL redirects to a different host. Original URL: https://www.sogou.com/web?query=%E5%86%9C%E4%B8%9A%E7%94%9F%E4%BA%A7%E6%89%98%E7%AE%A1%20%E4%B8%80%E6%9D%A1%E9%BE%99%20%E5%86%9C%E6%9C%BA%E4%BD%9C%E4%B8%9A%E6%89%98%E7%AE%A1 Redirect URL: http://www.sogou.com/antispider/?m=1&antip=web_hd&from=%2Fwe …[截断,原长1188]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:26）

Bing is returning generic results. Let me try other search engines and direct authoritative sources.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

Search engines are mostly blocked. DuckDuckGo timed out. Let me try to check if Bash has network access via curl. If curl works, I can fetch pages directly or use a search API.

Let me test curl to a known site. Sandbox might block network though. Let me try.

Also, WebFetch works for specific URLs. So I can go directly to authoritative sites. Let me think of known URLs:
- 北京市农业农村局: https://nyncj.beijing.gov.cn/
- 中国农业机械化信息网: http://www.amic.agri.cn/
- 农业农村部: http://www.moa.gov.cn/
- 北京市统计局: https://nj.tjj.beijing.gov.cn/

But finding specific pages requires search. Let me try Bing with site: operator, which might work differently. Or use Bing news. Actually, maybe Bing's generic results were because the query got mangled. Let me try a simpler query with site restriction.

Let me try curl first.

</details>

- 🔧 **Bash** `{"command": "curl -s -m 20 -A \"Mozilla/5.0 (Windows NT 10.0; Win64; x64)\" \"https://cn.bing.com/search?q=%E5%8C%97%E4%BA%AC%E5%B8%82%E5%86%9C%E6%9C%BA%E6%80%BB%E5%8A%A8%E5%8A%9B\" | head -c 2000; echo \"---EXIT:$?\"", "description": "Test network access with curl to Bing"}` → `<!DOCTYPE html><html dir="ltr" lang="zh" xml:lang="zh" xmlns="http://www.w3.org/1999/xhtml" xmlns:Web="http://schemas.live.com/Web/"><script type="text/javascript" nonce="TubaTqPHwAdPYX/eR5eiCHycgHzHaHYr//K03IW5sUY=" >//<![CDATA[ window.si_ST=new Date //]]></script><head><!--pc--><title>北京市农机总动力 - 搜索</title><meta conte …[截断,原长1818]`

- 🔧 **WebFetch** `{"prompt": "List all result titles and URLs that mention 农机 or 机械化 or 合作社.", "url": "https://cn.bing.com/search?q=site%3Anyncj.beijing.gov.cn+%E5%86%9C%E6%9C%BA"}` → `WebFetch completed, but the extraction model returned no text.`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:26）

Let me check whether direct network access via curl works, and try site-specific searches.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

curl has network access. I can use curl to fetch Bing search results and parse them. Bing has RSS format: /search?format=rss&q=... That's easy to parse! Let me use that.

Let me fetch Bing RSS for queries. This gives XML with titles, links, descriptions. 

Let me do parallel curl calls with format=rss.

Queries:
1. 北京市农机总动力 综合机械化率
2. 北京 农业生产托管 一条龙
3. 北京鑫利农机服务专业合作社
4. 北京兴农天力农机服务专业合作社
5. 北京市农机购置补贴 2024
6. 北京 秸秆综合利用 政策
7. 农机合作社 问题 机手老龄化

Let me run these. Also could use `-G --data-urlencode` for proper encoding.

Note: I cannot write files, but piping to head/grep is fine (not writing to file). Reading output is fine.

Let me run multiple curl in one bash command? Better separate for clarity but parallel tool calls are good. Actually I can do one bash command with several curls. Let me do that to be efficient.

Let me use a loop maybe. But simpler: multiple curls.

Let me construct. Chinese chars in URL need encoding; curl can handle with --data-urlencode -G.

</details>

- 🔧 **Bash** `{"command": "for q in \"北京市农机总动力 综合机械化率\" \"北京 农业生产托管 一条龙 农机作业\" \"北京鑫利农机服务专业合作社\" \"北京兴农天力农机服务专业合作社\"; do echo \"=== QUERY: $q ===\"; curl -s -m 25 -A \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\" -G \"https://cn.bing.com/search\" --data-urlencode \"q=$q\" --data-urlencode \"format=rss\" | grep -oE \"<(title|link|description)>[^<]*\" | sed 's/<[a-z]*>//'; ec …[截断,原长412]` → `=== QUERY: 北京市农机总动力 综合机械化率 === 必应：%b1%b1%be%a9%ca%d0ũ%bb%fa%d7ܶ%af%c1%a6 %d7ۺϻ%faе%bb%af%c2%ca http://www.bing.com:80/search?q=%25b1%25b1%25be%25a9%25ca%25d0%c5%a9%25bb%25fa%25d7%dc%b6%25af%25c1%25a6+%25d7%db%ba%cf%bb%25fa%d0%b5%25bb%25af%25c2%25ca 搜索结果 %b1%b1%be%a9%ca%d0ũ%bb%fa%d7ܶ%af%c1%a6 %d7ۺϻ%faе%bb%af%c2%ca http: …[截断,原长10200]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:27）

curl has network access. Bing supports an RSS output format which is easy to parse. Let me query multiple topics.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

The Chinese encoding in the shell is getting mangled (GBK vs UTF-8). The Git Bash on Windows may be outputting GBK/CP936. The query is being encoded incorrectly — it seems curl is converting to GBK bytes then percent-encoding, resulting in wrong search. Actually the issue: the shell passes bytes as GBK? The RSS query shows `%b1%b1%be%a9` which is GBK for 北京. Bing interpreted as... it returned B1 驾驶证 etc. So Bing decoded the query poorly, matching "B1" because %b1... 

The problem is the terminal encoding. The Chinese characters in my command are UTF-8, but bash on Windows with cp936... hmm. Actually the output shows the URL got GBK-encoded, meaning the shell's locale converted. And Bing search returned nonsense.

Better approach: precompute URL-encoded UTF-8 queries myself. I know UTF-8 percent encoding for common Chinese terms is hard manually. Alternatively, use Python to do the quoting. Python is likely available. Let me check python and use it with requests or urllib. Python will handle UTF-8 properly.

Let me test python availability.

Actually the issue might be that curl receives the argument already as GBK bytes because Git Bash's `--data-urlencode` uses local charset? No, curl just percent-encodes bytes it receives. The bytes received were GBK, meaning bash converted the text to GBK before passing. That's due to Windows console code page.

Using Python with explicit unicode strings in the script file... but I can't write files. I can pass `python -c "..."` with unicode escapes. Or use python with sys.argv. The same shell encoding issue may apply to the command string though. Hmm, if bash passes GBK bytes to python, python decodes argv using... Python on Windows uses Unicode argv from GetCommandLineW, so it should get correct Unicode if the console handles it. But Git Bash passes via msys, might convert.

Safest: use \u escapes in Python source. E.g. 北京 = \u5317\u4eac. I can generate percent-encoding from unicode escapes, avoiding literal Chinese entirely.

Let me write a python one-liner that takes \u-escaped strings, quotes them, and fetches Bing RSS, printing titles/links/descriptions. But output Chinese also has encoding issues. Output via bash may display mojibake. I can print with `sys.stdout.buffer.write(...)` encoded utf-8, and then the tool captures raw bytes; the harness may interpret as UTF-8. Let's try.

Let me first test python and a simple fetch.

Actually simpler: use Python urllib to fetch, and encode output as utf-8 explicitly. Let me do it.

Let me construct queries using unicode escapes:
- 北京市农机总动力 \u5317\u4eac\u5e02\u519c\u673a\u603b\u52a8\u529b
- 综合机械化率 \u7efc\u5408\u673a\u68b0\u5316\u7387
- 农业生产托管 \u519c\u4e1a\u751f\u4ea7\u6258\u7ba1
- 一条龙 \u4e00\u6761\u9f99
- 农机作业 \u519c\u673a\u4f5c\u4e1a
- 北京鑫利农机服务专业合作社: \u5317\u4eac\u946b\u5229\u519c\u673a\u670d\u52a1\u4e13\u4e1a\u5408\u4f5c\u793e
- 北京兴农天力农机服务专业合作社: \u5317\u4eac\u5174\u519c\u5929\u529b\u519c\u673a\u670d\u52a1\u4e13\u4e1a\u5408\u4f5c\u793e

Let me just build a Python script with a list of query strings as unicode escape sequences. Actually writing Chinese directly in python -c might work if Python gets proper Unicode. Let me test both.

Let me test: python -c "import sys; print(sys.argv)" 北京

Hmm, output encoding. Let me just try Python fetching and writing UTF-8 bytes.

Plan: 
python -c with code that has queries in \u escapes.

Let me test simple first.

</details>

- 🔧 **Bash** `{"command": "python --version 2>&1; python3 --version 2>&1; which python python3 2>&1", "description": "Check Python availability"}` → `Exit code 2 /usr/bin/bash: line 3: python: command not found /usr/bin/bash: line 3: python3: command not found which: no python in (/c/Users/UserX/bin:/mingw64/bin:/usr/local/bin:/usr/bin:/bin:/mingw64/bin:/usr/bin:/c/Users/UserX/bin:/c/Program Files (x86)/NVIDIA Corporation/PhysX/Common:/c/windows/system32:/c/windows: …[截断,原长3327]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:27）

The shell is mangling Chinese encoding. Let me use Python with unicode escapes to control encoding properly.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

Python is at /c/Users/UserX/AppData/Local/Programs/Python/Python312/python.exe but the path has Chinese chars and isn't in the msys path directly (the PATH entry uses Chinese). Let me try invoking it. Path: "/c/Users/UserX/AppData/Local/Programs/Python/Python312/python.exe". But typing UserX in the command will get mangled too, potentially. Hmm. Could use a glob: /c/Users/*/AppData/Local/Programs/Python/Python312/python.exe — but multiple users (UserX, UserX). Actually use `ls /c/Users/UserX/...` problematic.

Alternative: Node.js is available (/c/Program Files/nodejs). Node can do HTTP requests and print UTF-8. I can use node -e with unicode escapes in JS (\u5317). That avoids Chinese literal encoding issues entirely in the source (JS parses \u escapes). Node output to stdout: write UTF-8 buffer.

Node's https module available. Let's use node.

Let me test node version and a fetch.

Build a node script:
const https=require('https');
function get(url){return new Promise(...)}
const queries = ['\u5317\u4eac\u5e02\u519c\u673a\u603b\u52a8\u529b \u7efc\u5408\u673a\u68b0\u5316\u7387', ...];
Use encodeURIComponent to build URL. Fetch cn.bing.com/search?q=...&format=rss. Parse with regex for <item> title/link/description. Print.

Node -e with a long script and Chinese via \u escapes. Regex handling. Let me write it carefully.

Actually the RSS encoding: Bing RSS likely contains Chinese in UTF-8. We collect chunks as Buffer, concatenate, toString('utf8'). Good. Then print with process.stdout.write.

Let me write the command. It's long; use single quotes around the -e script to avoid shell interpretation. Inside use double quotes for JS strings. \u escapes preserved (shell single quotes don't interpret backslashes). Good.

Let me do it.

Queries (unicode escapes):
1. 北京市农机总动力 综合机械化率
北京 \u5317\u4eac 市 \u5e02 农 \u519c 机 \u673a 总 \u603b 动 \u52a8 力 \u529b
市 = \u5e02
农 = \u519c
机 = \u673a
总 = \u603b
动 = \u52a8
力 = \u529b
综合机械化率: 综 \u7efc 合 \u5408 机 \u673a 械 \u68b0 化 \u5316 率 \u7387

2. 北京 农业生产托管 一条龙 农机作业
农 \u519c 业 \u4e1a 生 \u751f 产 \u4ea7 托 \u6258 管 \u7ba1
一 \u4e00 条 \u6761 龙 \u9f99
作 \u4f5c 业 \u4e1a

3. 北京鑫利农机服务专业合作社
鑫 \u946b 利 \u5229 服 \u670d 务 \u52a1 专 \u4e13 业 \u4e1a 合 \u5408 作 \u4f5c 社 \u793e

4. 北京兴农天力农机服务专业合作社
兴 \u5174 农 \u519c 天 \u5929 力 \u529b

5. 北京市农机购置补贴 2024
购 \u8d2d 置 \u7f6e 补 \u8865 贴 \u8d34

6. 北京 秸秆综合利用 政策
秸 \u79f8 秆 \u79c6 综 \u7efc 合 \u5408 利 \u5229 用 \u7528 政 \u653f 策 \u7b56

7. 农机合作社 机手老龄化 问题
手 \u624b 老 \u8001 龄 \u9f84 化 \u5316 问 \u95ee 题 \u9898

8. 北京市 主要农作物 耕种收综合机械化率
耕 \u8015 种 \u79cd 收 \u6536

Let me just run batch 1 with 4 queries. Node script loops queries, fetches sequentially, prints.

Let me write generic code that takes queries array. Use \u escapes.

I'll do it now.

</details>

- 🔧 **Bash** `{"command": "node -e '\nconst https=require(\"https\");\nconst qs=[\"\\u5317\\u4eac\\u5e02\\u519c\\u673a\\u603b\\u52a8\\u529b \\u7efc\\u5408\\u673a\\u68b0\\u5316\\u7387\",\"\\u5317\\u4eac \\u519c\\u4e1a\\u751f\\u4ea7\\u6258\\u7ba1 \\u4e00\\u6761\\u9f99 \\u519c\\u673a\\u4f5c\\u4e1a\",\"\\u5317\\u4eac\\u946b\\u5229\\u519c\\u673a\\u670d\\u52a1\\u4e13\\u4e1a\\u5408\\u4f5c\\u793e\", …[截断,原长413]` → `===QUERY: 北京市农机总动力 综合机械化率 === - 北京市_百度百科 https://baike.baidu.com/item/%e5%8c%97%e4%ba%ac%e5%b8%82/126069 截至2025年末，北京市常住人口2180.0万人。 北京市地处中国北部、华北平原北部，东与天津市毗连，其余均与河北省相邻，中心位于东经116°20′、北纬39°56′，北京市地势西北高、东南低。 西部、北部和东北部三面环山，东南部是一片缓缓向渤海倾斜的平原。 - Beijing - 北京市人民政府门户网站 https://www.beijing.gov.cn/ 北京市人民政府门户网站——首都之窗（www.beijing.gov …[截断,原长9772]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:27）

Node.js is available and handles UTF-8 well. Let me use it with unicode escapes.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

Each query returns the exact same generic results regardless of query — Bing is clearly serving a cached/generic page to this bot/UA, not real search results. The URL-encoding is correct now (encodeURIComponent produced proper UTF-8). But Bing returns generic "北京" results. So Bing search via this method is useless.

Alternative search engines that work with curl:
- DuckDuckGo html (timed out via WebFetch, but curl might work). Try https://html.duckduckgo.com/html/?q=...
- Baidu (WebFetch blank; curl might work but Baidu requires JS/cookies)
- so.com (360搜索) https://www.so.com/s?q=
- search.brave.com
- startpage
- ecosia
- mojeek
- Marginalia
- Google (likely blocked in China? The machine has HZVPN path, maybe VPN available). Try google.com/search.

Let me try several with curl in parallel and check which returns real results. Note: the results should differ per query; I'll test with distinct queries.

Let me test DuckDuckGo lite/html, 360, Google, Brave, Mojeek.

Let me run a bash loop with curl for a Chinese query and grep for result titles. But Chinese literal query gets GBK-mangled by shell. Use node to do the requests for each engine. Better: use node with encodeURIComponent.

Let me write node script fetching multiple engines for one query and printing first 1500 chars or detected titles.

Engines:
- https://html.duckduckgo.com/html/?q=QUERY
- https://www.so.com/s?q=QUERY
- https://www.google.com/search?q=QUERY&num=20
- https://search.brave.com/search?q=QUERY
- https://www.mojeek.com/search?q=QUERY
- https://lite.duckduckgo.com/lite/?q=QUERY
- https://www.ecosia.org/search?q=QUERY
- https://search.marginalia.nu/search?query=QUERY

Let me test with query "北京市农机总动力" and print length + whether contains keyword.

Node https with gzip? Some engines return br/gzip. Node's https doesn't auto-decompress. Add Accept-Encoding: identity to get plain. Some may still return gzip. Let me set "Accept-Encoding":"identity".

Let me write script.

</details>

- 🔧 **Bash** `{"command": "node -e '\nconst https=require(\"https\");\nconst q=\"\\u5317\\u4eac\\u5e02\\u519c\\u673a\\u603b\\u52a8\\u529b\";\nconst engines=[\n [\"ddg-html\",\"https://html.duckduckgo.com/html/?q=\"+encodeURIComponent(q)],\n [\"ddg-lite\",\"https://lite.duckduckgo.com/lite/?q=\"+encodeURIComponent(q)],\n [\"so360\",\"https://www.so.com/s?q=\"+encodeURIComponent(q)],\n [\"goog …[截断,原长413]` → `ddg-html status=TIMEOUT len=0 hasKeyword=false title=none ddg-lite status=TIMEOUT len=0 hasKeyword=false title=none so360 status=200 len=378287 hasKeyword=true title=北京市农机总动力_360搜索 google status=TIMEOUT len=0 hasKeyword=false title=none brave status=TIMEOUT len=0 hasKeyword=false title=none mojeek status=403 len=329 ha …[截断,原长355]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:27）

Bing is serving generic cached pages. Let me test which alternative search engines return real results via Node.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

360搜索 (so.com) works and returns 378KB with keyword. Let me parse 360 search results. 360 result HTML structure: titles in `<h3 class="res-title...">` with `<a ... href="...">`. Let me extract links and titles.

Let me write a parser that extracts result titles and URLs. 360 search result anchors: `<a ... data-mdurl=...` or `href="http://www.so.com/link?m=..."`. The actual URL may be in `<a ... href="http://www.so.com/link?...">` with title text, plus `data-url` maybe. Let me inspect a snippet.

Let me fetch and grep for patterns. I'll print segments around "res-title" or list all hrefs with text.

Let me just dump structure: search for `class="res-list"` or `<h3`. Let me print the first occurrence context.

I'll run node and extract regex matches of `<a[^>]*href="([^"]+)"[^>]*>([\s\S]{0,200}?)</a>` filtering those containing text. Actually 360 uses `<h3 class="res-title "><a href="..." ...>title</a></h3>`. Let me extract `<h3[^>]*>[\s\S]*?<a[^>]*href="([^"]+)"[^>]*>([\s\S]*?)</a>`.

Also need the real target URL. 360 sometimes includes `data-url` attribute on the h3 anchor like `<a href="http://www.so.com/link?m=..." data-url="http://real...">`. Let me capture all attributes.

Let me fetch one query and print the first 5 h3 blocks raw (limited length).

</details>

- 🔧 **Bash** `{"command": "node -e '\nconst https=require(\"https\");\nconst q=\"\\u5317\\u4eac\\u5e02\\u519c\\u673a\\u603b\\u52a8\\u529b\";\nfunction get(url){return new Promise((res)=>{const req=https.get(url,{headers:{\"User-Agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36\",\"Accept-Language\":\"zh-CN,zh;q=0.9\",\"A …[截断,原长412]` → `idx res-list=178416 umentElement.clientHeight:e=document.body.clientHeight>document.documentElement.clientHeight?document.body.clientHeight:document.documentElement.clientHeight,e}}</script><ul class="result"><li class="res-list"><h3 class="res-title"><a href="https://www.so.com/link?m=z%2B5ABIVKn2xff1guKFaY%2BCx7MFVcC …[截断,原长2657]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:28）

360 search works. Let me inspect its result structure and parse it.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

360 search returns real results with `data-mdurl` containing the real URL, and title text. I can parse `<h3 ... class="res-title"...>...<a ... data-mdurl="REALURL" ...>TITLE</a></h3>` and description in `res-desc` or `res-list-summary`.

Let me write a reusable parser and run multiple queries. I'll extract:
- title: text inside <a ...>TITLE</a> (strip <em>)
- url: data-mdurl
- desc: from <p class="res-desc">...</p> or res-list-summary

Let me create the node script for a batch of queries. To keep it efficient, run multiple queries in one node invocation.

Queries batch A (general data):
1. 北京市农机总动力 综合机械化率
2. 北京 主要农作物 耕种收综合机械化率
3. 北京市 农机社会化服务组织 数量
4. 北京 农业生产托管 服务面积

Batch B (model):
5. 农业生产托管 一条龙 保姆式 菜单式 农机
6. 山东 农业生产托管 案例 面积
7. 黑龙江 农业生产托管 案例

Batch C (cooperatives):
8. 北京鑫利农机服务专业合作社
9. 北京兴农天力农机服务专业合作社
10. 北京绿谷汇德 农机
11. 顺义 农机合作社

Batch D (policy):
12. 北京市 农机购置与应用补贴 实施方案
13. 北京市 秸秆综合利用 政策
14. 北京 深松整地 补贴

Batch E (problems):
15. 农机合作社 问题 机手老龄化 装备利用率

Let me run in a couple of node calls. Output could be long; limit to top 6 results each with 200-char desc.

Let me write the parser carefully. Regex for result blocks: split on `<li class="res-list` and also maybe other classes. Simpler: global regex on `<h3[^>]*class="res-title[^"]*"[^>]*>([\s\S]*?)<\/h3>`. Within, find data-mdurl and anchor text. Then find following description using res-desc or res-list-summary within next 2000 chars.

Let me implement:
const re=/<h3[^>]*class="res-title[^"]*"[^>]*>([\s\S]*?)<\/h3>/g;
for each match, block = match[1]; url = /data-mdurl="([^"]*)"/. title = strip tags from block.
desc: take substring of body after match.index up to 1500 chars, find /<p class="res-desc">([\s\S]*?)<\/p>/ or res-list-summary.

Let me code and run 5 queries.

Also, I should be careful: 360 may rate-limit after many rapid queries. Add small delay. Let's do 5 per call with 1s delay.

Let me go.

</details>

- 🔧 **Bash** `{"command": "node -e '\nconst https=require(\"https\");\nconst qs=[\n \"\\u5317\\u4eac\\u5e02\\u519c\\u673a\\u603b\\u52a8\\u529b \\u7efc\\u5408\\u673a\\u68b0\\u5316\\u7387\",\n \"\\u5317\\u4eac \\u4e3b\\u8981\\u519c\\u4f5c\\u7269 \\u8015\\u79cd\\u6536\\u7efc\\u5408\\u673a\\u68b0\\u5316\\u7387\",\n \"\\u5317\\u4eac\\u5e02 \\u519c\\u673a\\u793e\\u4f1a\\u5316\\u670d\\u52a1\\u7ec4\ …[截断,原长413]` → `===== 北京市农机总动力 综合机械化率 ===== - 中国 农业:农业机械总动力:北京|农业机械化数据集|农业统计数据集 URL: https://www.selectdataset.com/dataset/6151784539ee95dfef6e371780b2f673 - 北京市农业机械总动力_历年数据_聚汇数据 URL: https://www.gotohui.com/ndata/show-93851 下载数据未来预测数据注:农业机械总动力指全部农业机械动力的额定功率之和。农业机械是指用于种植业、畜牧业、渔业、农产品初加工、农用运输和农田基本建设等活动的机械及... - 2010-2019年北京拖拉机数量、拖拉机配套农具 …[截断,原长5684]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:28）

360 gives real results with `data-mdurl`. Let me build a parser and run the research queries.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

360 works well. Now let me search cooperatives and policies. Let me run batch.

Also I found a good source: 河北 6种农业生产托管服务模式 (含全产业链托管、菜单式多环节托管) - good for definition. And 黄龙县 保姆式托管 菜单式服务.

Let me now query cooperatives and policies, plus national production trusteeship data (Shandong, Heilongjiang).

Batch:
6. 北京鑫利农机服务专业合作社 顺义
7. 北京兴农天力农机服务专业合作社
8. 北京绿谷汇德 农机 平谷
9. 顺义 农机合作社
10. 北京市 农机购置与应用补贴 实施方案 2024

Then:
11. 北京市 秸秆综合利用 政策 2024
12. 北京 深松整地 补贴
13. 山东 农业生产托管 案例 面积
14. 黑龙江 农业生产托管 案例 面积
15. 农机合作社 问题 机手老龄化

Let me run two batches.

I should also try to fetch the actual authoritative pages later and verify. But first gather candidate sources.

Let me run batch of 5.

</details>

- 🔧 **Bash** `{"command": "node -e '\nconst https=require(\"https\");\nconst qs=[\n \"\\u5317\\u4eac\\u946b\\u5229\\u519c\\u673a\\u670d\\u52a1\\u4e13\\u4e1a\\u5408\\u4f5c\\u793e\",\n \"\\u5317\\u4eac\\u5174\\u519c\\u5929\\u529b\\u519c\\u673a\\u670d\\u52a1\\u4e13\\u4e1a\\u5408\\u4f5c\\u793e\",\n \"\\u5317\\u4eac\\u7eff\\u8c37\\u6c47\\u5fb7 \\u519c\\u673a\",\n \"\\u987a\\u4e49 \\u519c\\u673a\\ …[截断,原长413]` → `===== 北京鑫利农机服务专业合作社 ===== - 北京市鑫利农机服务专业合作社 - 爱企查 URL: https://aiqicha.baidu.com/company_detail_29353302435930 爱企查为您提供北京市鑫利农机服务专业合作社的企业信息查询服务,查询北京市鑫利农机服务专业合作社工商注册信息、电话邮箱、公司地址、经营风险、控股持股、发展动态、财务状况、股东法人高管... - 北京市鑫利农机服务专业合作社_360百科 URL: 北京市鑫利农机服务专业合作社，2008年12月19日成立，经营范围包括等。 详情&gt;&gt; - 北京市鑫利农机服务专业合作社 - 企查查 URL: https://www …[截断,原长5072]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:28）

Good progress. Now let me search the cooperative cases and policies.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

Good. Now I have solid leads. Let me update todos and continue researching: straw policy, deep loosening subsidy, Shandong/Heilongjiang trusteeship data, and cooperative problems. Then fetch key authoritative pages to verify specific data.

Let me run next batch of 360 queries, and also fetch the Beijing beijing.gov.cn subsidy page and nyncj pages.

Let me do the 360 batch first.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "Research Beijing agricultural mechanization overall data", "priority": "high", "status": "in_progress"}, {"content": "Research 'one-stop' farm machinery trusteeship model", "priority": "high", "status": "in_progress"}, {"content": "Research specific Beijing cooperative cases", "priority": "high", "status": "in_progress"}, {"content": "Research Beijing su …[截断,原长412]` → `{"oldTodos":[{"content":"Research Beijing agricultural mechanization overall data","status":"in_progress","priority":"high"},{"content":"Research 'one-stop' farm machinery trusteeship model","status":"pending","priority":"high"},{"content":"Research specific Beijing cooperative cases","status":"pending","priority":"hig …[截断,原长1220]`

- 🔧 **Bash** `{"command": "node -e '\nconst https=require(\"https\");\nconst qs=[\n \"\\u5317\\u4eac\\u5e02 \\u79f8\\u79c6\\u7efc\\u5408\\u5229\\u7528 \\u653f\\u7b56\",\n \"\\u5317\\u4eac \\u6df1\\u677e\\u6574\\u5730 \\u8865\\u8d34\",\n \"\\u5c71\\u4e1c \\u519c\\u4e1a\\u751f\\u4ea7\\u6258\\u7ba1 \\u6848\\u4f8b \\u9762\\u79ef\",\n \"\\u9ed1\\u9f99\\u6c5f \\u519c\\u4e1a\\u751f\\u4ea7\\u6258\\u …[截断,原长412]` → `===== 北京市 秸秆综合利用 政策 ===== - 关于《2026年度昌平区农作物秸秆综合 利用重点区实施方案》的政策解读 URL: https://www.bjchp.gov.cn/cpqzf/xxgk2671/cpqzcjd/2026070810194379396/index.html 2026年6月30日 - 北京市昌平区农业农村局 北京市昌平区农业服务中心关于印发《2026年度昌平区农作物秸秆综合利用重点区实施方案》的通知近日,北京市昌平区农业农村局、... - 关于对《2026年度昌平区农作物秸秆综合利用重点区实施方案(征求意见稿)》公开征集意见的反馈_区级反馈信息_首都之窗_北京市人民政府门户网站 URL: http …[截断,原长5307]`

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

I now have many leads. Now I need to verify specific facts by fetching authoritative pages. Key ones:

1. Beijing mechanization data: Search didn't yield specific latest Beijing figures. Let me try more targeted queries: "北京市 农作物耕种收综合机械化率 97%" or "北京 农业机械化 十四五". Also 北京市农机化统计公报. Let me search "北京 农业机械化 综合机械化率 2024" and "北京市 农机 十四五 规划".

2. Cooperative details: I need service area, equipment scale, honors. Let me search more:
- "鑫利农机 合作社 服务面积 装备"
- "鑫利农机 金跃 全国农机合作社示范社"
- "兴农天力 陈领 合作社 服务面积"
Also 北京市 国家级农机合作社示范社 名单.

3. Straw: Beijing straw comprehensive utilization rate 99%+ (人民政协网 2024). Good. Need official policy: 北京市 秸秆综合利用 实施方案. Search.

4. Deep loosening subsidy: Beijing-specific. Search "北京 农机深松 作业 补贴 北京" maybe 农业农村局. Might not exist in Beijing (deep loosening mainly northern dryland). Let me search "北京市 深松整地" more specifically.

5. 一条龙托管 definition: 河北6种模式 page, plus 农业农村部 农业生产托管服务规范. Let me fetch the 河北新闻网 page and maybe the agri.cn page.

Let me now fetch authoritative pages via WebFetch/node. Since WebFetch works for direct URLs, I'll use it for reading content. But Chinese pages via WebFetch should be fine (it fetches and converts).

I'll batch WebFetch calls:
A. https://www.beijing.gov.cn/zhengce/zhengcefagui/202503/t20250325_4044054.html - subsidy plan
B. https://nyncj.beijing.gov.cn/nyj/zwgk/zcjd84/543511218/index.html - policy interpretation
C. https://www.rmzxb.com.cn/c/2024-04-10/3522875.shtml - straw utilization 99%
D. https://hebei.hebnews.cn/2020-04/28/content_7816065.htm - 6 trusteeship models

But also need Beijing mechanization specifics. Let me do another 360 search batch first for those specifics, then fetch pages.

Let me run 360 search:
- 北京市 农业机械化 综合机械化率
- 北京 农机合作社 示范社 名单
- 鑫利农机 合作社 服务面积 金跃
- 兴农天力 陈领 合作社
- 北京市 秸秆综合利用 实施方案 农业农村局

Let me run.

</details>

- 🔧 **Bash** `{"command": "node -e '\nconst https=require(\"https\");\nconst qs=[\n \"\\u5317\\u4eac\\u5e02 \\u519c\\u4e1a\\u673a\\u68b0\\u5316 \\u7efc\\u5408\\u673a\\u68b0\\u5316\\u7387 2024\",\n \"\\u5317\\u4eac \\u519c\\u673a\\u5408\\u4f5c\\u793e \\u793a\\u8303\\u793e \\u540d\\u5355\",\n \"\\u946b\\u5229\\u519c\\u673a \\u91d1\\u8dc3 \\u670d\\u52a1\\u9762\\u79ef\",\n \"\\u5174\\u519c\\u592 …[截断,原长413]` → `===== 北京市 农业机械化 综合机械化率 2024 ===== - 2024年全国农业机械化发展统计公报 URL: https://njhs.moa.gov.cn/nyjxhqk/202511/t20251120_6479055.htm 紧抓重要农时机械化生产,强化大面积单产提升机械化支撑,全产业全链条协同推进农机装备补短板行动,坚持以用促研发、以用促制造、以用促转化,... - 北京市农林科学院信息技术研究中心 URL: http://www.nercita.org.cn/infos/detail?id=10820&type=206 2026年5月2日 - 张钟莉莉说,目前北京地区大田粮食作物的综合机械化率已经超过90%,但设 …[截断,原长5891]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:29）

Let me dig deeper on Beijing-specific figures, cooperative details, and straw policy.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

Good leads. Now let me fetch key authoritative pages to verify specifics:

1. Beijing subsidy plan: https://www.beijing.gov.cn/zhengce/zhengcefagui/202503/t20250325_4044054.html
2. Straw: 人民政协网 https://www.rmzxb.com.cn/c/2024-04-10/3522875.shtml ; 大兴区秸秆方案 https://www.bjdx.gov.cn/bjsdxqrmzf/zwfw/zfwj67/1380045/2032853/index.html
3. 河北 6种托管模式: https://hebei.hebnews.cn/2020-04/28/content_7816065.htm
4. Beijing mechanization: nercita article http://www.nercita.org.cn/infos/detail?id=10820&type=206 ; also search 北京市农机化 "十四五" or 北京市 农业机械化发展 报告.
5. Cooperative honors: 2017 全国农机合作社示范社 (鑫利), 2013/2016 (兴农天力).

Let me also search for Beijing 农机合作社数量/社会化服务组织数量 and 托管服务面积. Try queries:
- 北京 农业生产托管 项目 实施方案 2024
- 北京市 农业社会化服务 面积
- 北京 农机服务组织 数量 家

Also "北京市 十四五 农业机械化 规划" might have 2025 target mechanization rate.

Let me fetch several pages in parallel with WebFetch, and meanwhile run another 360 search batch.

Actually WebFetch fetches and answers. Let me use WebFetch for content extraction. I'll do 4-5 parallel.

Let me fetch:
- subsidy plan
- 河北 6 models
- straw 人民政协网
- 大兴秸秆方案
- nercita mechanization

And run 360 search batch for Beijing 托管/社会化服务数量 + 深松.

I can do WebFetch and Bash in same block? Yes, parallel tool calls allowed. Let me do that.

</details>

- 🔧 **WebFetch** `{"prompt": "Extract the exact details of this policy: implementing agency, document number, subsidy scope (补贴机具种类), subsidy rates/amounts (补贴标准/比例), whether it mentions 农机作业托管/社会化服务, 报废更新, and any quantified targets. Quote key sentences.", "url": "https://www.beijing.gov.cn/zhengce/zhengcefagui/202503/t20250325_4044054.html"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List the 6 types of agricultural production trusteeship service models (农业生产托管服务模式) described, with their definitions and any data on number of service organizations or service area in Hebei. Quote key sentences.", "url": "https://hebei.hebnews.cn/2020-04/28/content_7816065.htm"}` → `河北推广的6种农业生产托管服务模式如下： 1. **全产业链托管**：服务组织与农户签约，承担供、耕、种、防、收、销全程；农资等由组织承担，土地收益归农户，组织收取农资和作业等服务费，即“保姆式托管”，让农户“省心、省力、省钱”。 2. **菜单式多环节托管**：组织提供多环节套餐或单项服务，农户按自有工具、机械、劳力自愿选择托管环节或项目；易推广复制，但“利益联结稳定性相对较差”。 3. **土地股份合作分红**：农户保留承包经营权，由村级组织协调，以“土地入股+保底分红”方式入股托管组织，收益后按股分红，体现“利益共享、风险共担”。 4. **股份托管并行**：尊重农户意愿，股份合作与托管服务并行，“宜股则股、宜托则托”，兼顾两 …[截断,原长680]`

- 🔧 **WebFetch** `{"prompt": "Extract facts about Beijing straw comprehensive utilization: the utilization rate, year, policy basis, and any data on straw amount or treatment methods. Quote key sentences and note the publishing date and source.", "url": "https://www.rmzxb.com.cn/c/2024-04-10/3522875.shtml"}` → `REDIRECT DETECTED: The URL redirects to a different host. Original URL: https://www.rmzxb.com.cn/c/2024-04-10/3522875.shtml Redirect URL: https://www.rmzxw.com.cn/c/2024-04-10/3522875.shtml Status: 301 Moved Permanently To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again …[截断,原长631]`

- 🔧 **WebFetch** `{"prompt": "Extract the main content of this Daxing District straw comprehensive utilization action plan (2023-2025): targets, utilization rate, treatment methods (还田/离田/肥料化/饲料化/能源化), subsidy or policy measures, and responsible agencies. Quote key sentences.", "url": "https://www.bjdx.gov.cn/bjsdxqrmzf/zwfw/zfwj67/1380045/2032853/index.html"}` → `该网页仅为印发通知和附件目录，未展示方案正文，因此无法从现有内容中提取具体目标、利用率、还田/离田等技术方式、补贴标准或具体责任分工。 可确认信息如下： - 文件名称：《北京市大兴区秸秆类废弃物综合利用行动方案（2023-2025年）》 - 发文单位：“北京市大兴区农业农村局” - 文号：“京兴政农发〔2023〕29号” - 成文/发布日期：2023-04-19 / 2023-04-23；状态：“现行有效” - 印发对象：“各镇人民政府、区直相关单位” - 通知目的：“深入实施乡村振兴战略，推进绿色都市田园建设”；要求“请遵照执行” - 方案分节链接包括：“一、秸秆类废弃物利用现状”“二、发展思路与目标”“三、主要任务”“四、重点支 …[截断,原长399]`

- 🔧 **Bash** `{"command": "node -e '\nconst https=require(\"https\");\nconst qs=[\n \"\\u5317\\u4eac \\u519c\\u4e1a\\u751f\\u4ea7\\u6258\\u7ba1 \\u9879\\u76ee \\u5b9e\\u65bd\\u65b9\\u6848 \\u9762\\u79ef\",\n \"\\u5317\\u4eac \\u519c\\u4e1a\\u793e\\u4f1a\\u5316\\u670d\\u52a1 \\u9762\\u79ef \\u670d\\u52a1\\u7ec4\\u7ec7\",\n \"\\u5317\\u4eac\\u5e02 \\u6df1\\u677e\\u6574\\u5730 \\u4f5c\\u4e1a \\ …[截断,原长413]` → `===== 北京 农业生产托管 项目 实施方案 面积 ===== - 农业生产托管项目组织实施方案-20260510.docx - 人人文库 URL: https://www.renrendoc.com/paper/521811600.html (三)主要目标通过本项目的实施,力争在项目周期内,培育一批具备较强服务能力的农业生产托管服务组织;在主要粮食作物及特色经济作物上推广一定规模的托管服务面积;... - 农业生产托管试点项目方案- 360文库 URL: 农业生产托管试点项目方案1.项目背景与目标大力发展农业生产托管试点项目，是为了提高农业生产效益、推动农业现代化、促进农业产业融合发展、增加农民收入。本项... - 农业托管中心 …[截断,原长4531]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:29）

Now let me fetch key authoritative pages and search remaining gaps in parallel.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

Excellent find: 《北京市农业机械化提升行动实施方案(2023-2025年)》 - this is key for Beijing mechanization targets. URL: http://www.mei.net.cn/nyjx/202302/1676614067.html. Let me fetch it. Also the 北京市人大 report.

Also 北京农机深松整地有补贴 (2015) - 30万亩, 50元/亩. Need latest Beijing policy though. Let me search for latest 北京 深松 补贴. Also maybe 北京市 耕地地力保护补贴.

Let me now fetch key pages:
1. 北京市农业机械化提升行动实施方案(2023-2025年) - mei.net.cn
2. 北京市人大常委会 十四五 指标 - bjrd.gov.cn
3. nercita article on mechanization rate
4. straw redirect rmzxw.com.cn
5. subsidy policy - failed extraction; try again or fetch nyncj interpretation page.

Let me also try fetching nyncj.beijing.gov.cn interpretation.

Note WebFetch might fail on some. Let me try more.

Also I should get Beijing 农机总动力 latest. Try 北京市统计年鉴 or 北京市 2024 国民经济和社会发展统计公报 (may include 农机总动力). Search "北京市 2024年国民经济和社会发展统计公报 农业机械总动力". Also 中国农业机械化年鉴.

Let me batch:
WebFetch:
- http://www.mei.net.cn/nyjx/202302/1676614067.html
- https://www.bjrd.gov.cn/zyfb/zt/14jqgrd03chybjdbthdztbd/bgjd/202503/t20250306_4026895.html
- https://www.rmzxw.com.cn/c/2024-04-10/3522875.shtml
- https://nyncj.beijing.gov.cn/nyj/zwgk/zcjd84/543511218/index.html

And Bash 360 search:
- 北京市 2024年国民经济和社会发展统计公报 农业机械总动力
- 北京 农机总动力 万千瓦 2023
- 北京市 农业机械化提升行动实施方案 2023-2025 主要内容
- 北京 农机合作社 数量 家 京郊

Let me do it.

</details>

- 🔧 **WebFetch** `{"prompt": "Extract the main targets, tasks and quantified indicators of 《北京市农业机械化提升行动实施方案(2023-2025年)》: 农机总动力, 耕种收综合机械化率, 设施农业机械化率, socialized service organizations, trusteeship, subsidy measures. Quote key sentences with numbers.", "url": "http://www.mei.net.cn/nyjx/202302/1676614067.html"}` → `根据方案，2025年主要量化目标包括： - 动力：“将全市农机总动力稳定在120万千瓦左右” - 种植业：“全市农作物耕种收综合机械化率达到75%以上” - 设施农业：“设施农业机械化率达到55%以上” - 畜牧：“畜牧养殖机械化率达到85%以上” - 水产：“水产养殖机械化率达到50%以上” - 初加工：“农产品初加工机械化率达到50%以上” - 秸秆：“农作物秸秆基本实现全量化综合利用” - 2035年：“全市主要农作物生产实现全过程机械化，农业生产各领域基本`

- 🔧 **WebFetch** `{"prompt": "Extract any data on Beijing agricultural mechanization rate (农作物耕种收综合机械化率) or 农机 indicators mentioned, and whether the 十四五 target was met. Quote key sentences.", "url": "https://www.bjrd.gov.cn/zyfb/zt/14jqgrd03chybjdbthdztbd/bgjd/202503/t20250306_4026895.html"}` → `No Beijing-specific agricultural mechanization rate or 农机 indicator appears in the page. National data mentioned: - Target: “到2025年，农作物耕种收综合机械化率达到75%。” - Status: “据农业农村部统计，这一比率提前一年完成。” - Related: “我国三大主粮基本实现全程机械化”，乡村农机从业人员近5000万人，植保无人机保有量超过25万架。 The local example cited is 辽宁大连普兰店区战家村, not Beijing.`

- 🔧 **WebFetch** `{"prompt": "Extract facts about Beijing straw comprehensive utilization: the utilization rate, year, policy basis, and any data on straw amount or treatment methods. Quote key sentences and note the publishing date and source.", "url": "https://www.rmzxw.com.cn/c/2024-04-10/3522875.shtml"}` → `页面标注发布时间为“2024年04月10日 14:06”，来源为“农民日报”，作者为“赵博文”，刊载于人民政协网。 - 利用率：北京“秸秆利用率保持稳定在99%以上”；文章未给出99%对应的具体统计年份，仅称“近年来”。 - 政策依据：以“实施中央秸秆项目为抓手”，并形成“以肥料化为主，秸秆饲料化、基料化、原料化、能源化等多元利用”的体系。 - 数量数据：昌平区“建成农业废弃物综合利用站10个，四年来共处理农业废弃物15.1万吨”，“基本实现农作物秸秆、蔬菜尾菜全量化利用”。 - 处理方式：包括“秸秆直接还田、离田肥料化、基料化、原料化”等，以及“制作生物有机肥、土壤调理剂、生物覆盖材料等多元利用方式”。`

- 🔧 **WebFetch** `{"prompt": "Extract the key points of the policy interpretation for Beijing farm machinery purchase and application subsidy 2024-2026: subsidy objects, machinery types, subsidy standards, application process, and any mention of 社会化服务/托管. Quote key sentences.", "url": "https://nyncj.beijing.gov.cn/nyj/zwgk/zcjd84/543511218/index.html"}` → `**补贴对象**：覆盖从事农业生产的农民及各类农业生产经营组织，后者含集体经济组织、合作社、企业等。原文：“补贴对象为从事农业生产的农民和农业生产经营组织”。 **机具范围**：分中央与市级两套范围。中央部分“有20大类35个小类75个品目”；市级单独部分“有8大类16小类50个品目”。另有重点机具：“选择10个品目且不超过20个档次作为‘重点机具’”。 **补贴标准**：总体“有升有降”。中央补贴一般“按照不超过同档产品上年销售均价的30%测算”；部分重点机具“补贴标准测算比例提高到35%”；急需机具如移动式烘干机、履带式拖拉机等“补贴标准测算比例提高到40%”。市级单补一般“按照不超过同档产品上年销售均价的35%测算”。上限为： …[截断,原长530]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:30）

Found a key Beijing policy document. Let me fetch it and related sources.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

Good, Beijing mechanization figures from the 2023-2025 action plan:
- 农机总动力稳定在120万千瓦左右 (2025 target)
- 农作物耕种收综合机械化率达到75%以上 (2025 target)
- 设施农业机械化率55%以上
- 畜牧85%, 水产50%, 初加工50%
- 秸秆全量化综合利用

And nercita says 北京地区大田粮食作物综合机械化率已超过90%, 设施农业机械化仅50%左右 (2026-05 article? date looks odd). Need to verify.

Now need:
- 农机社会化服务组织数量 (Beijing) - likely not found; maybe 全市农机服务组织XX家. Let me search 北京 农机服务组织 数量 / 北京市农机合作社数量. Also 北京市 2024 统计年鉴.
- 托管服务面积 Beijing - likely not published; maybe 农业生产托管 in Beijing not common. Mark 未找到 if not found.

Cooperative specifics: need service area, equipment, honors. Sources:
- 鑫利: 2017全国农机合作社示范社; 2008-12-19成立; 顺义区; 法人金跃. Need service area. Search "鑫利农机合作社 作业面积" or fetch sohu 2017 list.
- 兴农天力: 2013 全国农机合作社示范社 (first batch), 2008/2009成立, 顺义区赵全营镇; 陈领 雷沃杯2012全国20佳理事长. Need service area and equipment. There's a page news.nongjigou.cn/n/201604/26/101185.html. Let me fetch.
- Also 北京市 全国农机合作社示范社名单 includes 北京河南寨农机服务专业合作社 (密云), 兴农天力. 

Let me fetch:
- http://news.nongjigou.cn/n/201604/26/101185.html (陈领 profile)
- http://www.nongji1688.com/news/201607/11/5508819.html (顺义 合作社转型)
- https://www.moa.gov.cn/xw/qg/202206/t20220624_6403247.htm (顺义鑫利 倒伏小麦)
- Maybe 360百科 pages (rendered? might not fetch well).

Also search for "北京 兴农天力 服务面积 亩" and "鑫利农机合作社 服务面积 亩", "绿谷汇德 农机 服务".

Let me also search Beijing 农机合作社数量 and 深松 latest.

Batch of searches + fetches in parallel.

Let me run 360 search for:
- 兴农天力农机合作社 作业面积 万亩
- 鑫利农机合作社 作业面积 万亩 顺义
- 北京 农机服务组织 合作社 数量 家
- 北京 深松整地 2023 补贴 实施方案
- 北京 小麦玉米 秸秆禁烧 综合利用

And fetch 陈领 article + 顺义转型 article.

Let me do it.

</details>

- 🔧 **WebFetch** `{"prompt": "Extract all facts about 北京兴农天力农机合作社 and its chairman 陈领: founding year, location, service area (亩/万亩), number of machines, members, business model (土地流转/托管/订单作业), honors. Quote key sentences.", "url": "http://news.nongjigou.cn/n/201604/26/101185.html"}` → ``

- 🔧 **WebFetch** `{"prompt": "Extract facts about Shunyi farm machinery cooperatives' transformation: names of cooperatives, service area, equipment counts, business model, straw/organic fertilizer operations, and challenges (麦田减少). Quote key sentences.", "url": "http://www.nongji1688.com/news/201607/11/5508819.html"}` → `根据网页内容： - 合作社名称：作业由“葛代子村鑫利农机服务专业合作社”实施，理事长为“金振启”。 - 作业地点/服务区域：可确认的作业地点是“北京市顺义区李遂镇魏辛庄村麦田”。 - 设备数量：现场有“2台大型联合收割机正紧张作业”；合作社转型中陆续购置“6台打捆机、30台拖拉机”。 - 秸秆与有机肥：现场“一部分小麦秸秆被粉碎成几厘米长的碎片，均匀地铺在田里，还有一部分秸秆被紧跟在后的秸秆打捆机打成捆等待回收。”合作社还“建起了有机肥生产厂”。 - 运作模式：“通过‘农户+农机合作社+养殖场+有机肥厂’的运作模式实现转型。” - 挑战与转型：因“北京的麦田逐渐减少，合作社的农机出现了‘吃不饱’的状况。”其重点转为“经营重点从种、收 …[截断,原长339]`

- 🔧 **WebFetch** `{"prompt": "Extract facts about 北京市鑫利农机服务合作社: its role in harvesting lodged wheat, number of harvesters dispatched, service area, and any data with dates. Quote key sentences.", "url": "https://www.moa.gov.cn/xw/qg/202206/t20220624_6403247.htm"}` → `- **角色**：在顺义区农业农村局、区农业技术综合服务中心调度下，北京市鑫利农机服务合作社提前购置、调集多功能谷物收割机，投入倒伏小麦抢收。原文：“北京市鑫利农机服务合作社提前购置、调集多台多功能谷物收割机”；效果为“让倒伏小麦也能被及时收获，保证颗粒归仓，减少农民损失”。 - **机具与方式**：该社调集的收割机“具有割台小、可调节、灵活度高等特点，可根据倒伏小麦长势分层对其进行收割”，并“能同步对秸秆进行粉碎还田”。 - **投入数量**：8台。原文：“目前，8台收割机正抢抓良好天气时机，对受灾倒伏小麦进行快速收割。” - **服务/作业区域**：在“李遂镇一处麦田”作业；全区倒伏“主要集中在受强对流天气影响较大的李遂镇及周边 …[截断,原长468]`

- 🔧 **Bash** `{"command": "node -e '\nconst https=require(\"https\");\nconst qs=[\n \"\\u5174\\u519c\\u5929\\u529b\\u519c\\u673a\\u5408\\u4f5c\\u793e \\u4f5c\\u4e1a\\u9762\\u79ef \\u4e07\\u4ea9\",\n \"\\u946b\\u5229\\u519c\\u673a\\u5408\\u4f5c\\u793e \\u4f5c\\u4e1a\\u9762\\u79ef \\u4e07\\u4ea9 \\u987a\\u4e49\",\n \"\\u5317\\u4eac \\u519c\\u673a\\u670d\\u52a1\\u7ec4\\u7ec7 \\u5408\\u4f5c\\u79 …[截断,原长413]` → `===== 兴农天力农机合作社 作业面积 万亩 ===== - 【新闻播报】蓬勃发展的顺义农民专业合作社——北京兴农天力农机服务专业合作社_农业 URL: https://www.sohu.com/a/463793839_121106842 北京兴农天力农机服务专业合作社成立于2008年,位于顺义区赵全营镇,现有社员365户,流转土地1.2万亩,农机资产3000余万.2012年,北京市政府在顺义... - 【新春走基层】一个乡镇打造的三种现代农业模式--中国供销合作网 URL: https://www.chinacoop.gov.cn/news.html?aid=1769549 在赵全营镇上,有一家北京兴农天力农机服务专业合作社,可 …[截断,原长5148]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:31）

Let me get cooperative specifics and remaining Beijing policy data.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

Very useful. Key sources:
- 兴农天力: sohu 2021 article: 成立于2008年, 顺义区赵全营镇, 社员365户, 流转土地1.2万亩, 农机资产3000余万. And moa.gov.cn 2022: 280余台件, 技术人员近80人, 自有1.2万亩 + 托管/服务 other farmers. Let me fetch the moa article "农田托管服务,让顺义农民种地不操心!" http://www.moa.gov.cn/xw/qg/202207/t20220707_6404199.htm — this is highly relevant: 一条龙/托管 in Shunyi. Fetch it.
- 鑫利: 顺义区李遂镇柳各庄村; 2008-12-19成立; 法人金跃; 种了1万多亩小麦; 秸秆还田+深松+高性能播种.
- 秸秆: 北京20余万亩小麦, 秸秆利用率稳定在99%以上 (科普网/搜狐 2022). And 人民政协网 2024 99%+.
- 深松: 2015 Beijing plan 30万亩 50元/亩. Not latest. Beijing may no longer run deep loosening subsidy separately. Note.

Still missing:
- Beijing 农机总动力 actual latest value (target 120万千瓦). Could find in 北京统计年鉴 or 2024公报. Search "北京市 农业机械总动力 万千瓦 2022 2023".
- Beijing 农机社会化服务组织数量, 托管服务面积: maybe search "北京市 农业生产托管 服务组织 数量 2023" and "北京 农业社会化服务 面积 万亩". Might be scarce. There's a 北京市 农业社会化服务 项目 maybe. Also 北京市 2023 农业社会化服务项目. Let me search once more.
- 一条龙农机作业托管 definition source: moa article on Shunyi 农田托管 likely describes 全程托管 "一条龙". Good.
- 生产托管 vs 土地流转: There's a 163 article "不想种地、也不想撂荒?农业生产托管" explaining definition. Also 农业农村部 农业生产托管服务规范. Let me find official definition.
- National trusteeship cases: 山东 2.5亿亩次 (2024), 黑龙江 8039万亩次 / 全程托管650万亩, 2025目标6000万亩. Need source URLs; have sohu/qq. Could verify via 人民网/央广网. 黑龙江 2021 央广网: 全程托管面积超2000万亩.
- Problems: sohu 2019 "纾解农机合作社发展四大难题" and toutiao. Let me fetch sohu 2019 article for specifics.

Also cooperative 绿谷汇德: search found 北京绿谷汇德农业科技有限公司 (平谷, 2015) and 北京绿谷汇德果品产销专业合作社 (平谷刘家店镇, 2008). The user asked "北京绿谷汇德" — likely the果品合作社. Not necessarily a machinery coop. I'll report what's found and note no public data on machinery service.

Let me now fetch:
1. http://www.moa.gov.cn/xw/qg/202207/t20220707_6404199.htm (顺义农田托管)
2. https://www.sohu.com/a/463793839_121106842 (兴农天力 profile)
3. https://www.sohu.com/a/329322522_651395 (四大难题)
4. https://www.163.com/dy/article/EMUKS8F70511DJHA.html (生产托管定义 vs 流转)

And search:
- 北京市 农业机械总动力 万千瓦
- 农业生产托管 定义 农业农村部 规范 服务合同
- 北京 农业生产托管 服务组织 数量 万亩

Let me run.

</details>

- 🔧 **WebFetch** `{"prompt": "Extract all facts about 农田托管服务 in Shunyi: which cooperatives, what the trusteeship model is (全程托管/环节托管), service area, number of machines, service fees/prices, benefits to farmers, and any term like 一条龙. Quote key sentences with numbers.", "url": "http://www.moa.gov.cn/xw/qg/202207/t20220707_6404199.htm"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "Extract facts about 北京兴农天力农机服务专业合作社: founding year, location, members, land transferred (流转), machinery assets, equipment counts, service area, honors, business model. Quote key sentences with numbers.", "url": "https://www.sohu.com/a/463793839_121106842"}` → `**北京兴农天力农机服务专业合作社** - **成立与地点**：成立于2008年，位于顺义区赵全营镇。 - **成员与资产**：原文称，“现有社员365户，流转土地1.2万亩，农机资产3000余万。” - **设备数量**：文中未给出具体农机台/套数，仅有“农机资产3000余万”。 **土地流转与服务/经营规模** - 2012年参与顺义区赵全营镇都市型万亩示范区工程，“流转了赵全营镇8个村的6300亩土地进行统一种植”。 - 经营方式为“统一种植、统一管理、统一防控、统一收获、统一销售”。 - 2019年，“2019年总收入5000余万元，吸收劳动力335人”；并“带动了周边5000多农户增加收入”。 - 文中未另列独立“服务面积 …[截断,原长981]`

- 🔧 **WebFetch** `{"prompt": "Extract the four major problems (四大难题) facing farm machinery cooperatives described: e.g. 机手老龄化, 装备利用率低, 维修能力弱, 土地细碎化, 融资难, 价格竞争. Include any data, survey findings, or official statements. Quote key sentences.", "url": "https://www.sohu.com/a/329322522_651395"}` → `文章把主要困难概括为：“资金筹措难、不少补贴兑现难、人才队伍培养难、经济纯收入增加难”。 - **资金筹措难**：买机具、建库棚、垫付作业费、流转或托管土地都需资金；缺少抵押物，大型机具抵押普遍未落实，正规贷款不易。文中举例：某产粮大县数家较大合作社因担保方出问题，贷款落空，上千公顷流转费无法支付。 - **补贴兑现难**：除购机补贴外，其他环节补贴验收后常被拖延。文中称：“有的地方不仅当年不能得到兑现，甚至三年前实施的作业补贴，到现在还一直没有兑现。”金额上，“一般农机合作社涉及几十万元，有的达近百万元”。 - **人才队伍培养难**：机手老化、流动差、专项培训不足、作业水平不一，有的社甚至没人会用电子信箱，账目也不规范。原文称： …[截断,原长550]`

- 🔧 **WebFetch** `{"prompt": "Extract the definition of 农业生产托管, how it differs from 土地流转/土地经营权流转, what 全程托管 and 环节(半)托管 mean, and any official policy basis or data. Quote key sentences.", "url": "https://www.163.com/dy/article/EMUKS8F70511DJHA.html"}` → `根据页面内容： - **定义**：文中写：“农业生产托管 是农户等经营主体在不流转土地经营权的条件下，将农业生产中的耕、种、防、收等全部或部分作业环节委托给农业生产性服务组织完成的农业经营方式。” - **与土地流转/土地经营权流转的区别**：托管不转移土地经营权；《规范》要求“前提条件是不流转土地经营权，只提供生产环节服务”，并“把小农户作为政策支持的主要对象”。页面称土地流转曾是规模化路径之一，但遇卖难时“毁约成为流转主体和小农户经常面临的难题”，甚至“很多流转主体开始给农户退地”。 - **全程托管与环节托管**：规范区分“全程托管、单环节托管、多环节托管、关键环节托管等服务方式”。农户可把“耕、种、防、收、加”等作业“全部委 …[截断,原长554]`

- 🔧 **Bash** `{"command": "node -e '\nconst https=require(\"https\");\nconst qs=[\n \"\\u5317\\u4eac\\u5e02 \\u519c\\u4e1a\\u673a\\u68b0\\u603b\\u52a8\\u529b \\u4e07\\u5343\\u74e6\",\n \"\\u519c\\u4e1a\\u519c\\u6751\\u90e8 \\u519c\\u4e1a\\u751f\\u4ea7\\u6258\\u7ba1 \\u670d\\u52a1\\u89c4\\u8303 \\u5b9a\\u4e49\",\n \"\\u5317\\u4eac \\u519c\\u4e1a\\u751f\\u4ea7\\u6258\\u7ba1 \\u670d\\u52a1\\u7e …[截断,原长413]` → `===== 北京市 农业机械总动力 万千瓦 ===== - 【更新至2024年】1978-2024年各省市农业机械总动力(万千瓦)(无缺失)_2024年上海市渔业机械动力-CSDN博客 URL: https://blog.csdn.net/2201_75673146/article/details/156719461 2026年1月18日 - 订阅专栏1978-2024年各省市农业机械总动力(万千瓦)(无缺失).举报举报专栏目录1978-2024年各省市农业机械总动力(万千瓦)(无缺失)... - 浪漫崀山-新宁县人民政府 URL: http://www.xinning.gov.cn/xinning/nzhly/nlist_zhly …[截断,原长4668]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:31）

Let me fetch the Shunyi trusteeship article and cooperative problem source, and search remaining gaps.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

Excellent! Found:
- 怀柔区 2024-2025 智能农机装备...作业补贴: 卫星平地100元/亩、农机深松整地50元/亩、高质量小麦播种35元/亩、高质量玉米播种35元/亩、丘陵山区玉米收获80元/亩. URL: https://www.bjhr.gov.cn/zwgk/zcjd2024/202601/t20260104_4397541.html
- 北京市公共资源交易服务平台 2024: 农机深松整地作业每2年对同一地块补贴1次; 秸秆粉碎覆盖还田只补贴1次; 少免耕播种.
- 房山区: 深松50元/亩、秸秆粉碎覆盖还田35元/亩、少免耕播种35元/亩.

- 北京丰台 "田管家" 农业生产托管 (moa 2024-05): could be relevant Beijing trusteeship case. Let me fetch.
- 兴农天力 details good.
- 顺义农田托管 moa article failed extraction; retry.
- 合作社问题 source good.

Still need:
- Beijing 农机总动力 actual value (target 120万千瓦 from plan). Actual latest maybe in 中国统计年鉴. Could try selectdataset or 聚汇数据 gotohui. But those aren't authoritative. Maybe 北京市统计年鉴 2024. Hard to get exact via search. Let me try searching "北京 农业机械总动力 123.9万千瓦" etc. Or the CSDN dataset. Better: 中国农业农村信息网 or 北京市统计公报. Let me search "北京市 2023年国民经济和社会发展统计公报 农业机械总动力" — likely the公报 doesn't include it. Statistical yearbook does. I'll report the plan's 120万千瓦 target and note actual latest not clearly found; maybe find from 国民经济统计资料. Let me attempt selectdataset fetch.

- 农机社会化服务组织数量 Beijing: not found. Maybe search "北京市 农机服务组织 个 全市". Try "北京市 农机合作社 示范社 数量" or "北京市 农业社会化服务组织 数量 个". Could also find in 北京市农业机械化提升行动实施方案 full text (mei.net.cn page). Let me fetch that page fully for service org data? It gave targets. Maybe mentions 培育区域性农机社会化服务组织. Let me fetch again with different prompt for tasks, or fetch the original on beijing.gov.cn.

Let me search for the official 北京市农业机械化提升行动实施方案 on beijing.gov.cn and fetch.

Let me also fetch:
- http://www.moa.gov.cn/xw/qg/202405/t20240527_6456153.htm (丰台 田管家)
- retry http://www.moa.gov.cn/xw/qg/202207/t20220707_6404199.htm
- https://www.bjhr.gov.cn/zwgk/zcjd2024/202601/t20260104_4397541.html
- search 北京市农业机械化提升行动实施方案 beijing.gov.cn

Let me batch.

Also need 全国 农业生产托管 data and 山东/黑龙江 verify. I have enough with news URLs; could add 央广网 黑龙江 and 齐鲁网 山东. Good.

Let me proceed.

</details>

- 🔧 **WebFetch** `{"prompt": "Extract the exact subsidy standards and scope of this Huairou District 2024-2025 operation subsidy plan: 卫星平地, 农机深松整地, 高质量小麦播种, 高质量玉米播种, 丘陵山区玉米收获 amounts per mu, subsidy objects, and policy basis. Quote key sentences.", "url": "https://www.bjhr.gov.cn/zwgk/zcjd2024/202601/t20260104_4397541.html"}` → `**金额标准（按验收合格面积计）** “卫星平地100元/亩、农机深松整地50元/亩、高质量小麦播种35元/亩、高质量玉米播种35元/亩、丘陵山区玉米收获80元/亩”。 **适用范围** “在我区域内且在永久基本农田上实施的卫星平地、农机深松整地、高质量小麦播种、高质量玉米播种和山区玉米机收作业并审核合格的给予补贴”。 附加限制包括：“卫星平地作业需和玉米或小麦高质量播种作业配套完成，卫星平地单独作业不予补贴”；“当年同一地块作业只补贴1次”；“对高标准农田建设方案中已包含卫星平地环节的地块，不给予卫星平地作业补贴”；“农机深松整地作业每2年对同一地块只补贴1次”；“丘陵山区玉米收获按照各镇乡划定区域范围并上报市局备案的作业可享受补 …[截断,原长559]`

- 🔧 **WebFetch** `{"prompt": "Extract all facts about 农业生产托管 in Beijing Fengtai mentioned here: what is 田管家, which platform/organization, service links (耕/种/防/收), service area, participants, and policy support. Quote key sentences.", "url": "http://www.moa.gov.cn/xw/qg/202405/t20240527_6456153.htm"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "Extract the full details of 农田托管服务 in Shunyi: cooperatives involved, trusteeship model (全程/环节托管), service area, number of machines, service prices/fees, farmers' benefits, and any terms like 一条龙 or 保姆式. Quote key sentences with numbers.", "url": "http://www.moa.gov.cn/xw/qg/202207/t20220707_6404199.htm"}` → `文章明确出现“种地全程托管，农机电话预约”；未出现“环节托管”或“保姆式”，而使用“田保姆”“一条龙”。农户付黔方“将地里所有的农活儿都托管给了合作社”，属于全流程托管描述。 **总体情况**：顺义“三夏”由“16家农机专业合作社和农机大户带领机手、技术人员穿梭在田间”提供服务。面积数据为“小麦收获面积约12万亩，玉米`

- 🔧 **Bash** `{"command": "node -e '\nconst https=require(\"https\");\nconst qs=[\n \"\\u5317\\u4eac\\u5e02\\u519c\\u4e1a\\u673a\\u68b0\\u5316\\u63d0\\u5347\\u884c\\u52a8\\u5b9e\\u65bd\\u65b9\\u6848 2023-2025 beijing.gov.cn\",\n \"\\u5317\\u4eac \\u519c\\u673a\\u793e\\u4f1a\\u5316\\u670d\\u52a1\\u7ec4\\u7ec7 \\u57f9\\u80b2 \\u533a\\u57df\\u6027 \\u5edf\\u4f1a\\u5316\\u670d\\u52a1\\u4e2d\\u5f …[截断,原长413]` → `===== 北京市农业机械化提升行动实施方案 2023-2025 beijing.gov.cn ===== - 北京市农业机械化提升行动实施方案(2023-2025) URL: https://njhs.moa.gov.cn/qcjxhtjxd/202301/t20230131_6419551.htm 农机社会化服务能力提升、农机监管和服务水平提升5大行动,组织实施15项重点工程39个主要项目,即北京农机化提升 3515 行动计划,加快提升本市农... - 北京市农业机械化提升行动实施方案(2023-2025年)_机械工业行业信息服务网站 URL: http://www.mei.net.cn/nyjx/202302/16766140 …[截断,原长5025]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:32）

Let me verify Beijing subsidy standards, the Shunyi trusteeship case, and find the official mechanization action plan.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

Great. Found official plan on njhs.moa.gov.cn (农业农村部 农机化司): https://njhs.moa.gov.cn/qcjxhtjxd/202301/t20230131_6419551.htm. Let me fetch it for full details on service organizations and 3515 plan.

Also 山东 2.5亿亩次 has 齐鲁网 video URLs; better to find a text source. The qq news one is text. Fine.

黑龙江: 人民网 2021 超2000万亩; 2022 超3000万亩 (人民网). 2021 农民日报: 4700多个服务组织. Good.

Now fetch the 3515 plan for details, especially 农机社会化服务能力提升行动 and targets. Also maybe Beijing 农机服务组织数量 targets.

Also fetch 丰台 田管家 (failed extraction twice - maybe page structure). Try once more later; might not be needed.

Remaining gaps:
- Beijing 农机社会化服务组织数量 (actual): plan might mention "培育区域性农机社会化服务中心XX个" or "农机服务组织XX家". Let me fetch plan.
- Beijing 托管服务面积: likely not published. The Shunyi moa article gives 顺义 三夏 16家农机合作社, 12万亩小麦; not托管面积. Mark 未找到 for city-level.
- 深松: have 怀柔/房山 standards; Beijing-level policy 2015 30万亩/50元; note latest specific.
- 秸秆禁烧: Beijing 99%+ utilization; 全面禁烧, 卫星监测零火点. Good.

Let me fetch the 3515 plan and also check 北京市 2024统计公报 for 农机总动力 maybe via search of statistical yearbook. Let me also try fetching selectdataset page (might have Beijing machinery power time series) - it's a data aggregator, not authoritative, but could point to 中国统计年鉴. I'll instead report the plan target and note actual value not found in authoritative accessible source.

Actually, I could fetch 北京市统计年鉴 online. The 北京市农业农村局 publishes 北京农村年鉴. Hard. I'll mark 未找到 for precise latest actual 农机总动力.

Let me fetch the plan page. And also do a search for "北京 农机合作社 示范社 名单 2023" and "北京 农业生产托管 面积 万亩" maybe.

Let me fetch plan + 黑龙江人民网 + maybe 山东 text.

Let me do:
WebFetch:
1. https://njhs.moa.gov.cn/qcjxhtjxd/202301/t20230131_6419551.htm — full plan
2. http://hlj.people.com.cn/n2/2022/1122/c220027-40203969.html — 黑龙江 3000万亩
3. https://news.qq.com/rain/a/20240921V0359800 — 山东 2.5亿亩次

And Bash search:
- 北京市 农机合作社 示范社 名单 2023 农业农村局
- 北京 农业社会化服务 组织 数量 家 农机
- 北京 小麦 玉米 秸秆 综合利用 补贴 方案

Let me go.

</details>

- 🔧 **WebFetch** `{"prompt": "Extract the full structure of 北京市农业机械化提升行动实施方案(2023-2025年): the 5 major actions (五大行动), 15 key projects, main quantified targets (2025), especially those on 农机总动力, 耕种收综合机械化率, 农机社会化服务能力提升 (number of service organizations, trusteeship/service area), subsidies, and 秸秆综合利用. Quote key sentences with numbers.", "url": "https://njhs.moa.gov.cn/qcjxhtjxd/202301/t20230131_64 …[截断,原长391]` → `方案采用“3大领域—5大行动—15项工程—39个项目”的“3515”推进框架。核心结构如下： **一、5大行动及对应15项重点工程** 1. “重点产业机械化提升行动”：含①种植业机械化水平提升、②养殖业机械化水平提升、③农产品加工业机械化水平提升、④农业生产宜机化改造。 2. “绿色智能装备升级行动”：含⑤农机节能减排迭代升级、⑥绿色农机化技术推广应用、⑦农机装备智能化改造、⑧农业机械化综合管理系统。 3. “重大科技联合攻关行动”：含⑨农机关键装备科技攻关和新技术推广应用。 4. “农机社会化服务能力提升行动”：含⑩农机服务组织装备能力提升、⑪农机服务组织基础设施配套提升、⑫农机服务组织规模经营能力提升。 5. “农机监管和服务 …[截断,原长803]`

- 🔧 **WebFetch** `{"prompt": "Extract facts about Heilongjiang agricultural production trusteeship: 全程托管 area (万亩), number of service organizations, number of small farmers served, years, and the 兰西模式. Quote key sentences with numbers and dates.", "url": "http://hlj.people.com.cn/n2/2022/1122/c220027-40203969.html"}` → ``

- 🔧 **Bash** `{"command": "node -e '\nconst https=require(\"https\");\nconst qs=[\n \"\\u5317\\u4eac\\u5e02 \\u519c\\u4e1a\\u673a\\u68b0\\u5316\\u63d0\\u5347\\u884c\\u52a8 \\u4e94\\u5927\\u884c\\u52a8 3515 \\u519c\\u673a\\u793e\\u4f1a\\u5316\\u670d\\u52a1\",\n \"\\u5317\\u4eac \\u519c\\u673a\\u5408\\u4f5c\\u793e \\u793a\\u8303\\u793e \\u540d\\u5355 2023 \\u519c\\u4e1a\\u519c\\u6751\\u5c40\", …[截断,原长412]` → `===== 北京市 农业机械化提升行动 五大行动 3515 农机社会化服务 ===== - 北京市农业机械化提升行动实施方案(2023-2025年)_机械工业行业信息服务网站 URL: http://www.mei.net.cn/nyjx/202302/1676614067.html 紧密围绕种植、养殖、农产品加工3大领域,深入实施重点产业机械化提升、绿色智能装备升级、重大科技联合攻关、农机社会化服务能力提升、农机... - 我市机械强农怎么干? “五大行动”来明确_要闻_新闻中心_长江网_cjn.cn URL: https://news.cjn.cn/hbpd_19912/yw_19915/202307/t4613394.htm  …[截断,原长4899]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:33）

Let me fetch the official Beijing mechanization action plan and verify national case data.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

I have most data. Let me now gather cooperative specifics for 鑫利 (service area) and finalize. Also the "两家合作社入选第一批全国全程机械化+综合农事服务典型案例" - which two? Likely 北京兴农天力 and 北京张书安. Let me fetch the sohu article to identify the Beijing cooperatives in the national typical cases. That's relevant for honor.

Also need 北京市农机合作社数量 - the plan didn't give. Maybe from 北京市农业机械试验鉴定推广站调研 or 北京农机化统计. Mark 未找到 if not.

Let me fetch:
1. https://www.sohu.com/a/397105122_120209831 — identify two Beijing cooperatives入选全国全程机械化+综合农事服务中心典型案例
2. http://bj.people.com.cn/n2/2022/0616/c82840-35317708.html — straw 99% (text, people.cn)
3. Maybe 鑫利 details: search "鑫利农机合作社 服务面积" found 1万多亩小麦. Let me get a bit more: The moa 2022 article says 8 harvesters, 李遂镇. Good enough.

Also 北京绿谷汇德: user asked; found 果品产销合作社 (2008, 平谷刘家店镇) and 农业科技公司 (2015, 平谷). No machinery service data. I'll state that no public info about a 农机 service cooperative named 绿谷汇德; likely refers to 果品合作社 (non-machinery) — mark accordingly.

Let me also check 大兴/房山/平谷 machinery cooperatives to name some. Search "大兴 农机合作社" "平谷 农机合作社" "房山 农机合作社". Quick search.

Let me do final batch: fetches + search.

Also need Beijing 农机总动力 actual value. Let me search "北京 农业机械总动力 万千瓦 2020 2021 2022 统计年鉴" one more time; maybe a stats page. If not found, note plan target and that actual latest not found.

Let me run.

</details>

- 🔧 **WebFetch** `{"prompt": "Identify which two Beijing cooperatives were selected in the first batch of national \"全程机械化+综合农事\" service center typical cases, and describe what each does (service area, model, honors). Quote key sentences.", "url": "https://www.sohu.com/a/397105122_120209831"}` → `入选的是 **北京兴农天力农机服务专业合作社** 和 **北京张书安农业技术服务专业合作社**。官方信息称：“农业农村部遴选发布了70个‘全程机械化+综合农事’服务中心典型案例”，且“北京兴农天力农机服务专业合作社和北京张书安农业技术服务专业合作社代表北京成功入选”。 **1. 北京兴农天力农机服务专业合作社（顺义区赵全营镇前桑园村）** 以农机作业服务为基础，通过土地流转、全程托管等方式推进适度规模经营；业务还扩展到蔬菜、花卉、休闲景观、农机科普、农产品加工销售等。其模式亮点是“装备优化服务创新并举 打造都市现代农业样板”，并“通过土地流转、全程托管等形式，实现了土地适度规模经营”。荣誉：第一批全国“全程机械化+综合农事”服务中心 …[截断,原长529]`

- 🔧 **WebFetch** `{"prompt": "Extract facts about Beijing straw comprehensive utilization rate: the exact percentage, year, the agency that stated it, and the two main straw treatment methods (粉碎还田 and 打捆离田) with their uses. Quote key sentences and note the date/source.", "url": "http://bj.people.com.cn/n2/2022/0616/c82840-35317708.html"}` → ``

- 🔧 **Bash** `{"command": "node -e '\nconst https=require(\"https\");\nconst qs=[\n \"\\u5927\\u5174 \\u519c\\u673a\\u5408\\u4f5c\\u793e \\u670d\\u52a1\",\n \"\\u5e73\\u8c37 \\u519c\\u673a\\u5408\\u4f5c\\u793e \\u670d\\u52a1\",\n \"\\u623f\\u5c71 \\u519c\\u673a\\u5408\\u4f5c\\u793e \\u670d\\u52a1\",\n \"\\u5317\\u4eac \\u519c\\u4e1a\\u673a\\u68b0\\u603b\\u52a8\\u52a8\\u529b 2022 \\u7edf\\u8b …[截断,原长413]` → `===== 大兴 农机合作社 服务 ===== - 北京市大兴区农机服务中心 - 爱企查 URL: https://aiqicha.baidu.com/company_detail_26841109035575 注册地址 大兴区黄村镇永华南里16号楼 查看地图经营范围 为本区农业机械化发展及农机科技,农机协作,农机信息咨询发展动态服务。.赵永兴他投资的 1 家公司经营状态 注销 成立日期 - 行政区划 北... - 沙县大兴农机专业合作社 - 水滴信用 URL: https://shuidi.cn/company-3342fae2fa4c070bdc08d0458393b2d4.html?from_search=1 - 北京市大兴区 …[截断,原长3969]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:33）

Let me finalize with the Beijing "全程机械化+综合农事" cases, other district cooperatives, and the official straw source.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

I have enough. Beijing 农机总动力 actual value not found in authoritative accessible source. I'll report the plan target (120万千瓦 by 2025) and note actual latest value not found publicly accessible (statistical yearbook paywalled / aggregator only).

Let me do one more attempt for the actual Beijing machinery power using the CSDN dataset maybe includes table. But it's a blog. Could try fetching it. Actually not worth; I'll mark it.

Also, I should verify Beijing 耕种收综合机械化率 actual latest. nercita says 大田粮食作物综合机械化率超过90% (but that's 大田粮食作物, not 主要农作物耕种收). The plan target is 75%+ by 2025. There might be a news saying 北京 2023 综合机械化率. Let me do one targeted search: "北京 农作物耕种收综合机械化率 2023 达到". Quick.

Also Beijing 农机社会化服务组织数量/托管面积 — mark 未找到. But maybe 北京市 2023 农业社会化服务项目 with 服务面积. Search once "北京市 农业生产托管服务项目 服务面积 万亩 2023".

Let me do a final quick search batch (3 queries), then compose the report. I should be mindful of time. Let me run.

Queries:
1. 北京 农作物耕种收综合机械化率 达到 2023
2. 北京市 农业生产托管 项目 面积 万亩 服务组织
3. 北京 农机合作社 数量 家 650 (maybe)

Let me run.

</details>

- 🔧 **Bash** `{"command": "node -e '\nconst https=require(\"https\");\nconst qs=[\n \"\\u5317\\u4eac \\u519c\\u4f5c\\u7269\\u8015\\u79cd\\u6536\\u7efc\\u5408\\u673a\\u68b0\\u5316\\u7387 \\u8fbe\\u5230 2023\",\n \"\\u5317\\u4eac\\u5e02 \\u519c\\u4e1a\\u751f\\u4ea7\\u6258\\u7ba1 \\u670d\\u52a1\\u9879\\u76ee \\u9762\\u79ef \\u4e07\\u4ea9\",\n \"\\u5317\\u4eac \\u5927\\u7530\\u7cae\\u98df\\u4f5c …[截断,原长413]` → `===== 北京 农作物耕种收综合机械化率 达到 2023 ===== - 农业生产能力持续提升 都市农业发展态势良好——2023年北京农业经济运行情况解读 URL: https://tjj.beijing.gov.cn/zxfbu/202401/t20240119_3539803.html 2024年1月19日 - 图 2023年北京农林牧渔分行业产值.2023年,北京农业生产结构进一步调整,粮食播种面积和总产量实现双增长,蔬菜生产继续稳中有进,生猪和家禽养殖规模缩小... - 北京市2023年国民经济和社会发展统计公报发布|农产品|在校生|总量_新浪新闻 URL: https://k.sina.com.cn/article_16 …[截断,原长3431]`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:34）

Let me do a final targeted search for Beijing's actual mechanization rate and trusteeship area.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

Found a very relevant source: 腾讯新闻 2022-11-29 "全市大田农业机械率达到86%..." says "目前全市农作物耕种收综合机械化水平突破79%，小麦、水稻、玉米等粮食作物耕种收综合机械化率已达86%以上". That's Beijing 2022 data (as of Nov 2022). Good. Let me fetch it to confirm details and date.

Let me fetch https://news.qq.com/rain/a/20221129A03UIE00 to verify. Also fetch nercita page for 大田粮食作物 >90% (2026). And maybe the toutiao article (may be blocked).

Let me fetch the QQ news article.

Then compose final answer. I think I have enough.

Let me also get the 北京市 2023 农业经济运行情况解读 (tjj.beijing.gov.cn) - probably no mechanization. Skip.

Let me fetch QQ article and nercita quickly.

</details>

- 🔧 **WebFetch** `{"prompt": "Extract all Beijing agricultural mechanization figures: 农作物耕种收综合机械化水平 percentage, 粮食作物耕种收综合机械化率, 烘干率, year/date, and any data on 农机服务组织/合作社/托管. Quote key sentences with numbers and note the article date and source.", "url": "https://news.qq.com/rain/a/20221129A03UIE00"}` → `REDIRECT DETECTED: The URL redirects to a different host. Original URL: https://news.qq.com/rain/a/20221129A03UIE00 Redirect URL: https://www.qq.com/babygohome/?pgv_ref=apub Status: 302 Found To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters: - ur …[截断,原长595]`

- 🔧 **WebFetch** `{"prompt": "Extract what this page says about Beijing agricultural mechanization: 大田粮食作物综合机械化率 percentage, 设施农业机械化水平 percentage, the person quoted, date, and any related data. Quote key sentences.", "url": "http://www.nercita.org.cn/infos/detail?id=10820&type=206"}` → `- 页面关键句：“目前北京地区大田粮食作物的综合机械化率已经超过90%，但设施农业机械化水平仅50%左右。” - 被引述者：张钟莉莉，页面标注职务为“北京市农林科学院智能装备技术研究中心副主任”。 - 时间：网页显示“时间：2026-05-09”，并注明“报道来源：北京日报 2026年5月2日”。 - 相关数据：其团队研发的东西垄水肥管理系统昵称“小东西”；页面称其“节水、节肥、省人工，还能实现10%左右的增产”，研发“前后用时近10年”，已在顺义、房山、通州等区温室大棚应用。`

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:34）

Found 2022 Beijing mechanization data. Let me verify it.

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

I have enough. Let me update todos to completed and write the final report.

Let me compile findings into a要点清单 in Chinese with source URLs. I must be careful: distinguish verified vs unverified, and mark 未找到 where appropriate. Avoid fabricating. Some dates in search results are odd (2026 dates because today is 2026-09-12 per context? Actually context says 2026-09-12? It says "Today's date is 2026-09-12"). Wait, the context says 2026-09-12. So 2026-dated articles are current. OK. That explains "2026-05-09". Good.

So current date is 2026-09-12. The user asks for 北京最新数据 2023-2025. I have:
- 2023-2025 plan targets (农机总动力120万千瓦, 综合机械化率75%+, 设施55%, 秸秆全量化利用/99%+).
- 2022 actual: 综合机械化水平突破79%, 粮食作物86%+ (from 腾讯 2022, but I couldn't fetch to confirm; search snippet gave it). The snippet: "全市农作物耕种收综合机械化水平突破79%，小麦、水稻、玉米等粮食作物耕种收综合机械化率已达86%以上，水稻、小麦产地烘干率分别达..." from 2022-11-29. I can cite the search-result snippet URL but should note I could not open page. Hmm, the search engine provided this description, which is a legitimate source snippet but I couldn't verify the page directly. I'll cite the URL and note it's from a 2022-11-29 腾讯新闻 report via search snippet.
- 2026 (北京日报 2026-05-02): 大田粮食作物综合机械化率超90%, 设施农业仅50%左右 (via nercita). This is post-2025. Good.

Beijing 农机总动力 actual value: not found; plan target 120万千瓦. Mark actual not found.

农机社会化服务组织数量 (Beijing): 未找到公开量化数据. Plan mentions no total number. 
托管服务面积 (Beijing city-level): 未找到. Shunyi "三夏" 16家农机合作社; 丰台 田管家 case exists but extraction failed; mention with source.
顺义 三夏: 16家农机专业合作社和农机大户, 小麦收获面积约12万亩 (moa 2022).

Cooperatives:
- 北京市鑫利农机服务专业合作社: 成立2008-12-19, 顺义区李遂镇柳各庄村, 法人金跃, 注册资本 (企查查/爱企查 says 579.25万 or likuso 1600.95万 - conflicting; better say "注册资本存在不同来源差异，企查查/爱企查显示约579万元，第三方黄页称1600.95万元，建议以国家企业信用信息公示系统为准"). Actually I should avoid over-claiming. The 爱企查 snippet: 注册资本 579.25万. qcc: no number shown. likuso: 1600.95万元. Conflicting → note.
  - 2017年全国农机合作社示范社 (sohu list)
  - 2022 顺义李遂镇倒伏小麦抢收, 调集8台收割机 (moa.gov.cn)
  - 种1万多亩小麦, 秸秆粉碎还田+深松+高性能播种 (科普网/搜狐 2022; agri.cn 2026)
  - 运营模式: 农户+农机合作社+养殖场+有机肥厂 (2016 农机1688) — note this article names 葛代子村鑫利农机服务专业合作社, 理事长金振启; may be a related entity.
  - 服务面积: 未找到明确公开数据.
- 北京兴农天力农机服务专业合作社: 成立2008 (工商登记2009-01-21? 360百科 says 2009-01-21; sohu says 成立于2008; article news.nongjigou says 2008). Note both. 顺义区赵全营镇前桑园村; 社员365户; 流转土地1.2万亩; 农机资产3000余万; 2019收入5000余万, 吸收劳动力335人; 280余台件设备、技术人员近80人 (moa 2022); 法人/理事长 陈领; 荣誉: 2010/2013/2016全国农机合作社示范社, 第一批全国"全程机械化+综合农事"服务中心典型案例, 国家农民合作社示范社(2018).
- 北京张书安农业技术服务专业合作社: 延庆区旧县镇西龙湾村, 第一批全国全程机械化+综合农事典型案例, 玉米全程机械化+秸秆打包.
- 北京绿谷汇德: no machinery service coop found; found 北京绿谷汇德果品产销专业合作社 (2008, 平谷刘家店镇, 法人岳海云) and 北京绿谷汇德农业科技有限公司 (2015, 平谷刘家店镇, 法人岳清涛). Note not confirmed as 农机合作社.
- 平谷: 北京绿谷达丰农机服务专业合作社 (2008-02-25, 平谷夏各庄镇, 注册资本100万, 经营范围整地等) — from liepin snippet. 平谷农机合作联社 (2011 中国农民合作社 article). 
- 房山: 北京金利农机服务专业合作社 (爱企查) — no details.
- 大兴: no specific coop found; 北京市大兴区农机服务中心 (institution, 注销).

Policy:
- 农机购置与应用补贴: 《2024—2026年度北京市农机购置与应用补贴实施方案》京政农发〔2024〕70号, 2024-12-30印发, 13个涉农区. 中央部分20大类35小类75品目, 市级8大类16小类50品目, 重点机具10品目≤20档次. 中央补贴不超过上年销售均价30%, 重点35%, 急需(移动式烘干机、履带拖拉机)40%; 市级单补不超35%. 上限: 农民50万/年, 经营组织500万/年. 操作: 自主购机、定额补贴、先购后补、区级结算、直补到卡.
  Sources: beijing.gov.cn 通知, nyncj 解读.
  Note: the beijing.gov.cn page fetch failed extraction but URL valid; nyncj interpretation worked.
- 农机报废更新补贴: 《北京市农业机械报废更新补贴实施方案》(2024-09-30?) URL.
- 深松整地: 怀柔 2024-2025: 农机深松整地50元/亩 (每2年同一地块1次), 卫星平地100元/亩, 高质量小麦播种35元/亩, 玉米35元/亩, 丘陵山区玉米收获80元/亩; 房山 similar 50/35/35. Policy basis: 北京市农业农村局 2024年度智能农机装备助力单产提升及保护性耕作技术推广作业补贴. 2015 Beijing plan: 30万亩, 50元/亩. Note: may be superseded; latest district-level standards as above.
- 秸秆: 北京秸秆综合利用率保持99%以上 (2022 新京报/人民网; 2024 人民政协网/农民日报). 处理方式: 粉碎还田肥料化; 打捆离田用于牛场垫料、食用菌原料、有机肥等; 昌平10个农业废弃物综合利用站, 四年处理15.1万吨. 大兴区秸秆类废弃物综合利用行动方案(2023-2025) 京兴政农发〔2023〕29号. 全面禁烧 (2015 全面禁烧和综合利用), 卫星监测零火点.
  Note: I should verify "禁烧" current policy — Beijing has 全面禁烧 per sources; mark.

Model:
- 农业生产托管定义 (山西地方标准/网易 article): 不流转土地经营权, 将耕、种、防、收全部或部分环节委托服务组织; 全程托管/单环节/多环节/关键环节; 与土地流转区别 (不转移经营权).
- 河北6种模式: 全产业链托管(保姆式), 菜单式多环节托管, 土地股份合作分红, 股份托管并行, 专业化托管, 供销社为农服务中心. Data: 2022 target 3.5万家, 2.5亿亩次.
- Beijing 顺义 2022 moa: "种地全程托管，农机电话预约"; "田保姆"; "一条龙"; 16家农机合作社; 小麦约12万亩.
- Beijing 丰台 "田管家" 托管 (moa 2024-05) — extraction failed; cite with note.
- 黄龙县 三岔镇 "保姆式托管、菜单式服务" (sina/sohu) example.
- 国家: 全国经营性主体111.1万个, 服务小农户近9300万户, 年服务面积22.9亿亩次 (2024年底, 农业农村部). Source URL? It appeared as a 360 result without mdurl. Let me use a citable one: I have snippet "农业农村部:全国111.1万个经营性主体提供农业社会化服务". No URL captured. Better cite 金文成/全国 data via sohu 477677057 (农业生产托管面积超16亿亩). Hmm uncertain. I'll mention national figure with caution or skip. Actually I can cite the moa.gov.cn 2019 70% page for 全国机械化率.

- 山东: 托管服务面积近2.5亿亩次, 80%以上托管粮食作物 (齐鲁网 2024-09-20; qq news). 昌乐县 231.5万亩次 (agri.cn 2025). 
- 黑龙江: 2021 全程托管超2000万亩, 4700多个服务组织 (农民日报 2021); 2022 耕种全程托管超3000万亩 (人民网 2022-11-22); 兰西县 托管61.5万亩占耕地23.5%, 全程18.35万亩 (2023 东北网). 2025目标全程托管6000万亩 (sohu). 8039万亩次 (2020). 
Note some numbers differ by indicator (全程托管 vs 托管总亩次).

Problems:
- sohu 2019 (中国农机化导报?): 四大难题 资金筹措难、补贴兑现难、人才队伍培养难、经济纯收入增加难; 机手老龄化、流动性差、培训不足; 融资难(无抵押物, 大型机具抵押未落实); 全国农机合作社7万家; 部分亏损或持平.
- toutiao: 机手队伍老化严重.
- 装备利用率低/土地细碎化/服务价格竞争/维修能力弱: not directly found in that article; I can note 未找到专门公开调研数据 for some, or mention the 蔬菜产业农机社会化服务组织发展现状及对策 (360文库) which discusses problems. Also 大兴区农机社会化服务模式研究 (CNKI master's thesis 2022) — relevant academic source. I'll list these as further reading without fabricating specifics.
- 农村人口老龄化对农机社会化服务的影响 (龙源期刊 2024) — academic.

Beijing organizational count: 未找到.

Now write the report. It should be a要点清单 in Chinese with source links. I'll organize by the 5 requested topics, mark clearly verified/unverified, and add a note on methodology and caveats (search engine used, dates odd). Also note that some data are from secondary/company-registration sources and should be cross-checked.

Let me be concise but complete. Include absolute URLs.

I should note that the "current date" is 2026-09, so "最新" data may extend to 2025/2026.

Let me write final answer. I'll avoid emojis. Use headings and bullets.

I'll mark:
- 找到的
- 未找到公开资料

Let me carefully list URLs.

Key URLs:
Beijing plan: https://njhs.moa.gov.cn/qcjxhtjxd/202301/t20230131_6419551.htm ; http://www.mei.net.cn/nyjx/202302/1676614067.html
补助 policy: https://www.beijing.gov.cn/zhengce/zhengcefagui/202503/t20250325_4044054.html ; https://nyncj.beijing.gov.cn/nyj/zwgk/zcjd84/543511218/index.html
报废更新: https://www.beijing.gov.cn/gate/big5/www.beijing.gov.cn/zhengce/zhengcefagui/202501/t20250102_3979031.html (big5 version; canonical maybe https://www.beijing.gov.cn/zhengce/zhengcefagui/202501/t20250102_3979031.html)
怀柔 deep loosening: https://www.bjhr.gov.cn/zwgk/zcjd2024/202601/t20260104_4397541.html
房山: https://www.bjfsh.gov.cn/ztzx/wqzt/zdlyzwgk/pihss/202204/t20220412_40044406.shtml
北京公共资源: https://ggzyfw.beijing.gov.cn/jyxxzbjggg/20240108/4293808.html
2015 深松: https://www.nongjitong.com/news/2015/372750.html
Straw: https://www.rmzxw.com.cn/c/2024-04-10/3522875.shtml ; https://www.bjnews.com.cn/detail/1655206585168969.html ; http://bj.people.com.cn/n2/2022/0616/c82840-35317708.html (cert issue but URL); https://www.bjdx.gov.cn/bjsdxqrmzf/zwfw/zfwj67/1380045/2032853/index.html
mechanization 2022: https://news.qq.com/rain/a/20221129A03UIE00
nercita 2026: http://www.nercita.org.cn/infos/detail?id=10820&type=206
chen ling article: http://news.nongjigou.cn/n/201604/26/101185.html (fetch failed, but URL)
兴农天力 sohu: https://www.sohu.com/a/463793839_121106842
兴农天力 moa: http://www.moa.gov.cn/xw/qg/202207/t20220707_6404199.htm
全国全程机械化+综合农事: https://www.sohu.com/a/397105122_120209831
鑫利 moa: https://www.moa.gov.cn/xw/qg/202206/t20220624_6403247.htm
鑫利 2022 小麦: http://www.kepu.gov.cn/jnsc2025/content_1744534.html ; https://www.sohu.com/a/557194895_114988
鑫利 2026 保护性耕作: http://www.agri.cn/zx/xxlb/bj/202603/t20260319_8820597.htm
顺义转型 2016: http://www.nongji1688.com/news/201607/11/5508819.html
示范社名单: http://www.moa.gov.cn/gk/tzgg_1/tfw/201302/t20130205_3215746.htm (2013 第一批, 兴农天力); https://www.sohu.com/a/212137352_651395 (2017, 鑫利)
企业注册: 爱企查鑫利 https://aiqicha.baidu.com/company_detail_29353302435930 ; 企查查鑫利 https://www.qcc.com/firm/c73acf0b62fc6aa15a457ac8779c310d.html ; 爱企查兴农天力 https://aiqicha.baidu.com/company_detail_28688946106716
绿谷汇德: https://aiqicha.baidu.com/company_detail_28838288109724 ; https://shuidi.cn/company-f05aa0cc90ce7182545942cd51f6656b.html
平谷绿谷达丰: https://www.liepin.com/company/gs37576779/
河北6模式: https://hebei.hebnews.cn/2020-04/28/content_7816065.htm
托管定义: https://www.163.com/dy/article/EMUKS8F70511DJHA.html
黄龙 保姆式: https://cj.sina.cn/articles/view/3834132443/e48837db00100x8k8 ; https://www.sohu.com/a/516400857_121207966
山东: https://news.qq.com/rain/a/20240921V0359800 ; https://www.agri.cn/zx/xxlb/sd/202508/t20250821_8760009.htm
黑龙江: https://www.farmer.com.cn/2021/07/01/wap_99873533.html ; http://hlj.people.com.cn/n2/2022/1122/c220027-40203969.html ; https://m.dbw.cn/heilongjiang/system/2023/10/30/059231175.shtml
丰台田管家: http://www.moa.gov.cn/xw/qg/202405/t20240527_6456153.htm
合作社问题: https://www.sohu.com/a/329322522_651395 ; https://www.toutiao.com/article/6723133538117353998/
学术: https://xuewen.cnki.net/CMFD-1013359307.nh.html (大兴区农机社会化服务模式研究) ; https://www.qikan.com.cn/article/5dd020240246.html
National mechanization 2024: https://njhs.moa.gov.cn/nyjxhqk/202511/t20251120_6479055.htm (2024全国农业机械化发展统计公报) — wait date 202511 = 2025-11. Good, national 2024 data: 75.64%.

Also 全国农机合作社示范社 mention.

Now, caveats: Dates from 360 search snippets may be unreliable (the search engine shows odd future dates). I verified key ones by fetching. Company registration data from 爱企查/企查查/水滴信用 are third-party aggregations; recommend 国家企业信用信息公示系统.

Let me write the final answer now. Given it's a subagent report, be thorough but structured.

I'll mark todo completed.

Length: substantial but organized. Let me write.

One more: The user asked "京郊农机社会化服务组织数量、托管服务面积" - mark 未找到公开量化数据 for both. Also "农机总动力" actual current - 未找到, plan目标120万千瓦.

Also "北京最新数据 2023-2025": I have plan targets for 2025 and 2022 actual 79%/86%; 2026 大田粮食>90%. Note that I could not find an official 2023-2025 actual statistic for 耕种收综合机械化率; the 2022 figure came from a news report I couldn't open directly (redirected). I'll state it carefully.

Let me write.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "Research Beijing agricultural mechanization overall data", "priority": "high", "status": "completed"}, {"content": "Research 'one-stop' farm machinery trusteeship model", "priority": "high", "status": "completed"}, {"content": "Research specific Beijing cooperative cases", "priority": "high", "status": "completed"}, {"content": "Research Beijing subsidie …[截断,原长412]` → `{"oldTodos":[{"content":"Research Beijing agricultural mechanization overall data","status":"in_progress","priority":"high"},{"content":"Research 'one-stop' farm machinery trusteeship model","status":"in_progress","priority":"high"},{"content":"Research specific Beijing cooperative cases","status":"in_progress","priori …[截断,原长1321]`

<details><summary>💭 `zcode-Explore` 思考链（deepseek-flash）</summary>

Now write final report in Chinese with URLs. Note methodology caveat: Bing via WebFetch gave generic results; used 360搜索 + direct page fetches; some source dates appear as 2026 because current date is 2026-09. I'll include this in a short 说明.

Let me write.

</details>

### 🤖 助手（`zcode-Explore` deepseek-flash，2026-09-12 19:35）

# 京郊现代农机服务与农机专业合作社调研要点

调研说明：Bing 直连返回的是通用缓存页、无法用于检索；本报告主要通过 360 搜索定位线索，再用 WebFetch 直读原文核实。企业工商信息来自爱企查/企查查/水滴信用等第三方聚合，建议写报告时以「国家企业信用信息公示系统」为准。凡未核实到的，标注「未找到公开资料」。

---

## 一、北京市农机化总体情况

1. **政策目标（最权威、可直接引用）**：《北京市农业机械化提升行动实施方案（2023-2025年）》提出「3515」框架（3大领域、5大行动、15项工程、39个项目），2025年量化目标：
   - 农机总动力「稳定在120万千瓦左右」；
   - 农作物耕种收综合机械化率「达到75%以上」；
   - 设施农业机械化率55%以上、畜牧养殖85%以上、水产养殖50%以上、农产品初加工50%以上；
   - 秸秆「基本实现全量化综合利用」，并「力争全市秸秆综合利用率保持在99%以上」；
   - 农机社会化服务能力提升行动含「农机服务组织装备能力、基础设施配套、规模经营能力」3项工程；推动「社会化服务、土地托管、土地流转」等形式，并创建全国「全程机械化+综合农事」服务中心。
   来源（农业农村部农机化司全文）：https://njhs.moa.gov.cn/qcjxhtjxd/202301/t20230131_6419551.htm
   来源（转载）：http://www.mei.net.cn/nyjx/202302/1676614067.html

2. **综合机械化率实际值（需注意口径与年份）**：
   - 2022年11月报道称「全市农作物耕种收综合机械化水平突破79%，小麦、水稻、玉米等粮食作物耕种收综合机械化率已达86%以上」，并提及水稻、小麦产地烘干率。来源：https://news.qq.com/rain/a/20221129A03UIE00 （该页现已跳转，正文未能直接打开，数据来自搜索摘要，引用前建议再核实）
   - 2026年5月北京日报报道（北京市农林科学院智能装备技术研究中心副主任张钟莉莉）：「目前北京地区大田粮食作物的综合机械化率已经超过90%，但设施农业机械化水平仅50%左右。」来源：http://www.nercita.org.cn/infos/detail?id=10820&type=206
   - **2023-2025 年北京市官方公布的「实际」耕种收综合机械化率数值：未找到公开资料**（仅找到2025年目标值75%以上与上述口径不同的报道）。

3. **农机总动力实际最新值：未找到公开资料**。仅找到2025年目标「120万千瓦左右」；历年数据见第三方汇总（非官方，谨慎引用）：https://www.gotohui.com/ndata/show-93851 、https://www.selectdataset.com/dataset/6151784539ee95dfef6e371780b2f673

4. **京郊农机社会化服务组织数量：未找到公开量化数据**。仅在《提升行动实施方案》中看到「每区建设1-2支常态化农机应急作业服务队」等措施，未见全市服务组织总数。
   旁证：北京市农业机械试验鉴定推广站曾赴通州区调研农机服务组织（农机哥网转载，日期显示2025-12）：https://www.nongjige.com/showinfo-269-3435-0.html

5. **北京市/京郊农业生产托管服务面积：未找到公开的市级汇总数据**。仅有区级/农时性数据：
   - 顺义区「三夏」由「16家农机专业合作社和农机大户」服务，小麦收获面积约12万亩（详见第二部分）。来源：http://www.moa.gov.cn/xw/qg/202207/t20220707_6404199.htm
   - 丰台区有「田管家」农业生产托管服务报道（页面正文未能抓取，仅存线索）：http://www.moa.gov.cn/xw/qg/202405/t20240527_6456153.htm

---

## 二、「一条龙农机作业托管服务」模式

1. **农业生产托管的标准定义**（可写进报告）：「农户等经营主体在不流转土地经营权的条件下，将农业生产中的耕、种、防、收等全部或部分作业环节委托给农业生产性服务组织完成的农业经营方式。」
   - **与土地流转的区别**：托管不转移土地经营权，只提供生产环节服务，政策上把小农户作为支持对象；而土地流转会转移经营权，遇农产品卖难时容易出现毁约、退地。
   - **托管形式**：全程托管、单环节托管、多环节托管、关键环节托管（即常说的「半托管」为部分环节委托）。
   来源：https://www.163.com/dy/article/EMUKS8F70511DJHA.html

2. **「保姆式」「菜单式」的官方/地方表述**（河北经验，分类最清晰）：
   - 全产业链托管（供、耕、种、防、收、销全程，组织收服务费，即「保姆式托管」，农户「省心、省力、省钱」）；
   - 菜单式多环节托管（农户按需选环节或单项套餐，易复制但利益联结稳定性相对较差）；
   - 土地股份合作分红；股份托管并行；专业化托管（专做植保、农资、秸秆收贮、烘干销售等）；供销社「为农服务中心」。
   - 规模数据：2022年目标覆盖面达70%以上、服务组织3.5万家以上、服务面积2.5亿亩次以上。
   来源：https://hebei.hebnews.cn/2020-04/28/content_7816065.htm
   - 地方实例（「保姆式」托管＋「菜单式」服务的提法）：陕西黄龙县三岔镇，https://cj.sina.cn/articles/view/3834132443/e48837db00100x8k8 、https://www.sohu.com/a/516400857_121207966

3. **京郊本地「一条龙/全程托管」实证（顺义）**：北京市农业农村局转载报道明确出现「种地全程托管，农机电话预约」「田保姆」「一条龙」表述；农户「将地里所有的农活儿都托管给了合作社」，属全流程托管。来源：http://www.moa.gov.cn/xw/qg/202207/t20220707_6404199.htm

4. **全国性托管数据（用于对比论证）**：
   - 全国经营性服务主体约111.1万个，服务小农户近9300万户，年服务面积超22.9亿亩次（其中粮油作物17.8亿亩次，2024年底，农业农村部）。该条为搜索摘要、原URL未捕获，建议另找农业农村部原文核对。
   - 全国农作物耕种收综合机械化率2024年达75.64%（《2024年全国农业机械化发展统计公报》）。来源：https://njhs.moa.gov.cn/nyjxhqk/202511/t20251120_6479055.htm

5. **外省代表案例（可作对比章节）**：
   - 山东：农业托管服务面积近2.5亿亩次、80%以上托管对象为粮食作物（齐鲁网/山东新闻联播，2024-09）。来源：https://news.qq.com/rain/a/20240921V0359800 、https://v.iqilu.com/sdws/wswjxw/202409/20/5593363.html ；昌乐县耕、种、防、收各环节托管总面积231.5万亩次（中国农业农村信息网，2025-08）：https://www.agri.cn/zx/xxlb/sd/202508/t20250821_8760009.htm
   - 黑龙江：2021年全程托管超2000万亩、4700多个服务组织（农民日报）：https://www.farmer.com.cn/2021/07/01/wap_99873533.html ；2022年耕种全程托管超3000万亩（人民网）：http://hlj.people.com.cn/n2/2022/1122/c220027-40203969.html ；兰西县托管61.5万亩、占耕地23.5%，其中全程托管18.35万亩（东北网，2023-10）：https://m.dbw.cn/heilongjiang/system/2023/10/30/059231175.shtml
   - 注意：黑龙江「托管亩次」「全程托管亩」口径不同，不可直接相加比较。

---

## 三、京郊具体合作社案例

### 1. 北京市鑫利农机服务专业合作社（顺义）
- 成立时间：2008-12-19；所在地：北京市顺义区李遂镇柳各庄村（另有资料显示注册地顺义区李遂镇）；法定代表人金跃。工商来源：https://aiqicha.baidu.com/company_detail_29353302435930 、https://www.qcc.com/firm/c73acf0b62fc6aa15a457ac8779c310d.html 、https://www.11467.com/qiye/29514569.htm
- 注册资本：来源不一致（爱企查显示约579.25万元，第三方黄页称1600.95万元），引用需谨慎。
- 荣誉：**2017年全国农机合作社示范社**。来源：https://www.sohu.com/a/212137352_651395
- 装备与作业：2022年顺义李遂镇倒伏小麦抢收中，该社「提前购置、调集多台多功能谷物收割机」，现场8台作业，收割机可分层收割并同步秸秆粉碎还田；截至2022-06-21顺义全区完成小麦收获14688.9亩。来源：https://www.moa.gov.cn/xw/qg/202206/t20220624_6403247.htm
- 经营规模：2022年报道称其「种了1万多亩小麦」。来源：http://www.kepu.gov.cn/jnsc2025/content_1744534.html 、https://www.sohu.com/a/557194895_114988
- 技术模式：2026年报道其把常规种植与保护性耕作融合，「秸秆粉碎还田、深松作业，又进行浅旋实施精准高性能播种」。来源：http://www.agri.cn/zx/xxlb/bj/202603/t20260319_8820597.htm
- **服务面积、装备总台套数：未找到明确公开数据。**
- 另有一篇2016年报道提到「葛代子村鑫利农机服务专业合作社」、理事长金振启，采用「农户+农机合作社+养殖场+有机肥厂」模式，并因「北京的麦田逐渐减少，合作社的农机出现了‘吃不饱’」而转型秸秆综合利用；是否为同一主体需进一步核实。来源：http://www.nongji1688.com/news/201607/11/5508819.html

### 2. 北京兴农天力农机服务专业合作社（顺义）
- 成立：多数报道称成立于2008年（工商登记日期显示2009-01-21）；所在地：顺义区赵全营镇前桑园村；法定代表人/理事长陈领。
  工商来源：https://aiqicha.baidu.com/company_detail_28688946106716 、https://www.qcc.com/firm/821a2fc27bb6bc635673bf5a2ea477ec.html
- 规模（2021年报道）：「现有社员365户，流转土地1.2万亩，农机资产3000余万」；2012年参与赵全营镇都市型万亩示范区，流转8个村6300亩，实行「统一种植、统一管理、统一防控、统一收获、统一销售」；2019年总收入5000余万元，吸收劳动力335人，带动周边5000多农户。来源：https://www.sohu.com/a/463793839_121106842
- 装备（2022年报道）：「有拖拉机、收割机、播种机、粉碎机、植保机等280余台件，种植和农机技术人员近80人」，除自有1.2万亩外还对外服务。来源：http://www.moa.gov.cn/xw/qg/202207/t20220707_6404199.htm
- 模式：以农机作业服务为基础，通过**土地流转、全程托管**推进适度规模经营，并向蔬菜、花卉、休闲观光、农产品加工销售延伸。
- 荣誉：2010年、2013年、2016年全国农机合作社示范社（首批1022家名单见农业部通知），2018年国家农民合作社示范社；**第一批全国「全程机械化+综合农事」服务中心典型案例**（代表北京入选）。来源：http://www.moa.gov.cn/gk/tzgg_1/tfw/201302/t20130205_3215746.htm 、https://www.sohu.com/a/397105122_120209831

### 3. 北京张书安农业技术服务专业合作社（延庆）
- 第一批全国「全程机械化+综合农事」服务中心典型案例（与兴农天力同为北京入选的2家）。聚焦玉米全程机械化，开展「一站式」综合农事服务，并承担秸秆回收打包，形成秸秆综合利用「延庆模式」。来源：https://www.sohu.com/a/397105122_120209831
- 地址：延庆区旧县镇西龙湾村（同上）。

### 4. 北京绿谷汇德（平谷）
- **未找到名为「北京绿谷汇德农机（服务）专业合作社」的公开资料。** 可查到的主体为：
  - 北京绿谷汇德果品产销专业合作社（成立2008-04-08，平谷区刘家店镇北店东路29号，法定代表人岳海云，注册资本300万元）——果品产销，非农机。来源：https://aiqicha.baidu.com/company_detail_28838288109724
  - 北京绿谷汇德农业科技有限公司（成立2015-10-23，平谷区刘家店镇北店村，法定代表人岳清涛）。来源：https://shuidi.cn/company-f05aa0cc90ce7182545942cd51f6656b.html
  - 结论：该名称不能确认为农机合作社，报告中不宜作为农机案例使用。

### 5. 大兴/顺义/房山/平谷其他农机合作社线索
- 平谷：北京绿谷达丰农机服务专业合作社（成立2008-02-25，平谷区夏各庄镇夏各庄村，注册资本100万元，经营范围含整地等）。来源：https://www.liepin.com/company/gs37576779/
- 平谷：曾有「平谷农机合作联社」报道（《中国农民合作社》2011年第10期）。来源：https://www.cnki.com.cn/Article/CJFDTotal-ZGNM201110032.htm
- 房山：北京金利农机服务专业合作社（爱企查有工商条目，但未查到服务面积/装备等实质数据）。来源：https://aiqicha.baidu.com/company_detail_30375242383323
- 大兴：**未找到具体农机合作社的服务数据**；查到的是已注销的「北京市大兴区农机服务中心」（事业单位性质）。相关学术研究：硕士学位论文《北京大兴区农机社会化服务模式研究》（2022），https://xuewen.cnki.net/CMFD-1013359307.nh.html
- 通州：北京国胜农机服务专业合作社（企知道条目，无实质数据）：https://qiye.qizhidao.com/company/19973518b72ca9001e5fdea0aa09053f.html

---

## 四、北京市农机补贴、深松、秸秆与禁烧政策

1. **农机购置与应用补贴**：《2024—2026年度北京市农机购置与应用补贴实施方案》（京政农发〔2024〕70号，2024-12-30印发，全市13个涉农区实施）。
   - 机具范围：中央部分20大类35小类75品目；市级单独部分8大类16小类50品目；选10个品目、不超过20个档次为「重点机具」。
   - 补贴比例：中央一般「不超过同档产品上年销售均价的30%」，重点机具提至35%，急需机具（移动式烘干机、履带式拖拉机等）提至40%；市级单补一般不超过35%。
   - 上限：农民年度累计不超过50万元；农业生产经营组织年度累计不超过500万元。
   - 操作方式：「自主购机、定额补贴、先购后补、区级结算、直补到卡（户）」。
   来源（政策原文，页面正文未抓取但链接有效）：https://www.beijing.gov.cn/zhengce/zhengcefagui/202503/t20250325_4044054.html
   来源（政策解读，已核实）：https://nyncj.beijing.gov.cn/nyj/zwgk/zcjd84/543511218/index.html
   - 另有《北京市农业机械报废更新补贴实施方案》：https://www.beijing.gov.cn/zhengce/zhengcefagui/202501/t20250102_3979031.html

2. **深松整地与保护性耕作作业补贴**（现为区级实施，市里给政策/资金框架）：
   - 怀柔区《2024-2025年度智能农机装备助力单产提升及保护性耕作技术推广作业补贴实施方案》政策解读：**卫星平地100元/亩、农机深松整地50元/亩、高质量小麦播种35元/亩、高质量玉米播种35元/亩、丘陵山区玉米收获80元/亩**；对象为区内从事农机作业服务的生产经营主体；限制条件包括「农机深松整地作业每2年对同一地块只补贴1次」「当年同一地块作业只补贴1次」等。来源：https://www.bjhr.gov.cn/zwgk/zcjd2024/202601/t20260104_4397541.html
   - 房山区口径：深松整地50元/亩、秸秆粉碎覆盖还田35元/亩、少免耕播种35元/亩。来源：https://www.bjfsh.gov.cn/ztzx/wqzt/zdlyzwgk/pihss/202204/t20220412_40044406.shtml
   - 市级招标公告口径：农机深松整地每2年对同一地块补贴1次；秸秆粉碎覆盖还田年度同一地块只补贴1次。来源：https://ggzyfw.beijing.gov.cn/jyxxzbjggg/20240108/4293808.html
   - 早期市级方案（2015）：在京郊推广深松整地30万亩、每亩补贴50元。来源：https://www.nongjitong.com/news/2015/372750.html
   - 注：未找到2024-2026年一份覆盖全市、统一金额的「北京市深松整地补贴」单独文件；现行多为区级实施方案，建议引用时注明区级口径。

3. **秸秆综合利用与禁烧**：
   - 综合利用率：北京「秸秆利用率保持稳定在99%以上」，形成「以肥料化为主，秸秆饲料化、基料化、原料化、能源化等多元利用」体系；昌平区建成农业废弃物综合利用站10个，四年处理15.1万吨（人民政协网转载农民日报，2024-04-10）：https://www.rmzxw.com.cn/c/2024-04-10/3522875.shtml
   - 2022年市级口径：「当前全市农作物秸秆综合利用率达到99%以上」；小麦秸秆两种处理方式——直接粉碎还田（肥料化）、打捆离田（牛场垫料、食用菌原料或有机肥）。来源：https://www.bjnews.com.cn/detail/1655206585168969.html 、http://bj.people.com.cn/n2/2022/0616/c82840-35317708.html
   - 区级方案：《北京市大兴区秸秆类废弃物综合利用行动方案（2023-2025年）》（京兴政农发〔2023〕29号），含「秸秆类废弃物利用现状、发展思路与目标、主要任务、重点支持内容」等章节（正文为附件/一图读懂，网页仅目录）。来源：https://www.bjdx.gov.cn/bjsdxqrmzf/zwfw/zfwj67/1380045/2032853/index.html
   - 禁烧：《京津冀及周边地区秸秆综合利用和禁烧工作方案（2014—2015年）》要求北京、天津、河北等推进综合利用与禁烧；北京多年要求「全面禁烧」，并有「连续三年卫星监测零火点」的报道。来源：https://www.chinacoop.gov.cn/news.html?aid=851249 、https://m.ixigua.com/video/6543025202949784067
   - **未找到2024-2026年新发布的北京市级「秸秆禁烧」专门文件全文**，建议引用《北京市农业机械化提升行动实施方案》中「秸秆基本实现全量化综合利用」和上述利用率报道。

---

## 五、农机合作社发展中的共性问题

主要公开调研/评论来源（内容较具体的两篇）：
- 《纾解农机合作社发展"四大难题"迫在眉睫！》（搜狐，2019，转载行业媒体）把问题概括为：「资金筹措难、不少补贴兑现难、人才队伍培养难、经济纯收入增加难」。
  - 资金/融资难：购机、建库棚、垫付作业费、流转或托管土地都缺资金；缺少抵押物，「大型机具抵押普遍未落实」，正规贷款不易；举例某产粮大县数家较大合作社因担保方出问题贷款落空，上千公顷流转费无法支付。
  - 补贴兑现难：「有的地方不仅当年不能得到兑现，甚至三年前实施的作业补贴，到现在还一直没有兑现」，一般涉及几十万元，有的近百万元。
  - 人才/机手老龄化：「农机合作社机手队伍老龄化严重，人员流动性差，缺乏必要的专项技术培训，农机操作作业水平参差不齐」，有的社没人会用电子信箱、账目也不规范。
  - 盈利难：规模扩大但利润低、负债多，「大部分处于亏损或持平的经营状况。赢利能力普遍不强」，现金流紧张。
  - 规模背景：文中称「目前，我国农机合作社已发展到7万家」；**未提供具体调查样本或官方统计数据**。
  来源：https://www.sohu.com/a/329322522_651395
- 同类观点：「调研中发现的普遍现象是，农机合作社机手队伍老化严重，人员稳定性差，缺乏必要的专项技术培训，农机操作水平参差不齐」。来源：https://www.toutiao.com/article/6723133538117353998/
- **土地细碎化、装备利用率低、维修能力弱、服务价格竞争、融资难**等：在上述两篇中有「融资难、机手老龄化、盈利难」的直接论述；**「装备利用率低」「维修能力弱」「服务价格竞争」「土地细碎化」的专门量化调研数据未找到公开资料**。可参考的学术/行业资料：
  - 《北京市蔬菜产业农机社会化服务组织发展现状及对策》（360文库，无稳定直链）
  - 《北京大兴区农机社会化服务模式研究》硕士论文：https://xuewen.cnki.net/CMFD-1013359307.nh.html
  - 《农村人口老龄化对农机社会化服务的影响》（龙源期刊，2024）：https://www.qikan.com.cn/article/5dd020240246.html
- 一个侧面佐证（京郊现实约束）：顺义合作社因「北京的麦田逐渐减少，合作社的农机出现了‘吃不饱’的状况」，被迫从种收转向秸秆综合利用。来源：http://www.nongji1688.com/news/201607/11/5508819.html

---

## 六、写作时可用的关键数字速查

| 项目 | 数值 | 年份/口径 | 来源 |
|---|---|---|---|
| 北京农机总动力目标 | 稳定在120万千瓦左右 | 2025目标 | njhs.moa.gov.cn 方案 |
| 北京耕种收综合机械化率目标 | 75%以上 | 2025目标 | 同上 |
| 北京设施农业机械化率目标 | 55%以上 | 2025目标 | 同上 |
| 北京大田粮食作物综合机械化率 | 超90% | 2026年5月报道 | nercita.org.cn |
| 北京农作物耕种收综合机械化水平 | 突破79%；粮食作物86%以上 | 2022年11月报道（未直接打开，待核） | news.qq.com |
| 北京秸秆综合利用率 | 99%以上 | 2022、2024报道 | bjnews / rmzxw |
| 全国耕种收综合机械化率 | 75.64% | 2024 | 2024全国农机化统计公报 |
| 顺义三夏服务主体 | 16家农机合作社和农机大户 | 2022 | moa.gov.cn |
| 兴农天力规模 | 社员365户、流转1.2万亩、农机资产3000余万、280余台件 | 2021/2022 | sohu / moa.gov.cn |
| 山东托管面积 | 近2.5亿亩次 | 2024 | 齐鲁网 |
| 黑龙江全程托管 | 2021超2000万亩；2022超3000万亩 | 2021/2022 | farmer.com.cn / 人民网 |

## 七、明确「未找到公开资料」的项
1. 北京市2023-2025年官方「实际」农作物耕种收综合机械化率、农机总动力年末实际值。
2. 京郊（全市）农机社会化服务组织数量、农业生产托管服务面积。
3. 北京市鑫利农机服务专业合作社的服务面积、装备总台套数、确切注册资本（各来源冲突）。
4. 北京绿谷汇德作为「农机合作社」的任何资料（仅有果品合作社与农业科技公司）。
5. 大兴/房山具体农机合作社的服务面积、装备、经营模式数据。
6. 农机合作社「装备利用率低」「维修能力弱」「服务价格竞争」「土地细碎化」的专门量化调研数据（仅有定性论述与学术论文线索）。
