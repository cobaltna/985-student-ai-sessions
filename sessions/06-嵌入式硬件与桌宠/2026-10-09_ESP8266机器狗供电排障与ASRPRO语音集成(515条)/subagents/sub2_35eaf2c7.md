# 子代理会话 sess_subagent_agent_7926cc5f-d529-40c8-b899-8e1835eaf2c7

模型: deepseek-v4.1-flash

## 👤 用户（2026-10-16 20:36）

我需要你调研「天问五幺 ASRPRO 2.0 / ASRPRO-4M」离线语音识别开发板的**官方教程和示例代码**，重点是它与外部单片机（如 ESP8266）通过 UART 串口通信的用法。请用 WebFetch/WebSearch 访问官方网站与文档。

需要确认的具体问题（逐条给出答案 + 来源 URL）：

1. 天问Block（twen51 图形化 IDE）里，做「语音识别 → 串口发送」的积木块叫什么名字？在积木分类的哪个位置？发送字符串时"添加换行"选项的作用和默认状态？
2. ASRPRO 的 UART1（TX=PA2/RX=PA3）和 UART2（TX=PA5/RX=PA6）在天问Block 里怎么选？默认波特率是多少（9600？）？能否改成 115200？
3. 天问Block 编译/下载流程：是否需要登录、是否需要联网生成语音模型、生成模型大概耗时、"编译"和"下载"按钮的区别、串口下载的步骤（长按下载按钮2秒？）。
4. 唤醒词和命令词怎么配置？词条数量限制？"命令词"和"唤醒词"在图形块里的写法（例如"当识别到【命令词】时执行"）。是否支持自定义词条 / 拼音输入 / 方言？
5. 官方有没有提供 ASRPRO 与 Arduino/ESP32/ESP8266 通信的示例工程或教程文章？如果有，给出链接和核心做法。
6. 天问Block 是否有官方在线文档站（如 wiki / docs 域名）？给出首页 URL 和"串口通信"相关页面的 URL。
7. 是否有 ASRPRO 的"入门模式"（免编程模式）说明？入口在哪？

搜索建议关键词：「天问Block 教程」「ASRPRO 串口发送」「ASRPRO UART 通信」「twen51 ASRPRO 官方文档」「天问五幺 ASRPRO 2.0 教程」「ASRPRO 与 Arduino 串口」「asrpro wiki」。

注意：
- 官方网站可能是 twen51.com、twen51.cn、wiki.twen51.com、docs.twen51.com 之类，请自行确认真实域名。
- 站内论坛/文档可能是动态页面，WebFetch 可能失败，失败就换其他来源（CSDN、B站文档、gitee/github 上的开源例程），但必须标注来源并说明可信度。
- 不要编造。找不到就明确说"未找到"。
- 中文内容请用中文回答。

输出格式：按上面 7 个问题分条回答，每条给出「结论 + 来源 URL + 可信度(高/中/低)」。最后附一段「官方示例如有则摘录核心积木/代码片段」。不要写与问题无关的内容。

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Let me start by researching this. I'll use WebFetch to try official domains first. Let me try several in parallel.

Let me check if WebSearch is available... The tools list doesn't include WebSearch explicitly, but the task says use WebFetch/WebSearch. I only have WebFetch. Let me use WebFetch on likely URLs.

Let me try:
- https://www.twen51.com
- https://twen51.com
- https://wiki.twen51.com
- https://docs.twen51.com

Let me do a few parallel fetches.

</details>

- 🔧 **WebFetch** `{"prompt": "这是什么网站？请列出首页导航、主要栏目、以及是否提到 ASRPRO、天问Block IDE、教程/文档/串口通信相关内容。给出看到的所有链接。", "url": "https://www.twen51.com"}` → ``

- 🔧 **WebFetch** `{"prompt": "这是什么网站？列出首页导航和主要栏目，是否提到 ASRPRO、天问Block、教程、文档、串口通信。给出所有链接。", "url": "https://wiki.twen51.com"}` → ``

- 🔧 **WebFetch** `{"prompt": "这是什么网站？列出导航栏目和相关链接，是否涉及 ASRPRO 语音识别、天问Block、串口通信。", "url": "https://docs.twen51.com"}` → ``

- 🔧 **WebFetch** `{"prompt": "这个网站是什么？主要栏目有哪些？是否与天问五幺、ASRPRO、天问Block相关？", "url": "https://twen51.cn"}` → ``

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:36）

I'll research the official 天问五幺 ASRPRO resources. Let me start by probing the likely official domains.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Interesting: www.twen51.com resolves but cert is for haohaodada.com / www.haohaodada.com. That means twen51.com points to the same server as haohaodada.com (好好搭搭). Let me try haohaodada.com. Also try www.twen51.com with http? WebFetch upgrades to https. Let me try haohaodada.com.

Also try twen51.com without www. And search.

</details>

- 🔧 **WebFetch** `{"prompt": "这是什么网站？列出首页所有栏目和导航链接，是否提到天问Block、ASRPRO、教程、文档、下载、串口通信？给出完整 URL 列表。", "url": "https://www.haohaodada.com"}` → `这是一个名为“好好搭搭在线”的创客/编程教育网站。首页栏目和导航链接包括：首页、创作、发现、课程、拍客、赛事、学校（含我的学校、我的班级、课堂作业）、产品、登录、注册，以及精选专题、近期活动、作品天地、公开课等板块。 **是否提到天问Block、ASRPRO、教程、文档、下载、串口通信？** - 天问Block：未提到 - ASRPRO：未提到 - 教程：未直接出现“教程”字样，但有“课程”栏目 - 文档：未提到 - 下载：未提到 - 串口通信：未提到 **完整 URL 列表：** - https://domain/new/index.php - https://domain/new/adminmoban.php - https:/ …[截断,原长4394]`

- 🔧 **WebFetch** `{"prompt": "这个网站是什么？列出主要栏目和链接，是否与天问五幺、ASRPRO、天问Block、离线语音识别相关？", "url": "https://twen51.com"}` → ``

- 🔧 **WebFetch** `{"prompt": "这个 wiki 首页有哪些内容？列出所有导航栏目、页面链接，是否包含 ASRPRO、天问Block、串口通信、UART 相关页面？", "url": "https://haohaodada.com/wiki"}` → `The server returned HTTP 404 Not Found. The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.`

- 🔧 **WebFetch** `{"prompt": "搜索\"天问Block ASRPRO 串口 教程\"，列出所有结果的标题、URL 和摘要，尤其是官方站(twen51/haohaodada)以及 CSDN、B站、gitee 上的内容。", "url": "https://www.bing.com/search?q=%E5%A4%A9%E9%97%AEBlock+ASRPRO+%E4%B8%B2%E5%8F%A3+%E6%95%99%E7%A8%8B"}` → `REDIRECT DETECTED: The URL redirects to a different host. Original URL: https://www.bing.com/search?q=%E5%A4%A9%E9%97%AEBlock+ASRPRO+%E4%B8%B2%E5%8F%A3+%E6%95%99%E7%A8%8B Redirect URL: https://cn.bing.com/search?q=%E5%A4%A9%E9%97%AEBlock+ASRPRO+%E4%B8%B2%E5%8F%A3+%E6%95%99%E7%A8%8B Status: 302 Found To complete your re …[截断,原长634]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:36）

Interesting — twen51.com resolves to the same host as haohaodada.com (好好搭搭). Let me follow that lead.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

haohaodada.com is the "好好搭搭" site but not the ASRPRO one. Let me search. The real domain might be "twen51.com" which resolves to haohaodada IP. Actually the cert altname covers haohaodada.com — so twen51.com is likely an alias hosted on same server. Let me try cn.bing.com search and also try www.twen51.com with different approach.

Let me do web searches.

</details>

- 🔧 **WebFetch** `{"prompt": "列出所有搜索结果的标题、URL 和摘要，尤其是官方站(twen51/haohaodada/twen51.cn)以及 CSDN、B站、gitee 上的内容。注明哪些是官网文档。", "url": "https://cn.bing.com/search?q=%E5%A4%A9%E9%97%AEBlock+ASRPRO+%E4%B8%B2%E5%8F%A3+%E6%95%99%E7%A8%8B"}` → `根据提供的搜索结果页面，没有任何结果与“天问Block ASRPRO 串口 教程”相关，也没有 twen51/haohaodada/twen51.cn、CSDN、B站或 gitee 的内容。所有结果都是关于汉字“天”的字典/百科页面。 搜索结果列表（标题、URL、摘要）： 1. **天（汉语文字）_百度百科** - URL: https://baike.baidu.com/item/%E5%A4%A9/34055 - 摘要：“天，汉语通用规范一级字（常用字），读作tiān。 指事字（一说象形字，一说会意字）。 最早见于甲骨文，像正面站着的“人”形，用方 …” 2. **天 tiān - 汉典** - URL: https://www …[截断,原长1751]`

- 🔧 **WebFetch** `{"prompt": "列出所有搜索结果的标题、URL 和摘要，重点找天问五幺/天问Block 官网域名 (twen51) 和 ASRPRO 官方文档/wiki 地址。", "url": "https://cn.bing.com/search?q=%E5%A4%A9%E9%97%AE%E4%BA%94%E5%B9%BA+ASRPRO+%E5%AE%98%E6%96%B9+wiki+%E6%96%87%E6%A1%A3"}` → `根据提供的页面内容，**没有找到任何天问五幺/天问Block 官网域名 (twen51) 或 ASRPRO 官方文档/wiki 地址**。该页面实际是搜索引擎结果页，查询词虽为“天问五幺 ASRPRO 官方 wiki 文档”，但返回的结果全部是“天”这个汉字的字典释义，与 ASRPRO 或天问五幺无关。 以下是所有搜索结果的标题、URL 和摘要： 1. **天（汉语文字）_百度百科** - URL: https://baike.baidu.com/item/%E5%A4%A9/34055 - 摘要: “天，汉语通用规范一级字（常用字），读作tiān。 指事字（一说象形字，一说会意字）。 最早见于甲骨文…” 2. **天 tiān - …[截断,原长1566]`

- 🔧 **WebFetch** `{"prompt": "这个网站是什么？列出导航和链接，是否有 ASRPRO、天问Block、教程、串口、下载内容？", "url": "https://www.twen51.cn"}` → ``

- 🔧 **WebFetch** `{"prompt": "这个网站是什么？列出导航栏目和链接，是否与天问五幺 ASRPRO 语音识别开发板相关？", "url": "http://twen51.com"}` → ``

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:37）

Let me search via Bing and probe other likely domains.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Bing search results got hijacked/not useful (returning dictionary results). Let me try other search engines and known wiki domains. ASRPRO docs might be at "www.twen51.com" official. Let me try duckduckgo, and try known domains like "asrpro.twen51.com", "twen51.com/wiki", "wiki.haohaodada.com", "docs.haohaodada.com".

Also I recall ASRPRO related: "天问Block" download site. The official site may be "www.haohaodada.com" (好好搭搭) which is the company 杭州好好搭搭. Their ASRPRO product docs might be at "http://www.haohaodada.com/new/..." Actually the twen51.com cert being haohaodada suggests twen51.com is a CNAME alias for haohaodada.com. So twen51.com IS the official site but serves haohaodada's cert (misconfigured). Let me try http (not https) for www.twen51.com browsing via a different approach, or try curl.

Let me try curl through Bash to check domains. But sandbox network may be restricted. Let me try WebFetch on other likely URLs.

Known: 天问Block official site might be "https://www.twen51.com" but cert mismatch. Since WebFetch upgrades HTTP to HTTPS, that breaks. Hmm. Let me try curl in bash.

Actually the env - network access from bash may be sandboxed. Let's test.

Let me also try search engines: duckduckgo html, sogou, baidu.

Let me do a batch.

</details>

- 🔧 **Bash** `{"command": "for h in twen51.com www.twen51.com twen51.cn www.twen51.cn wiki.twen51.com docs.twen51.com haohaodada.com www.haohaodada.com wiki.haohaodada.com docs.haohaodada.com asrpro.twen51.com; do echo \"=== $h ===\"; curl -s -I -m 10 \"http://$h\" 2>&1 | head -5; done", "description": "Probe candidate domains via curl"}` → `=== twen51.com === HTTP/1.1 302 Found Date: Fri, 16 Oct 2026 12:37:28 GMT Server: Apache Location: /new/twen51/index.php Connection: close === www.twen51.com === HTTP/1.1 302 Found Date: Fri, 16 Oct 2026 12:37:28 GMT Server: Apache Location: /new/twen51/index.php Connection: close === twen51.cn === === www.twen51.cn == …[截断,原长727]`

- 🔧 **WebFetch** `{"prompt": "列出所有搜索结果的标题、URL 和摘要。要找天问五幺 ASRPRO 官方文档、天问Block 教程、串口通信。", "url": "https://html.duckduckgo.com/html/?q=%E5%A4%A9%E9%97%AEBlock+ASRPRO+%E4%B8%B2%E5%8F%A3%E9%80%9A%E4%BF%A1+%E6%95%99%E7%A8%8B"}` → ``

- 🔧 **WebFetch** `{"prompt": "列出所有搜索结果的标题、URL、摘要，找天问Block ASRPRO 官方文档/wiki/教程。", "url": "https://html.duckduckgo.com/html/?q=ASRPRO+%E5%A4%A9%E9%97%AEBlock+%E5%AE%98%E6%96%B9+wiki"}` → ``

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:37）

Bing results were useless (dictionary noise). Let me try other search engines and check domains via curl.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

twen51.com redirects to /new/twen51/index.php. Let me fetch that. Also try DuckDuckGo lite via curl.

</details>

- 🔧 **WebFetch** `{"prompt": "这是天问五幺官网首页。列出所有导航栏目、菜单和链接（含完整 URL），特别是：教程、文档、下载、资料、ASRPRO、天问Block、串口通信相关。给出完整 URL 列表。", "url": "https://twen51.com/new/twen51/index.php"}` → ``

- 🔧 **Bash** `{"command": "curl -s -L -m 25 \"https://lite.duckduckgo.com/lite/?q=ASRPRO%20%E5%A4%A9%E9%97%AEBlock%20%E4%B8%B2%E5%8F%A3\" 2>&1 | grep -oE 'https?://[^\"<> ]+' | grep -viE 'duckduckgo|\\.css|\\.js|\\.png|\\.ico' | sort -u | head -60", "description": "DuckDuckGo lite search via curl"}` → `(Bash completed with no output)`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:37）

twen51.com is real and redirects to `/new/twen51/index.php`. Let me explore it.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

HTTPS fails cert. Use http:// via WebFetch — but WebFetch upgrades HTTP to HTTPS. So use curl instead to fetch content.

Let me curl the twen51 page.

</details>

- 🔧 **Bash** `{"command": "curl -s -L -m 25 \"http://twen51.com/new/twen51/index.php\" -o /tmp/twen51.html 2>&1; echo \"size: $(wc -c < /tmp/twen51.html)\"; file /tmp/twen51.html; python -c \"print(open('/tmp/twen51.html','rb').read()[:500])\" 2>/dev/null || head -c 500 /tmp/twen51.html", "description": "Fetch twen51 homepage via curl"}` → `size: 56871 /tmp/twen51.html: HTML document, Unicode text, UTF-8 text, with very long lines (675) <!DOCTYPE html> <html lang="zh-cn" class="m-page m-page-view"> <head> <meta charset="utf-8"> <!-- <meta name="description" itemprop="description" content="澶╅棶Block 鍗曠墖鏈哄紑鍙戝埄鍣�锛屾敮鎸丼TC鍏ㄧ郴鍒�8浣嶅崟鐗囨満锛�32浣岮RM鍜孯ISC-V鍐呮牳銆�"/> -->  …[截断,原长467]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:38）

HTTPS cert mismatch. Let me fetch via curl over http.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The page is UTF-8 but the encoding got mangled — actually it's GBK bytes interpreted... no, it says UTF-8 but the Chinese is garbled (UTF-8 bytes of GBK?). Actually the content shows mojibake where UTF-8 decoded as latin - typical of the bytes being UTF-8 but terminal showing... Let me just extract links and read with Read tool. Actually better: use python to parse. Let me grep for hrefs.

</details>

- 🔧 **Bash** `{"command": "python -c \"\nimport re\nd=open('/tmp/twen51.html','rb').read().decode('utf-8',errors='replace')\nlinks=re.findall(r'href=[\\\"\\']([^\\\"\\']+)[\\\"\\']',d)\nseen=[]\nfor l in links:\n if l not in seen: seen.append(l)\nfor l in seen: print(l)\n\" 2>&1 | head -80", "description": "Extract links from twen51 homepage"}` → `/usr/bin/bash: line 3: python: command not found`

- 🔧 **Bash** `{"command": "python -c \"\nimport re\nd=open('/tmp/twen51.html','rb').read()\ntry:\n t=d.decode('utf-8')\nexcept: t=d.decode('gbk',errors='replace')\n# print visible text\nt2=re.sub(r'<script.*?</script>','',t,flags=re.S)\nt2=re.sub(r'<style.*?</style>','',t2,flags=re.S)\nt2=re.sub(r'<[^>]+>',' ',t2)\nt2=re.sub(r'\\s+',' ',t2)\nprint(t2[:4000])\n\"", "description": "Extract vis …[截断,原长409]` → `Exit code 127 /usr/bin/bash: line 3: python: command not found`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

No python in bash PATH. Use node or grep. Let me use grep/sed... but AGENTS says avoid. I'll use node.

Actually let me use the Read tool on the file after processing. Simpler: use grep -oE.

Let me just use node.

</details>

- 🔧 **Bash** `{"command": "node -e \"\nconst fs=require('fs');\nconst d=fs.readFileSync('/tmp/twen51.html','utf8');\nconst links=[...d.matchAll(/href=[\\\"']([^\\\"']+)[\\\"']/g)].map(m=>m[1]);\nconsole.log([...new Set(links)].join('\\n'));\n\"", "description": "Extract links with node"}` → `Exit code 1 node:fs:439 return binding.readFileUtf8(path, stringToFlags(options.flag)); ^ Error: ENOENT: no such file or directory, open 'C:\tmp\twen51.html' at Object.readFileSync (node:fs:439:20) at [eval]:3:12 at runScriptInThisContext (node:internal/vm:219:10) at node:internal/process/execution:451:12 at [eval]-wra …[截断,原长643]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Path issue: /tmp is not real. Let me use a working dir. Use $TEMP or the cwd. Let me write to the working dir.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && curl -s -L -m 25 \"http://twen51.com/new/twen51/index.php\" -o twen51.html && ls -la twen51.html && node -e \"\nconst fs=require('fs');\nconst d=fs.readFileSync('twen51.html','utf8');\nconst links=[...d.matchAll(/href=[\\\"']([^\\\"']+)[\\\"']/g)].map(m=>m[1]);\nconsole.log([...new Set(links)].filter …[截断,原长414]` → `-rw-r--r-- 1 user 197121 56871 Oct 16 20:38 twen51.html static/images/favicon.ico static/css/min.css static/css/style.css static/css/default_wide_zh-cn.css static/css/initial.css static/css/bootstrap_3.3.1.css static/css/index.css static/css/paging.css static/css/iconfont.css static/css/public_model.css static/css/rese …[截断,原长1111]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Found: learnSource.php?id=68, art_show.php?id=230, forum fid=80, and a twenBlock.zip download. Let me read the visible text and explore these pages. Let me fetch learnSource.php?id=68 and art_show.php?id=230 and the forum.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && node -e \"\nconst fs=require('fs');\nconst d=fs.readFileSync('twen51.html','utf8');\nlet t=d.replace(/<script[\\s\\S]*?<\\/script>/g,'').replace(/<style[\\s\\S]*?<\\/style>/g,'');\nt=t.replace(/<[^>]+>/g,' ').replace(/&nbsp;/g,' ').replace(/\\s+/g,' ');\nconsole.log(t.slice(0,5000));\n\"", "descripti …[截断,原长413]` → ` --> --> --> 天问五幺官网 - 一站式单片机开发 天问五幺官网 - 一站式单片机开发 --> --> 首页 在线编程 发现 课程 学校 我的学校 我的班级 课堂作业 资料 软件 社区 登录 注册 --> 个人资料 班级管理 --> 登录 LOGIN 手机号码: * --> 验证码: 登录 登录 忘记密码 --> 忘记密码 手机号登录 免费注册 注册 REGIST 注册 当前位置： 首页 天问Block 天问Block 单片机开发利器，支持STC全系列单片机，STC89/90、STC12 系列、STC15 系列、STC8 系列，STC16 系列，后续...支持所有国产芯片--51、32、RISC-V。 --> 天问Bloc …[截断,原长1777]`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && for u in \"learnSource.php?id=68\" \"art_show.php?id=230\" \"course.php\" \"display_code.php\"; do echo \"=== $u ===\"; curl -s -L -m 20 \"http://twen51.com/new/twen51/$u\" -o \"t_$(echo $u|tr '?=&' '___').html\"; ls -la \"t_$(echo $u|tr '?=&' '___').html\"; done", "description": "Fetch key twen51 pa …[截断,原长385]` → `=== learnSource.php?id=68 === -rw-r--r-- 1 user 197121 46897 Oct 16 20:39 t_learnSource.php_id_68.html === art_show.php?id=230 === -rw-r--r-- 1 user 197121 50114 Oct 16 20:39 t_art_show.php_id_230.html === course.php === -rw-r--r-- 1 user 197121 27524 Oct 16 20:39 t_course.php.html === display_code.php === -rw-r--r-- 1 …[截断,原长375]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:38）

Found the real site. Let me explore its key pages.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Let me set up a todo list and continue exploring. I found the official site is twen51.com (杭州天问五幺科技有限公司). Let me explore the "资料" (resources) page which likely has tutorials, and find ASRPRO pages.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "确认官网域名并抓取首页/资料/课程栏目结构", "status": "in_progress", "priority": "high"}, {"content": "定位天问Block 教程/文档与 ASRPRO 专页(wiki/docs)", "status": "pending", "priority": "high"}, {"content": "查证串口发送积木名称、UART1/2、波特率", "status": "pending", "priority": "high"}, {"content": "查证编译下载流程、词条配置、入门模式", "status": "pending", "priority": "high"}, {"content": "查找 ASRPRO 与 Arduino/ES …[截断,原长412]` → `{"oldTodos":[],"todos":[{"content":"确认官网域名并抓取首页/资料/课程栏目结构","status":"in_progress","priority":"high"},{"content":"定位天问Block 教程/文档与 ASRPRO 专页(wiki/docs)","status":"pending","priority":"high"},{"content":"查证串口发送积木名称、UART1/2、波特率","status":"pending","priority":"high"},{"content":"查证编译下载流程、词条配置、入门模式","status":"pending","prio …[截断,原长550]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Let me look at the fetched pages, and search for ASRPRO-specific pages. The site uses IDs. Let me search the site for ASRPRO. Let me look at learnSource.php and the 资料 (resource) page, and try to find a wiki.

Let me dump text of learnSource.php?id=68 (可能是天问Block离线版软件介绍) and look for ASRPRO related pages via search on the site. Let me also check the forum.

Actually there may be a dedicated ASRPRO docs site. Let me search. The homepage mentioned "天问Block离线版软件介绍" linking to learnSource.php?id=68 maybe.

Let me grep the downloaded pages for "ASRPRO" and for URLs.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && for f in t_learnSource.php_id_68.html t_art_show.php_id_230.html t_course.php.html t_display_code.php.html; do echo \"=== $f ===\"; node -e \"\nconst fs=require('fs');const d=fs.readFileSync('$f','utf8');\nlet t=d.replace(/<script[\\s\\S]*?<\\/script>/g,'').replace(/<style[\\s\\S]*?<\\/style>/g,'').r …[截断,原长414]` → `=== t_learnSource.php_id_68.html === --> --> --> 天问五幺官网 - 一站式单片机开发 首页 在线编程 发现 课程 学校 我的学校 我的班级 课堂作业 资料 软件 社区 登录 注册 --> 个人资料 班级管理 --> 登录 LOGIN 手机号码: * --> 验证码: 登录 登录 忘记密码 --> 忘记密码 手机号登录 免费注册 注册 REGIST 注册 当前位置： 首页 天问Block ASRPRO学习资料专区 天问51开发板 ASRPRO ASRPRO ASRPRO语音芯片内置脑神经网络处理器，支持DNN、TDNN、RNN等神经网络及卷积运算硬件运算，非软件运算，支持语音识别、声纹识 …[截断,原长5235]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Excellent. Found the ASRPRO learning resource page (learnSource.php?id=68). There are official 例程 (official examples) with 223 items over 28 pages, including "专业 编程-1-1.智能语音对话". Let me find the ASRPRO official examples listing, and importantly the 串口 examples. Also there's a 资料 页面 (资料栏目) which may link to documentation/wiki.

Let me look for:
1. The 资料 (resources) page - probably "learnSource.php"
2. ASRPRO official examples list
3. Wiki/docs - maybe on haohaodada bbs forum

Let me get all links from learnSource page.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && node -e \"\nconst fs=require('fs');const d=fs.readFileSync('t_learnSource.php_id_68.html','utf8');\nconst links=[...d.matchAll(/href=[\\\"']([^\\\"']+)[\\\"']/g)].map(m=>m[1]);\nconsole.log([...new Set(links)].filter(l=>!/\\.(css|js|png|jpg|ico)/.test(l)).join('\\n'));\n\"", "description": "Extract l …[截断,原长414]` → `index.php adminmoban.php display_code.php course.php school_list.php my_school_list.php my_class_list.php user_taskWork_list.php learnSource.php?id=68 art_show.php?id=230 http://www.haohaodada.com/new/bbs/forum.php?mod=forumdisplay&fid=80 # school_newMessageNotice.php userpwdchang.php ./ learnSource.php?id=65 course_pl …[截断,原长1640]`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && for u in \"learnSource.php\" \"video.php\" \"software.php\"; do echo \"=== $u ===\"; curl -s -L -m 20 \"http://twen51.com/new/twen51/$u\" -o \"x_$u.html\"; node -e \"\nconst fs=require('fs');const d=fs.readFileSync('x_$u.html','utf8');\nlet t=d.replace(/<script[\\s\\S]*?<\\/script>/g,'').replace(/<st …[截断,原长414]` → `=== learnSource.php === 参数id错误！ --- LINKS --- === video.php === 404 Not Found 返回主页 --> 404 - 页面未找到 404 哎呀，页面迷路啦！ 你访问的页面不存在、已被删除或地址输入错误 返回首页 联系客服 --- LINKS --- /new/ / mailto:<邮箱> === software.php === 404 Not Found 返回主页 --> 404 - 页面未找到 404 哎呀，页面迷路啦！ 你访问的页面不存在、已被删除或地址输入错误 返回首页 联系客服 --- LINKS --- /new/ / mailto:<邮箱>`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:39）

Found the ASRPRO resource hub. Let me extract all its links and find the official examples and docs.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Key findings:
- `https://dolphin666.github.io/docs/#/` — a docs site! Possibly the official wiki.
- `Arduino_example.php?href=asr_pro` — Arduino example page!
- `/C51/asr_pro_e.php?new` — ASRPRO 在线编程 (入门模式?)
- `coursePlayCloud.php?id=24` and `id=29` — video courses
- `learning_show.php?id=...` — learning materials

Let me fetch these. Note the site is http://twen51.com/new/twen51/ and also haohaodada.com/new/... Paths like `/C51/asr_pro_e.php` — relative to root? Let's check both.

Also dolphin666.github.io/docs — likely the official 天问Block docs (语雀 or this). Let me fetch.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && for u in \"Arduino_example.php?href=asr_pro\" \"C51/asr_pro_e.php?new\" \"C51/asr_pro.php?id=97624\" \"learning_show.php?id=564\" \"learning_show.php?id=652\" \"learning_show.php?id=559\" \"learning_show.php?id=565\"; do fn=$(echo \"$u\" | tr '?=&/ ' '____'); echo \"=== $u -> $fn ===\"; curl -s -L -m …[截断,原长414]` → `=== Arduino_example.php?href=asr_pro -> Arduino_example.php_href_asr_pro === -rw-r--r-- 1 user 197121 37213 Oct 16 20:39 y_Arduino_example.php_href_asr_pro.html === C51/asr_pro_e.php?new -> C51_asr_pro_e.php_new === -rw-r--r-- 1 user 197121 2267 Oct 16 20:39 y_C51_asr_pro_e.php_new.html === C51/asr_pro.php?id=97624 ->  …[截断,原长972]`

- 🔧 **WebFetch** `{"prompt": "这是什么文档站？列出首页所有导航条目和链接，是否包含天问Block、ASRPRO、串口通信、UART、词条配置相关内容？给出完整 URL 列表。", "url": "https://dolphin666.github.io/docs/"}` → `该页面仅显示“天问51 API文档”和“加载中...”，没有列出任何导航条目、链接或具体主题内容。因此无法确认是否包含天问Block、ASRPRO、串口通信、UART或词条配置相关内容，也无法给出完整 URL 列表。`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:39）

Excellent finds — a docs site, an Arduino example page, and an online-programming page. Let me fetch them all.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The docs site is a JS SPA (docsify). Let me look at the learning pages and the Arduino example page content.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && for f in y_Arduino_example.php_href_asr_pro.html y_C51_asr_pro_e.php_new.html y_learning_show.php_id_564.html y_learning_show.php_id_652.html y_learning_show.php_id_565.html; do echo \"======== $f ========\"; node -e \"\nconst fs=require('fs');const d=fs.readFileSync('$f','utf8');\nlet t=d.replace(/< …[截断,原长414]` → `======== y_Arduino_example.php_href_asr_pro.html ======== --> --> --> 天问五幺官网 - 一站式单片机开发 首页 在线编程 发现 课程 学校 我的学校 我的班级 课堂作业 资料 软件 社区 登录 注册 --> 个人资料 班级管理 --> 登录 LOGIN 手机号码: * --> 验证码: 登录 登录 忘记密码 --> 忘记密码 手机号登录 免费注册 注册 REGIST 注册 当前位置： 首页 天问Block ASRPRO(例程) 案例类别 全部案例 --> 例程选择 ASRPRO 全部项目 --> 徽章板 好搭酷-mini 好搭酷-nano 好搭Bit Nano实验 …[截断,原长5996]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:39）

The docs site is a docsify SPA. Let me examine the learning pages and Arduino example content.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Excellent — huge finds. There are official Yuque knowledge bases: https://www.yuque.com/twen51/asrpro and https://www.yuque.com/twen51/twblock. Also an ASRPRO resource download page with 串口范例 (serial examples) and PDF manuals. The "ASRPRO资料下载" page (learning_show.php?id=565) has download links — let me extract them.

Let me extract links from those pages (the PDF/zip downloads, the yuque links, the video course links).

Also the Arduino_example.php page has a case category list. There's a category "Arduino开源硬件" and "ASRPRO". The Arduino example page is for the online program display; there might be ASRPRO examples with Arduino code.

Let me extract links from learning_show.php?id=565 (ASRPRO资料下载) and the Arduino example page, and also fetch the yuque ASRPRO knowledge base.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && node -e \"\nconst fs=require('fs');const d=fs.readFileSync('y_learning_show.php_id_565.html','utf8');\nconst links=[...d.matchAll(/href=[\\\"']([^\\\"']+)[\\\"']/g)].map(m=>m[1]);\nconsole.log('=== LINKS (565 ASRPRO资料下载) ===');console.log([...new Set(links)].filter(l=>!/\\.(css|js|png|jpg|ico)\\$/.te …[截断,原长414]` → `=== LINKS (565 ASRPRO资料下载) === index.php adminmoban.php display_code.php course.php school_list.php my_school_list.php my_class_list.php user_taskWork_list.php learnSource.php?id=68 art_show.php?id=230 http://www.haohaodada.com/new/bbs/forum.php?mod=forumdisplay&fid=80 # school_newMessageNotice.php userpwdchang.php ./  …[截断,原长3369]`

- 🔧 **WebFetch** `{"prompt": "这是天问五幺 ASRPRO 语音芯片的官方知识库（语雀）。请列出：1) 文档目录/大纲的所有条目和链接；2) 所有与\"串口\"\"UART\"\"发送\"\"通信\"相关的条目及其链接；3) 所有与\"编译\"\"下载\"\"词条\"\"命令词\"\"唤醒词\"相关的条目及链接。给出完整 URL。", "url": "https://www.yuque.com/twen51/asrpro"}` → `I can’t list those items or provide complete URLs because the only content provided is: “天问ASRPRO · 语雀” The page content does not include the document outline, entry titles, links, or URL paths. Therefore I cannot extract or provide: 1. All目录/大纲条目和链接 2. “串口”“UART”“发送”“通信”相关条目及链接 3. “编译”“下载”“词条”“命令词”“唤醒词”相关条目及链接 If you  …[截断,原长397]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:40）

Major finds: official Yuque knowledge bases and an ASRPRO resource page with 串口范例. Let me extract links and fetch the Yuque ASRPRO knowledge base.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Yuque is JS-rendered. Let me try the Yuque API to get the docs outline. Yuque has an API: https://www.yuque.com/api/v2/repos/twen51/asrpro/docs or the book's "toc". Let me try the public API.

Also let me fetch the ASRPRO example programs (zip) and the Arduino example detail, and the config/programming manual PDFs.

Let me try Yuque API endpoints.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && echo \"=== yuque toc ===\"; curl -s -m 20 \"https://www.yuque.com/api/v2/repos/twen51/asrpro/toc\" -H \"User-Agent: Mozilla/5.0\" | head -c 3000; echo; echo \"=== yuque docs ===\"; curl -s -m 20 \"https://www.yuque.com/api/v2/repos/twen51/asrpro/docs\" -H \"User-Agent: Mozilla/5.0\" | head -c 2000",  …[截断,原长413]` → `=== yuque toc === {"status":401,"message":"Unauthorized"} === yuque docs === {"status":401,"message":"Unauthorized"}`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && for f in \"asr_pro_e_2024.pdf\" \"asr_pro_2024.pdf\"; do curl -s -L -m 40 \"http://twen51.com/new/twen51/jpeguploadfile/twen/ASRPRO/$f\" -o \"dl_$f\"; ls -la \"dl_$f\"; file \"dl_$f\"; done; for z in \"asr_pro_e_2024.zip\" \"asr_pro_2024.zip\"; do curl -s -L -m 60 \"http://twen51.com/new/twen51/jpegu …[截断,原长414]` → `-rw-r--r-- 1 user 197121 2267 Oct 16 20:40 dl_asr_pro_e_2024.pdf dl_asr_pro_e_2024.pdf: HTML document text HTML document, Unicode text, UTF-8 text -rw-r--r-- 1 user 197121 2267 Oct 16 20:40 dl_asr_pro_2024.pdf dl_asr_pro_2024.pdf: HTML document text HTML document, Unicode text, UTF-8 text -rw-r--r-- 1 user 197121 2267  …[截断,原长417]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:40）

The Yuque knowledge base is JS-rendered. Let me try the Yuque API and fetch the official ASRPRO example zips/PDFs.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The download paths are relative to a different root. The links were `/jpeguploadfile/...` so likely `http://twen51.com/jpeguploadfile/twen/ASRPRO/...`. Let me try. Also the zip files are 2267 bytes = 404 page.

Let me try the correct path.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && for base in \"http://twen51.com\" \"http://www.haohaodada.com\" \"http://twen51.com/new/twen51\"; do echo \"=== base=$base ===\"; curl -s -L -m 40 \"$base/jpeguploadfile/twen/ASRPRO/asr_pro_e_2024.pdf\" -o tmp.pdf; ls -la tmp.pdf; file tmp.pdf; done", "description": "Find correct base path for downlo …[截断,原长385]` → `=== base=http://twen51.com === -rw-r--r-- 1 user 197121 12550197 Oct 16 20:40 tmp.pdf tmp.pdf: PDF document, version 1.7 === base=http://www.haohaodada.com === -rw-r--r-- 1 user 197121 12550197 Oct 16 20:40 tmp.pdf tmp.pdf: PDF document, version 1.7 === base=http://twen51.com/new/twen51 === -rw-r--r-- 1 user 197121 226 …[截断,原长410]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The correct base is http://twen51.com/jpeguploadfile/... Let me download the two manuals and the example zips. These are the authoritative sources.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && mkdir -p asrpro && cd asrpro && for f in \"asr_pro_e_2024.pdf\" \"asr_pro_2024.pdf\" \"asr_pro_axiom_doc.pdf\" \"asr_pro_core.pdf\" \"ASRPRO-Plus-Factoryprocedure2024.zip\" \"ASRPRO-CORE.zip\" \"asr_pro_e_2024.zip\" \"asr_pro_2024.zip\"; do curl -s -L -m 90 \"http://twen51.com/jpeguploadfile/twen/ASR …[截断,原长414]` → `asr_pro_e_2024.pdf -> PDF document, version 1.7 12550197 asr_pro_2024.pdf -> PDF document, version 1.7 42473712 asr_pro_axiom_doc.pdf -> PDF document, version 1.7, 2 page(s) 2457263 asr_pro_core.pdf -> PDF document, version 1.7, 129 page(s) 2313407 ASRPRO-Plus-Factoryprocedure2024.zip -> Zip archive data, made by v6.3, …[截断,原长908]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:40）

Got the real download base. Let me download the official manuals and example code archives.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

I have the official manuals and example code. Let me extract the PDFs and zips. Need a PDF text extractor. Let me check what tools are available: conda python, pdftotext? Let me check.

Actually per AGENTS.md, conda python has opencv and docx. Let me find python paths.

Let me first check the zips (example code), those are most important for "串口范例". And extract PDF text with a tool.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && mkdir -p ex_e ex_p core && unzip -o -q asr_pro_e_2024.zip -d ex_e 2>&1 | head; unzip -o -q asr_pro_2024.zip -d ex_p 2>&1 | head; echo \"=== ex_e (配置模式) tree ===\"; find ex_e -maxdepth 3 | head -60; echo \"=== ex_p (编程模式) tree ===\"; find ex_p -maxdepth 2 | head -80", "description": "Extract of …[截断,原长414]` → `=== ex_e (配置模式) tree === ex_e ex_e/asr_pro_e ex_e/asr_pro_e/1.+¨¦íÀÂ+² ex_e/asr_pro_e/1.+¨¦íÀÂ+²/1.ÍÃ-_˴ʶÂÈ+¦.hd ex_e/asr_pro_e/1.+¨¦íÀÂ+²/10.ʲ¢+©¯Áþã¢+ÏÍã¦Ѧ¿.hd ex_e/asr_pro_e/1.+¨¦íÀÂ+²/2.˴ʶ+ÏÍã¦ÕÈÏLED.hd ex_e/asr_pro_e/1.+¨¦íÀÂ+²/3.˴ʶ+ÏÍãÁÑ+¦Áþã¸.hd ex_e/asr_pro_e/1.+¨¦íÀÂ+²/4.˴ʶ+ÏÍã---À+¦Áþã¸.hd ex_e/asr_pro_e/1.+¨ …[截断,原长1551]`

- 🔧 **Bash** `{"command": "ls \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" ; which pdftotext; ls /c/ProgramData/anaconda3/python.exe 2>/dev/null; ls \"/c/Users/UserX/anaconda3/python.exe\" 2>/dev/null; ls /c/Users/UserX/anaconda3/python.exe 2>/dev/null; where.exe python 2>/dev/null", "description": "Locate python and pdftotext"}` → `Exit code 1 EDA-Robot机器狗项目/ asrpro/ dl_asr_pro_2024.pdf dl_asr_pro_2024.zip dl_asr_pro_e_2024.pdf dl_asr_pro_e_2024.zip pkgdoc.txt t_art_show.php_id_230.html t_course.php.html t_display_code.php.html t_learnSource.php_id_68.html tmp.pdf twen51.html x_learnSource.php.html x_software.php.html x_video.php.html y_Arduino_e …[截断,原长597]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:41）

Downloaded the official manuals and example archives. Let me extract them.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The zip filenames are GBK-encoded. pdftotext is available. Let me extract the PDFs and convert filenames. Also the example .hd files - let me look at serial examples (串口范例 = folder "2.串口范例"). The garbled names need GBK decoding.

Let me use python to properly extract and list.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && /c/ProgramData/anaconda3/python.exe -c \"\nimport os,sys\nsys.stdout.reconfigure(encoding='utf-8')\nfor root,d,files in os.walk('ex_p'):\n for fn in files:\n p=os.path.join(root,fn)\n try: nm=p.encode('utf-8','surrogateescape').decode('gbk')\n except: nm=p\n print(nm)\n\"", "descripti …[截断,原长4 …[截断,原长383]` → `ex_p\asr_pro\1.+篓娄铆脌脗+虏\1.脥脙-_舜识脗脠+娄.hd ex_p\asr_pro\1.+篓娄铆脌脗+虏\10.什垄+脕-脕镁茫垄+脧脥茫娄薛驴.hd ex_p\asr_pro\1.+篓娄铆脌脗+虏\11.什垄+漏炉脕镁茫垄+脧脥茫娄薛驴.hd ex_p\asr_pro\1.+篓娄铆脌脗+虏\12.+脻+娄驴-娄茫赂脨脣-娄娄夕i.hd ex_p\asr_pro\1.+篓娄铆脌脗+虏\13.+脻+娄驴-娄茫赂+脧脥茫+--漏.hd ex_p\asr_pro\1.+篓娄铆脌脗+虏\14.PWM+脧脥茫娄脮脠脧脕茫--脗+.hd ex_p\asr_pro\1.+篓娄铆脌脗+虏\15.ADC脗-+铆--脗+娄陆漏冒茫 …[截断,原长3470]`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && pdftotext -enc UTF-8 asr_pro_e_2024.pdf manual_config.txt && pdftotext -enc UTF-8 asr_pro_2024.pdf manual_prog.txt && wc -l manual_config.txt manual_prog.txt", "description": "Convert ASRPRO manuals to text"}` → ` 1107 manual_config.txt 2819 manual_prog.txt 3926 total`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:41）

pdftotext is available and there's conda python. Let me extract the PDFs and fix the GBK filenames.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

This is a goldmine. Let me decode the filenames properly and read the manuals. The filenames are UTF-8 bytes mis-decoded. Let me redo decoding: the raw bytes are actually GBK? Let me handle it correctly. Actually the zip stores names in GBK and unzip decoded as latin1/utf8 wrongly. Let me re-extract with a proper tool (python zipfile with cp936).

Also "编程模式" example folder 3 is 串口范例 (serial examples). Let me extract properly.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\Robot dog 1.1\\_research\\dl\\pkg\\asrpro\\manual_e.txt"}` → ``

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && rm -rf ex_e ex_p && /c/ProgramData/anaconda3/python.exe -c \"\nimport zipfile,os,sys\nsys.stdout.reconfigure(encoding='utf-8')\nfor z,d in [('asr_pro_e_2024.zip','ex_e'),('asr_pro_2024.zip','ex_p')]:\n zf=zipfile.ZipFile(z)\n for n in zf.namelist():\n try: real=n.encode('cp437').decode('gbk')\ …[截断,原长393]` → `done`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:42）

Excellent — official manuals extracted and the 编程模式 examples include a 串口范例 folder. Let me re-extract with correct encoding and read the manuals.

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && /c/ProgramData/anaconda3/python.exe -c \"\nimport os,sys\nsys.stdout.reconfigure(encoding='utf-8')\nfor root,dirs,files in os.walk('ex_p'):\n for fn in files:\n print(os.path.join(root,fn))\n\" | head -100", "description": "List decoded example filenames"}` → `ex_p\asr_pro\1.基础范例\1.智能语音对话.hd ex_p\asr_pro\1.基础范例\10.引脚低电平控制播报.hd ex_p\asr_pro\1.基础范例\11.引脚高电平控制播报.hd ex_p\asr_pro\1.基础范例\12.软件定时器延时关闭.hd ex_p\asr_pro\1.基础范例\13.软件定时器控制闪烁.hd ex_p\asr_pro\1.基础范例\14.PWM控制板载灯亮度.hd ex_p\asr_pro\1.基础范例\15.ADC读取亮度传感器值.hd ex_p\asr_pro\1.基础范例\16.内部存储器保存数据.hd ex_p\asr_pro\1.基础范例\17.英文自定义语音识别. …[截断,原长2692]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

We have official examples including 2.串口范例. The .hd files are 天问Block project files (probably JSON). Let me look at them and the manuals.

Let me read the manuals. First check file size. manual_config.txt and manual_prog.txt were created earlier. Let me grep them for relevant keywords.

Actually those .txt were created before re-extract. They still exist. Let me grep.

Let me use grep for keywords like "串口", "波特率", "UART", "换行", "编译", "下载", "唤醒词", "命令词", "入门模式".

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && ls -la *.txt *.pdf *.zip; echo \"=== 配置模式 manual 结构 ===\"; grep -nE \"第[一二三四五六七八九十]+|目录|^[0-9]+\\.[0-9]\" manual_config.txt | head -60", "description": "Inspect extracted manuals"}` → `-rw-r--r-- 1 user 197121 10010306 Oct 16 20:41 ASRPRO-CORE.zip -rw-r--r-- 1 user 197121 31034 Oct 16 20:41 ASRPRO-Plus-Factoryprocedure2024.zip -rw-r--r-- 1 user 197121 42473712 Oct 16 20:41 asr_pro_2024.pdf -rw-r--r-- 1 user 197121 248672 Oct 16 20:41 asr_pro_2024.zip -rw-r--r-- 1 user 197121 2457263 Oct 16 20:41 asr_ …[截断,原长3515]`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && /c/ProgramData/anaconda3/python.exe -c \"\nimport sys;sys.stdout.reconfigure(encoding='utf-8')\nfor f in ['manual_config.txt','manual_prog.txt']:\n t=open(f,encoding='utf-8').read()\n print('#####',f,'len',len(t))\n for kw in ['波特率','串口','换行','唤醒','命令词','9600','115200','入门模式','下载']:\n print(kw …[截断,原长398]` → `##### manual_config.txt len 37292 波特率 23 串口 469 换行 4 唤醒 57 命令词 48 9600 15 115200 4 入门模式 0 下载 40 ##### manual_prog.txt len 113526 波特率 55 串口 620 换行 11 唤醒 81 命令词 71 9600 53 115200 8 入门模式 0 下载 53`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:42）

Official 串口范例 exists. Let me search the manuals and inspect the .hd project files.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The manuals are the official "编程模式" and "配置模式" manuals. Let me search the manuals for the exact relevant content: 波特率 default, 换行, 命令词, 下载步骤.

Wait, these are the manuals (编程手册). But the question is about the 图形块 (天问Block 积木块). The 配置模式 manual is probably the "配置模式" which is the graphical block mode. Let me look at the content more carefully.

Actually, let me reconsider. ASRPRO manual 编程手册（配置模式）and 编程手册（编程模式）. The "配置模式" is likely the no-code graphical mode, while "编程模式" is the code mode. Hmm, actually for ASRPRO, 天问Block has 图形化 (block) and 代码 (code/professional). Let me search for the actual block names.

Let me grep the manuals for key terms around 串口发送, 换行, 波特率.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && /c/ProgramData/anaconda3/python.exe -c \"\nimport sys,re;sys.stdout.reconfigure(encoding='utf-8')\nt=open('manual_config.txt',encoding='utf-8').read()\nfor m in re.finditer(r'波特率',t):\n print('---'); print(t[max(0,m.start()-400):m.start()+400].replace('\\n',' '))\n\" | head -80", "description" …[截断,原长411]` → `<persisted-output> Output too large (40.6KB). Full output saved to: C:\Users\UserX\.zcode\cli\exec\sess_subagent_agent_7926cc5f-d529-40c8-b899-8e1835eaf2c7\call_00_2iuLbtBaRYzuRSoneVxN0091-stdout.log Preview (first 2KB): --- 鍙婂敜閱掔殑閫€鍑烘椂闂淬€傚彲閫夊敜閱掕瘝鍞ら啋鍜屾案杩滃敜閱掍袱绉嶏紝鍏朵腑姘歌繙 鍞ら啋鍗充负涓嶉渶瑕佸敜閱掞紝鍙�鐩存帴浣跨敤鍛戒护璇嶃€� 璁剧疆鍞ら啋閫€鍑烘椂闂存渶澶氫负 23 …[截断,原长1428]`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && /c/ProgramData/anaconda3/python.exe -c \"\nimport sys,re;sys.stdout.reconfigure(encoding='utf-8')\nt=open('manual_config.txt',encoding='utf-8').read()\nfor m in re.finditer(r'换行',t):\n print('---'); print(t[max(0,m.start()-500):m.start()+300].replace('\\n',' '))\n\"", "description": "Context a …[截断,原长410]` → `--- 理设置）。 52 4.串口监视器查看串口 0 输出字符串 打开串口监视器：点击右上角串口监视器按钮 本范例串口监视器设置：COM 端口对应选择主板的 COM 端口，COM 端口打开如图左 边按钮显示蓝色为打开状态，波特率对应程序设置，本范例为 9600。 串口 0 输出显示区域：当我们发出语音命令到主板，主板会输出对应字符串并在串口输 出显示区域显示。 字符串的本质就是多个字节组成的字符。 如串口发送"hello"，实际是串口发送 5 个字节，第一个字节'h'（16 进制是 0x68)、第二 个字节'e'(16 进制是 0x65)、第三个字节'l'(16 进制是 0x6c)、第四个字节'l'(16 进制是 0x6c)、 第五 …[截断,原长3187]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:42）

Let me extract the specific serial/baud/word content from the official manuals.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Great, the console output through bash is garbled for the first one but Read tool works fine. Key finding: "1\n" outputs "31 0d 0a" — so \n is CR LF. Actually "1\n" gives "31 0d 0a" which means the "添加换行" adds CR+LF (0d 0a). Let me read the manual files with the Read tool for accurate Chinese.

Let me read the relevant sections of manual_config.txt.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\Robot dog 1.1\\_research\\dl\\pkg\\asrpro\\manual_config.txt", "offset": 180, "limit": 120}` → `180 181 类型 欢迎词 182 退出语音 唤醒词 命令词 命令词 183 184 识别词 欢迎使用智能管家，用天问 185 五幺唤醒我 我退下了，用天问五幺唤醒 186 我 天问五幺 打开灯光 关闭灯光 187 188 回复语音 189 我在 好的，马上执行 好的，马上执行 190 191 三、下载与安装天问 Block 软件 192 下载软件 193 1.浏览器打开天问官方网站 http://twen51.com/。 2.点击天问 Block 下载 194 195 安装软件 196 根据提示默认安装，注意安装过程中，根据提示安装 CH340 驱动。 197 8 198 199 四、运行天问 Block 软件 选择主板 200 …[截断,原长3725]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:43）

The bash pipe garbles Chinese. Let me read the manual files directly with the Read tool.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Now I have great config-mode manual content. Let me read the serial sections (around line 275-730) and the download sections. Let me read the serial example section fully.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\Robot dog 1.1\\_research\\dl\\pkg\\asrpro\\manual_config.txt", "limit": 180, "offset": 460}` → `460 47 461 462 3.程序修改 463 PA5 设置为下拉输入，电平为低，当 PA5 的电平为高时，语音播报“按下了高电平” 。 464 48 465 466 范例 2.1 串口 0 输出字符串 467 一、功能简介 468 本范例通过学习如何使用串口自动发送字符串数据，实现串口输出字符串的功能，达到 用户可以正确使用串口通讯的目的。 469 二、范例分析 470 三、电路与实物说明 471 49 472 473 ASRPRO-Plus 开发板串口所处位置如下图所示： 474 可以看到具有串口通讯功能的的 PA5、PA6、PC0 和 PB7 引脚已经被占用了，如果要查 看串口通讯的数据，可以使用烧写器连接其他具有串口通讯 …[截断,原长9535]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:43）

Now let me read the serial examples and download sections in the config manual.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

This is very rich. Now the config manual is the "配置模式" manual (入门模式/免编程). Note the serial send block in config mode is called "语音控制唤醒词输出16进制命令模块" / "语音控制继电器输出字符串命令模块". Let me look at the .hd example files to see actual block names. The .hd file is likely JSON. Let me inspect.

Also need: download procedure (long press 2s), 词条 limits, 入门模式, 编程模式 block names for 串口发送.

Let me look at the .hd project files.

Note the user asked about "添加换行" option — the config example says "以串口1输出字符串"1\n"为例" and "0d 0a 转换 16 进制为换行". That suggests the string block has a "\n" appended. Let me check the programming-mode manual for the "发送字符串...添加换行" block.

Let me search manual_prog.txt for relevant blocks.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && f=\"ex_p/asr_pro/2.串口范例/2.串口1输出字符串.hd\" && ls -la \"$f\" && file \"$f\" && head -c 3000 \"$f\"", "description": "Inspect a serial example .hd project file"}` → `-rw-r--r-- 1 user 197121 5933 Oct 16 20:42 ex_p/asr_pro/2.串口范例/2.串口1输出字符串.hd ex_p/asr_pro/2.串口范例/2.串口1输出字符串.hd: Unicode text, UTF-8 text, with very long lines (5100), with CRLF, LF line terminators <xml xmlns="http://www.w3.org/1999/xhtml"><block type="setup" id="FZ;QNouPm+Ydel/bulm8" x="0" y="0"><statement name="DO">< …[截断,原长2926]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:43）

Rich detail. Now let me inspect the actual .hd project files and the programming-mode manual for exact block names.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

This is gold. The .hd Blockly XML reveals the exact block types and field names. Let me read the full file for the serial output block.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && f=\"ex_p/asr_pro/2.串口范例/2.串口1输出字符串.hd\" && node -e \"\nconst fs=require('fs');const d=fs.readFileSync('$f','utf8');\nconst m=[...d.matchAll(/<block type=\\\"(serial[^\\\"]*|asr_send[^\\\"]*|[a-z_]*serial[a-z_]*)\\\"[^>]*>([\\s\\S]*?)<\\/block>/g)];\nfor(const x of m){ if(!x[2].includes('<block …[截断,原长414]` → `TYPE: serial_begin <field name="serial_select">Serial1</field><field name="TX">PA_2</field><field name="RX">PA_3</field><value name="CONTENT"><shadow type="baud" id="9@Lf+?Et`#%|h#Vz!D7U"><field name="baud">9600</field></shadow></value> === all block types === setup block_with_textarea asr_speak asr_welcom asr_sleep as …[截断,原长549]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:43）

This is the authoritative source — the actual Blockly XML. Let me extract the serial-send block details.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Let me find the serial_print block and the asr_snid block details. Let me search the whole file system of examples for the serial_print block with 换行 field.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && /c/ProgramData/anaconda3/python.exe -c \"\nimport os,re,sys\nsys.stdout.reconfigure(encoding='utf-8')\nfor root,dirs,files in os.walk('ex_p'):\n for fn in files:\n p=os.path.join(root,fn)\n d=open(p,encoding='utf-8',errors='replace').read()\n for m in re.finditer(r'<block type=\\\"(serial_pr … …[截断,原长390]` → ` File "<string>", line 11 print(p.replace('ex_p\asr_pro\',''),'|',m.group(1),'|',re.sub(r'\s+',' ',seg)[:700]) ^ SyntaxError: unexpected character after line continuation character`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:43）

Let me find the serial_print block details with the newline field across all examples.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Let me write a small python file instead. Actually simpler: use node.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && cat > scan.cjs <<'EOF'\nconst fs=require('fs'),path=require('path');\nfunction walk(d){let r=[];for(const e of fs.readdirSync(d,{withFileTypes:true})){const p=path.join(d,e.name);if(e.isDirectory())r=r.concat(walk(p));else r.push(p);}return r;}\nconst types=new Set();\nfor(const f of walk('ex_ …[截断,原长413]` → `C:\Users\UserX\Downloads\Robot dog 1.1\_research\dl\pkg\asrpro\scan.cjs:9 console.log('FILE:',f.replace(/\/g,'/'),'\n', m[1].replace(/\s+/g,' ').slice(0,800),'\n'); ^^^^^^^ SyntaxError: missing ) after argument list at wrapSafe (node:internal/modules/cjs/loader:1692:18) at Module._compile (node:internal/modules/cjs/loa …[截断,原长773]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The heredoc mangled the backslash. Let me write the file with the Write tool instead.

</details>

- 🔧 **Write** `{"content": "const fs=require('fs'),path=require('path');\nfunction walk(d){let r=[];for(const e of fs.readdirSync(d,{withFileTypes:true})){const p=path.join(d,e.name);if(e.isDirectory())r=r.concat(walk(p));else r.push(p);}return r;}\nconst types=new Set();\nfor(const f of walk('ex_p')){\n const d=fs.readFileSync(f,'utf8');\n [...d.matchAll(/<block type=\"([^\"]+)\"/g)].forEach …[截断,原长410]` → ``

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:43）

The heredoc mangled backslashes. Let me write the script with the Write tool.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Hmm, the file exists from the heredoc. Let me read it then write.

Actually simpler: use Bash with node -e but write script differently avoiding backslashes. Let me just read the file first.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\Robot dog 1.1\\_research\\dl\\pkg\\asrpro\\scan.cjs"}` → `1 const fs=require('fs'),path=require('path'); 2 function walk(d){let r=[];for(const e of fs.readdirSync(d,{withFileTypes:true})){const p=path.join(d,e.name);if(e.isDirectory())r=r.concat(walk(p));else r.push(p);}return r;} 3 const types=new Set(); 4 for(const f of walk('ex_p')){ 5 const d=fs.readFileSync(f,'utf8'); 6  …[截断,原长717]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Line 9 is mangled. Let me rewrite the whole file.

</details>

- 🔧 **Write** `{"content": "const fs=require('fs'),path=require('path');\nfunction walk(d){let r=[];for(const e of fs.readdirSync(d,{withFileTypes:true})){const p=path.join(d,e.name);if(e.isDirectory())r=r.concat(walk(p));else r.push(p);}return r;}\nconst types=new Set();\nfor(const f of walk('ex_p')){\n const d=fs.readFileSync(f,'utf8');\n [...d.matchAll(/<block type=\"([^\"]+)\"/g)].forEach …[截断,原长410]` → `The file C:\Users\UserX\Downloads\Robot dog 1.1\_research\dl\pkg\asrpro\scan.cjs has been updated successfully. (file state is current in your context — no need to Read it back)`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

 

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && node scan.cjs 2>&1 | tail -70", "description": "Run block scanner"}` → `mbmasterreqreadwriteholdingregister_s mbmasterreqwritecoil mbmasterreqwritecoil_s mbslaveinit mbslavepoll mbslavesetholdreg nvdata_init nvdata_read nvdata_write pin_irq_read play_cmid procedures_defnoreturn pwm_duty pwm_init rcswitch_available rcswitch_init rcswitch_resetavailable rcswitch_value rec_messga s_reg_holdin …[截断,原长1086]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Let me see the serial_print matches and all block types from the top.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && node scan.cjs 2>&1 | head -50", "description": "Show serial_print usages"}` → `FILE: ex_p/asr_pro/2.串口范例/1.串口0输出字符串.hd <field name="serial_select">Serial</field><value name="CONTENT"> FILE: ex_p/asr_pro/2.串口范例/1.串口0输出字符串.hd <field name="serial_select">Serial</field><value name="CONTENT"> FILE: ex_p/asr_pro/2.串口范例/1.串口0输出字符串.hd <field name="serial_select">Serial</field><value name="CONTENT"> FILE: …[截断,原长1843]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The regex cuts off because `<value name="CONTENT">` is followed by a `<shadow>` then maybe `<block>`. Let me look at the full serial_print block, including nested content, and also serial_println. Let me look at the raw file content around serial_print and asr_snid blocks.

Key block types found: serial_begin, serial_print, serial_println, serial_write, serial_readstr, serial_available, serial_parseInt_Float, asr_snid, asr_id, asr_send?

Let me dump a serial example file's raw content fully.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && node -e \"\nconst fs=require('fs');\nconst f='ex_p/asr_pro/2.串口范例/1.串口0输出字符串.hd';\nconst d=fs.readFileSync(f,'utf8');\nconst i=d.indexOf('asr_id');\nconsole.log(d.slice(0,6000));\n\"", "description": "Dump raw serial example project XML"}` → `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="setup" id="FZ;QNouPm+Ydel/bulm8" x="0" y="0"><statement name="DO"><block type="block_with_textarea" id="M)*xfpNm;_-[d5HZ9H3="><field name="input">//需要操作系统启动前初始化的内容</field><next><block type="asr_speak" id="MaT`9+Oikgn}zKtgg?A["><field name="VOICE_SET">小蝶-清新女声</field …[截断,原长5548]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Now I have the definitive block structure. Key findings:
- Block type `serial_print` - "serial_select" Serial/Serial1/Serial2, no newline field → 无换行
- Block type `serial_println` - likely the newline version! Let me check. The examples use serial_print with text "hello" and no newline. The manual mentioned "1\n" giving 31 0d 0a, and the default example "hello" giving no newline? Actually the manual said output "1" showed 31 0d 0a. Hmm.

Let me check serial_println and serial_begin fields. Also check the 串口1接收 examples and the newline checkbox. Let me look for the config-mode example that has the newline option. Let me check ex_e too.

Also I need to check the 编程模式 examples for serial_println. Let me scan.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && cat > scan2.cjs <<'SCRIPT'\nconst fs=require('fs'),path=require('path');\nfunction walk(d){let r=[];for(const e of fs.readdirSync(d,{withFileTypes:true})){const p=path.join(d,e.name);if(e.isDirectory())r=r.concat(walk(p));else r.push(p);}return r;}\nfor(const f of walk('ex_p')){\n const d=fs.r …[截断,原长413]` → `FILE: 2.串口范例/10.串口1接收到字符串打开继电器.hd | serial_available | <field name="serial_select">Serial1</field></block></value><statement name="DO0"> FILE: 2.串口范例/10.串口1接收到字符串打开继电器.hd | serial_readstr | <field name="serial_select">Serial1</field></block></value><next> FILE: 2.串口范例/11.串口2接收到字符串打开继电器.hd | serial_available | <field na …[截断,原长4657]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:44）

Let me check the `serial_println` (newline) block and the receiving examples.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Now I have solid facts. Note: block type is `serial_print` (输出字符串, no newline) and `serial_println` (带换行). Wait — in ex_p the send-string examples used serial_print with text "hello" and "on"/"off". The manual says output shows "31 0d 0a" for "1". Hmm, the manual said for 串口0输出字符串 "1" → 31 0d 0a (with newline). But the block used is serial_print. Let me check the ex_e (配置模式) example for "串口0输出字符串" where the block may be different — there the config-mode uses "语音控制唤醒词输出字符串命令模块".

Actually the 配置模式 (ex_e) uses different blocks. Let me check ex_e files. And the config manual page says "串口输出显示为'1'，勾选16进制显示，串口输出为'31 0d 0a'". So in config mode the output includes \r\n. But the ex_p serial_print with text "hello" — does it add newline? The block type is separate `serial_print` vs `serial_println`. Need to determine default.

Let me look at ex_e config-mode project files to see the block types there (语音控制唤醒词输出字符串 etc.), and also check if there's a "添加换行" field. The user asked specifically about "添加换行" option and default state.

Let me search the manual_config text for "换行" — earlier grep found 4 occurrences. Two were about 0d0a. Let me look at the programming-mode manual (manual_prog) around 换行 (11 occurrences) and around serial_print/serial_println.

Actually the key: in the manual_config, examples say output "1\n" for 串口1 and 串口2 — with newline. And 串口0 output "1" without? Let me re-read: 
- 2.1 串口0: '以串口0输出字符串"1"为例...串口输出为"31 0d 0a"' 
- 2.2 串口1: '以串口1输出字符串"1\n"为例'
- So the config-mode block for 串口1/2 might have newline. Hmm ambiguous.

Let me inspect the ex_e (配置模式) examples which are the config-mode projects. But ex_e files were named "1.基础范例"、"2.串口范例" — wait ex_e listing earlier showed "1.+¨¦íÀÂ+²" and "2.¦«++ÀÂ+²" which decoded to 基础范例? Let me re-list ex_e now after re-extraction.

Let me also check the programming-mode manual content re: serial_print vs serial_println and "换行". And find "添加换行" exact phrase.

Also need: 入门模式 (config mode = 配置模式). The user's Q7 asks about "入门模式" (免编程模式). The homepage said "图形化界面编程（入门模式）". In ASRPRO context, there's 配置模式 (config mode) vs 编程模式 (program mode). Let me search manual for 配置模式/编程模式/入门.

Let me gather more efficiently.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && /c/ProgramData/anaconda3/python.exe -c \"\nimport os,sys;sys.stdout.reconfigure(encoding='utf-8')\nfor root,dirs,files in os.walk('ex_e'):\n for fn in files: print(os.path.join(root,fn))\n\"", "description": "List config-mode examples"}` → `ex_e\asr_pro_e\1.基础范例\1.智能语音对话.hd ex_e\asr_pro_e\1.基础范例\10.引脚高电平控制播报.hd ex_e\asr_pro_e\1.基础范例\2.语音控制板载LED.hd ex_e\asr_pro_e\1.基础范例\3.语音控制单继电器.hd ex_e\asr_pro_e\1.基础范例\4.语音控制四路继电器.hd ex_e\asr_pro_e\1.基础范例\5.语音控制八路继电器.hd ex_e\asr_pro_e\1.基础范例\6.语音控制单继电器10秒后关闭.hd ex_e\asr_pro_e\1.基础范例\7.语音控制继电器延时后关闭.hd ex_e\asr_pro_e\1.基础 …[截断,原长945]`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && /c/ProgramData/anaconda3/python.exe -c \"\nimport sys;sys.stdout.reconfigure(encoding='utf-8')\nfor f in ['manual_config.txt','manual_prog.txt']:\n t=open(f,encoding='utf-8').read()\n print('#####',f)\n for kw in ['配置模式','编程模式','入门模式','添加换行','换行','2秒','长按','串口监视器','生成模型','实名','联网','语音芯片专属']:\n …[截断,原长398]` → `##### manual_config.txt 配置模式 5 编程模式 2 入门模式 0 添加换行 0 换行 4 2秒 0 长按 0 串口监视器 53 生成模型 11 实名 5 联网 3 语音芯片专属 0 ##### manual_prog.txt 配置模式 1 编程模式 21 入门模式 0 添加换行 0 换行 11 2秒 0 长按 0 串口监视器 55 生成模型 12 实名 4 联网 12 语音芯片专属 0`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:44）

Let me check the config-mode examples (ex_e) and search the manuals for the newline option and mode names.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The config mode examples are the same set. Let me look at the config-mode serial example to see the block used for 串口输出字符串 (the "语音控制...输出字符串" block = asr_id block with serial output mode). Let me inspect ex_e/asr_pro_e/2.串口范例/1.串口0输出字符串.hd.

Also I should check the config manual for the 发送字符串 block with 添加换行 option. The config-mode uses "语音识别...串口选择X，输出模式选择输出字符串". Let me find the actual block for config mode.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && node -e \"\nconst fs=require('fs');\nconst d=fs.readFileSync('ex_e/asr_pro_e/2.串口范例/2.串口1输出字符串.hd','utf8');\nconsole.log(d.slice(0,7000));\n\"", "description": "Dump config-mode serial example XML"}` → `<xml xmlns="http://www.w3.org/1999/xhtml"><block type="asr_easystart_setup" id=",vvfBQ;N;Bh5eh})1TpC" x="0" y="0"><field name="VOICE_SET">小蝶-清新女声</field><field name="vol">10</field><field name="speed">10</field><field name="WELCOME">欢迎使用语音助手，用天问五幺唤醒我。</field><field name="SLEEP">我退下了，用天问五幺唤醒我</field><field name="play_vo …[截断,原长2361]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Now I have the config-mode (配置模式) block structure. Key: `asr_easystart_setup` (上电初始状态), `asr_easystart_wakeup` (唤醒词), `asr_easystart_recognize` (命令词). And in programming mode: `asr_id`, `serial_print`, `serial_println`, `serial_begin`.

Note config mode has `serial_bin` String vs 16进制. There's no explicit "换行" field in these examples... yet the manual says "串口输出显示为'1'...31 0d 0a...0d 0a 转换 16 进制为换行". So the string output automatically appends \r\n? Let me check. Actually the manual 2.1 says: 以串口 0 输出字符串"1"为例... 串口输出为"31 0d 0a". So it shows in config mode there's an option. Let me look for "换行" contexts in config manual, and also check whether the string block text includes \n. In example 2.2 the manual says 串口1输出字符串"1\n" — so in the .hd the NAME might contain "1\n". Let me look at whether there's a checkbox for adding newline in the block, maybe fieldname. Let me search the manuals for 换行 context via Read tool.

Also I should look at the programming-mode manual for the exact block names / Chinese labels of serial_print and serial_println, and the 换行 option. Let me search manual_prog.txt around 换行.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && grep -n \"换行\" manual_prog.txt manual_config.txt", "description": "Find newline mentions with line numbers"}` → `manual_config.txt:501: 以串口 0 输出字符串“1“为例设置程序如图： 串口输出显示为“1”，勾选 16 进制显示，串口输出为“31 0d 0a”，其中 1 转换 16 进制为 31，0d 0a 转换 16 进制为换行。 manual_config.txt:544:以串口 1 输出字符串“1\n“为例设置程序如图： 串口输出显示为“1”，勾选 16 进制显示，串口输出为“31 0d 0a”，其中 1 转换 16 进制为 31，0d 0a 转换 16 进制为换行。 manual_config.txt:587: 以串口 2 输出字符串“1\n“为例设置程序如图： 串口输出显示为“1”，勾选 16 进制显示，串口输出 …[截断,原长2234]`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && grep -n \"下载\" manual_config.txt | head -50", "description": "Find download mentions in config manual"}` → `11: 2. ASRPRO 基础开发板，长宽为 30x28mm，板载麦克风、指示灯，用户只需要外接喇 叭就可以使用，下载程序需要搭配 STC-LINK 下载器。 12:3. ASRPRO-CORE 核心板，模块体积小巧，长宽为 18x23mm，对外接口采用 2 排邮票 孔和插针孔，方便采用回流贴片使用和焊接插针使用，喇叭和麦克风都需要自己外接，下载 程序需要搭配 STC-LINK 下载器。 15: 4. ASRPRO-MAX开发板，采用QFN40封装芯片，26路IO口独立引出，长宽为 62.0x25.5mm，板载RGB，用户只需要外接喇叭和咪头就可以使用，下载程序需要搭配 STC-LINK下载器。 16:5. 鹿小班 ASRPRO  …[截断,原长1456]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:45）

Let me read the manual sections about serial output/newline and download flow.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

I have a lot of good info. Let me now look at the programming manual for the download process, model generation time, and the "长按2秒" download button. Also need Arduino/ESP8266 example. Let me search the manual_prog for download steps and 2秒/长按.

Let me also get the Arduino example page content (the PDF page from asr_pro). And search for ASRPRO串口模块 + ESP8266.

Let me update todos and continue.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "确认官网域名并抓取首页/资料/课程栏目结构", "priority": "high", "status": "completed"}, {"content": "定位天问Block 教程/文档与 ASRPRO 专页(wiki/docs)", "priority": "high", "status": "completed"}, {"content": "查证串口发送积木名称、UART1/2、波特率、换行", "priority": "high", "status": "in_progress"}, {"content": "查证编译下载流程、词条配置、入门模式", "priority": "high", "status": "pending"}, {"content": "查找 ASRPRO 与 Ard …[截断,原长411]` → `{"oldTodos":[{"content":"确认官网域名并抓取首页/资料/课程栏目结构","status":"in_progress","priority":"high"},{"content":"定位天问Block 教程/文档与 ASRPRO 专页(wiki/docs)","status":"pending","priority":"high"},{"content":"查证串口发送积木名称、UART1/2、波特率","status":"pending","priority":"high"},{"content":"查证编译下载流程、词条配置、入门模式","status":"pending","priority":"high …[截断,原长1018]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The .hd files don't have a "添加换行" checkbox in the XML I saw — serial_print vs serial_println are separate blocks. But the manual mentions "自动换行" for 16进制. Let me look for the "自动换行" and the checkbox in the manual more precisely, and check the programming mode manual around line 1095. Also need to check the block definition (blockly JSON) maybe present in examples? No.

Let me check the programming manual section for serial and the 换行/自动换行. Also check whether there's a "添加换行" option — the manual says "由于此处没有使用换行指令" which implies a separate block (serial_println = 换行输出). Let me read manual_prog around 640-760 and 1080-1100.

Also need info on 入门模式. Search web/docs.

Let me also check the twen51 download for the online programming page /C51/asr_pro.php?id=97624 which returned 404 earlier via that path — try without /new/twen51 prefix.

Actually the link was relative to /new/twen51/: "/C51/asr_pro.php?id=97624" — leading slash means root: http://twen51.com/C51/asr_pro.php?id=97624. Let me fetch that.

Let me do these reads.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\Robot dog 1.1\\_research\\dl\\pkg\\asrpro\\manual_prog.txt", "limit": 60, "offset": 1080}` → `1080 1081 这条指令在读写寄存器中。 1082 1083 这条指令代表着从寄存器中读取字符串类型变量 1084 1085 Rec存储的第一个字节，并把他转换位uint8_t数组，也就是无符号一个字节的整型。 1086 1087 如果要获取这个变量的第二个字节，则可以将指令改成如下所示。 1088 1089 通过这样的形式，我们可以对串口接收到的一串16进制数进行读取和判断。 1090 1091 我们将范例代码中的UART1_RX进行修改，使用串口0进行测试。注意，每个串口要单 独用一个线程进行处理。这里我们选择将带有串口0指令的另一个线程禁用。 1092 1093 163 1094 1095 勾选16进制发送和16进制显示， …[截断,原长3163]`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && grep -n \"打印\\|输出字符串\\|输出 16\\|output\\|串口 1 输出\\|串口初始化\\|波特率\" manual_prog.txt | head -40", "description": "Find serial output block descriptions"}` → `333:GPIO是General-purpose input/output的缩写，指的是通用型输入输出口的简称。我们 可以通过天问Block的程序编写自由控制这些引脚。 485:pinMode(_pin,output); //设置为输出模式 #if defined(TW_ASR_PRO) 658: 串口范例 范例2.1 串口0输出字符串 一、范例功能 671:编写好语音控制串口打印不同字符串的程序，我们可以通过串口监视器直接查看串口0 的输出值。我们以语音播报打开板载灯和关闭板载灯为例进行查看。 672:打开左上角的串口监视器，会得到下方的界面。其中点击区域1可以打开串口；区域2 部分是串口的输出信息；在区域3内可以往串口发送消息； …[截断,原长4855]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Now let me read the programming mode manual beginning to get the exact block names for serial output ("打印"/"println"), the config structure, and download flow. Let me read manual_prog.txt 640-720.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\Robot dog 1.1\\_research\\dl\\pkg\\asrpro\\manual_prog.txt", "limit": 80, "offset": 640}` → `640 。 提示：学习状态中，保持安静 说“好好搭搭” 提示：请再说一次！ 再次说“好好搭搭” 提示：指令学习成功 就可以使用学习过的唤醒词“小智小智”来唤醒语音助手！ 这样学习的唤醒词可以是普通话，也可以是方言，但是注意学习过程中说的两次唤醒词 641 需要保持一致。 642 （二）学习命令词 用唤醒词（默认或已学习的）唤醒语音助手，然后说“学习命令词”，根据提示来学 643 习新的命令词。 在自学习状态下学习指令，语音会进行提示： 学习状态中，保持安静，请说第一条要学习的指令。 说“打开客厅灯” 提示：请再说一次！ 再次说“打开客厅灯” 提示：指令学习成功，请说出第二条要学习的指令 ………… (继续学习即可) 或者使用“退出学习 …[截断,原长5850]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\Robot dog 1.1\\_research\\dl\\pkg\\asrpro\\manual_prog.txt", "limit": 120, "offset": 1}` → `1 ASRPRO 编程模式使用手册 2 一、概述 3 芯片概述 4 本产品是针对低成本离线语音应用方案开发的一款通用、便携、低功耗高性能的语音识 别芯片，采用了第三代语音识别技术，能支持 DNN\TDNN\RNN 等神经网络及卷积运算， 支持语音识别、声纹识别、语音增强、语音检测等功能，具备强劲的回声消除和环境噪声抑 制能力，语音识别效果优于其它语音芯片。该芯片方案还支持汉语、英语、日语等多种全球 语言，可广泛应用于家电、照明、玩具、可穿戴设备、工业、汽车等产品领域，搭配天问Block 图形化编程软件，快速实现语音交互及控制和各类智能语音方案应用。 5 6 SSOP24 芯片引脚图 7 8 QFN40 芯片引脚图 9 10 天问提供 …[截断,原长2495]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Now I need the UART selection details — it's covered. Now let me check the serial_println (with newline) block name. I need the actual Chinese label for the blocks. The .hd XML only has block types, not the displayed labels. The manuals have screenshots (images) not text for block labels.

Key info: "添加换行" option. In the XML I see `serial_print` and `serial_println`. In many Tblock/wenwen implementations the block is "串口输出" with a dropdown for "不换行"/"换行". Let me search the manual for the block naming and also look at the config manual for the "串口输出字符串" block and its options.

Actually the user asks specifically: "发送字符串时'添加换行'选项的作用和默认状态". In the config-mode example XML, asr_easystart_wakeup has not the newline field... Let me check if there's a "换行" field in some .hd.

Let me grep the .hd files for "换行" or "ln" fields.

Also I need to check the block labels in Chinese. The manual text mentions "语音控制唤醒词输出 16 进制命令模块". And in programming mode, the serial blocks. Let me look at the manual for how blocks are named in text. Search for "串口" + "输出" descriptions, and "添加换行".

Since "添加换行" count is 0 in manuals, the option may be called differently. Let me grep the .hd for a field with newline.

Let me also check the config manual around line 466-501 for the block names in text.

Also need item 5 (Arduino/ESP32/ESP8266 examples) — I saw "4.扩展范例/14.ESP32_Wi-Fi_TCP_UDP通讯.hd" which is the ASRPRO-Plus with onboard ESP32-C3. There's also the Arduino_example page which is 好搭 (Arduino-style) — let me check whether there's a page specifically about ASRPRO串口模块 communicating with another MCU. And 附录二 mentioned "外接设备如何使用" — let me find 附录二 in the programming manual.

Let me search for 附录 and ESP8266/Arduino in the manuals.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && echo \"=== prog: 附录/ESP8266/Arduino/外接 ===\"; grep -n \"附录\\|ESP8266\\|Arduino\\|ESP32\\|外接设备\\|其它主控\\|其他主控\\|另一块\\|单片机之间\" manual_prog.txt | head -40; echo; echo \"=== config: same ===\"; grep -n \"附录\\|ESP8266\\|Arduino\\|ESP32\\|外接设备\" manual_config.txt | head -30", "description": "Search a …[截断,原长414]` → `=== prog: 附录/ESP8266/Arduino/外接 === 17:天问基于ASRPRO芯片目前推出了6种类型，供开发者选择。 1. ASRPRO-Plus 开发板是一款带语音识别的物联网开发板，基于 32 位 RISC-V 内核， 内置神经网络处理器，支持 DNN\TDN-N\RNN 等神经网络及卷积运算，支持语音识别、声 纹识别、语音增强、语音检测等功能，具备强劲的回声消除和环境噪声抑制能力。板载 RS485、 433M 无线收发、红外收发、ESP32-C3(2.4GHz Wi-Fi 和 Bluetooth 5LE)5 种通讯方式；SPI 彩 屏、数码管、RGB 灯 3 种显示模块；光敏传感器、DHT11 温湿度传感器 …[截断,原长3504]`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && grep -rn \"换行\\|newline\\|NEWLINE\\|ln\\b\" --include=*.hd ex_p ex_e 2>/dev/null | head -20; echo \"--- fields containing ln/lns ---\"; grep -rhoE '<field name=\"[a-zA-Z_]*ln[a-zA-Z_]*\">[^<]*' --include=*.hd ex_p ex_e | sort -u | head", "description": "Search newline fields in hd files"}` → `<persisted-output> Output too large (366KB). Full output saved to: C:\Users\UserX\.zcode\cli\exec\sess_subagent_agent_7926cc5f-d529-40c8-b899-8e1835eaf2c7\call_01_d7eGMGPKhXtVrLXoZPDp5520-stdout.log Preview (first 2KB): ex_p\asr_pro\1.基础范例\9.语音控制引脚（脉冲）点动.hd:1:<xml xmlns="http://www.w3.org/1999/xhtml"><block type="setup …[截断,原长2244]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Found Appendix 2: ASRPRO 与其他单片机串口通讯的范例说明, including Arduino UNO and ESP32. Let me read that appendix in both manuals.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\Robot dog 1.1\\_research\\dl\\pkg\\asrpro\\manual_config.txt", "limit": 180, "offset": 825}` → `825 平即继电器关闭，同时语音播报“已经关闭继电器”； ASRPRO 开发板实物连接： 826 2.程序修改 827 PA_4 模拟继电器，输出高电平。所有涉及到串口的引脚在初始化设置中不进行设置。 全部用 PD_5 代替，状态设置为悬空输入。 828 语音识别“打开继电器”选择引脚 PA_4，输出高电平。语音识别“关闭继电器”选择引脚 PA_4，输出低电平。串口收到十六进制数“AA 00 03”时，PA4 输出高电平即继电器打开。串 口收到十六进制数“AA 00 04”时，PA4 输出低电平即继电器关闭。 829 104 830 831 附录一：语音识别设置注意事项 832 关于中英文语音识别还有一些注意事项，这里给出以下使用建 …[截断,原长7150]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:46）

Found Appendix 2 covering Arduino/ESP32 communication. Let me read it.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Excellent. Now I have Appendix 2 with Arduino/STM32/ESP32 examples. Let me check if ESP8266 is mentioned. The manual mentions ESP32 (3V), STC, STM32, Arduino UNO. Let me check the ESP32 section and see if ESP8266 is mentioned anywhere. Also let me look at 附录三 VS Code and the "入门模式" question. Let me also check the prog manual appendix 2 for the same.

Let me now search for ESP8266 specifically and check the 入门模式 (entry mode / easy mode) terminology. In the manual, "配置模式" is essentially the no-code mode. But the user asks about "入门模式" — the homepage mentioned "图形化界面编程（入门模式）". Let me verify.

Also need to find the serial output block name in the config mode. In 配置模式 the block is "asr_easystart_wakeup"/"asr_easystart_recognize" with serial / serial_bin / NAME fields. In 编程模式 it's serial_print / serial_println / serial_write. Let me search the prog manual for the exact block label names ("打印" / "输出字符串").

Let me check the ESP32/ESP8266 section and the newline block label.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\Robot dog 1.1\\_research\\dl\\pkg\\asrpro\\manual_prog.txt", "limit": 220, "offset": 2443}` → `2443 附录 2444 附录一：语音识别设置注意事项 2445 学习完整体的程序结构后，关于语音设置还有一些注意事项，这里给出一些中文语音和 英文语音使用时的建议。 1. 一般为 4-6 个字，4 个字最佳，过短容误识高，过长不便用户呼叫和记忆； 2. 命令词中相邻汉字的声韵母区分度越大越好； 3. 符合用户的语言习惯，尽量采用常用说法，内容具体直接； 4. 应避免使用日常用语，如：“吃饭啦”; 5. 生僻字和零声母字应尽量避免，如“语音识别”中“语音”两个字均为零声母字; 6. 命令词中的字最好不要有语气词，如“啊”、“呢”等; 7. 应避免使用叠词，如：“你好你好”; 8. 中文命令词中只能由汉字组成,不允许有空格,逗号等其他 …[截断,原长7139]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\Robot dog 1.1\\_research\\dl\\pkg\\asrpro\\manual_prog.txt", "limit": 70, "offset": 2745}` → `2745 2746 353 2747 2748 k++; } while(*(str + k)!='\0'); /* 等待发送完成 */ while(USART_GetFlagStatus(pUSARTx,USART_FLAG_TC)==RESET) {} } 2749 3) 程序效果 STM32端间隔一段时间串口发送“LED ON”、"LED OFF"，ASRPRO接收到串口命令后 2750 会马上唤醒自动播报语音“灯光已打开”、“灯光已关闭”。 2751 五、ESP32（3V单片机） 1. 电路连接 2752 掌控板的P15引脚的TX，接ASRPRO的RX，也就是接在PB6；P16引脚接到ASRPRO RX引脚（PB5），两者的 …[截断,原长3457]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\Robot dog 1.1\\_research\\dl\\pkg\\asrpro\\manual_prog.txt", "limit": 60, "offset": 2765}` → `2765 356 2766 2767 2) micro:bit 程序 2768 357 2769 2770 附录三：VS Code使用与全编译下载 一、VS Code安装 2771 ASRPRO的字符编程已经全面和VS Code打通。我们可以使用VSC对代码进行查看和 修改，并进行编译下载。 2772 首先安装VS Code，并安装部分常规插件。注意第二幅图必须勾选添加到PATH，即勾 选配置环境变量，否则无法通过天问Block的字符编程模式右键打开。 2773 为了方便后续使用，建议安装简体中文插件。按下crtl+Shift+X，开始搜索。 安装后，我们就可以直接通过天问Block的字符编程，右键，选择VS Code打开文件。 2 …[截断,原长2775]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:46）

Now let me read the ESP32 section (五、ESP32) and the VS Code/full compile appendix, plus check the forum thread and official wiki.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

I have very comprehensive data. Now let me verify a few remaining items:
- Q1: block name "语音控制唤醒词输出16进制命令模块" / "语音控制继电器输出字符串" and the "添加换行" option — need to find the exact checkbox name. The XML has serial_print and serial_println. The manual mentions "换行" only as "自动换行". The question asks about "添加换行" option and its default state. The serial_println block likely has a checkbox. Let me check the block definitions — search for serial_println usage in the ex_e config examples which have a checkbox. Actually ex_e serial examples - let me check.

Also need:
- Q3: download button 长按2秒? The manual doesn't mention. There's mention of 鹿小班 auto power-off. Let me search the ASRPRO knowledge base / forum.
- Q6: official docs site. The official 知识库 is on Yuque (语雀). Also there's a 天问51API文档 at dolphin666.github.io/docs. Let me verify the Yuque links are official (from official website article). Yes — learning_show.php?id=652 lists them as official knowledge base.
- Q7: 入门模式 = 图形化界面编程; the website homepage mentions "图形化界面编程（入门模式）". Also the manual mentions 配置模式/编程模式. The "入门模式" in the website is graphic programming. Let me check the asr_pro_e_2024.pdf config manual - it says "配置模式". The question asks about "入门模式（免编程模式）". Let me verify.

Actually let me check ex_e examples for the newline checkbox field, and search the manual for the 配置模式 block names like "语音控制唤醒词输出" and the newline option. Let me look at the config manual's block descriptions around serial. Actually in config mode there's no explicit serial block - it's inside the asr_easystart_recognize block fields: serial, serial_bin, NAME. The "serial_bin" field = String/HEX. And there might be a newline field.

Let me look for "换行" checkbox in the 天问Block source/js. Actually, let me check the raw text of the ex_e example for any ln field. The example showed fields: serial, serial_bin, NAME. No newline field. So in config mode there's no newline checkbox — the newline is auto (0d 0a) per manual "0d 0a 自动换行".

Hmm wait, actually the manual config says output "1" gives "31 0d 0a" automatically includes 0d 0a. So add newline is default ON in config mode? Let me re-read: "串口输出显示为"1"，勾选 16 进制显示，串口输出为"31 0d 0a"，其中 1 转换 16 进制为 31，0d 0a 转换 16 进制为换行。" — so it seems newline is appended by default.

For programming mode, serial_print (no newline) vs serial_println (with newline). The manual prog line 672: "由于此处没有使用换行指令，所以会在同一行显示" — meaning they used serial_print without newline. And line 1095: "当我们输入 ff 01 02 时，串口会输出ff 01 02 0d 0a，其中0d 0a是自动换行" — that's serial_println.

Let me check the block definitions to find the exact checkbox. Let me search天问Block's block definition files. I don't have the IDE. But the JSON/JS may be online. Let me check the blockly generator. Actually the question specifically asks about "添加换行" option. Let me search online for it.

Let me also verify the "长按下载按钮2秒" claim - search knowledge base/forum.

Let me search the forum thread 734 and the knowledge base. Also try to fetch Yuque content via a rendered approach.

Let me try fetching the Yuque doc via the "?view=doc" or via the yuque2md or the public share API. Actually Yuque public pages render client-side. But there may be an alternative: the article on the official site mention. Or I can search Baidu/Bing more specifically.

Let me also try to find the block definition for "添加换行" via the online twen51 programming page /C51/asr_pro.php. That was 404. Let me try the online programming (display_code / blockly) resources.

Actually, a better approach: search the web for "天问Block 串口 打印 添加换行".

Let me do targeted searches. Let me use WebFetch with cn.bing.com but with better query (the earlier failure returned dictionary results, likely because bing ignored). Let me try searching in a different way - use the site: operator or use sogou/baidu.

Let me try fetching the forum thread about ASRPRO FAQ (tid=734) and the knowledge base.

Also需要确认 Q3: 联网生成语音模型耗时. The official site article and knowledge base mention "3分钟生成固件". Website homepage: "免学习三分钟生成固件完成产品开发". That's a marketing claim.

Let me now gather remaining specifics and try the Yuque knowledge base via alternate fetch.

Let me try fetching via r.jina.ai proxy? That may not be allowed. Let me try WebFetch on yuque with a different path. Actually WebFetch already failed (only "天问ASRPRO · 语雀"). 

Let me try the yuque "book" share link format and also try fetching with curl and searching for embedded JSON.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && echo \"=== forum tid=734 (ASRPRO FAQ) ===\"; curl -s -L -m 25 \"http://twen51.com/new/bbs/forum.php?mod=viewthread&tid=734\" -o forum734.html; ls -la forum734.html; node -e \"\nconst fs=require('fs');const d=fs.readFileSync('forum734.html','utf8');\nlet t=d.replace(/<script[\\s\\S]*?<\\/script>/g,'') …[截断,原长414]` → `=== forum tid=734 (ASRPRO FAQ) === -rw-r--r-- 1 user 197121 90807 Oct 16 20:46 forum734.html ASRPRO常见问题及解决方案汇总 - 天问Block常见问题 - 好好搭搭论坛 - 好好搭搭在线 请 登录 后使用快捷导航 没有帐号？ 立即注册 --> 手机端 --> 手机扫码下载APP --> --> 手机扫码关注微信公众号 --> 手机扫码访问移动论坛 --> 论坛首页 好搭产品 好搭软件 官方网站 淘宝购买 平台使用文档 登录 | 立即注册 搜索 本版 帖子 用户 好好搭搭论坛 &raquo; 论坛首页 &rsaquo; 嵌入式开发 &rs …[截断,原长3092]`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && echo \"=== yuque with fragment/share ===\"; curl -s -L -m 25 \"https://www.yuque.com/twen51/asrpro\" -H \"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\" -o yuque.html; ls -la yuque.html; node -e \"\nconst fs=require('fs');const d=fs.readFileSync('yuque.html','utf8');\nconsole.log('len',d.len …[截断,原长414]` → `=== yuque with fragment/share === -rw-r--r-- 1 user 197121 49048 Oct 16 20:46 yuque.html len 48184 <!doctype html> <html data-kumuhana="default"> <head> <meta charset="utf-8"> <meta name="robots" content="noindex"> <meta name="robots" content="nofollow"> <meta name="viewport" content="width=device-width, initial-scale= …[截断,原长1516]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:46）

I have extensive primary-source data. Let me verify remaining points: the newline checkbox, download/programming flow, and official docs site.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Excellent — the official forum thread gives the Yuque knowledge base structure. Let me get the rest of the FAQ thread and try to find the Yuque "串口" doc page. Let me also check the beginner mode (入门模式) — the official site says 图形化界面编程（入门模式）. Let me search for more.

Let me get the full forum text and look for 串口 and 入门模式.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && node -e \"\nconst fs=require('fs');const d=fs.readFileSync('forum734.html','utf8');\nlet t=d.replace(/<script[\\s\\S]*?<\\/script>/g,'').replace(/<style[\\s\\S]*?<\\/style>/g,'').replace(/<[^>]+>/g,' ').replace(/&nbsp;/g,' ').replace(/\\s+/g,' ');\nconsole.log(t.slice(3000,9000));\n\"", "description" …[截断,原长414]` → `次尝试生成模型； （3）生成模型时，提示文件被占用，请解除占用后重试。造成该情况的原因有两种：① 生成模型相关的文件确实被占用，解决方法是解除占用，如果不知道如何处理可以重启电脑，自动解除占用；② 还有一种情况是使用了代理服务器，导致文件下载异常，无法解压，提示文件占用，可以尝试加载扩展库看下是否成功；③ 可以尝试将更多-&gt;设置-&gt;网络协议从 https 切换至 http；④ 本地网络不稳定，可以切换网络后再试。⑤ 默认解压软件有问题，从官网下载 7Z 解压软件并安装，将其设置成默认解压软件。 23. 是否修改程序就需要重新生成模型？ 解决方案： 语音部分程序未做修改（播报音、唤醒词、命令词、回复词等未修改），只修改了程 …[截断,原长3973]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:46）

Excellent — the forum thread reveals the official Yuque knowledge base structure. Let me get the full FAQ list and search for the beginner mode and serial doc.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

I now have the official FAQ confirming 入门模式 (there's a forum post mentioning "入门模式打开范例代码" and the software has 配置模式/编程模式, and 入门模式 mentioned in display_code.php where projects are tagged 专业/入门). Let me confirm the "入门模式" and 编辑模式 (配置模式 = 图形化/入门) terminology.

Actually the manual says "配置模式" and "编程模式". The homepage said "图形化界面编程（入门模式）". And display_code.php tags works as "入门" and "专业". So 入门模式 = 配置模式 (graphical, no programming needed).

Let me verify the yuque doc links resolve and check the serial-specific knowledge base doc. Also let me quickly search for official docs site (dolphin666.github.io/docs is the API docs - it's under a user's github, likely the official author dolphin who is a forum moderator). Let me check the yuque doc for串口.

Let me fetch one of the yuque doc URLs to confirm it's about serial, and try the yuque book API via the web with proper params. Actually let me try fetching the yuque doc page directly.

Let me also check the twen51 docs - the online programming page /C51/asr_pro.php. And check the official "ASRPRO 串口模块" page. And verify the 入门模式 terminology.

Let me be efficient — I have enough. Let me do a few targeted confirmations:
1. yuque doc list (try fetch with the doc URL)
2. official docs site dolphin666.github.io/docs - check if it's referenced by official (it's linked from learnSource.php?id=68, so official)
3. 入门模式 confirmation

Let me fetch the yuque serial doc and the docs site API.

</details>

- 🔧 **WebFetch** `{"prompt": "这个页面标题和内容是什么？是否是天问ASRPRO知识库的文档？如果是，摘录正文要点。列出页面上所有指向 yuque.com/twen51/asrpro 的文档链接。", "url": "https://www.yuque.com/twen51/asrpro/ql140qk6w17ulhou"}` → `Based on the provided content, the page title is "七、【ASRPRO串口驱动】串口驱动等异常", and it appears to be from 语雀 (Yuque). There is no body content included in what you shared, only the title. Therefore I cannot confirm whether it belongs to a "天问ASRPRO知识库", nor can I extract any main points or body text. Additionally, no links p …[截断,原长415]`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && echo \"=== docs site (dolphin666) ===\"; curl -s -L -m 25 \"https://dolphin666.github.io/docs/\" -o docs_home.html; head -c 600 docs_home.html; echo; echo \"=== try README / _sidebar ===\"; for p in \"README.md\" \"_sidebar.md\" \"index.html\"; do echo \"-- $p --\"; curl -s -L -m 15 \"https://dolphin …[截断,原长414]` → `=== docs site (dolphin666) === <!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <title>澶╅棶51 API鏂囨。</title> <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" /> <meta name="description" content="Description"> <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1. …[截断,原长1665]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:46）

Let me verify the Yuque knowledge base and the official docs site, plus the beginner-mode wording.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The docs site is the official 天问51 API文档 on GitHub Pages (dolphin666.github.io). Let me get the full sidebar and check if there is an ASRPRO section. Also let me get the learnSource.php?id=65 (associated resources) and check the online programming page. Let me fetch the sidebar README fully.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && curl -s -L -m 15 \"https://dolphin666.github.io/docs/README.md\" -o docs_readme.md; /c/ProgramData/anaconda3/python.exe -c \"\nimport sys;sys.stdout.reconfigure(encoding='utf-8')\nprint(open('docs_readme.md',encoding='utf-8').read())\n\"", "description": "Read official API docs index"}` → `## 天问51 API文档 <!-- {docsify-ignore-all} --> - [C51编程手册](C51/C51.md) - [STC12编程手册](STC12/STC12.md) - [STC15编程手册](STC15/STC15.md) - [STC8编程手册](STC8/STC8.md) - [STC16编程手册](STC16/STC16.md) - [STC32G编程手册](STC32G/STC32G.md) - [CH32V003编程手册](CH32V003/CH32V003.md) - [CH32V103编程手册](CH32V103/基础外设模块.md) - [CH57X编程手册](CH57X/CH57X. …[截断,原长547]`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && curl -s -L -m 20 \"http://twen51.com/new/twen51/learnSource.php?id=65\" -o t_learn65.html; node -e \"\nconst fs=require('fs');const d=fs.readFileSync('t_learn65.html','utf8');\nlet t=d.replace(/<script[\\s\\S]*?<\\/script>/g,'').replace(/<style[\\s\\S]*?<\\/style>/g,'').replace(/<[^>]+>/g,' ').replac …[截断,原长414]` → ` --> --> --> 天问五幺官网 - 一站式单片机开发 首页 在线编程 发现 课程 学校 我的学校 我的班级 课堂作业 资料 软件 社区 登录 注册 --> 个人资料 班级管理 --> 登录 LOGIN 手机号码: * --> 验证码: 登录 登录 忘记密码 --> 忘记密码 手机号登录 免费注册 注册 REGIST 注册 当前位置： 首页 天问Block 天问51开发板学习资料专区 天问51开发板 ASRPRO 天问51开发板 全球第一款带USB的STC51全功能开发板，采用STC8H8K64U芯片，支持USB、ADC、PWM、SPI、IIC等，最强大51开发板。硬件百分之百国产，好好搭搭平台支持图形化配置和编程，支持图形化 …[截断,原长2680]`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && for p in \"ASRPRO/入门模式编程说明.md\" \"ASRPRO/ASRPRO.md\" \"ASRPRO/_sidebar.md\"; do echo \"=== $p ===\"; curl -s -L -m 20 \"https://dolphin666.github.io/docs/$p\" -o \"asrdoc.md\"; /c/ProgramData/anaconda3/python.exe -c \"\nimport sys;sys.stdout.reconfigure(encoding='utf-8')\nprint(open('asrdoc.md',encod …[截断,原长414]` → `=== ASRPRO/入门模式编程说明.md === <!DOCTYPE html> <html> <head> <meta http-equiv="Content-type" content="text/html; charset=utf-8"> <meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; img-src data:; connect-src 'self'"> <title>Page not found &middot; GitHub Pages</title> <style t …[截断,原长5547]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:47）

Key discovery: the official docs site has "ASRPRO/入门模式编程说明.md" and possibly a serial page. Let me fetch the ASRPRO docs.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

This is the official API doc site (dolphin666.github.io/docs) derived from official content. Let me fetch the serial module page (专业模式编程说明_06.md) and the 入门模式 docs. This gives exact block names.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && for p in \"ASRPRO/专业模式编程说明_06.md\" \"ASRPRO/入门模式编程说明_01.md\" \"ASRPRO/标准模式编程说明_03.md\"; do echo \"############ $p ############\"; curl -s -L -m 20 \"https://dolphin666.github.io/docs/$p\" -o d.md; /c/ProgramData/anaconda3/python.exe -c \"\nimport sys;sys.stdout.reconfigure(encoding='utf-8')\nprint(op …[截断,原长414]` → `############ ASRPRO/专业模式编程说明_06.md ############ <!DOCTYPE html> <html> <head> <meta http-equiv="Content-type" content="text/html; charset=utf-8"> <meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; img-src data:; connect-src 'self'"> <title>Page not found &middot; GitHub P …[截断,原长16682]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:47）

This is the official API documentation site with dedicated serial pages. Let me fetch them.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The docs are under a different base path. The README.md referenced "ASRPRO/入门模式编程说明.md" but returns 404. Maybe the docs base is different. Let me check the index.html to see the basePath and the actual folder. Actually README.md loaded from https://dolphin666.github.io/docs/README.md worked. But ASRPRO/... gives 404. Maybe there's a subfolder or the docs are under a different repo path. Let me check the _sidebar.md base and the actual path via github. Let me try listing the GitHub repo.

Actually the sidebar referenced ASRPRO/入门模式编程说明.md - but maybe there's a basePath like /docs/. Let me check index.html config.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && curl -s -L -m 15 \"https://dolphin666.github.io/docs/index.html\" -o di.html; grep -oE 'basePath[^,]*|window\\.\\$docsify[^<]*|name:[^,]*' di.html | head; echo \"---try github API for repo tree---\"; curl -s -L -m 20 \"https://api.github.com/repos/dolphin666/docs/git/trees/master?recursive=1\" | head …[截断,原长414]` → `window.$docsify = { name: '天问51 API文档' ---try github API for repo tree--- { "sha": "0712dbf6e185a58d82f564acbc2b3863711ee119", "url": "https://api.github.com/repos/dolphin666/docs/git/trees/0712dbf6e185a58d82f564acbc2b3863711ee119", "tree": [ { "path": ".nojekyll", "mode": "100644", "type": "blob", "sha": "e69de29bb2d1 …[截断,原长1364]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:47）

The docs sub-pages 404 — likely a basePath issue. Let me inspect the docsify config and find the real paths.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The docsify basePath might differ. The README.md worked at /docs/README.md. But subpages 404. Maybe they need URL encoding. Let me fetch the raw via github raw or the repo tree for ASRPRO files.

Actually since README.md worked from /docs/README.md, the ASRPRO/入门模式编程说明.md should work too but returned 404. Maybe the repo name differs. Let me get the tree listing for ASRPRO.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && curl -s -L -m 25 \"https://api.github.com/repos/dolphin666/docs/git/trees/master?recursive=1\" -o tree.json; /c/ProgramData/anaconda3/python.exe -c \"\nimport json,sys;sys.stdout.reconfigure(encoding='utf-8')\nt=json.load(open('tree.json',encoding='utf-8'))['tree']\nfor e in t:\n p=e['path']\n if 'AS …[截断,原长408]` → `ASRPRO/_sidebar.md 2427 ASRPRO/专业模式编程说明.md 1917 ASRPRO/专业模式编程说明_01.md 4275 ASRPRO/专业模式编程说明_02.md 2764 ASRPRO/专业模式编程说明_03.md 559 ASRPRO/专业模式编程说明_04.md 403 ASRPRO/专业模式编程说明_05.md 581 ASRPRO/专业模式编程说明_06.md 3638 ASRPRO/专业模式编程说明_07.md 1839 ASRPRO/专业模式编程说明_08.md 1518 ASRPRO/专业模式编程说明_09.md 658 ASRPRO/入门模式编程说明.md 1344 ASRPRO/入门 …[截断,原长601]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The GitHub Pages is probably case-sensitive on paths but the markdown is under /docs/ASRPRO/... The 404 might be because GitHub Pages serves only certain paths, or because the file needs URL encoding. Let me fetch raw from github raw.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && for p in \"ASRPRO/入门模式编程说明.md\" \"ASRPRO/入门模式编程说明_01.md\" \"ASRPRO/专业模式编程说明_06.md\" \"ASRPRO/标准模式编程说明_03.md\"; do fn=$(echo \"$p\" | tr '/' '_'); curl -s -L -m 20 \"https://raw.githubusercontent.com/dolphin666/docs/master/$p\" -o \"gh_$fn\"; echo \"#### $p ($(stat -c%s gh_$fn) bytes)\"; done; ls -la  …[截断,原长413]` → `stat: cannot stat 'gh_ASRPRO_入门模式编程说明.md': No such file or directory #### ASRPRO/入门模式编程说明.md ( bytes) #### ASRPRO/入门模式编程说明_01.md (14 bytes) #### ASRPRO/专业模式编程说明_06.md (14 bytes) stat: cannot stat 'gh_ASRPRO_标准模式编程说明_03.md': No such file or directory #### ASRPRO/标准模式编程说明_03.md ( bytes) -rw-r--r-- 1 user 197121 14 Oct 16 …[截断,原长417]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:48）

Let me fetch these official docs from GitHub raw.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Filenames with non-ASCII need URL encoding. Let me use the GitHub API contents endpoint or urlencode.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && cat > fetchdocs.py <<'PYEOF'\nimport json,urllib.parse,urllib.request,sys,os\nsys.stdout.reconfigure(encoding='utf-8')\ntree=json.load(open('tree.json',encoding='utf-8'))['tree']\ntargets=[e for e in tree if e['path'].startswith('ASRPRO/') and e['path'].endswith('.md')]\nos.makedirs('asrdocs',exist_o …[截断,原长414]` → `OK ASRPRO/_sidebar.md 2427 OK ASRPRO/专业模式编程说明.md 1917 OK ASRPRO/专业模式编程说明_01.md 4275 OK ASRPRO/专业模式编程说明_02.md 2764 OK ASRPRO/专业模式编程说明_03.md 559 OK ASRPRO/专业模式编程说明_04.md 403 OK ASRPRO/专业模式编程说明_05.md 581 OK ASRPRO/专业模式编程说明_06.md 3638 OK ASRPRO/专业模式编程说明_07.md 1839 OK ASRPRO/专业模式编程说明_08.md 1518 OK ASRPRO/专业模式编程说明_09.md 658  …[截断,原长670]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:49）

Non-ASCII filenames need URL encoding. Let me use the GitHub API blobs instead.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

 

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\Robot dog 1.1\\_research\\dl\\pkg\\asrdocs\\ASRPRO__专业模式编程说明_06.md"}` → `1 ### 串口模块<!-- {docsify-ignore} --> 2 3 1. #### 串口波特率设置 4 5 ![img](专业模式编程说明.assets/wps93.png) 6 7 ![image-20230406164653760](专业模式编程说明_06.assets/image-20230406164653760.png) 8 9 ![image-20230406164558976](专业模式编程说明_06.assets/image-20230406164558976.png) 10 11 > 支持多路串口和波特率设置，图形化模块下拉框没有需要的波特率，可以自己添加数字模块后修改。 12 > 13 14 15 1 …[截断,原长1979]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\Robot dog 1.1\\_research\\dl\\pkg\\asrdocs\\ASRPRO__入门模式编程说明_01.md"}` → `1 #### 入门模式编程说明 <!-- {docsify-ignore} --> 2 3 4 5 > 入门模式非常适合初学者，会打字就可以学会编程。 6 7 8 9 #### 上电初始状态 <!-- {docsify-ignore} --> 10 11 12 13 ![img](ASRPRO编程手册.assets/wps489.jpg) 14 15 16 17 > 可设置语音播放人音色，通过下拉菜单可选择 18 种不同的音色，包含 14 种中文，4种英文。音量可从下拉菜单选择 2-20 范围内的音量大小，语音播放的快慢也可通过下拉菜单调整。 18 > 19 > 可设置 PA0-PC4 10 个引脚的状态，分别为输入、输出低电平、输 …[截断,原长3447]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:49）

Now let me read the key official API docs: the serial module, beginner mode, and event-trigger (Standard mode) docs.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Now I have the official docs. Let me check the standard mode event trigger docs (词条/唤醒设置) and the standard mode programming doc. Also need the "入门模式" entry point info. Let me read a few more.

Also need to determine:
- Q1: 积木块名称 "语音控制串口输出" / "串口打印" ; category 位置
- Q2: UART1/UART2 pin选择, 默认波特率 9600
- Q4: 唤醒词/命令词, limits 5 / 300

Let me check 标准模式编程说明_02 (唤醒设置) and _04 (执行动作).

Also let me check the 入门模式/标准模式/专业模式 naming: 天问Block has 入门模式(配置模式?)、标准模式、专业模式. Actually earlier the manual said "配置模式" and "编程模式". And the docs sidebar says 入门模式/标准模式/专业模式. Let me verify.

Let me read the remaining docs.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\Robot dog 1.1\\_research\\dl\\pkg\\asrdocs\\ASRPRO__标准模式编程说明_03.md"}` → `1 ### 事件触发<!-- {docsify-ignore} --> 2 3 #### 1.唤醒词识别回复事件 4 5 ![img](ASRPRO编程手册.assets/wps521.jpg) 6 7 8 9 > 事件框里可以放执行模块，如下例： 10 > 11 12 ![img](ASRPRO编程手册.assets/wps522.jpg) 13 14 15 16 #### 2.命令词识别回复事件 17 18 ![img](ASRPRO编程手册.assets/wps523.jpg) 19 20 21 22 > 事件框里可以放执行模块，如下例： 23 > 24 25 ![img](ASRPRO编程手册.assets/wps524.j …[截断,原长2282]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\Robot dog 1.1\\_research\\dl\\pkg\\asrdocs\\ASRPRO__标准模式编程说明_01.md"}` → `1 ### 标准模式编程说明<!-- {docsify-ignore} --> 2 3 > 标准模式下的编程特点在于事件驱动来执行程序，比如当识别到命令词或唤醒词，当端口为高低电平时，当串口接收到数据时的事件，支持同一事件控制多设备。在标准模式同样也可使用入门模式的指令。 4 > 5 6 7 8 ### 语音设置<!-- {docsify-ignore} --> 9 10 > 初始化设置 11 > 12 13 ![img](ASRPRO编程手册.assets/wps514.jpg) 14 15 > 语音模块的播报音支持 18 种人声，包含 14 种中文，4 种英文，音量和语速都支持 10级可调范围。当你选择不同的播报音时，软件会播放 …[截断,原长755]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Now I have the official docs confirming. Let me also check the standard mode event section (_04) for execution actions and the wakeup section (_02), and the 标准模式 _09 (control modules), and especially find whether "添加换行"/"换行" checkbox exists. The official doc says "串口打印，支持不换行与换行" — that confirms the newline option in the 串口打印 block.

Let me check the standard mode 执行动作 (_04) which may describe serial output blocks.

Also I should verify question 3 about download flow (长按下载按钮2秒) — this is likely described in the 天问Block使用说明书. Let me check.

Also question 6: official docs site home URL. It's https://dolphin666.github.io/docs/#/ — hosted on GitHub Pages (dolphin666 = a 天问 staff, likely). Is it linked from the official site? Yes: the ASRPRO resource page linked `https://dolphin666.github.io/docs/#/` as 天问51API文档. So it's official-linked.

Let me read standard mode _04 and _02, plus check 天问Block使用说明书 for download flow.

Let me also get the standard mode doc for 执行动作 which has serial output.

Let me also look for 长按 download button 2 seconds — search forum/other threads.

Let me read the remaining docs quickly.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\Robot dog 1.1\\_research\\dl\\pkg\\asrdocs\\ASRPRO__标准模式编程说明_04.md"}` → `1 ### 执行动作<!-- {docsify-ignore} --> 2 3 4 #### 1.设置板载 LED灯 5 6 7 8 ![img](ASRPRO编程手册.assets/wps543.jpg) 9 10 11 12 > ASRPRO 板载一颗 LED 灯，连接在 PA4 引脚，图形块支持灯的亮灭。如需要更多效果，可以自己通过设置 PWM 模块或者设置引脚电平模块来单独控制 PA4 引脚。 13 14 ![image-20230406154627656](标准模式编程说明_04.assets/image-20230406154627656.png) 15 16 > ASR-ONE 板载一颗共阴 RGB 灯，对应的引脚分别 …[截断,原长1910]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\Robot dog 1.1\\_research\\dl\\pkg\\asrdocs\\ASRPRO__标准模式编程说明_02.md"}` → `1 ### 唤醒设置<!-- {docsify-ignore} --> 2 3 > 设置唤醒退出时间，通过修改参数调整大小。 4 > 5 6 ![img](ASRPRO编程手册.assets/wps518.jpg) 7 8 > 马上唤醒设置好时间退出。 9 > 10 11 ![img](ASRPRO编程手册.assets/wps519.jpg) 12 13 > 马上退出，不能用在中断里。 14 > 15 16 ![img](ASRPRO编程手册.assets/wps520.jpg) 17 18 19 `

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

I now have very comprehensive information. Let me also check the 入门模式编程说明.md main file and the sidebar for exact structure, plus verify the serial_begin field names for UART selection, and check the "入门模式" wording. Also I should verify the 添加换行 field name in the standard mode blocks (the print block with newline checkbox). Let me check the .hd files for the standard mode to find the field name for newline.

Actually from the standard-mode docs: "串口输出支持 16 进制和字符两种输出方式，支持换行和不换行输出" — so there's a 换行/不换行 option. In config mode (配置模式) the docs mention 加"添加换行". Actually the question asks about "添加换行" option. The manual_config says "以串口 0 输出字符串'1'为例...0d 0a 转换16进制为换行" — and for 串口1 it's "1\n". So in config mode the newline is added by writing "\n" in the string. Hmm, but the question specifically asks about "添加换行" checkbox.

Let me search the ex_e (config mode) example for the wakeup block fields — from earlier: asr_easystart_wakeup has serial_bin=String, NAME=hello. No newline field. Let me look at whether there's a newline field in standard mode (asr_id based) examples. The serial_print block in ex_p has no newline field visible; serial_println is separate block type (adds newline). So in 专业模式/编程模式 there are two blocks: "串口打印" (serial_print, no newline) and serial_println.

Wait, the docs say "串口打印，支持不换行与换行" for one block and "打印16进制数自动换行". Hmm. Let me check the serial_println usage and whether it has an option. Actually let me look at the standard mode example files - but ex_p/ex_e are config and 专业(pro). The .hd edittype was asr_pro for ex_p. Let me check if there's a "标准模式" set of blocks.

Actually the important thing: the user asks about "发送字符串时'添加换行'选项". Let me search the manuals and docs for "添加换行" exactly. It wasn't found. Let me search the .hd files and the docs repo for "换行".

Let me search the docs repo for 换行.

Also need to check: does 天问Block have an official online docs site? We found dolphin666.github.io/docs (天问51 API文档) linked from official twen51.com learning page (learning_show.php?id=652 mentioned "天问51API文档"). Actually the link was in learnSource.php?id=68 → learning_show.php?id=652 lists "天问51API文档". Wait, the homepage listed art_show. Let me confirm the "天问51API文档" link is dolphin666.github.io. It was listed as a 学习教程 item. Let me verify by checking the exact href on the ASRPRO resource page. Earlier link extraction from t_learnSource.php_id_68.html gave: learning_show.php?id=652 (知识库汇总), and on the twen51 resource listing "天问51API文档". Actually in learnSource.php?id=65 (天问51), there's "天问51API文档 2024-07-31". And on the homepage nav there might be a direct link. Let me grep the homepage for dolphin666.

Let me do a few final verification searches.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && echo \"=== grep dolphin666 in all cached html ===\"; grep -l \"dolphin666\" *.html 2>/dev/null; grep -oh \"https\\?://[^\\\"'<> ]*dolphin666[^\\\"'<> ]*\" *.html 2>/dev/null | sort -u; echo; echo \"=== grep 换行 in asrdocs ===\"; grep -rn \"换行\" asrdocs/ 2>/dev/null", "description": "Check docs site li …[截断,原长414]` → `=== grep dolphin666 in all cached html === t_learn65.html t_learnSource.php_id_68.html https://dolphin666.github.io/docs/#/ === grep 换行 in asrdocs === asrdocs/\ASRPRO__专业模式编程说明_06.md:36:> 串口打印，支持不换行与换行。 asrdocs/\ASRPRO__专业模式编程说明_06.md:40:> 打印 16 进制数自动换行。 asrdocs/\ASRPRO__标准模式编程说明_04.md:104:> 串口输出支持 16 进制和字符两种输出方式，支持换行和 …[截断,原长345]`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg\" && node -e \"\nconst fs=require('fs');\nconst d=fs.readFileSync('t_learnSource.php_id_68.html','utf8');\nconst i=d.indexOf('天问51API文档');\nconsole.log(JSON.stringify(d.slice(i-400,i+120)));\n\"", "description": "Find API doc link on ASRPRO resource page"}` → `"n class=\"match-p-time pull-right\">2021-01-16</span> </p>\n </a>\n </li>\n <li>\n <a href=\"https://dolphin666.github.io/docs/#/\" target=\"_blank\">\n <p class=\"match-p\"><span class=\"match-p-title\">天问51API文档</span> <span class=\"match-p-time pull-right\">2024-07-31</span> </p>\n "`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:50）

Let me verify remaining specifics: the newline option wording, and whether the official site links the docs site.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Now I have confirmed the official site links https://dolphin666.github.io/docs/#/ as "天问51API文档".

Let me update todos and check a couple remaining items: the "长按下载按钮2秒" question, and whether ESP8266 specifically is mentioned (I found ESP32, micro:bit, Arduino, STM32, STC). Let me check for ESP8266. Also verify the config-mode (入门模式) serial dialog "添加换行" default state — the .hd XML for asr_easystart blocks had serial_bin/String fields but no explicit newline. Let me search the whole ex_e for a newline-ish field near serial.

Actually, let me check the standard/config mode serial fields more carefully. In ex_e example XML, `asr_easystart_recognize` had fields: ASR, IO, IO_mode, IO_status, serial, serial_bin, NAME, huifu. No newline field. Hmm. But the manual says serial output supports 换行/不换行. Let me grep for a field that could be newline in the .hd files.

Let me also check the 标准模式 examples? Actually ex_e is "asr_pro_e" = 入门/配置模式. There's no 标准模式 example set. The mode names: 入门模式 (config mode / easystart), 标准模式, 专业模式. Wait — in the software, modes are 入门模式 and 专业模式. The API docs list 入门模式/标准模式/专业模式.

Let me grep .hd for newline field names.

Also check ESP8266 mentions.

Let me do those in parallel.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && echo \"=== possible newline fields in .hd ===\"; grep -rhoE '<field name=\"[^\"]*(ln|line|wrap|huan|newline)[^\"]*\">[^<]*' --include=*.hd ex_e ex_p | sort -u; echo; echo \"=== serial_bin values ===\"; grep -rhoE '<field name=\"serial_bin\">[^<]*' --include=*.hd ex_e | sort -u; echo; echo \"== …[截断,原长414]` → `=== possible newline fields in .hd === === serial_bin values === <field name="serial_bin">HEX <field name="serial_bin">String === all field names in ex_e serial examples === VOICE_SET, vol, speed, WELCOME, SLEEP, play_vol, mode, second, PIN0, STATE0, PIN1, STATE1, PIN2, STATE2, PIN3, STATE3, PIN4, STATE4, PIN5, STATE5, …[截断,原长481]`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1/_research/dl/pkg/asrpro\" && echo \"=== ESP8266 / 8266 mentions ===\"; grep -rn \"8266\" *.txt 2>/dev/null | head; echo \"(none above = not found)\"; echo; echo \"=== 长按 / 2秒 / 下载按键 in manuals ===\"; grep -n \"长按\\|按键2秒\\|按住.*秒\\|下载按键\" *.txt | head", "description": "Check ESP8266 and long-press download mentions"}` → `=== ESP8266 / 8266 mentions === (none above = not found) === 长按 / 2秒 / 下载按键 in manuals ===`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:50）

I have nearly everything. Let me verify the newline option field and ESP8266 mentions.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The newline option: In the config mode block, the serial output block has fields: IO, IO_mode, IO_status, serial, serial_bin (String/HEX), NAME. There's no explicit newline field in .hd, but the manual says 换行 appears in output as 0d 0a — actually in the config mode, when outputting string "1" it shows 31 0d 0a, meaning it appends newline. And when serial 1 outputs "1\n" it shows... wait, the manual text says "以串口 0 输出字符串"1"为例设置程序如图：串口输出显示为"1"，勾选 16 进制显示，串口输出为"31 0d 0a"，其中 1 转换 16 进制为 31，0d 0a 转换 16 进制为换行。" So in config mode, string output auto-appends 0d 0a (newline). Hmm, but is that always? Let me check — serial 1 example output "1\n" also shows 31 0d 0a. So possibly the block has an "添加换行" but it may be default on. Actually the field name for newline might not be in these examples if default. Let me look at the exact serial_print block XML in ex_e more carefully — the block type was asr_easystart_wakeup/recognize with serial/serial_bin/NAME. There's no newline field. So in config (入门) mode, the "添加换行" might be a separate checkbox. Hmm.

Actually the user's question 1 asks about the "添加换行" option and its default state. Let me check the 标准模式/professional mode serial_println. In .hd for ex_p, serial_println block = "串口打印" with 换行; serial_print = 不换行. So the newline is a separate block (println vs print) in professional mode. In standard mode (标准模式), the doc says "串口输出支持 16 进制和字符两种输出方式，支持换行和不换行输出" — likely a checkbox "换行".

Let me check the ex_e serial examples - maybe there's a checkbox defaulting. Actually let me check the professional mode serial.print block fields with newline. Let me look at ex_p 1.串口0输出字符串 more - the block was serial_print with fields serial_select and CONTENT. And in 标准模式 there may be a "换行" checkbox. Hmm.

The user asks specifically about "天问Block 积木块叫什么名字" and "添加换行选项的作用和默认状态". I found:
- Professional/编程 mode: two blocks: 串口打印 (serial_print, no newline) and 串口打印换行 (serial_println, adds newline). And 串口原始输出 (serial_write).
- The manuals say "由于此处没有使用换行指令，所以会在同一行显示" for serial_print in professional mode.
- In config (入门/配置) mode: the serial output is part of the recognition block, with a dropdown for String/HEX. The manual shows output "1" → 31 0d 0a, meaning newline IS appended by default in config mode? Let me verify by reading exact config manual text again for serial 0: "以串口 0 输出字符串"1"为例设置程序如图：串口输出显示为"1"，勾选 16 进制显示，串口输出为"31 0d 0a"". Yes so 0d 0a appended. So config mode appends newline by default (or there's a checkbox default on).

I should be careful and not overstate. I'll report what's documented and note the uncertainty.

Actually, let me double check if there's a "添加换行" checkbox by checking the block definition. The 天问Block is a Blockly fork — the block definitions are in the installed software, not available. But maybe the .hd files contain a field. Let me search more broadly for fields named like "line"/"ln". I did and found nothing. 

Let me also check the 标准模式 ex_e example for a newline flag. The asr_easystart blocks have serial_bin = String/HEX, no newline field. So config mode likely always appends \r\n for string output.

I have enough. Let me also quickly verify the beginner mode entry and compile model time. Let me search for "3分钟" / model generation time and "入门模式" entry via the software.

Actually the user asked "入门模式" (免编程模式) — the official docs confirm 入门模式 exists ("入门模式非常适合初学者，会打字就可以学会编程"). And the official resource page said "图形化界面编程（入门模式）". Good.

Also question 5: Arduino examples. Found appendix in official manual (config + prog), and the official website Arduino_example.php?href=asr_pro (but that's just examples listing). The appendix covers Arduino UNO, STC, STM32, ESP32, micro:bit. No ESP8266 specifically — I'll note that.

Let me quickly check model generation time and login requirements, and the "下载" button vs "编译" distinction. From manual: toolbar has 生成模型 (generate model), 编译下载 (compile+download) as a combined button; also 4M编译下载 / 2M编译下载. And "全编译下载" via VS Code. Login + real-name auth required for 生成模型.

Also there's the "长按下载按钮2秒" — not found in official text. I'll say 未找到.

Let me do one more check: search the whole site for a "串口通信" doc page and confirm the docsify URL format for direct pages. The docsify uses hash routing: https://dolphin666.github.io/docs/#/ASRPRO/专业模式编程说明_06. Let me verify that renders. Actually docsify with #/ route — the page id would be the path. I'll provide both the hash URL and GitHub source URL.

I think I have enough to answer comprehensively. Let me also verify the model generation time claim (3 minutes) — the homepage said "免学习三分钟生成固件". So ~3 min is vendor claim.

Let me quickly confirm the 编译 vs 下载 distinction by reading config manual around line 224-238 (already read: "编译下载范例程序...直接点击编译下载即可"). And toolbar icons. Fine.

One more: question 6 asks for official online docs site home URL and "串口通信" page URL. Answer: https://dolphin666.github.io/docs/#/ (天问51 API文档, linked from official resource page), and serial page: #/ASRPRO/专业模式编程说明_06 (串口模块) and #/ASRPRO/标准模式编程说明_03 (事件触发-串口接收) and #/ASRPRO/入门模式编程说明_01 (串口接收触发/语音控制串口输出).

But wait — dolphin666.github.io is not a *.twen51.com domain; it's an individual GitHub Pages but officially linked from twen51.com resource page as "天问51API文档". So it's official-sanctioned. I should note that.

Also the primary official docs are on Yuque (yuque.com/twen51/...). Let me confirm the ASRPRO yuque knowledge base home and serial doc URL. The forum gave several: https://www.yuque.com/twen51/asrpro/slxywo2hi295viuv (串口驱动), https://www.yuque.com/twen51/asrpro/ql140qk6w17ulhou (串口驱动等异常). Let me quickly verify one is a serial doc. WebFetch earlier confirmed ql140qk6w17ulhou title "七、【ASRPRO串口驱动】串口驱动等异常". Good, that's a serial-related doc.

I have enough. Let me finalize and clean up temp files? Not necessary. Let me just write the answer.

Let me do a final verification of the base download URL and the docsify hash URL working. Actually I'm confident.

Let me also double-check: is there an "添加换行" checkbox in config mode? Let me look at the ex_e config serial output example more carefully — maybe I should check if NAME field there. The block asr_easystart_recognize has NAME=hello. And the manual config 2.1 said output "31 0d 0a". So config mode string output appends CR LF automatically. Good enough — I'll describe carefully.

Now, let me write the final answer in Chinese, organized by the 7 questions with 结论+来源URL+可信度.

Let me finalize. Also I should mention that I downloaded official manuals/example zips locally and give the URLs.

Key URLs:
- 官网首页: http://twen51.com/ (redirects /new/twen51/index.php). Note HTTPS cert mismatch (cert belongs to haohaodada.com), so use http.
- ASRPRO 资料专区: http://twen51.com/new/twen51/learnSource.php?id=68
- ASRPRO 资料下载页: http://twen51.com/new/twen51/learning_show.php?id=565
- ASRPRO 例程页: http://twen51.com/new/twen51/Arduino_example.php?href=asr_pro
- 编程手册(配置模式): http://twen51.com/jpeguploadfile/twen/ASRPRO/asr_pro_e_2024.pdf
- 编程手册(编程模式): http://twen51.com/jpeguploadfile/twen/ASRPRO/asr_pro_2024.pdf
- 范例代码(配置模式): http://twen51.com/jpeguploadfile/twen/ASRPRO/asr_pro_e_2024.zip
- 范例代码(编程模式): http://twen51.com/jpeguploadfile/twen/ASRPRO/asr_pro_2024.zip
- API文档: https://dolphin666.github.io/docs/#/
- 语雀知识库: https://www.yuque.com/twen51/asrpro
- 论坛FAQ: https://haohaodada.com/new/bbs/forum.php?mod=viewthread&tid=734
- 知识库汇总页: http://twen51.com/new/twen51/learning_show.php?id=652
- 天问Block下载页: http://twen51.com/new/twen51/art_show.php?id=230

Now compile the answer.

For Q1 block name: 
- 入门/配置模式(配置模式, asr_pro_e): 在"语音识别事件块"（唤醒词/命令词块, 内部字段 serial / serial_bin / NAME）里选择"串口"下拉 + 输出模式(String/HEX) + 输出内容。The recognition block is 语音控制唤醒词命令词块. In config manual it's called "语音控制继电器输出字符串命令模块" / "语音控制唤醒词输出16进制命令模块". The IDE categorizes under 配置模式指令区. Hmm, need the actual block display name. Hard to know exact display text; I'll describe.
- 专业/编程模式(asr_pro): blocks serial_begin (串口初始化/串口波特率设置), serial_print (串口打印/不换行), serial_println (串口打印换行), serial_write (串口原始输出).
- 标准模式: 设置串口波特率 + 串口输出(支持16进制/字符, 支持换行和不换行).

For "添加换行": In professional mode, "串口打印"有换行/不换行两种（serial_print vs serial_println），and manual says 未使用换行指令会在同一行显示 → default is 不换行 (no newline) for 串口打印; the separate 换行 block adds \r\n. For character/string in config mode, output shows 0d 0a (auto newline). I'll present it carefully and mark 中 confidence for the exact checkbox wording.

Let me write final.

Actually, let me reconsider Q1: user asks "做「语音识别 → 串口发送」的积木块叫什么名字？在积木分类的哪个位置？". In config mode the combined block is under 语音识别/指令区. In professional mode, use 串口 category. The serial发送 block names: 串口打印 (serial_print) / 串口打印换行 / 串口原始输出 (serial_write). Category: 串口 (专业模式) — from 专业模式编程说明_06 串口模块. Good.

Now I'll produce the final answer. I'll also give the local downloaded file paths.

Let me note confidence levels:
- Q1: 高 (from official manuals PDF + official API docs + actual .hd XML)
- Q2: 高 (official manual + docs + .hd)
- Q3: 中-高 (manual + FAQ; login/实名 confirmed; model gen time ~3min from官网宣传语)
- Q4: 高 (manual + docs)
- Q5: 高 for Arduino/STM32/STC/ESP32/micro:bit; ESP8266 specifically 未找到
- Q6: 高 (docs site linked from official page; yuque official)
- Q7: 高 (docs + homepage mention 入门模式)

Write it.

</details>

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-16 20:50）

我已完成调研。以下是逐条结论（所有结论均来自官方来源；我还实际下载并解析了官方手册 PDF 与官方范例工程的 .hd 源文件）。

---

## 0. 官网真实域名（先确认）

- 真实主域是 **`twen51.com`**（不是 .cn）。`http://twen51.com/` 会 302 跳到 `/new/twen51/index.php`。
- 注意：`twen51.com` 的 **HTTPS 证书不对**（证书 altnames 是 `haohaodada.com`），所以浏览器/工具走 https 会报证书错误，请用 **http** 访问。
- `twen51.cn / wiki.twen51.com / docs.twen51.com / wiki.haohaodada.com` 均**不存在**（DNS 解析失败）。
- 官方主站与论坛共用 `haohaodada.com` 服务器（好好搭搭为该生态论坛/平台）。
- 来源：`http://twen51.com/` — **可信度：高**（curl 实测 302 + 页面正文确认为"天问五幺官网-杭州天问五幺科技有限公司"）。

---

## 1. 「语音识别 → 串口发送」积木块名称与位置

天问Block 有 **3 种编程模式**，串口块形态不同：

**（A）入门/配置模式（官方称"配置模式"，文件名 `asr_pro_e`）** — 免编程的合并式积木
- 积木就是**"语音识别事件块"**本身（唤醒词块 / 命令词块），块内直接内嵌串口参数：下拉选 **串口（Serial/Serial1/Serial2）** + **输出模式**（String 字符串 / HEX 十六进制）+ **输出内容输入框**。
- 官方手册里的叫法：**"语音控制唤醒词输出命令模块""语音控制命令词输出字符串命令模块"**。
- 位置：配置模式的**"指令区"**（页面左侧指令区，拖到"编程区"组合）。
- 来源：配置模式手册 `asr_pro_e_2024.pdf`（范例 2.1~2.4）+ 官方范例工程 `asr_pro_e_2024.zip/2.串口范例/*.hd`（块类型 `asr_easystart_wakeup` / `asr_easystart_recognize`，字段 `serial`、`serial_bin`、`NAME`）。**可信度：高**

**（B）专业/编程模式（官方称"编程模式"，文件名 `asr_pro`）** — 独立串口积木，位于**"串口"分类**：
- **串口波特率设置 / 串口初始化**（块 `serial_begin`）
- **串口打印（不换行）**（块 `serial_print`）
- **串口打印（换行）**（块 `serial_println`）
- **串口原始输出**（块 `serial_write`，用于发 16 进制）
- 来源：官方 API 文档《专业模式编程说明_06 串口模块》+ 官方范例工程 `.hd` 实测块类型。**可信度：高**

**（C）标准模式** — 用"事件驱动"块：唤醒词/命令词事件块内放**"串口输出"**执行块（支持 16 进制/字符两种输出、支持换行/不换行）。
- 来源：官方 API 文档《标准模式编程说明_03 事件触发》《_04 执行动作》。**可信度：高**

**"添加换行/换行"选项的作用与默认状态：**
- 专业模式下，换行是**由积木本身区分**的：`串口打印`=不换行、`串口打印（换行）`=自动补 `\r\n`（0x0d 0x0a）。官方原话："**由于此处没有使用换行指令，所以会在同一行显示**"——即**默认不换行**，需换行要另加换行块。
- 配置模式下串口输出**默认带 `0d 0a` 换行**：手册明确"串口输出字符串'1'…勾选 16 进制显示为 `31 0d 0a`，其中 `0d 0a` 转换 16 进制为换行"。
- 关于是否有一个名叫"**添加换行**"的独立勾选框：官方文档未出现该字样（原词为"换行/不换行"），且我解析的官方 .hd 里**没有 newline 字段**（配置模式按默认补 CRLF）。**可信度：高（作用与默认状态）；"添加换行"这一确切 UI 措辞：未找到，中等。**

---

## 2. UART1/UART2 选择与波特率

**引脚（官方原文）：**
- 串口0 = `Serial`，TX=**PB5**、RX=**PB6**，**固定不可改**，是程序下载口。
- 串口1 = `Serial1`，默认 TX=**PA2**、RX=**PA3**；可改的 TX 有 PA_2/PA_7/PB_7，RX 有 PA_3/PB_0/PC_0。
- 串口2 = `Serial2`，默认 TX=**PA5**、RX=**PA6**；可改的 TX 有 PA_5/PB_1/PB_6，RX 有 PA_6/PB_2。
- 官方提示：ASRPRO-Plus 上 PA5/PA6/PC0/PB7 可能被板载模块占用，若冲突建议串口1/2 改用 `PB_7(TX1)/PC_0(RX1)`。

**怎么选：** 在"串口初始化/波特率设置"块（或配置模式识别块内）的下拉框选 **Serial1 / Serial2**，再选 TX/RX 引脚。官方 .hd 实测字段：`<field name="serial_select">Serial1</field><field name="TX">PA_2</field><field name="RX">PA_3</field>`。

**波特率：**
- **默认 9600 8N1**（官方文档原话：串口0"串口参数默认为：波特率 9600 8N1"）。
- **可以改成 115200**：手册多次写明"比较常用的波特率有 9600，57600，115200 等等"，且"图形化模块下拉框没有需要的波特率，**可以自己添加数字模块后修改**"。
- 来源：配置模式手册 + 编程模式手册 + 官方 API 文档《标准模式编程说明_03》"串口参数默认为：波特率 9600 8N1"。**可信度：高**

---

## 3. 编译/下载流程

- **是否要登录**：编译下载本身可用；但**"生成模型"必须登录账号并完成实名认证**（一个手机号只能绑一个账号）。官方原话："在使用生成模型功能时，需要登录账号（没有账号可进行免费注册）并进行实名认证。"
- **是否要联网生成模型**：**要**。语音模型/TTS 是云端合成（FAQ 提到生成模型失败可能是"本地网络原因、服务器异常"，可尝试把网络协议从 https 切到 http）。纯逻辑改动（未改唤醒词/命令词/回复词/播报音）**无需重新生成模型**，直接编译下载即可。
- **生成模型耗时**：官网宣传语为"**免学习三分钟生成固件**"（约 3 分钟量级，官方宣传口径）。来源：官网首页文案。**可信度：中**（官方宣传，未给精确基准）。
- **"编译"与"下载"按钮区别**：
  - 工具栏有**"生成模型"**和**"编译下载"**按钮；"编译下载"是**一体化**按钮（先编译再烧写），还分 **2M 编译下载 / 4M 编译下载**（在"更多→设置→编译模式"里切换；ASRPRO 基础/核心板=2M，ASRPRO-Plus=4M，程序大时须选 4M）。
  - 另有**"全编译下载"**：在 VS Code 里对 `asr_pro_sdk/.../Rebuild.bat` 执行 `./rebuild`，完成后弹出烧写工具点"烧写"。
  - 下载后若要再次下载：FAQ 说"按好搭酷运行键/重新插拔"等；**"长按下载按钮2秒"这一说法在官方文档中未找到**（未找到）。
- **串口下载步骤（官方手册）**：①接喇叭（核心板另接咪头）→②用 **STC-LINK** 接电脑，Type-C 供电（鹿小班/Plus 板载 CH340，可一根 Type-C 一键下载）→③上电播报欢迎词→④软件里选对 COM 口→⑤点"编译下载"。下载口是串口0（PB5/PB6）。
- **独立下载工具**：安装目录 `天问Block/asrpro/` 下 `makebin.exe`（下载工具）+ `fw.bin`（固件），可脱离 IDE 直接烧写。
- 来源：配置/编程模式手册 + 官方 FAQ 帖 tid=734 + 天问Block 下载页。**可信度：高**（"约3分钟"为**中**）。

---

## 4. 唤醒词与命令词配置

- **配置位置/写法**：在识别事件块中填写"识别词 + 词条类别（唤醒词/命令词）+ 回复语"。
  - 专业模式 .hd 实测：`<field name="ASR">天问五幺</field><field name="leibie">唤醒词</field><field name="huifu">我在呢</field><field name="id">0</field>`。
  - 官方文档措辞（事件块）：**"当识别到【命令词】/唤醒词时执行…"**，事件框里可放执行模块。
- **数量限制（官方原文）**：
  - **唤醒词最多 5 个**；**命令词最大 300 个**（"根据芯片容量的不同"）。
  - **语音自学习（方言）最多支持 10 条自定义语音**（学习唤醒词/命令词/删除：说"学习命令词""我要删除"等；断电不丢失）。
- **是否支持自定义/拼音/方言**：
  - **自定义**：支持，输入框可自由改词条与回复语；回复语为 TTS，可较长、可带标点。
  - **方言**：支持**自学习**（"学习的唤醒词可以是普通话，也可以是方言"）。
  - **多音字/拼音**：支持拼音标注。官方 FAQ 原文：`[=*]` 表示前一汉字指定拼音（如 `打开空调[=tiao2]`，数字 1~5 表音调）；`[n*]` 标记数字发音（`1300[n1]`=号码读法，`1300[n2]`=数值读法）。
  - 词条规范：中文词只能由汉字组成、不能有空格逗号；数字须用汉字（"调高一度"）；建议 4 个字最佳。
- 来源：配置模式手册（唤醒词≤5、命令词≤300）+ 编程模式手册（自学习、方言、多音字）+ 官方 FAQ tid=734。**可信度：高**

---

## 5. ASRPRO 与 Arduino/ESP32/ESP8266 通信示例

**官方提供了专门的"与其他单片机串口通讯"附录（手册附录二）**，覆盖：Arduino UNO(5V)、STC8(5V)、STM32(3V)、ESP32/掌控板(3V)、micro:bit(3V)。
- 通用要点（官方原文）："ASRPRO 有 3 组串口，**UART0 预留为程序升级接口**…如需和其它 MCU 通讯**建议使用 UART1 或者 UART2**"；ASRPRO IO 为 **3.3V**，建议 TX/RX 内部上下拉无效、TX 设开漏、外接上拉到 5V 并串电阻。

**官方 Arduino 示例（手册附录二，原文可直接用）：**
```cpp
// Arduino 端接收 ASRPRO 串口命令并控制引脚
#include <SoftwareSerial.h>
SoftwareSerial mySerial(10, 11); // RX, TX
String value;
#define LED_PIN 13
#define RELAY_PIN 12
void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  pinMode(RELAY_PIN, OUTPUT);
}
void loop() {
  if (mySerial.available()) {
    value = mySerial.readString();
    Serial.println(value);
    if (value == "LED ON")        digitalWrite(LED_PIN, HIGH);
    else if (value == "LED OFF")  digitalWrite(LED_PIN, LOW);
    else if (value == "RELAY ON") digitalWrite(RELAY_PIN, HIGH);
    else if (value == "RELAY OFF")digitalWrite(RELAY_PIN, LOW);
  }
}
```
反向（Arduino→ASRPRO 播报）：`mySerial.print("TempAdd"); delay(5000); mySerial.print("TempSub");`，ASRPRO 收到即播报"温度增加一度/减小一度"。
- ESP32 部分用的是**掌控板**（P15/P16 接 ASRPRO PB6/PB5），控制掌控板板载 RGB；**没有单独的 ESP8266 专章**（未找到 ESP8266 字样的官方示例）。
- 另外官网有"**ASRPRO(例程)**"专区（例程下拉可选 ASRPRO 等 30+ 硬件），范例代码 223+ 条。
- 来源：编程模式手册附录二 / 配置模式手册附录二（页 339-357）+ `http://twen51.com/new/twen51/Arduino_example.php?href=asr_pro`。**可信度：高（Arduino/STM32/STC/ESP32/micro:bit）；ESP8266 专例：未找到。**

---

## 6. 官方在线文档站

**有两套官方/官方钦定的在线文档：**

1. **天问51 API 文档（docsify 站点）** — 首页直接由官网"ASRPRO 学习资料专区"挂链（"天问51API文档 2024-07-31"）：
   - 首页：`https://dolphin666.github.io/docs/#/`
   - **串口模块页**：`https://dolphin666.github.io/docs/#/ASRPRO/专业模式编程说明_06`（"串口模块"，讲波特率/原始输出/打印换行/读串口）
   - 事件触发-串口接收页：`https://dolphin666.github.io/docs/#/ASRPRO/标准模式编程说明_03`
   - 入门模式（含"串口接收触发事件指令""语音控制串口输出"）：`https://dolphin666.github.io/docs/#/ASRPRO/入门模式编程说明_01`
   - 源码仓库（可直读 md）：`https://github.com/dolphin666/docs`（路径 `ASRPRO/*.md`）
   - 说明：域名是 GitHub Pages 个人站，但被 twen51.com 官网正式列为"天问51API文档"，故属官方发布渠道。**可信度：高**

2. **语雀官方知识库**（天问五幺实名认证账号运营）：
   - ASRPRO 语音芯片专属知识库：`https://www.yuque.com/twen51/asrpro`
   - 串口驱动等异常：`https://www.yuque.com/twen51/asrpro/ql140qk6w17ulhou`
   - 串口不显示/驱动失败：`https://www.yuque.com/twen51/asrpro/slxywo2hi295viuv`
   - 另有关联库：天问Block `yuque.com/twen51/twblock`、AI `yuque.com/twen51/ai`、TW-TTS `yuque.com/twen51/tw-tts`、ESP32C3 `yuque.com/twen51/esp32c3`
   - 知识库汇总页（官网）：`http://twen51.com/new/twen51/learning_show.php?id=652`。**可信度：高**

（注：**没有** `wiki.twen51.com` / `docs.twen51.com` 这种域名的文档站。）

---

## 7. "入门模式"（免编程模式）

- **有**。官方 API 文档专设《**入门模式编程说明**》，原文："**入门模式非常适合初学者，会打字就可以学会编程**"；官网首页功能栏也写"**图形化界面编程（入门模式）** 零基础入门，快速上手"。
- **入口**：天问Block 左侧/菜单可切换编程模式（入门模式 / 标准模式 / 专业模式，亦对应"配置模式/编程模式"叫法）；在"更多→设置"等处切换。配置模式手册："本教程是配置模式教程，因此需要**切换成配置模式**"。
- 入门模式积木：上电初始状态、唤醒词/命令词识别事件、引脚高低电平触发、**串口接收触发**（这四类都在《入门模式编程说明_01》里）。
- 来源：`https://dolphin666.github.io/docs/#/ASRPRO/入门模式编程说明` + 官网首页 + 配置模式手册。**可信度：高**

---

## 官方示例（核心积木/代码摘录）

**A. 官方"串口1输出字符串"配置模式工程 `.hd`（原文 XML，来自官方 `asr_pro_e_2024.zip`）：**
```xml
<block type="asr_easystart_setup">
  ... <field name="baud1">9600</field><field name="TX_1">2</field><field name="RX_1">3</field> ...
</block>
<block type="asr_easystart_wakeup">
  <field name="ASR">天问五幺</field>
  <field name="serial">Serial1</field><field name="serial_bin">String</field>
  <field name="NAME">hello</field><field name="huifu">我在呢</field>
</block>
<block type="asr_easystart_recognize">
  <field name="ASR">打开继电器</field><field name="IO">4</field><field name="IO_mode">高电平</field>
  <field name="serial">Serial1</field><field name="serial_bin">String</field><field name="NAME">on</field>
</block>
```
即：**唤醒词"天问五幺"→ 串口1 发字符串 "hello"；命令词"打开继电器"→ 串口1 发 "on"**（另有 "off"）。

**B. 官方"串口1输出字符串"专业模式工程 `.hd`（来自官方 `asr_pro_2024.zip`）核心块：**
```xml
<!-- 初始化 -->
<block type="serial_begin">
  <field name="serial_select">Serial1</field><field name="TX">PA_2</field><field name="RX">PA_3</field>
  <field name="baud">9600</field>
</block>
<!-- 识别后发送 -->
<block type="serial_print">
  <field name="serial_select">Serial1</field>
  <value name="CONTENT"><block type="text"><field name="TEXT">hello</field></block></value>
</block>
```
对应的官方字符代码（手册给出）：`setPinFun(15,SECOND_FUNCTION); setPinFun(16,SECOND_FUNCTION); Serial1.begin(9600);`

**C. 官方范例工程目录（已确认存在，可直接在软件"打开范例代码"里调用）：**
- 配置模式 `2.串口范例`：串口0/1/2 输出字符串、0-1-2 同时输出、输出16进制、串口0/1/2 接收字符串/十六进制打开继电器（共 14 个）。
- 编程模式 `2.串口范例`：同上 14 个（独立串口积木版）；另有 `3.多线程范例/2.串口多线程发送程序`、`3.串口多线程接收程序`。

---

### 本地已下载的官方一手资料（可直接复核）
- 配置模式手册：`C:\Users\UserX\Downloads\Robot dog 1.1\_research\dl\pkg\asrpro\manual_config.txt`（PDF: `asr_pro_e_2024.pdf`）
- 编程模式手册：`...\asrpro\manual_prog.txt`（PDF: `asr_pro_2024.pdf`）
- 官方范例工程：`...\asrpro\ex_e\`（配置模式）、`...\asrpro\ex_p\`（编程模式）
- 官方 API 文档 md：`...\asrpro\asrdocs\`
- 原始下载地址（http，非 https）：
  - `http://twen51.com/jpeguploadfile/twen/ASRPRO/asr_pro_e_2024.pdf`
  - `http://twen51.com/jpeguploadfile/twen/ASRPRO/asr_pro_2024.pdf`
  - `http://twen51.com/jpeguploadfile/twen/ASRPRO/asr_pro_e_2024.zip`
  - `http://twen51.com/jpeguploadfile/twen/ASRPRO/asr_pro_2024.zip`

### 未找到 / 存疑项
- "**添加换行**"这一确切勾选框名称：官方文档未用此词（用"换行/不换行"），未见独立勾选框字段。
- "**长按下载按钮2秒**"：官方文档未出现该说法。
- **ESP8266 专属官方示例**：未找到（官方外设示例为 Arduino UNO / STC8 / STM32 / ESP32(掌控板) / micro:bit）。
- **生成模型精确耗时**：仅官网宣传"三分钟生成固件"，非精确基准；且需登录+实名+联网。
