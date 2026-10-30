# 子代理会话 sess_subagent_agent_c18f806e-93ae-4f3e-8906-b120bb2d280b

模型: deepseek-v4.1-flash

## 👤 用户（2026-10-08 23:57）

Task: find the ORIGINAL open-source project behind a Chinese hobby robot-dog codebase, so I can compare servo gait numbers with a modified copy.

The project is an ESP8266 (NodeMCU) desktop quadruped robot called "EDA-Robot", PlatformIO + LittleFS, with U8g2 SSD1306 OLED, ESPAsyncWebServer, 4 servos, and web pages index.html/control.html/engine.html/setting.html. It is very likely published on 立创开源硬件平台 (oshwhub.com), GitHub, or Gitee, possibly accompanying a Bilibili video or CSDN article.

Do at least 6-10 distinct web searches (mix Chinese and English), and fetch the most promising pages. Try queries such as:
- "EDA-Robot" 机器狗
- EDA-Robot ESP8266 桌面机器狗
- 立创开源 机器狗 ESP8266 舵机 U8g2 心知天气
- oshwhub 机器狗 esp8266
- "桌面机器狗" ESP8266 LittleFS ESPAsyncWebServer
- github 机器狗 esp8266 littlefs u8g2 舵机
- 电子diy 机器狗 4舵机 网页控制 esp8266
- distinctive code strings: "回收机器狗" (a button label in control.html), "drawXBMP(0, 0, 128, 64, dowhat)", "servo2.write(140)", "toplefthand"
- EDA-Robot 心知天气 API key SB3j4zrxZ7nuRXv8v

Report back concisely:
1. Best-matching original project URL(s) with what it is.
2. If found, quote VERBATIM the original bodies of: front(), back(), left(), right(), sitdown(), lie(), toplefthand(), toprighthand(), dosleep() — all servoN.write() numbers and delay()s in order. Also the original servo attach() lines with pulse widths (e.g. attach(engine1, 500, 2500)).
3. State explicitly whether in the original, the left-side and right-side legs receive the SAME servo numbers or MIRRORED/complementary numbers (e.g. 40 vs 140) in front()/back().
4. Any info on servo mounting orientation (mirrored left/right vs all identical) and which value (<90 or >90) swings a leg forward.
5. If nothing is found, say so plainly, list the URLs you actually checked, and note the closest similar projects.

Do not invent code you did not see. Mark anything uncertain as uncertain. If search tooling fails, retry a few different queries before giving up, then report what you tried.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Let me start by looking at the local codebase to understand the distinctive strings, then do web searches.

Let me first check the working directory to understand what we have.

The task is: find the ORIGINAL open-source project behind a Chinese hobby robot-dog codebase. I have web search... wait, I don't have a WebSearch tool listed. I have WebFetch. Let me check the tools: AskUserQuestion, Bash, Edit, Read, Skill, TaskOutput, TaskStop, TodoRead, TodoWrite, WebFetch, Write, RespondToCoordinator, ReadSessionContext, CreateWorkflow, AmendWorkflow, SaveWorkflow, EvalWorkflowSnippet, ListWorkflowRuns, GetWorkflowRun, ResumeWorkflowRun, ResolveWorkflowQuestion, ListSavedWorkflows, ListModels, mcp__node_repl__js.

No WebSearch tool. But I can use WebFetch with search engine URLs, e.g., Bing search URLs: https://www.bing.com/search?q=... or DuckDuckGo html: https://html.duckduckgo.com/html/?q=... WebFetch fails on some things but let's try. Also Bash may have curl available — I can use curl to fetch search results. That's probably more reliable. Let's use curl through Bash.

Let me first explore the local directory to extract the distinctive strings.

Plan:
1. Local recon: list files, grep for servo writes, button labels.
2. Web searches with curl/Bing/Baidu/DuckDuckGo.
3. Fetch promising pages (oshwhub, github, gitee, csdn, bilibili).
4. Report.

Let's start with local recon in parallel with a first search.

</details>

- 🔧 **Bash** `{"command": "find \"C:/Users/UserX/Downloads/Robot dog 1.1\" -type f | head -100", "description": "List files in robot dog project"}` → `C:/Users/UserX/Downloads/Robot dog 1.1/.gitignore C:/Users/UserX/Downloads/Robot dog 1.1/.pio/build/nodemcuv2/.sconsign311.dblite C:/Users/UserX/Downloads/Robot dog 1.1/.pio/build/nodemcuv2/firmware.bin C:/Users/UserX/Downloads/Robot dog 1.1/.pio/build/nodemcuv2/firmware.elf C:/Users/UserX/Downloads/Robot dog 1.1/.pio/ …[截断,原长9716]`

- 🔧 **Bash** `{"command": "curl -s -m 30 -A \"Mozilla/5.0 (Windows NT 10.0; Win64; x64)\" \"https://html.duckduckgo.com/html/?q=%22EDA-Robot%22+%E6%9C%BA%E5%99%A8%E7%8B%97\" | head -c 6000", "description": "DuckDuckGo search for EDA-Robot robot dog"}` → `(Bash completed with no output)`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-08 23:57）

I'll start by reconnoitering the local codebase for distinctive strings, and simultaneously begin web searching.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The DuckDuckGo HTML search returned nothing. Let me try again with different approach. Let me also look at the source files.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1\" && ls -R --ignore=\".pio\" . 2>/dev/null | head -80", "description": "List project files excluding .pio"}` → `.: build_log.txt data/ include/ lib/ platformio.ini src/ test/ ./data: control.html engine.html index.html setting.html ./include: README ./lib: README ./src: image.cpp main.cpp ./test: README`

- 🔧 **Bash** `{"command": "curl -s -m 30 -A \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36\" \"https://www.bing.com/search?q=%22EDA-Robot%22+%E6%9C%BA%E5%99%A8%E7%8B%97\" -o /tmp/bing1.html; wc -c /tmp/bing1.html", "description": "Bing search EDA-Robot robot dog"}` → `189 /tmp/bing1.html`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-08 23:58）

Let me look at the source files and try search engines in parallel.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Bing returned only 189 bytes - probably a redirect. Let me check the content, and read the source files.

</details>

- 🔧 **Bash** `{"command": "cat /tmp/bing1.html; echo \"---\"; curl -s -m 30 -A \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36\" -L \"https://lite.duckduckgo.com/lite/?q=%22EDA-Robot%22\" -o /tmp/ddg1.html; wc -c /tmp/ddg1.html", "description": "Check search responses"}` → `Exit code 1 <html><head><title>Object moved</title></head><body> <h2>Object moved to <a href="https://cn.bing.com/search?q=%22EDA-Robot%22+%E6%9C%BA%E5%99%A8%E7%8B%97">here</a>.</h2> </body></html> --- wc: /tmp/ddg1.html: No such file or directory`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1\" && cat platformio.ini; echo \"=== BUILD LOG HEAD ===\"; head -40 build_log.txt; echo \"=== data/index.html size ===\"; wc -c data/*.html src/*.cpp", "description": "Read platformio.ini and project metadata"}` → `; PlatformIO Project Configuration File ; ; Build options: build flags, source filter ; Upload options: custom upload port, speed and extra flags ; Library options: dependencies, extra library storages ; Advanced options: extra scripting ; ; Please visit documentation for the other options and examples ; https://docs.p …[截断,原长2611]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Let me look at main.cpp to get the served code, and try more search engines. Let me use WebFetch which might work better.

</details>

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1\" && head -80 src/main.cpp", "description": "Read head of main.cpp"}` → `#include <Arduino.h> #include<Servo.h> #include<Wire.h> #include<LittleFS.h> #include<ESP8266WiFi.h> #include<WiFiUdp.h> #include<U8g2lib.h> #include<EspAsyncWebserver.h> #include <image.cpp> #include<NTPClient.h> #include<ArduinoJson.h> #include<ESP8266HTTPClient.h> //按键 #define BUTTON_PIN 2 // GPIO2 引脚 (D4) #define B …[截断,原长2374]`

- 🔧 **Bash** `{"command": "for u in \"https://search.marcia.cc\" ; do echo skip; done; curl -s -m 40 -A \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\" \"https://cn.bing.com/search?q=%22EDA-Robot%22&ensearch=0\" -o /tmp/bing_cn.html; wc -c /tmp/bing_cn.html", "description": "Bing CN search for EDA-Robot"}` → `skip 98167 /tmp/bing_cn.html`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-08 23:59）

Now let me read the local source and run several searches in parallel.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Good, we got a Bing CN search result. Let me parse it. Also let me read the servo action functions in the local project (modified copy) so I can compare.

Let me do a bunch of things: parse bing results, and grep for the servo functions.

</details>

- 🔧 **Bash** `{"command": "cd /tmp && python -c \"\nimport re,html\ns=open('bing_cn.html',encoding='utf-8',errors='ignore').read()\n# extract result blocks\nfor m in re.finditer(r'<h2><a href=\\\"(.*?)\\\".*?>(.*?)</a></h2>', s, re.S):\n url=m.group(1); t=re.sub('<.*?>','',m.group(2))\n print(html.unescape(t)[:100],'||',url[:160])\n\" 2>&1 | head -30", "description": "Parse Bing results"}` → `/usr/bin/bash: line 3: python: command not found`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1\" && grep -n \"void front\\|void back\\|void left\\|void right\\|void sitdown\\|void lie\\|void toplefthand\\|void toprighthand\\|void dosleep\\|attach(\" src/main.cpp | head -40", "description": "Locate gait functions in main.cpp"}` → `502:void front() 529:void back() 556:void left() 597:void right() 638:void sitdown() 647:void lie() 660:void toplefthand() 674:void toprighthand() 689:void dosleep() 845: servo1.attach(engine1, 500, 2500); // 配置舵机PWM，500µs=0度，2500µs=180度 846: servo2.attach(engine2, 500, 2500); 847: servo3.attach(engine3, 500, 2500); 84 …[截断,原长357]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-08 23:59）

Search engine is working. Let me parse results and read the local gait functions.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Python not in bash PATH (per memory note). Let me use full path or use pwsh. Let me find python paths.

Let me read the local gait functions (for reference/comparison, though the task is about finding the original — but reading them helps me know what strings to search and to compare).

Also need to search. Let me find python path.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\Robot dog 1.1\\src\\main.cpp", "limit": 410, "offset": 495}` → `495 u8g2.drawStr(64, 30, temperatureString.c_str()); 496 u8g2.drawStr(64, 50, "Humidity"); 497 String humidityString = String(humidity) + " %"; 498 u8g2.drawStr(64, 60, humidityString.c_str()); 499 } while (u8g2.nextPage()); 500 } 501 } 502 void front() 503 { 504 servo2.write(140); //舵机2旋转至140度 505 servo3.write(40); // …[截断,原长8925]`

- 🔧 **Bash** `{"command": "ls \"C:/Users/UserX/miniconda3/python.exe\" \"C:/Users/UserX/anaconda3/python.exe\" 2>/dev/null; where python.exe 2>/dev/null; ls /c/Users/UserX/AppData/Local/Programs/Python 2>/dev/null", "description": "Locate python interpreter"}` → `Exit code 2`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

I have the local (modified) copy content. Now I need to search the web. Let me try python for parsing — python not found in bash PATH per memory. Let me use pwsh, or just use grep/sed on the HTML. Actually let me use a different approach: use `grep -o` on the HTML.

Let me now do many searches. Let me check what search engines are accessible. Bing CN worked (98KB). Let me extract results.

</details>

- 🔧 **Bash** `{"command": "cd /tmp && grep -o '<h2><a href=\"[^\"]*\"[^>]*>[^<]*' bing_cn.html | sed 's/<h2><a href=\"//; s/\"[^>]*>/ || /' | head -30", "description": "Extract Bing CN results"}` → `(Bash completed with no output)`

- 🔧 **Bash** `{"command": "cd /tmp && curl -s -m 40 -A \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\" \"https://cn.bing.com/search?q=EDA-Robot+ESP8266+%E6%A1%8C%E9%9D%A2%E6%9C%BA%E5%99%A8%E7%8B%97+%E8%88%B5%E6%9C%BA\" -o b2.html; grep -o '<h2><a href=\"[^\"]*\"[^>]*>[^<]*' b2.html | sed 's/<h2><a href=\"//; s/\"[^>]*>/ || /' |  …[截断,原长412]` → `(Bash completed with no output)`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:00）

I have the local copy's code. Now let me parse search results and run multiple searches.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The extraction regex fails. Let me look at the raw HTML structure of bing.

</details>

- 🔧 **Bash** `{"command": "cd /tmp && grep -o 'href=\"http[^\"]*\"' bing_cn.html | grep -v bing.com | grep -v microsoft | sort -u | head -40", "description": "Extract all external URLs from Bing results"}` → `href="http://edachallenge.cn/" href="https://baike.baidu.com/item/EDA%2FIP%E8%A1%8C%E4%B8%9A/67288674" href="https://beian.miit.gov.cn" href="https://beian.mps.gov.cn/#/query/webSearch?code=11010802047360" href="https://blog.csdn.net/coachip/article/details/128718727" href="https://dxzhgl.miit.gov.cn/dxxzsp/xkz/xkzgl/r …[截断,原长641]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The Bing search for "EDA-Robot" gave irrelevant results (about EDA industry). Let me try other search engines and more specific queries. Let me check what search engines are accessible. Let me try:
1. Baidu
2. Sogou
3. DuckDuckGo lite
4. GitHub code search (needs auth maybe)
5. oshwhub search API
6. Gitee search
7. Google

Let me also check the first search result from the failed ddg. Let me test connectivity to various search endpoints.

</details>

- 🔧 **Bash** `{"command": "cd /tmp\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\necho \"=== DDG lite ===\"; curl -s -m 25 -A \"$ua\" \"https://lite.duckduckgo.com/lite/?q=%22EDA-Robot%22\" -o d1.html -w \"%{http_code} %{size_download}\\n\"\necho \"=== Google ===\"; curl -s -m 25 -A \"$ua\" \"https://www.google.com/search? …[截断,原长412]` → `=== DDG lite === 000 0 === Google === 000 0 === Baidu === 302 471 === Sogou === 200 540543 === oshwhub api === 404 0`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:01）

Bing gave irrelevant results. Let me test multiple search engines and direct platform searches.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Sogou works. Baidu redirect. Let me check sogou results.

Also DDG and Google blocked (000 = connection failure). Let me check the sogou output.

Let me also try searx instances.

</details>

- 🔧 **Bash** `{"command": "cd /tmp && grep -o 'href=\"[^\"]*\"' sg1.html | grep -viE 'sogou|weixin|sogoucdn|soso|\\.js|\\.css' | sort -u | head -40; echo \"=== titles ===\"; grep -oP '(?<=<h3[^>]*>).*?(?=</h3>)' sg1.html | sed 's/<[^>]*>//g' | head -20", "description": "Parse Sogou results"}` → `href="#" href="+c,d,a,i)}catch(o){}}};void 0!==window.uigs_pvflag&&window.uigs_pvflag||window.uigs_spv||f(),window.uigs_spv=1;var s=I()?document.body.onclick:document.onclick;I()?document.body.onclick=function(o){var n;return s&&(n=s(o)),g(o),n}:document.onclick=function(o){var n;return s&&(n=s(o)),g(o),n};var p=!1;win …[截断,原长7718]`

- 🔧 **Bash** `{"command": "cd /tmp\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\necho \"=== searx be ===\"; curl -s -m 25 -A \"$ua\" \"https://searx.be/search?q=%22EDA-Robot%22+esp8266&format=json\" -o sx1.json -w \"%{http_code} %{size_download}\\n\"\necho \"=== github code search ===\"; curl -s -m 25 -A \"$ua\" \"https:/ …[截断,原长412]` → `=== searx be === 000 0 === github code search === 200 205977 === gitee search === 301 178`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:02）

Sogou works. Let me parse it and try more engines.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Let me continue. GitHub API works (200, 205977 bytes - that's a search result for EDA-Robot repositories). Let me check that and continue searching. Let me set up a todo list too.

Let me check gh1.json first.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "Recon local project + extract distinctive strings", "status": "completed", "priority": "high"}, {"content": "Run 6-10 web searches (CN + EN) across engines", "status": "in_progress", "priority": "high"}, {"content": "Fetch most promising candidate pages", "status": "pending", "priority": "high"}, {"content": "Compare original vs local gait code, report v …[截断,原长411]` → `{"oldTodos":[],"todos":[{"content":"Recon local project + extract distinctive strings","status":"completed","priority":"high"},{"content":"Run 6-10 web searches (CN + EN) across engines","status":"in_progress","priority":"high"},{"content":"Fetch most promising candidate pages","status":"pending","priority":"high"},{"c …[截断,原长485]`

- 🔧 **Bash** `{"command": "cd /tmp && python3 --version 2>/dev/null || node --version 2>/dev/null; echo \"---GH---\"; node -e \"\nconst j=require('/tmp/gh1.json');\nconsole.log('total',j.total_count);\n(j.items||[]).slice(0,20).forEach(i=>console.log(i.full_name,'|',i.description,'|',i.html_url));\n\" 2>&1 | head -30", "description": "Parse GitHub repo search results"}` → `v24.13.0 ---GH--- node:internal/modules/cjs/loader:1424 throw err; ^ Error: Cannot find module '/tmp/gh1.json' Require stack: - C:\Users\UserX\AppData\Local\Temp\[eval] at Module._resolveFilename (node:internal/modules/cjs/loader:1421:15) at defaultResolveImpl (node:internal/modules/cjs/loader:1059:19) at resolveForCJS …[截断,原长844]`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1\" && grep -o 'href=\"[^\"]*\"' data/control.html | sort -u | head -40; echo \"=== buttons ===\"; grep -oE '(名称|value|onclick)=?[^>]{0,60}' data/control.html | head -30", "description": "Inspect control.html for distinctive strings"}` → `href="./" href="./engine.html" href="./setting.html" === buttons === value { value" id="batteryVoltageDisplay" value" id="batteryPercentageDisplay" onclick="sendCommand('front')" onclick="sendCommand('left')" onclick="sendCommand('right')" onclick="sendCommand('back')" onclick="sendCommand('toplefthand')" onclick="send …[截断,原长843]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:02）

GitHub API works. Let me check those results and continue with more searches.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

/tmp isn't shared between bash and node (node is Windows). Let me use a Windows temp dir path compatible with both. Git Bash /tmp maps to C:\Users\...\AppData\Local\Temp. Let me check by using the actual windows path.

Let me just save files into a working dir like C:/Users/UserX/Downloads/_search or use the bash temp. Actually the issue: node ran and required '/tmp/gh1.json' which node interprets as C:\tmp\gh1.json. The bash /tmp is C:\Users\UserX\AppData\Local\Temp. Interesting - the Windows user is UserX but the path used is C:\Users\UserX. Probably C:\Users\UserX is a junction or the profile dir.

Let me write search scratch files to a fixed dir, e.g. C:/Users/UserX/Downloads/_s4search. But I shouldn't create clutter... A temp dir is fine. Let me use C:/Users/UserX/AppData/Local/Temp/s4search.

Also, the GitHub search returned 205977 bytes - let me re-do with a proper path.

Let me also do a bunch of searches now:
- GitHub code search (needs auth for code search API, but repo search works)
- oshwhub search
- Sogou parse with correct approach

Let me set up a scratch dir and run several queries.

</details>

- 🔧 **Bash** `{"command": "mkdir -p /c/Users/UserX/AppData/Local/Temp/s4s && cd /c/Users/UserX/AppData/Local/Temp/s4s && pwd -W\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\nS=/c/Users/UserX/AppData/Local/Temp/s4s\n# GitHub repo searches\ncurl -s -m 30 -A \"$ua\" \"https://api.github.com/search/repositories?q=%E6%9C%BA%E5 …[截断,原长412]` → `C:/Users/UserX/AppData/Local/Temp/s4s gh1 200 25980 gh2 200 205977 gh3 200 26822`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; mkdir -p $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\n# oshwhub search page attempts\ncurl -s -m 30 -A \"$ua\" \"https://oshwhub.com/search?q=%E6%9C%BA%E5%99%A8%E7%8B%97\" -o $S/osh1.html -w \"osh1 %{http_code} %{size_download}\\n\"\ncurl -s -m 30 -A  …[截断,原长412]` → `osh1 200 434330 osh2 404 0 sg1 302 323 sg2 302 587`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:03）

Node and bash have different `/tmp`. Let me set up a shared scratch dir and run a batch of searches.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Let me parse these. Note the working directory temp is under UserX user. Let me check results.

Interesting: gh2 (EDA-Robot) returned 205977 bytes - that's a lot for a repo search... might be because it matched many things. Let me parse.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S; node -e \"\nconst fs=require('fs');\nfor (const f of ['gh_dog8266.json','gh_edarobot.json','gh_quad.json']) {\n try{\n const j=JSON.parse(fs.readFileSync(f,'utf8'));\n console.log('=====',f,'total',j.total_count);\n (j.items||[]).slice(0,15).forEach(i=>console.log(' ',i.full_name,'|',(i.description||'').slice(0,80),'| …[截断,原长401]` → `===== gh_dog8266.json total 4 ace-trump-tech/MindPaw | 🐕 MindPaw — 基于 ESP8266 的开源桌面四足机器狗，支持语音、手势、网页遥控、豆包 AI 对话与 PAD 情感交互。可选 AI Infra 网 | https://github.com/ace-trump-tech/MindPaw ace-trump-tech/MindPaw-Robot | 🐕 MindPaw — 基于 ESP8266 的桌面级四足机器狗，支持语音交互 (HLK-V20)、手势识别 (OV2640+轻量MLP)、AI 对话 (豆包 | https://github.com/ace-trump …[截断,原长3083]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S; echo \"=== osh1 title/len ===\"; grep -oE '<title>[^<]*</title>' osh1.html; echo \"=== osh1 script data ===\"; grep -oE 'window\\.__[A-Z_]+__' osh1.html | sort -u | head; echo \"=== sg redirects ===\"; head -c 400 sg1.html; echo; head -c 400 sg2.html", "description": "Inspect oshwhub and sogou responses"}` → `Exit code 1 === osh1 title/len === <title>搜索页 - EDA开源硬件平台</title> === osh1 script data === === sg redirects === head: cannot open 'sg1.html' for reading: No such file or directory head: cannot open 'sg2.html' for reading: No such file or directory`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Excellent! Major finding: `pluckypioneer/eda_robotR1` on GitHub — "EDA-Robot 是一个基于 ESP8266 开发的机器狗控制系统". This looks like the exact match. Let me fetch that repo.

Also osh1.html is the oshwhub search page with 434KB - it may contain JS-rendered data. Let me check.

Let me fetch the pluckypioneer/eda_robotR1 repo files.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\ncurl -s -m 30 -A \"$ua\" \"https://api.github.com/repos/pluckypioneer/eda_robotR1\" -o repo_meta.json -w \"meta %{http_code}\\n\"\ncurl -s -m 30 -A \"$ua\" \"https://api.github.com/repos/pluckypioneer/ed …[截断,原长413]` → `meta 200 tree 200 commits 200 FULL: pluckypioneer/eda_robotR1 | stars 1 | created 2025-07-25T13:20:31Z | pushed 2025-07-31T15:26:21Z | fork false | parent undefined | homepage DESC: EDA-Robot 是一个基于 ESP8266 开发的机器狗控制系统，支持通过 Web 界面进行远程控制机器狗的运动、表情显示等功能，并具备电池状态监测、WiFi 配置、时间同步和天气查询等附加功能。 blob 94 .gitignore tree .vscode blob  …[截断,原长675]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:04）

Major hit: `pluckypioneer/eda_robotR1` on GitHub. Let me fetch its files.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

This looks like it. Note: the tree has data/control.html, data/index.html, data/setting.html but NOT engine.html. The local copy has engine.html additionally. So the local copy is a modified/evolved version. Let's fetch src/main.cpp and README.md from the original repo.

Also let me check the README and commit history, and find the original project on oshwhub (the "R1" suggests there may be R0/other versions). Let's also search for other repos by pluckypioneer.

Let me fetch main.cpp raw.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\ncurl -sL -m 40 -A \"$ua\" \"https://raw.githubusercontent.com/pluckypioneer/eda_robotR1/HEAD/src/main.cpp\" -o orig_main.cpp -w \"main %{http_code} %{size_download}\\n\"\ncurl -sL -m 40 -A \"$ua\" \"http …[截断,原长412]` → `main 200 25994 readme 200 3262 control 200 7339 pio 200 621`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\necho \"=== pluckypioneer other repos ===\"\ncurl -s -m 30 -A \"$ua\" \"https://api.github.com/users/pluckypioneer/repos?per_page=100\" -o user_repos.json -w \"%{http_code}\\n\"\nnode -e \"\nconst fs=requ …[截断,原长412]` → `=== pluckypioneer other repos === 200 AI-Voice-Assistant-for-Runners | | fork false | created 2025-10-14 | https://github.com/pluckypioneer/AI-Voice-Assistant-for-Runners Biomedical-signal-processing-and-analysis-STUDY | My Biomedical signal processing and analysis Study Note | fork false | created 2025-10-18 | https:/ …[截断,原长1781]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:05）

Found a very strong candidate. Let me fetch the original source and search for related projects.

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\AppData\\Local\\Temp\\s4s\\orig_README.md"}` → `1 # 基于ESP8266的机器狗 EDA-Robot 项目说明 2 3 ## 项目概述 4 EDA-Robot 是一个基于 ESP8266 开发的机器狗控制系统，支持通过 Web 界面进行远程控制机器狗的运动、表情显示等功能，并具备电池状态监测、WiFi 配置、时间同步和天气查询等附加功能。 5 6 ## 硬件依赖 7 - 主控：ESP8266 开发板（推荐 NodeMCU v2） 8 - 执行机构：4 个舵机（分别连接引脚 14、16、12、13） 9 - 显示设备：SSD1306 128x64 OLED 屏幕（I2C 接口） 10 - 输入设备：2 个按键（引脚 2、15） 11 - 电源：支持电压监测的电池供电模块 12 1 …[截断,原长1810]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S; grep -n \"source\\|立创\\|oshwhub\\|bilibili\\|B站\\|原文\\|开源\\|原作者\\|作者\" orig_README.md", "description": "Search README for original source references"}` → `33:- 错误、晕、嘉立创 LOGO 等特殊状态 86:> **项目基于嘉立创 EDA 开发平台,项目来源于嘉立创平台原作者**`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:05）

Found the original. Let me read the README (for the source link) and compare the gait code.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

This repo (pluckypioneer/eda_robotR1) is itself a derivative — "项目来源于嘉立创平台原作者" (project comes from an original author on the 嘉立创/JLC EDA platform). Note the AP password differs: README says "11451419", local copy says "12345678". Also file sizes differ: local main.cpp 36505 bytes vs orig 25994. Local data/control.html 8877 vs orig 7339. Local has engine.html which orig lacks. So local is a MODIFIED copy (version 1.1), and pluckypioneer is an intermediate published copy.

Wait — actually re-read the task: "find the ORIGINAL open-source project behind a Chinese hobby robot-dog codebase, so I can compare servo gait numbers with a modified copy." The local copy is "Robot dog 1.1" and there's a modified copy. Hmm, the local one might be the modified copy. Either way, I need to find the original.

pluckypioneer/eda_robotR1 says the original is from 嘉立创 (JLC) platform. Let me now compare the gait functions between local and pluckypioneer, and then search oshwhub for the true original.

Let me diff the gait functions.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');\nlet s=fs.readFileSync('orig_main.cpp','utf8');\nconst names=['front','back','left','right','sitdown','lie','toplefthand','toprighthand','dosleep'];\nfor(const n of names){\n const re=new RegExp('void '+n+'\\\\\\\\(\\\\\\\\)\\\\\\\\s*\\\\\\\\{[\\\\\\\\s\\\\\\\\S]*?\\\\\\\\n\\\\\\\\} …[截断,原长410]` → `--- front --- NOT FOUND --- back --- NOT FOUND --- left --- NOT FOUND --- right --- NOT FOUND --- sitdown --- NOT FOUND --- lie --- NOT FOUND --- toplefthand --- NOT FOUND --- toprighthand --- NOT FOUND --- dosleep --- NOT FOUND`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S; grep -n \"attach(\" orig_main.cpp; echo \"=== ap_ssid/pass ===\"; grep -n \"ap_ssid\\|ap_password\\|softAP\\|APIBase\\|defaultWeatherKey\" orig_main.cpp | head -20", "description": "Check original attach lines and settings"}` → `567: servo1.attach(engine1,500,2500); // 连接舵机到指定引脚 568: servo2.attach(engine2,500,2500); 569: servo3.attach(engine3,500,2500); 570: servo4.attach(engine4,500,2500); === ap_ssid/pass === 580: WiFi.softAP(ssid, password); // 设置WiFi为热点模式 583: Serial.println(WiFi.softAPIP()); // 打印WiFi IP地址`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:05）

Found an intermediate derivative. Let me compare gaits and hunt for the true original on oshwhub.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The gait functions may have different formatting. Let me look at the whole original main.cpp around servo writes.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S; grep -n \"void \\|servo[0-9]\\.write\\|servo[0-9]\\.writeMicroseconds\" orig_main.cpp | head -120", "description": "List functions and servo writes in original"}` → `75:void ICACHE_RAM_ATTR handleButtonPress() {//ICACHE_RAM_ATTR用于中断处理函数,存到RAM里 79:void handleWiFiConfig(){ 254:void loadWiFiConfig(){ 286:void fetchWeather(){ 366:void front(){ 367: servo3.write(40); //左前向前旋转50度 368: servo2.write(140);//右后向前旋转50度 370: servo1.write(40); 371: servo4.write(140); 373: servo2.write(90); 374: …[截断,原长2701]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S; wc -l orig_main.cpp; grep -n \"void \" orig_main.cpp", "description": "Count lines and list all original functions"}` → `740 orig_main.cpp 75:void ICACHE_RAM_ATTR handleButtonPress() {//ICACHE_RAM_ATTR用于中断处理函数,存到RAM里 79:void handleWiFiConfig(){ 254:void loadWiFiConfig(){ 286:void fetchWeather(){ 366:void front(){ 392:void back(){ 418:void left(){ 457:void right(){ 489:void sitdown(){ 497:void lie(){ 509:void toplefthand(){ 522:void topri …[截断,原长451]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:05）

Let me extract all the servo motion code from the original properly.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Now let me read the exact original gait functions verbatim with line numbers. Let me read lines 360-540.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\AppData\\Local\\Temp\\s4s\\orig_main.cpp", "offset": 360, "limit": 180}` → `360 String humidityString = String(humidity) + " %"; 361 u8g2.drawStr(64, 60, humidityString.c_str()); 362 } while (u8g2.nextPage()); 363 } 364 } 365 366 void front(){ 367 servo3.write(40); //左前向前旋转50度 368 servo2.write(140);//右后向前旋转50度 369 delay(100); 370 servo1.write(40); 371 servo4.write(140); 372 delay(100); 373 ser …[截断,原长3297]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:06）

Excellent — I have the original gaits. Let me read them verbatim.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Now I have the original. Note the original repo is `pluckypioneer/eda_robotR1` — but the README says "项目基于嘉立创 EDA 开发平台,项目来源于嘉立创平台原作者" (based on JLC EDA platform, from the original author on JLC platform). So this GitHub repo is likely also a copy/derivative of the true original. But wait — its created date is 2025-07-25 whereas the local copy appears newer (v1.1 with LittleFS, battery monitoring ADC, setting.html). Hmm, but the local copy is a MODIFIED copy — likely derived from this one.

Wait actually, let me reconsider. The task says "find the ORIGINAL open-source project behind a Chinese hobby robot-dog codebase". The local "Robot dog 1.1" has extra features (battery ADC, setting.html with weather API key, LittleFS, AP mode config). The GitHub eda_robotR1 has 3 html pages (control, index, setting) — no engine.html! Hmm, and the local has 4 including engine.html.

So eda_robotR1 is closely related but not identical. It's possible eda_robotR1 is an earlier version of the same lineage. Let me check:
- Local: ap_ssid "EDA-Robot", password "12345678", weather key "SB3j4zrxZ7nuRXv8v"
- eda_robotR1: ssid/password variables — README says "EDA-ROBOT" pass "11451419"

Different. So they share ancestry. The README of eda_robotR1 explicitly says it comes from 嘉立创 (JLC) platform original author. So the true original is on oshwhub (立创开源硬件平台) — 嘉立创 = JLCPCB/LCEDA = 立创.

Now I need to find the actual oshwhub original project. Let me search oshwhub.

Let me also check: the local code has `drawXBMP(0, 0, 128, 64, dowhat)` and `toplefthand`. Let me check the local control.html for "回收机器狗".

Let me do a bunch of searches now:
1. oshwhub search via API
2. Baidu search
3. Sogou (with proper handling)
4. CSDN / Bilibili

Let me try the oshwhub search API endpoints. oshwhub.com is the 立创开源硬件平台 (formerly oshwhub.com, now also "oshwhub.com" → "oshwhub"). The search page loads via JS. Let me find the API.

Common API: https://oshwhub.com/api/search/product?q=... or https://pro.lceda.cn/api/...

Actually oshwhub search page: https://oshwhub.com/search?q=xxx — loads via JS from an API like https://oshwhub.com/api/search?key=...

Let me look at the osh1.html content for API hints.

Also try Baidu with proper cookie/UA.

Let me also do a Google search via a proxy or try startpage/mojeek/brave.

Let me try several search engines: mojeek.com, search.brave.com, startpage.com, ecosia, marginalia, and Yandex.

Let me batch these.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\necho \"=== mojeek ===\"; curl -s -m 25 -A \"$ua\" \"https://www.mojeek.com/search?q=%22EDA-Robot%22+%E6%9C%BA%E5%99%A8%E7%8B%97\" -o mj1.html -w \"%{http_code} %{size_download}\\n\"\necho \"=== brave === …[截断,原长413]` → `Exit code 28 === mojeek === 403 352 === brave === 000 0 === ecosia === 301 167 === marginalia === 302 145 === startpage === 000 0 === searxng priv === 000 0`

- 🔧 **Bash** `{"command": "cd \"C:/Users/UserX/Downloads/Robot dog 1.1\" && echo \"=== 回收机器狗 ===\"; grep -n \"回收机器狗\" data/*.html; echo \"=== dowhat ===\"; grep -n \"drawXBMP(0, 0, 128, 64, dowhat)\\|dowhat\" src/main.cpp | head; echo \"=== engine.html title ===\"; grep -oE \"<title>[^<]*</title>|<h[12][^>]*>[^<]*</h[12]>\" data/*.html; echo \"=== local ap/weather ===\"; grep -n \"ap_ssid\\| …[截断,原长412]` → `=== 回收机器狗 === data/control.html:189: <button class="button" onclick="sendCommand('sleep')">回收机器狗</button> === dowhat === 132: server.on("/dowhatstate", HTTP_GET, [](AsyncWebServerRequest *request) 1011: u8g2.drawXBMP(0, 0, 128, 64, dowhat); === engine.html title === data/engine.html:<title>舵机调试界面</title> data/engine.ht …[截断,原长913]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:06）

Found the original lineage. Now let me hunt for the true oshwhub/JLC original and check local distinctive strings.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The local copy is a modified/rewritten version of the GitHub repo `pluckypioneer/eda_robotR1`. But the GitHub repo says the project comes from 嘉立创 (JLC/LCEDA = 立创开源硬件平台 oshwhub). So the true original is on oshwhub. Let me search oshwhub.

Note important differences already:
- Original: `void dosleap()` with servo1.write(0), servo4.write(0), servo3.write(180), servo2.write(180). Local: `void dosleep()` with servo1.write(0), servo3.write(180), servo2.write(180), servo4.write(0).
- Original front(): servo3.write(40) // 左前向前旋转50度 ... local: servo2.write(140), servo3.write(40)...

Wait, let me compare carefully. Actually local front():
```
servo2.write(140);
servo3.write(40);
...
servo1.write(40);
servo4.write(140);
```
Original front():
```
servo3.write(40); //左前
servo2.write(140);//右后
...
servo1.write(40);
servo4.write(140);
```
So same numbers, order swapped. Hmm interesting. Actually the original's front uses servo2 and servo3, then servo1/servo4.

Hold on. These are very similar but the local version has different delays etc. Let me diff more carefully.

Also toprighthand: original `servo1.write(0); delay(100); servo1.write(90);` — no 180/150. Local: servo1.write(180); delay(100); servo1.write(150); — different.

And toplefthand: original servo3.write(0); delay(100); servo3.write(90). Local: servo3.write(0); delay(100); servo3.write(30); delay(100).

So the local "Robot dog 1.1" is a modified copy. Now the question is: what's the ORIGINAL project. The user wants original. The GitHub repo `pluckypioneer/eda_robotR1` is itself probably a copy from JLC (嘉立创) platform. Let's search oshwhub for the original.

Let me search oshwhub. The osh1.html was 434KB. Let me check if it has data embedded. Also there's an oshwhub API. Let me look at what API endpoints work.

Also, let's check the local project for hints — e.g., image.cpp contains a JLC/嘉立创 logo. And the README in the GitHub repo mentions 嘉立创. The 立创开源硬件平台 (oshwhub.com) is JLC's open hardware platform. Let me search there.

Let me also try searching Chinese search engines that work: Sogou redirected (302). Let's follow redirects with -L and a cookie jar. Also try 360 search (so.com), Baidu with -L.

Let me do a batch.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\necho \"=== sogou -L ===\"; curl -sL -m 30 -A \"$ua\" -c cj.txt -b cj.txt \"https://www.sogou.com/web?query=EDA-Robot%20%E6%9C%BA%E5%99%A8%E7%8B%97\" -o sg_eda.html -w \"%{http_code} %{size_download}\\n\" …[截断,原长411]` → `=== sogou -L === 200 5608 === so.com 360 === 200 353611 === baidu -L === 200 1488 === oshwhub api v2 === 404 0`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S; grep -oE 'https?://[^\"'\"'\"' <>]*' osh1.html | grep -viE 'jlc|lceda|easyeda|w3.org|schema.org|miit|beian' | sort -u | head -30; echo \"=== osh1 embedded json keys ===\"; grep -oE '\"(title|name|uuid|projectName)\":\"[^\"]{0,60}\"' osh1.html | head -20", "description": "Inspect oshwhub search HTML"}` → `https://hm.baidu.com/hm.js?ce257455315c373d95fb598829d3cd09\\\ https://lckfb.com/\ https://mro.szlcsc.com/\ https://oshwhub.com/ https://oshwhub.com/\ https://oshwhub.com/activities https://oshwhub.com/activities/expert https://oshwhub.com/activities/spark2026 https://oshwhub.com/activities/spark2026/share https://oshw …[截断,原长1425]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:07）

Local copy confirmed as a derivative. Now let me hunt the true oshwhub original with more searches.

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== SOGOU eda (5608 bytes - likely block/captcha) ===\"; head -c 1200 sg_eda.html\necho; echo \"=== BAIDU (1488) ===\"; head -c 900 bd1.html", "description": "Inspect Sogou and Baidu responses"}` → `=== SOGOU eda (5608 bytes - likely block/captcha) === <!DOCTYPE HTML> <html> <head> <meta charset="utf-8"> <link rel="shortcut icon" href="//www.sogou.com/images/logo/new/favicon.ico?v=4" type="image/x-icon"> <title>搜狗搜索</title> <script> (function () { if (!window.Promise) { document.writeln('<script src="https://cdnjs …[截断,原长1817]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');const s=fs.readFileSync('so1.html','utf8');\nconst re=/<h3[^>]*>([\\s\\S]{0,300}?)<\\/h3>/g; let m,i=0;\nwhile((m=re.exec(s))&&i<25){console.log(i++, m[1].replace(/<[^>]*>/g,'').trim().slice(0,110));}\nconsole.log('--- links ---');\nconst re2=/<a[^>]+href=\\\"(https?:\\/\\/[^\\\"]+)\ …[截断,原长412]` → `0 其他人还搜了 1 相关搜索 · 反馈 --- links ---`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:08）

Let me parse the working search results (Sogou, 360, Baidu) and continue.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Sogou and Baidu blocked. 360 returned nothing useful (empty result page for exact phrase). Let me try:
- Bing with proper params (maybe the earlier parse failed because the format differs). Let me look at the actual bing_cn.html to see structure — earlier grep for `<h2><a href=` returned nothing. Let me try a plain node parse of bing.

Also try:
- GitHub code search API requires auth. Try grep.app, searchcode.com.
- Try oshwhub API with correct endpoint.
- Try Gitee search API.
- Try CSDN search.
- Try bilibili search API.

Let me batch these.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\necho \"=== grep.app ===\"; curl -s -m 25 -A \"$ua\" \"https://grep.app/api/search?q=eda_robot\" -o gap1.json -w \"%{http_code} %{size_download}\\n\"\necho \"=== searchcode ===\"; curl -s -m 25 -A \"$ua\" …[截断,原长413]` → `=== grep.app === 429 33948 === searchcode === 404 19 === gitee api === 200 2 === bilibili search === 200 5464 === csdn so === 200 38284`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');const s=fs.readFileSync('bing_cn.html','utf8');\nconsole.log('len',s.length);\nconst idx=s.indexOf('b_algo'); console.log('b_algo at',idx);\nconst re=/<h2[^>]*>([\\s\\S]{0,400}?)<\\/h2>/g; let m,i=0;\nwhile((m=re.exec(s))&&i<20){const t=m[1].replace(/<[^>]*>/g,'').trim();const h=(m[1 …[截断,原长412]` → `node:fs:439 return binding.readFileUtf8(path, stringToFlags(options.flag)); ^ Error: ENOENT: no such file or directory, open 'C:\Users\UserX\AppData\Local\Temp\s4s\bing_cn.html' at Object.readFileSync (node:fs:439:20) at [eval]:2:35 at runScriptInThisContext (node:internal/vm:219:10) at node:internal/process/execution: …[截断,原长700]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:08）

Sogou/Baidu are blocked. Let me try more searchable sources and code-search engines.

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== BILIBILI ===\"; node -e \"\nconst j=require('./bl1.json');\nif(j.code!==0){console.log('code',j.code,j.message);}\nconst r=(j.data&&j.data.result)||[];\nr.slice(0,15).forEach(v=>console.log(v.title.replace(/<[^>]*>/g,''),'|',v.author,'|https://www.bilibili.com/video/'+v.bvid));\n\"\necho \"=== CSDN ===\"; n …[截断,原长412]` → `=== BILIBILI === node:internal/modules/cjs/loader:1908 throw err; ^ SyntaxError: C:\Users\UserX\AppData\Local\Temp\s4s\bl1.json: Unexpected token '<', "<!DOCTYPE "... is not valid JSON at parse (<anonymous>) at Object..json (node:internal/modules/cjs/loader:1905:39) at Module.load (node:internal/modules/cjs/loader:1481 …[截断,原长2036]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:09）

Working APIs: Bilibili, CSDN. Let me parse those.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Very useful leads: "EDR-Robot 小智AI机器狗", "EDA-Robot-Pro", "【智能机器狗实训营】【基础营】做个狗吧：基于ESP8266与SG-90舵机的低成本DIY机器狗" — this last one is likely the 立创 training camp. Let me fetch these CSDN pages and search for the 智能机器狗实训营 which is a JLC/立创 educational activity.

Let me search for "智能机器狗实训营" and find the oshwhub original project.

Note that the CSDN article titles may be AI-generated/spam, so verify. Let me fetch the key page about 【智能机器狗实训营】【基础营】做个狗吧 and the 嘉立创机器狗复刻成功的经验之谈.

Also search oshwhub for "机器狗 实训营".

Let's do it.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\necho \"=== CSDN 做一个狗 (实训营) ===\"; curl -sL -m 30 -A \"$ua\" \"https://blog.csdn.net/接口与连接设计/article/details/159137629\" -o csdn_dog.html -w \"%{http_code} %{size_download}\\n\"\necho \"=== CSDN 嘉立创机器狗复刻  …[截断,原长412]` → `=== CSDN 做一个狗 (实训营) === 404 31553 === CSDN 嘉立创机器狗复刻 === 521 2258 === CSDN EDR-Robot 小智AI === 521 2140`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\necho \"=== CSDN search: 智能机器狗实训营 ===\"; curl -s -m 25 -A \"$ua\" \"https://so.csdn.net/api/v3/search?q=%E6%99%BA%E8%83%BD%E6%9C%BA%E5%99%A8%E7%8B%97%E5%AE%9E%E8%AE%AD%E8%90%A5&t=all&p=1\" -o cs2.json -w  …[截断,原长413]` → `=== CSDN search: 智能机器狗实训营 === 200 立创EDA智能机器狗实训营：基于安信可RD-03E毫米波雷达的人体跟随功能实现 || https://blog.csdn.net/weixin_35728286/article/details/159136776 【智能机器狗实训营】【基础营】做个狗吧：基于ESP8266与SG-90舵机的低成本DIY机器狗硬件改造与实现 || https://blog.csdn.net/接口与连接设计/article/details/159137629 中国软件杯飞桨小汪线下实训营-Go1Demo-大学生程序设计竞赛资源 || https://wenku.csdn.net/doc/ …[截断,原长2959]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:09）

Strong leads. Let me fetch the CSDN articles and search for the 立创 training camp original.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Very promising: "立创ESP8266机器狗项目复刻指南：基于Maxwell开源设计的手机遥控桌面机器人" and "立创EDA开源项目：基于ESP8266与SG90舵机的智能机器狗（4497595A）". Also "【智能机器狗实训营】【基础营】做个狗吧". Let me fetch these (CSDN often blocks with 521, let me try differently — maybe using Google cache or a different approach). Let me try fetching with different headers.

Also let me search oshwhub directly. The oshwhub search page is a JS SPA; there may be an API endpoint like https://oshwhub.com/api/eda/search/product or https://oshwhub.com/api/search/product. Let me investigate the oshwhub search page's JS for API paths.

Let me do parallel work:
1. Fetch CSDN articles with better headers/retries.
2. Find oshwhub API.

The "4497595A" looks like a 立创 project ID (like a serial number). Let me search oshwhub for that.

Actually, on oshwhub, project URLs look like https://oshwhub.com/<username>/<project-name>. There's also a search API. Let me look at the JS bundle to find endpoints.

Let me try known endpoint patterns:
- https://oshwhub.com/api/eda/product/search?...
- https://oshwhub.com/api/search/product/...

Let me just grab the oshwhub search page HTML and look for the JS chunk names, then fetch the chunk to find the API.

Alternatively use the "立创商城" open API. Hmm.

Let me also try searching for the oshwhub project via Bing with site: restriction — Bing was returning irrelevant results for "EDA-Robot" but maybe site:oshwhub.com 机器狗 ESP8266 will work better.

Let me run these in parallel.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36\"\nfor pair in \"maxwell|https://blog.csdn.net/微控制器（mcu）/article/details/159135208\" ; do :; done\n# use url-encoded paths\ncurl -sL -m 30 -A \"$ua\" -H \"Accept-Language: zh-CN,zh;q=0.9\" -H \"Accept:  …[截断,原长413]` → `maxwell 404 31553 4497595A 404 31553 dog 521 2575`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\necho \"=== bing site:oshwhub ===\"; curl -s -m 25 -A \"$ua\" \"https://cn.bing.com/search?q=site%3Aoshwhub.com+%E6%9C%BA%E5%99%A8%E7%8B%97+ESP8266\" -o b_osh.html -w \"%{http_code} %{size_download}\\n\"\ …[截断,原长412]` → `=== bing site:oshwhub === 200 100617 === bing EDA-Robot oshwhub === 200 100615 === bing 4497595A === 200 100827 === oshwhub js chunks === src="https://static.oshwhub.com/web/oshwhub/_next/static/chunks/fd9d1056-96f2ce78ff3bc886.js" src="https://static.oshwhub.com/web/oshwhub/_next/static/chunks/2117-e9bfc1fc0dfd3e24.js …[截断,原长1949]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:10）

Excellent leads. Let me fetch those CSDN articles and probe oshwhub's API.

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');\nfor(const f of ['b_osh.html','b_eda2.html','b_4497.html']){\n const s=fs.readFileSync(f,'utf8');\n console.log('=====',f);\n const seen=new Set();\n const re=/<h2[^>]*>([\\s\\S]{0,500}?)<\\/h2>/g;let m;\n while((m=re.exec(s))){\n const t=m[1].replace(/<[^>]*>/g,'').trim();\n const  …[截断,原长408]` → `===== b_osh.html 机器（由各种金属和非金属部件组装成的装置）_百度百科 || https://baike.baidu.com/item/%E6%9C%BA%E5%99%A8/2275865 机器（汉语词语）_百度百科 || https://baike.baidu.com/item/%E6%9C%BA%E5%99%A8/65322532 machine - 搜索 词典 || https://global.bing.com/dict/search?q=machine&amp;FORM=BDVSP6&amp;cc=cn 一文搞懂 “机器”：不是所有机械都叫机器！分类实例小白也能 ... || https://www.tou …[截断,原长2317]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\nfor u in \"https://oshwhub.com/api/search/product?keyword=%E6%9C%BA%E5%99%A8%E7%8B%97\" \"https://oshwhub.com/api/project/search?keyword=%E6%9C%BA%E5%99%A8%E7%8B%97\" \"https://oshwhub.com/api/v1/search/ …[截断,原长412]` → `404 0 https://oshwhub.com/api/search/product?keyword=%E6%9C%BA%E5%99%A8%E7%8B%97 200 40 https://oshwhub.com/api/project/search?keyword=%E6%9C%BA%E5%99%A8%E7%8B%97 404 0 https://oshwhub.com/api/v1/search/project?keyword=%E6%9C%BA%E5%99%A8%E7%8B%97 404 0 https://oshwhub.com/api/eda/search?keyword=%E6%9C%BA%E5%99%A8%E7%8B …[截断,原长336]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:10）

Let me parse the Bing results for oshwhub and try oshwhub's Next.js data endpoints.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The oshwhub search page is a Next.js app; results load via client-side. Let me check the /api/project/search response (200 with 40 bytes — probably an error message).

Let me try the Next.js server-side rendering: maybe there's an RSC payload. Also try oshwhub search with different paths. Actually, let me try using the browser use skill? That's an option — I have browser-use:control-browser available. That could render oshwhub search page and CSDN articles. That might be the most reliable path.

But first, let me check what /api/project/search returned.

Also let me reconsider: the GitHub repo pluckypioneer/eda_robotR1 is created 2025-07-25, quite recent, and says "项目基于嘉立创 EDA 开发平台,项目来源于嘉立创平台原作者". So pluckypioneer is also a re-uploader. The task says find the ORIGINAL project. There's clearly a lineage: some original on oshwhub (立创开源硬件平台) — possibly by an author who published ESP8266 桌面机器狗 with U8g2, 心知天气, servo pins 14,16,12,13.

Note the local copy has differences: AP password "12345678" vs original "11451419", dosleep vs dosleap, toprighthand servo1.write(180/150) vs original (0/90), lie() order differs, sitdown same. And local has extra engine.html (servo debug page) and different functions.

So the "original" pluckypioneer repo might itself be a copy of a yet-earlier original. The deliverable: find the ORIGINAL open-source project. Let me check the lineage more. Let me search oshwhub directly with browser automation, plus more searches.

Let me try using the control-browser skill to load oshwhub search. Actually first try simpler HTTP approaches: Next.js SSR might embed data in the HTML for search page. The osh1.html is 434KB — maybe results are included. Let me grep for "机器狗" in osh1.html.

Actually I grep'd for URLs but not for Chinese text. Let me grep for 机器狗.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== machine dog occurrences in osh1.html ===\"; grep -o \"机器狗\" osh1.html | wc -l\necho \"=== otest.out ===\"; cat otest.out\necho \"=== search for project links pattern ===\"; grep -oE '\"/[A-Za-z0-9_-]{2,40}/[A-Za-z0-9_-]{4,40}\"' osh1.html | sort -u | head -30", "description": "Look for results inside oshwhu …[截断,原长395]` → `=== machine dog occurrences in osh1.html === 0 === otest.out === === search for project links pattern ===`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\necho \"=== 360 search for EDA-Robot 机器狗 ===\"; curl -sL -m 25 -A \"$ua\" \"https://www.so.com/s?q=%22EDA-Robot%22+%E6%9C%BA%E5%99%A8%E7%8B%97+ESP8266\" -o so2.html -w \"%{http_code} %{size_download}\\n\" …[截断,原长412]` → `=== 360 search for EDA-Robot 机器狗 === 200 360393 === 360 search for 立创开源 机器狗 esp8266 舵机 === 200 367192 === 360 search 回收机器狗 === 200 362169`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:11）

Let me check the oshwhub search HTML payload more carefully and try browser automation.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

oshwhub search page is a client-side Next.js app that doesn't include results in HTML. Let me parse the 360 results.

Also, let me try browser automation via the browser-use skill to actually search oshwhub. But maybe first let's parse 360 results.

Also try oshwhub with different search URL format - maybe `https://oshwhub.com/search?keyword=...` or use the "explore" pages. Also there's an open API: `https://oshwhub.com/api/v1/project/search`? Let me look at the JS chunks for API paths.

Let me parse 360 first.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');\nfor(const f of ['so2.html','so3.html','so4.html']){\n const s=fs.readFileSync(f,'utf8');\n console.log('=====',f);\n const re=/<h3[^>]*>([\\s\\S]{0,600}?)<\\/h3>/g;let m;let i=0;\n while((m=re.exec(s))&&i<20){const t=m[1].replace(/<[^>]*>/g,'').replace(/\\s+/g,' ').trim();\n if(t.l …[截断,原长411]` → `===== so2.html 0 ESP8266四足机器人:Wi-Fi控制的桌面级仿生狗设计-CSDN博客 1 复刻嘉立创EDA-ESP8266机器狗 - 立创开源硬件平台 2 其他人还搜了 3 智能机器人怎么样 花30元,DIY了一只机器狗!全开源了!_什么值得买 4 《无线电》2025年第6期速览|蓝牙|射频|通信|单片机|元器件_网易订阅 5 智能机器小狗 - 立创开源硬件平台 6 终于搞定了!花30元,DIY了一只机器狗!|机器狗|电路|舵机_新浪科技_新浪网 7 阳阳的机器狗 - 立创开源硬件平台 8 相关搜索 · 反馈 9 猜您关注反馈 10 相关人物反馈 ===== so3.html 0 其他人还搜了 1 Arduin …[截断,原长748]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

 

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');const s=fs.readFileSync('so2.html','utf8');\n// find blocks around the titles and their target urls (360 uses redirect or data-url)\nconst re=/([\\s\\S]{0,1500}?)(复刻嘉立创EDA|智能机器小狗|阳阳的机器狗)([\\s\\S]{0,2000}?)/g;\nlet m;while((m=re.exec(s))){\n const blk=m[1]+m[2]+m[3];\n const us=blk.ma …[截断,原长410]` → `(Bash completed with no output)`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S; grep -oE 'https?://[a-z0-9.]*oshwhub\\.com[^\"'\"'\"'\\\\ <>]{0,60}' so2.html so3.html 2>/dev/null | sort -u | head -20; echo \"=== also look for encoded urls ===\"; grep -oE '(https?%3A%2F%2F|//)oshwhub[^\"'\"'\"'\\\\ <>]{0,80}' so2.html so3.html | head -20", "description": "Grep oshwhub URLs directly"}` → `=== also look for encoded urls === so2.html://oshwhub.com/ly1919/esp8266-desktop-pet so2.html://oshwhub.com/wwwsss1234/ji-qi-gou so2.html://oshwhub.com/14402a/yangyangs-robot-dog`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:11）

Very promising: "复刻嘉立创EDA-ESP8266机器狗" and "hello-hachi" on oshwhub. Let me get those URLs.

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\ncurl -sL -m 30 -A \"$ua\" \"https://oshwhub.com/ly1919/esp8266-desktop-pet\" -o ow_ly.html -w \"ly1919 %{http_code} %{size_download}\\n\"\ncurl -sL -m 30 -A \"$ua\" \"https://oshwhub.com/wwwsss1234/ji-qi …[截断,原长412]` → `ly1919 200 505274 wwwsss 200 489917 14402a 200 486193`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');const s=fs.readFileSync('so3.html','utf8');\nconst i=s.indexOf('hello-hachi');\nconsole.log(s.slice(Math.max(0,i-2000),i+1500).replace(/<[^>]*>/g,' ').replace(/\\s+/g,' ').slice(0,2000));\n\"", "description": "Extract hello-hachi context from 360 results"}` → `T%2BB2AC76hYlxOXllonc%2FELp5R4dVFnP04p8heGN6Ty3qzTKN2iVtyn23CMQTT066nnnmyZj3SAesQnLI4dPe4kGGNUFOzFwUvnSyapG00K2ZbjEu%2BGSr%2BwFGVkPSIra05f70n0HdQBsyGHoIgR9Xx5QdeYLrEpT5ITipoHHqLrxNGV4aAwNH6KOoVhB9KTKeFdr2IzlFbgOmCIczDkpv0Ti1G35pxXf6StaXcmg4QEYfcsoY1SrmFx9Z1rgvgSwhD%2BoXgHOU0JoQwHf%2Bk57X0ZxQPSfU9QvEEwIBQYusyBZhlJBsFPM% …[截断,原长942]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:12）

Excellent — three oshwhub candidates. Let me fetch them.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Let me now check the three oshwhub pages for content, particularly whether they contain code with servo numbers. Let me grep for "servo" / code in them. Also search for "hello-hachi" on oshwhub.

Let me update todos too.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nfor f in ow_ly.html ow_ws.html ow_yy.html; do echo \"===== $f\"; grep -oE '<title>[^<]*</title>' $f; echo \"servo count: $(grep -o 'servo' $f | wc -l)\"; echo \"ESP8266 count: $(grep -o 'ESP8266' $f | wc -l)\"; echo \"U8g2: $(grep -o 'U8g2\\|u8g2' $f | wc -l)\"; grep -oE '(description|og:description)\" content=\"[^\"] …[截断,原长412]` → `===== ow_ly.html <title>复刻嘉立创EDA-ESP8266机器狗 - 立创开源硬件平台</title> servo count: 0 ESP8266 count: 12 U8g2: 2 description" content="跟学立创EDA-Robot机器狗开源项目，完整复刻硬件、软件、3D结构；可实现多种运动控制、情绪表情、天气拓展等。 ===== ow_ws.html <title>智能机器小狗 - 立创开源硬件平台</title> servo count: 0 ESP8266 count: 14 U8g2: 0 description" content="本项目是基于ESP8266的智能机器狗，具有手 …[截断,原长552]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\necho \"=== 360: hello-hachi ===\"; curl -sL -m 25 -A \"$ua\" \"https://www.so.com/s?q=hello-hachi+%E7%AB%8B%E5%88%9B+%E6%9C%BA%E6%A2%B0%E7%8B%97\" -o so5.html -w \"%{http_code} %{size_download}\\n\"\ngre …[截断,原长412]` → `=== 360: hello-hachi === 200 358718 https://oshwhub.com/2303210217akai/desktop-mechanical-dog-10 https://oshwhub.com/jamal121/hello-hachi https://oshwhub.com/wwwsss1234/ji-qi-gou https://oshwhub.com/wy030002/intelligent-robot-dog === 360: EDA-Robot 立创 === 200 365680 https://oshwhub.com/course-examples/bot-dog https://o …[截断,原长400]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:12）

Let me inspect the fetched oshwhub pages and search for hello-hachi.

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\ncurl -sL -m 35 -A \"$ua\" \"https://oshwhub.com/course-examples/bot-dog\" -o ow_botdog.html -w \"bot-dog %{http_code} %{size_download}\\n\"\ncurl -sL -m 35 -A \"$ua\" \"https://oshwhub.com/course-example …[截断,原长411]` → `bot-dog 200 618020 eda-robotpro 200 660340 hello-hachi 200 493633 ji-qi-gou 200 489917`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:13）

Key find: `oshwhub.com/course-examples/bot-dog`. Let me fetch it and the other candidates.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

 

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');\nfor(const f of ['ow_botdog.html','ow_edapro.html','ow_hachi.html','ow_ws.html','ow_ly.html']){\n const s=fs.readFileSync(f,'utf8');\n const t=(s.match(/<title>([^<]*)<\\/title>/)||[])[1]||'';\n const d=(s.match(/name=\\\"description\\\" content=\\\"([^\\\"]*)\\\"/)||[])[1]||'';\n c …[截断,原长412]` → `===== ow_botdog.html | EDA-Robot机器狗 - 立创开源硬件平台 DESC: 此项目采用ESP8266主控，支持手机遥控，采用插件封装，非常适合新手焊接。 hit servo3.write 16 hit servo1 16 hit front() 4 hit SG90 2 hit SG-90 2 hit AsyncWeb 118 hit index.html 22 hit engine.html 6 hit dowhat 2 ===== ow_edapro.html | EDA-RobotPro AI智能机器狗 - 立创开源硬件平台 DESC: 本项目是EDA-Robot的升级版，搭载ESP32S3实现小 …[截断,原长800]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

bot-dog is the original: it has servo3.write, engine.html, dowhat, AsyncWeb. Let me extract the full page content from ow_botdog.html.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');const s=fs.readFileSync('ow_botdog.html','utf8');\n// Next.js puts data in self.__next_f pushes; extract readable text\nlet txt=s.replace(/<script[\\s\\S]*?<\\/script>/g,' ');\ntxt=txt.replace(/<style[\\s\\S]*?<\\/style>/g,' ');\ntxt=txt.replace(/<[^>]*>/g,' ').replace(/&nbsp;/g,' ') …[截断,原长412]` → ` EDA-Robot机器狗 - 立创开源硬件平台 首页 开源广场 扩展广场 活动 大学计划 发现 文章 创意 论坛 集市 开源达人 星火计划 初级赛道 高阶赛道 悬赏赛道 邀请有礼 发作品 登录 注册 嘉立创产业服务站群 电子产业 嘉立创PCB PCB、FPC制造服务 嘉立创SMT 一站式PCBA服务平台 嘉立创激光钢网治具 激光钢网&治具制造 嘉立创EDA 国产PCB设计工具 机械产业 嘉立创FA 机械/电气零部件一站式商城 嘉立创3D打印 树脂、尼龙、金属3D打印服务 嘉立创CNC机械智造 机加件一件起订，3天交货 更多服务 嘉立创CAM 国产线路板CAM软件 Forface 3D SaaS化3D技术服务平台 硬创社 好玩的硬件 …[截断,原长3999]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:13）

Found it — `oshwhub.com/course-examples/bot-dog`. Let me extract its full content.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

This is the original project on oshwhub: `https://oshwhub.com/course-examples/bot-dog` — "EDA-Robot机器狗", created 2024-11-29, GPL 3.0, ESP8266, AP mode, weather (心知?), 4 servos pins 14/16/12/13 with offsets. Let me read on to find the servo attach lines, gait code (front/back/left/right), and more.

Let me get the rest of the page text.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');const s=fs.readFileSync('ow_botdog.html','utf8');\nlet txt=s.replace(/<script[\\s\\S]*?<\\/script>/g,' ').replace(/<style[\\s\\S]*?<\\/style>/g,' ').replace(/<[^>]*>/g,' ').replace(/&nbsp;/g,' ').replace(/&amp;/g,'&').replace(/\\s+/g,' ');\nconsole.log(txt.slice(4000,16000));\n\"", " …[截断,原长412]` → `tion: none; line-height: 2; /* 通过调整line-height的值来调整文字的垂直位置 */ text-align: center; /* 文字居中 */ box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* 添加立体感 */ transition: all 0.3s ease; /* 添加过渡效果 */ } button:hover { background-color: skyblue; /* 鼠标悬停时的背景颜色 */ transform: translateY(2px); /* 点击效果 */ box-shadow: 2px 2px 8px rgba(0, …[截断,原长12000]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:14）

This is the original. Let me extract the full code section from the page.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

This is definitely the original project (course-examples/bot-dog, EDA-Robot机器狗). Let me get the rest, especially the gait code (front/back/left/right) which appears with offset PWM model rather than raw servo writes. Let me continue extracting.

Note: the original uses `engine1offsetleftpwm` etc. — a calibration-offset model. Let's see the rest of the text.

Actually, this is important: the local copy's front() uses servo2.write(140) etc. with no offsets. The course-examples original uses offset-based. Let me continue reading.

But also note: pluckypioneer/eda_robotR1 GitHub repo has the offset-free version with servo3.write(40) etc. Hmm, actually the GitHub one is offset-free, which matches the local "Robot dog 1.1" more closely in structure. So the lineage needs care.

Let me get the rest of the bot-dog page text.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');const s=fs.readFileSync('ow_botdog.html','utf8');\nlet txt=s.replace(/<script[\\s\\S]*?<\\/script>/g,' ').replace(/<style[\\s\\S]*?<\\/style>/g,' ').replace(/<[^>]*>/g,' ').replace(/&nbsp;/g,' ').replace(/&amp;/g,'&').replace(/&#x26;gt;/g,'>').replace(/&#x3C;/g,'<').replace(/\\s+/g,' …[截断,原长412]` → `LEN 27148 e(); String pass = request->getParam("pass", true)->value(); String uid = request->getParam("uid", true)->value(); String city = request->getParam("city", true)->value(); String api = request->getParam("api", true)->value(); // 打印接收到的参数 Serial.println(ssid); Serial.println(pass); // 保存WiFi信息到JSON文件 DynamicJso …[截断,原长11155]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:14）

Let me get the rest of the original page content.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

This is the ORIGINAL project: `https://oshwhub.com/course-examples/bot-dog` — "EDA-Robot机器狗" by 嘉立创 (JLC / course-examples account), with 代码仓 Gitee https://gitee.com/JasonYANG170/eda-robot.

Note important detail: The ORIGINAL uses 360-degree servos with `writeMicroseconds()` and offset compensation. It has `left90()` and `right90()` — i.e., the original is a 360° continuous-rotation servo version.

The local copy (Robot dog 1.1) uses `write(40)/write(140)` and 180° servos. The README of pluckypioneer/eda_robotR1 says "项目来源于嘉立创平台原作者".

Now let me get the Gitee repo: https://gitee.com/JasonYANG170/eda-robot

The task asks specifically:
1. Best-matching ORIGINAL project URL(s)
2. VERBATIM original bodies of front(), back(), left(), right(), sitdown(), lie(), toplefthand(), toprighthand(), dosleep() — all servoN.write() numbers and delay()s in order. And the original servo attach() lines with pulse widths.
3. Whether in original, left/right legs get SAME servo numbers or MIRRORED numbers (e.g., 40 vs 140) in front()/back().
4. Servo mounting orientation info and which value (<90 or >90) swings a leg forward.
5. If nothing found, say so.

So I need to determine which "original" version corresponds. The local copy has `attach(engine1, 500, 2500)` and `write(40)/write(140)`. The pluckypioneer/eda_robotR1 has `attach(engine1,500,2500)` too. But the oshwhub original uses writeMicroseconds and 360° servos.

Note there's also an attachment "EDA-Robot(180度舵机版)_V1.0.zip" and "EDA-Robot(180度舵机版)_V1.1.zip" — the LOCAL copy is "Robot dog 1.1" which matches "180度舵机版_V1.1"! That's the likely origin: the 180-degree servo version V1.1 of the original project.

Let me check the Gitee repo JasonYANG170/eda-robot which may have the 180-degree versions. Let me fetch it.

Also there may be branches/tags. Let me check.

Let me fetch the gitee repo tree.

Also I should check the oshwhub attachments for download links — but those require login.

Let's go to Gitee.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\ncurl -sL -m 35 -A \"$ua\" \"https://gitee.com/JasonYANG170/eda-robot\" -o gt_eda.html -w \"page %{http_code} %{size_download}\\n\"\ncurl -s -m 35 -A \"$ua\" \"https://gitee.com/api/v5/repos/JasonYANG170/ …[截断,原长412]` → `page 200 552 api 200 6726 branches 200 556 tags 200 259 root 200 4926`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:14）

Found the original: oshwhub `course-examples/bot-dog` with code repo `gitee.com/JasonYANG170/eda-robot`. Let me fetch the Gitee repo.

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');\nconst m=JSON.parse(fs.readFileSync('gt_meta.json','utf8'));\nconsole.log('NAME:',m.full_name,'|',m.human_name);\nconsole.log('DESC:',m.description);\nconsole.log('default_branch:',m.default_branch,'| created',m.created_at,'| pushed',m.pushed_at,'| stars',m.stargazers_count,'| forks …[截断,原长412]` → `NAME: JasonYANG170/eda-robot | JasonYANG17/EDA-Robot DESC: default_branch: main | created 2025-04-25T15:25:33+08:00 | pushed 2025-10-17T09:46:41+08:00 | stars 10 | forks 7 homepage: null | license: null --- branches --- [{"name":"main","commit":{"sha":"72b8c27ad6f0a774e3cac0ce63db226f9640ef0e","url":"https://gitee.com/ …[截断,原长1080]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\ncurl -s -m 35 -A \"$ua\" \"https://gitee.com/api/v5/repos/JasonYANG170/eda-robot/git/trees/72b8c27ad6f0a774e3cac0ce63db226f9640ef0e?recursive=1\" -o gt_tree.json -w \"tree %{http_code} %{size_download}\\ …[截断,原长412]` → `tree 200 4920 truncated false count 21 94 .gitignore 182 .idea/.gitignore 601 .idea/misc.xml 274 .vscode/extensions.json 82 README.md 6101 data/control.html 2564 data/index.html 3180 data/setting.html 1386 include/README 1035 lib/README 1788 platformio.ini 54909 src/image.cpp 35104 src/main.cpp 518 test/README`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:15）

The true original repo. Let me get the full file tree and the source files.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The Gitee repo is the current version (V1.3, with 180-degree servo support, offset calibration). But the user wants the original gait numbers matching `servoN.write(40)`, `servo2.write(140)` etc. Note the GitHub `pluckypioneer/eda_robotR1` had those exact `write()` numbers. Also there's "EDA-Robot(360度舵机版).zip" in the oshwhub attachments — that's the older 360-degree version.

Wait — actually let me reconsider. The Gitee main branch is the latest (180-degree version with offsets). The user's local copy has raw `servoN.write(40..140)` values which matches the older 360-degree version code / and matches pluckypioneer's eda_robotR1.

Hmm, but actually let me think about the lineage:
- `oshwhub.com/course-examples/bot-dog` = the official JLC course-example project (EDA-Robot机器狗), created 2024-11-29. Code repo = `gitee.com/JasonYANG170/eda-robot`.
- The 360-degree version (`EDA-Robot(360度舵机版).zip`) is the older release. The GAIT in the 360 version likely uses raw write() numbers... Actually no. Let me check: the JLC page describes the CURRENT code (with offsets and writeMicroseconds). The local copy uses `servo1.attach(engine1, 500, 2500)` and `servoN.write(40/140/90)` with `delay(100)`.

Hmm, wait. Let me reconsider: which is the ancestor of the user's local "Robot dog 1.1"? The user's copy has:
- `int engine1 = 14; engine2 = 16; engine3 = 12; engine4 = 13; int speed = 300;` — matches JLC page (same pins, same speed=300).
- `500, 2500` pulse widths.
- LittleFS (JLC uses SPIFFS).
- 心知天气 key `SB3j4zrxZ7nuRXv8v` — this is a real-looking key.
- data/: index.html, control.html, engine.html, setting.html
- Local control.html has engine.html link (电机校准页 = servo calibration page) and '回收机器狗' button.

The JLC original code has engine.html too (校准页), and offset calibration vars. So local copy is the 180-degree version adapted.

But the user asks for the ORIGINAL bodies of front(), back(), etc. — VERBATIM with all servoN.write() numbers and delays. The Gitee main branch is the original. Let me fetch src/main.cpp from Gitee and examine.

Let me get the file. Gitee API contents for a file gives base64.

Also I should fetch the oshwhub attachment "EDA-Robot(360度舵机版).zip" if downloadable — but attachments need login probably.

Let me fetch Gitee src/main.cpp.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\ncurl -s -m 40 -A \"$ua\" \"https://gitee.com/api/v5/repos/JasonYANG170/eda-robot/contents/src/main.cpp?ref=main\" -o gt_main.json -w \"main %{http_code} %{size_download}\\n\"\ncurl -s -m 40 -A \"$ua\" \" …[截断,原长413]` → `main 200 47368 pio 200 2961 readme 200 652 gitee_main.cpp OK 35104 gitee_pio.ini OK 1788 gitee_README.md OK 82`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:15）

The Gitee repo is the true original. Let me fetch its source and compare the gait functions.

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');\nlet s=fs.readFileSync('gitee_main.cpp','utf8');\nfor(const n of ['front','back','left','right','sitdown','lie','toplefthand','toprighthand','dosleep','dosleap','left90','right90']){\n const re=new RegExp('void\\\\\\\\s+'+n+'\\\\\\\\s*\\\\\\\\(\\\\\\\\s*\\\\\\\\)\\\\\\\\s*\\\\\\\\{[ …[截断,原长411]` → `24 gitee_gaits.txt 12`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S; grep -n \"attach(\\|servo[0-9]\\.writeMicroseconds\\|int engine\\|offset\\|ap_ssid\\|ap_password\\|softAP\" gitee_main.cpp | head -50", "description": "Check Gitee attach lines and engine defs"}` → `38:int engine1 = 14; // 舵机1引脚 39:int engine2 = 16; // 舵机2引脚 40:int engine3 = 12; // 舵机3引脚 41:int engine4 = 13; // 舵机4引脚 810: servo1.attach(engine1, 500, 2500); // 配置舵机PWM，500µs=0度，2500µs=180度 811: servo2.attach(engine2, 500, 2500); 812: servo3.attach(engine3, 500, 2500); 813: servo4.attach(engine4, 500, 2500); 821: WiF …[截断,原长381]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:16）

I have the authoritative original. Let me extract its gait functions and compare.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The regex failed. Let me use a different approach — find function definitions with a proper brace matcher.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');\nfunction extract(src,names){\n const out={};\n for(const n of names){\n const re=new RegExp('void\\\\\\\\s+'+n+'\\\\\\\\s*\\\\\\\\(\\\\\\\\s*\\\\\\\\)\\\\\\\\s*\\\\\\\\{','g');\n const m=re.exec(src);\n if(!m){out[n]=null;continue;}\n let i=re.lastIndex-1, depth=0;\n for(;i<src.len …[截断,原长396]` → `GITEE-ORIGINAL extracted 0 / 12 front,back,left,right,sitdown,lie,toplefthand,toprighthand,dosleep,dosleap,left90,right90 LOCAL-MODIFIED read err ENOENT: no such file or directory, open 'C:\c\Users\UserX\Downloads\Robot dog 1.1\src\main.cpp'`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The Gitee original extracted 0? That means the functions are named differently. Let me check the actual function names in gitee_main.cpp.

Also the local path needs Windows-style. Let me check.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S; grep -n \"^void \\|^int \\|^float \" gitee_main.cpp | head -40; echo \"=== case list ===\"; grep -n \"case [0-9]*:\" gitee_main.cpp | head -20", "description": "List functions in Gitee original"}` → `31:float batteryVoltage = 0; // 计算电池电压 32:int batteryPercentage = 0;//电量百分比 38:int engine1 = 14; // 舵机1引脚 39:int engine2 = 16; // 舵机2引脚 40:int engine3 = 12; // 舵机3引脚 41:int engine4 = 13; // 舵机4引脚 60:int prevEmojiState = -1; // 用于跟踪之前的 emojiState 61:int actionstate = 0;//活动状态标签 62:int emojiState = 0; // 表情状态标签 66:void I …[截断,原长1048]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S; file gitee_main.cpp; head -c 600 gitee_main.cpp | od -c | head -20", "description": "Check file encoding of Gitee main.cpp"}` → `gitee_main.cpp: C source, Unicode text, UTF-8 text 0000000 / / - - - - - - - - - - - - - - 0000020 - - - - - - - - - - - - - - - - * 0000060 \n / / E D A - R o b o t ( 1 8 0 0000100 345 272 246 350 210 265 346 234 272 347 211 210 346 234 254 ) 0000120 \n / / C o d e V e r s i o n : V 0000140 1 . 1 \n / / - - - - - - -  …[截断,原长855]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:16）

Let me check the actual function names in the Gitee original.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The Gitee file is "EDA-Robot(180度舵机版)" CodeVersion: V1.1. Functions exist. My extractor failed because of the regex escaping in the shell. Let me write a script file instead.

Note: The Gitee repo is the 180-degree servo version (V1.1). The original oshwhub project has both 180-degree and 360-degree versions.

Important: the local modified copy uses `servoN.write(140)` etc (180-degree version style) with `attach(engine1, 500, 2500)`.

Let me extract the gaits properly with a script file.

</details>

- 🔧 **Write** `{"file_path": "C:\\Users\\UserX\\AppData\\Local\\Temp\\s4s\\extract.js", "content": "const fs = require('fs');\n\nfunction extract(src, names) {\n const out = {};\n for (const n of names) {\n const re = new RegExp('void\\\\s+' + n + '\\\\s*\\\\(\\\\s*\\\\)\\\\s*\\\\{');\n const m = re.exec(src);\n if (!m) { out[n] = null; continue; }\n let i = m.index + m[0].length - 1, depth = …[截断,原长398]` → `File created successfully at: C:\Users\UserX\AppData\Local\Temp\s4s\extract.js (file state is current in your context — no need to Read it back)`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:17）

The Gitee file is the 180-degree version V1.1. Let me extract the gaits with a proper script file.

- 🔧 **Bash** `{"command": "cd /c/Users/UserX/AppData/Local/Temp/s4s && node extract.js", "description": "Run gait extraction script"}` → `GITEE_ORIGINAL_180V11 found 9 / 12 | missing: dosleap,left90,right90 GH_eda_robotR1 found 9 / 12 | missing: dosleep,left90,right90 LOCAL_MODIFIED found 9 / 12 | missing: dosleap,left90,right90`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\AppData\\Local\\Temp\\s4s\\GITEE_ORIGINAL_180V11_gaits.txt"}` → `1 ===== GITEE_ORIGINAL_180V11 :: front ===== 2 void front() 3 { 4 servo2.write(140); //舵机2旋转至140度 5 servo3.write(40); //舵机旋转至40度 6 delay(100);//延时100s 7 servo1.write(40); //内容同上 8 servo4.write(140); 9 delay(100); 10 servo2.write(90); 11 servo3.write(90); 12 delay(100); 13 servo1.write(90); 14 servo4.write(90); 15 delay …[截断,原长3967]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Now I have the true ORIGINAL gaits (Gitee JasonYANG170/eda-robot, the 180-degree servo V1.1 version). And the local modified copy. Let me now diff them carefully.

Local copy from earlier read (lines 502-695):

front():
```
servo2.write(140);
servo3.write(40);
delay(100);
servo1.write(40);
servo4.write(140);
delay(100);
servo2.write(90);
servo3.write(90);
delay(100);
servo1.write(90);
servo4.write(90);
delay(100);
servo1.write(140);
servo4.write(40);
delay(100);
servo2.write(40);
servo3.write(140);
delay(100);
servo1.write(90);
servo4.write(90);
delay(100);
servo2.write(90);
servo3.write(90);
```

Gitee original front(): identical servo numbers! servo2=140, servo3=40, servo1=40, servo4=140 ... yes identical.

Wait — but the local one at line 504-505 writes servo2(140) and servo3(40) — the same as original. Hmm, so front() is identical.

back(): local:
```
servo3.write(140);
servo2.write(40);
delay(100);
servo4.write(40);
servo1.write(140);
delay(100);
servo3.write(90);
servo2.write(90);
delay(100);
servo4.write(90);
servo1.write(90);
delay(100);
servo4.write(140);
servo1.write(40);
delay(100);
servo3.write(40);
servo2.write(140);
delay(100);
servo4.write(90);
servo1.write(90);
delay(100);
servo3.write(90);
servo2.write(90);
```
Original back(): servo3 140, servo2 40, delay; servo4 40, servo1 140, delay; servo3 90, servo2 90... identical.

Hmm. So front/back are identical to the Gitee original V1.1. But the FIRST candidate (pluckypioneer/eda_robotR1 GitHub) had slightly different front/back ordering. Let me check the difference between orig_main.cpp (GH R1) front and Gitee front.

GH R1 front:
```
servo3.write(40); //左前向前旋转50度
servo2.write(140);//右后向前旋转50度
delay(100);
servo1.write(40);
servo4.write(140);
delay(100);
servo2.write(90);
servo3.write(90);
delay(100);
servo1.write(90);
servo4.write(90);
delay(100);
servo1.write(140);
servo4.write(40);
delay(100);
servo3.write(140);
servo2.write(40);
delay(100);
servo1.write(90);
servo4.write(90);
delay(100);
servo2.write(90);
servo3.write(90);
```
vs Gitee front: servo2(140), servo3(40) ordering swapped in first pair. Same values. Slight difference: GH writes servo2 first then servo3; Gitee writes servo2 then servo3 too... wait Gitee: `servo2.write(140); servo3.write(40);` Yes same. GH: `servo3.write(40); servo2.write(140);` — reversed order but same values. Both have a "left-front/right-rear" comment. Very close.

So the local modified copy matches the Gitee original V1.1 for front/back/left/right/sitdown/lie/toplefthand/toprighthand/dosleep. Let me do a precise diff to find where the local copy differs. Let me diff each function mechanically.

Also important: the task asks about the ORIGINAL "dosleep()" — the Gitee original has `dosleep()` with servo1(0), servo3(180), servo2(180), servo4(0) — matches local. And `dosleap()` in GH R1 = servo1(0), servo4(0), servo3(180), servo2(180) — the 360-degree-era version.

Now let me do the actual diff. Also check the left/right: the question #3 asks whether left-side and right-side legs receive the SAME servo numbers or MIRRORED (40 vs 140) in front()/back(). In the original front(): servo2=140 & servo3=40 (the two diagonal?), servo1=40 & servo4=140. So servo2/servo3 pair gets 140/40 and servo1/servo4 gets 40/140 — these are mirrored between the two pairs. Within a pair (servo1 & servo4), values are 40 and 140 — mirrored. Let's be careful: in front(), first block: servo2.write(140), servo3.write(40) → pair A (servo2, servo3) with different values. Then servo1.write(40), servo4.write(140) → pair B with the opposite assignment. Then later servo1.write(140), servo4.write(40) → swung the other way; servo2.write(40), servo3.write(140).

So in each step, the two servos within a group get complementary (40 vs 140), and the diagonal counterparts get the same values. Specifically in the original front() step1: servo2=140, servo3=40; step2: servo1=40, servo4=140. So the left legs (say servo1,servo3) vs right legs (servo2,servo4)... Hmm I need to be careful about which servo is which leg.

Let me check the local copy's engine.html and README to see servo-to-leg mapping. Let me look at the engine.html and control.html in the local project and also image/main for comments about which servo is which leg. Also the pluckypioneer README might have that info. And the oshwhub original page mentions "舵机左转补偿" per engine1..4 offsets.

Let me also check the local copy's differences — that's the primary goal: "compare servo gait numbers with a modified copy". The task is to find the ORIGINAL and quote its verbatim bodies. I have that. But I should also confirm whether the local copy differs and how (that's the purpose). Let me diff.

Also, I should double check: is the local copy "Robot dog 1.1" based on the 180-degree version V1.1 (which is what Gitee main branch holds, per the header comment "EDA-Robot(180度舵机版) CodeVersion: V1.1")? The local main.cpp uses `servo1.write(...)` with degrees 0-180 and 500-2500 attach — consistent with 180-degree version. And the folder is named "Robot dog 1.1" — matching V1.1! Great.

Let me diff precisely and also gather servo mounting info. Let me check the local files for servo-leg mapping hints.

</details>

- 🔧 **Write** `{"content": "const fs = require('fs');\nconst S = 'C:/Users/UserX/AppData/Local/Temp/s4s/';\n\nfunction extract(src, names) {\n const out = {};\n for (const n of names) {\n const re = new RegExp('void\\\\s+' + n + '\\\\s*\\\\(\\\\s*\\\\)\\\\s*\\\\{');\n const m = re.exec(src);\n if (!m) { out[n] = null; continue; }\n let i = m.index + m[0].length - 1, depth = 0;\n for (; i < sr …[截断,原长396]` → `File created successfully at: C:\Users\UserX\AppData\Local\Temp\s4s\diff.js (file state is current in your context — no need to Read it back)`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:18）

Now let me do a precise diff between the original and the local modified copy.

- 🔧 **Bash** `{"command": "cd /c/Users/UserX/AppData/Local/Temp/s4s && node diff.js", "description": "Diff original vs modified gait sequences"}` → `====================== front ORIGINAL (gitee) : s2.write(140) | s3.write(40) | delay(100) | s1.write(40) | s4.write(140) | delay(100) | s2.write(90) | s3.write(90) | delay(100) | s1.write(90) | s4.write(90) | delay(100) | s1.write(140) | s4.write(40) | delay(100) | s2.write(40) | s3.write(140) | delay(100) | s1.write(9 …[截断,原长6591]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The local modified copy is byte-for-byte identical (modulo comments/whitespace) with the Gitee original in all 8 gait functions. Wait — that means the local copy's gait numbers ARE the original. Interesting. Let me double check the diff — but note the local file has extra comments. Let me verify norm equality exactly to be sure. The report says "[== ORIGINAL: IDENTICAL]" based on norm() equality (comments and whitespace stripped). Let me verify how different the local copy is overall — is it a "modified copy" or just a copy?

Also I should check the mirror question: in the original front(), servo2.write(140) and servo3.write(40) — these are both front legs? Let's think: the original says in the OSHW page comments "//+30C 2/3" for the 360 version. In the 180 version, we need to determine which servos are left legs and which are right legs. The task asks: "State explicitly whether in the original, the left-side and right-side legs receive the SAME servo numbers or MIRRORED/complementary numbers (e.g. 40 vs 140) in front()/back()."

Looking at the original front():
- servo2.write(140); servo3.write(40); delay(100);
- servo1.write(40); servo4.write(140); delay(100);
- servo2.write(90); servo3.write(90); delay(100);
- servo1.write(90); servo4.write(90); delay(100);
- servo1.write(140); servo4.write(40); delay(100);
- servo2.write(40); servo3.write(140); delay(100);
- servo1.write(90); servo4.write(90); delay(100);
- servo2.write(90); servo3.write(90);

So pairs: (servo1, servo4) move together as one diagonal pair, and (servo2, servo3) as the other. servo1 and servo4 get SAME numbers (40,40 / 140,140)... wait: servo1.write(40) and servo4.write(140) — those are COMPLEMENTARY (40 and 140). Hmm, in the first half: servo1.write(40), servo4.write(140) — complementary. Second: servo1.write(140), servo4.write(40) — complementary again (swapped). And servo2/servo3: 140/40 then 40/140 — also complementary.

So in the original 180-degree version, servos on the same "pair" (1&4, and 2&3) receive COMPLEMENTARY values (e.g. 40 vs 140), NOT the same. That indicates mirrored mounting: servo1 and servo4 are mounted mirror-image, as are servo2 and servo3.

Hmm wait, but again: pairs move together. Let's think about which physical legs: The comment in the original 360 version page says "//-30C 1/4" and "//+30C 2/3", so servo1&4 form one diagonal pair, and servo2&3 form the other diagonal pair. So servo1 = one leg, servo4 = the diagonal opposite leg. In a quadruped trot, diagonal legs move together.

Now for "mirrored": For diagonal legs mounted at 180 degrees relative to each other, applying complementary values (40 and 140) makes them rotate in the same physical direction (both forward or both backward). So the answer: servo1/servo4 receive complementary numbers (40 and 140), same for servo2/servo3.

Hmm, but the question asks specifically about "left-side and right-side legs". Let me get more info: I need to determine which servos correspond to left vs right. Let me look at the original code more (the engine.html or control mapping, or 3D structure). Also I should check the local copy's engine.html (舵机调试界面) — this might reveal the servo-to-leg mapping ("左前", "右后" etc.).

In the oshwhub original page text, the 360-version front() comments said:
```
//+30C 2/3
//-30C 1/4
```
Hmm that's just pairs.

Let me check whether there's a mapping in the original v1.0 360 version: "int engine1 = 14;" etc. Actually the page said in the original code section: "engine1offsetleftpwm" etc.

Let me look for a place in code that names legs: maybe in image.cpp or the HTML or a README/wiki. The wiki link: "EDA-Robot_嘉立创EDA Wiki". Let's search for that — maybe there's a leg-naming diagram.

Also to answer question 4 about which value swings a leg forward: from the original's own comments (360 version, oshwhub page): "//+30C 2/3" uses `servo2.writeMicroseconds(1500 + speed + engine2offsetleftpwm)` and `servo3.writeMicroseconds(1500 - speed - engine3offsetleftpwm)`. The comment "+30C" refers to a phase of gait (30 degrees cycle). Hmm, that's about the gait cycle phases, not forward direction.

Actually the comments in the 360 version: "+30C", "-30C", "0C" refer to the gait phase offsets in the bionic simulation. Not direction.

For 180 version, in front(): the sequence is: legs 2/3 swing with (140, 40) then ... Actually the naming in the modified local copy control.html says nothing about legs. But engine.html of local copy might have descriptions like "左前腿" etc. Let me check both local data/engine.html and the priginal repo's engine.html (which doesn't exist in the Gitee tree! The Gitee tree has data/control.html, index.html, setting.html — no engine.html. The local copy ADDED engine.html (舵机调试界面). That is a modification.

Wait, actually the local has engine.html (6387 bytes) and main.cpp serves /engine.html with the servo calibration endpoints? Let me check the local main.cpp for /engine1offset... endpoints. The original Gitee main.cpp — does it have engine offsets? The oshwhub page for the 360-version shows offsets (engine1offsetleftpwm etc.), but the Gitee main.cpp (180 V1.1) — let me check.

Let me diff the local main.cpp vs the Gitee original in more depth: size 35104 (Gitee) vs local 36505. Let me check for the distinguishing features: local uses LittleFS, ESPAsyncWebServer-esphome, bblanchon ArduinoJson 7 — the Gitee version might use SPIFFS and different libs. And the local has an ADC/battery thing? The local has `voltageDividerRatio = 8.4` etc.

Actually, importantly, are the local gait functions REALLY identical? The diff said yes for all 8. Hmm! That's suspicious — the task assumed the local copy is "modified" and the gait numbers might differ. But maybe the modification is elsewhere (LittleFS migration, engine.html, web server). Let me verify by byte-comparison of the extracted function bodies to be sure my normalization isn't hiding differences. Let me do an exact character-level diff after stripping only whitespace.

Actually norm() strips comments and whitespace. If the numbers were different, seq() would show it. seq() showed identical sequences including all numbers and delays. That's strong evidence that the gait numbers are IDENTICAL between local and the Gitee 180 V1.1 original.

Hmm wait, but I should double check whether local's front() maybe has extra trailing content or the function got modified in subtle non-numeric ways. The exact equality on norm() says the code is identical modulo comments/whitespace. Good.

But hold on — I should double check that the local version isn't derived from a DIFFERENT version (e.g. the "V1.1" vs "V1.3" or the 360 version). The local has no engine offsets. The Gitee main.cpp is 180 V1.1. Identical gait sequences. Also local's `lie()` order: servo1.write(180); servo3.write(0); servo2.write(0); servo4.write(180) matches Gitee exactly and differs from GH R1's ordering. So local is derived from the Gitee original (or a common source).

Now let me also verify: is local maybe identical in ALL respects (i.e., not really modified)? Differences: local uses LittleFS + ESPAsyncWebServer-esphome + U8g2 2.36.12 + ArduinoJson 7.4.2 + NTPClient, Gitee platformio.ini — let me read it. Local also has engine.html added, AP password changed from 11451419 (README says password 11451419) to 12345678. And the local has building; weather API key default. Let me diff more systematically to characterize modifications — useful for the user's comparison task.

Let me check:
1. Gitee platformio.ini content.
2. Local vs Gitee main.cpp diff (rough).
3. Check for servo attach lines: both 500/2500. ✓ (local: servo1.attach(engine1, 500, 2500) — same)
4. Leg naming: search for 左/右/前/后 leg naming in originals.

Also the task asked about the "original" bodies of front(), etc. — I have them from the canonical Gitee original (eda-robot 180 version V1.1, matching the "EDA-Robot(180度舵机版)_V1.1.zip" attachment on oshwhub). Also, let me check if there's a 360-version main.cpp available (the "EDA-Robot(360度舵机版).zip" attachment) — hard to download from oshwhub attachments. Maybe gitee has a branch/tag "v1.0 资源迁移".

Also worth checking: maybe the official wiki (wiki.lceda.cn or similar) documents EDA-Robot with leg naming and servo mounting orientation. The page mentioned "在线文档：EDA-Robot_嘉立创EDA Wiki". Let me find that URL. That answers question 4 (which value swings a leg forward, mirrored mounting).

Let me look at the ow_botdog.html for the wiki link, and the Gitee README.

Also check the local engine.html (added by the modifier) since it may include calibration UI and maybe leg labels.

Let me do these in parallel:
- Read gitee_README.md and gitee_pio.ini
- grep for wiki link in ow_botdog.html
- read local data/engine.html
- check local main.cpp for differences vs gitee (e.g., LittleFS, http endpoints)

Then search for the wiki page and for leg orientation info.

Note: I've done many searches already (>8 distinct queries):
1. Bing: "EDA-Robot" 机器狗
2. Bing CN: "EDA-Robot"
3. Bing: EDA-Robot ESP8266 桌面机器狗 舵机
4. DDG (failed), Google (failed), Baidu (blocked), Sogou (blocked), searx (failed), mojeek (403), brave (fail), ecosia (301), marginalia (302), startpage (fail)
5. GitHub API: 机器狗 esp8266, EDA-Robot, quadruped esp8266 servo
6. 360: EDA-Robot 机器狗 ESP8266, 立创开源 机器狗 esp8266 舵机 U8g2, "回收机器狗", hello-hachi 立创 机械狗, 立创 EDA-Robot 机器狗 开源
7. CSDN API: EDA-Robot 机器狗, 智能机器狗实训营, 立创开源 机器狗 舵机 ESP8266
8. Gitee API search
9. oshwhub fetches

That's well over 6-10 distinct searches. Good.

Now let me nail down: leg/mirror info + wiki. Let me also check the "复刻嘉立创EDA-ESP8266机器狗" (ly1919) page text for statements about left/right servo mirroring, and the "智能机器小狗" (wwwsss1234) which appears to be the same original course project (it also uses engine offsets; likely the 360 version). Actually wwwsss1234/ji-qi-gou might be the same author's project or a student copy.

Wait — actually, is the oshwhub "course-examples/bot-dog" the ORIGINAL, or is it a "课程示例" (course example) that is itself derived from something else? It says "本项目提供了完整的说明及源码" and links to its own Gitee repo. It's under the account "course-examples" which is likely the 嘉立创EDA official 课程/实训 account. The creation date is 2024-11-29. And it's part of 立创EDA 实训活动 (实训营). The Gitee repo created 2025-04-25 (later, maybe migrated). Let me check the wiki page for the whole official course, and check if there's an even earlier version. Let me also check the video: "EDA-Robot演示视频.mp4" attachment. And Bilibili may have 嘉立创EDA official video.

Let me also verify the claim that the local copy is derived from this project: local 's ap_ssid = "EDA-Robot" matches original's hotspot name "EDA-Robot" (page says: 连接名称为EDA-Robot的WIFI热点). Local AP password 12345678 vs README 11451419 — the Gitee README says? Let me read gitee_README.md (82 bytes).

Let me gather these.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\AppData\\Local\\Temp\\s4s\\gitee_README.md"}` → `1 # EDA-Robot 2 本仓库存储为180舵机代码，360舵机版程序已不再维护`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\AppData\\Local\\Temp\\s4s\\gitee_pio.ini"}` → `1 ; PlatformIO Project Configuration File 2 ; 3 ; Build options: build flags, source filter 4 ; Upload options: custom upload port, speed and extra flags 5 ; Library options: dependencies, extra library storages 6 ; Advanced options: extra scripting 7 ; 8 ; Please visit documentation for the other options and examples  …[截断,原长1865]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:18）

Local gaits are byte-identical to the Gitee original. Let me gather supporting details (leg mapping, wiki, modifications).

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The Gitee repo is the "180 servo code" version. The original oshwhub page mentions 360-degree version was the initial one (V1.0), and 180-degree version came later (v1.2 program change: "程序新增支持180度舵机版本，可无需校准").

Wait — important nuance. The local modified copy says "CodeVersion: V1.1" style. Let me check the local main.cpp header comment and gitee main.cpp header for version info. Also check whether the local file matches the Gitee v1.1 180-degree version exactly.

Also, the task asks about servo mounting orientation and which value swings a leg forward. Let me look at the wiki doc for leg mapping: "servo1" = 右前? Let's check the oshwhub page text for mapping. It says commands like "左前" comments in the derivative GH repo (servo3 = 左前). Let's search the wiki (EDA-Robot_嘉立创EDA Wiki) for leg assignment and orientation info.

Also let's check the local main.cpp header comment vs Gitee. And check whether local == gitee for the whole file (diff the servo sections / do a diff of the two files normalized).

Let me do a full-file normalized diff to quantify how much the local copy deviates.

Also, the task's items:
1. Best-matching original project URL(s). -> oshwhub course-examples/bot-dog (EDA-Robot机器狗), gitee.com/JasonYANG170/eda-robot, plus wiki doc link.
2. Quote verbatim original bodies of front(), back(), left(), right(), sitdown(), lie(), toplefthand(), toprighthand(), dosleep() — DONE from Gitee.
3. Whether left/right legs get SAME or MIRRORED numbers in front()/back() -> In original front(): servo2=140, servo3=40 (same "pair"; note servo2 and servo3 are a diagonal pair? Actually servo2+servo3 are one pair, servo1+servo4 another). Let me determine the leg mapping.

From the oshwhub page: engine1 = 14 (舵机1), engine2 = 16, engine3 = 12, engine4 = 13. In front(): servo2 & servo3 move as a pair (140/40), servo1 & servo4 as a pair (40/140). Then reversed. So within a pair, values are complementary (40 vs 140). 

From GH derivative comment: "servo3.write(40); //左前向前旋转50度" and "servo2.write(140);//右后向前旋转50度" — so servo3 = 左前 (front-left), servo2 = 右后 (rear-right), forming a diagonal pair. And servo1/servo4 = the other diagonal: servo1 = 右前, servo4 = 左后 presumably.

Let me verify by looking at the wiki. Let me try fetching the wiki doc: "EDA-Robot_嘉立创EDA Wiki". Also check the oshwhub page HTML for leg mapping info, and the local engine.html which may label servos.

Let me check local engine.html for servo labels, and the setting/index pages.

Also, item 4: servo mounting orientation (mirrored vs identical) and which value (<90 or >90) swings a leg forward.

From front(): first half uses servo2=140, servo3=40 and servo1=40, servo4=140 (i.e., 2&4 above 90, 1&3 below 90); second half reversed. Since it's a diagonal-pair walking gait with complementary numbers, this indicates mirrored mounting between the two diagonals. Need evidence. Let me look at the wiki page and the 3D/assembly description.

Let me also do the full normalized diff of local vs gitee to quantify modifications, and get the local file's header comment (version).

Then optionally check the wiki URL. Let me find the wiki link from the oshwhub HTML.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== wiki/doc links in oshwhub page ===\"; grep -oE 'https?://[^\"'\"'\"' <>\\\\)]*' ow_botdog.html | grep -viE 'oshwhub|jlc|static|hm.baidu|w3.org|schema' | sort -u | head -20\necho \"=== local main.cpp header ===\"; head -12 \"/c/Users/UserX/Downloads/Robot dog 1.1/src/main.cpp\"\necho \"=== gitee main.cpp hea …[截断,原长411]` → `=== wiki/doc links in oshwhub page === https://beian.miit.gov.cn https://beian.mps.gov.cn/#/query/webSearch?code=44030002004384 https://docs.lceda.cn https://docs.lceda.cn/cn/FAQ/Business/index.html https://docs.lceda.cn/cn/FAQ/Contact-Us/index.html https://gitee.com/JasonYANG170/eda-robot https://gitee.com/JasonYANG17 …[截断,原长1426]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\ncp \"/c/Users/UserX/Downloads/Robot dog 1.1/src/main.cpp\" local_main.cpp\necho \"=== normalized unified diff: ORIGINAL(gitee) vs LOCAL ===\"\nnode -e \"\nconst fs=require('fs');\nconst norm=s=>s.replace(/\\/\\*[\\s\\S]*?\\*\\//g,'').replace(/\\/\\/[^\\n]*/g,'').replace(/[ \\t]+/g,' ').replace(/\\r/g,'').replace(/\\n{ …[截断,原长412]` → `=== normalized unified diff: ORIGINAL(gitee) vs LOCAL === sizes 20364 21565 diff lines: 844 250 229`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:19）

Local gaits are byte-identical to the Gitee original. Let me get the remaining details: leg mapping, wiki doc, and quantify the local modifications.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The gait functions are identical; the diff is mostly FS->LittleFS, SPIFFS->LittleFS, and added features. Let me confirm the leg mapping from the original docs (wiki) and check whether servo1..4 map to specific legs. Let me look at the original code comments and the wiki/PDF.

Let me also check the local modifications summary (LittleFS vs SPIFFS, engine calibration removed, etc.). And check the front() semantics for which servo is which leg.

Let me look at the oshwhub page text for leg mapping info and the wiki PDF.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== original code comments about servo/leg names ===\"\ngrep -n \"舵机1\\|舵机2\\|舵机3\\|舵机4\\|左前\\|右前\\|左后\\|右后\\|前左\\|前右\\|后左\\|后右\\|engine1\\|engine2\\|engine3\\|engine4\" gitee_main.cpp | head -30\necho; echo \"=== original setup attach block ===\"\nsed -n '800,830p' gitee_main.cpp", "description": "Find leg-ser …[截断,原长412]` → `=== original code comments about servo/leg names === 34:Servo servo1;//声明舵机1 35:Servo servo2;//声明舵机2 36:Servo servo3;//声明舵机3 37:Servo servo4;//声明舵机4 38:int engine1 = 14; // 舵机1引脚 39:int engine2 = 16; // 舵机2引脚 40:int engine3 = 12; // 舵机3引脚 41:int engine4 = 13; // 舵机4引脚 487: servo2.write(140); //舵机2旋转至140度 810: servo1.at …[截断,原长1434]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== local: FS vs LittleFS, offset/calibration presence ===\"\ngrep -c \"SPIFFS\" local_main.cpp; grep -c \"LittleFS\" local_main.cpp\necho \"--- offset vars in local ---\"; grep -c \"offset\" local_main.cpp\necho \"--- offset vars in original ---\"; grep -c \"offset\" gitee_main.cpp\necho \"=== local endpoints  …[截断,原长412]` → `=== local: FS vs LittleFS, offset/calibration presence === 1 18 --- offset vars in local --- 0 --- offset vars in original --- 0 === local endpoints added (top of handleWiFiConfig) === 32 28 === local only-ish new strings === 12345678 local=1 orig=0 11451419 local=0 orig=0 heart local=0 orig=0 weather local=18 orig=15  …[截断,原长410]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:19）

Local gaits are byte-identical to the original. Let me confirm the leg/servo mapping from the original docs and summarize the local deltas.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Let me check the local vs original servo->leg mapping question. The key question is whether in the original, left-side and right-side legs receive SAME or MIRRORED numbers.

From the original front():
```
servo2.write(140); //舵机2旋转至140度
servo3.write(40);  //舵机旋转至40度
delay(100);
servo1.write(40);
servo4.write(140);
...
servo1.write(140);
servo4.write(40);
...
servo2.write(40);
servo3.write(140);
```

So: servo2=140 & servo3=40 (first), then servo1=40 & servo4=140. Then later servo1=140/servo4=40 and servo2=40/servo3=140.

So each pair (servo2,servo3) and (servo1,servo4) alternates between (140,40) and (40,140). This is the mirroring: for servo2/servo3 pair, they always get complementary values (140 vs 40); same for servo1/servo4.

Now which servo is which leg? The 360-degree version page showed engine1..4 = pins 14,16,12,13. The page said "engine1offsetleftpwm = -93; // 舵机左转补偿" etc. Let me look for a leg mapping in the wiki doc. Let's try to fetch the online wiki doc.

Let me find the "EDA-Robot_嘉立创EDA Wiki" link. The page had a PDF link: https://image.lceda.cn/easyedaResource/images/90df0661fc474cfd82e2d9b4c6448a27.pdf — that's probably the offline doc.

Also, need to check the OSHWHUB page for the "在线文档" link. Let me grep for lceda.cn wiki link in the raw HTML.

Also let me check the servo->leg mapping from the engine.html local file, and the oshwhub page's calibration section which described "电机左转90度" etc.

Also, image.cpp might reveal which servo is which leg? Let me check the local engine.html for labels.

Let me also check whether the local project has any hints about leg mapping: e.g., "left90"/"right90" functions.

Let me also do a couple more searches to satisfy the 6-10 search requirement and note them. I've done: Bing (x3), Sogou (x2), Baidu, 360 (x6), DDG, Google, GitHub API (x3), Gitee API, CSDN (x4), Bilibili, grep.app, searchcode, mojeek, brave, ecosia, marginalia, startpage, searx, oshwhub (x4). That's well over 10.

Let me now:
1. Get the wiki doc link and check the leg mapping.
2. Check engine.html in local for leg labels.
3. Verify the "EDA-Robot 360度舵机版" (V1.0) code which had writeMicroseconds. The oshwhub attachments include "EDA-Robot(360度舵机版).zip" — the page content body displayed the 360-degree code. The 180-degree repo is the maintained one and matches local byte-for-byte.

Wait — important: the local project's main.cpp has `LittleFS` and `#include <image.cpp>` and gaits identical to the Gitee 180 V1.1. But the local main.cpp also has ESP8266HTTPClient, weather, etc. Both have weather. The local uses LittleFS instead of SPIFFS. The local also has a different AP password ("12345678" vs original's "EDA-Robot"/"11451419"?). Let me check the original ssid/password.

Let me grep `ssid` and `password` in gitee_main.cpp.

Also local has BUILD on platformio with esphome/ESPAsyncWebServer-esphome @ ^3.2.2 while original uses ottowinter @ 3.3.0. Minor.

So the local copy = the Gitee original 180-version V1.1 with modifications (LittleFS migration, AP password, added serial commands, etc.). Let me verify: does the local have serialListen with the same emoji commands? The Gitee original has serialListen at line 712. Let me diff that too. Actually the normalized diff will show.

Let me look at the norm_diff.txt to characterize the modifications.

Let me check a few specific things in the diff.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== ORIGINAL ssid/password/api ===\"; grep -n 'ssid\\s*=\\|password\\s*=\\|const char \\*ssid\\|const char \\*password\\|useruid\\|weatherapi\\|seniverse\\|cityname' gitee_main.cpp | head -20\necho; echo \"=== ORIGINAL api key if any ===\"; grep -n \"key=\\|SB3j\\|api.seniverse\" gitee_main.cpp | head", "descri …[截断,原长412]` → `=== ORIGINAL ssid/password/api === 45:const char *ssid = "EDA-Robot";//WIFI名称 46:const char *password = ""; // 无密码 51:const char *weatherAPI = "http://api.seniverse.com/v3/weather/daily.json?key=";//心知天气API地址 55:String cityname = "";//城市名称 56:String weatherapi = "";//心知天气API密钥 64:const char *ssidFile = "/ssid.json";//配 …[截断,原长787]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== wiki link search in raw oshwhub html ===\"\ngrep -oE 'https?://[^\"'\"'\"'<>\\\\)]*wiki[^\"'\"'\"'<>\\\\)]*' ow_botdog.html | sort -u | head -10\ngrep -oE 'https?://[^\"'\"'\"'<>\\\\)]*docs\\.lceda[^\"'\"'\"'<>\\\\)]*' ow_botdog.html | sort -u | head -10\necho \"=== local engine.html servo labels ===\"\ngre …[截断,原长412]` → `=== wiki link search in raw oshwhub html === https://openmoji.org/\n\u003c/details\u003e\n\u003cdetails\u003e\n\u003csummary\u003e是否需要网络\u003c/summary\u003e\n仅时钟及天气功能依赖网络，其余功能均可在无网络情况下使用。\n\u003c/details\u003e\n\u003cdetails\u003e\n\u003csummary\u003e如何遥控\u003c/summary\u003e\n开机后连接名称为EDA-Robot的WIFI热点，浏览器输入192.168.4.1即可 …[截断,原长1857]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:19）

Let me check the original's AP credentials, the wiki doc link, and characterize the local modifications.

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\nfor p in eda-robot-introduce eda-robot-hardware eda-robot-3d eda-robot-download; do\n curl -sL -m 30 -A \"$ua\" \"https://wiki.lceda.cn/zh-hans/course-projects/smart-internet/eda-robot/$p.html\" -o wiki_ …[截断,原长412]` → `eda-robot-introduce 200 136243 eda-robot-hardware 200 233039 eda-robot-3d 200 130934 eda-robot-download 200 135462`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:20）

Let me check the official wiki documentation for servo mounting/orientation details.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

 

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');\nfor(const f of ['wiki_eda-robot-hardware.html','wiki_eda-robot-3d.html']){\n let s=fs.readFileSync(f,'utf8');\n s=s.replace(/<script[\\s\\S]*?<\\/script>/g,' ').replace(/<style[\\s\\S]*?<\\/style>/g,' ').replace(/<[^>]*>/g,' ').replace(/&nbsp;/g,' ').replace(/&amp;/g,'&').replace(/ …[截断,原长412]` → `########## wiki_eda-robot-hardware.html ... 0拓展坞 USB模块(3.0集线器) SL2.1A集线器 GL823K简易读卡器 页面导航 ​ 2.1 电路图原理分析 ​ 该项目在硬件设计中涉及的主要电路模块包括： (1) 主控电路：作为项目的核心控制单元，负责处理按键输入、驱动显示屏，并通过内置Wi-Fi模块实现网络连接，用于获取实时信息和远程更新数据。 (2) 舵机电路：作为项目的运动部分，负责控制舵机，确保电机正常驱动。 (3) 电源电路：为整个电路系统提供稳定的电源输出，确保所有模块在合适的电压下稳定运行。 该项目的硬件部分设计较为简单，主要通过软硬件结合实现信息显示与运动交互控制。  …[截断,原长9191]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The wiki hardware page didn't clearly explain servo orientation. Let me search the introduce wiki page and 3d page more specifically for leg mapping and servo orientation. Also, let me look at the local engine.html which might document servo mounting.

Let me check the local data/engine.html and control.html for leg labels, and search the wiki for "舵机" + "左" + "右" mapping in the introduce page.

Actually, an important question: which servo is which leg? The original code has servo1..servo4. The front() function writes servo2/servo3 together and servo1/servo4 together. In the local code (identical), no leg names given. But the GH fork eda_robotR1 (which is based on the 360 version?) has comments "//左前向前旋转50度" for servo3.

Let me check the local engine.html and image.cpp for any mapping. Also check if there is a README in the local project mentioning leg mapping.

Let me also check the original 360-degree version program, which may be available in the oshwhub attachments (软件源码.zip). That's the version with offset calibration (engine1offsetleftpwm = -93 etc.), which is the 360 version. But the local code is 180-degree version (uses servo.write(140) etc.), matching Gitee V1.1.

Let me verify: local uses `servo.write()` with values 0-180, and `speed = 300` variable, and no offset variables. Wait, local has `int speed = 300;` at line 39! Let me check. Earlier grep showed local main.cpp line 39-ish: `int speed = 300;`. Hmm, in the local file I read at the top: 

```
int engine1 = 14;
int engine2 = 16;
int engine3 = 12;
int engine4 = 13;
int speed = 300;
```

That matches the original 180 version too? Let me check the Gitee original for speed. Earlier grep of gitee_main.cpp showed engine1..engine4 at lines 38-41. Let me check if it has `int speed`.

Let me check the engine.html in local data — it might be an added file (the Gitee original has only control.html, index.html, setting.html — no engine.html!). Indeed the Gitee tree shows data/: control.html, index.html, setting.html. The local has engine.html additionally. That's a local modification (servo debug console).

Wait — but the oshwhub page mentions "engine.html" route and "/engine.html" server route, and mentions "电机校准页" (motor calibration page). The 360 version had engine.html. The Gitee 180 version V1.1 has no engine.html. Hmm, but actually the local project has engine.html, and local main.cpp has route /engine.html. Let me check if gitee main.cpp has /engine.html route. Let me check.

Also the oshwhub attachments include "EDA-Robot(360度舵机版).zip" which has the engine.html calibration page. The local project seems to be based on the 180-degree version but with engine.html added? Let me verify.

Let me grep gitee_main.cpp for "engine.html" and "SPIFFS" and "LittleFS".

Also, I should confirm the left/right mirroring question: In the original front(): servo2.write(140), servo3.write(40) — so servo2 and servo3 are complementary (140 vs 40). And servo1.write(40), servo4.write(140). So servo1/servo3 get 40 and servo2/servo4 get 140 at the same phase; then later servo1.write(140), servo4.write(40), servo3.write(140), servo2.write(40). So indeed left/right legs get mirrored/complementary numbers.

Which are left vs right? In the local control.html, buttons for toplefthand / toprighthand. In the original toplefthand() writes servo3, toprighthand() writes servo1. So servo3 = left, servo1 = right. The GH fork's front() has comments: servo3.write(40); //左前向前旋转50度 and servo2.write(140);//右后向前旋转50度. So servo3 = 左前 (left front), servo2 = 右后 (right rear), servo1 = 右前? Let's think: In toprighthand() it's servo1. So servo1 = right side. And in front(), servo1 and servo4 move together (phase shifted), servo2 and servo3 together... Hmm.

Actually from the GH fork comments: servo3 (left front) and servo2 (right rear) are in the first pair; servo1 and servo4 in the second pair. So the pairing is diagonal: servo3+servo2 diagonal, servo1+servo4 diagonal. So servo1 = 右前 (right front)? and servo4 = 左后 (left rear)? Given toprighthand = servo1 => right front. toplefthand = servo3 => left front. So servo2 = right rear, servo4 = left rear. Hmm wait but that gives pairing: servo3 (LF) + servo2 (RR) = diagonal ✓; servo1 (RF) + servo4 (LR) = diagonal ✓. Yes! That's consistent.

But the GH fork comment says "servo2.write(140);//右后向前旋转50度" — "right rear swings forward". Good.

Hmm, but actually the pin order: engine1=14, engine2=16, engine3=12, engine4=13. Typically these map to actual physical legs. I should be careful about claiming the mapping; the GH fork comments are the evidence. Let me verify by fetching the GH fork's full front() with comments and check control.html labels in the original oshwhub page: "抬左手 抬右手" - toplefthand/toprighthand.

Let me also check whether the wiki introduce page mentions which servo is which leg. Let me grep for "左前" in wiki_introduce.

Also I need to answer question 4: servo mounting orientation (mirrored left/right vs identical) and which value (<90 or >90) swings a leg forward. Evidence:
- front() : servo2.write(140) & servo3.write(40) simultaneously; servo1.write(40) & servo4.write(140) simultaneously. And back() is the reverse: servo3.write(140), servo2.write(40) first, then servo1.write(140), servo4.write(40).
- In front(): for servo2 the value is 140, for servo3 it's 40. Since servo2 = right rear and servo3 = left front (diagonal pair), reversed values.

Hmm, but what swings forward? In front(), the first motion is servo2 (RR) to 140 and servo3 (LF) to 40 — i.e., the "lift/swing" phase. Then servo2/servo3 return to 90. Hmm, actually looking at front() more carefully:

front():
1. s2=140, s3=40, delay 100
2. s1=40, s4=140, delay 100
3. s2=90, s3=90, delay 100
4. s1=90, s4=90, delay 100
5. s1=140, s4=40, delay 100
6. s2=40, s3=140, delay 100
7. s1=90, s4=90, delay 100
8. s2=90, s3=90

This is a diagonal trot: phase A (s2,s3) go to one extreme, phase B (s1,s4) go to the same-side extreme, then both return; then phase B goes to the other extreme, phase A goes to the other extreme, then return. 

Comments in the 360-version oshwhub page (front() with microseconds) show labels: "//+30C 2/3", "//-30C 1/4", "// 0C 2/3", "// 0C 1/4", "//+30C 1/4", "//-30C 2/3", "// 0C 1/4", "// 0C 2/3". So for 2/3 (servo2/servo3): +30 offset then 0 then -30 then 0; for 1/4: -30 then 0 then +30 (hmm the sequence is -30, 0, +30, 0? Let's re-read:

```
//+30C 2/3 servo2.writeMicroseconds(1500 + speed + engine2offsetleftpwm); servo3.writeMicroseconds(1500 - speed - engine3offsetleftpwm); delay(500-runtime);
servo2.writeMicroseconds(1500); servo3.writeMicroseconds(1500);
//-30C 1/4 servo1.writeMicroseconds(1500 - speed - engine1offsetrightpwm); servo4.writeMicroseconds(1500 + speed + engine4offsetrightpwm); delay(500-runtime); 
servo1.writeMicroseconds(1500); servo4.writeMicroseconds(1500);
// 0C 2/3 servo2.writeMicroseconds(1500 - speed - engine2offsetrightpwm); servo3.writeMicroseconds(1500 + speed + engine3offsetrightpwm); delay(500-runtime);
servo2.writeMicroseconds(1500); servo3.writeMicroseconds(1500);
// 0C 1/4 servo1.writeMicroseconds(1500 + speed + engine1offsetleftpwm); servo4.writeMicroseconds(1500 - speed - engine4offsetleftpwm); delay(500-runtime);
servo1.writeMicroseconds(1500); servo4.writeMicroseconds(1500);
//+30C 1/4 ...
//-30C 2/3 ...
// 0C 1/4 ...
// 0C 2/3 ...
```

Hmm, the labels "+30C"/"-30C"/"0C" are a bit cryptic. Anyway.

The key point for interpretation: the 360 version used 360° continuous-rotation servos with calibration offsets; the 180 version (V1.1) uses positional servos with hardcoded angles, where 90 = neutral, and values <90 or >90 swing the leg. Mirroring: for the same "forward" pose, servo1/servo3 get 40 while servo2/servo4 get 140 — complementary. So the left and right legs are mounted mirrored (opposite orientation), requiring complementary values. Note: this is servo1 vs servo3 (both one diagonal?) Hmm.

Let's establish geometry from the front() sequence in the 180 version:
- Pair (s2, s3) move together with opposite values (s2=140,s3=40).
- Pair (s1, s4) move together with opposite values (s1=40,s4=140).
So within each pair, the two servos get complementary values. With mapping s1=RF, s2=RR, s3=LF, s4=LR: pair A = (s2=RR, s3=LF) - diagonal, complementary; pair B = (s1=RF, s4=LR) - diagonal, complementary. And note first pair A gets (140, 40) i.e., s2=140 while s3=40. Then pair B gets s1=40, s4=140. So s1 (RF) copies s3 (LF)? s3=40 in step 1, s1=40 in step 2. And s2=140 in step1, s4=140 in step2. So the two front legs (s1, s3) both use 40 in the first phase, and the two rear legs (s2, s4) both use 140. That's interesting: front legs share one value, rear legs share the complementary value. That means: left-front and right-front are mounted mirrored relative to each other (since they need opposite PWM for the same physical direction)?? Hmm, no — if front legs s1 and s3 both write 40 at the same time, then in the physical robot they must be mirrored mounts (so the same PWM value produces mirrored physical motion, which for a left/right pair walking means both legs move forward). Yes: s1 and s3 are a left/right pair (both front), and they receive the SAME value (40), which implies mirrored mounting. Similarly s2, s4 are the rear pair and both receive 140.

Wait, but I derived servo1=右前 and servo3=左前 from toplefthand/toprighthand. So front pair (s1 RF, s3 LF) both get 40 while rear pair (s2 RR, s4 LR) both get 140. Hmm, s3=LF gets 40 in step 1 and s1=RF gets 40 in step 2 — but at different times (100ms apart). And rear s2=140 in step1, s4=140 in step2.

So exactly: within a phase, the front/rear pairs both move out and then return? Let's trace the full 8-step cycle:

t1: s2=140 (RR), s3=40 (LF)
t2: s1=40 (RF), s4=140 (LR)
t3: s2=90, s3=90
t4: s1=90, s4=90
t5: s1=140 (RF), s4=40 (LR)
t6: s2=40 (RR), s3=140 (LF)
t7: s1=90, s4=90
t8: s2=90, s3=90

So servos 1&3 (front legs) get 40 at t2/t1 and 140 at t5/t6; servos 2&4 (rear legs) get 140 at t1/t2 and 40 at t6/t5. So each leg alternates between 40 and 140, with the front and rear pairs in anti-phase (diagonal trot). And legs 1 and 3 (the front left/right pair) get the SAME numbers at the same phase; legs 2 and 4 (rear pair) get the SAME numbers. This is consistent with mirrored mounting between left and right legs.

Hmm — but careful: does servo1 and servo3 both getting 40 mean they're mirrored? If both front legs have identical mounting, then the same PWM (40) would swing both legs in the same rotational direction, which physically would be one forward and one backward (since they're on opposite sides facing opposite directions... no). Hmm. Actually this is about which way "forward" is. Let me reason physically:

For a servo mounted on the left side with horn pointing outward-left, and a servo on the right side with horn pointing outward-right (mirrored), writing 40 on both makes the left leg rotate CW (viewed from left) and the right leg rotate CCW (viewed from right) — which are mirror images, i.e., both legs swing the same way relative to the body (both forward). That's the mirrored mounting case and the code uses the same value for both => consistent with mirrored mounting.

For toplefthand/toprighthand: s3 goes to 0 then 30 then 90 (lift), s1 goes to 180 then 150 then 90. Interesting - these are NOT symmetric: left uses 0..30, right uses 180..150. If mirrored mounting, "lift" would be the same direction for both... 0 vs 180 are opposite ends of travel. So for the lifting motion, left goes toward 0 and right goes toward 180.

Hmm, so the left and right legs are mounted so that... let's think: the servos are mounted in the base plate, all pointing the same direction (all identical orientation, since they're mounted on the same PCB in the same direction, "底壳部分为舵机设计了4个限位槽" - 4 slots). Hmm, if all 4 servos are mounted identically (all horns pointing the same way), then the same value produces the same physical rotation direction for all 4. Then in front(), giving the front pair 40 and the rear pair 140 would mean front legs rotate one way and rear legs the other way — which is what you want for a trot (front legs step forward while rear push back = same rotation? no...).

Hmm, in a walking gait, all legs need to swing backward relative to the body to push the body forward — all 4 legs rotate the SAME physical direction during stance. And during swing, all 4 rotate the opposite direction. So if all servos are mounted identically, all 4 legs should receive the SAME value in a "stand and push" pattern... but a trot has diagonal pairs in anti-phase, so the diagonal pairs get complementary values: LF+RR together, RF+LR together. In this code, front pair (s1,s3) get 40 while rear pair (s2,s4) get 140 — that's front-vs-rear, not diagonal, in terms of value grouping. Hmm, but wait: is the grouping front/rear or left/right?

I derived s1=RF, s3=LF (front pair) from toplefthand/toprighthand. But hold on — is that derivation right? toplefthand() uses servo3, toprighthand() uses servo1. Yes, that's direct evidence for s3=left, s1=right. Which end (front or rear) is unknown from that alone.

Alternative mapping possibility: s3 = left-front, s1 = right-front (from GH fork comment "servo3.write(40); //左前向前旋转50度"). Hmm, the GH fork comment says s3 = 左前 (left front). And says s2 = 右后 (right rear). That's consistent with s1=右前(RF) and s4=左后(LR).

So the pairs in front() are: {s1 RF, s3 LF} = front pair → same value 40 first; {s2 RR, s4 LR} = rear pair → same value 140 first.

Hmm, that means left/right legs get the SAME values (RF=LF=40; RR=LR=140) → mirrored mounting? No wait. If left and right legs are mirrored in mounting, then to make them both swing "forward" you'd need... Let's set up: a servo horn rotates in a plane parallel to the body's side plane (legs swing fore-aft). Actually for these desktop dogs, the servos are mounted flat on the base with the horn axis vertical, and the legs stick out to the sides. The horn rotates in the horizontal plane: the leg swings forward/backward. Left and right legs point in opposite lateral directions.

Case 1: servos all mounted identically (same orientation, e.g., all horns' zero pointing forward). Then a given PWM value produces rotation in the same angular direction, say CCW viewed from above, for all 4. For the left leg (pointing left) and right leg (pointing right), the CCW rotation moves the left leg forward and the right leg backward. So for both to swing forward you'd need complementary values (e.g., left=40, right=140). In that case front() would give s_LF=40 & s_RF=140 — but the code gives both 40. Hmm, but 40 vs 140 for the front pair... in front() the front pair both = 40 at their phase. So under Case 1 that would mean the front legs both swing the same rotational direction → one forward, one backward. That can't walk.

So more likely Case 2: the legs/servos are mirrored left-right. Then a given identical value makes both left and right legs swing the same direction (both forward or both back). So front()'s use of identical values (both front legs = 40) is consistent with mirrored mounting (mirrored horns/legs), i.e., left and right are mirror images.

Hmm, but that's contradicted by toplefthand(0..30) vs toprighthand(180..150) — if mirrored, "lift the leg" would be the same value direction for both. 0 vs 180 are opposite. So for the lift, the two sides use opposite extremes. Hmm, that suggests all servos mounted identically (non-mirrored), because with identical mounting, "rotate the leg up/outward" would be opposite rotational directions for left vs right legs.

Hmm, this is a contradiction. Let me reconsider: maybe in toplefthand, s3 lifts the leg by rotating the leg from 90 to 0 then to 30 — i.e., "up" is toward 0 for the left side; and toprighthand rotates s1 from 90 to 180 then 150 — "up" toward 180 for the right side. If the mounts were mirrored, lifting would be the same direction on both sides (e.g., both toward 0). So the observations suggest the servos are NOT mirror-mounted (all identical orientation), so lifting left leg = decrease angle, lifting right leg = increase angle.

But then front() giving both front legs the same value 40 would mean they swing in the same rotational direction... which for identically-mounted left and right legs means one goes forward and other goes backward. Hmm! Unless the gait relies on that: this is a "swing" pattern. Let's think about what makes a trot with identical (non-mirrored) mounts: For a trot, LF and RR move together (both swing forward → need same physical direction), and RF and LR together. With non-mirrored identical mounting, "same physical rotation direction" = same PWM value. So LF and RR should get the same value, and RF and LR the same (complementary) value. That means the pairs should be diagonal: {LF, RR} and {RF, LR}.

Now in front(): the pairs are (s2,s3) and (s1,s4) — with s3=LF, s2=RR → that's the diagonal {LF, RR}! And (s1=RF, s4=LR) → the other diagonal. ✓. But WAIT: within pair (s2,s3), the values are s2=140 and s3=40 — NOT the same. Hmm. And within pair (s1,s4): s1=40, s4=140 — not the same. So within diagonals the values are complementary (140 vs 40), while between diagonals at a given phase... s2=140 (t1) and s4=140 (t2) — same value but different times.

Hmm. So the pattern is: 
- Diagonal A (s2=RR, s3=LF): s2 gets 140, s3 gets 40 (complementary).
- Diagonal B (s1=RF, s4=LR): s1 gets 40, s4 gets 140 (complementary).

So the left legs (s3 LF, s4 LR) get: s3=40, s4=140 → complementary. The right legs (s1 RF, s2 RR) get: s1=40, s2=140 → complementary. So left legs and right legs each have one leg at 40 and the other at 140. And crucially: s1 (RF) = 40 and s3 (LF) = 40 → the two FRONT legs get the same value; s2 (RR) = 140 and s4 (LR) = 140 → the two REAR legs get the same value.

So the value grouping is front-vs-rear, i.e., front legs share a value, rear legs share the complementary value. Hmm, interesting. That's an unusual gait (front/rear pairs rather than diagonal), but with delays and the 100ms sequencing/timing, the actual physical result is a "shuffling" walk. Actually, this is the classic beginner 4-servo dog code where the pairing is front-pair vs rear-pair with phase offsets; it works because each pair alternates.

Given the front pair shares a value and rear pair shares the complementary value, and given the "lift" direction is opposite on left vs right (0 for left, 180 for right), we can conclude... hmm, let me think about whether front legs sharing a value is consistent with NOT-mirrored, same-orientation mounts:

Since front legs both get 40 (say "leg rotates CW" for both), and rear legs get 140 ("CCW" for both). Hmm, if all 4 servos are mounted identically (same orientation, e.g., all shafts at the same corner of the servo), then CW rotation of the horn moves the left leg and right leg in opposite fore/aft directions (left leg forward, right leg back). So front-left would go forward and front-right would go back — the dog would try to twist, not walk. Unless the legs are mounted mirrored (left legs mirrored vs right legs).

I think the real physical arrangement is: servos are all mounted in the same orientation in the base (4 slots), but the LEGS (the plastic feet) are mirror-images, so left and right legs' "outward" direction is mirrored. Hmm, the effect of that is second-order.

I should be careful and not overclaim. The safest, evidence-based statements:
1. In the original front()/back(), left-side and right-side legs receive complementary numbers in some places and identical in others; specifically, servo1 (right) and servo3 (left) both get 40 in front() (and both get 140 in back()'s second phase); servo2 (right rear) and servo4 (left rear) both get 140 in front(). So it's NOT a simple "40 vs 140 mirror between left and right"; rather, the complementary pairs are front-pair vs rear-pair (servo2/servo3 vs servo1/servo4 as diagonals), and left/right legs on the same end receive the SAME value.

Hmm wait, I need to double check the leg assignment. Let me verify with the oshwhub 360-version front() comments: "+30C 2/3" and "-30C 1/4", "0C 1/4", "0C 2/3" — the labels suggest "C" = ? Maybe "C" is degrees and the number is the pair (2/3 = servos 2 and 3 as a pair, 1/4 = servos 1 and 4 as a pair). So the pairs are {2,3} and {1,4} — consistent with what I said. The sign indicates direction: +30 for pair 2/3, -30 for pair 1/4, then 0 for pair 2/3, 0 for pair 1/4... So the two pairs move in opposite sign directions. In the 360 version, speed offsets are applied via offsetleft/offsetright calibration values per servo, which encode the physical direction/trim of each servo. This suggests that in the 360 version, individual calibration offsets per servo (left/right turn compensation) were per-servo, meaning each servo has its own direction/speed calibration.

OK. The most reliable statement for the user's purposes: 

Regarding question 3 (same vs mirrored): In front(), servo2=140 & servo3=40 are simultaneous and complementary; servo1=40 & servo4=140 are simultaneous and complementary. So the mirrored/complementary pairing is (servo1,servo4) and (servo2,servo3) — i.e., the servos that move as a diagonal pair with opposite numbers. Also, the two front legs (s1,s3) end up with the same number and the two rear legs (s2,s4) with the same number at corresponding phases.

Hmm, hold on. Let me re-derive which servos belong to which planform position. Is there independent evidence? Let's look at the local/original image.cpp or web pages, or the wiki software page (maybe eda-robot-software page exists with a wiring table). Let me check the wiki pages list. The oshwhub page had links: introduce, hardware, 3d, enclosure, download. Maybe there's also a "software" page. Let me try eda-robot-software.html.

Also the local project's control.html might label buttons with servo/leg names.

Also there might be a 立创 wiki page "EDA-Robot项目电子实训文档.pdf" (the attachment). The PDF link: https://image.lceda.cn/easyedaResource/images/90df0661fc474cfd82e2d9b4c6448a27.pdf — that's probably a different pdf (the one shown in the page). Actually the oshwhub page says 离线文档：请查看附件【EDA-Robot项目电子实训文档.pdf】. Let me try the wiki software page and maybe get the PDF.

Let me also check: does the local project have `int speed = 300;`? Let me check the Gitee original for that.

Let me run these checks.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== does original have speed var / engine.html route? ===\"\ngrep -n \"int speed\\|engine.html\\|/engine\\|LittleFS\\|SPIFFS\" gitee_main.cpp | head -20\necho \"=== local engine.html button labels ===\"\nnode -e \"\nconst fs=require('fs');let s=fs.readFileSync('/c/Users/UserX/Downloads/Robot dog 1.1/data/engine …[截断,原长412]` → `Exit code 1 === does original have speed var / engine.html route? === 198: fs::File file = SPIFFS.open(ssidFile, "w"); // 打开文件进行写入 228: // 检查SPIFFS文件系统中是否存在index.html文件 229: if (SPIFFS.exists("/index.html")) { 230: fs::File file = SPIFFS.open("/index.html", "r"); // 打开index.html文件 250: // 检查SPIFFS文件系统中是否存在index.html文件  …[截断,原长1748]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\nfor p in eda-robot-software eda-robot-introduce; do\n curl -sL -m 30 -A \"$ua\" \"https://wiki.lceda.cn/zh-hans/course-projects/smart-internet/eda-robot/$p.html\" -o w2_$p.html -w \"$p %{http_code} %{siz …[截断,原长413]` → `eda-robot-software 200 348161 eda-robot-introduce 200 136243 ## w2_eda-robot-introduce.html | 舵机1 => 3K简易读卡器 页面导航 ​ 资料超详细 👇 项目介绍 硬件设计 软件设计 烧录教程 3D结构 附件下载 硬件工程 3D工程 项目简介🪄 ​ 本项目基于ESP8266构建，是一个可以手机控制的桌面宠物，电路大部分使用插件封装，易于新手焊接，方便焊接。 本项目不含电池成本大致为30元，主要费用在于舵机12元，屏幕4.5元，主控4元 项目功能 ​ ✅手机遥控 ✅表情显示 ✅每日天气 ✅时钟显示 项目参数🔮 ​ 本设计采用ESP8266主控 …[截断,原长4894]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:21）

Let me check the local project's extra files and the wiki software page for leg/servo mapping.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The wiki software page mentions left90() and right90() functions, but the Gitee 180-version code doesn't have them as `void left90()` - wait, I searched and it said NOT FOUND. Let me check the actual wiki software page, which is the 360-degree version. The wiki mentions left90() and right90() - that's the 360 servo version which used writeMicroseconds with offsets. The Gitee repo has only the 180 version (V1.1), which the README says: "本仓库存储为180舵机代码，360舵机版程序已不再维护".

So the local modified copy's front()/back()/left()/right()/sitdown()/lie()/toplefthand()/toprighthand()/dosleep() are byte-identical (modulo comments/whitespace) to the Gitee 180-degree V1.1 original.

Let me also verify the local code uses LittleFS instead of SPIFFS (a modification), and check the local differences summary. Let me also check the oshwhub page's "附件" (attachments) - software source zip. And check whether oshwhub also hosts an earlier version. Also try one or two more searches to be thorough — e.g., the 360 version source on oshwhub attachments, and confirm the authors.

Let me finish with:
1. Check local mods (LittleFS vs SPIFFS, AP password, weather key, added endpoints like /left90 /right90 maybe)
2. Get oshwhub project metadata (author, created time, views).

Let me also double-check the servo mapping question: In the original, front() moves servo2/servo3 (first pair) and servo1/servo4 (second pair). In front(): servo2.write(140); servo3.write(40) — these are same direction? servo2=140, servo3=40 — that's mirrored/complementary. Then servo1.write(40); servo4.write(140) — also mirrored. So servo2/servo3 are mirrored, and servo1/servo4 are mirrored. In sitdown: servo2.write(140), servo4.write(40) — mirrored. In lie: servo1.write(180), servo3.write(0), servo2.write(0), servo4.write(180) — servo1/servo4 = 180 and servo2/servo3 = 0. So pairs (servo1,servo4) and (servo2,servo3) are mirrored pairs.

Wait — in lie: servo1=180, servo3=0, servo2=0, servo4=180. So servo1 & servo4 same (180), servo2 & servo3 same (0). Hmm, that contradicts. Let's re-read: 

lie():
- servo1.write(180)
- servo3.write(0)
- servo2.write(0)
- servo4.write(180)

So servo1=180, servo2=0, servo3=0, servo4=180. So servo1 & servo4 are together (180), servo2 & servo3 together (0).

But in front(): servo2=140, servo3=40 (opposite), servo1=40, servo4=140 (opposite).

Hmm. So in front(), servo2/servo3 rotate opposite directions, and servo1/servo4 rotate opposite directions. In lie, servo1/servo4 both 180 and servo2/servo3 both 0.

Actually with mirrored mounting: for a mirrored pair, sending the same angle makes them rotate in opposite physical directions. In front(), servo1 and servo4 receive 40 and 140 (different numbers), so if they are mounted mirrored, they'd actually move in the same physical direction... Hmm, this is getting complicated. Let me carefully determine this from the code comments — but the original comments are sparse.

Actually, for the report I should just state facts:
- In the original front(), the two "left/right" pairs get complementary numbers: servo2=140 & servo3=40 (one servo is the "front-left", other "front-right"), and servo1=40 & servo4=140.
- In sitdown(): servo2=140, servo4=40 → complementary.
- In lie(): servo1=180, servo3=0, servo2=0, servo4=180 → this suggests servo1&servo4 as same physical role, servo2&servo3 same role... 

Hmm wait. Let me think about the geometry. A typical 4-servo quadruped where each servo directly drives a leg. If the servos are mounted mirrored left/right (i.e., left legs' servos face one way, right legs' face the other), then:
- to swing a leg forward on the left, you write a value < 90 or > 90 depending on side.

For "front" (walking forward), each leg swings forward then backward. Looking at the sequence:
- Servo2=140, servo3=40 → one leg forward, other backward? Actually for walking, diagonal legs move together.

Hmm, actually let me reconsider: with 2 servos per side pair, maybe (servo1, servo2) are on one side (front-left and back-left?) and (servo3, servo4) on the other side.

Let's use the pairing that the code itself uses: pairs that move together are (servo2, servo3) and (servo1, servo4) — these are moved in the same "phase" in front/back. In front(): first servo2 & servo3 move (140/40), then servo1 & servo4 (40/140). Then all return to 90 (neutral). Then servo1 & servo4 move (140/40), then servo2 & servo3 (40/140). 

So the "diagonal gait": first half lifts/swings pair A, second half pair B. Actually a standard trot: diagonal legs (front-left + back-right) move together.

Given the code moves (servo2, servo3) together and (servo1, servo4) together, likely servo2 & servo3 are one diagonal pair and servo1 & servo4 the other diagonal pair. Hmm, but they're given opposite numbers 140/40.

Alternatively, servo1/servo2 are on the left side (front-left, back-left) and servo3/servo4 on the right side, mounted mirrored. Then servo2 & servo3 = back-left & front-right (diagonal), and servo1 & servo4 = front-left & back-right (other diagonal). That fits a trot gait! And the opposite numbers (140 vs 40) would be because the two legs of a diagonal are on mirrored sides: to move both forward, one needs >90 and the other <90 (because the servos are mirrored).

That's consistent with: mirrored left/right mounting, so for a diagonal pair moving forward together, one servo gets 140 and the mirrored one gets 40. 

And in lie(): servo1=180, servo4=180, servo2=0, servo3=0. Hmm, that would mean servo1 & servo4 (front-left & back-right) go to 180 and servo2 & servo3 (back-left & front-right) go to 0. Under mirroring, servo1=180 (front-left extreme) & servo4=180 (back-right extreme) — for a mirrored pair those give opposite physical directions... 

Hmm, unless each leg's pitch has a sign such that 0 = leg tucked, 180 = leg extended. In lie() ("趴下" = lie flat), all four legs should splay flat. So servo1=180 and servo4=180 both extend, but they're mirrored so same number = opposite physical? That doesn't work either. Actually with mirrored mounting, same number = opposite physical rotation ONLY if the mirror is about the fore-aft axis... 

I think I'm overanalyzing. Rather than assert, I should report what the code says and flag the pairing as an inference, marked uncertain. But I can state the concrete fact: in front()/back() the left and right legs receive mirrored/complementary numbers (e.g., 140 vs 40), i.e. NOT the same numbers within each diagonal pair; and within a pair (servo1/servo4 or servo2/servo3) the numbers are 40 vs 140 — complementary.

Also, in sitdown(): servo2=140, servo4=40. So servo2 and servo4 are the "front legs" that lift, and they take complementary values. If servo2 & servo4 were a mirrored pair (both front legs) — hmm, but earlier I hypothesized servo2 & servo3 form a diagonal pair. In sitdown, the front legs are raised — if front legs are servo2 and servo4, then servo2 and servo4 get 140 and 40.

Let's cross-check with toplefthand() = servo3 (grab left hand), toprighthand() = servo1 (grab right hand). So servo3 = left hand (left front leg), servo1 = right hand (right front leg). Therefore servo2 and servo4 = the two hind legs (left hind = servo2? right hind = servo4?).

So: front legs = servo1 (right front) and servo3 (left front). Hind legs = servo2 and servo4.

In sitdown(): servo2=140, servo4=40 → both hind legs bend → sitting (hind legs fold). Makes sense!

In lie(): servo1=180, servo3=0, servo2=0, servo4=180 → front-right=180, front-left=0, hind-left=0, hind-right=180. So the left legs (servo3, servo2) = 0, and the right legs (servo1, servo4) = 180. So left and right are mirrored: left legs at 0, right legs at 180 for "lying flat with legs splayed out". That confirms: servo3 = left-front, servo2 = left-hind, servo1 = right-front, servo4 = right-hind. And left vs right receive MIRRORED numbers (0 vs 180 for the same physical pose).

Now front(): servo2=140 (left-hind), servo3=40 (left-front) — hmm, these are on the same side but different numbers? That means left-front and left-hind rotate in different directions (one forward, one backward) — that's a walking/trotting motion where diagonal legs are in phase: left-front (servo3=40) and right-hind (servo4) ... wait in front() first move is servo2=140 & servo3=40. servo2 = left-hind = 140, servo3 = left-front = 40. Those are opposite directions. So left legs move in opposite directions. Then next: servo1=40 (right-front) & servo4=140 (right-hind): right legs also opposite.

Hmm, that's like a "twisting"/crawling gait. Then to return to neutral, then again. OK. Actually for a 4-servo robot where each servo drives a leg's rotation about a vertical (yaw) axis, the walking motion is done by rotating legs like a "rotating" crawl — the robot drags itself forward. This is the classic "servo leg rotates about vertical axis, friction-based crawl" design. So in front(): left-front (servo3) and left-hind (servo2) get opposite numbers (40 vs 140) meaning the left legs rotate in opposite yaw directions; and same for the right.

Given mirrored mounting: servo3 (left-front) = 40, servo1 (right-front) = 40. Same number on mirrored servos → opposite physical yaw. And servo2 (left-hind) = 140, servo4 (right-hind) = 140. Hmm, so left-front & right-front both get 40; left-hind & right-hind both get 140.

So the answer to question 3 (whether left/right get SAME or MIRRORED numbers): In front()/back(), the left and right legs receive the SAME numbers for the same leg-position (front-left servo3=40 & front-right servo1=40; hind-left servo2=140 & hind-right servo4=140). And the front/back legs receive COMPLEMENTARY numbers (40 vs 140). Interesting — that's the opposite of what the task hypothesized ("40 vs 140").

Let me verify with front() carefully:
```
servo2.write(140); // 舵机2旋转至140度
servo3.write(40);  
delay(100);
servo1.write(40);  
servo4.write(140); 
```
servo2 = left-hind = 140; servo3 = left-front = 40; servo1 = right-front = 40; servo4 = right-hind = 140.
So pairs by number: {servo3, servo1} = 40/40 (the two FRONT legs) and {servo2, servo4} = 140/140 (the two HIND legs); the left/right sides get the SAME numbers.

Then:
```
servo1.write(140); servo4.write(40);
```
servo1 = right-front = 140, servo4 = right-hind = 40 — that's the "return" swing (opposite phase). Hmm, that's actually a phase-2 for the right side while... wait no, in this second half, the right side legs swing the other way.

Hmm, so within front(), the sequence is: (1) front legs 40 + hind legs 140 → (2) all to 90 → (3) right-front 140 + right-hind 40 → (4) left-front 40 + ... wait step (5) is servo2.write(40) (left-hind = 40) and servo3.write(140) (left-front = 140). So it alternates: first the front/hind pattern (40/140), then the right legs swing (140/40), then the left legs swing (140/40). 

Hmm, this is a rotation-based crawl: the robot rotates its legs in one direction all together to push, then lifts and resets. Honestly, this is the classic "rotate all legs CCW then reset" walk.

I'll report facts:
- Left vs right legs get the SAME numbers (servo1 right-front and servo3 left-front both 40; servo2 left-hind and servo4 right-hind both 140), i.e., all four servos are mounted identically (NOT mirrored), OR the code compensates.
- Front vs hind legs get COMPLEMENTARY numbers (40 vs 140) in the same sub-step.
- The pairs sharing the same numbers in front() are {servo3, servo1} = {both front legs} and {servo2, servo4} = {both hind legs}.

Hmm wait, but in lie(): servo1=180, servo4=180 (both RIGHT legs = 180) and servo2=0, servo3=0 (both LEFT legs = 0). That means left/right get opposite numbers in lie(). That contradicts "left/right get same numbers".

Hmm! Unless my leg assignment is wrong. Let's redo with an alternative: maybe servo1 & servo4 are the two front legs... no, toplefthand uses servo3 and toprighthand uses servo1. "抬左手" (lift left hand) = servo3 → left-front = servo3. "抬右手" (lift right hand) = servo1 → right-front = servo1. That's solid.

So in lie(): servo1 (right-front) = 180, servo3 (left-front) = 0 → left/right front legs get mirrored numbers (0 vs 180). And servo2 (left-hind) = 0, servo4 (right-hind) = 180 → left-hind = 0, right-hind = 180. So indeed in lie(), left = 0 and right = 180 — mirrored numbers. So the left/right legs are MIRRORED in lie().

But in front() step 1: servo2 (left-hind) = 140, servo4 (right-hind) = 140 → same numbers. That contradicts mirrored mounting... unless front() is intentionally not symmetric (it's a crawling/turning gait). But wait, front() is "前进" (forward). Hmm, in a friction-crawl gait with mirrored legs, to go forward you might write the same number to mirrored servos because mirrored servos with the same command rotate in opposite yaw (which is what you want: both legs sweep "backward" relative to the body?). Hmm no.

Honest approach: I'll report the verbatim code and describe the number patterns factually (which servos get the same vs complementary numbers in each function), and explicitly flag the physical interpretation as uncertain, since the original code+wiki doesn't document mounting orientation in the parts I could read. I can also point out that lie() and dosleep() and sitdown() imply left/right mirroring, while front()/back() assign identical numbers to the left/right pair-of-front and pair-of-hind servos.

Actually, let me reconsider the geometry once more. Actually maybe the pairing is: servo1 = right-front, servo2 = right-hind, servo3 = left-front, servo4 = left-hind. Then in lie(): servo1 (right-front) = 180, servo2 (right-hind) = 0, servo3 (left-front) = 0, servo4 (left-hind) = 180. Still left/right mirrored.

Alternatively: maybe lie() is deliberately asymmetric... no, "lie" should be symmetric.

OK, hold on. Let me reconsider: what if the servos are mounted such that each servo drives a leg about a horizontal axis (pitch), not yaw? Then "legs splay out flat" = ... Let's test with lie(): all four legs at extremes (180/0) → yes, that's legs extended flat/splayed, which is what "趴下/lie" means (the dog lies flat with legs out). Both left legs are at 0 (servo2, servo3) hmm no: with my assignment left legs = servo3 (LF) and servo2 (LH) = 0 and right legs = servo1 (RF), servo4 (RH) = 180. So left legs at 0 and right at 180. If servos are mirrored (left/right mounted oppositely), then the same physical pose requires opposite numbers → left at 0, right at 180 = same physical pose. ✓. That's consistent with MIRRORED mounting.

Now front() with mirrored mounting: servo3 (LF) = 40, servo1 (RF) = 40 → mirrored servos given same number → legs rotate in OPPOSITE physical directions. For a forward walk with mirrored legs, you'd expect opposite physical yaw... Actually for a walking gait, you want each leg to sweep backward (in body frame). For the left leg, "backward" is one servo direction; for the right leg (mirrored), "backward" is the opposite servo direction. So you need opposite numbers. But the code gives the same number (40) to both front-left and front-right. That would sweep them in opposite body-frame directions → the robot would twist, not walk forward. UNLESS the servos are NOT mirrored but all mounted identically, in which case the same number = same physical direction... but then lie() with 0/180 for left/right would give an asymmetric pose.

Hmm. Contradiction. Unless in front() the *pairing* is not LF/RF. Let me recheck: what if the first sub-step moves servo2 & servo3 (which are, e.g., right-front & right-hind = the whole RIGHT side)? For the right side to move forward you'd need... hmm.

Actually let's just consider: pairs {servo2, servo3} and {servo1, servo4} get the complementary values in the same sub-step (140 & 40). If {servo2, servo3} = left-front & right-front... no wait.

Possibility: {servo2, servo3} = the two legs of one SIDE... hmm, but toplefthand = servo3, toprighthand = servo1. servo2 and servo4 unknown. In sitdown, servo2 & servo4 are used (hind legs fold) with 140/40 — consistent with servo2 and servo4 being the hind legs, one left one right. And in sitdown, they get complementary numbers (140 vs 40) → mirrored mounting for hind pair. ✓ Consistent with lie() giving mirrored numbers for left/right. ✓✓

So: servo1 = right-front, servo3 = left-front (from toplefthand/toprighthand), servo2 = left-hind (or right-hind), servo4 = the other hind leg. In lie(): servo1=180 (right-front), servo3=0 (left-front) → mirrored ✓. servo2=0, servo4=180 → so servo2 = left-hind, servo4 = right-hind (to match left=0/right=180). 

Now back to front(): sub-step 1 = servo2 (left-hind) = 140 and servo3 (left-front) = 40 → the LEFT side's two legs get opposite numbers → left legs yaw in the same physical direction (opposite numbers on non-mirrored left-side servos... hmm, but left-front and left-hind may be mounted mirrored relative to each other too, front-to-back!).

Ah, that's it: in these 4-servo designs, typically the two servos on each side are mirrored front-to-back (or the legs are mirror images). For the left-side pair: to make both left legs sweep backward, servo LF and LH need opposite numbers if they're mounted mirrored about the mid-line. So front() sub-step 1: left-hind 140 + left-front 40 = both left legs sweep the same way ✓. Sub-step 2 = servo1 (RF) = 40 and servo4 (RH) = 140 → both right legs sweep the same way (mirrored relative to left: RF=40 corresponds to RF's backward direction... whatever). Then all to 90. Then sub-step 3: servo1 (RF) = 140, servo4 (RH) = 40 → right legs sweep the other way. Sub-step 4: servo2 (LH) = 40, servo3 (LF) = 140 → left legs sweep the other way. So the gait = move all legs one way (steps 1-2), neutralize, then move them back (steps 3-4). This is a classic "push then swing" friction crawl. 

So the code pairs by SIDE (left pair = servo2 + servo3 → wait no, servo2 = left-hind and servo3 = left-front → yes! {servo2, servo3} = LEFT SIDE pair; {servo1, servo4} = RIGHT SIDE pair: servo1 = right-front, servo4 = right-hind ✓).

So in front(): left side = (servo3=40, servo2=140); right side = (servo1=40, servo4=140). Left and right get the SAME numbers (LF & RF both 40; LH & RH both 140). Since the right side is mirrored relative to the left, the same numbers give opposite physical yaw on the two sides... For a forward crawl: all four legs must push backward. With side-mirrored mounting: on the left side, leg sweep backward = some servo value; on the right side (mirrored about the body centerline), the backward sweep = the same value if the mirroring is left-right (a mirror swap). Yes! With left-right mirrored mounting, applying the SAME command to mirrored servos produces the SAME body-frame rotation direction (this is exactly how mirrored servos are used: identical numbers → symmetric leg motion; e.g., both legs splaying outward with the same number). 

Yes — mirror symmetry: if the right leg is the mirror image of the left leg and its servo is also mirrored, then applying the same angle produces a mirror-symmetric configuration, i.e., both legs rotate "forward" (in their own frames). So front() with same numbers on left/right = symmetric = both legs sweep forward/backward together. ✓ This is consistent with lie() too: lie() gives 0 for left and 180 for right — that's ANTI-symmetric, i.e., legs splay outward... hmm, for "lying flat", either works.

OK so what's the truthful, defensible statement?

Facts from the code:
- front(): the two front legs (servo1 right-front, servo3 left-front) both get 40 in the same step; the two hind legs (servo2 left-hind, servo4 right-hind) both get 140. → Left/right legs of the same position receive the SAME numbers.
- Left and right therefore are commanded identically, which is the hallmark of MIRRORED mounting (mirrored servos + same command = symmetric motion). This is an inference, but it's strongly supported: sitdown() commands the two hind legs 140 vs 40 (opposite) to fold them symmetrically — implying for hind legs, opposite numbers = symmetric. Hmm, that contradicts the front() inference!

Ugh. sitdown(): servo2 (LH) = 140, servo4 (RH) = 40 → opposite numbers for the two hind legs, described as "坐下" (sit down, i.e., hind legs fold symmetrically). And front() step 1 has servo2 (LH) = 140 and servo4 (RH) = 140 → same numbers for the two hind legs.

Both patterns appear for the SAME pair (servo2 & servo4), with different numbers. So the design must be: the two hind servos are mirrored opposite hand... hmm, or not mirrored.

Hmm, if the two hind servos (2 & 4) are mounted as mirror images, then same number = symmetric. In sitdown they get 140 and 40 = anti-symmetric — that would be an asymmetric pose (one leg folds, the other extends). That can't be "sit". So they're probably mounted the SAME way (identical orientation), in which case 140/40 = one rotates one way, the other the other way... also asymmetric in body frame. Hmm!

Unless... servo2 is a LEFT leg and servo4 is a RIGHT leg with mirrored mounting, and "sitting" means both hind legs rotate outward (in opposite body-frame directions) — e.g., legs splay sideways → the body drops. That's plausible actually! Sitting in this design = hind legs fold sideways/outward, dropping the rear. With mirrored mounting, opposite numbers produce opposite body-frame rotations = both legs rotating "outward"... hmm, no: opposite body-frame rotations = one outward one inward.

I don't have the physical build. The honest answer: the code does not document the mounting; from the code, left and right legs sometimes get identical numbers (front/back step 1-2) and sometimes complementary numbers (sitdown, lie), so I cannot determine orientation from the code alone. I should say this plainly and mark it uncertain. I can, however, give the concrete facts:
- lie() and dosleep() and sitdown() pair the two left legs with 0 and the two right legs with 180 (lie) — i.e., left/right mirrored numbers.
- front()/back() pair the two FRONT legs (servo1, servo3) with the same value and the two HIND legs (servo2, servo4) with the same value, and use complementary values between front and hind.
- In front()/back(), the left-side legs do NOT receive mirrored values relative to the right-side legs; they receive identical values (both front legs 40, both hind legs 140).

Wait, but hold on. Let me re-examine whether servo1 is a front leg and servo2 is a hind leg. toplefthand = servo3, toprighthand = servo1 → servo3 and servo1 are the "hands". Hmm, unless "left hand" = left-front and "right hand" = right-front. Yes.

Then in lie(): servo1 = 180 (RF), servo3 = 0 (LF), servo2 = 0 (LH), servo4 = 180 (RH). So RIGHT legs = 180, LEFT legs = 0. So left/right互补 → mirrored.

And front(): sub-step 2: servo1 = 40 (RF), servo4 = 140 (RH); sub-step 3 (later): servo1 = 140, servo4 = 40. And sub-step 1: servo2 = 140 (LH), servo3 = 40 (LF); later servo2 = 40, servo3 = 140 (LF). So in each sub-step, left and right legs at the same position get the SAME number: RF & LF both 40 then both 140... wait: sub-step 1 gives LH=140, LF=40. Sub-step 2 gives RF=40, RH=140. Sub-step 3 gives RF=140, RH=40. Sub-step 4 gives LH=40, LF=140.

Group by physical position:
- LF (servo3): 40 (step1), then 140 (step4).
- LH (servo2): 140 (step1), then 40 (step4).
- RF (servo1): 40 (step2), then 140 (step3).
- RH (servo4): 140 (step2), then 40 (step3).

So in step1: LF=40, LH=140 (left legs complementary). step2: RF=40, RH=140 (right legs complementary). step3: RF=140, RH=40. step4: LF=140, LH=40.

So: within a side, front & hind are complementary. Across sides, the same position gets the same number (LF=40 & RF=40 in steps1-2; LH=140 & RH=140 in steps1-2). So left/right get the SAME numbers — meaning front/back legs are the complementary pair, left/right are identical.

So the answer to Q3 is: In front()/back(), the left-side and right-side legs of the same position receive the SAME servo numbers (LF & RF = 40, LH & RH = 140), NOT mirrored/complementary. The complementary (40 vs 140) relationship in front()/back() is between FRONT legs and HIND legs, not between left and right. In sitdown()/lie(), by contrast, the left/right pair receives complementary numbers (lie: left 0 / right 180; sitdown: servo2 140 / servo4 40).

That's a clean, defensible answer, and it means the modified copy's expectation of mirrored might be wrong. And which value swings forward? Can't determine from code alone without build info — but I can note the comment in the original `front()`: the original wiki/Gitee has comments "//舵机2旋转至140度" which don't say direction. In the oshwhub 360-version page there were comments "//左前向前旋转50度" in the 360 version of front() — wait, that was in `orig_main.cpp` (GH repo eda_robotR1) line 367: `servo3.write(40); //左前向前旋转50度` and `servo2.write(140);//右后向前旋转50度`. So in that derivative, servo3 = 左前 (left-front) and servo2 = 右后 (right-rear) — a DIAGONAL pair! And comment says "向前旋转" (rotate forward) with values 40 and 140 respectively.

Hmm interesting — that comment claims servo3 = left-front and servo2 = right-rear. That contradicts my inference that servo2 = left-hind. It's just a comment by a derivative author though. It says the diagonal pair moves forward: servo3 (left-front) = 40 → forward; servo2 (right-rear) = 140 → forward. So <90 swings forward on the left-front, and >90 swings forward on the right-rear. That's consistent with mirrored mounting: for mirrored legs, forward = 40 on one and 140 on the other. And this comment is from the GitHub derivative's front() which used a diagonal-pair gait (their front() moved servo3=40 & servo2=140 then servo1=40 & servo4=140 → so diagonal pairs (s3,s2) and (s1,s4)).

Hmm, so in the derivative's interpretation: pairs {servo2, servo3} and {servo1, servo4} ARE the diagonal pairs. With servo3=left-front & servo2=right-rear. Then the other diagonal = servo1 (right-front) & servo4 (left-rear). Then in lie(), left-front (s3)=0, right-front (s1)=180, left-rear (s4)=180, right-rear (s2)=0 → left legs: LF=0, LH=180 → complementary (mirrored) ✓; right legs: RF=180, RH=0 → complementary ✓. Consistent with mirrored left/right mounting AND with the diagonal-pair reading. 

And in front(), step1: s3 (LF) = 40, s2 (RH) = 140 → the diagonal pair. step2: s1 (RF) = 40, s4 (LH) = 140 → the other diagonal pair. So the two legs of each diagonal pair get complementary values 40/140 → consistent with mirrored mounting (a left leg and a right leg = mirrored pair, forward = 40 on left / 140 on right).

So under THIS mapping: in front(), the left-side and right-side legs receive COMPLEMENTARY/mirrored numbers: left-front = 40 while right-front = 140 (in different sub-steps, but the same "forward" role gets 40 on left, 140 on right). Yes! Because the left legs (s3, s4) get {40, 140} and the right legs (s1, s2) get {140, 40} — for the same phase, left-front 40 vs right-front 140 (step 3 has s1=140 which is the "forward" for the right-front per the derivative's comment... hmm).

Let's line this up with the derivative's comment-based semantics: "向前" (forward) = 40 on left legs, 140 on right legs. In front(): 
- step1: s3 (LF) = 40 → forward ✓ (left-forward swings forward); s2 (RH) = 140 → forward ✓ (right-rear swings forward). Diagonal 1 = forward.
- step2: s1 (RF) = 40 → hmm, that's 40 on a RIGHT leg. Under mirroring, forward for a right leg should be 140. Hmm. Unless... the derivative's comment says `servo1.write(40);` right after `servo2.write(140)` with comment "//右后向前旋转50度" attached to servo2 only, and servo1's line has no comment. So the comments only label the first two lines.

OK. Given the ambiguity, I'll present the facts and clearly mark the mounting/direction question as follows:
- The best evidence for direction is a comment in the derivative repo pluckypioneer/eda_robotR1: `servo3.write(40); //左前向前旋转50度` and `servo2.write(140);//右后向前旋转50度` → i.e., in that author's build, <90 swings the LEFT-front leg forward and >90 swings the RIGHT-rear forward; equivalently forward = 40 on left legs, 140 on right legs.
- Caveat: this comment is not in the original; it's from a derivative; and the local modified copy dropped these comments. Also the original 360-version (oshwhub page) comment for its own front() was different.

I think that's a good, honest report. Let me also verify whether the local copy has any left90/right90 and check the differences summary (LittleFS vs SPIFFS, AP password 12345678 vs empty, weather key hardcoded, extra endpoints). Let me also produce the count of differing lines and key local additions, and identify the local data/*.html vs original data/*.html differences (local control.html has extra buttons like 回收机器狗 which is not in the original).

Let me check if "回收机器狗" appears in the original control.html (from Gitee). And check the original control.html content.

Also grab the oshwhub project stats (views, author) — the page showed "17.3w" views, created 2024-11-29, updated 2025-11-19, author: course-examples (嘉立创官方账号). Let me extract author info.

Let me do these final checks.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\ncurl -s -m 40 -A \"$ua\" \"https://gitee.com/api/v5/repos/JasonYANG170/eda-robot/contents/data/control.html?ref=main\" -o gt_ctl.json -w \"ctl %{http_code}\\n\"\ncurl -s -m 40 -A \"$ua\" \"https://gitee. …[截断,原长413]` → `ctl 200 eng 200 gitee_control.html OK 6101 gt_eng.json -> [] === 回收机器狗 in original control.html? === 0 no file === local control.html button labels === 前进 | 左转 | 右转 | 后退 | 抬左手 | 抬右手 | 坐下 | 趴下 | 自由模式开 | 自由模式关 | 回收机器狗 | 开心(*^▽^*) | 难受(╥╯^╰╥) | 生气 | 好奇 | 喜欢 | 错误 | 晕 | LOGO | 时间TIME | 天气预报`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:22）

Local gaits are byte-identical to the original. Let me finish verifying the differences and the leg-mapping evidence.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

So `engine.html` does NOT exist in the Gitee original repo — it's a local addition. And "回收机器狗" is not in the original control.html either. Let me confirm: local control.html has 21 buttons, original has fewer. Also local has engine.html (not in original repo). Let me check the original control.html buttons.

Also the local modified copy has "dosleep" command named 'sleep' in control.html → sends 'sleep' over websocket? Let's check how local sends commands. Actually the task is about gait numbers. I have enough.

Let me verify the original control.html button list, and also check the oshwhub attachment "EDA-Robot(180度舵机版)_V1.1.zip" to double-check whether the v1.1 zip contains identical gaits — but I already have Gitee which is the official repo linked from the oshwhub page. That's authoritative.

Let me quickly get the original control.html button list for completeness and check the local engine.html (servo debug page) that isn't in the original.

Also key question 4: servo mounting orientation. The Gitee 180-degree code comments say nothing about mirroring. Let me look at the original's comments in front() — they were stripped? No, in Gitee front() there is `//舵机2旋转至140度` etc. No mirroring comments.

But the interesting evidence: in the 360-degree version (oshwhub description), there were engine offset calibration values: engine1offsetleftpwm = -93, engine1offsetrightpwm = -87, engine2offsetleftpwm = -120, engine2offsetrightpwm = -122, engine3offsetleftpwm = -3, engine3offsetrightpwm = -57, engine4offsetleftpwm = -78, engine4offsetrightpwm = -109. These are per-servo calibration offsets for 360° continuous-rotation servos.

Let me check whether the oshwhub 3D page or hardware page tells the mounting. Let me search the wiki software page for "左前" mapping or for the 360-degree version code (which had the front() with writeMicroseconds).

Actually more importantly for Q4 — the local modified copy's engine.html is a servo debug page. Let me see if it reveals channel-to-leg names (e.g., "左前腿"/"右前腿").

Let me check the local engine.html for servo channel labels.

Also, I should check the oshwhub attachment zip for the 180-degree V1.1 to confirm it matches Gitee. But that requires login probably. I have the official link from oshwhub → Gitee, which is enough.

Let me also do a couple more searches to be thorough (the task asked for 6-10 searches). Let me count what I've done:
1. DDG html (failed - empty)
2. Bing cn "EDA-Robot" 机器狗 (worked but irrelevant)
3. Bing cn EDA-Robot ESP8266 桌面机器狗 舵机
4. GitHub API: 机器狗 esp8266 → FOUND pluckypioneer/eda_robotR1
5. GitHub API: EDA-Robot
6. GitHub API: quadruped esp8266 servo
7. Sogou EDA-Robot (blocked)
8. Sogou 立创开源 机器狗 (blocked)
9. oshwhub search page (empty JS)
10. 360 so.com: EDA-Robot 机器狗 (found oshwhub links)
11. 360: 立创开源 机器狗 esp8266 舵机 U8g2
12. 360: "回收机器狗"
13. CSDN API: EDA-Robot 机器狗
14. CSDN API: 智能机器狗实训营
15. CSDN API: 立创开源 机器狗 舵机 ESP8266
16. 360: hello-hachi 立创 机械狗
17. 360: 立创 EDA-Robot 机器狗 开源
18. Bing site:oshwhub.com 机器狗 ESP8266
19. Bilibili API (blocked, HTML)
20. mojeek/brave/ecosia/marginalia/startpage/searx (mostly blocked)

That's well over 10 distinct searches. Good.

Let me now check local engine.html content and the oshwhub 360 version reference, then also try to find what the local modifications are (since the user wants to compare servo gait numbers — the answer is gaits are identical).

Let me check local engine.html for the servo channel labels which might indicate leg mapping.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== ORIGINAL control.html buttons ===\"\nnode -e \"\nconst fs=require('fs');let s=fs.readFileSync('gitee_control.html','utf8');\nconsole.log([...s.matchAll(/<button[^>]*>([^<]*)<\\/button>/g)].map(m=>m[1].trim()).join(' | '));\n\"\necho; echo \"=== LOCAL engine.html content ===\"\ncat \"/c/Users/UserX/Downloads …[截断,原长412]` → `=== ORIGINAL control.html buttons === ↑ | ← | → | ↓ | 抬左手 | 抬右手 | 坐下 | 趴下 | 自由模式开 | 自由模式关 | 回收 | 开心 | 生气 | 难受 | 好奇 | 喜欢 | 错误 | 晕 | 嘉立创LOGO | 时间 | 天气 === LOCAL engine.html content === <!DOCTYPE html> <html lang="zh"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <ti …[截断,原长1588]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:23）

Let me check the local engine.html (not in original) and the original control.html buttons.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

I have enough. The original control.html has button "回收" while local has "回收机器狗" (a modification). Let me verify the local engine.html is the added new file and check the servo slider labels for angle info. Also verify the servo numbers symmetry question definitively, and note the mounting/orientation info. Let me look at the engine.html servo labels.

Let me also double-check the local engine.html for servo labels and any note about orientation.

</details>

- 🔧 **Bash** `{"command": "grep -n \"servo-label\\|舵机[1-4]\\|data-servo\\|servoId\\|min=\\|max=\\|value=\" \"/c/Users/UserX/Downloads/Robot dog 1.1/data/engine.html\" | head -40", "description": "Inspect local engine.html servo labels"}` → `31: .servo-label { 122: <div class="servo-label">舵机1 (右前腿)</div> 125: <input type="range" min="0" max="180" value="90" class="slider" id="servo1" oninput="updateServo(1, this.value)"> 132: <div class="servo-label">舵机2 (右后腿)</div> 135: <input type="range" min="0" max="180" value="90" class="slider" id="servo2" oninput=" …[截断,原长678]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== ORIGINAL: 360 version availability? check download page attachments ===\"\nnode -e \"\nconst fs=require('fs');let s=fs.readFileSync('wiki_eda-robot-download.html','utf8');\ns=s.replace(/<script[\\s\\S]*?<\\/script>/g,' ').replace(/<[^>]*>/g,' ').replace(/\\s+/g,' ');\nconst i=s.indexOf('附件');\nconsole.log(s …[截断,原长412]` → `=== ORIGINAL: 360 version availability? check download page attachments === 屏幕显示实验 十、ADC输入实验 十一、综合案例实验 天空星-可调电源拓展板 一、项目介绍 二、电路原理 三、电路设计 四、代码介绍 天空星-简易万用表拓展板 一、项目介绍 二、电路原理 三、电路设计 四、代码介绍 天空星-信号发生器拓展板 一、项目介绍 二、电路原理 三、电路设计 四、代码介绍 五、焊接介绍 天空星-物联网拓展板 一、项目介绍 开发板电子秤项目 一、项目介绍 RDA5807调频收音机项目 一、项目介绍 二、电路原理 二、电路设计 四、代码介绍 简易频率计项目 一、项 …[截断,原长2680]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

I have mostly everything. Let me check the local engine.html servo label mapping (right front, right back, left front, left back) — this appears to be a local addition (engine.html doesn't exist in the original Gitee repo). Wait, but the local engine.html has these labels. Let me also check whether the local engine.html labels match the original mapping.

Note: local engine.html says: 舵机1 (右前腿), 舵机2 (右后腿), 舵机3 (左前腿), 舵机4 (左后腿).

Now, in the original comment in front(): servo2.write(140) //舵机2旋转至140度 — no leg names. But GH eda_robotR1's front() has: servo3.write(40); //左前向前旋转50度 — "left front rotates forward". Hmm, that's from the derivative not original. Let me check original gitee_main.cpp for leg-name comments like 左前.

Let me search the original for leg names. Earlier grep on gitee_main.cpp for 左前/右前 etc. returned nothing (only 舵机1/2/3/4 pin comments). Let me confirm and also check the GH eda_robotR1 file which had the "左前向前旋转50度" comment.

Actually earlier I ran grep with those patterns on gitee_main.cpp and results showed lines 34-41 and 487 and 810-813 only. So 左前 comment exists only in orig_main.cpp (GH copy). Let me verify.

Also I should determine mirroring: In front(), original: servo2=140, servo3=40 (same delay step), then servo1=40, servo4=140. So servo2 vs servo3 get 140 vs 40 (complementary), servo1 vs servo4 get 40 vs 140 (complementary). So they are MIRRORED, not the same.

Mapping: servo1=engine1=GPIO14, servo2=GPIO16, servo3=GPIO12, servo4=GPIO13.

Now per local engine.html: servo1=右前腿 (right front), servo2=右后腿 (right back), servo3=左前腿 (left front), servo4=左后腿 (left back).

Hmm wait — but the original comment in front says servo2 (右后 per local labels) = 140 with servo3 (左前) = 40. So diagonal pairing: servo2 (right back) + servo3 (left front) move together = diagonal gait. Yes, front() pairs servo2/servo3 (diagonal) and servo1/servo4 (other diagonal). That's consistent.

Now, regarding which value (<90 or >90) swings a leg forward: In front(), servo3 (left front) = 40 (<90) and servo2 (right back) = 140. In GH eda_robotR1 derivative, comment says "servo3.write(40); //左前向前旋转50度" — left front rotates forward at 40 degrees, and "servo2.write(140);//右后向前旋转50度". So for left front leg (<90 = 40) = forward; for right back (140 = >90) = forward. That indicates opposite servo orientations on left vs right sides — i.e., a mirrored mounting: on the left side forward is <90, on the right side forward is >90 (or vice versa depending which leg). Wait — servo2 is right-back and forward = 140 (>90); servo3 is left-front and forward = 40 (<90). Hmm, but those are front/back pairs, not left/right pairs necessarily. Also servo1 (right front) in that same first step goes to 40 and servo4 (left back) goes to 140.

Hmm — careful. In front() step 1, servo2=140 & servo3=40, then step 2 servo1=40 & servo4=140. If servo1 = right front and servo3 = left front, then front-right gets 40 and front-left gets ... wait servo3=40 too. Hmm, that would be the same. Let me re-check.

Local engine.html labels: servo1=右前腿, servo2=右后腿, servo3=左前腿, servo4=左后腿.

front(): 
- servo2 (右后) = 140
- servo3 (左前) = 40
- then servo1 (右前) = 40
- servo4 (左后) = 140

Hmm, so in the first pair (servo2, servo3): 右后=140, 左前=40. In the second pair (servo1, servo4): 右前=40, 左后=140.

So right legs: 右后=140, 右前=40 → they differ (one is >90, other <90)?? That's odd for a "same direction" gait... Actually no: for a leg to swing forward, the servo angle needed depends on the servo's mounting orientation (which way the horn faces). Front legs and back legs typically are mirrored front-to-back, so "forward" for a front leg might be a different sign than for a back leg. So the numbers are consistent with mirrored mounting front/back AND left/right.

Hmm, so which is it? Let me think about the actual gait: In a standstill "walk", the diagonal pair moves together. Pair A = servo2 & servo3 (右后 + 左前) — that is a diagonal pair (right-back with left-front). ✓ This is a trot diagonal pair. Pair B = servo1 & servo4 (右前 + 左后) — also diagonal. ✓ 

So the pairing of gait is diagonal, which requires left/right mirroring: on the left side, "swing forward" = 140 for a back leg and 40 for... hmm wait, we have servo4 (左后) = 140 in the same step as servo2 (右后) = 140? No: step 1 is servo2=140, servo3=40. step 2 is servo1=40, servo4=140.

Hmm so in step 1 the moving diagonal is {2,3} and step 2 moves {1,4}. In step 1: 右后=140 (forward?), 左前=40 (forward?). In step 2: 右前=40, 左后=140.

For 右前 and 左前 both to swing forward: 右前=40, 左前=40 — same value! And for 右后 and 左后 both forward: 右后=140, 左后=140 — same value. 

So: right-front and left-front use the SAME value for forward (40), and right-back and left-back use the SAME value (140). That means left and right servos are NOT mirrored — they are mounted identically (mirror-symmetric legs driven the same way), and the front/back pairs are the ones that differ (front legs: forward = <90 i.e. 40; back legs: forward = >90 i.e. 140).

Hmm, but wait. That interpretation assumes 40 = forward for both front legs. Let's cross-check with the derivative's comment which said "servo3.write(40); //左前向前旋转50度" (left front rotates forward) and "servo2.write(140);//右后向前旋转50度" (right back rotates forward). servo3 = left front → 40 = forward for left front ✓. servo2 = right back → 140 = forward for right back ✓. Consistent!

And in that derivative (GH eda_robotR1) the mapping is presumably same labels. Hmm, but this comment is from a derivative, not the original; still it's a useful annotation, and it's consistent with the "front legs forward = 40, back legs forward = 140, left and right identical" interpretation.

Wait, but let me double check with left()/right() to be safe. In left(): servo1=80, servo4=80; then servo3=120, servo2=120. Hmm: turning left presumably rotates all legs in the same rotational sense. servo1 (右前) and servo4 (左后) = 80 together; servo3 (左前) and servo2 (右后) = 120 together. So again: servo1 & servo4 get the same value; servo2 & servo3 get the same. Consistent with the diagonal pairing, and left/right identical.

Also sitdown(): servo2 (右后) = 140, servo4 (左后) = 40 — hmm! Here 右后=140 while 左后=40. That's OPPOSITE values for the two back legs! That contradicts "left and right mounted identically"...

Hmm. Wait. sitdown: servo2=140, servo4=40, delay(3000), then both to 90. To sit, both back legs must fold. If both back legs fold the same way, they'd need... hmm, actually folding the back legs means rotating both hind legs so the dog's rear drops. For that, both hind legs rotate in the same physical direction. servo2=140 and servo4=40 are opposite numeric values, so if the servos were mounted identically these would be opposite physical directions. So sitdown() implies left/right back legs are MIRRORED (mounting their horns mirrored), so that +50° and -50° both fold the rear.

Hmm, but that contradicts the front() analysis? Let's re-examine. Hmm, wait — maybe in front(), servo2 and servo4 are diagonal, not left/right. Let me redo the mapping. Which servos are left/right?

Local engine.html (a local, modified project file — actually is engine.html in the original? The Gitee repo has only control.html, index.html, setting.html — no engine.html. So engine.html is a LOCAL ADDITION. Its labels might be the modifier's own interpretation.) Hmm, so I can't fully trust that.

Let me instead reason from the known-360-version file (GH eda_robotR1 is a copy of some version) — it had comments "servo3.write(40); //左前向前旋转50度" and "servo2.write(140);//右后向前旋转50度". So: servo3 = 左前 (left front), servo2 = 右后 (right back). Therefore servo1 = 右前 (right front), servo4 = 左后 (left back). That matches the local engine.html labels. Good, so mapping is: 1=右前, 2=右后, 3=左前, 4=左后.

Now front() step1: servo2 (右后) = 140 forward; servo3 (左前) = 40 forward. So right-back forward = 140; left-front forward = 40.
step2: servo1 (右前) = 40 forward; servo4 (左后) = 140 forward. So right-front forward = 40; left-back forward = 140.

So:
- Front legs: forward = 40 (both right front and left front!). 
- Back legs: forward = 140 (both right back and left back!).

Interesting — front legs and back legs are OPPOSITE numerically, but left and right within the same pair are the SAME numerically. That means: left & right are mounted MIRRORED (mirror-symmetric), and front & back are mounted the SAME (identical orientation), roughly — i.e., there's a mirror across the left-right axis... hmm, wait. Let's think physically.

If left and right legs are mirror images of each other (mirror plane = the vertical fore-aft center plane), then to swing both forward, the servos must rotate in OPPOSITE numerical directions (e.g. left = 40, right = 140), because mirroring reverses the rotation sense. So "left and right both = 40" would mean they are mounted IDENTICALLY (not mirrored) — both rotate the same numerical way, which for identical mounting means both legs swing the same physical way (both forward or both backward).

And front vs back: front legs forward = 40, back legs forward = 140 → front and back legs mounted mirror-wise (mirrored across the left-right... no, across the transverse axis, i.e., back legs are mirror of the front legs). Under a fore-aft mirror, the rotation sense also flips → yes, that's consistent with back legs being mirror-mounted relative to front legs.

OK so the evidence says: left/right = identical mounting (same number = same physical direction), front/back = mirrored mounting (opposite numbers).

Now check sitdown: servo2 (右后) = 140, servo4 (左后) = 40. Both are back legs, which are mounted identically (per above), so 140 and 40 are opposite physical directions... That would mean one hind leg swings one way and the other the opposite way. For "sit", you might want both hind legs to fold forward/backward the same way, which would need the same number if mounted identically. Hmm. Unless sitting is achieved by splaying: e.g., hind legs rotate in opposite directions to lower the body? Hmm, actually for a 4-legged robot with one servo per leg (hip pitch), "sit" = rotate both hind hips forward, dropping the rear. If hind legs are identically mounted, both need the same number. So sitdown's 140/40 seems to contradict.

Hmm, so maybe left/right ARE mirrored: left-side servos mounted mirrored relative to right side. Then: sitdown: 右后=140, 左后=40 → mirrored mounting → both fold the same physical way ✓. And front(): 右后=140, 左后=140 → same number → opposite physical directions ✗ for a walk.

Hmm, contradiction. Unless in front() the two hind legs are supposed to move in opposite directions! Actually — YES. Think about a walking gait: in a "creep/trot" the diagonal pair swings forward while the other diagonal pushes back. But here step 1 = {servo2, servo3} = {右后, 左前} — a diagonal pair. If left/right mirrored and front/back identical... hmm, then 右后=140 and 左前=40 with mirrored left-right mounting: for a mirrored pair (right back vs left front are not mirrored pairs though).

Let's do it rigorously. Define mounting sign per leg: physical direction = sign_i * (angle_i - 90). For a "forward swing", physical direction should be, say, +.

From front():
 step1: servo2 = 140 → +50; servo3 = 40 → -50. Both are in the "swing forward" phase (they're the pair that lifts/moves while the other pair... hmm, actually in a trot, the diagonal pair moves forward together).
 step2: servo1 = 40 → -50; servo4 = 140 → +50. Also "swing forward" phase for the other diagonal.

Hmm, but actually, wait. Look at the structure of front() again:

```
servo2.write(140); servo3.write(40); delay(100);
servo1.write(40);  servo4.write(140); delay(100);
servo2.write(90);  servo3.write(90);  delay(100);
servo1.write(90);  servo4.write(90);  delay(100);
servo1.write(140); servo4.write(40);  delay(100);
servo2.write(40);  servo3.write(140); delay(100);
servo1.write(90);  servo4.write(90);  delay(100);
servo2.write(90);  servo3.write(90);
```

So the pattern per servo over the cycle is: leg A (1,4): 90 → 40 → 90 → 90 → 140 → 90 → 90. leg B (2,3): 90 → 140 → 90 → 90 → 40 → 90.

So each servo alternates: +50 then -50 (relative to 90), i.e., swing one way then the other. Legs 1,4 do 40 then 140; legs 2,3 do 140 then 40. So legs 1&4 (右前 + 左后 = diagonal) do the same phase, legs 2&3 (右后 + 左前 = the other diagonal) do the opposite phase. 

Since the two legs within a diagonal pair (e.g., 右前 and 左后) are left-right mirrored, they need opposite numbers to move in the same physical direction — and indeed they get the SAME number (40 for both 1 and 4). So they move in OPPOSITE physical directions. Hmm, that means the two legs in a diagonal pair move in opposite physical directions. That's... actually consistent with a gait where one diagonally-opposite pair is in "stance/push" while the other is in "swing". No wait, they move simultaneously.

Hmm, hold on. Actually, maybe the intended reading is different: 右前 swinging forward (40) while 左后 pushes backward (40 means for left-back the opposite physical direction = pushing back). And 右后 pushes back (140 → for right back, if right front's forward is 40... ) hmm, we need the mounting signs.

Let's just define: physical_forward_angle_sense for each servo. Let's denote for servo_i whether increasing angle moves the leg forward. We know from the derivative comment: left-front (servo3) rotating to 40 = forward → for servo3, decreasing = forward (40 < 90 = forward). And right-back (servo2) rotating to 140 = forward → for servo2, increasing = forward.

Hmm, but that comment is describing the first step of front() as a "forward" motion. If in the first step both servo2 and servo3 are "forward", then the first step is: right-back leg forward + left-front leg forward = the diagonal pair {右后, 左前} swings forward. That's a diagonal/trot gait. Then step 2: servo1 (右前) = 40 and servo4 (左后) = 140 should also be forward (the other diagonal swings forward). By symmetry, if servo3 (左前) forward = 40 and servo1 (右前) forward = 40, then left-front and right-front have the SAME sign; and servo2 (右后) forward = 140, servo4 (左后) forward = 140 → left-back and right-back have the same sign. So left/right are NOT mirrored (same sign), but front/back are mirrored (opposite sign).

But then sitdown() 右后=140, 左后=40 is inconsistent... unless "sit" isn't folding both hind legs the same way. Hmm — but with one servo per leg and a rear-only "sit" pose: to lower the rear, you'd rotate both hind legs so that the body tilts down at the back. Both hind legs rotate the SAME physical direction (e.g., both "forward" = the hip swings forward, dropping the rear). If left/right hind legs are identically mounted (same sign), you'd write the same number for both — but the code writes 140 and 40. So under my "same sign" conclusion, sitdown() would produce a "splayed" asymmetric pose.

Hmm. Alternatively, my assumption could be wrong and instead: left/right ARE mirrored (so same number = opposite physical direction), and the derivative's comment "左前向前旋转50度" is just a loose comment (the author annotating his own belief) — and front() actually works as: 右后 and 左前 move in OPPOSITE directions (i.e., the diagonal-pair interpretation is wrong; it's more like both left legs then both right legs?).

Hmm, let me look at left() and right() and lie() and dosleep() for further evidence:

left(): 
```
servo1=80, servo4=80  → both -10
servo3=120, servo2=120 → both +30
servo1=40, servo4=40 → -50
servo3=140, servo2=140 → +50
all=90
servo1=100, servo4=100 → +10
servo3=60, servo2=60 → -30
servo1=90, servo4=90
servo3=40, servo2=40 → -50
servo3=90, servo2=90
```
So {1,4} get the same number always, and {2,3} get the same number always, and they're always opposite in sign. So servos 1 and 4 move together in terms of numbers; servos 2 and 3 move together.

right(): {1,4} same, {2,3} same, opposite signed. Same structure but the phase order is swapped between left() and right().

Hmm interesting: left() starts with {1,4} = 80 (−10) then {2,3} = 120 (+30); right() starts with {1,4} = 100 (+10) then {2,3} = 60 (−30). So left and right are literally the mirror in the numeric domain (80↔100, 120↔60, 40↔140, 140↔40, 60↔120, 100↔80). So turning left vs right swaps the roles of the +/− numbers. This is consistent with servos 1,4 being on one "side-role" and 2,3 on another, and turning is done by rotating legs in a coordinated way where the two groups go opposite.

Now the key: the groupings {1,4} and {2,3} are exactly diagonal pairs (右前+左后 and 右后+左前) under the mapping 1=右前, 2=右后, 3=左前, 4=左后. If instead the mapping were 1=左前, 2=左后, 3=右前, 4=右后, the groupings {1,4} and {2,3} would still be diagonal pairs.

So, diagonals pair up and move in the same numeric direction. That means for the diagonal-pair-moves-together gait to be physical, left and right must be mirror-mounted, so same number = opposite physical rotation... no wait. Hmm, for a diagonal pair, e.g. 右前 (front-right) and 左后 (back-left): these two legs are related by a 180° rotation about the vertical axis, NOT by a left-right mirror. Ugh — for a diagonal pair to both swing forward physically, what's required?

Think of a real quadruped trotting: right-front and left-hind legs move in phase (same phase), and left-front/right-hind in antiphase. So in front(), the two "in-phase" sets are {1,4} = {右前, 左后} and {2,3} = {右后, 左前}. ✓ That's exactly the trot diagonal phasing. 

For 右前 and 左后 to swing forward together: 右前's forward and 左后's forward. Since 左后 is the 180°-rotation of 右前 (if all four legs are mirror-symmetric in the standard "left = mirror of right, front = mirror of back" arrangement, then the left-back is the 180° rotation of right-front), the servo numbering: if legs are mounted such that left legs are mirror of right legs (which is how you'd physically build a dog — the legs are mirror images of each other), then 右前 forward and 左后 forward are related by 180° rotation → the servo horn rotation sense: rotating the same physical rotation direction (both swinging forward) requires... 

Let's set coordinates. Right-front leg swinging forward = rotating about the transverse (left-right) axis in, say, the +θ direction (right-hand rule with axis pointing right... whatever). Left-back leg swinging forward = rotating about the same transverse axis in the same +θ direction (both legs swing forward = both rotate the same way about the transverse axis!). Yes — for the 180°-rotated leg pair, "forward" for both = same rotation direction about the transverse axis (because the axis is fixed and the 180° rotation maps a forward swing to a forward swing).

Now, is the servo mounted such that its horn rotation sense about the transverse axis is the same for both? For the left-back leg (a 180° rotated copy of the right-front leg in space, if the whole leg assembly is rotated 180° about the vertical axis): rotating the entire assembly 180° about the vertical axis reverses the rotation sense about the transverse axis as seen in body frame... Hmm, this gets confusing.

Let me just do a concrete model. Coordinates: x = forward, y = left, z = up. Servo axis for a "hip pitch" leg along y (transverse). Leg swings forward when it rotates about +y by angle φ>0? Let's say the leg (a rod pointing down, -z) rotates so its tip moves to +x (forward): rotation about y-axis by ... For a vector (0,0,-1) (down), rotating about +y by angle α gives (x,z) = (-sin α * ... ). Rotation about y by α: x' = x cos α + z sin α; z' = -x sin α + z cos α. With (0,0,-1): x' = -sin α, z' = -cos α. For the tip to move forward (+x), we need sin α < 0 → α < 0. So forward swing = negative rotation about +y. Fine, sign conventions aside.

Now consider the left-back leg, whose hip servo also has its axis along y (parallel). If the servo is the same physical part mounted in the same orientation (rotation axis +y, and its "increasing angle" corresponds to the same rotation sense about +y), then both right-front and left-back would rotate the same way about +y for the same commanded incrementation → both swing forward. So diagonal pairs would both swing forward with the same numeric direction. Which means: left-back and right-front are mounted with the SAME orientation (axes parallel, same sense) — and this is exactly what you get if you build the two legs as identical copies without mirroring. And left-front vs right-front: for a trot, left-front must swing forward when right-front swings backward. If left-front were identically mounted (same sense about +y), it would need the opposite number — which is exactly what we see ({1,4} vs {2,3} group with opposite signs: right-front=40 while left-front=140). So left-front is mounted with the same orientation as right-front, but is commanded the opposite number to swing the same physical way. Hmm — but that's the trot antiphase, so left-front is NOT swinging the same way as right-front at the same time. So this tells us nothing about left-front mounting sign directly!

Hmm. OK let's be careful and use the pairing information: {1,4} = {right-front, left-back} move in numeric lockstep; {2,3} = {right-back, left-front} in numeric lockstep, opposite.

For the gait to be a proper trot, we need {right-front, left-back} to swing together physically (same physical direction at the same time) and {right-back, left-front} to swing together physically, opposite to the first pair. Hmm — that requires: right-front and left-back have the same mounting sign (both increasing = same physical direction), and right-back and left-front have the same mounting sign, opposite to the first pair.

So: sign(右前) = sign(左后) = −sign(右后) = −sign(左前).

Where sign = d(physical swing direction)/d(angle). Under this: right-front and left-front have OPPOSITE signs → left and right are MIRRORED. And right-front vs right-back have opposite signs → front and back are MIRRORED too.

Hmm! That's the "all four legs mirrored" (i.e., each leg's mounting is a mirror image of its neighbor) arrangement, which is the natural way to build a dog from 3D-printed parts: the left legs are mirror copies of the right legs, and the front legs are mirror copies of the back legs. In such an arrangement, each of the four servos has a different sign pattern: signs = [+, −, −, +] for [1,2,3,4] = [右前, 右后, 左前, 左后]... 

Then sitdown: servo2 = 140 (右后), servo4 = 40 (左后). With sign(右后) = −, sign(左后) = + (say), then 140 → physical: −(50) = −50 sense, and 40 → +( −50 ) = −50 sense. Both = −50 physical → SAME physical direction ✓✓. So both hind legs fold the same physical way. That fits "sit" perfectly!

And front() with signs [+,−,−,+]: 
- servo2 (右后) = 140 → physical −(140−90) = −50.
- servo3 (左前) = 40 → physical −(40−90) = +50.
So the {2,3} pair move in OPPOSITE physical directions!? Hmm, that breaks the trot.

Hmm. Ugh. Let me re-derive. There's an ambiguity: which legs are in phase in a trot. Let's think again about whether {1,4} and {2,3} must be the diagonal pairs.

Actually hold on. Are {1,4} = {右前, 左后}? Under 1=右前, 2=右后, 3=左前, 4=左后: 1 and 4 = right-front and left-back = diagonal ✓. 2 and 3 = right-back and left-front = the other diagonal ✓. So yes, {1,4} and {2,3} are the two diagonals. Good.

In a trot, the diagonal pairs move in phase, so {1,4} together physically, {2,3} together physically, and the two pairs antiphase. In the code, {1,4} get the same NUMBER and {2,3} get the opposite NUMBER. So for the physical motion to be a trot, we need: sign(1) = sign(4) and sign(2) = sign(3) = −sign(1). So [sign1, sign2, sign3, sign4] = [+,−,−,+] or [−,+,+,−].

Under [+,−,−,+] = [右前 +, 右后 −, 左前 −, 左后 +]: 
- right-front vs right-back: opposite → front/back mirrored ✓ (natural).
- right-front vs left-front: opposite → left/right mirrored ✓ (natural).
- right-back vs left-back: opposite → left/right mirrored ✓.
So all four legs are mirrored relative to their neighbors — i.e., the classic mirrored mounting. 

Now check sitdown with signs [+,−,−,+]: 右后 = 140 → physical −(50): call that "direction D". 左后 = 40 → physical +(40−90) = −50 → also direction D ✓ (same physical direction). Both hind legs fold the same way ✓✓. Consistent!

Now check front() first step: 右后 (sign −) = 140 → physical −50 (D). 左前 (sign −) = 40 → physical +50 (opposite of D). Hmm! Both in the "same phase" pair {2,3} but opposite physical directions?! That can't be a trot...

Hmm wait, no! I made an error: for {2,3} to be physically in phase, we need sign(2) = sign(3) — and in my sign assignment both are −, and they get the same NUMBER... 

Oh wait, no! Look at front(): step 1 has servo2 = 140 AND servo3 = 40. They do NOT get the same number! Let me recheck: `servo2.write(140); servo3.write(40); delay(100);` — 140 and 40, different! And step 2: `servo1.write(40); servo4.write(140);` — also different!

I earlier mis-stated. Let me redo: the pairs that get the SAME number in front() are... step 1: {2,3} get {140, 40} — different. Step 2: {1,4} get {40,140} — different. Later: `servo1.write(140); servo4.write(40);` different. `servo2.write(40); servo3.write(140);` different.

So in front(), within the diagonal pair {1,4}: servo1 = 40 while servo4 = 140 — DIFFERENT. And within {2,3}: servo2 = 140, servo3 = 40 — DIFFERENT. So within each diagonal pair, the numbers are opposite. Under mirrored mounting (sign flips between left and right / front and back, per [+,−,−,+]), opposite numbers = same physical direction ✓. 

Let me verify: sign1=+, sign2=−, sign3=−, sign4=+. front() step 2: servo1 = 40 → physical +(40−90) = −50; servo4 = 140 → physical +(140−90) = +50?? Wait sign4 = +, so servo4 = 140 → physical +50. Hmm, that's opposite to servo1's −50, but they should be in phase (same physical direction) since they're a diagonal pair moving together.

Hmm, I think I need to be more careful: in a diagonal pair that swings forward together, the two legs both swing FORWARD = same physical direction. So {1,4} get {40, 140} and must both be the same physical direction → sign1 * (40−90) = sign4 * (140−90) → sign1 * (−50) = sign4 * (+50) → sign1 = −sign4. So sign1 and sign4 are OPPOSITE. And {2,3} get {140,40} both same physical: sign2*(140−90) = sign3*(40−90) → sign2 = −sign3. So sign2 = −sign3.

And the two pairs are antiphase: sign1*(−50) = −[sign2*(+50)] → sign1 = sign2.

So: sign1 = sign2, sign3 = −sign2, sign4 = −sign1 = −sign2. So signs = [+, +, −, −] for [1,2,3,4] = [右前, 右后, 左前, 左后].

Interesting! So: 右前 and 右后 have the SAME sign; 左前 and 左后 have the same sign, opposite to the right side. So LEFT and RIGHT are MIRRORED (opposite signs), and FRONT and BACK are IDENTICAL (same sign). 

Hmm, that's the opposite conclusion from before. Hmm, but wait: is it physically sensible? A quadruped built with left legs = mirror of right legs (very common), and front legs = same (not mirrored) as back legs (e.g., all four legs are identical parts mounted the same way, with left/right handled by mirroring the part). Then the servo sign for the left legs is opposite to the right legs' (mirroring the leg flips the rotation sense about the transverse axis... hmm, does it? Mirroring across the fore-aft vertical plane maps the transverse axis direction to its negative → yes, the rotation sense flips). And front vs back legs identical (not mirrored) keeps the same sign (they're translations of one another, no reflection). ✓ Physically consistent.

Now check sitdown with signs [+,+,−,−]: servo2 (右后, sign +) = 140 → physical +(50); servo4 (左后, sign −) = 40 → physical −(40−90) = +50. SAME ✓. Both hind legs fold the same way ✓✓. 

And check lie() and dosleep() and toplefthand/toprighthand:
- lie(): servo1 = 180, servo3 = 0, servo2 = 0, servo4 = 180. With signs [+,+,−,−]: servo1 → +(90); servo2 → −(0−90) = +90; servo3 → −(0−90) = +90; servo4 → +(90). ALL FOUR = +90 → all four legs rotate the same physical direction by 90° ✓ — that's exactly "lie down" (all legs splayed flat). Consistent!! 

- dosleep(): servo1 = 0, servo3 = 180, servo2 = 180, servo4 = 0. Signs: servo1 → −90; servo2 → +90... hmm: sign2 = + → +(180−90) = +90. servo3 (sign −) → −(180−90) = −90. servo4 (sign −) → −(0−90) = +90. So servo1 = −90, servo2 = +90, servo3 = −90, servo4 = +90. So right-front and left-front at −90, right-back and left-back at +90 — the opposite of lie()'s +90 (all four +90). Hmm, so dosleep() = the reverse of lie() for front legs and same... hmm: in lie() all four = +90. In dosleep: front legs = −90, back legs = +90. So dosleep is NOT the mirror of lie — it puts front legs at 0° and back legs at 180°. Right: servo1 = 0 (front right at 0 = −90 physical), servo3 = 180 (front left at 180 = −90 physical: sign3=− → −(180−90) = −90 ✓). servo2 = 180 (back right at 180 = +90), servo4 = 0 (back left at 0 = +90). So front legs at −90 and back legs at +90 → all four legs rot...

Hmm, in lie(): front-right = 180 → +90 (sign1=+); front-left = 0 → −(0−90) = +90 ✓; back-right = 0 → +(0−90) = −90?? Wait I need to recompute. sign2 = +: servo2 = 0 → physical = sign2*(0−90) = −90. Hmm! Earlier I said servo2 = 0 → −(0−90) = +90 using sign2 = −. Let me redo carefully with signs = [+, +, −, −] (sign1=+, sign2=+, sign3=−, sign4=−):

lie(): servo1=180 → +1*(180−90) = +90. servo2=0 → +1*(0−90) = −90. servo3=0 → −1*(0−90) = +90. servo4=180 → −1*(180−90) = −90.
So right-front=+90, right-back=−90, left-front=+90, left-back=−90. Hmm! So front legs both +90, back legs both −90. That means front legs swing one way and back legs swing the other way. Hmm, is that "lie down"? If front legs rotate +90 and back legs −90, then... front legs go flat forward and back legs go flat backward → the body drops flat = "lie". YES, that's plausible! (Belly on the floor, front legs splayed forward, back legs splayed backward — the classic "sphinx/flat" pose.) ✓ Consistent.

dosleep(): servo1 = 0 → −90; servo3 = 180 → −90 (front legs both −90: splayed backward); servo2 = 180 → +90; servo4 = 0 → +90 (back legs both +90: splayed forward). So dosleep = the mirror of lie (front and back swapped) ✓ Both are plausible "flat" poses; and indeed the original had dosleep and lie as separate functions (and the local modified copy's control.html sends 'sleep'). Hmm, in the original both exist. Fine.

This sign model is fully self-consistent: signs = [+, +, −, −] i.e. right side one sign, left side the other; front/back identical. Wait, but hold on: is [+,+,−,−] the only solution? The equations were sign1 = sign2, sign2 = −sign3, sign3 = −sign4. That gives [+,+,−,−] or the global negation [−,−,+,+] (which is the same arrangement up to a global convention). So yes — up to global sign, LEFT and RIGHT legs are mirrored, FRONT and BACK identical.

But hmm, this conclusion assumed the gait is a trot (diagonal pairs in phase, antiphase between diagonals), which the code structure strongly implies (pairs {1,4} and {2,3} = diagonals). But there's an alternative: the two diagonal pairs could BOTH be in "swing" phase simultaneously in a different manner... no. Actually, there's another possibility: front() is not a trot but a "diagonal pair lands while the other lifts" sequence. Whatever the exact gait, the phase relations I derived hold: within a diagonal pair, the two legs move in the same physical direction (that's what "the pair moving together" means) and the other pair moves oppositely. Actually hmm, must the second pair move oppositely? In a trot yes. In a "bound" or "walk" it could differ. But the code clearly alternates the two groups ({1,4} at 40 then the other at 140 etc.), which is the trot pattern.

Hmm, but hold on, actually there's yet another subtlety: maybe within front(), the two diagonal pairs are in the SAME physical phase, i.e. all four legs swing forward/backward together (a "hop"/"pronk" gait) rather than a trot. Then the equations would be: within {1,4} same physical (sign1 = −sign4), within {2,3} same physical (sign2 = −sign3), AND the two pairs same physical direction: sign1*(40−90) = sign2*(140−90) → sign1 = −sign2. That would give [+,−,−,+] — the mirrored-everywhere model. Hmm! So the two candidate sign models correspond to different gaits (trot vs pronk/bound).

Which is it? A "bound" (both front legs together, both back legs together) would be the natural quadruped gait to implement with diagonal... no: in a bound, {front legs} move together and {back legs} together. Here the pairs are diagonal {1,4} = {右前,左后} — NOT front/back together. Hmm, so for a bound, the code would have grouped {1,3} (both front) and {2,4} (both back). It doesn't; it groups {1,4} and {2,3} = diagonals. So the grouping is diagonal → trot: the diagonals are antiphase (that's what "diagonal gait" means: opposite legs in phase with each other, and the two diagonals in antiphase). 

Hmm, but wait: is that right? In a trot, right-fore + left-hind move together (in phase), left-fore + right-hind in phase, and the two pairs antiphase. Here {1,4} = {右前, 左后} ✓ and {2,3} = {右后, 左前} ✓. Yes, that's the trot. And in a trot the two pairs are antiphase ✓ (code: they alternate).

So my derivation stands: signs = [+,+,−,−] → left/right MIRRORED, front/back IDENTICAL. Hmm, but this contradicts the "comment" in the derivative (GH eda_robotR1) which said "左前向前旋转50度" for servo3=40 in the same step as "右后向前旋转50度" for servo2=140. Under my model, servo3=40 (left-front, sign −) = +50 physical = same as servo2=140 (right-back, sign +) = +50 physical ✓✓ — CONSISTENT! Both swing "+50 physical". And under the other model ([+,−,−,+] for a bound), servo3=40 and servo2=140 would also be the same physical direction. Hmm, so that comment doesn't discriminate. Right — because it only tells us about the {2,3} pair.

Hmm, so what discriminates the trot vs bound? Both models make the {2,3} pair and {1,4} pair internally consistent; the difference is whether the two pairs are in phase or antiphase, which we can't determine from the numbers alone (a "phase" is not observable from a single leg's angle). Hmm — but actually the ORDER of the code tells us: in front(), the sequence is: move {2,3} to ±50, then move {1,4} to ∓50, then return both to 90, then move {1,4} to ±50 (the opposite sign), then {2,3} to the opposite sign, then return. Hmm, in a trot you'd expect: pair A forward while pair B backward (simultaneously), then swap. In the code, they're sequenced one after another with 100ms delays — it's a "static" gait where the robot moves legs one group at a time (like move diagonal A forward, then diagonal B forward... ). Hmm, hmm.

Let's read the code as a literal time sequence, interpreting each write as "put leg at this angle":
t0: {2,3} = (140, 40)  [right-back +50 physical, left-front +50 physical] → both at "+50"
t1: {1,4} = (40, 140)  [right-front −50 physical, left-back −50 physical] → both at "−50"
t2: {2,3} → 90 (neutral), t3: {1,4} → 90 (neutral)
t4: {1,4} = (140, 40) → right-front +50, left-back +50 → both "+50"
t5: {2,3} = (40, 140) → right-back −50, left-front −50 → both "−50"
t6: {1,4} → 90, t7: {2,3} → 90.

So over the cycle, all four legs each go +50 then −50 (or −50 then +50): legs 1,4 do −50 first then +50; legs 2,3 do +50 first then −50. So all four legs undergo the same physical stroke sequence, just phase-shifted: the diagonal pairs alternate in antiphase. In real walking terms: this is a "one leg at a time in diagonal pairs" sequence. Whether the physical stroke is "forward then backward" for all legs — YES, since each leg does +50 then −50 in physical terms (sign-corrected), each leg rotates one way then the other, and the gait advances if the returning motion is... hmm, actually a walking gait needs the leg to (a) lift and swing forward and (b) push back while on the ground. With a single servo per leg (just hip pitch), you can't do a proper walk; the "gait" here just splays the legs forward/back alternately, which produces a shuffling crawl forward. Typical of these toy dogs. Fine — the exact locomotion physics is not the point.

KEY POINT for the user's question #3: In front() and back(), left-side and right-side legs receive MIRRORED/COMPLEMENTARY numbers, NOT the same. E.g., front(): right-front (servo1) = 40 while left-front (servo3) = 40... hmm wait. Hmm! Let me look again very concretely with the leg mapping:

front():
 servo2 = 140 (右后 / right-back)
 servo3 = 40  (左前 / left-front)
 then servo1 = 40 (右前 / right-front)
 then servo4 = 140 (左后 / left-back)

So right-back = 140, right-front = 40; left-front = 40, left-back = 140. So LEFT and RIGHT within the same longitudinal pair: right-front = 40 and left-front = 40 → THE SAME. Right-back = 140 and left-back = 140 → THE SAME. So in front(), the left and right legs receive the SAME numbers; the front and back legs receive MIRRORED (complementary) numbers!

Hold on. That's a cleaner statement of the raw facts: within front(), servo1 = servo3 = 40 (same step? no — servo3 at t0 and servo1 at t1, so slightly staggered but the same value), and servo2 = servo4 = 140. So yes, left-right same value; front-back complementary.

Hmm hmm. But my sign-derivation said left/right are mirrored (opposite signs) and front/back identical. Then left-right getting the SAME number would mean left and right legs swing in OPPOSITE physical directions — which is the antiphase of... no: the two front legs (right-front and left-front) are in the same diagonal phase? No! Right-front ∈ {1,4} diagonal, left-front ∈ {2,3} diagonal. So right-front and left-front are in ANTIPHASE (in a trot) — they SHOULD move in opposite physical directions at any given time! And with mirrored mounting (opposite signs), the SAME number gives OPPOSITE physical directions ✓✓. So "left and right get the same number" is exactly what a trot requires with mirrored left/right mounting!

And front vs back: right-front (servo1) and right-back (servo2): servo1 = 40, servo2 = 140 → complementary ✓, and with front/back identical mounting (same sign), complementary numbers give opposite physical directions — which is again correct for a trot, since right-front and right-back are in antiphase too (right-front ∈ pair A, right-back ∈ pair B).

So everything is consistent with: diagonal pairs antiphase; left/right mirrored mounting; front/back identical mounting. And in terms of raw numbers: left↔right same values, front↔back complementary values.

Now, one more check with the user's specific observation: the user asked "whether in the original, the left-side and right-side legs receive the SAME servo numbers or MIRRORED/complementary numbers (e.g., 40 vs 140) in front()/back()". Based on the original code: SAME. E.g., front(): servo1 (right-front) = 40 and servo3 (left-front) = 40; servo2 (right-back) = 140 and servo4 (left-back) = 140. So left and right receive the SAME numbers; the COMPLEMENTARY (40 vs 140) relation appears between front and back legs (and between the two diagonals).

Hmm, but wait. I should double check the leg mapping, because everything hinges on it. Evidence:
1. GH derivative eda_robotR1 comments: "servo3.write(40); //左前向前旋转50度" and "servo2.write(140);//右后向前旋转50度". So servo3 = 左前 (left-front), servo2 = 右后 (right-back). Hmm — but that derivative is NOT the original; it's a modified copy by another person who may have re-labeled. Let me double check by looking at the 360-degree version text on oshwhub (the published original 360 code shown on the oshwhub page). In the oshwhub page's front() (360 version), there were no leg-name comments. Hmm.

2. Local engine.html (added by the modifier): 舵机1 (右前腿), 舵机2 (右后腿), 舵机3 (左前腿), 舵机4 (左后腿). Same mapping: 1=right-front, 2=right-back, 3=left-front, 4=left-back. Two independent sources agree. 

Let me try to find the original's own statement of the mapping. The oshwhub page text I extracted didn't include a leg-name mapping for servos. But maybe the original 360-degree code comments in the version published as a release attachment had them? Or maybe the wiki software page shows the front() code with comments. Let me check the wiki software page for front() code and any leg names. Also, the derivative's comment might have been inherited from an earlier original version (the 360 version) — let me check: does the oshwhub page's front() show comments? From the extracted text: "void front() { //+30C 2/3 servo2.writeMicroseconds(1500 + speed + engine2offsetleftpwm);" — no leg names, just "+30C 2/3" annotations. Hmm, "2/3" is servo2/servo3. So the original 360 code didn't name legs in those comments. So the leg names in the GH derivative presumably came from that modifier's own hardware. Hmm, or from the original's other files (maybe the original's engine.html? The original Gitee repo has no engine.html; but the 360 version attachments might have had an engine.html with labels!).

Let me check the local engine.html more fully — it's likely from the original 360-version package (the local project is a modified copy of something with engine.html). Actually the local project has engine.html and a /engine route with LittleFS. The Gitee original has no engine.html and uses SPIFFS. So the local project is derived from a version that has engine.html — perhaps the 360-degree version (EDA-Robot(360度舵机版).zip) which may have used LittleFS and engine.html! Interesting. Hmm, so the local project might be a modified copy of the 360 version rather than the 180 version.

Hmm, but the local gaits are byte-identical to the 180 version's gaits (the user's servo numbers match exactly). And the local has "回收机器狗" instead of "回收" — a local change. So the local copy is a modification of the 180 version (the Gitee repo) most likely, with engine.html added by the modifier (or taken from the 360 version). Either way, the local leg labels in engine.html align with the derivative's comments.

Let me try to see if there's an original statement about mounting. Let me check the local engine.html's JS to see if it maps servo index → pin, and check the original 360 version code if accessible. I could look at the CSDN articles — they sometimes quote the original code with comments. Also the derivative's main.cpp may have inherited comments from an earlier original state (e.g., "左前向前旋转50度" might come from the original's earlier version). Let me check git history of the GH derivative? It has only a few commits.

Also: I can look for the 360-degree version source (EDA-Robot(360度舵机版).zip) — attachment on oshwhub; probably requires login. Alternatively CSDN articles quoting the 360 code. Let me check the oshwhub page for the 360 code's comments on leg names, e.g. "左前" in the page. Let me grep the raw oshwhub html for 左前/右前/etc.

Let me also verify: does the original oshwhub page text contain "左前"? Let me grep.

Additionally, I should note the "1.2: 程序新增支持180度舵机版本" version history, and that the Gitee repo is the 180 version V1.1.

Let me also grab the original platformio.ini, which I have (uses SPIFFS-based project, FS.h, ottowinter/ESPAsyncWebServer-esphome). Local uses LittleFS (18 occurrences) vs original SPIFFS. Confirms modification.

Let me do these checks now: grep 左前 in ow_botdog.html raw, and check the local project's docs/attachments, and check the CSDN article that describes the original servo mapping ("立创EDA开源项目：基于ESP8266与SG90舵机的智能机器狗（4497595A）硬件设计与组装全攻略" or "从零复刻嘉立创EDA开源ESP8266机器狗").

Let me also record the searches performed so far for the report:
1. Bing CN: "EDA-Robot" 机器狗 (no relevant)
2. Bing CN: EDA-Robot ESP8266 桌面机器狗 舵机 (no)
3. Bing CN: site:oshwhub.com 机器狗 ESP8266 (irrelevant)
4. Bing CN: 立创 EDA-Robot 机器狗 ESP8266 (irrelevant)
5. GitHub API: repositories q=EDA-Robot → found pluckypioneer/eda_robotR1
6. GitHub API: q=机器狗 esp8266 → found MindPaw etc.
7. GitHub API: q=quadruped esp8266 servo
8. CSDN search API: EDA-Robot 机器狗 → found articles
9. CSDN search API: 智能机器狗实训营
10. CSDN search API: 立创开源 机器狗 舵机 ESP8266 → found 立创 ESP8266 机器狗复刻指南 (Maxwell), 4497595A, etc.
11. 360 search: "EDA-Robot" 机器狗 ESP8266 → found oshwhub links (复刻嘉立创EDA-ESP8266机器狗 ly1919, 智能机器小狗 wwwsss1234, 阳阳的机器狗 14402a)
12. 360 search: 立创开源 机器狗 esp8266 舵机 U8g2
13. 360 search: "回收机器狗"
14. 360 search: hello-hachi 立创 机械狗
15. 360 search: 立创 EDA-Robot 机器狗 开源 → found course-examples/bot-dog and course-examples/eda-robotpro
16. DuckDuckGo lite (blocked), Google (blocked), Baidu (captcha), Sogou (captcha), Mojeek (403), Brave/Ecosia/Startpage/searx (blocked), grep.app (429), searchcode (404), Gitee search API (empty)
17. Bilibili search API (returned HTML not JSON — hmm, it returned 5464 bytes of HTML; failed)
18. oshwhub API variants (404)
19. Gitee API: repos/JasonYANG170/eda-robot → the code repo

That's well over 6-10 distinct searches. Good.

Let me now do a few more targeted things:
- grep 左前/右前 in the raw oshwhub bot-dog page (to see if the original page names legs).
- Fetch the local engine.html fully to see the servo→GPIO mapping and any orientation notes.
- Check the local project's README/attachments (none).
- Maybe check the derivative MindPaw/others? Not needed.
- Check whether the original 360 version code is visible somewhere (e.g., CSDN article "从零复刻嘉立创EDA开源ESP8266机器狗" might quote a different gait with leg comments).

The user's core need: compare servo gait numbers with a modified copy. I have the original gait numbers verbatim and confirmed the local copy's gaits are byte-identical (so the "modified copy" only changed non-gait things: LittleFS vs SPIFFS, AP password, weather key default, added engine.html/route, 'sleep' command, '回收机器狗' label, etc.). That's a very useful finding.

Wait — but hold on: the local copy's toplefthand/toprighthand match the 180-version original (0→30→90 and 180→150→90) but the GH derivative differs. And the local's lie() matches the original 180 version. So the local copy came from the original 180 version. But hmm, the local has engine.html + LittleFS. Let me verify whether the 360 version used LittleFS: the local's .gitignore, platformio.ini use LittleFS, and local main.cpp includes LittleFS.h and has "engine1offset..." endpoints? No — local has 0 occurrences of "offset". The original 180 version has no offsets either (offsets are only in the 360 version shown on the oshwhub page). So the local project = 180 version (no offsets) + LittleFS + engine.html + AP password + default weather key.

Hmm, interesting: the original 180 Gitee version uses SPIFFS while the local uses LittleFS. Someone modernized it. Also the original's ssid = "EDA-Robot", password = "" (no password) — the local sets password "12345678". And the original has no default weather key; local adds "SB3j4zrxZ7nuRXv8v". OK.

Let me quickly check the local main.cpp for /engine routes and the 'sleep' command mapping to dosleep, and the weather API differences (now.json vs daily.json), to describe the modifications accurately but briefly. Actually the report should focus on the original + gait comparison + the 4 specific questions. I'll keep modifications brief.

One more important check for question #4: "which value (<90 or >90) swings a leg forward". From the original code alone, we can state: for the front legs (servo1 = right-front, servo3 = left-front) the "forward stroke" number is 40 (<90) in front(); for the back legs (servo2 = right-back, servo4 = left-back) it is 140 (>90). Wait, careful — in front(), which is the forward stroke: the sequence has each leg going to 40 then 140 at different times. In a forward-walking gait, hmm, both are used. The question "which value swings a leg forward" — the derivative comment says 左前 40 = 向前 (forward) and 右后 140 = 向前. Hmm, that derivative's comment refers to the first step of front() as the forward-swing phase. So: front legs forward = 40 (<90); back legs forward = 140 (>90). Hmm, but is the first step the swing phase or the stance phase? For a forward motion, hmm.

Actually, the user's real intent (they're comparing gait numbers between the original and a modified copy) is likely to understand whether a leg swinging forward uses <90 or >90. I'll report: In the original front(), the first half (servo2=140 + servo3=40, then servo1=40 + servo4=140) is annotated in a downstream public fork (pluckypioneer/eda_robotR1) as "向前旋转" (rotating forward): 左前(servo3)=40 and 右后(servo2)=140. So for the left-front leg, <90 (40) is forward; for the right-back leg, >90 (140) is forward. This implies opposite physical mounting sense between the two servos in a diagonal pair... hmm, which is consistent with mirrored left/right mounting + identical front/back mounting (my model): under signs [+,+,−,−]: servo3 (left-front, sign −) = 40 → +50 physical; servo2 (right-back, sign +) = 140 → +50 physical ✓ same physical phase.

I should be careful to present raw facts and mark interpretations as uncertain. Also note: the local modified copy's engine.html labels servo1 as 右前腿 etc. — but that's a modifier-added file; and pluckypioneer's fork has the same mapping in comments. Both are derivatives, so the leg mapping is "very likely but not stated in the original code itself".

Hmm, let me try harder to find the original's own leg-naming. Ideas:
- The 360-degree version's oshwhub page text: search for 左前 in ow_botdog.html.
- The wiki software page: search for 左前/右前 (I did search for 左前 in w2_eda-robot-software.html — the earlier loop printed only matches for 舵机1..4, 90度, 0度, 180度; no 左前/右前 hits, meaning those strings aren't in the software page).
- Maybe the original's engine.html (in the 360 version zip) has labels like 舵机1(右前腿) — the local copy's engine.html could literally be that file, unmodified, from the original 360 attachment! If so, the labels ARE original (from the 360 version package). Hmm, I can't verify without the zip. The 360 version is "已不再维护" (no longer maintained) and the zip is an attachment on oshwhub (may need login). Let me try to find the 360-version source elsewhere, e.g., in another fork on GitHub/Gitee, or the CSDN article.

Let me search GitHub API for forks/copies: q="EDA-Robot" or "eda-robot" + servo, or code search for "回收机器狗"... GitHub code search API requires auth. Hmm, but I can search repositories by name: q=eda-robot, q=robot-dog esp8266 littlefs.

Also try searching for the 360 version's distinctive strings: "engine1offsetleftpwm" (from the oshwhub 360 code) — via GitHub code search API (needs auth; unauthenticated code search is not allowed). Let me try anyway; and also try grep.app again (429 earlier, maybe retry), and searchcode with proper URL.

Let me also try Gitee's search API for "机器狗" repos (it returned empty array earlier: "200 2" = "[]"). Maybe search with different terms or the Gitee search page.

Actually, for the report it's probably enough. But let me make a couple more attempts to (a) find the 360 version source with leg labels, and (b) confirm that engine.html exists in the original 360 package. Let me try the CSDN article "从零复刻嘉立创EDA开源ESP8266机器狗：硬件设计、软件编程与结构组装全流程解析" (weixin_36123300/158948448) and the 4497595A article via 360's cached text or CSDN's API. Actually CSDN blocked direct fetch (404/521). Hmm, the so.csdn.net API gave titles, and the 360 search snippet gave partial text. Let me try fetching CSDN via a different UA or the m. version? Or use the "ai.so.com" summary? Let me try fetching the CSDN article via r.jina.ai? That's an external service; might not be allowed/blocked. Let me just try one: https://r.jina.ai/https://blog.csdn.net/... Hmm, it's a public reader proxy. It might work. But it may also be considered fine to use. Let me try.

Also for the 360 version, the "EDA-Robot(360度舵机版).zip" attachment link might be visible on the oshwhub page (attachment links). Let me grep for attachment URLs in ow_botdog.html — earlier I saw an odd "https://pbt-" truncated link. Let me look for the attachments API: oshwhub has /api/project/{uuid}/attachment or similar. Let me grep the raw html for "attachment" and for the pdf link (image.lceda.cn/...pdf) — found the offline doc PDF: https://image.lceda.cn/easyedaResource/images/90df0661fc474cfd82e2d9b4c6448a27.pdf. That's the EDA-Robot项目电子实训文档.pdf! Let me download and search it for leg names and the servo code (the 180 version doc). That could contain the original leg mapping and possibly the code with leg comments. 

Let me do that — it's a strong primary source.

Plan:
1. Download the PDF, extract text (pdftotext? Might not be installed. Use node? Hmm. Maybe use Python? No python in bash PATH; per memory, conda python full path. Let me check ~/.zcode/memory/python-envs.md? That's the AGENTS.md index. Simpler: try `pwsh` with python full path from the memory file. Let me read the memory file quickly.)
2. grep for 左前/右前/舵机1 in the PDF text.

Let me also grep the oshwhub raw page for 左前/右前 first (cheap).

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== leg-name terms in raw oshwhub bot-dog page ===\"\nfor k in 左前 右前 左后 右后 前腿 后腿 镜像 反向 安装方向; do printf \"%s: %s\\n\" \"$k\" \"$(grep -o \"$k\" ow_botdog.html | wc -l)\"; done\necho \"=== attachments/pdf links ===\"\ngrep -oE 'https://[^\"]*\\.(pdf|zip|xlsx|mp4)' ow_botdog.html | sort -u | head -20", "descriptio …[截断,原长412]` → `=== leg-name terms in raw oshwhub bot-dog page === 左前: 0 右前: 0 左后: 0 右后: 0 前腿: 0 后腿: 0 镜像: 0 反向: 0 安装方向: 0 === attachments/pdf links === https://image.lceda.cn/easyedaResource/images/90df0661fc474cfd82e2d9b4c6448a27.pdf https://image.lceda.cn/oshwhub/project/attachments/1cbae5b1f7ed4f9d9209d771c856396a.zip https://imag …[截断,原长1023]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\ncurl -sL -m 60 -A \"$ua\" \"https://image.lceda.cn/easyedaResource/images/90df0661fc474cfd82e2d9b4c6448a27.pdf\" -o eda_robot_doc.pdf -w \"pdf %{http_code} %{size_download} %{content_type}\\n\"\nls -la e …[截断,原长412]` → `pdf 200 509304 application/pdf -rw-r--r-- 1 user 197121 509304 Oct 9 00:26 eda_robot_doc.pdf 0000000 % P D F - 1 . 7 \n % 241 263 305 327 \n 1 0000020 0 o`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:24）

Let me check the raw oshwhub page for leg-mapping terms and try to download the official PDF doc.

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\ncat > pdftxt.js <<'EOF'\nconst {execSync}=require('child_process');\nEOF\nls \"C:/Users/UserX/miniconda3/envs/opencv/python.exe\" 2>/dev/null; ls \"C:/ultralytics-main/.venv/Scripts/python.exe\" 2>/dev/null\nwhere soffice.com 2>/dev/null; ls /c/Program\\ Files/LibreOffice/program/soffice.com 2>/dev/null", "description …[截断,原长412]` → `C:/ultralytics-main/.venv/Scripts/python.exe* /c/Program Files/LibreOffice/program/soffice.com*`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\n# software source zip (3.5MB likely) - find the largest attachment\nfor f in 1cbae5b1f7ed4f9d9209d771c856396a 1f105ddb15984777b02b3d6a41b089f5 2686655fc5e54288b6389d81cb3d9545 3d5e14de313647bcbc6fd047787 …[截断,原长412]` → `1cbae5b1f7ed4f9d9209d771c856396a Content-Length: 33947718 1f105ddb15984777b02b3d6a41b089f5 Content-Length: 33958851 2686655fc5e54288b6389d81cb3d9545 Content-Length: 35138116 3d5e14de313647bcbc6fd047787b4c71 Content-Length: 133471671 79ea8924fab54c65a5060b3d5df74900 Content-Length: 12758243`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:26）

Let me check the official documentation zip for leg-mapping and servo orientation details.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Let me update the todo list and try to find the small software source zip (12.7MB is likely the 180-degree V1.1 or software source). Let me download the 12.7MB one and check. Also, let me check the "软件源码.zip" which was mentioned. Actually let me first check the file names associated with each attachment.

Actually, the key deliverable is done: I found the original project and verified the gaits are identical. Let me do a couple more searches to be thorough (the task asked for 6-10 distinct searches), and verify the servo mounting orientation question. The mount orientation isn't documented explicitly, but let me check the 3D enclosure or the attachment zip for hints. Let me grab the software source zip (12.7MB) which might contain the 180-degree V1.0/V1.1 with comments about leg placement.

Let me also check the wiki software page for the front() code to compare with Gitee.

Let me be efficient: download the 12.7MB zip, list contents, look for any doc about servo orientation.

Also I should count my searches so far:
1. DuckDuckGo html "EDA-Robot" 机器狗 (failed)
2. Bing CN "EDA-Robot" 机器狗 (no relevant)
3. Bing CN EDA-Robot ESP8266 桌面机器狗 舵机 (failed parse)
4. Sogou EDA-Robot 机器狗 (302/blocked)
5. GitHub API: 机器狗 esp8266 → found pluckypioneer/eda_robotR1
6. GitHub API: EDA-Robot → same
7. GitHub API: quadruped esp8266 servo
8. oshwhub search page
9. Gitee API: 机器狗 esp8266
10. Bilibili API (blocked, HTML)
11. CSDN API: EDA-Robot 机器狗 → found articles
12. CSDN API: 智能机器狗实训营
13. CSDN API: 立创开源 机器狗 舵机 ESP8266
14. 360 so.com: "EDA-Robot" 机器狗 ESP8266 → oshwhub links
15. 360 so.com: 立创开源 机器狗 esp8266 舵机 U8g2 → hello-hachi
16. 360 so.com: "回收机器狗"
17. 360 so.com: hello-hachi 立创 机械狗
18. 360 so.com: 立创 EDA-Robot 机器狗 开源 → course-examples/bot-dog
19. Bing site:oshwhub.com 机器狗 ESP8266
20. Mojeek, Brave, Ecosia, Marginalia, Startpage, searx (all failed)
21. grep.app (429)

That's well over 6-10 distinct searches. Good.

Now let me finish the orientation question. The key question #3: "whether in the original, the left-side and right-side legs receive the SAME servo numbers or MIRRORED/complementary numbers (e.g. 40 vs 140) in front()/back()."

From the original front():
- servo2.write(140), servo3.write(40) — in the same step, so servo2 and servo3 get complementary values (140 vs 40)
- servo1.write(40), servo4.write(140) — complementary
So yes, in the original the paired legs receive MIRRORED values (140 vs 40), not the same.

Now which is left/right? From local engine.html: servo1=右前腿 (right front), servo2=右后腿 (right rear), servo3=左前腿 (left front), servo4=左后腿 (left rear). Note: the local engine.html is NOT in the original repo (engine.html is absent from Gitee repo, and the original code has no /engine route). Wait — actually the local repo has engine.html and the original Gitee repo does NOT. But the oshwhub bot-dog page mentions /engine.html route in the code shown on the page. Let me check: the page showed `server.on("/engine.html"...)`. And the Gitee main.cpp has "server.on("/engine.html"" at line 270. Yes! The original code has /engine.html route, but the data/ folder in Gitee repo only has control.html, index.html, setting.html. So engine.html is missing from the Gitee repo (maybe in the attached zip).

So the local engine.html with 舵机1(右前腿), 舵机2(右后腿), 舵机3(左前腿), 舵机4(左后腿) — is that from the original? Let me verify by checking the attachments zip. That would be authoritative for the leg mapping.

Let me download the 12.7MB zip (likely 软件源码.zip) and check whether engine.html is in it and whether it labels legs.

Actually, let me check the wiki software page too, since it had detailed code. Let me search the wiki software page for "engine1" mapping descriptions (左前 etc.).

Let me do that quickly.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "Recon local project + extract distinctive strings", "priority": "high", "status": "completed"}, {"content": "Run 6-10 web searches (CN + EN) across engines", "priority": "high", "status": "completed"}, {"content": "Fetch most promising candidate pages", "priority": "high", "status": "completed"}, {"content": "Compare original vs local gait code, report v …[截断,原长412]` → `{"oldTodos":[{"content":"Recon local project + extract distinctive strings","status":"completed","priority":"high"},{"content":"Run 6-10 web searches (CN + EN) across engines","status":"in_progress","priority":"high"},{"content":"Fetch most promising candidate pages","status":"pending","priority":"high"},{"content":"Co …[截断,原长1003]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\ncurl -sL -m 120 -A \"$ua\" \"https://image.lceda.cn/oshwhub/project/attachments/79ea8924fab54c65a5060b3d5df74900.zip\" -o src_attach.zip -w \"zip %{http_code} %{size_download}\\n\"\nnode -e \"\nconst {ex …[截断,原长412]` → `zip 200 12758243 Archive: src_attach.zip Length Date Time Name --------- ---------- ----- ---- 0 2025-04-25 15:39 EDA-Robot机器狗项目/ 0 2025-04-25 15:38 EDA-Robot机器狗项目/3D文件/ 122 2025-03-21 16:51 EDA-Robot机器狗项目/3D文件/嘉立创云CAD工程分享链接.txt 0 2025-04-25 15:38 EDA-Robot机器狗项目/3D文件/适配V1.2(外置开关版,仅支持FDM)/ 274127 2025-03-21 16:51 EDA-Ro …[截断,原长2460]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:26）

Let me update my progress and verify the leg-mapping from the official attachment.

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nunzip -l src_attach.zip 2>/dev/null | sed -n '40,90p'", "description": "List rest of attachment contents"}` → ` 0 2025-04-25 15:38 EDA-Robot机器狗项目/固件/180度舵机版_V1.1/ 398656 2025-04-14 16:36 EDA-Robot机器狗项目/固件/180度舵机版_V1.1/firmware.bin 1466400 2025-04-14 16:36 EDA-Robot机器狗项目/固件/180度舵机版_V1.1/firmware.elf 1024000 2025-04-14 16:36 EDA-Robot机器狗项目/固件/180度舵机版_V1.1/spiffs.bin 0 2025-04-25 15:39 EDA-Robot机器狗项目/固件/360度舵机版/ 402768 2025-03-21  …[截断,原长1568]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:27）

Excellent — the official training-camp attachment. Let me extract the official PDF which explains leg/servo mapping.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Note: the local project's engine.html was NOT in the original repo (gitee has no engine.html) — wait, the local has engine.html and original oshwhub mentions engine.html route. Actually in the gitee repo there's only control.html, index.html, setting.html. But the oshwhub page text mentions engine.html routes. So local engine.html might be from the 360-degree version or from the local modification.

Let me extract the official PDF to look for leg mapping. Let me use soffice to convert PDF to text, or use the venv python with a pdf library.

Also important: check the 360 version zip (EDA-Robot(360度舵机版).zip) which may include the code with servo calibration and leg mapping. But the task is mainly about the original gait numbers.

Let me extract the PDF.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nmkdir -p att && unzip -o -q src_attach.zip \"EDA-Robot机器狗项目/EDA-Robot项目电子实训文档.pdf\" \"EDA-Robot机器狗项目/训练营资源包/SCH_机器狗原理图.pdf\" -d att 2>&1 | head -5\nfind att -type f | head", "description": "Extract official PDFs from attachment"}` → `att/EDA-Robot机器狗项目/EDA-Robot项目电子实训文档.pdf att/EDA-Robot机器狗项目/训练营资源包/SCH_机器狗原理图.pdf`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\n\"C:/ultralytics-main/.venv/Scripts/python.exe\" -c \"\nimport sys\ntry:\n from pypdf import PdfReader\nexcept ImportError:\n try:\n from PyPDF2 import PdfReader\n except ImportError:\n print('NO_PYPDF'); sys.exit(0)\nr=PdfReader(r'C:\\Users\\UserX\\AppData\\Local\\Temp\\s4s\\att\\EDA-Robot机器狗项目\\EDA-Robot项目电子实训文档. …[ …[截断,原长389]` → `NO_PYPDF`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nls \"C:/Users/UserX/miniconda3\" 2>/dev/null | head; ls /c/Users/UserX/ | head -30; ls /c/ | head -20", "description": "Locate python installations"}` → `AppData/ Application Data@ Contacts/ Cookies@ Desktop/ Documents/ Downloads/ Favorites/ Library/ Links/ Local Settings@ Music/ My Documents@ NTUSER.DAT NTUSER.DAT{a2332f18-cdbf-11ec-8680-002248483d79}.TM.blf NTUSER.DAT{a2332f18-cdbf-11ec-8680-002248483d79}.TMContainer00000000000000000001.regtrans-ms NTUSER.DAT{a2332f18 …[截断,原长822]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

No miniconda. Let me use pdftotext if available, or LibreOffice soffice which can convert PDF to text. Actually, let me check if pdftotext exists.

Actually, let me instead check the oshwhub project page & the wiki software page for the leg mapping — I already have the local engine.html saying 舵机1(右前腿), 舵机2(右后腿), 舵机3(左前腿), 舵机4(左后腿). Wait — but that's the LOCAL engine.html which isn't in the original repo. Hmm, but that's the most valuable info for leg mapping. Let me note it as coming from the local (modified) copy's engine.html, not the original.

Wait, actually — engine.html isn't in the Gitee original repo (the API returned [] for data/engine.html). But the oshwhub page mentioned a 电机校准页 (engine.html) for the 360 version. So engine.html may come from the 360-degree version, which was not in the Gitee repo. Let me check the 360 version zip.

Actually, let me try to get the 360-degree firmware/software. But actually the important comparison the user wants is gait numbers. I have those.

Let me try pdftotext for the training doc. Let me check availability.

Actually, I have enough. But the leg mapping (which servo is which leg) is important for question 4. Let me try to determine it from:
1. Local engine.html labels: servo1=右前腿, servo2=右后腿, servo3=左前腿, servo4=左后腿
2. The original's front() comment: "servo3.write(40); //左前向前旋转50度" - suggests servo3 = 左前 (left front). Wait, no! Let me re-read.

From GH eda_robotR1/eda_robotR1 (the 360 version):
```
servo3.write(40); //左前向前旋转50度
servo2.write(140);//右后向前旋转50度
```
Hmm, that's from the GitHub copy which mirrors the 360-degree version original. So servo3 = 左前 (left front), servo2 = 右后 (right rear)?

Hmm but local engine.html says servo3 = 左前腿. That's consistent! servo3 = 左前腿.

And servo2 = 右后腿 (local engine.html) but the comment says "右后向前旋转50度" — consistent! servo2 = 右后腿.

Then servo1 and servo4: from the 360 code, "servo1.write(40)" and "servo4.write(140)" — the pattern pairs (servo1, servo4) as the other diagonal. With servo3=左前 and servo2=右后, the remaining are 右前 and 左后. Which is which?

In front(), the comment says +30C for 2/3 and -30C for 1/4. In the oshwhub 360 code shown in the page:
```
//+30C 2/3
servo2.writeMicroseconds(1500 + speed + engine2offsetleftpwm);
servo3.writeMicroseconds(1500 - speed - engine3offsetleftpwm);
...
//-30C 1/4
servo1.writeMicroseconds(1500 - speed - engine1offsetrightpwm);
servo4.writeMicroseconds(1500 + speed + engine4offsetrightpwm);
```
So 2/3 = one diagonal pair (servo2, servo3 = 右后 + 左前), 1/4 = the other diagonal (servo1, servo4 = 右前 + 左后).

From local engine.html: servo1 = 右前腿, servo4 = 左后腿. That gives the diagonal pairing:
- Diagonal A: servo2 (右后腿) + servo3 (左前腿) ✓ — these are diagonal
- Diagonal B: servo1 (右前腿) + servo4 (左后腿) ✓ — these are diagonal

Great, consistent. So leg mapping: servo1=右前腿 (right front), servo2=右后腿 (right rear), servo3=左前腿 (left front), servo4=左后腿 (left rear).

Now for the "same vs mirrored" question. In front():
- servo2.write(140) and servo3.write(40) — in one diagonal, one goes >90 and other <90. These are diagonal legs (right rear + left front), so for a diagonal pair moving in the same direction (forward), with mirrored mounting you'd expect... hmm.

Actually let's think about it. The question is about left-side vs right-side legs. Left-side legs = 左前(servo3) + 左后(servo4). Right-side = 右前(servo1) + 右后(servo2).

In front():
- servo2 (右后) = 140, servo3 (左前) = 40 → 140 vs 40 → MIRRORED/complementary
- servo1 (右前) = 40, servo4 (左后) = 140 → 40 vs 140 → MIRRORED/complementary

So in the diagonal pair (servo2=右后 & servo3=左前), the numbers are complementary (140 vs 40): right rear and left front. These are diagonal, but they're mirrored in number.

For lateral pairs: servo3 (左前) = 40 vs servo1 (右前) = 40 → SAME (both 40). And servo2 (右后) = 140 vs servo4 (左后) = 140 → SAME (both 140).

Hmm interesting. So in front():
- Left front (s3) = 40, Right front (s1) = 40 → SAME
- Left rear (s4) = 140, Right rear (s2) = 140 → SAME

So the front legs get 40 and the rear legs get 140, and the left/right legs get the SAME number. That's the "same" case, not mirrored!

Wait, but let me look at the second half of front():
- servo1.write(140); servo4.write(40); → 右前=140, 左后=40
- servo2.write(40); servo3.write(140); → 右后=40, 左前=140

So in the second swing: 右前(s1)=140, 左前(s3)=140 → SAME. 右后(s2)=40, 左后(s4)=40 → SAME.

So YES: in front(), the left and right legs receive the SAME servo numbers (s1 & s3 same, s2 & s4 same). The diagonals get complementary numbers (40 vs 140).

Let me double check with back():
- s3.write(140); s2.write(40) → 左前=140, 右后=40 (diagonal, complementary)
- s4.write(40); s1.write(140) → 左后=40, 右前=140 (diagonal, complementary)
Hmm wait: s1 = 右前 = 140, s4 = 左后 = 40. Diagonal pair (s1,s4) = 140/40 → complementary.
- Later: s4.write(140); s1.write(40) → 左后=140, 右前=40
- s3.write(40); s2.write(140) → 左前=40, 右后=140

So in back(), s1(右前)=140 & s3(左前)=140 → SAME. s2(右后)=40 & s4(左后)=40 → SAME.

So the pattern holds in both front() and back(): left/right pairs get SAME numbers; diagonal pairs get complementary.

So the answer to question 3: SAME, not mirrored.

Hmm, wait. Let me reconsider. The local engine.html labels might not be reliable for the original. Let me double check against the "360度" version comments in the GitHub copy (which said 左前/右后).

Actually the GH copy `eda_robotR1` has comments "//左前向前旋转50度" on servo3 and "//右后向前旋转50度" on servo2. This is 360-version origin code. And local engine.html (which is a modified-page not in original) says s3=左前腿, s2=右后腿. These are two independent sources agreeing. Also the 360 code comment labels go: servo3 → 左前, servo2 → 右后.

Hmm, but wait: which source is the engine.html? It's likely from the 360-version's data folder. Let me verify by downloading the 360 version zip to see if engine.html exists there and what labels it has. That would confirm the leg mapping from the ORIGINAL authors. Let me do that — the zip "EDA-Robot(360度舵机版).zip" is one of the attachments (12758243 was the software source; let me check which one is the 360 version).

Actually the attachment I downloaded (79ea8924fab54c65a5060b3d5df74900.zip = 12.7MB) was labeled "EDA-Robot机器狗项目" which contains 硬件工程, 固件, 3D文件, BOM, 表情, 训练营资源包, PDF. So that's the "EDA-Robot机器狗项目.zip".

Let me download "软件源码.zip" and "EDA-Robot(360度舵机版).zip" to check for engine.html. Sizes: 33947718, 33958851, 35138116, 133471671, 12758243. The 133MB is probably the 3D/whole project. Let me check headers to identify.

Actually, let me be efficient. The key question about servo mapping is mostly answered. But to be thorough on question 4 (servo mounting orientation), let me check the 360-version zip which contains the calibration page (engine.html) since the oshwhub description says 校准页 exists for 360 version.

Let me download the remaining attachments and search for engine.html.

Actually 33-35MB each × 3 = ~100MB. That's fine but slow. Let me first check which one contains engine.html by downloading and listing. Let me do the ones most likely: The description says "软件源码.zip" 3459 downloads and "EDA-Robot(360度舵机版).zip" 778 downloads. Let me try to get the listing of links with their names from the raw HTML.

Let me grep the raw HTML for attachment names near those URLs.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');const s=fs.readFileSync('ow_botdog.html','utf8');\n// find attachment name + url pairs\nconst re=/\\\"id\\\":\\\"[^\\\"]*\\\",\\\"name\\\":\\\"([^\\\"]+)\\\"[\\s\\S]{0,400}?\\\"url\\\":\\\"(https:\\/\\/image\\.lceda\\.cn\\/oshwhub\\/project\\/attachments\\/[^\\\"]+)\\\"/g;\nlet m;whi …[截断,原长412]` → `--- alt pattern --- t/attachments/b3f76c6e5f174920be5ff881c51cb053.mp4 | ctx: -cell style=text-align:center>1</td><td class=ant-table-cell ant-table-cell-ellipsis style=text-align:center><div class=appendixTable_download__mbdDM data-href= t/attachments/79ea8924fab54c65a5060b3d5df74900.zip | ctx: -cell style=text-align: …[截断,原长1552]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:29）

Let me identify which attachment contains the calibration page (engine.html) for the leg mapping.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Attachment #2 (79ea8924...) = 软件源码.zip which I downloaded = EDA-Robot机器狗项目 (the training camp resource). Attachment #3 (2686655fc5e54288b6389d81cb3d9545) is likely "EDA-Robot(180度舵机版)_V1.0.zip", #4 = V1.1, #5 (133MB) = 360度舵机版, #6 = project zip.

Let me get the attachment names to confirm, and importantly download the V1.0 180-degree zip to check the ORIGINAL control.html/engine.html and see if the gaits there differ. Actually the key question was about the original gait numbers, which I have from Gitee (V1.1 180-degree). 

Let me now also check the 180-degree V1.0 and the 360-degree version to see the servo mapping / orientation info. And check the engine.html in the 360 version (calibration page) which may include leg names.

Actually, let me look for names in the page text table. Let me extract the appendix table text.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');const s=fs.readFileSync('ow_botdog.html','utf8');\nconst i=s.indexOf('appendixTable');\nlet seg=s.slice(i-3000,i+9000);\nseg=seg.replace(/<td[^>]*>/g,' || ').replace(/<[^>]*>/g,'').replace(/&nbsp;/g,' ').replace(/\\s+/g,' ');\nconsole.log(seg.slice(0,2200));\n\"", "description": "Ext …[截断,原长412]` → `0819 || 50 || 4.1 || 5 || 瓷片电容 || 100nF || C84772 || 1 || 0.1881 || 10 || 1.88 || 6 || 直插电阻 || 10kΩ || C2894649 || 8 || 0.0183 || 100 || 1.83 || 8 || 直插电阻 || 750kΩ || C714344 || 1 || 0.0188 || 50 || 0.94 || 9 || 直插电阻 || 100kΩ || C2894647 || 1 || 0.0668 || 100 || 1.79 || 10 || 轻触按键 || 6x6-TH || C42416243 || 2 || 0.03145 …[截断,原长1424]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:29）

Let me confirm attachment names and check the 360-degree version for leg mapping and orientation.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

So:
- Attachment #5 "软件源码.zip" = 79ea8924fab54c65a5060b3d5df74900.zip (12758243 bytes) — that's what I downloaded (the full project with PDFs, firmware, etc.). Hmm, actually that seems like EDA-Robot机器狗项目.zip. Let me check: #2 EDA-Robot机器狗项目.zip = 2686655fc5e54288b6389d81cb3d9545.zip (35MB). #3 = 1cbae5b1f7ed4f9d9209d771c856396a.zip (33.9MB). #5 = 79ea8924... (12.7MB) - which I downloaded and it contained "EDA-Robot机器狗项目/" folder with PDFs, firmware, 3D files, BOM, and 训练营资源包. Wait, that's actually "软件源码.zip" per numbering (5th row). Hmm, the numbering in the table: 1 = mp4, 2 = 2686655..., 3 = 1cbae5b1..., 4 = 3d5e14de..., 5 = 79ea8924..., 6 = 1f105ddb... 

Wait let me re-check the order of data-href: mp4(#1), 79ea8924(#? in the second listing appeared as 2), 2686(#3?), 1cbae(#4?), 3d5e(#5?), 1f10(#6?). The second regex listed them in document order: b3f76c(#1), 79ea8924(#2), 2686(#3), 1cbae(#4), 3d5e(#5), 1f10(#6), a4df(#7).

Hmm, the first node listing (from the pattern with cell 1) gave: mp4 first, then 79ea8924 with context "cell>1</td>"? Actually the context shows the preceding cell text which is the row number. For 79ea8924 the context ends with "cell>1</td><td...appendixTable_download__mbdDM data-href=" — that "1" might be the 下载次数 column or the row index. Let me just verify what I downloaded: it had 3D files, BOM, PDF, Gerber, 固件 (firmware bins), 硬件工程 (.epro), 表情 (bmp), 训练营资源包. That's the "EDA-Robot机器狗项目.zip" content, not "软件源码.zip".

Hmm. Actually the file listing said "EDA-Robot机器狗项目/..." as the top folder. The table row #2 is "EDA-Robot机器狗项目.zip" with 下载次数 2041. So 79ea8924 = #2 in the appendix table order as listed by the second regex. Wait but the first regex's context showed "cell>1" preceding. Whatever — I downloaded the one that contains the full project package including the training PDF. Good enough: it's an official attachment. Actually let me double check by listing the second regex order properly with the row number.

It doesn't matter much. What matters: I want the "软件源码.zip" to confirm whether the official source has same gaits and whether the engine.html has leg labels. But actually I already have the Gitee repo which is the authoritative source code repo linked from the oshwhub page ("代码仓 Gitee"). And I confirmed local gaits are identical to Gitee main.cpp. 

But wait — an important nuance: the local project has engine.html with labels 舵机1(右前腿), 舵机2(右后腿), 舵机3(左前腿), 舵机4(左后腿). The Gitee original lacks engine.html in its tree (only control.html, index.html, setting.html). Hmm, actually the Gitee tree listed data/control.html, index.html, setting.html — no engine.html. But the 360-degree version (EDA-Robot(360度舵机版).zip) might contain engine.html. The local copy has LittleFS + engine.html + engine calibration page (engine.html) which resembles the 360版 program with per-servo offset calibration (engine1offsetleftpwm etc.). And indeed the oshwhub description mentioned 电机校准页 and engine1offsetleftpwm variables — that's the 360 version. The local code has LittleFS (not SPIFFS) and a different AP password (12345678), plus defaultWeatherKey hardcoded.

So the modified copy appears derived from the 180-degree V1.1 source (gaits identical) but with a custom engine.html web servo-debug page and LittleFS migration. I should verify: does the local code have left90/right90? No. Does the 180 V1.1 Gitee have left90? No (not found). The oshwhub description mentions left90()/right90() in the software wiki page for the 360 version. The local doesn't have them. OK.

Let me now check the 360 version zip to see whether its gaits differ and whether it contains engine.html with leg labels — that's directly relevant to question 4 (servo mounting orientation). The 360版 zip is attachment #6 (1f105ddb..., 33.9MB) or #3/#4. Let me download the 360度舵机版 zip and check.

Actually, the more targeted: the local engine.html labels 舵机1(右前腿), 舵机2(右后腿), 舵机3(左前腿), 舵机4(左后腿). This gives left/right leg mapping. And front(): servo2(右后) write 140, servo3(左前) write 40 — mirrored values 140 vs 40. So same: left front (servo3) 40 and right rear (servo2) 140 in step 1, then right front (servo1) 40 and left rear (servo4) 140. Interesting: so in the original, servo1(右前) and servo3(左前) both get 40 in the "first" phase... wait:

front() original:
- servo2.write(140) [右后], servo3.write(40) [左前]  → diagonal pair
- servo1.write(40) [右前], servo4.write(140) [左后]
So in the first two steps: 左前=40, 右后=140, 右前=40, 左后=140. So all "front" legs get 40 and all "rear" legs get 140?? No wait: 左前(servo3)=40, 右前(servo1)=40, 右后(servo2)=140, 左后(servo4)=140. Hmm interesting. So actually within front(), the front legs (1&3) both go to 40 and the rear legs (2&4) both go to 140 at the "swing" phase. Then they return to 90, then swap: servo1(右前)=140, servo4(左后)=40, servo2(右后)=40, servo3(左前)=140.

Hmm, so it's not simply mirrored by left/right — it's diagonal/phase-based. Let me get this right by tabulating with leg names.

Leg map (from LOCAL engine.html, which is a modification but the servo pins/naming likely carries over):
- servo1 = engine1 = GPIO14 = 舵机1 = 右前腿 (right front)
- servo2 = engine2 = GPIO16 = 舵机2 = 右后腿 (right rear)
- servo3 = engine3 = GPIO12 = 舵机3 = 左前腿 (left front)
- servo4 = engine4 = GPIO13 = 舵机4 = 左后腿 (left rear)

Original front() (gitee 180° V1.1):
1. servo2=140 (右后), servo3=40 (左前) — delay 100
2. servo1=40 (右前), servo4=140 (左后) — delay 100
3. servo2=90, servo3=90 — delay 100
4. servo1=90, servo4=90 — delay 100
5. servo1=140 (右前), servo4=40 (左后) — delay 100
6. servo2=40 (右后), servo3=140 (左前) — delay 100
7. servo1=90, servo4=90 — delay 100
8. servo2=90, servo3=90

So the left-side servo (servo3, left front) gets 40 in the first half and 140 in the second half; the right-side counterpart servo1 (right front) gets 40 in the first half and 140 in the second half — SAME numbers, not mirrored! servo1 and servo3 both = 40 then both = 140. And the rear pair servo2 (right rear) and servo4 (left rear) both = 140 then both = 40.

So: front legs (1,3) same values; rear legs (2,4) same values; front legs are opposite-phase to rear legs. That is: left and right legs receive the SAME servo numbers (not mirrored). Wait — but that only works if the left and right legs are mounted mirrored physically... Hmm, no. If left and right servos are mounted mirror-image, then giving both the same angle makes them move in mirrored directions, producing forward vs backward swing... Actually with mirrored mounting, giving both the same numeric angle makes the legs swing opposite in body frame — that's what you want for walking (one leg forward while the other backward? no...).

Hmm, careful. For a walking gait in a quadruped, you typically want diagonal pairs to move together. Here front legs (servo1 right-front and servo3 left-front) both get 40, and the diagonal pair (right-rear servo2 and left-rear servo4) both get 140 opposite. So servo1 (RF) and servo3 (LF) move together with same numbers → for a forward walking motion you'd want RF and LF to swing in the SAME direction? For a trot, diagonal pairs work together: LF + RR together, RF + LR together. Here we have front pair together (RF+LF at 40) and rear pair together (RR+LR at 140). Hmm that's a "bound" or... Actually hmm, wait: the phase for leg "swing forward" vs "stance".

Anyway the key deliverable for Q3: in the original front()/back(), do the left and right legs receive the SAME servo numbers or MIRRORED (e.g., 40 vs 140)?

Answer: For the FRONT pair: servo1 (right front) and servo3 (left front) receive the SAME numbers (both 40 in step 1/2, both 140 in step 5/6). For the REAR pair: servo2 (right rear) and servo4 (left rear) likewise receive the SAME numbers. So SAME, not mirrored, when paired front-with-front and rear-with-rear. The mirroring is between FRONT and REAR (40 vs 140), i.e., diagonal/anti-phase.

Hmm, but the "toplefthand" function: servo3=0 then 30; toprighthand: servo1=180 then 150. So lifting left front = servo3 → 0/30 (low values), lifting right front = servo1 → 180/150 (high values). That indicates the two front servos are mounted mirrored, since to lift the corresponding "hand" you need opposite numeric extremes. That's strong evidence that the left/right servos are mounted in mirror orientation (rotated 180° about the leg axis), so equal numbers give opposite mechanical directions.

Hmm, but then in front(), giving servo1 and servo3 the same number (both 40) would swing them in opposite directions mechanically — which is exactly what we said. Hmm, so then which is "forward"? For a walk where front-left and front-right both swing... in a "front-swing" both front legs move forward, and both rear legs move backward → then front legs pull and the body moves... hmm actually that would make the dog "crawl"/"bound". Actually with the phases it's a trot-like gait.

OK. I should be careful and just report facts:
- servo→leg mapping: from the local (modified) engine.html labels: servo1=右前腿, servo2=右后腿, servo3=左前腿, servo4=左后腿. This is from the MODIFIED copy, not the original — I must flag it as such. But is there an original source for the mapping? The 360° version zip from oshwhub likely contains engine.html with these labels, or the PDF. Let me check the 360 version and the official PDF (via LibreOffice conversion or the python env).

Let me try extracting PDF text using a different approach — maybe pdftotext exists, or use the conda python at C:\Users\UserX\miniconda3? Earlier ls showed no miniconda3 in the user dir listing (the first command errored with exit code 2 possibly because files don't exist). Let me search for python.exe.

Actually the AGENTS.md says conda python is not on PATH and I should read ~/.zcode/memory/python-envs.md for the full list. Let me do that.

Alternatively, LibreOffice soffice.com exists → can convert PDF? Not really (PDF import via draw). But there's a simpler path: the training PDF text might not be needed. What I need for Q4 is servo mounting orientation. The engine.html labels (in the local modified copy) tell servo→leg mapping. For mounting orientation, the strongest evidence:
1. toplefthand uses servo3 → 0/30 while toprighthand uses servo1 → 180/150: opposite extremes for the same mechanical action → mirrored mounting for the front pair.
2. lie() uses servo1=180, servo3=0, servo2=0, servo4=180 → again left-right opposite extremes for the same "lie flat" action → mirrored mounting.
3. dosleep: servo1=0, servo3=180, servo2=180, servo4=0 → opposite again.
4. sitdown: servo2=140, servo4=40 → opposite extremes for the rear pair → mirrored mounting for rear pair too. Wait servo2=140 and servo4=40 — those are mirrored/complementary! So for sitdown, the rear pair DOES get mirrored numbers (140 vs 40). Hmm! So for the rear pair: servo2=140 & servo4=40 are complementary. While in front() the rear pair both got 140... 

Hmm wait, front() step 1: servo2=140, servo4=140 — same. sitdown: servo2=140, servo4=40 — mirrored.

Hmm, that's inconsistent unless the meaning differs. Let's think about geometry: In sitdown, both rear legs need to move in the same mechanical direction (both fold backward), so with mirrored mounting you'd need complementary numbers (140 vs 40). And in front(), the rear legs need to move in opposite mechanical directions (anti-phase) so they need equal numbers. That's self-consistent with mirrored mounting!

Similarly the front pair: front() gives servo1=servo3 (same numbers) → they move in opposite mechanical directions (anti-phase) — consistent with mirrored mounting.

And in left()/right(): servo1 & servo4 always share the same number, and servo2 & servo3 always share. Under mirrored mounting (1&3 mirrored, 2&4 mirrored), equal numbers for 1&4 means... hmm, 1 is right-front, 4 is left-rear — those are diagonal, not a mirrored pair, so equal numbers there produce phase-shifted motion. Fine.

So: the evidence strongly indicates mirrored mounting of left/right legs, and the front() function gives the SAME numbers to left and right legs (equal numbers = opposite mechanical swing because of mirror mounting).

Hold on. Let me reconsider. Actually maybe not mirrored — maybe simply "rotated 180°" about the servo axis = mirrored. Yes that's what I said.

Now which value (<90 or >90) swings a leg forward? I can't determine this from code alone without knowing the mounting. But maybe the original wiki/PDF says. Let me look at the 360° version's engine.html (calibration page) which may have labels like "电机左转90度" etc. And the oshwhub description says the calibration instructions: "点击一次'电机左转90度'" — so left rotation = ? The left90()/right90() functions in the 360 version apply offsets. Let me get the 360° source zip and compare; it may also contain the engine.html with leg labels and offset signs that reveal orientation.

Let me download EDA-Robot(360度舵机版).zip (attachment #6 = 1f105ddb... 33.9MB, or #3 1cbae5b1 33.9MB). Which one is the 360 version? The table order: 1 mp4, 2 EDA-Robot机器狗项目.zip, 3 EDA-Robot(180度舵机版)_V1.0.zip, 4 EDA-Robot(180度舵机版)_V1.1.zip, 5 软件源码.zip, 6 EDA-Robot(360度舵机版).zip, 7 xlsx.

Now the second regex found order: b3f76c(mp4), 79ea8924, 2686, 1cbae, 3d5e, 1f10, a4df. So:
- 79ea8924 (12.7MB) = #2 EDA-Robot机器狗项目.zip → this is what I downloaded; it contained the full project incl. firmware for 180 V1.0/V1.1/360, 3D, BOM, Gerber, 硬件工程, 训练营资源包, PDF. Yes! That matches "EDA-Robot机器狗项目.zip". Good.
- 2686 (35.1MB) = #3 EDA-Robot(180度舵机版)_V1.0.zip
- 1cbae (33.9MB) = #4 EDA-Robot(180度舵机版)_V1.1.zip

Hmm, but then #5 软件源码.zip = 3d5e (133MB)? That seems too big for 软件源码. Hmm, maybe 3d5e is something else. And #6 360版 = 1f10 (33.9MB).

Wait, sizes: 180 V1.0 = 33.9MB, 180 V1.1 = 35.1MB, 软件源码 = 133MB?, 360版 = 33.9MB. Ok whatever.

Since the local modified copy has engine.html (calibration page) which is in the 360 version, and it also has LittleFS, let me download the 360版 zip (1f105ddb, 33.9MB) and check its source + engine.html. That's the likely direct parent for the "engine.html" page and the offset-calibration features. Wait, but the local copy does NOT have the offset/calibration variables or left90/right90... The local copy's engine.html is a servo slider debug page (simple per-servo angle sliders) — probably written by the person who modified it (custom). Hmm, but the local code has routes for /engine.html and probably /servo?action... Let me check the local main.cpp for what the engine.html page posts to. Let me grep.

Let me also check the 180 V1.1 zip for engine.html (it may exist there since the Gitee repo lacks it). Actually the Gitee repo tree (main branch) shows only control/index/setting — no engine.html. Yet Gitee main.cpp HAS server.on("/engine.html", ...) per my earlier grep (line 270). So engine.html exists as a route but the file isn't in the repo. Interesting.

Let me now:
1. grep local main.cpp for engine.html routes & servo debug endpoint (to see if engine.html is custom).
2. Download the 360版 zip, check for engine.html and leg labels.
3. Try to extract text from the official PDF (worth one attempt via LibreOffice or find a python).

Let me do these.

</details>

- 🔧 **Bash** `{"command": "cd \"/c/Users/UserX/Downloads/Robot dog 1.1\" && grep -n \"engine.html\\|/servo\\|angle\\|setangle\\|/set\" src/main.cpp | head -30; echo \"=== engine.html JS fetch calls ===\"; grep -oE \"fetch\\([^)]*\\)|'/[a-zA-Z0-9_?=&{}]*'\" data/engine.html | sort -u | head -20", "description": "Check local engine.html endpoints"}` → `158: server.on("/servo1", HTTP_GET, [](AsyncWebServerRequest *request) 160: if (request->hasParam("angle")) { 161: int angle = request->getParam("angle")->value().toInt(); 162: if (angle >= 0 && angle <= 180) { 163: servo1.write(angle); 167: server.on("/servo2", HTTP_GET, [](AsyncWebServerRequest *request) 169: if (req …[截断,原长1466]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\ncurl -sL -m 200 -A \"$ua\" \"https://image.lceda.cn/oshwhub/project/attachments/1f105ddb15984777b02b3d6a41b089f5.zip\" -o v360.zip -w \"360 %{http_code} %{size_download}\\n\"\nunzip -l v360.zip 2>/dev/nu …[截断,原长412]` → `360 200 33958851 17904 2024-12-12 14:02 EDA-Robot/.pio/build/nodemcuv2/FrameworkArduino/core_esp8266_main.cpp.o 331856 2024-12-24 09:16 EDA-Robot/.pio/build/nodemcuv2/src/main.cpp.o 10357 2024-11-15 16:05 EDA-Robot/.pio/libdeps/nodemcuv2/ArduinoJson/README.md 10357 2024-09-18 16:49 EDA-Robot/.pio/libdeps/nodemcuv2/<邮箱> …[截断,原长1306]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:30）

Let me examine the 360-degree version (which has the calibration page) and check the local engine.html endpoints.

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nmkdir -p v360 && unzip -o -q v360.zip \"EDA-Robot/src/main.cpp\" \"EDA-Robot/platformio.ini\" \"EDA-Robot/data/*\" -d v360 2>&1 | head -3\nfind v360 -type f | head -10", "description": "Extract 360-degree version source files"}` → `v360/EDA-Robot/data/control.html v360/EDA-Robot/data/engine.html v360/EDA-Robot/data/index.html v360/EDA-Robot/data/setting.html v360/EDA-Robot/platformio.ini v360/EDA-Robot/src/main.cpp`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:31）

Got the 360-degree original source tree. Let me extract and compare its gaits.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

 

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== 360 version header ===\"; head -20 v360/EDA-Robot/src/main.cpp\necho; echo \"=== 360: engine offsets + speed + runtime ===\"; grep -n \"offset\\|int speed\\|runtime\\|int engine\" v360/EDA-Robot/src/main.cpp | head -25", "description": "Inspect 360-degree version source"}` → `=== 360 version header === // 导入头文件 #include <Arduino.h> #include <Servo.h> #include <U8g2lib.h> #include <Wire.h> #include <FS.h> #include <ESP8266WiFi.h> #include <ESPAsyncWebServer.h> #include <ESP8266HTTPClient.h> #include <NTPClient.h> #include <ArduinoJson.h> #include <WiFiUdp.h> #include "image.cpp" #define BUTT …[截断,原长2116]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== 360 version: gait functions ===\"; grep -n \"^void \\|^float \\|^int \" v360/EDA-Robot/src/main.cpp | head -30\necho; echo \"=== 360 control.html buttons ===\"; node -e \"\nconst fs=require('fs');let s=fs.readFileSync('v360/EDA-Robot/data/control.html','utf8');\nconsole.log([...s.matchAll(/<button[^>]*>([^< …[截断,原长412]` → `=== 360 version: gait functions === 31:float batteryVoltage = 0; // 计算电池电压 32:int batteryPercentage=0; 53:int engine1 = 14; // 舵机引脚 54:int engine1offsetleftpwm = -93; // 舵机左转补偿 55:int engine1offsetrightpwm = -87; // 舵机左转补偿-40 56:int engine2 = 16; // 舵机引脚 57:int engine2offsetleftpwm = -120; // 舵机左转补偿 58:int engine2offse …[截断,原长1204]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:31）

Now I have the 360-degree original (the ancestor of the local copy's architecture). Let me analyze it.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The 360 version is the earliest (Dec 2024), uses writeMicroseconds with offsets. The local modified copy's "Robot dog 1.1" appears descended from the V1.1 180-degree version (gitee) — the gaits are byte-identical.

Let me check hierarchy:
1. 360 version (Dec 2024) - `writeMicroseconds` + offsets + runtime
2. 180-degree V1.0 (Mar 2025)
3. 180-degree V1.1 (Apr 2025) = gitee repo main branch = matches local exactly

Let me verify the 180 V1.0 zip vs V1.1 to see which one the local matches. Also let me get the 180-degree zip.

Actually, I already have strong conclusions. Let me do a couple more things:
1. Verify the local copy's engine.html is NOT in either original (confirms local modification).
2. Check the 180 V1.0 to be thorough — the attachment 1cbae5b1f7ed4f9d9209d771c856396a is "EDA-Robot(180度舵机版)_V1.1.zip" (item 4), and 2686655fc5e54288b6389d81cb3d9545 is item 3 = V1.0. Actually let me determine: order is 1=video, 2=项目zip, 3=180_V1.0, 4=180_V1.1, 5=软件源码.zip, 6=360度舵机版, 7=xlsx.

Wait, from the HTML: attachment list order was 1 video mp4, 2 = 79ea...zip (12.7MB - that's what I downloaded, and it was the "EDA-Robot机器狗项目" full package), 3 = 2686655...zip, 4 = 1cbae5b1...zip, 5 = 3d5e14de...(133MB), 6 = 1f105ddb...(33.9MB), 7 = xlsx.

Hmm, my assumption was wrong. Let me verify: 79ea8924 = 12.75MB = "EDA-Robot机器狗项目.zip" = the full project package. 2686655 = item 3 = "EDA-Robot(180度舵机版)_V1.0.zip". 1cbae5b1 = item 4 = "EDA-Robot(180度舵机版)_V1.1.zip". 3d5e14de = item 5 = "软件源码.zip" (133MB, contains .pio junk). 1f105ddb = item 6 = "EDA-Robot(360度舵机版).zip" (33.9MB — matches, it had .pio dirs). 

Wait, but item 5 is "软件源码.zip" at 3459 downloads and 133MB. And item 6 = 360度舵机版 at 778 downloads. Hmm, actually the 360 zip I downloaded (1f105ddb, 33.9MB) had "EDA-Robot/src/main.cpp" with offsets — that's the 360 version. So item 6 = 1f105ddb = 360度舵机版. Correct.

So item 4 = 1cbae5b1 = 180度舵机版_V1.1. Let me download that to compare with local exactly. And item 3 = 2686655 = V1.0.

Actually, the local project's gaits match the gitee main branch (V1.1 = 180度舵机版本). Let me download 1cbae5b1 (V1.1) to be thorough and check if local's engine.html exists there.

Actually, more efficient: let me download 1cbae5b1 (17MB... no, 33.9MB) - that's manageable.

Let me do that to definitively identify which version the local copy is derived from (and whether engine.html came from there).

Time check: I've done many searches. Let me wrap up with this final verification.

Actually the key question was answered. But the local has engine.html with 舵机1 (右前腿) etc. and /servoN?angle= endpoints, which is NOT in the 180 V1.1 gitee version (28 endpoints) — the local has 32 endpoints. Let me confirm the local's engine.html endpoints came from a modification.

Let me check the 180 V1.1 zip.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\ncurl -sL -m 250 -A \"$ua\" \"https://image.lceda.cn/oshwhub/project/attachments/1cbae5b1f7ed4f9d9209d771c856396a.zip\" -o v180_11.zip -w \"v180_11 %{http_code} %{size_download}\\n\"\nunzip -l v180_11.zip …[截断,原长411]` → `v180_11 200 33947718 17904 2025-04-14 11:38 EDA-Robot/.pio/build/nodemcuv2/FrameworkArduino/core_esp8266_main.cpp.o 267260 2025-04-14 16:25 EDA-Robot/.pio/build/nodemcuv2/src/main.cpp.o 10357 2024-11-15 16:05 EDA-Robot/.pio/libdeps/nodemcuv2/ArduinoJson/README.md 10357 2024-09-18 16:49 EDA-Robot/.pio/libdeps/nodemcuv2/ …[截断,原长1125]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:32）

Let me verify by downloading the official 180-degree V1.1 zip.

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nunzip -l v180_11.zip 2>/dev/null | grep -E \"src/main.cpp|platformio.ini\" | head -5\nmkdir -p v180 && unzip -o -q v180_11.zip \"EDA-Robot/src/main.cpp\" \"EDA-Robot/data/*\" \"EDA-Robot/platformio.ini\" -d v180\nls -la v180/EDA-Robot/src/ v180/EDA-Robot/data/ 2>/dev/null\necho \"=== compare V1.1 official main.cpp vs  …[截断,原长412]` → ` 267260 2025-04-14 16:25 EDA-Robot/.pio/build/nodemcuv2/src/main.cpp.o 1838 2024-12-10 14:14 EDA-Robot/platformio.ini 36170 2025-04-14 16:29 EDA-Robot/src/main.cpp v180/EDA-Robot/data/: total 16 drwxr-xr-x 1 user 197121 0 Apr 14 2025 ./ drwxr-xr-x 1 user 197121 0 Oct 9 00:33 ../ -rw-r--r-- 1 user 197121 6270 Dec 30 202 …[截断,原长727]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\ncp v180/EDA-Robot/src/main.cpp official_v11.cpp\nnode -e \"\nconst fs=require('fs');\nfunction extract(src,names){const out={};for(const n of names){const re=new RegExp('void\\\\\\\\s+'+n+'\\\\\\\\s*\\\\\\\\(\\\\\\\\s*\\\\\\\\)\\\\\\\\s*\\\\\\\\{');const m=re.exec(src);if(!m){out[n]=null;continue;}let i=m.index+m[0].l …[截断,原长413]` → `func | officialV1.1==gitee | officialV1.1==local front YES | YES back YES | YES left YES | YES right YES | YES sitdown YES | YES lie YES | YES toplefthand YES | YES toprighthand YES | YES dosleep YES | YES --- official V1.1 front --- --- local front ---`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:33）

Let me compare the official V1.1 build to the Gitee source and extract its gait functions.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The seq extraction returned empty — probably because the official V1.1 uses different formatting. Let me look at the official V1.1's front() to see.

Actually, norm comparison says YES for all — identical to Gitee and to local. But seq printed empty... that's odd. Wait, the issue is `seq(O.front)` — O.front may be undefined because I used O.front but the key is 'front' — that should work. Unless the regex `servo(\d)\.(write...)` fails... Hmm but seq(L.front) also empty, and local front definitely has servo2.write(140).

Oh! The issue is that in the node -e string, the `\d` and `\.` got mangled by bash escaping through double quotes. In the earlier diff.js I used a file. Let me just use a script file. But the key confirmation (norm equality) is meaningful.

Let me write a proper script file for this.

</details>

- 🔧 **Write** `{"content": "const fs = require('fs');\nconst S = 'C:/Users/UserX/AppData/Local/Temp/s4s/';\n\nfunction extract(src, names) {\n const out = {};\n for (const n of names) {\n const re = new RegExp('void\\\\s+' + n + '\\\\s*\\\\(\\\\s*\\\\)\\\\s*\\\\{');\n const m = re.exec(src);\n if (!m) { out[n] = null; continue; }\n let i = m.index + m[0].length - 1, d = 0;\n for (; i < src.le …[截断,原长396]` → `File created successfully at: C:\Users\UserX\AppData\Local\Temp\s4s\diff2.js (file state is current in your context — no need to Read it back)`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:33）

Let me redo that check via a script file to avoid shell escaping issues.

- 🔧 **Bash** `{"command": "cd /c/Users/UserX/AppData/Local/Temp/s4s && node diff2.js", "description": "Run comparative gait diff"}` → `func | offV1.1==gitee | offV1.1==local | offV1.1==ghR1 front YES YES no back YES YES no left YES YES no right YES YES no sitdown YES YES YES lie YES YES no toplefthand YES YES no toprighthand YES YES no dosleep YES YES no --- official V1.1 front() --- s2.write(140) | s3.write(40) | delay(100) | s1.write(40) | s4.write( …[截断,原长1110]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Definitive. The local copy's gait functions are bit-identical (after comment/whitespace normalization) to the official EDA-Robot 180-degree V1.1 release and to the Gitee repo.

Let me get the verbatim bodies with comments for the report. Let me read the official V1.1 gaits verbatim so I quote exactly.

Also I need to verify the leg mapping claim (servo1=右前腿 etc.) — I have that from the LOCAL engine.html (line 122-155): servo1 (右前腿), servo2 (右后腿), servo3 (左前腿), servo4 (左后腿). But this engine.html is local-only (not in the original). Let me check what the 360-degree original engine.html said about legs, since that's where the engine.html came from.

Actually, the 360 original zip has engine.html. Let me check it — and the 180 V1.1 zip doesn't have engine.html (only control/index/setting). Let me grep the 360's engine.html for 腿 labels.

Also, the 360 version control.html has the 100%-identical button set to original, and lacks 回收机器狗. The local has 回收机器狗 (a modification) and engine.html (borrowed from 360 version).

Let me check the 360 engine.html labels.

Then, for the "which value swings a leg forward" question — I need to reason about it but mark uncertainty. From front(): servo2=140 & servo3=40 for legs... Actually let me reason carefully.

Leg mapping (from engine.html in local copy, and need to check 360 original): servo1=右前腿 (right front), servo2=右后腿 (right rear), servo3=左前腿 (left front), servo4=左后腿 (left rear).

Wait — that's reversed relative to what a normal reading would be. Hmm, in front(), servo2.write(140) is paired with servo3.write(40) — servo2 (right rear) 140 and servo3 (left front) 40. Then servo1 (right front) 40 and servo4 (left rear) 140.

Hmm, that's diagonal pairing: RF+LR at 40, RR+LF at 140. That is a diagonal trot gait. And note the pairing is: {servo1=RF, servo4=LR} get the SAME number (40), and {servo2=RR, servo3=LF} get the SAME number (140). So within one diagonal pair the two legs get the same number, but the two diagonals get complementary numbers (40 vs 140).

So the answer to Q3: in front()/back(), the left-side and right-side legs get MIRRORED/complementary numbers — specifically the two diagonals are anti-phase: {1,4} = 40 while {2,3} = 140 (then later swapped: {1,4} = 140 while {2,3} = 40). Within a diagonal pair, one is a right leg and one is a left leg, and they receive the SAME number. So it's neither purely "same" nor purely "mirrored" — it is diagonal (contralateral anti-phase) pairing.

Let me be careful about the local engine.html mapping. Let me verify with the official docs whether servo1..4 = which legs. Let me check the 360 engine.html and also look at the official 360 doc text (main.cpp comments). Also the oshwhub page mentioned "舵机校准" with "电机左转90度" for the 360 version.

Let me grep the 360 engine.html for leg names and check the official V1.1 control.html.

Actually, an important check: is the local engine.html's leg mapping (servo1=右前腿, servo2=右后腿, servo3=左前腿, servo4=左后腿) present in the official 360 engine.html? Let me check.

Let me also check the local image.cpp vs official image.cpp, and count endpoints. And check whether local control.html differs.

Let me run these checks.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== 360 official engine.html leg labels ===\"\ngrep -oE '>[^<>]*(舵机|腿)[^<>]*<' v360/EDA-Robot/data/engine.html | head -20\necho \"=== 360 official engine.html slider ids ===\"\ngrep -oE 'id=\"servo[0-9]\"|servo[0-9]' v360/EDA-Robot/data/engine.html | sort -u | head\necho \"=== 360 official: search leg words === …[截断,原长412]` → `=== 360 official engine.html leg labels === === 360 official engine.html slider ids === === 360 official: search leg words === 右前: 0 左前: 0 右后: 0 左后: 0 前腿: 0 后腿: 0`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== official V1.1 control.html buttons ===\"\nnode -e \"\nconst fs=require('fs');let s=fs.readFileSync('v180/EDA-Robot/data/control.html','utf8');\nconsole.log([...s.matchAll(/<button[^>]*>([^<]*)<\\/button>/g)].map(m=>m[1].trim()).join(' | '));\n\"\necho \"=== local control.html vs official V1.1 ===\"\nnode -e …[截断,原长412]` → `=== official V1.1 control.html buttons === ↑ | ← | → | ↓ | 抬左手 | 抬右手 | 坐下 | 趴下 | 自由模式开 | 自由模式关 | 回收 | 开心 | 生气 | 难受 | 好奇 | 喜欢 | 错误 | 晕 | 嘉立创LOGO | 时间 | 天气 === local control.html vs official V1.1 === official len 5938 local len 8665 identical false official cmds: front,left,right,back,toplefthand,toprighthand,sitdown,lie …[截断,原长616]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:34）

Definitive: local gaits are bit-identical to the official V1.1 release. Let me verify the leg mapping and orientation evidence.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The local copy's control.html is a modified version of the official one (same commands, "sleep" = 回收 which in local is "回收机器狗"). Local added engine.html with 舵机1(右前腿), 舵机2(右后腿), 舵机3(左前腿), 舵机4(左后腿) labels.

Wait — important. In the local engine.html: 舵机1 = 右前腿, 舵机2 = 右后腿, 舵机3 = 左前腿, 舵机4 = 左后腿. That's the mapping. But is this the local author's own annotation, or from the original? The original's engine.html (360) doesn't have those labels. Let me check official V1.1's engine.html — it didn't exist in the v180 data dir (only control, index, setting). So the local engine.html is a NEW add by the local modifier — the servo debug console is an addition.

Now, for question 3: same vs mirrored numbers in the original.

In the original front():
- servo2.write(140); servo3.write(40)  → first pair: s2=140, s3=40 (opposite)
- servo1.write(40); servo4.write(140)  → second pair: s1=40, s4=140 (opposite)
- s2=90, s3=90
- s1=90, s4=90
- s1=140, s4=40 → s1/s4 mirrored
- s2=40, s3=140 → s2/s3 mirrored

So within each pair (s2,s3) and (s1,s4), the values are COMPLEMENTARY/mirrored: when one is >90 the other is <90. So the left and right legs of the same "axle" receive mirrored numbers.

Mapping from local engine.html: s1=右前腿 (right front), s2=右后腿 (right rear), s3=左前腿 (left front), s4=左后腿 (left rear). So:
- pair (s1,s4) = right-front & left-rear → mirrored (40 vs 140)
- pair (s2,s3) = right-rear & left-front → mirrored (140 vs 40)

Hmm, this is a diagonal pairing in that naming. But that's the local author's labels. Let me be careful — the local engine.html labels are the local modifier's; but they're plausible: on this 4-servo design each servo drives one leg, and the servos are mounted at board edges.

Actually wait. Let me reconsider. The comment in the GH R1 fork's front() says:
servo3.write(40); //左前向前旋转50度
servo2.write(140);//右后向前旋转50度

So GH R1 fork's comments say servo3 = 左前 (left front), servo2 = 右后 (right rear). Interesting: that matches local engine.html's s3=左前腿, s2=右后腿. And s1/s4: the fork's comment says "//-30C 1/4 servo1... servo4" implying 1 and 4 are the other diagonal pair.

Hmm, but that's the GH fork's own comment. In any case, the key answer to question 3: LEFT and RIGHT LEGS RECEIVE MIRRORED/COMPLEMENTARY NUMBERS (e.g., 140 vs 40) — NOT the same numbers. This is because the four servos are mounted with mirrored orientation (or the pairs are diagonally opposed), so an identical command would move legs in opposite directions.

Wait, I should be careful about the claim "mirrored mounting". Let me think about what the code implies. In the original front():
- Phase A: s2→140, s3→40 (both leave 90 in OPPOSITE directions), then s1→40, s4→140 (also opposite).
- Step 2: both back to 90.
- Phase B: s1→140, s4→40 (opposite), s2→40, s3→140 (opposite).

So one full cycle: (s2,s3) = (140,40) then (40,140); (s1,s4) = (40,140) then (140,40). So each pair is anti-symmetric around 90. This is consistent with a trot gait where diagonally opposite legs are in phase and the mirrored values reflect that the two legs of a pair are mounted mirrored, OR that the pairing is diagonal.

Hmm, actually with s1=右前, s2=右后, s3=左前, s4=左后:
Phase A (first half-step): s2 (right rear) =140, s3 (left front) =40. s1 (right front) =40, s4 (left rear)=140.
So: right-front=40, left-front=40 → SAME number for the LEFT and RIGHT FRONT legs! And right-rear=140, left-rear=140 → SAME for the two rear legs!

Interesting! So if the engine.html labels are right (s1=右前, s2=右后, s3=左前, s4=左后), then in front() the left and right legs of the same end receive the SAME number (40/40 for front, 140/140 for rear), and the mirrored numbers appear between the diagonals... no wait.

Let me redo. Phase A: s2.write(140) then s3.write(40). s1.write(40), s4.write(140).
- s1 = 右前 = 40
- s2 = 右后 = 140
- s3 = 左前 = 40
- s4 = 左后 = 140

So front legs (s1,s3) = 40, 40; rear legs (s2,s4) = 140, 140.

Phase B: s1.write(140), s4.write(40), s2.write(40), s3.write(140)
- s1 = 右前 = 140
- s2 = 右后 = 40
- s3 = 左前 = 140
- s4 = 左后 = 40
Front legs = 140,140; rear = 40,40.

So the SAME number goes to the left and right legs of the same axle/end. This means the servos are mounted MIRRORED (left/right mirrored), so that an identical write value makes the two legs swing in opposite (mirrored) directions — which is exactly what you want for walking. That is: left-side and right-side legs receive the SAME servo numbers, and the mirroring is achieved mechanically by mounting the servos mirrored.

Hmm, but which is it? The two hypotheses:
(a) Left/right servos mounted mirrored → same numbers produce mirrored leg motion. Then the code would send SAME numbers to left/right of the same axle.
(b) Left/right servos mounted identically → code must send complementary numbers (40 vs 140) to make them mirror.

From the code: front legs get 40,40 and rear legs get 140,140 in phase A. Under mapping s1=RF, s2=RR, s3=LF, s4=LR, that means hypothesis (a): same numbers for left/right. 

Hmm, but I derived that only from the local engine.html labels which the local modifier added. Let me double check that mapping is credible. Hmm — the local engine.html says 舵机1 (右前腿) → engine1 = pin 14 (GPIO14 = D5). Let me verify against the schematic PDF if possible... The 360 official code comments say "舵机1引脚" only, no leg names.

The GitHub fork (pluckypioneer/eda_robotR1) has comments in front(): "servo3.write(40); //左前向前旋转50度" and "servo2.write(140);//右后向前旋转50度". That assigns s3=左前, s2=右后 — consistent with local engine.html (s3=左前腿, s2=右后腿). Two independent sources agree on s2=右后 and s3=左前. By elimination s1 and s4 are 右前 and 左后 — local engine.html says s1=右前腿, s4=左后腿. 

So under this mapping:
- Phase A of front(): RF=40, RR=140, LF=40, LR=140 → the two right legs (RF=40, RR=140) differ; the two left legs (LF=40, LR=140) differ; and the pairs (RF,LF)=(40,40) and (RR,LR)=(140,140) match.

So front-left and front-right share the same value; rear-left and rear-right share the same value. That means in front(), left and right legs of the same pair receive the SAME servo numbers (not mirrored numbers), and mirroring must be mechanical (servos mounted mirrored left/right).

Hmm wait, but actually there's a subtlety. Are "front legs" a single pair that moves together, or is the design where each servo drives one leg about a "hip" axis such that left and right legs of the same axle need opposite rotation? For a walker, when the left-front leg swings forward, the right-front leg is planted; the LEGS alternate diagonally. Hmm, in the code, phase A moves front pair to one value and rear pair to the other value; then phase B reverses. Actually let me reconsider: the code moves s2/s3 first, then s1/s4 — these are the diagonal pairs (RR+LF) and (RF+LR) if the mapping is s1=RF, s2=RR, s3=LF, s4=LR.

So the "pair" in the code = diagonal pair: (s2=RR, s3=LF) and (s1=RF, s4=LR). In phase A: s2=140, s3=40 — for a diagonal pair, the two legs are on opposite sides and at opposite ends; they need MIRRORED values if the mirror axis is... hmm, for a diagonal pair moving in phase, the two legs' rotations relative to their own body frames are the same (both swing forward), so if servos are mounted mirrored left/right (as they must be for the two sides), the values would be... 

OK this is getting deep. The important, defensible facts I can state:
1. In the original front()/back(), each functional pair gets COMPLEMENTARY numbers: e.g. (s2=140, s3=40) and (s1=40, s4=140) in phase A; flipped in phase B. So they are NOT all the same number, and NOT all mirrored the same way — it's a two-phase pattern where each pair swaps between {140,40} and {40,140}.
2. Any specific leg-to-side mapping requires the schematic/labels. Local engine.html (author's own label) says s1=右前腿, s2=右后腿, s3=左前腿, s4=左后腿. Under that label, phase A gives front legs (s1,s3) both 40 and rear legs (s2,s4) both 140 → so left & right legs of the same end receive the SAME number, which implies servos are mounted mirrored left/right. And the code's "pair" (s2,s3)/(s1,s4) is the diagonal pair.

Hmm, but hold on: I should double-check whether the local engine.html mapping is inherited from somewhere in the original lineage rather than invented. Let me look for a "halfwidth/fullwidth" note... Actually, let me check the local project's other files (build_log.txt, README in include/, etc.) for any leg mapping. And let me check whether the PDF (official training docs) contains a leg-to-servo table. That PDF is 9.3MB — I extracted it. Let me try to extract text using soffice (LibreOffice) since python lacks pypdf. Or I could just try pip install pypdf... but sandbox. Let me use LibreOffice: soffice.com --headless --convert-to txt.

Let me do that. Also the 原理图 PDF might show "左前" etc. Let me look for leg labels in the schematic PDF (SCH_机器狗原理图.pdf).

Let me try soffice conversion.

Also I still need to nail down question 4: which value (<90 or >90) swings a leg forward. Evidence:
- GH fork comment: "servo3.write(40); //左前向前旋转50度" → left-front forward = 40 (<90). And "servo2.write(140);//右后向前旋转50度" → right-rear forward = 140 (>90). Interesting! So for left-front, <90 = forward; for right-rear, >90 = forward. That's consistent with mirrored mounting (opposite polarity for the two sides).

Hmm, but wait: the comment says "向前旋转50度" (rotate forward 50 degrees) for both 40 (from 90, that's -50) and 140 (from 90, that's +50). So the fork author's comments indicate: 左前 at 40 means forward; 右后 at 140 means forward. Since left-front and right-rear are diagonally opposite and both swing forward in phase A... Actually in the ORIGINAL phase A: s2.write(140), s3.write(40). Under mapping s3=左前, s2=右后: 左前=40 and 右后=140. Both "forward" per the fork's comments. Great, so this is consistent: for the left-front leg, <90 (40) = forward; for the right-rear leg, >90 (140) = forward. I.e., the sign convention differs per leg because of mirrored mounting.

Hmm, but careful: the fork's comments are from a derivative (pluckypioneer). Still, it's evidence, and it's the only explicit directional statement I've found. I should mark it as coming from a derivative fork's comments and note it as "the only explicit direction statement found".

Also, "toplefthand()" in the original: servo3.write(0) then 30 then 90. And toprighthand(): servo1.write(180) then 150 then 90. Under mapping s3=左前腿, s1=右前腿: raising the LEFT hand uses servo3 (left front) and uses values on the LOW side (0, 30); raising the RIGHT hand uses servo1 (right front) with values on the HIGH side (180, 150). This strongly supports the mirrored-mounting hypothesis: left-side leg swings "up/forward" with low values, right-side leg with high values. This is consistent and mutually corroborating with the local engine.html labels (s1=右前, s3=左前).

So question 3's answer: in the original, left-side and right-side legs of the same end receive the SAME number in front()/back() (per the mapping s1=RF, s2=RR, s3=LF, s4=LR: front pair both 40 then both 140; rear pair 140 then 40), and the values ARE mirrored/complementary between the front and rear pairs (40 vs 140). Hmm — the user asked: "whether in the original, the left-side and right-side legs receive the SAME servo numbers or MIRRORED/complementary numbers (e.g. 40 vs 140) in front()/back()."

So the answer has a wrinkle: whether it's "same" or "mirrored" depends on which pairing you call left/right. Let me lay out the facts precisely and let the numbers speak:
- front() phase A: s2=140, s3=40, then s1=40, s4=140.
- If s1=RF, s2=RR, s3=LF, s4=LR → front legs (s1,s3) = (40,40) SAME; rear legs (s2,s4) = (140,140) SAME; and the diagonals (s2,s3)=(140,40) and (s1,s4)=(40,140) are COMPLEMENTARY.
- So: within one axle (front or rear), left and right get IDENTICAL numbers; between the front axle and rear axle, the numbers are complementary (40 vs 140).
- This implies servos are mounted MIRRORED (left vs right), since identical numbers produce mirror-symmetric leg motion.

That's a clean, defensible answer — but I must flag that the leg-name mapping comes from labels added by others (local engine.html + the GH fork's comments), not from the original's own source (whose comments only say 舵机1..4).

Hmm, one more consideration: maybe the local engine.html labels were added by the local modifier and could be wrong. But the fork's comments independently agree on s2=右后, s3=左前. Two independent sources. I'll present as "consistent across two independent derivative sources; not stated in the original source itself".

Let me also try to get the official PDF text to look for a servo/leg table + calibration instructions, and the schematic PDF. Let me use soffice.

Actually — also worth checking: the local copy's own README/build_log/other files may say something about the leg layout. Let me grep. Also the local project has "build_log.txt" — check for clues about who modified it.

Let me run these.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nmkdir -p txtout\n\"/c/Program Files/LibreOffice/program/soffice.com\" --headless --convert-to txt:Text --outdir txtout \"att/EDA-Robot机器狗项目/EDA-Robot项目电子实训文档.pdf\" >/dev/null 2>&1\nls -la txtout/ 2>/dev/null | head", "description": "Convert official PDF to text via LibreOffice", "timeout": 240000}` → `total 32 drwxr-xr-x 1 user 197121 0 Oct 9 00:36 ./ drwxr-xr-x 1 user 197121 0 Oct 9 00:35 ../`

- 🔧 **Bash** `{"command": "cd \"/c/Users/UserX/Downloads/Robot dog 1.1\" && echo \"=== build_log tail ===\"; tail -30 build_log.txt; echo; echo \"=== include/README ===\"; cat include/README | head -20; echo \"=== gitignore ===\"; cat .gitignore", "description": "Check local provenance files"}` → `=== build_log tail === | ^~~~~~~~~~~~~~~~~~ src\main.cpp:738:22: note: declared here 738 | void ICACHE_RAM_ATTR handleButtonPress2() | ^~~~~~~~~~~~~~~~~~ src\main.cpp:842:79: warning: 'void handleButtonPress2()' is deprecated: Use IRAM_ATTR in place of ICACHE_RAM_ATTR to move functions into IRAM [-Wdeprecated-declarati …[截断,原长2523]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:35）

Local gaits are bit-identical to the official V1.1 release. Let me extract the official training PDF for the leg mapping and check local provenance files.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The LibreOffice conversion didn't produce a txt. Let me try different approach - use pdftotext if available, or use the venv python with installing pypdf. Actually, let me check if there is pymupdf or similar. Let me check what packages are in the ultralytics venv, and also check for the conda opencv python env.

Actually let me try a simpler approach — check if the wiki software page (HTML) contains the leg mapping info, which we already partly fetched. Let me search the software wiki page for front() explanation and leg mapping. Also the "训练营" training camp article.

Actually, the key question 3 and 4: "in the original, do left and right legs receive the SAME servo numbers or MIRRORED?" I can answer definitively from the code: in front(), servo2.write(140) and servo3.write(40) — these are complementary (sum = 180). servo1.write(40) and servo4.write(140). So mirroring exists by servo pairs.

And local engine.html labels: 舵机1 (右前腿), 舵机2 (右后腿), 舵机3 (左前腿), 舵机4 (左后腿). But this is the LOCAL engine.html which is a mod (not in original V1.1 zip — the V1.1 zip data/ has only control.html, index.html, setting.html — no engine.html!). Indeed, official V1.1 data/ listing showed only control.html, index.html, setting.html. So engine.html is a local addition. The leg labels in engine.html come from the local author. But wait — the 360 version had engine.html. Let me check the 360 version's engine.html for leg labels — earlier grep found no 腿 words in v360 engine.html either. Let me check its content.

Let me look at the 360 engine.html content directly.

Also, for orientation: front() comments in the 360 version say "//+30C 2/3 servo2.writeMicroseconds(1500 + speed + engine2offsetleftpwm)" — let me extract the comments from the 360 front() to understand which leg goes forward. And the offsets: engine1offsetleftpwm = -93 means the left-turn compensation for engine1... Actually these are 360-degree servo speed offsets.

Hmm, but for the 180-degree version, servos are position-controlled. The gait: front()  first moves servo2→140 and servo3→40 (i.e., >90 and <90 complementary). So one goes to 140, the other to 40. That's the mirrored/complementary relation.

Let me now check the official tutorial PDF for the servo mounting orientation description. Let me try harder to extract PDF text. Options:
- pip install pypdf in the venv (needs network, might work)
- Use the official 360-version comments
- Check wiki software page HTML for the front() explanation with leg names

Let me try the wiki software page text extraction, searching for "front" and "左前" etc. Earlier grep for 左前 in w2_eda-robot-software.html... I didn't grep that. Let me do it.

Also let's check the "训练营" (training camp) CSDN article "【智能机器狗实训营】【基础营】做个狗吧：基于ESP8266与SG-90舵机的低成本DIY机器狗硬件改造与实现" — that CSDN article might describe leg mapping. It 521'd before. CSDN blocks. Maybe try with different UA or via a mirror.

Let me first grep the wiki software page for leg names and front() discussion.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');\nlet s=fs.readFileSync('w2_eda-robot-software.html','utf8').replace(/<script[\\s\\S]*?<\\/script>/g,' ').replace(/<[^>]*>/g,' ').replace(/&nbsp;/g,' ').replace(/&amp;/g,'&').replace(/\\s+/g,' ');\nfor(const k of ['左前','右前','左后','右后','前腿','后腿','四足','抬左手','motion','步态','仿生']){\n let i …[截断,原长410]` → `## 四足 => 8 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 4.6.8 运动控制 ​ 与 …[截断,原长2428]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== 360 version front() with comments ===\"\nnode -e \"\nconst fs=require('fs');\nconst s=fs.readFileSync('v360/EDA-Robot/src/main.cpp','utf8');\nconst i=s.indexOf('void front()');\nconsole.log(s.slice(i, i+2400));\n\"", "description": "Extract 360 version front() with comments"}` → `=== 360 version front() with comments === void front() { //+30C 2/3 servo2.writeMicroseconds(1500 + speed + engine2offsetleftpwm); servo3.writeMicroseconds(1500 - speed - engine3offsetleftpwm); delay(500-runtime); servo2.writeMicroseconds(1500); servo3.writeMicroseconds(1500); //-30C 1/4 servo1.writeMicroseconds(1500 - …[截断,原长2151]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:36）

Let me extract the leg-mapping info from the official wiki and 360-version comments.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Very important finding. The official wiki says: "先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出" — legs 2 and 3 step forward, legs 1 and 4 push backward. And "4个电机的转动角度一致" (all four motors rotate through the same angle).

Now for the leg mapping question: In the local derivation, engine.html says servo1 = 右前腿 (right front leg), servo2 = 右后腿, servo3 = 左前腿, servo4 = 左后腿. But note that engine.html and the whole /servo1?angle= calibration interface is a local modification (not in official V1.1 — official V1.1 zip has no engine.html). Wait — official V1.1 data/ has control.html, index.html, setting.html only. So engine.html is local-only. The 360 version also doesn't have engine.html? Let me check: v360/EDA-Robot/data/ has control.html, engine.html, index.html, setting.html. Yes! The 360 version has engine.html. Let me check its labels.

Earlier my grep for 舵机 in v360 engine.html returned nothing. Let me check what v360's engine.html contains.

Also let me check the mirror question. In front(): servo2.write(140), servo3.write(40) at the same time — these are opposite numbers (140 vs 40 = mirror of 90). Then servo1.write(40), servo4.write(140). So the diagonally-opposite legs get the SAME value: servo2 & servo4 both 140 (one at a time in phase), servo1 & servo3 both 40. Hmm, let's be careful:

front():
- phase A: servo2=140, servo3=40
- phase B: servo1=40, servo4=140
- ...

So servo2 and servo4 get 140 (a pair) and servo1 and servo3 get 40 (another pair). That's a diagonal relationship if 2&4 are diagonal, or a "same side front/back" relationship.

Note the wiki says 2 and 3 step forward, 1 and 4 push back. In front() phase A, servo2=140 and servo3=40 simultaneously — those two legs move FORWARD at the same time (2 and 3). But they use different numbers (140 and 40)! That's the key insight: left-side and right-side legs receive MIRRORED/complementary numbers. servo2=140 vs servo3=40. So legs 2 and 3 are on opposite sides of the body, and to move both forward, one needs 140 and the other needs 40 → mirrored mounting.

Wait but the wiki also says "4个电机的转动角度一致" — the four motors rotate through the same angle (magnitude), i.e., 140-90 = 50 and 90-40 = 50, same 50-degree rotation. That's consistent: the magnitude is the same, but direction is mirrored (one is +50, the other is -50) due to mirrored servo mounting.

Hmm, actually in the 360 version, front(): servo2.writeMicroseconds(1500 + speed + offset), servo3.writeMicroseconds(1500 - speed - offset). So servo2 and servo3 rotate in OPPOSITE directions (one +, one -) while the comment says "+30C 2/3" both. So yes — servo2 and servo3 are on opposite sides, mounted mirrored, and to swing both forward they must receive opposite-direction commands. In the 180-degree version this becomes 140 vs 40.

So the answer for question 3: In front(), servo2=140 and servo3=40 (mirrored/complementary, not the same), and servo1=40, servo4=140. So the pairs receiving the SAME number are (2,4) and (1,3). In back() it's the opposite: servo3=140, servo2=40 first, then servo4=40, servo1=140.

So which pairs are diagonal? Let's think about it. In back(): servo3=140, servo2=40 then servo4=40, servo1=140. So pair (2,4)=... no: in back phase A: servo3=140, servo2=40; phase B: servo4=40, servo1=140. So pairs: (3,1) = 140, and (2,4) = 40.

Hmm, so in the 180 version, the same-number pairs are {2,4} and {1,3} — in front() it's 2&4=140 at different phases. Wait no: front() phase A: servo2=140, servo3=40. Phase B: servo1=40, servo4=140. So in phase A the same-value pair is 2 (140) and... nothing else at 140. Let me lay it out:

front() 180 version:
1. s2=140, s3=40
2. s1=40, s4=140
3. s2=90, s3=90
4. s1=90, s4=90
5. s1=140, s4=40
6. s2=40, s3=140
7. s1=90, s4=90
8. s2=90, s3=90

So steps 1 & 2 are the "swing forward" of legs (2,3) then (1,4); steps 5 & 6 are the "push back".

In step 1, s2=140 and s3=40 are the two legs that move forward together — with mirrored numbers.
In step 2, s1=40 and s4=140 also move together.
In step 5, s1=140 and s4=40 (moving in the other direction).
In step 6, s2=40 and s3=140.

So the same-number relationships: s2 and s4 both ever take 140 (in steps 1 and 2 respectively) — hmm, they take 140 in different steps. Which legs are "the same side"? 

Key: at any instant, the pair moving together is {s2,s3} or {s1,s4}, and within each pair the numbers are complementary (140 vs 40) — meaning those two servos are mirrored relative to each other.

{s2, s3} mirror pair; {s1, s4} mirror pair.

Now the local engine.html says: servo1 = 右前腿 (right front), servo2 = 右后腿 (right rear), servo3 = 左前腿 (left front), servo4 = 左后腿 (left rear).

Hmm — that gives {s2, s3} = right-rear + left-front = cross-diagonal (trot diagonal), and {s1, s4} = right-front + left-rear = the other diagonal. That's a classic trot gait! Diagonally opposite legs move together, which is exactly how a quadruped trots. And the mirrored numbers (140 vs 40) then make sense: the two diagonally-opposite legs are mounted in opposite orientations (since they're on opposite sides AND opposite ends... hmm, actually mirrored mounting is about left-right).

Hmm wait. But the wiki says legs 2 and 3 step forward together — with the local engine.html ORIENTATION (s2=right-rear, s3=left-front), legs 2 and 3 are diagonal → trot gait. That is physically correct for a walk/trot. Good, consistent.

But careful: is engine.html's leg mapping from the local modified copy or from the official 360 version? The local engine.html has the labels 舵机1 (右前腿) etc. Let me check whether the 360 official engine.html has those labels. My earlier grep for 舵机 in v360 engine.html returned nothing, which is suspicious. Let me look at the actual v360 engine.html content.

Actually, wait. The earlier grep output for v360 engine.html showed nothing at all — maybe the file uses different encoding (GBK?). Let me check.

Let me now verify:
1. v360 official engine.html content (does it have leg labels?)
2. Whether the local engine.html leg labels match the official or are local-added.
3. The 360-version's engine.html might be the source of the local engine.html.

Let me also determine the direction question: which value (<90 or >90) swings a leg forward. Evidence: wiki says legs 2 and 3 step forward using servo2=140, servo3=40. So for leg 2, >90 (140) = forward; for leg 3, <90 (40) = forward. That's the mirror. But since we don't know the physical mounting for each, we can say: in front(), the "forward swing" phase is s2=140/s3=40, and the "push back" phase is s2=40/s3=140. So relative to each servo's own mounting, the forward direction differs between mirrored pairs.

Hmm, but which is leg 1 and 4? front() step 2: s1=40, s4=140 moves with the same direction as step 1 (i.e., also forward-swing, per the 360 comment: "+30C 2/3" then "-30C 1/4" hmm).

The 360 comments say:
- "+30C 2/3" → s2 = 1500 + speed, s3 = 1500 - speed → both rotate +30 deg in their own frame? The comment means both legs swing in the "+30°" direction of their own mirror-flipped frame (i.e., both legs move the same physical direction).
- Hmm, actually "+30C" might mean "the leg goes +30 degrees forward"? For a 360 servo, 1500+speed and 1500-speed are opposite rotations. So legs 2 and 3 rotate in opposite directions physically — but since they're mounted mirrored, they both swing forward. Then "-30C 1/4" means legs 1 and 4 swing backward.

So the pattern: legs 2,3 = forward; legs 1,4 = backward; then continue trot.

Hmm wait, look at the sequence in 360 front():
1. +30C 2/3 (s2=+speed, s3=-speed) → legs 2,3 forward
2. -30C 1/4 (s1=-speed, s4=+speed) → legs 1,4 backward
3. 0C 2/3 (s2=-speed, s3=+speed) → legs 2,3 backward? (return to 0 with opposite motion) 
4. 0C 1/4 (s1=+speed, s4=-speed) → legs 1,4 forward
5. +30C 1/4 (s1=+speed, s4=-speed) → legs 1,4 forward
6. -30C 2/3 (s2=-speed, s3=+speed) → legs 2,3 backward
7. 0C 1/4 (s1=-speed, s4=+speed) → legs 1,4 backward
8. 0C 2/3 (s2=+speed, s3=-speed) → legs 2,3 forward

Hmm, this is a bit garbled but it's a continuous-motion gait for 360 servos (each writeMicroseconds(1500±) starts the servo rotating; writeMicroseconds(1500) stops it). For 180 servos, write() sets position.

Anyway. The key answers:

3. In the original front(), the pairs that move together get MIRRORED/complementary numbers: servo2=140 with servo3=40, and servo1=40 with servo4=140. Not identical. The pairs receiving the SAME number are (1,3) and (2,4) — i.e., diagonals per the local engine.html mapping — but they get them at different phases/times.

Hmm, careful. Let me re-examine. In front():
- s2=140 and s4=140 — the same value! s2 in step 1, s4 in step 2 (consecutive). Are these "the same side" or "diagonal"?
- s3=40 and s1=40 — the same value; s3 in step 1, s1 in step 2.

So the same-value pairs are {s1, s3} (both = 40 at the "back" instant, both = 140 at the "forward" instant in steps 5-6) and {s2, s4} (both = 140 in steps 1-2, both = 40 in steps 5-6).

Hmm no: in step 1, s2=140 and s3=40. In step 2, s1=40 and s4=140. So at any instant, the two legs moving get complementary values. But across the pair, legs 2 & 4 both get 140 (at different times), and legs 1 & 3 both get 40.

Since {2,4} receive identical numbers over the cycle and {1,3} receive identical numbers, and per local engine.html s2=right-rear, s4=left-rear → that would mean BOTH REAR legs get identical numbers! And s1=right-front, s3=left-front → both FRONT legs get identical numbers.

Hmm, that contradicts. Let's compute the actual motion: if s2 (right rear) and s4 (left rear) are mounted mirrored L/R, then the same numeric value produces opposite physical rotations — so the two rear legs move in opposite directions. In a trot, diagonal pairs move together, so right-rear + left-front move together (both = 140) and left-rear + right-front move together (both = 40). Since left-front (s3) and right-front (s1) both get 40... and right-rear (s2) and left-rear(s4) both get 140... 

Hmm. For a trot with mirrored L/R mounting:
- Diagonal A = {right-front, left-rear}: physically move together
- Diagonal B = {left-front, right-rear}: physically move together

If L/R are mirrored, then to move diagonal A in the same physical direction, right-front and left-rear need OPPOSITE numbers (140 vs 40). And with mapping s1=right-front, s4=left-rear, that's s1 vs s4 = 40 vs 140 — which matches step 2 (s1=40, s4=140)! 

And diagonal B = {left-front s3, right-rear s2}: step 1 has s2=140, s3=40 — opposite numbers. Matches!

So the local engine.html mapping (s1=RF, s2=RR, s3=LF, s4=LR) is CONSISTENT with the front() code IF left and right servos are mounted mirror-inverted. Both "moving together" pairs are diagonals, and within each diagonal the numbers are complementary because of the mirror.

Alternatively, if there were NO mirroring (all servos mounted identically), then s2=140 & s3=40 would move in opposite physical directions, and step 1 would be "one leg forward, one backward" — which would not be a trot. And the same-number pairs {s1,s3} and {s2,s4} would move in the same physical direction — meaning front-right + front-left together = both front legs together, which is a "bounding" gait, not walking. The wiki explicitly says 2 and 3 step forward together and 1 and 4 push back together — consistent with the mirror interpretation only if 2,3 are diagonal.

Hmm, but wait: if all four servos were mounted identically (no mirroring), then 2&4 with the same number = same physical direction. The wiki says 2 and 3 move forward together with values 140 and 40 — under no-mirroring those would be opposite directions, which contradicts "both forward". So the mirroring conclusion holds: LEFT/RIGHT servo mounting is mirrored, and within a moving pair the code uses complementary values (~40 vs ~140, symmetric about 90).

Actually hold on. Let me reconsider: 2 and 3 in the local mapping are right-rear and left-front (diagonal). Under mirrored L/R mounting, a diagonal pair needs complementary numbers to move the same way. ✓. Under identical mounting, a diagonal pair would need the SAME number to move the same way — but the code gives complementary. ✗. So mirrored mounting (left/right mirrored) is the right interpretation, and the wiki's "legs 2 and 3 step forward together" is consistent with the trot diagonal.

Good. But I should be careful: this is inference, and I should mark it as inference with the evidence. The strongest verbatim evidence is:
- wiki text: "先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出，然后再将2和3腿归位，最后将3和4腿归位即可" and "4个电机的转动角度一致" (all four motors rotate the same angle magnitude).
- front(): s2=140 & s3=40 simultaneously (complementary values), then s1=40 & s4=140 simultaneously.
- 360-version comments: "+30C 2/3" with s2=1500+speed, s3=1500-speed → opposite-direction commands for legs 2 and 3 which the author labels as the same motion phase.

So: within a moving pair, the numbers are mirrored/opposite; and this is deliberate mirroring for left/right mounting.

Now what about direction (<90 vs >90 = forward)? For s2 (right-rear per local engine.html), 140 = the forward-swing phase (step 1, paired with s3). For s3 (left-front), 40 = forward. Hmm, but that's for the "step out" phase; in step 6 they're reversed (s2=40, s3=140) which per wiki would be "return" (归位). Hmm, actually step 6 comes after step 5 (which is s1=140, s4=40 "push back"). In the 360 comments, steps 5-6 are "+30C 1/4" and "-30C 2/3", labeled "0C" for the rotations... The 180 version is essentially a sequence of discrete moves.

Let me be careful and describe: in front(), the first phase sets s2=140/s3=40 and the second sets s1=40/s4=140; the reverse phase (steps 5-6) sets s1=140/s4=40 then s2=40/s3=140.

Anyway, the honest answer to Q4: The original source code contains NO comments or docs about servo mounting orientation ("镜像"/"mirrored" never appears). The evidence for mirroring is indirect: the wiki's statement that legs 2&3 move forward together while the code commands them to complementary values, plus "4个电机的转动角度一致"... hmm, "4个电机的转动角度一致" means the rotation angle magnitude is the same for all four. 

Actually, thinking about it more: since the 360 version uses the same offset variables (engineXoffsetleftpwm/rightpwm) with different values per servo, and the front() uses +speed for s2 and -speed for s3 within the same phase, this is strong evidence of mirrored mounting of the left/right sides (or at least opposite rotation directions needed).

Let me also check whether there's an explicit statement anywhere. Let me look in the engine.html of the 360 official version — its labels may say which servo is which leg. My grep found nothing; let me actually dump the file.

Also I want to verify whether the LOCAL project's engine.html+servo endpoints are a local addition or from the official 360 version. The 360 official has engine.html — let me diff it with local engine.html.

Then I also want to quantify the local modifications for the user (they want to compare gait numbers, so mainly I need to assert gaits are identical).

Let me check the v360 engine.html content now.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nfile v360/EDA-Robot/data/engine.html\necho \"=== v360 engine.html (first 60 lines) ===\"\nhead -60 v360/EDA-Robot/data/engine.html\necho \"=== size ===\"; wc -c v360/EDA-Robot/data/engine.html \"C:/Users/UserX/Downloads/Robot dog 1.1/data/engine.html\"", "description": "Inspect official 360 engine.html"}` → `v360/EDA-Robot/data/engine.html: HTML document, Unicode text, UTF-8 text, with CRLF line terminators === v360 engine.html (first 60 lines) === <!DOCTYPE html> <html lang='en'> <head> <meta charset='UTF-8'> <meta name='viewport' content='width=device-width, initial-scale=1.0'> <title>EDA-Robot</title> <style> body { mar …[截断,原长1421]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:36）

Let me verify the 360 official engine.html leg labels and the local modifications.

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== official v360 engine.html: button labels + endpoints ===\"\nnode -e \"\nconst fs=require('fs');let s=fs.readFileSync('v360/EDA-Robot/data/engine.html','utf8');\nconsole.log('BUTTONS:',[...s.matchAll(/<button[^>]*>([^<]*)<\\/button>/g)].map(m=>m[1].trim()).join(' | '));\nconsole.log('CMDS:',[...new Set([...s …[截断,原长412]` → `=== official v360 engine.html: button labels + endpoints === BUTTONS: 减少 | 增加 | 减少 | 增加 | 减少 | 增加 | 减少 | 增加 | 减少 | 增加 | 减少 | 增加 | 减少 | 增加 | 减少 | 增加 | 减少 | 增加 | 电机左转90度 | 电机右转90度 CMDS: speeddown,speedup,engine1offsetleftpwmdown,engine1offsetleftpwmup,engine1offsetrightpwmdown,engine1offsetrightpwmup,engine2offsetleftpwm …[截断,原长740]`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== summary: distinctive local strings not in official V1.1 ===\"\nnode -e \"\nconst fs=require('fs');\nconst L=fs.readFileSync('local_main.cpp','utf8');\nconst O=fs.readFileSync('official_v11.cpp','utf8');\nconst keys=['回收机器狗','SB3j4zrxZ7nuRXv8v','12345678','LittleFS','drawXBMP(0, 0, 128, 64, dowhat)','/servo1 …[截断,原长412]` → `=== summary: distinctive local strings not in official V1.1 === 回收机器狗 local: 0 | officialV1.1: 0 SB3j4zrxZ7nuRXv8v local: 1 | officialV1.1: 0 12345678 local: 1 | officialV1.1: 0 LittleFS local: 18 | officialV1.1: 0 drawXBMP(0, 0, 128, 64, dowhat) local: 1 | officialV1.1: 1 /servo1 local: 1 | officialV1.1: 0 ICACHE_RAM_ …[截断,原长507]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:37）

Local `engine.html` (slider debug page) does NOT exist in the original — it is a modification. Let me confirm the local provenance and finalize.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Interesting - "回收机器狗" is 0 in local_main.cpp but present in local control.html. Let me confirm. Earlier: `data/control.html:189: <button class="button" onclick="sendCommand('sleep')">回收机器狗</button>`. Yes. Original has "回收" as button label. Local changed it to "回收机器狗".

Now let me finalize. I have everything. Let me do a final couple of searches to make sure I note the OSHWHUB page URL and also check whether there's a Bilibili video. Let me do a couple more quick searches to complete the 6-10 search requirement and check for the bilibili video.

Actually I've done many searches:
1. Bing "EDA-Robot" 机器狗 (irrelevant)
2. Bing EDA-Robot ESP8266 桌面机器狗 舵机 (irrelevant)
3. GitHub API search EDA-Robot → found pluckypioneer/eda_robotR1
4. GitHub API search 机器狗 esp8266 → found 4
5. GitHub API quadruped esp8266 servo
6. oshwhub search page
7. Sogou (blocked)
8. Baidu (blocked)
9. 360/so.com multiple (worked) - found oshwhub links
10. CSDN search API several queries
11. Bilibili API (returned HTML not JSON)
12. grep.app, searchcode, searx, mojeek, brave, ecosia, startpage (blocked/failed)

Let me do one last check on the bilibili video to be complete, then write the report.

Let me quickly check the CSDN article about the training camp ("做个狗吧") since it's paywalled, and check bilibili for an EDA-Robot video.

Actually, let me quickly try bilibili search properly.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nua=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36\"\n# bilibili needs cookie; try wbi-less search api\ncurl -s -m 25 -A \"$ua\" -H \"Referer: https://search.bilibili.com\" \"https://api.bilibili.com/x/web-interface/wbi/search/type?search_type=video&keyword …[截断,原长412]` → `200 31389 {"code":0,"message":"OK","ttl":1,"data":{"seid":"8967455470268965995","page":1,"pagesize":20,"numResults":1000,"numPages":50,"suggest_keyword":"","rqt_type":"search","exp_list":{"100010":true,"5500":t so7 200 https://www.bilibili.com/video/BV1DxfPYmEJS/ https://www.bilibili.com/video/BV1FaV66DEoQ/ https://www …[截断,原长395]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:37）

Let me do a final check for a Bilibili video and the training-camp article.

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');const j=JSON.parse(fs.readFileSync('bl2.json','utf8'));\nconst r=(j.data&&j.data.result)||[];\nconsole.log('count',r.length);\nr.slice(0,12).forEach(v=>console.log((v.title||'').replace(/<[^>]*>/g,''),'|',v.author,'| https://www.bilibili.com/video/'+v.bvid));\n\"", "description": "Pa …[截断,原长411]` → `count 20 【台湾清华大学】EDA电子设计自动化(一) (2026 李炯霆) | ctu1896 | https://www.bilibili.com/video/BV13CVm6xEuJ B站最全Robot Framework自动化测试框架搭建零基础入门到实战！ | 测试脚艺人 | https://www.bilibili.com/video/BV15b4y1f7s8 波形发生器立创EDA仿真 | 53166_mq | https://www.bilibili.com/video/BV1eq4y1z7T3 EDA-Robot复刻教程 | 丶月丶初 | https://www.bilibili.com/video/BV1ksK …[截断,原长1057]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:38）

Let me check the Bilibili results for the EDA-Robot video.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Found a Bilibili replication tutorial video: "EDA-Robot复刻教程" by 丶月丶初 (BV1ksKf6QEs6).

I have enough now. Let me do a final verification: the local project has an engine.html which is NOT in the original 180 V1.1. Let me check whether the local project also modified main.cpp in ways beyond that. And confirm whether local's servo2/servo3 in front() = the exact ordering of the original.

Actually wait — one important nuance. The task asks specifically:
3. State explicitly whether in the original, the left-side and right-side legs receive the SAME servo numbers or MIRRORED/complementary numbers (e.g. 40 vs 140) in front()/back().

From the original front():
- servo2.write(140), servo3.write(40) — servo2 and servo3 get COMPLEMENTARY numbers (140 vs 40)
- servo1.write(40), servo4.write(140) — servo1 and servo4 get COMPLEMENTARY (40 vs 140)
- Then servo1.write(140), servo4.write(40) — swapped
- Then servo2.write(40), servo3.write(140) — swapped

So within a pair, they're mirrored. And servo1/servo4 pair moves in the opposite phase from servo2/servo3.

Hmm, but the question is about "left-side and right-side legs". Given the local engine.html labels: 舵机1 (右前腿), 舵机2 (右后腿), 舵机3 (左前腿), 舵机4 (左后腿). So:
- servo1 = right-front, servo4 = left-back  → diagonal pair (1,4)
- servo2 = right-back, servo3 = left-front → diagonal pair (2,3)

So the pairing is DIAGONAL (trot gait), not left/right. That's a key finding. The diagonal pairs move in anti-phase.

Note: this leg labeling comes from the LOCAL engine.html (a modification), so I should mark it as uncertain for the original. But the wiki says "先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出" (first step legs 2 and 3 forward, then push legs 1 and 4 back) — this confirms 2/3 and 1/4 are the two diagonal pairs, consistent with a trot gait. It doesn't say which is left/right explicitly. Actually in a quadruped trot, 2&3 as one diagonal and 1&4 as the other is standard. Given local engine.html labels them 1=right-front, 2=right-back, 3=left-front, 4=left-back — that gives (2,3) = right-back + left-front = one diagonal, (1,4) = right-front + left-back = the other diagonal. Consistent.

Now for the direction: In front(), servo3 (left-front) writes 40 and servo2 (right-back) writes 140 first. Wiki says "先将机械狗的2和3号腿向前迈出" = legs 2 and 3 step FORWARD. So:
- servo3 (left-front): 40 = forward
- servo2 (right-back): 140 = forward

Then servo1 (right-front) writes 40, servo4 (left-back) writes 140 = legs 1 and 4 pushed BACK (向后蹬出).

Hmm, so servo1=40 → backward, and servo3=40 → forward. That's contradictory unless the servo mounting orientation is mirrored between the pairs. This is exactly the "mirrored mounting" question. 

So: for the front legs (servo1 = right-front, servo3 = left-front), a value < 90 gives... servo3=40 → left front leg forward; servo1=40 → right front leg backward. So the two front servos have mirrored mounting: the SAME number (40) moves them in OPPOSITE directions. Similarly for rear legs: servo2=140 → right-back forward; servo4=140 → left-back backward. So servo2 and servo4 are also mirrored relative to each other.

Wait, that means the mounting is mirrored left/right — the left-side servos and right-side servos are mounted as mirror images, so the same angle value produces opposite swings. That's an important conclusion. Let me double-check with the comment in the original Gitee front():

```
servo2.write(140); //右后向前旋转50度
servo3.write(40); //左前向前旋转50度
```
Hmm — hold on, that was from the GitHub copy `orig_main.cpp`. Let me recheck. In `orig_main.cpp` (github eda_robotR1):
```
void front(){
    servo3.write(40); //左前向前旋转50度
    servo2.write(140);//右后向前旋转50度
```
So the GitHub copy explicitly comments servo3 = 左前 (left-front) and servo2 = 右后 (right-back), and BOTH comments say "向前旋转50度" (rotate forward 50 degrees). servo3=40 and servo2=140 both = "forward". 

And then:
```
    servo1.write(40);
    servo4.write(140);
```
servo1 and servo4 with no comment. Then:
```
    servo1.write(140);
    servo4.write(40);
```
with comment "// 0C 1/4" style... let me look again. Actually in orig_main.cpp the comments are stripped. Let me re-read the Gitee original comments.

From the Gitee original front():
```
    servo2.write(140); //舵机2旋转至140度
    servo3.write(40);  //舵机旋转至40度
    delay(100);//延时100s
    servo1.write(40);  //内容同上
    servo4.write(140); 
```
Comments are minimal here. But the GitHub copy has the informative comments 左前/右后. That's a derivative but preserves the original's intent.

So conclusion on orientation: this is genuinely important. servo3 (left-front) = 40 → forward, servo2 (right-back) = 140 → forward. So for these two legs (which are on opposite sides AND opposite ends), forward is achieved by opposite values. This is consistent with either (a) mirrored left/right mounting, or (b) the leg geometry being point-symmetric.

Given the wiki says legs 2 and 3 step forward and 1,4 push back, and 2/3 are on opposite diagonals — if mounting were all identical, then all four legs would swing the same absolute direction for the same number, and you couldn't have 2 forward + 1/4 backward with 2&3 using opposite values. So the mounting must be mirrored for at least some servos.

Let me reason more concretely. A typical quadruped with 4 servo horns each rotating a leg in the vertical plane: each servo drives ONE leg. If all 4 servos were mounted identically (same orientation), then a value >90 would rotate all 4 legs the same angular direction. In front(), we need legs 2,3 forward and legs 1,4 backward. With 2&3 using 140/40 respectively and 1&4 using 40/140 respectively — the values are: 2=140, 3=40, 1=40, 4=140. So legs 2 and 4 get 140, legs 1 and 3 get 40 when stepping... 

Hmm, at the first step: 2=140, 3=40 (both forward), then 1=40, 4=140 (both backward). So:
- Legs with value 140: leg2 (forward), leg4 (backward)
- Legs with value 40: leg3 (forward), leg1 (backward)

So value 140 → forward for leg2 but backward for leg4. And 40 → forward for leg3, backward for leg1. So leg2 and leg4 are mounting-mirrored relative to each other; leg1 and leg3 are mounting-mirrored relative to each other.

If leg1=right-front, leg4=left-back, leg2=right-back, leg3=left-front:
- Mirror pairs: (leg1 right-front, leg4 left-back) and (leg2 right-back, leg3 left-front).

Interesting — that's not a simple left/right mirror; it's a diagonal mirror (point symmetry about the body center). That is actually the classic arrangement for these cheap 4-servo dogs: the servos are mounted on the two long sides, and the legs are diagonally symmetric.

Hmm, but I should be careful. I shouldn't over-claim. Let me be precise about what's certain vs. inferred:

CERTAIN (from source):
- front() numbers are exactly as listed
- The wiki states: "先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出，然后再将2和3腿归位，最后将3和4腿归位即可" (first legs 2 & 3 step forward, then legs 1 & 4 push back, then 2&3 return, then 1&4 return)
- So within the walking sequence, legs {2,3} are one phase group and {1,4} are the other — diagonal pairs.
- In front(), servo2=140 pairs with servo3=40 (both "forward"), and servo1=40 pairs with servo4=140 (both "back"). So the same numeric value (e.g., 140) means "forward" for servo2 but "backward" for servo4.

INFERRED (mark as uncertain):
- Left/right leg assignment: only from the LOCAL engine.html (a modification, not the original) which labels 舵机1=右前腿, 舵机2=右后腿, 舵机3=左前腿, 舵机4=左后腿. The originals' HTML doesn't have this label. The GitHub derivative comment (左前/右后 for servo3/servo2) corroborates servo3=left-front and servo2=right-back, which matches the local engine.html. So it's likely correct, with corroboration from two independent derivative sources.
- Whether "less than 90" or "greater than 90" swings a leg forward: depends on the leg. For servo3 (left-front) and servo2 (right-back): forward = 40 and 140 respectively, so no single answer. I should state this precisely.

Let me also verify: is `int speed = 300` present in the 180 version? Let's check. The local copy has `int speed = 300;` Let me check official V1.1. Also check the local copy's servo2/servo3 write order vs original — already confirmed identical.

Let me also grab the local's engine.html + confirm it's the one difference (the /servoN endpoints). And verify how big the local diff is.

Let me do these final checks and then write the report. I also want to double check whether the local copy's `front()` sequence is truly character-identical including comments. Let me get an exact raw diff of the two front() functions.

</details>

- 🔧 **Write** `{"content": "const fs = require('fs');\nconst S = 'C:/Users/UserX/AppData/Local/Temp/s4s/';\n\nfunction extract(src, name) {\n const re = new RegExp('void\\\\s+' + name + '\\\\s*\\\\(\\\\s*\\\\)\\\\s*\\\\{');\n const m = re.exec(src);\n if (!m) return null;\n let i = m.index + m[0].length - 1, d = 0;\n for (; i < src.length; i++) {\n if (src[i] === '{') d++;\n else if (src[i] = …[截断,原长402]` → `File created successfully at: C:\Users\UserX\AppData\Local\Temp\s4s\verify.js (file state is current in your context — no need to Read it back)`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:38）

Let me do a final exact character-level verification of the gait functions and the local modifications.

- 🔧 **Bash** `{"command": "cd /c/Users/UserX/AppData/Local/Temp/s4s && node verify.js", "description": "Run final exact verification"}` → `### EXACT character-identical test (official V1.1 vs LOCAL MODIFIED) ### front exact-identical: NO | len 567 vs 552 back exact-identical: NO | len 530 vs 510 left exact-identical: NO | len 901 vs 879 right exact-identical: NO | len 917 vs 892 sitdown exact-identical: NO | len 138 vs 133 lie exact-identical: NO | len 23 …[截断,原长1529]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The differences in lengths are just comments/whitespace. My earlier normalized comparison showed the sequences were identical. Let me confirm by printing both normalized side by side to be precise — the servo numbers and delays are identical, only comments differ. Let me do a final check on trailing `delay(100)` in left()/right() and verify the sequence identity once more, and produce the exact servo number lists.

Note dosleep length differs (166 vs 112) — official has trailing spaces. Let me check the exact content of both dosleep.

Let me get the official V1.1 dosleep, back, left, right, lie, toplefthand, toprighthand verbatim so I can report exactly.

</details>

- 🔧 **Write** `{"content": "const fs = require('fs');\nconst S = 'C:/Users/UserX/AppData/Local/Temp/s4s/';\nfunction extract(src, name) {\n const re = new RegExp('void\\\\s+' + name + '\\\\s*\\\\(\\\\s*\\\\)\\\\s*\\\\{');\n const m = re.exec(src);\n if (!m) return null;\n let i = m.index + m[0].length - 1, d = 0;\n for (; i < src.length; i++) {\n if (src[i] === '{') d++;\n else if (src[i] === …[截断,原长402]` → `File created successfully at: C:\Users\UserX\AppData\Local\Temp\s4s\verify2.js (file state is current in your context — no need to Read it back)`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:39）

Lengths differ only in comments/whitespace. Let me confirm the sequence identity and capture the official V1.1 text verbatim.

- 🔧 **Bash** `{"command": "cd /c/Users/UserX/AppData/Local/Temp/s4s && node verify2.js 2>&1 | head -130", "description": "Verify token-level gait identity"}` → `=== TOKEN STREAM IDENTITY (servo writes + delays only, in order) === front V1.1==LOCAL: IDENTICAL | gitee==LOCAL: IDENTICAL | tokens 23 back V1.1==LOCAL: IDENTICAL | gitee==LOCAL: IDENTICAL | tokens 23 left V1.1==LOCAL: IDENTICAL | gitee==LOCAL: IDENTICAL | tokens 31 right V1.1==LOCAL: IDENTICAL | gitee==LOCAL: IDENTIC …[截断,原长2425]`

- 🔧 **TodoWrite** `{"todos": [{"content": "Recon local project + extract distinctive strings", "priority": "high", "status": "completed"}, {"content": "Run 6-10 web searches (CN + EN) across engines", "priority": "high", "status": "completed"}, {"content": "Fetch most promising candidate pages", "priority": "high", "status": "completed"}, {"content": "Compare original vs local gait code, report v …[截断,原长412]` → `{"oldTodos":[{"content":"Recon local project + extract distinctive strings","status":"completed","priority":"high"},{"content":"Run 6-10 web searches (CN + EN) across engines","status":"completed","priority":"high"},{"content":"Fetch most promising candidate pages","status":"completed","priority":"high"},{"content":"Co …[截断,原长1123]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:40）

Verified: the local gait numbers are token-identical to the official original. Let me update the todo list and finalize.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Let me write my final report. Let me get the remaining verbatim functions printed for the report — I have them in the file already. Let me quickly read the rest of the verify2 output to have dosleep and others.

Actually I already have from the earlier Read of GITEE_ORIGINAL_180V11_gaits.txt the verbatim text of all the functions, which matches the official V1.1. Let me get the remaining ones (sitdown, lie, toplefthand, toprighthand, dosleep) which I already have from that file read.

Let me produce the final report.

Key facts:
1. Original project: 立创开源硬件平台 (oshwhub) `https://oshwhub.com/course-examples/bot-dog` — "EDA-Robot机器狗", professional version, GPL 3.0, created 2024-11-29. Companion code repo: `https://gitee.com/JasonYANG170/eda-robot`. Official wiki docs: `https://wiki.lceda.cn/zh-hans/course-projects/smart-internet/eda-robot/eda-robot-introduce.html`. Bilibili replica tutorial: BV1ksKf6QEs6 (that's a replica, not original).

2. Verbatim original bodies — official 180-degree V1.1 (attached zip "EDA-Robot(180度舵机版)_V1.1.zip"), which is IDENTICAL to the Gitee main branch.

3. Left/right legs: same servo numbers across both sides? Let me check that carefully. In front(), the values used are 140 and 40 on all four servos — same magnitude numbers, and the ratio pattern is: on one phase, servo2=140/servo3=40 and servo1=40/servo4=140. So it's a "same value set, phase-offset" arrangement rather than mirrored 40 vs 140 per side. Actually, let's be careful and precise:

front():
- servo2=140, servo3=40 (diagonal pair 2/3)
- servo1=40, servo4=140 (diagonal pair 1/4)

So in the same phase, servo2 and servo4 get 140 while servo3 and servo1 get 40. That means servo1 & servo3 get 40 while servo2 & servo4 get 140. This is a diagonal pairing (1&3 vs 2&4) not left/right pairing.

The local engine.html (a local addition, not original) says servo1=右前腿 (right front), servo2=右后腿 (right rear), servo3=左前腿 (left front), servo4=左后腿 (left rear).

Under that mapping: phase 1 → 右后(140), 左前(40); phase 2 → 右前(40), 左后(140). So the left/right legs receive the SAME NUMBER VALUES (both 40 and 140 appear on both sides) but MIRRORED/complementary within a phase: on the same diagonal, one side 40 and the other 140. So the diagonal pairs 1&3 (right-front & left-front) and 2&4 (right-rear & left-rear) are actually... wait let me redo.

Under the local engine.html mapping:
- servo1 = 右前腿 (right front), pin 14
- servo2 = 右后腿 (right rear), pin 16
- servo3 = 左前腿 (left front), pin 12
- servo4 = 左后腿 (left rear), pin 13

front() step 1: servo2=140 (right rear), servo3=40 (left front) — that's a diagonal pair. 
step 2: servo1=40 (right front), servo4=140 (left rear) — the other diagonal.

So left-front=40 and right-front=40 both occur, but at different times. In the same instantaneous phase, right-rear=140 & left-front=40; right-front=40 & left-rear=140. So each diagonal has one leg at 40 and the opposite at 140 — mirrored/complementary numbers within a diagonal pair. Both left and right sides get both 40 and 140 at different times.

Important: so the answer to Q3 is: they are MIRRORED (complementary) in the sense that within each diagonal pair one leg goes to 40 while the other goes to 140; the same magnitude set {40,140} is used on both sides, not a "40 vs 140 always on left vs right" rule. Precisely: at any instant, legs in the same diagonal get opposite values (40 vs 140), and the two diagonals are 180° out of phase. Which means the left legs never receive a separate value range from the right legs — the code does not use distinct left/right constants. But the mounting is such that value <90 on one side means forward, and on the diagonal opposite, >90 means forward... Hmm, I should be careful.

Actually, let's think about it as the original documentation explains: "先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出" — "first step legs 2 and 3 forward, then push legs 1 and 4 backward". So legs 2 and 3 move forward when they get 140 and 40 respectively... Hmm, that says "2和3号腿向前迈出" while the code sets servo2=140, servo3=40. So for leg 2 (servo2), forward = 140 (>90); for leg 3 (servo3), forward = 40 (<90). That's the mirroring! Servo2 and servo3 are the diagonal pair; they move the same direction (forward) with OPPOSITE numbers because they are mounted mirrored.

Then "再将1和4腿向后蹬出" (then push legs 1 and 4 backward) while code sets servo1=40, servo4=140. So leg 1 backward = 40 (<90), leg 4 backward = 140 (>90). Again mirrored: servo1 & servo4 move together but with opposite numbers.

So the mirroring pairing is: servos 1&4 are on the same side-pair (or same diagonal) and 2&3 on the other. Let me determine which diagonal. Let's reason from front() phase 3+4: servo1=140, servo4=40 (legs 1 and 4). And the doc says this is the "1和4腿向后蹬" phase — legs 1 and 4 push backward. Then the last part: servo1=90, servo4=90, servo2=90, servo3=90 returning to center.

Then in the loop: servo2=40, servo3=140 with doc: hmm the second half of front is the second half-cycle where the diag pairs swap.

OK so the pairing is: {1,4} move as one group (the "front" pair? or one diagonal), {2,3} as the other.

With the local engine.html labels: servo1=右前, servo4=左后 → {1,4} = right-front + left-rear = a diagonal! And servo2=右后, servo3=左前 = the other diagonal. So {2,3} and {1,4} are the two diagonals. That's consistent: diagonal pairs move together (trot gait), with mirrored values within each pair.

So:
- Q3 answer: Within each diagonal pair, the two legs receive MIRRORED/complementary numbers (one 140, the other 40) — because they are mounted mirrored. The same two numbers 40 and 140 are used on all four servos; there is no "left always 40 / right always 140". So in front(), the left-side and right-side legs receive the SAME set of numbers, but each specific leg gets the "mirrored" one relative to its diagonal partner.

- Q4: servo mounting: The original hardware uses 4 identical SG90 servos with the same orientation, held in 4 limiting slots in the bottom shell (文档: 底壳部分为舵机设计了4个限位槽). Hmm — the wiki says the bottom case has 4 limit slots for the servos, and "将所有脚固定到相同角度" (fix all feet to the same angle) for calibration. That suggests all four servos are mounted identically (all same orientation), not mirrored! But then how does the code work with mirrored values?

Hmm. This is important. Let me think about the geometry. Actually for a 4-legged robot where each servo rotates a leg about a horizontal axis perpendicular to the body's long axis... Actually, in this robot, each servo drives a "foot" that swings. If all four servos are mounted with the same orientation (arm pointing in the same direction), then the same angle value moves all four legs in the same rotational direction (e.g., all forward or all backward). To walk, you'd want diagonal pairs to move in opposite rotational directions (one pushes back, the other swings forward). 

Hmm, so with all servos mounted identically, servo1=40 (i.e., counterclockwise) makes leg1 rotate one way. servo4=140 makes leg4 rotate the other way. If for leg 1 rotating "one way" = forward, and for leg 4 we want forward too, we'd need the same value. But the code gives opposite values... unless the legs point in opposite directions, i.e., legs 1 and 4 point outward in opposite directions so the same rotation makes them move in opposite linear directions.

Hmm. Actually for this kind of "leg swings about a horizontal axis" design: front legs and rear legs point in opposite directions from the body. Wait no — in this robot the 4 legs are at the 4 corners.

Let me be careful. I know from the calibration instructions: "1.将所有脚固定到相同角度。" (Fix all feet to the same angle) then "点击一次'电机左转90度'" and "找到转动大于90度或小于90度的脚，进行舵机补偿" — find the feet that rotate more or less than 90 degrees and compensate. This is about SPEED calibration for 360° servos (making all four rotate at the same rate), not about mounting mirroring. It says all feet are fixed to the same angle initially.

Hmm, "将所有脚固定到相同角度" means physically setting each foot at the same angle relative to its servo body. This implies the servos are mounted identically and feet are set identically. Then rotating all servos by the same amount would move all feet the same rotational direction.

So then to walk, for a "trot" gait you want diagonal pairs to swing in opposite directions. Hmm, wait, no. Let's think again: In a trot, at any moment, diagonal pair A swings forward while pair B pushes back. If both pairs are mounted identically, "swing forward" for the front leg of pair A and "push back" for the rear leg of pair B — hmm, these are the same rotation direction if the legs' geometry is such that rotation direction maps to opposite linear directions for front vs rear.

Actually here's the thing: this is the classic "4 legs all rotate about parallel horizontal axes" design where each leg is like a crank. Let's set up: the body has left and right sides. Each leg is a rod extending sideways/outward from a servo horn that rotates about a horizontal axis parallel to the body's long axis... no.

I think I should be careful and mark as uncertain. The key evidence:
- All 4 servos: same model SG90, all mounted in the 4 limit slots in the bottom shell.
- The code contains no per-servo polarity constants (no offsets in the 180 version), and it uses symmetric values 40/140 around 90 on all four servos, with diagonal pairs getting opposite values.
- The original documentation (360° version write-up) says: angle 1500µs is center; "4个电机的转动角度一致" (the four motors rotate by the same angle).

That phrase "4个电机的转动角度一致" (all 4 motors rotate through the same angle) + the mirrored numeric values strongly implies all four servos are mounted identically (same orientation), and the opposite numbers (40 vs 140) are what produce opposite swinging directions for the legs of a diagonal. Hmm, but if the rotation angle is the same magnitude and opposite sign, then the legs must be arranged such that one leg's servo rotating +50° swings it forward while its diagonal partner's servo rotating -50° also swings its leg forward. 

Given front legs and rear legs: for a walking machine with all servos mounted the same way (e.g., all horns pointing "outward" along the body's X axis, rotation about the X axis... 

Let me just look at the geometry differently: In this design, the "foot" is a flat piece attached to the servo horn. Looking at the 3D files: foot.stl. The leg is a single segment (no knee). Each servo rotates its leg in a plane perpendicular to the body's long axis? If servos are mounted with rotation axes parallel to the body's lateral (Y) axis, then rotating a leg moves it forward/backward (in the X direction) — that's what we want for walking. Front-right leg at servo1: rotating to 40 vs 140 moves the foot forward or backward in X. For the left-front leg at servo3: rotating to 40 vs 140 moves its foot to the opposite X direction IF the servo is mounted mirrored (rotation axis reversed), or the same X direction if mounted identically.

Given the code gives servo2=140 & servo3=40 together (for the diagonal {2,3} = right-rear & left-front), and the doc says legs 2 and 3 "向前迈出" (step forward) together: leg2=140→forward, leg3=40→forward. Since leg 2 and leg 3 are on OPPOSITE sides (right-rear and left-front), and they move forward with opposite numeric values, this means the left-side servos and right-side servos are mounted MIRRORED relative to each other (or equivalently, the legs point in opposite directions). Hmm, but wait, they are also on opposite ends (front vs rear). Ugh, {2,3} = right-rear + left-front is a diagonal, so it mixes both side and end.

Hmm OK. Let me check: which pairs move together? From front(): first half, {2,3} then {1,4}; second half, {1,4} then {2,3}. And the doc says the diag pairs are "2和3号腿" and "1和4腿". So {2,3} and {1,4} are the diagonals. With local labels: 1=右前(RF), 2=右后(RR), 3=左前(LF), 4=左后(LR). So {1,4} = RF+LR (one diagonal) and {2,3} = RR+LF (the other diagonal). ✓ These are the standard diagonals.

Now within diagonal {2,3}: 2=RR goes 140 = forward, 3=LF goes 40 = forward. So for the right-rear leg, >90 = forward; for the left-front leg, <90 = forward.
Within diagonal {1,4}: 1=RF goes 40 = backward, 4=LR goes 140 = backward. So for right-front, <90 = backward (i.e., >90 = forward); for left-rear, >90 = backward (i.e., <90 = forward).

Hmm, that's inconsistent: RR: >90 forward; RF: >90 forward. Both right legs: >90 = forward. LF: <90 = forward; LR: <90 = forward. Both left legs: <90 = forward. 

So the pattern is: on the RIGHT side of the body, value >90 (140) swings the leg forward; on the LEFT side, value <90 (40) swings the leg forward. That's exactly mirroring by side! And the front/back distinction doesn't matter — all right-side servos share the same polarity, all left-side servos share the same polarity, and they're opposite.

Wait, but that's weird for a design where all servos are mounted "the same" in the bottom shell with feet set to "the same angle". Hmm. But actually it's consistent: if the left servos are mounted mirrored relative to right servos (so their rotation axes point in opposite directions along Y), then the same value would move left and right legs in opposite X directions; to get both to move forward you need mirrored values. Hmm no — if the axes point in opposite directions (mirrored mounting), then the SAME numeric value produces opposite physical swing directions, meaning to make both legs go forward you need... the same value? Let's compute: servo value v maps to horn angle θ = (v-90)*k where k>0 (same for all since same model). Physical rotation direction: right servo rotates +θ about +Y (say); left servo mirrored rotates +θ about -Y, which in world coords is -θ about +Y. So the linear motion of the foot: for right leg, displacement along X = f(θ); for left leg, displacement along X = f(-θ) = -f(θ) roughly (for the same mounting position). So same value v gives opposite X motion for left vs right → therefore, to move both legs forward (same X direction) you need mirrored values (v and 180-v). ✓ Consistent!

But wait — is the axis +Y for one and -Y for the other, i.e. are left servos physically flipped 180° about the vertical axis? That's the "mirrored" mounting. Hmm, but the calibration instruction says "将所有脚固定到相同角度" (set all feet to the same angle) which might just mean set all feet to point in the same direction relative to their servo (before tightening the screw), which for mirrored servos means the feet point in mirrored physical directions. Hmm, ambiguous.

Hmm, hold on. Actually maybe the axes are parallel and identical but the legs extend in opposite directions... no, all four legs point outward.

Hmm, let me look for more direct evidence. Actually, there's a much better source: the 360-degree version's front() comments use "+30C", "-30C", "0C" annotations which come from a clock-face convention, and the offsets engineXoffsetleftpwm/engineXoffsetrightpwm. The 360 version has NO sign constants per servo either — it uses ±(speed + offset) with the + and - chosen explicitly per servo per phase. Notice: servo1 in "+30C 1/4" phase: 1500 - speed - engine1offsetrightpwm (negative direction), and in "0C 1/4": 1500 + speed + engine1offsetleftpwm. So servo1 gets both signs. And in the "1/4" group, servo1 goes negative while servo4 goes positive (mirrored), and vice versa. So indeed within a diagonal group ({1,4}), the two servos always receive OPPOSITE directions of rotation. Same for {2,3}. This is consistent with left/right mirroring.

And crucially, is it mirrored by left/right or by front/rear (i.e., by diagonal)? Since servos 1&3 are the "front" pair in one diagonal-sense... hmm: {1,4} is RF+LR, {2,3} is RR+LF. Within {1,4}: servo1 (RF) and servo4 (LR) opposite signs. Within {2,3}: servo2 (RR) and servo3 (LF) opposite signs. So the "opposite-sign" pairs are (RF,LR) and (RR,LF) — each is a diagonal, i.e., one front leg + the opposite rear leg. That means the opposite-sign pairing mixes a left and a right leg. So the mirroring is left/right (RF vs LR is right vs left, RR vs LF is right vs left). ✓ Consistent with my conclusion: left/right are mirrored.

So: left servos mounted mirrored w.r.t. right servos. Good, and the same numbers are used, just mirrored/complementary (40 vs 140), consistent with "same-magnitude, opposite-sign" rotation.

But careful: the local engine.html (a local modification, not in the original) provides the leg mapping. I should mark that mapping as coming from the local copy and note that I could not independently verify it from the original docs (the original wiki doesn't name the legs; it uses "2和3号腿"/"1和4腿"). Actually, the original DOES give the pairing {1,4} and {2,3} as diagonals.

Hmm, one more check: is the local engine.html mapping plausible? servo1 = 右前腿 (right front) with pin 14 (GPIO14/D5), servo2 = 右后腿 (RR) pin 16, servo3 = 左前腿 (LF) pin 12, servo4 = 左后腿 (LR) pin 13. Hmm, that gives {1,4} = RF + LR — a diagonal ✓, and {2,3} = RR + LF — the other diagonal ✓, and left/right mirroring ✓ ({1,4} = right+left; {2,3} = right+left). Consistent with the original code's semantics. But since engine.html isn't in the original, this mapping is the modifier's (or another derivative's) contribution. Hmm. I should mark it as "from the local modified copy / likely from a derivative" and uncertain whether original uses those leg names.

Actually wait. Let me reconsider: I could verify by checking whether the original's control.html had a "dowhat" drawXBMP and what the local additions were. Not needed.

Let me also double check "回收机器狗" is not in the original control.html (it's "回收" in the original) — confirmed: original button label is "回收", local is "回收机器狗". Good — this confirms the local copy was modified (or descended from a modified fork).

Additional useful info for the user's comparison purpose:
- Original (V1.1, 180°) gait functions are token-identical to the local copy's — so the servo numbers were NOT modified. The local modifications are elsewhere: LittleFS instead of SPIFFS, buttons on GPIO2/GPIO15 kept, added engine.html servo debug console + /servo1../servo4 endpoints, AP password "12345678" instead of empty, hardcoded weather key "SB3j4zrxZ7nuRXv8v", IRAM_ATTR instead of ICACHE_RAM_ATTR, comment/style changes, and "回收机器狗" label.
- Note the difference: the local uses `dosleep()` where the local `sleep` command maps to dosleep; original 360 version has `dosleap()` (typo) — hmm, the 180 version has dosleep? Let me check. In the Gitee/official V1.1, the function is named... I extracted 'dosleep' successfully from gitee_main.cpp and official_v11.cpp (dosleep found YES). Wait, earlier grep of gitee showed "void dosleap()" at line 533 — that was for the OTHER file (orig_main.cpp = GitHub eda_robotR1). Let me recheck: earlier "grep -n 'void '" on gitee_main.cpp showed: ... 674:void dosleep(). Yes gitee has dosleep. And orig_main.cpp (GitHub) had dosleap at 533. OK good.

Let me double check the exact body of original dosleep: 
```
void dosleep()
{
    servo1.write(0);                   
    servo3.write(180);                 
    servo2.write(180);                 
    servo4.write(0); 
}
```
Hmm, this text came from GITEE_ORIGINAL_180V11_gaits.txt which I read. ✓. Note the order: servo1=0, servo3=180, servo2=180, servo4=0. Local: servo1=0, servo3=180, servo2=180, servo4=0 — from my earlier read of local main.cpp at line 689-695: 
```
void dosleep()
{
    servo1.write(0);
    servo3.write(180);
    servo2.write(180);
    servo4.write(0);
}
```
✓ identical.

Note: verify.js said dosleep official len 166 vs local 112 (whitespace/comments differ) but token stream IDENTICAL. Good.

Also should mention attach lines: `servo1.attach(engine1, 500, 2500);` etc. — identical in both. And engine pins 14/16/12/13.

Also the local `speed = 300` and `runtime` — the local has `int speed = 300;` but no runtime and no offsets; the original 180 V1.1 also has speed=300? Let me check: verify.js said official V1.1 offset vars = 0 and local = 0. And "speed: int speed = 300;" was found in local. Did official V1.1 have speed? Let me check quickly... I didn't confirm. Let me do a quick check to be accurate.

Actually let me run one more quick command to check official V1.1's speed/servo pin definitions and whether there's an engine.html. Also confirm the local servo pin numbers vs original (14/16/12/13 same).

Also, I want to double-check the claim about the ORIGINAL project's date/author and the GPL 3.0 license, and that the oshwhub project IS the original (created 2024-11-29, updated 2025-11-19), by 立创 course-examples account. The wiki is official 嘉立创EDA training material ("智能机器狗实训营"). The Gitee repo is credited on the oshwhub page as "代码仓 Gitee https://gitee.com/JasonYANG170/eda-robot".

Hmm, one caveat: the oshwhub project page is under "course-examples" which is the official 立创 course account, so the original author may be a JLC staff member / the training camp creator (JasonYANG17 / JasonYANG170). The GitHub repo pluckypioneer/eda_robotR1 (created 2025-07-25) is a derivative with the README saying "项目基于嘉立创 EDA 开发平台,项目来源于嘉立创平台原作者" — i.e., it's a re-post/derivative. Its gait numbers DIFFER slightly (e.g., left/right swapped order, toplefthand 0→90 without the 30, toprighthand 0 instead of 180, lie order 180,180,0,0) so it's a separate variant. Wait, careful — orig_main.cpp (from GitHub eda_robotR1) had gaits that differ from the original. Let me look: its front is servo3=40, servo2=140 (order swapped), left() has values 100/60/140/40 (i.e., the mirrored variant), toplefthand 0→90 (no 30), toprighthand 0→90 (instead of 180→150). Hmm interesting: that derivative's left() looks like it swapped the roles: it uses 100/60/140/40 for servos 1/4 — that's the same as the original's right() first half... Actually the GH R1 left() = original right() with different ending, and its right() = original left()... Anyway, it's a different variant. Also its lie() is 180,180,0,0 and toplefthand/toprighthand differ. So GH R1 is NOT the source of the local copy — the local copy matches gitee/official V1.1 exactly.

So the answer for the user's purpose (comparing servo gait numbers with a modified copy) is clear and clean: the local copy's gait numbers are UNMODIFIED from the official original.

Let me run the last verification command to check official V1.1 speed var + servo pin defs + presence of engine.html (to state local additions accurately).

Then write the final report.

For the report, I need to quote VERBATIM the original bodies of front(), back(), left(), right(), sitdown(), lie(), toplefthand(), toprighthand(), dosleep() with all servo numbers and delays in order, plus attach lines. I have all of these from the Read of GITEE_ORIGINAL_180V11_gaits.txt (which equals official V1.1). I'll quote them.

I should also answer Q3 (same vs mirrored) and Q4 (mounting orientation; which value swings forward).

For Q4, the evidence I have:
- Original doc for 360 version: "先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出" (first step legs 2&3 forward, then push legs 1&4 back) — with the code values at those moments: legs 2&3 forward uses servo2=140/servo3=40; legs 1&4 back uses servo1=40/servo4=140.
  Therefore: forward = 140 for servo2 (RR under local mapping) and 40 for servo3 (LF); backward = 40 for servo1 (RF) and 140 for servo4 (LR). Equivalently: forward = >90 on right-side servos (1,2), forward = <90 on left-side servos (3,4) — under the local engine.html leg mapping.
- All four servos identical model SG90, mounted in 4 limit slots; wiki says nothing explicit about mirrored mounting. So this inference about mirroring should be marked as "derived from code + doc wording, consistent with left/right mirrored mounting; the official docs don't state the orientation explicitly." I'll mark as high-confidence inference, not verbatim doc statement.

Let me do the final verification command.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== official V1.1: pins, speed, attached files ===\"\ngrep -nE \"^int engine[0-9]|int speed|int runtime|offset\" official_v11.cpp | head -15\necho \"--- official V1.1 servo attach ---\"; grep -n \"attach(\" official_v11.cpp\necho \"--- official V1.1 has engine.html route? ---\"; grep -c \"engine.html\" official …[截断,原长412]` → `=== official V1.1: pins, speed, attached files === 38:int engine1 = 14; // 舵机1引脚 39:int engine2 = 16; // 舵机2引脚 40:int engine3 = 12; // 舵机3引脚 41:int engine4 = 13; // 舵机4引脚 --- official V1.1 servo attach --- 810: servo1.attach(engine1, 500, 2500); // 配置舵机PWM，500µs=0度，2500µs=180度 811: servo2.attach(engine2, 500, 2500); 81 …[截断,原长684]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:41）

Let me run one final verification of the original's variable definitions and confirm the local additions.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Wait - official V1.1 has engine.html route (3 occurrences)? Let me check. Earlier we saw v180/EDA-Robot/data/ has control.html, index.html, setting.html - no engine.html. But main.cpp references engine.html in 3 places. Let me check what those are. Maybe leftover route for a file that doesn't exist. Let me verify.

Also local has `int speed = 300;` while official V1.1 doesn't seem to have speed... let me check. Actually the grep output for official V1.1 didn't show "int speed" or "int runtime". Let me confirm.

Actually the grep pattern was `^int engine[0-9]|int speed|int runtime|offset` and only engine1-4 matched. So official V1.1 (180 deg) has no speed/runtime vars. That's the 360 version's thing.

So local has `int speed = 300;` which is a leftover from the 360 version, but unused in the 180 gaits.

Let me double check local uses of `speed`.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== official V1.1: engine.html references ===\"\ngrep -n \"engine.html\" official_v11.cpp\necho; echo \"=== LOCAL: is 'speed' actually used anywhere? ===\"\ngrep -n \"speed\" \"/c/Users/UserX/Downloads/Robot dog 1.1/src/main.cpp\"", "description": "Check engine.html refs and speed usage"}` → `=== official V1.1: engine.html references === 270: server.on("/engine.html", HTTP_GET, [](AsyncWebServerRequest *request) 273: if (SPIFFS.exists("/engine.html")) { 274: fs::File file = SPIFFS.open("/engine.html", "r"); // 打开index.html文件 === LOCAL: is 'speed' actually used anywhere? === 38:int speed = 300;`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:42）

Let me confirm the engine.html route reference in official V1.1 and whether local's `speed` is actually used.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

I have everything I need. Let me finalize the report.

Summary of findings:

1. Original project: 
   - 立创开源硬件平台 (oshwhub): https://oshwhub.com/course-examples/bot-dog — "EDA-Robot机器狗", 2024-11-29, GPL 3.0, 17.3w views. Official JLC course project.
   - Gitee code repo: https://gitee.com/JasonYANG170/eda-robot (official code repo linked from oshwhub: "代码仓 Gitee https://gitee.com/JasonYANG170/eda-robot")
   - Official wiki: https://wiki.lceda.cn/zh-hans/course-projects/smart-internet/eda-robot/eda-robot-introduce.html
   
2. The local copy is a direct derivative of the official V1.1 180-degree version. Its gait functions are token-identical (same servo values and delays in the same order).

The original bodies: I have them verbatim from official V1.1 = Gitee main branch (which is the 180-degree V1.1).

Note there's a subtlety: the report asks for the ORIGINAL bodies of front(), back(), left(), right(), sitdown(), lie(), toplefthand(), toprighthand(), dosleep(). The original V1.1 has those exact values. Good.

3. Left vs right legs: In the original front(), servo2/servo3 get 140/40 and servo1/servo4 get 40/140 — these are MIRRORED/complementary values (40 vs 140) between the servo1/servo4 group and servo2/servo3 group. So the answer: mirrored/complementary, NOT same.

Let me be precise: In front():
- servo2.write(140); servo3.write(40) → opposite values (140 vs 40)
- servo1.write(40); servo4.write(140) → opposite
So servo2 and servo3 are complementary to each other, servo1 and servo4 are complementary to each other. And servo1/servo2 are complementary (40 vs 140), servo3/servo4 complementary (40 vs 140).

The evidence for leg mapping comes from the LOCAL engine.html (which labels 舵机1 (右前腿), 舵机2 (右后腿), 舵机3 (左前腿), 舵机4 (左后腿)) — but that file is a LOCAL addition, not in the original. So I must mark that as coming from the modified copy, not the original. Hmm — that's an important caveat. The local engine.html is not in the original repo (original has control.html, index.html, setting.html; local has those + engine.html + also a servos debug page).

Wait, actually the local data/ has control.html, engine.html, index.html, setting.html. The original V1.1 has control.html, index.html, setting.html. The 360 version has control.html, engine.html, index.html, setting.html — engine.html in 360 is the calibration page with 减少/增加 buttons and offset endpoints. The local engine.html is a different slider-based debug page — a local modification. So the leg labels 右前腿/右后腿/左前腿/左后腿 come from the local modification, not the original.

However, the official 360 version's front() comments say "先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出" — 2 and 3 legs step forward, 1 and 4 push back. And the wiki 4.6.8 运动控制 section documents the 180-degree version logic. So servo 2,3 = one diagonal pair (one group), 1,4 = other.

Actually in the official 360 code + wiki text: "先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出，然后再将2和3腿归位，最后将3和4腿归位即可."

For leg mounting orientation: I did not find explicit documentation about mirrored vs identical servo mounting. There's the calibration info in 360 version (offsets) and "四个电机的转动角度一致" (the four motors' rotation angles are the same) — which suggests all four servos are mounted in the SAME orientation and rotate the same angle (they use the same value 140/40 pattern... no wait, they use complementary 40/140).

Hmm, "4个电机的转动角度一致" means the rotation amounts are equal (all using the same |speed|). The compensation offsets differ per motor, hand-tuned.

I should be careful and mark the leg-mounting orientation as UNCERTAIN, with evidence:
- The original code assigns complementary values (40 vs 140) to the two diagonal groups, which is consistent with mirrored mounting OR with legs arranged such that opposing rotation swings them the same way.
- The official wiki says "4个电机的转动角度一致" and describes the gait as 2/3 legs forward then 1/4 legs backward.
- Which value (<90 or >90) swings a leg forward: In front(), the comment says servo2.write(140) //舵机2旋转至140度 and previously in the 360 version code the comment "+30C 2/3" with `1500 + speed + offset` for servo2 and `1500 - speed - offset` for servo3. Given "1500 + speed" corresponds to forward for 2/3 group. In the 180 version, 140 (>90) for servo2 and 40 (<90) for servo3 in the forward first step. So >90 for servo2 = forward, <90 for servo3 = forward. This is because the two servos are mounted mirrored relative to each other.

Actually careful: the original front() first step is the +30C (positive 30 degrees) for 2/3, where "C" likely means 度 (degree) — a Chinese abbreviation for 度 is "°"/"度"; they wrote "+30C" meaning +30 degrees. In 360 code: `servo2.writeMicroseconds(1500 + speed + engine2offsetleftpwm)` under comment `//+30C 2/3`. With speed=300 and offset ~ -120, that's 1500+300-120 = 1680 µs > 1500 → positive rotation. In the 180 version that became `servo2.write(140)` (>90 = positive rotation). And servo3 = 1500 - 300 - (-3) = 1203 µs < 1500 → `servo3.write(40)` (<90 = negative rotation). So servo2 and servo3 are driven with OPPOSITE angular directions for the same physical "forward step". This means they're mounted mirrored (or one is left-side and the other right-side).

So: within the pair (2,3), the numbers are complementary (140/40). Between (1,4): servo1 gets 40, servo4 gets 140 — also complementary. But servo2(140) and servo1(40) are complementary too, and servo3(40)/servo4(140).

So in front(): all four servos: 140, 40, 40, 140 — servo2=140, servo3=40, servo1=40, servo4=140.
In back(): servo3=140, servo2=40, servo1=140, servo4=40.

So for run: front uses (s2,s1)=140 and (s3,s4)=40 first; back uses (s3,s2)=140... let me just report accurately and note the mirroring.

I'll state: the original uses MIRRORED/complementary numbers (40 vs 140) — not identical — for the paired servos in front()/back(); i.e., one servo of each pair gets 40 while the other gets 140 in the same phase.

4. Servo mounting orientation: I found no explicit official documentation of "mirrored left/right vs all identical". The closest evidence:
- Original wiki 4.6.8: "4个电机的转动角度一致" (the four motors rotate by the same angle magnitude) + per-motor calibration offsets (engineXoffsetXpwm) in the 360 version, because 360° servos can't hold an angle.
- 360 version's front() shows the paired servos driven with opposite sign of (speed + offset): servo2 = 1500+speed+off, servo3 = 1500-speed-off.
- Therefore: the code treats servo pairs (2,3) as mirrored pairs — one value >90 and one <90 produce the SAME physical swing direction.
- Which value swings a leg forward: For servo2 and servo4, >90 (140) is used for the "forward step" in front(); for servo1 and servo3, <90 (40) is used. So it depends on which leg; the code is "complementary", implying the leg pairs are mounted mirrored.

I need to be careful and mark it uncertain as I did not see an explicit mounting diagram text; there might be one in the PDF I couldn't extract (LibreOffice conversion produced nothing — the PDF may be image-based; the txtout dir was empty).

Let me note that I could not extract the official PDF text (image-based/scanned), so any mounting diagram inside it is unverified.

Actually let me quickly try one more time to extract the PDF - maybe try pdftotext if available, or check if there's a python with pypdf. Let me check quickly. Actually, the local environment said conda python exists but I couldn't find miniconda3. Let me do a very quick check for pdftotext, then wrap up. Time is fine.

Let me also double check: does the official 180 V1.1 control.html include 回收 button (yes: "回收"). The local has "回收机器狗". The local main.cpp's endpoints include /sleep which maps to dosleep — need to check. Let me verify local /sleep maps to dosleep, and the original's /sleep behaviour.

Also worth noting the local copy's key modifications vs original:
- LittleFS instead of SPIFFS
- Hardcoded default weather key SB3j4zrxZ7nuRXv8v + AP password 12345678 (original: no password)
- New engine.html slider debug page + /servoN?angle= endpoints (not in original)
- IRAM_ATTR instead of ICACHE_RAM_ATTR
- Removed 360-degree offsets/speed calibration (original V1.1 has none either)
- settings.html extended

Let me do a couple of final quick checks then write the report.

Actually, the report is the main deliverable. Let me verify /sleep→dosleep in local, and check what the original does on 'sleep'/dosleep call, then finalize.

Let me also record the exact set of URLs I checked for the "list the URLs you actually checked" requirement (in case relevant). Since I found it, it's less critical but good to include key ones.

Let me quickly run those two greps.

</details>

- 🔧 **Bash** `{"command": "cd \"/c/Users/UserX/Downloads/Robot dog 1.1\" && grep -n 'server.on(\"/sleep\"' -A5 src/main.cpp | head -12; echo \"=== local dosleep call site ===\"; grep -n \"dosleep()\" src/main.cpp", "description": "Check local sleep endpoint mapping"}` → `=== local dosleep call site === 689:void dosleep() 782: dosleep(); 959: dosleep(); // 执行一次舵机动作`

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S; echo \"=== original: sleep route ===\"; grep -n '\"/sleep\"' -A6 official_v11.cpp | head -14; echo \"=== official wiki page list (leg/orientation) ===\"; grep -oE '四足|一脚|装配|组装|朝向' w2_eda-robot-software.html | sort | uniq -c", "description": "Check original sleep route and orientation terms"}` → `=== original: sleep route === === official wiki page list (leg/orientation) === 3 四足`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:42）

Let me do two final confirmations before reporting.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Let me check the original's "sleep" route in official V1.1 vs local.

Actually, the official V1.1 has a "回收" button that maps to 'sleep' command, and the local's control.html has "回收机器狗" mapped to 'sleep'. Let me check the original's /sleep route and what it does.

Let me quickly check.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== original V1.1 'sleep' route ===\"; grep -n \"sleep\" official_v11.cpp | head -10\necho \"=== original v180 control.html sleep button ===\"; grep -oE \"sendCommand\\('sleep'\\)[^<]*<|>[^<]*回收[^<]*<\" v180/EDA-Robot/data/control.html | head -5\necho \"=== 360 original sleep route ===\"; grep -n \"sleep\" v360 …[截断,原长412]` → `=== original V1.1 'sleep' route === 122: server.on("/sleep", HTTP_GET, [](AsyncWebServerRequest *request) 674:void dosleep() 745: if(receivedString=="dosleep"){ 746: dosleep(); 921: dosleep(); // 执行一次舵机动作 === original v180 control.html sleep button === sendCommand('sleep')">回收< === 360 original sleep route ===`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Good. So the original V1.1 already has "/sleep" route → dosleep(), and the "回收" button (labelled 回收, local changes it to "回收机器狗"). So the local modifies the button label to "回收机器狗".

Now let me confirm the exact original dosleep body from the official and get the final verbatim. Let me also verify the servo-to-leg mapping claim: In local engine.html, labels are 舵机1(右前腿), 舵机2(右后腿), 舵机3(左前腿), 舵机4(左后腿). But that's local-added (engine.html isn't in official V1.1... wait, official V1.1 DOES have engine.html route and references. Let me check if the v180 zip contained engine.html - no, it only had control/index/setting. But the source references /engine.html route. So official V1.1 expects engine.html but the data folder in that zip doesn't include it (maybe a packaging gap). The 360 version DID include engine.html. So official engine.html exists in the 360 version — the "motor calibration" page with 减少/增加 buttons.

So the local's engine.html (with slider per-servo 舵机1 (右前腿) etc.) is a NEW local modification. That's important for the leg mapping question: the leg mapping label exists only in the local modified copy, not the original. I should note that as uncertain/added.

Let me double check whether the original has any leg mapping documentation. Let me search the official PDF text. LibreOffice conversion produced nothing. Let me try a different approach - maybe check if there's web-based text of the wiki software page describing legs. The wiki said "先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出" — legs numbered 2/3 and 1/4, no left/right mapping.

Actually, let me reason about the mechanics from the original code to answer question 3 and 4:

front():
- servo2.write(140), servo3.write(40)
- servo1.write(40), servo4.write(140)
- servo2.write(90), servo3.write(90)
- servo1.write(90), servo4.write(90)
- servo1.write(140), servo4.write(40)
- servo2.write(40), servo3.write(140)
- servo1.write(90), servo4.write(90)
- servo2.write(90), servo3.write(90)

So servo pairs: (2,3) and (1,4). Within pair (2,3): 140/40 = opposite values. Within pair (1,4): 40/140 = opposite. So legs 2,3 get the SAME movement direction (both "forward" if 140 means forward for servo2 and 40 means forward for servo3 given mirrored mounting), and 1,4 same. It's the "diagonal gait": 2&3 move forward while 1&4 stay, then 1&4 push back, etc. Wait, actually reading the wiki: "先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出" - first legs 2 and 3 step forward, then legs 1 and 4 push backward.

Important: within a diagonal pair (2,3), the values are complementary: servo2=140 and servo3=40. That is consistent with mirrored mounting: the same physical rotation direction requires mirrored commands on the opposite side. Same for (1,4): servo1=40, servo4=140.

So the answer to Q3: In the original front(), left and right servos receive MIRRORED/complementary numbers in the sense that servo2=140 while servo3=40 and servo1=40 while servo4=140. Wait, but which are left vs right? Without leg labels we can't be certain from the original source. Local engine.html says servo1=右前腿, servo2=右后腿, servo3=左前腿, servo4=左后腿. Under that mapping: front() has servo2 (right rear)=140 and servo3 (left front)=40 (diagonal pair), then servo1 (right front)=40 and servo4 (left rear)=140.

Hmm, that's a diagonal trot pattern: the two diagonally-opposite legs move together as one pair, and both get mirrored values. That means for legs on opposite sides, the SAME physical forward swing requires opposite numeric offsets from 90 — i.e., mirrored mounting. Specifically:
- Leg pair (servo2, servo3): 140 and 40 → opposite sides of 90 by 50 degrees.
- Leg pair (servo1, servo4): 40 and 140.

That is: within each diagonal pair, one servo goes >90 and the other goes <90. This strongly implies mirrored servo mounting between the two sides.

But note also front(): the second half does servo1.write(140), servo4.write(40) — that's the reverse of the first-half pair for legs 1,4. So in the "push" phase, servo1 goes 140 and servo4 goes 40, i.e., they swap. So both pairs swing through symmetric extremes.

Hmm, wait, actually if legs are diagonally paired (2,3) and (1,4), and in the first phase (2,3) get 140/40 and in the second phase (1,4) get 40/140 — hold on, first phase is servo2=140, servo3=40, then servo1=40, servo4=140. Then phase 2: servo1=140, servo4=40, then servo2=40, servo3=140. So each servo visits both 140 and 40. Interesting: for servo1, it first goes to 40 (with servo4=140), then to 140 (with servo4=40). Hmm, that seems like a "step forward then push back" cycle: for pair (1,4), the phase-1 movements are opposite to phase-2.

Hmm, wait, actually let me re-read. In front():
1. servo2=140, servo3=40 (pair A swings one way)
2. servo1=40, servo4=140 (pair B swings one way — mirrored)
3. servo2=90, servo3=90 (pair A returns)
4. servo1=90, servo4=90 (pair B returns)
5. servo1=140, servo4=40 (pair B swings the other way)
6. servo2=40, servo3=140 (pair A swings the other way)
7. servo1=90, servo4=90
8. servo2=90, servo3=90

So yes: pair A = {servo2, servo3}, pair B = {servo1, servo4}. Within each pair values are complementary (one 140, other 40). And within each pair, the same phase-1 value assignment.

So the answer to Q3: In the original, legs on opposite sides receive COMPLEMENTARY (mirrored) numbers, not identical: servo2=140 vs servo3=40 (pair), servo1=40 vs servo4=140 (pair). And notably pairs are diagonal.

Now Q4: mounting orientation and which value swings forward. From code alone: for servo2 at 140 and servo3 at 40 to produce the same physical swing direction (as the diagonal gait requires), they must be mirror-mounted. Each servo's forward vs backward direction isn't labeled in the source. The wiki says 2 and 3 legs step forward first. So the value causing "forward" depends on the individual servo: servo2 → 140 is forward, servo3 → 40 is forward, servo1 → 40, servo4 → 140. Hmm, but wait, is it "forward step"? The wiki: "先将机械狗的2和3号腿向前迈出" — first step legs 2 and 3 forward. Hmm, but actually in the code the sequence is: servo2=140, servo3=40 first, THEN servo1=40, servo4=140. Hmm, so legs 2&3 step first. So per wiki: 2&3 forward means servo2→140 swings leg 2 forward and servo3→40 swings leg 3 forward. So >90 for servo2 = forward; <90 for servo3 = forward. Then 1&4 "向后蹬出" (push back): servo1→40 and servo4→140 push back.

Wait, but careful — the code's first two steps are: (servo2=140, servo3=40) then (servo1=40, servo4=140). The wiki says first 2&3 forward, then 1&4 backward. That matches. Then "再将2和3腿归位" (2&3 return to 90) then "最后将3和4腿归位" (3&4 return) — hmm, wiki says 3和4, likely a typo for 1和4. In code, after the 1&4 push, servo2/servo3 return to 90, then servo1/servo4 return to 90. So the wiki's "3和4" is likely a typo.

So: legs 2 & 3 = "left-side pair"? or diagonal pair? Hmm. If 2&3 are a diagonal pair, then per local engine.html labels (servo2=右后, servo3=左前) yes diagonal. And 1&4 (右前, 左后) also diagonal. So the gait is a diagonal trot.

Hmm, but hold on. Which is it: do 2&3 get mirrored values because they're on opposite sides (mirrored mounting), or...? Yes — servo2=140 (右后) and servo3=40 (左前). These are on opposite sides (right vs left). For both to swing "forward", given mirrored mounting, values must be mirrored about 90. Suggests: right-side servos swing forward with >90, left-side with <90 (or vice versa). Specifically under local engine.html mapping: servo1 (右前): forward-direction value? For 1&4 pair "向后蹬出" push back with servo1=40, so forward for servo1 would be >90 (140). And servo4 (左后): push back with 140, so forward = <90 (40). And servo2 (右后): forward with 140 (>90); servo3 (左前): forward with 40 (<90).

So the consistent pattern: RIGHT-side servos (1, 2) swing forward with values >90; LEFT-side servos (3, 4) swing forward with values <90. This is a strong, self-consistent inference — and it means the left and right sides are mirror-mounted (or at least commanded mirrored).

However I must mark this as inference, since the original source doesn't label left/right. The local engine.html does label them (舵机1 右前腿, 舵机2 右后腿, 舵机3 左前腿, 舵机4 左后腿), and that labeling matches the geometry: servo1&2 = right, servo3&4 = left; and the pairs (1,4) and (2,3) are indeed diagonals. This is a coherent cross-check.

Actually hold on. Let me reconsider: is (2,3) a diagonal? servo2=右后 and servo3=左前 → yes, diagonal. (1,4): 右前 and 左后 → diagonal. Great, fully consistent with the wiki's "2和3号腿向前迈出，再将1和4腿向后蹬出" being a diagonal trot.

So Q3 answer: MIRRORED/complementary. In front(), servo2=140 while servo3=40; servo1=40 while servo4=140. The left-side (3,4) and right-side (1,2) servos receive complementary numbers, not identical. Specifically within each diagonal pair the values are mirror images about 90.

Hmm, but let me be careful about what "the same servo numbers or mirrored" means for the question. The question asks about "left-side and right-side legs". In front(): pair (2=右, 3=左): 140 vs 40 → mirrored. Pair (1=右, 4=左): 40 vs 140 → mirrored. So: mirrored.

And also symmetrically, left/right same-leg-type pairs (1 右前 vs 3 左前): in phase 2, servo1=40, servo3... wait servo3 is in pair (2,3). Hmm. Let me just tabulate: pairs are diagonal, and within each diagonal pair the two servos (one on each side) get complementary numbers.

Now, one more check: The user wants "the original servo attach() lines with pulse widths". Official V1.1: servo1.attach(engine1, 500, 2500), etc. pins 14, 16, 12, 13. Confirmed.

Also there's the 360 version which uses same pins and same attach?? Let me check the 360 version's attach lines and pin defs. Earlier we saw engine1..4 = 14,16,12,13 and offsets. Let me check attach lines in 360 version quickly. Actually I have enough. But let me grab it to be thorough, since the user asked "original servo attach() lines". The 180 V1.1 is what matches their code. Let me quickly check 360's attach.

Also I should double check the local's dosleep and the original's dosleep: original official V1.1 dosleep len 166 (has comments), local 112. Token identical: w1:write(0), w3:write(180), w2:write(180), w4:write(0). 4 tokens. Good.

Let me quickly verify the 360 attach lines, then write the report. Also let me grab dosleep verbatim strings for exactness (already have).

Let me check the 360 attach lines.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== 360 version attach lines ===\"; grep -n \"attach(\" v360/EDA-Robot/src/main.cpp\necho \"=== 360 dosleep/dosleap ===\"; grep -n \"void dosleep\\|void dosleap\" -A6 v360/EDA-Robot/src/main.cpp | head -20", "description": "Check 360 version attach and sleep"}` → `=== 360 version attach lines === 846: servo1.attach(engine1); 847: servo2.attach(engine2); 848: servo3.attach(engine3); 849: servo4.attach(engine4); === 360 dosleep/dosleap ===`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:43）

Let me verify the 360-version attach lines and finalize.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

Now I have everything. Let me also quickly check the local's servoN attach lines and confirm they match, and check whether the local `dosleep` differs.

Local line 845-848:
```
servo1.attach(engine1, 500, 2500); // 配置舵机PWM，500µs=0度，2500µs=180度
servo2.attach(engine2, 500, 2500);
servo3.attach(engine3, 500, 2500);
servo4.attach(engine4, 500, 2500);
```
Matches official V1.1 exactly.

Now, let me also double check the question 3: are left/right legs SAME or MIRRORED in front()/back()? 

In front():
- servo2.write(140), servo3.write(40) — 140 vs 40 → MIRRORED
- servo1.write(40), servo4.write(140) — 40 vs 140 → MIRRORED

And the local engine.html says: 舵机1 (右前腿), 舵机2 (右后腿), 舵机3 (左前腿), 舵机4 (左后腿).

So legs are paired across the diagonal: servo2 (right rear) & servo3 (left front) are a diagonal pair; servo1 (right front) & servo4 (left rear) are the other diagonal pair. Within each diagonal pair, the two servos get COMPLEMENTARY values (140/40). So the leg pairs are diagonal pairs, and left/right sides are mirrored (opposite values) — this is a trot gait.

Importantly: servo2/servo3 (a diagonal pair) get (140, 40) — one is 140, other is 40. And servo1/servo4 (the other diagonal) get (40, 140). So across BOTH diagonals it's mirrored: the diagonal pair {1,4} has (40,140) and {2,3} has (140,40).

So: left-side and right-side legs receive MIRRORED/complementary numbers. Specifically in front(): servo1=40 & servo4=140 (opposite), servo2=140 & servo3=40 (opposite).

Now question 4: servo mounting orientation and which value swings a leg forward.

Evidence:
- The local engine.html labels: 舵机1 (右前腿), 舵机2 (右后腿), 舵机3 (左前腿), 舵机4 (左后腿). But note: this engine.html is a LOCAL ADDITION (not in the official V1.1 or 360 zip). So this mapping is from the modified copy, not the original. I must mark it as such. However, it is plausible/derived. Actually wait — local engine.html was added by the modifier. Hmm, but did the 360 version have engine.html? Yes, the 360 version DID have data/engine.html but it was a calibration page (减少/增加 buttons), not the slider page. The local engine.html is a slider page with 舵机N (腿) labels. So those leg labels come from the local modification, NOT the official original.

Interesting: also note in local main.cpp, /servo1.../servo4 routes were added (not in original) — those are the new endpoints for engine.html sliders.

For the orientation question: the official docs say "推荐使用180度舵机，自带限位器，无需校准" and "4个电机的转动角度一致" (the 4 motors' rotation angles are the same) — meaning all 4 servos are mounted the SAME way (not mirrored physically), and the mirroring is achieved purely in software by writing complementary values. That's an important finding: from the wiki, "4个电机的转动角度一致" in the 360-version context relates to syncing rotation. Let me be careful about that quote: "为了确保4个舵机能同步，还加入了engineXoffsetXpwm，用于控制各个电机的补偿，这就需要我们耐心去找到适宜的补偿值。4个电机的转动角度一致。" 

Hmm, this is about the 360 version's offsets. It says the 4 motors' rotation angles are the same (i.e., they should be synchronized), so compensation values are used.

For which value swings a leg forward: I don't have direct documented evidence. Let me reason from the code but mark as inference:
- In front(): first, servo2 & servo3 → 140/40, then servo1 & servo4 → 40/140. Comment in official wiki: "先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出，然后再将2和3腿归位，最后将3和4腿归位即可" — "first step legs 2 and 3 forward, then push legs 1 and 4 backward". 

Wait, that's for the 360 version (using microseconds). Let me read it again: "前进的逻辑如下，先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出，然后再将2和3腿归位，最后将3和4腿归位即可。"

So official documentation says: legs 2 and 3 step forward, legs 1 and 4 push backward. And within front(), servo2=140, servo3=40 at that moment. Hmm, so leg 2 goes forward with 140, and leg 3 goes forward with 40. That's because they're on opposite sides (mirrored mounting direction) OR... wait.

Hmm, but the wiki says legs 2&3 move forward together. servo2 writes 140 and servo3 writes 40. If both "move forward" but get opposite values, that means the two servos are physically mirrored (opposite mounting orientation). That contradicts "4个电机的转动角度一致".

Hmm, careful. Actually the wiki states the 360 version's logic. In the 180 version, front() has servo2=140, servo3=40 in the first step. Let's not over-infer. But it's a notable clue: servo2 and servo3 belong to a diagonal pair (right-rear + left-front per local engine.html), and diagonal pairs work together in a trot. If servo2 (right rear) = 140 and servo3 (left front) = 40 both mean "forward", then the servos on opposite sides are mounted mirrored (or the linkage geometry differs).

Actually, hmm. Let me re-read the local engine.html labels: 舵机1 (右前腿), 舵机2 (右后腿), 舵机3 (左前腿), 舵机4 (左后腿). With this: {servo2 (右后), servo3 (左前)} is a diagonal pair. {servo1 (右前), servo4 (左后)} is the other diagonal. This is the classic trot diagonal pairing. 

And in front(), the diagonal {2,3} first gets (140, 40), then {1,4} gets (40, 140). Since within a diagonal pair the two legs are on opposite sides (right-rear and left-front), and they are moving in the same direction (both forward per the docs for step 1), the mirrored values (140 vs 40) imply mirrored mounting.

Hmm, but wait — but the wiki quote about "4个电机的转动角度一致" says all four rotate consistently... For the 360 version this means rotation speed consistency. Let's avoid over-claiming.

Let me be careful and mark: The strong evidence is:
1. Values are complementary within a diagonal pair (140/40, 40/140) — a mirrored relationship.
2. Local (modified copy's) engine.html assigns: servo1=右前腿 (right front), servo2=右后腿 (right rear), servo3=左前腿 (left front), servo4=左后腿 (left rear).
3. Official wiki says for front(): legs 2&3 step forward first, then legs 1&4 push back.

So in front(), leg2 (right-rear) goes "forward" at 140 and leg3 (left-front) goes "forward" at 40. Same physical motion, opposite numeric values → mirrored servo mounting.

Hmm, but this is an inference. However, it's a well-supported one. But hold on: is the "forward" claim correct? "先将机械狗的2和3号腿向前迈出" — yes, legs 2 and 3 step forward.

Hmm, but actually there's a subtlety: maybe the legs 2 and 3 numbers refer to legs on the same side? Like legs 1&2 = left side, legs 3&4 = right side? No — because in the local engine.html, 1=右前, 2=右后, 3=左前, 4=左后. Hmm, that gives a weird ordering (right front, right rear, left front, left rear). But this ordering is exactly the one in the latest eda_robotR1 (GH) and local... hmm, actually the local engine.html is what the modifier wrote.

Hmm — hold on. Let me reconsider. Let me look at the wiring order in the official PCB. Actually — let me think about the physical layout: engine pins 14, 16, 12, 13 in order. In the 3D design, the 4 servos sit in 4 slots. Without a hardware diagram I can't be certain.

But there's an important cross-check: `sitdown()` writes servo2=140, servo4=40. If servo2=right rear and servo4=left rear, then in sitdown, both REAR legs go (140, 40) — complementary, i.e., rear legs fold. That's consistent: sit() = rear legs fold down. And lie() writes servo1=180, servo3=0, servo2=0, servo4=180 — all 4 legs go to the extreme; 1&4 opposite to 2&3. So 1 and 4 are on the same side-pairing? Hmm: lie has {1:180, 4:180} and {2:0, 3:0}. So servos 1&4 get the SAME value, and servos 2&3 get the SAME value in lie(). 

Hmm! In lie(), servo1 and servo4 both = 180 (same), servo2 and servo3 both = 0 (same). If 1=右前, 4=左后 (diagonal pair), then both diagonal-1 legs go to the same value 180. And in front(), diagonal {1,4}: servo1=40, servo4=140 (opposite). Hmm, that's inconsistent with "same motion → same value" unless lie() isn't a symmetric motion... but lie() IS a symmetric motion (both front legs and both rear legs move the same way... no wait, lie = 趴下, all 4 legs splay out).

For lie(): if 1=右前,4=左后 → 180 and 2=右后,3=左前 → 0. For a "lie down" pose, all four legs should move outward/rotate the same way. If leg1 (right front) needs 180 and leg3 (left front) needs 0, then front-left and front-right are mirrored. Similarly right-rear (2)=0 and left-rear (4)=180. Consistent with mirrored left/right mounting.

OK so consistent story: legs are physically mirrored left vs right; the code writes complementary values for left/right.
Front legs = 1 (right) and 3 (left). Rear legs = 2 (right) and 4 (left).

Check: toplefthand() → servo3.write(0) then back to 30→90. servo3 = 左前腿 (left front leg) per the local engine.html. That's fully consistent: "抬左手" (lift left hand) operates 左前 (left front leg) = servo3. 
And toprighthand() → servo1.write(180) → servo1 = 右前腿 (right front leg). "抬右手" operates 右前 = servo1. 

So the local engine.html mapping (1=右前, 2=右后, 3=左前, 4=左后) is strongly corroborated by the toplefthand/toprighthand semantics (抬左手 = servo3, 抬右手 = servo1). This is a solid inference, effectively confirmed.

And sitdown() → servo2 (右后) = 140, servo4 (左后) = 40 — both REAR legs, complementary. Confirmed: sit down = rear legs fold. 

So now the mirror question: front legs are servo1 (right) and servo3 (left). In front(): servo1 → 40 then later 140; servo3 → 40 then later 140. Left and right front legs get mirrored/complementary numbers. Rear legs: servo2 (right rear) and servo4 (left rear). In front(): servo2=140, servo4=140 at the same time... hmm, wait.

Let me carefully lay out front():
Step 1: s2=140, s3=40 
Step 2: s1=40, s4=140
Step 3: s2=90, s3=90
Step 4: s1=90, s4=90
Step 5: s1=140, s4=40
Step 6: s2=40, s3=140
Step 7: s1=90, s4=90
Step 8: s2=90, s3=90

So the pairing used by the code is {2,3} and {1,4} — diagonal pairs. Within pair {2,3}: 2=右后, 3=左前 → opposite corners. Values 140/40 → complementary. Within pair {1,4}: 1=右前, 4=左后 → opposite corners. Values 40/140 → complementary.

So in front(): the two legs of each diagonal receive complementary (mirrored) values, and the two diagonals are in anti-phase. That is the standard trot.

Also in sitdown(): servo2 (右后, right rear) = 140, servo4 (左后, left rear) = 40 → the two rear legs receive complementary values (mirrored), consistent.

So answer to Q3: MIRRORED/complementary, e.g. 40 vs 140 — and specifically this holds within each working pair in front()/back().

Now Q4: which value (<90 or >90) swings a leg forward?

Evidence: 
- The wiki: "先将机械狗的2和3号腿向前迈出" — legs 2 and 3 step forward. In front(), step 1 sets servo2=140, servo3=40. So leg2 moves forward with 140 (>90), leg3 moves forward with 40 (<90). These are MIRRORED servos (right rear vs left front), so the same physical "forward" direction corresponds to opposite numeric values. So: for one side, >90 = forward; for the mirrored side, <90 = forward. That's the honest answer.

Hmm, but can I determine which? servo2 = 右后腿 (right rear). It goes to 140 = forward. So for the right rear leg, >90 swings forward. servo3 = 左前腿: goes to 40 = forward, so for the left front leg, <90 = forward.

Hmm, but wait: is the local engine.html leg mapping trustworthy enough? It's the modifier's own file (in the local copy). It's corroborated by 抬左手/抬右手 = servo3/servo1. So yes, reasonably strong. But this is the LOCAL copy's file, not the original's. The original's own docs don't state the leg names. I'll flag: the leg-name mapping comes from the modified copy's engine.html, corroborated by toplefthand/toprighthand semantics.

Also: the modifier's code comments in front() say "//舵机2旋转至140度" — no direction. In the GH fork, front() begins "servo3.write(40); //左前向前旋转50度" — comment "左前向前旋转50度" = left-front rotates forward 50 degrees! And "servo2.write(140);//右后向前旋转50度" = right-rear rotates forward. Great — that's from the GH derivative (pluckypioneer/eda_robotR1), which explicitly labels: 左前 = left front = servo3 → writes 40 "向前旋转" (forward); 右后 = right rear = servo2 → writes 140 "向前旋转" (forward).

That's independent corroboration of BOTH the leg mapping (servo3=左前, servo2=右后) AND the direction: servo3=40 means forward (left-front), servo2=140 means forward (right-rear). 

Let me verify those comments verbatim. Earlier I saw:
```
366	void front(){
367	    servo3.write(40); //左前向前旋转50度
368	    servo2.write(140);//右后向前旋转50度
```
Yes.

So: left-front (servo3): 40 → forward (i.e., <90 = forward on the left side). Right-rear (servo2): 140 → forward (>90 = forward on the right side). Mirrored mounting confirmed.

Hmm, careful: 左前 is on the LEFT side and 右后 is on the RIGHT side; both are on different sides. And the comment says both "向前" (forward) at 40 and 140 respectively. So yes: on the left side, values below 90 swing the leg forward; on the right side, values above 90 swing the leg forward (for the corresponding phase).

Wait — but which servo is on the left and which on the right? servo3 = 左前 (left front) and servo2 = 右后 (right rear). So servo3 (left) forward = 40 (<90). servo2 (right) forward = 140 (>90). Good.

Now also let's double check the servo3 = left-front claim from the GH fork. In the GH fork, front() is:
servo3.write(40); //左前向前旋转50度
servo2.write(140);//右后向前旋转50度
→ servo3 is 左前 (left front), servo2 is 右后 (right rear). And by extension servo1 = 右前 (right front), servo4 = 左后 (left rear). This matches the local engine.html labels exactly! Excellent — two independent sources agree. Though note the GH fork and local are both derivatives; but the GH fork's comments use the original's variable names with explicit leg labels.

Hmm, but do they really? Actually — the fact that pluckiyoneer's fork comments "左前" and "右后" on servo3/servo2 could also come from the original's own docs. Either way, they match the local engine.html. Good.

Also, mounting orientation: 
- Between front-left (servo3: forward=40) and front-right (servo1: forward=? ). In front(), step 2: s1=40, s4=140, described as "再将1和4腿向后蹬出" (legs 1 and 4 push backward). So servo1=40 = backward (right front). Combined with servo3=40 = forward (left front) → confirms left/right mirroring: same value 40 means forward on left, backward on right.

Great, so this is a strong, verifiable answer:
- Servos are mounted mirrored left/right. All left-side/lower values... hmm, more precisely: for a given numeric value, the physical direction is opposite on the left vs right.
- Forward for left-front (servo3) = 40 (<90); forward for right-front (servo1) = 140 (>90).

Hmm wait, but servo3 is left FRONT and servo1 is right FRONT. Let me double check that the diagonal pair {1,4} at 40/140 are both "pushing backward". Wiki: "再将1和4腿向后蹬出" — yes, legs 1 and 4 push back. In code, s1=40 and s4=140. So servo1 (right front) = 40 → backward; servo4 (left rear) = 140 → backward. So for the right-front, 40 = backward, hence 140 = forward. For the left-rear, 140 = backward, so 40 = forward.

Consistent mirroring rule: LEFT side (3=左前, 4=左后): <90 = forward, >90 = backward. RIGHT side (1=右前, 2=右后): >90 = forward, <90 = backward.
Check with servo3 (left front): 40 = forward ✓ (wiki: leg 3 steps forward at step 1)
Check with servo2 (right rear): 140 = forward ✓ (wiki: leg 2 steps forward at step 1)
Check with servo1 (right front): 40 = backward ✓ (wiki: leg 1 pushes back at step 2)
Check with servo4 (left rear): 140 = backward ✓ (wiki: leg 4 pushes back)
All four consistent! And this matches GH fork comments for servo3 (左前 forward = 40) and servo2 (右后 forward = 140).

So the rule holds: mirrored left/right mounting; left side <90 = forward, right side >90 = forward.

Now, one caveat: this assumes the local engine.html leg labels and the GH fork comments are correct — both are derivatives, but they agree with each other and with the official wiki's motion narrative. I'll flag the confidence level.

Now let me also verify the local's modifications summary for a concise report, and note the key difference: the local is based on the official 180-degree V1.1 (the "training camp"/实训营 release), with these changes:
- FS → LittleFS (18 occurrences)
- SPIFFS → LittleFS
- added /servo1../servo4 slider debug endpoints + engine.html slider page (not in original)
- AP password "12345678" (original: empty = no password)
- hardcoded weather API key SB3j4zrxZ7nuRXv8v (original: user-configurable, empty)
- NTP uses ntp1.aliyun.com (original: nevigate... let me check)
- IRAM_ATTR instead of ICACHE_RAM_ATTR
- removed speed/runtime offsets (there were none in 180 version)
- "回收机器狗" label vs original "回收"
- lib deps versions bumped (ESPAsyncWebServer-esphome ^3.2.2 vs 3.3.0, U8g2 ^2.36.12 vs 2.36.2, ArduinoJson ^7.4.2 vs 7.2.0)
- deleted .vscode etc.

Let me quickly check the NTP server in the original.

Actually, let me also grab the original's local attached servo attach lines exactly and the exact original verbatim bodies for the report. I have those.

Let me check the original NTP.

Also I should double check: does the local's `dosleep` match the original? The token check said IDENTICAL for all 9. Good.

Let me check the original NTP line quickly and then write the report. Also, I want to give the exact attachment URL for the 180 V1.1 zip so the user can re-download.

Let me also note: the Gitee repo is the official code repo linked from the oshwhub project: https://gitee.com/JasonYANG170/eda-robot

And the wiki: https://wiki.lceda.cn/zh-hans/course-projects/smart-internet/eda-robot/

Let me do the final NTP check.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\necho \"=== NTP in original V1.1 ===\"; grep -n \"NTPClient timeClient\\|ntp\" official_v11.cpp | head -5\necho \"=== NTP in local ===\"; grep -n \"NTPClient timeClient\\|ntp\" local_main.cpp | head -5\necho \"=== weather URL original vs local ===\"; grep -n \"seniverse\" official_v11.cpp local_main.cpp | head -5\necho …[截断,原长412]` → `=== NTP in original V1.1 === 48:WiFiUDP ntpUDP;//声明UDP 49:NTPClient timeClient(ntpUDP, "ntp1.aliyun.com", 8 * 3600, 60000);//配置NTP服务器 === NTP in local === 51:WiFiUDP ntpUDP; 52:NTPClient timeClient(ntpUDP,"ntp1.aliyun.com",8*3600,60000); === weather URL original vs local === local_main.cpp:55:const char *weatherAPIBase …[截断,原长561]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

I have everything. Let me compile the final report.

Key findings:
1. Original project: oshwhub.com/course-examples/bot-dog — "EDA-Robot机器狗" by JasonYANG170 (嘉立创 JLC training course project), with Gitee code repo https://gitee.com/JasonYANG170/eda-robot. Official wiki docs at wiki.lceda.cn.

2. Original gait functions verbatim (official V1.1 180-degree servo version, identical to Gitee main.cpp).

3. Left/right legs: in front(), servo2/servo3 get 140/40 and servo1/servo4 get 40/140 — MIRRORED/complementary pairs. Specifically: servo2.write(140) & servo3.write(40); servo1.write(40) & servo4.write(140). So servo1/servo3 = 40 while servo2/servo4 = 140 — they're complementary (40 vs 140), NOT the same.

Wait, actually let me be careful: servo1 and servo4 are on the same side (per local engine.html: servo1=右前腿, servo2=右后腿, servo3=左前腿, servo4=左后腿). Hmm, local engine.html says: 舵机1 (右前腿), 舵机2 (右后腿), 舵机3 (左前腿), 舵机4 (左后腿). So right side = servo1(FR), servo2(RR)... wait that's odd: servo2 = 右后腿 (right rear), servo3 = 左前腿 (left front), servo4 = 左后腿 (left rear). So right-side legs = servo1 + servo2, left-side legs = servo3 + servo4.

Hmm, but in front(): servo2.write(140); servo3.write(40); then servo1.write(40); servo4.write(140).

So servo1 (right front) = 40, servo2 (right rear) = 140; servo3 (left front) = 40, servo4 (left rear) = 140.

So within a side: right side = servo1(40) & servo2(140) — complementary. Left side = servo3(40) & servo4(140) — complementary. And servo1 == servo3 (both 40), servo2 == servo4 (both 140).

So: servo1 (RF) and servo3 (LF) get the SAME number (40); servo2 (RR) and servo4 (LR) get the SAME number (140). The diagonal pairs get the same value.

Actually careful: the local engine.html labels (舵机1 右前腿, 舵机2 右后腿, 舵机3 左前腿, 舵机4 左后腿) is LOCAL-only annotation (not in original — must verify). Actually I should mark this as: the leg labels come from the local copy's engine.html which is a local addition. The original wiki says "先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出" — legs 2 and 3 step forward, legs 1 and 4 push back. And in front(), at the moment of stepping forward: servo2.write(140) & servo3.write(40)... Hmm, that says "先2、3腿向前，1、4腿向后蹬" - initially 2/3 are moved (140 and 40) and then 1/4 (40 and 140).

Hmm, but wait — this is the 180° version, and 140/40 apparently correspond to forward/backward swing. In 360 version the comments are "+30C 2/3" meaning 2/3 leg rotates +30°C (clockwise?) and "0C 1/4".

Actually for the 360 version: `servo2.writeMicroseconds(1500 + speed + ...)` = 1500+300 = 1800 (i.e., >1500 = clockwise, "+30C" = +30° clockwise) for servo2 & servo3 gets 1500 - speed = 1200. So servo2 and servo3 rotate in OPPOSITE directions with the same magnitude. Since servo2 is on the right-rear and servo3 on left-front (if local labels are right), that's consistent with mirrored mounting: the same "forward step" requires opposite PWM offsets on the two sides.

Hmm wait. That's an important point for the user's question 3 & 4. Let me be careful and factual:

In the 360° version (the direct ancestor with calibration), front() uses:
- servo2: 1500 + speed (1800), servo3: 1500 - speed (1200)
- servo1: 1500 - speed (1200), servo4: 1500 + speed (1800)

So servo2 & servo4 get +300 while servo1 & servo3 get -300 (modulo offsets). This is the mirrored scheme: within each side, the front and rear legs receive OPPOSITE offsets (servo1 -300 / servo2 +300 on one side; servo3 -300 / servo4 +300 on the other side).

For the 180° version, 140/40: servo2=140, servo3=40, servo1=40, servo4=140. So servo2 & servo4 = 140, servo1 & servo3 = 40. That maps exactly onto the 360° pattern: servo1,3 = "minus" direction → 40; servo2,4 = "plus" direction → 140. 90 is center; 40 is 50 below center, 140 is 50 above center. Consistent with the 360 version's ±(speed) around 1500.

So the answer to Q3: In front(), the left-side and right-side legs do NOT all receive the same numbers; servo1(40) & servo4(140) vs servo2(140) & servo3(40). Within a diagonal/opposite pair they're mirrored: 40 vs 140.

Hmm, but I need to state the mapping carefully without over-claiming which physical leg. The original code does not label legs. The local engine.html (a local addition, unverified against the original) labels 舵机1=右前腿, 舵机2=右后腿, 舵机3=左前腿, 舵机4=左后腿. I must mark it as "from the local copy's engine.html, not from the original".

Actually wait, is that labeling plausible? Front legs: servo1 (right front) and servo3 (left front). Rear: servo2 (right rear), servo4 (left rear). In front(): servo1=40, servo3=40 (both front legs same), servo2=140, servo4=140 (both rear legs same). And the wiki says "先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出" — legs 2&3 step forward first, then 1&4 push back.

Hmm, so with servo1=40/servo3=40 and servo2=140/servo4=140, the two front legs move together and the two rear legs move together. That's a "bounding"-ish gait. And per the wiki, in the first phase 2&3 move (servo2 140, servo3 40)... 

Actually the phase structure of front() (which is 8 steps):
1. servo2=140, servo3=40 (delay 100)
2. servo1=40, servo4=140 (delay 100)
3. servo2=90, servo3=90 (delay 100)
4. servo1=90, servo4=90 (delay 100)
5. servo1=140, servo4=40 (delay 100)
6. servo2=40, servo3=140 (delay 100)
7. servo1=90, servo4=90 (delay 100)
8. servo2=90, servo3=90

Hmm, this is odd — the wiki says "180度版" front() logic: 2&3 forward, then 1&4 backward... but the code shows servo2=140 & servo3=40 then servo1=40 & servo4=140, then reset to 90, then servo1=140 & servo4=40, servo2=40 & servo3=140, then reset.

So it's a symmetric 4-phase cycle: (2,3) at ±, (1,4) at ∓, reset, (1,4) at ±, (2,3) at ∓, reset. Hmm, that's two "swing" phases and two "return" phases.

OK. I shouldn't over-interpret gait semantics. I'll report the numbers verbatim and describe the pattern factually:
- Within each step, the two legs in a pair receive complementary values (40 vs 140 around the 90 neutral).
- servo1 & servo3 always receive the SAME value; servo2 & servo4 always receive the SAME value.
- In the first half, servo2/servo4 = 140 and servo1/servo3 = 40; in the second half they swap.

And for the 360° original (which has explicit comments), the same phase receives +/-speed around 1500, confirming the "same side legs get mirrored counters" pattern... hmm, actually no: servo2 (one side) +300, servo3 (other side) -300 in the same phase. Let me tabulate the 360 version:

front() 360:
Phase 1 "+30C 2/3": servo2 = 1500+speed+off2L, servo3 = 1500-speed-off3L
Phase 2 "-30C 1/4": servo1 = 1500-speed-off1R, servo4 = 1500+speed+off4R
Phase 3 "0C 2/3": servo2 = 1500-speed-off2R, servo3 = 1500+speed+off3R
Phase 4 "0C 1/4": servo1 = 1500+speed+off1L, servo4 = 1500-speed-off4L
Phase 5 "+30C 1/4": servo1 = 1500+speed+off1L, servo4 = 1500-speed-off4L
Phase 6 "-30C 2/3": servo2 = 1500-speed-off2R, servo3 = 1500+speed+off3R
Phase 7 "0C 1/4": servo1 = 1500-speed-off1R, servo4 = 1500+speed+off4R
Phase 8 "0C 2/3": servo2 = 1500+speed+off2L, servo3 = 1500-speed-off3L

So in the 360 version, servo2 and servo3 ALWAYS get opposite signs in the same phase; servo1 and servo4 also always opposite. Note off1leftpwm = -93, off1rightpwm = -87 (different values for the two directions, which are "left turn compensation" and "right turn compensation" i.e., the compensation for clockwise vs counterclockwise motion). 

Hmm, wait: the naming "engine1offsetleftpwm" with comment "舵机左转补偿" — the value is subtracted when driving in that direction. Since all offsets are negative (-93, -120, -3, -78...), `1500 - speed - offset` = 1500 - 300 + 93 = 1293. And `1500 + speed + offset` = 1500 + 300 - 93 = 1707.

Anyway, that's a 360° servo version (speed control), where calibration differs per servo. Crucially for the user: in the 360 version, the compensation numbers per servo differ wildly (-93, -87, -120, -122, -3, -57, -78, -109) which reflects per-servo speed differences, not mounting mirroring.

For the 180° version, the numbers are purely 40/90/140, meaning "50° from center" in each direction, applied with OPPOSITE sign on the two sides of a diagonal — i.e., the left and right legs are mounted MIRRORED, so the same physical forward step is +50 on one side and -50 on the other.

Hmm, is that the right reading? Let's think: In front() phase 1, servo2=140, servo3=40. servo2 and servo3... if servo2 is right-rear and servo3 is left-front (per local labels), these are diagonal, not left-right. Diagonals in a quadruped are usually the SAME phase (trot). Hmm.

If servo1=right-front, servo2=right-rear, then a right-side pair is {1,2}, and left-side pair is {3,4} (left-front=3, left-rear=4).

In front() phase 1: servo2 (RR) = 140, servo3 (LF) = 40 — a diagonal pair with mirrored values. Phase 2: servo1 (RF) = 40, servo4 (LR) = 140 — the other diagonal with mirrored values.

Hmm interesting. So {servo2, servo4} = 140 and {servo1, servo3} = 40 in phases 1-2. {servo2, servo4} = right-rear + left-rear = both REAR legs. {servo1, servo3} = right-front + left-front = both FRONT legs. So actually it groups by FRONT vs REAR, not by left vs right! Both front legs get 40, both rear legs get 140.

That is consistent with the wiki text: "先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出" — hmm, that says legs 2 and 3 move forward first, then 1 and 4 push back. Under the local labels, 2=RR, 3=LF. That's a diagonal. Hmm, that conflicts with my grouping.

Hmm. Whatever the interpretation, I should present the numbers and note the ambiguity. The key deliverable: state whether left-side and right-side legs receive the SAME or MIRRORED numbers in front()/back().

With local labels (servo1=RF, servo2=RR, servo3=LF, servo4=LR):
- front() phase 1: servo2(RR)=140, servo3(LF)=40 → right and left get DIFFERENT (mirrored) values; within phase 1 the values are mirrored.
- front() phase 2: servo1(RF)=40, servo4(LR)=140 → mirrored again (right front = 40, left rear = 140).

Hmm, so if labels are right: servo1 & servo3 (both front) always same; servo2 & servo4 (both rear) always same. And front-pair vs rear-pair are always complementary (40 vs 140).

So the answer: NOT mirrored per-side; rather grouped front-pair/rear-pair, with the two groups always complementary (40 vs 140, i.e., ±50 around 90). Servo1=servo3 always; servo2=servo4 always.

Hmm, but let me double check with the 360 version to see whether that's consistent. In 360 front(), phase 1: servo2 = 1500+speed (plus), servo3 = 1500-speed (minus). Under local labels: RR = plus, LF = minus → opposite signs on a diagonal. And phase 2: servo1 = minus (RF), servo4 = plus (LR). So in 360, {servo2, servo4} = plus, {servo1, servo3} = minus in phases 1-2. Same as 180: {servo2, servo4} together (plus = 140 = >90) and {servo1, servo3} together (minus = 40 = <90). ✓ Consistent!

So both versions agree: servo1 & servo3 always share the same value; servo2 & servo4 always share the same value; and the two groups are complementary.

Now the physical meaning depends on the actual mounting. The local engine.html says servo1 = 右前腿 (RF), servo2 = 右后腿 (RR), servo3 = 左前腿 (LF), servo4 = 左后腿 (LR). Under this, front legs = {servo1, servo3} = same value always, rear legs = {servo2, servo4} = same value always. So front and rear legs swing in opposite directions at any moment → that's a "bounding gallop" style gait (both front legs together, both rear legs together, 180° out of phase). That's actually a plausible amateur quadruped gait.

Hmm, but is it mirrored (left vs right)? With this mapping, left legs = {servo3, servo4}, right legs = {servo1, servo2}. If mounting were mirrored (left servos mounted as mirror images of right), then "both front legs swing forward" would require opposite values on servo1 (RF) and servo3 (LF) — because the mirror flips the sign. But the code gives them the SAME value (40 and 40). That means either (a) the servos are all mounted in the SAME orientation (not mirrored), so same value = same physical rotation direction; or (b) the mechanical linkage is such that same value produces the same physical swing.

Hmm, and I should be careful: the wiki says "4个电机的转动角度一致" (the four motors' rotation angles are consistent/the same). That's a strong statement in the official docs! And in the 360 section: "4个电机的转动角度一致。" Let me re-read: "所以，为了确保4个舵机能同步，还加入了engineXoffsetXpwm，用于控制各个电机的补偿，这就需要我们耐心去找到适宜的补偿值。4个电机的转动角度一致。"

Context: this is in the 前进 section, after explaining the compensation values needed to make the four servos synchronized (because the 360° servos have imprecise speed). "4个电机的转动角度一致" = "the four motors' rotation angle is the same/consistent" — meaning the four servos are commanded with the same magnitude (speed) in a given phase, just opposite sign. Hmm, ambiguous but it supports the "same magnitude" reading.

So for Q4 (mounting orientation and which value swings a leg forward):
- I did NOT find explicit documentation of mounting orientation (mirrored vs identical) in the original materials I fetched. I must mark it as UNCERTAIN / not found.
- However, the code's "mirrored/complementary" pairing (40 vs 140 around 90) plus the 360° version's explicit "+30C"/"-30C" comments (clockwise vs counterclockwise rotation drive) shows the two opposite-direction drives are needed for a walk cycle. In the 360 version, the servo that needs "plus" (CW, >1500) is servo2/servo4 and the one that needs "minus" (CCW, <1500) is servo1/servo3 — and phases alternate.

Hmm, so actually the pattern in the 360 version is: at a given moment, some servos drive CW and others CCW. That means either mirrored mounting or the mechanical arrangement makes opposite rotation correspond to the same physical swing. Since the comments label them +30C ("30° clockwise") and -30C, and the pairs are (2,3) and (1,4)... 

Hmm, pages. Let me not overreach. The key factual statements:
1. Original found. 
2. Verbatim gait code.
3. Pattern: servo1&3 same, servo2&4 same, groups complementary (40 vs 140). So left/right pairs (if the local labels are correct, left = {3,4}, right = {1,2}) are NOT all the same; but the mirroring is by diagonal/anti-phase grouping, and importantly the code never uses "same value for all four" during motion.

Hmm wait, the user's question 3 explicitly asks: "State explicitly whether in the original, the left-side and right-side legs receive the SAME servo numbers or MIRRORED/complementary numbers (e.g. 40 vs 140) in front()/back()."

Let me answer precisely with the data: In front(), servo1 and servo3 receive identical values throughout (both 40, then both 90, then both 140...), and servo2 and servo4 receive identical values throughout — but the {1,3} group and the {2,4} group always receive complementary values (one group 40, the other 140). So at any instant during front(), two legs are at <90 and two legs are at >90 (except during the neutral 90 transitions).

Hmm, but "left-side" and "right-side": I can't definitively assign left/right from the original. The original materials don't say. The local engine.html says servo1=右前腿, servo2=右后腿, servo3=左前腿, servo4=左后腿 — and if that's taken at face value, left-side legs are servo3 and servo4, right-side legs are servo1 and servo2. In front(): servo1=40, servo2=140 (right side: 40 & 140 = complementary), servo3=40, servo4=140 (left side: 40 & 140 = complementary). So within each side, the front and rear legs are complementary (40 vs 140), and the two sides are IDENTICAL to each other (left mirrors right in value: LF=RF=40, LR=RR=140). 

Hmm! That's a clean answer: left side and right side receive the SAME values (not mirrored) — i.e., servo1 (RF)=servo3 (LF)=40 and servo2 (RR)=servo4 (LR)=140. The mirror/complementary relation is between front and rear within a side.

Hmm, but hold on. Is the local engine.html's leg assignment trustworthy? It's a modification (the engine.html is a local addition, the original V1.1 doesn't have engine.html; the 360 version's engine.html is a calibration page with no leg labels). So the labels come from the person who made the modified copy. They could be accurate (they built the robot) or not.

I'll report: taking the local engine.html's labels (servo1=右前腿/RF, servo2=右后腿/RR, servo3=左前腿/LF, servo4=左后腿/LR) — which are NOT in the original and are unverified — the answer is: left and right receive IDENTICAL values; front and rear within each side receive complementary values (40 vs 140). So the servos are NOT mounted mirrored; all four are mounted in the same orientation, and same-number = same physical swing direction... 

Hmm, but wait. If all four servos are mounted identically (same orientation), then "all front legs swing forward" would indeed need the same value on both front servos. And "the rear legs swing backward" would need the opposite value. That's consistent! So: same-orientation mounting + front/rear anti-phase = bounding gait. 

Hmm, but for a quadruped to walk (bounding is a valid gait for a dog-like robot — front legs together, rear legs together is a "bounding"/"gallop" gait; real dogs do it). OK.

But also — hmm, actually if all four are mounted the same way and front/rear are anti-phase, then in the 360 version the "+30C"/"-30C" comments: phase 1 has servo2 (RR) = +30C and servo3 (LF) = -30C. Hmm, that's diagonal-anti-phase, not front/rear. Wait: servo2 = RR, servo3 = LF. So phase 1: RR clockwise, LF counterclockwise. Phase 2: servo1 (RF) = -30C... let me recompute: phase 2 is "-30C 1/4": servo1 = 1500 - speed - off1R → minus, servo4 = 1500 + speed + off4R → plus. So RF = CCW, LR = CW.

So phases 1-2: {servo2, servo4} = CW (RR, LR = both REAR), {servo1, servo3} = CCW (RF, LF = both FRONT). ✓ Front/rear anti-phase, consistent with the 180° version. 

So the 360's "+30C" phase labels group {2,3} = {RR, LF} and {1,4} = {RF, LR}, which are DIGONAL pairs... hmm, phase label "+30C 2/3" means in that phase servos 2 and 3 are driven with +30C? No — servo2 = +, servo3 = − in phase 1. Hmm, so the phase label "2/3" just names which servos are being commanded in that step, and "+30C" describes... the leading servo? Ambiguous. The label probably describes the direction of the *body* or the *first* servo. Not worth over-analyzing.

My consolidated factual claim: the {servo1, servo3} group and {servo2, servo4} group are always complementary, and both 180° and 360° versions agree. Under the local engine.html labels, {1,3} = both front legs, {2,4} = both rear legs → front legs mirror rear legs. Left and right legs move identically (same values).

Hmm, hold on. Actually let me reconsider: is it {1,3}=front? Local engine.html: 舵机1 (右前腿), 舵机2 (右后腿), 舵机3 (左前腿), 舵机4 (左后腿). Yes: 1=RF, 2=RR, 3=LF, 4=LR. So {1,3} = {RF, LF} = front pair ✓. {2,4} = {RR, LR} = rear pair ✓.

Good. So:
- Front pair (servo1, servo3) always same value.
- Rear pair (servo2, servo4) always same value.
- Front and rear pairs are complementary (e.g., front 40 / rear 140).
- Therefore left and right legs get the SAME numbers (not mirrored), and same numbers across left/right implies all four servos are mounted in the SAME orientation (not mirrored).

Wait, careful — that last inference is my reasoning, not documented. I should mark it as inference: "if the leg labels are correct, then since left and right receive identical values, the servos must be mounted in the same orientation (mirrored mounting would require mirrored values)." I'll flag it as an inference, and note that I found NO explicit statement about mounting orientation in the original docs.

4. Which value swings a leg forward: The official wiki (360° section) says: "前进的逻辑如下，先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出，然后再将2和3腿归位，最后将3和4腿归位即可" (legs 2 and 3 step forward first, then legs 1 and 4 push backward). Hmm, "2和3号腿向前迈出" — legs 2 and 3 move forward. In the code's first step, servo2 = 140 (180° version) and servo3 = 40. Hmm, so "moving forward" corresponds to servo2 = 140 and servo3 = 40?? That would mean for servo2 (>90 = forward) and for servo3 (<90 = forward)? That contradicts my "same orientation" inference. Unless the wiki's "2和3号腿" description refers to the 360° version where these are speed/direction commands, not angles.

Hmm. Actually for the 360 version, "向前迈出" for legs 2 and 3 corresponds to phase 1 where servo2 = +30C and servo3 = -30C. So one goes +, one goes −, and both legs "step forward" — which means the two servos ARE mounted mirrored (or the leg geometry mirrors them). Hmm! That's evidence for mirrored mounting.

Hmm, so there's tension:
- If mounting is mirrored (left mirrored vs right), then left/right legs stepping forward both need opposite servo directions.
- The wiki says legs 2 and 3 step forward in the same phase with opposite drive directions (servo2 +, servo3 −), implying servo2 and servo3 are mirror-mounted → hence "2" and "3" are on opposite sides (left/right), not front/rear.
- But the local engine.html labels say 2 = RR and 3 = LF, which ARE on opposite sides (right-rear and left-front). Diagonally opposite. Hmm, so under the local labels, servo2 and servo3 are on opposite sides AND opposite ends. 

Hmm, so which is it? The original materials don't give leg names, so I cannot resolve front/rear vs left/right assignment definitively. The safest, most useful answer:

- Fact: {servo1, servo3} always share a value; {servo2, servo4} always share a value; the two groups are complementary (40 vs 140 around 90).
- Fact: The official wiki describes front() as "legs 2 and 3 step forward, then legs 1 and 4 push back" — so according to the official text, in the SAME command phase, the pair that steps forward includes servo2 and servo3, which receive OPPOSITE values (140 and 40). That means "step forward" requires opposite servo numbers on servo2 vs servo3 → servos are mounted MIRRORED in the pairs that matter (or at least servo2 and servo3 are mounted opposite to each other).
- Therefore: mirrored/complementary numbers (40 vs 140), NOT the same numbers, for the legs that move together in the official described gait.

Hmm, that's a nice resolution: The pairs that move together are {2,3} and {1,4} (diagonals), and they receive complementary values. So the answer to Q3 is: MIRRORED/complementary, and the grouping is diagonal / by the official text.

Hmm, hmm. Let me re-read the official text once more: "前进的逻辑如下，先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出，然后再将2和3腿归位，最后将3和4腿归位即可。"

Reading the code's phase order:
Phase 1: servo2=140, servo3=40 (delay 100)
Phase 2: servo1=40, servo4=140 (delay 100)
Phase 3: servo2=90, servo3=90 (delay 100)
Phase 4: servo1=90, servo4=90 (delay 100)
Phase 5: servo1=140, servo4=40 (delay 100)
Phase 6: servo2=40, servo3=140 (delay 100)
Phase 7: servo1=90, servo4=90 (delay 100)
Phase 8: servo2=90, servo3=90

Official description: (a) 2和3腿向前迈出, (b) 1和4腿向后蹬出, (c) 2和3腿归位, (d) 1和4腿归位.
Matching: (a) = phase 1 (2,3 move: 140, 40), (b) = phase 2 (1,4 move: 40, 140), (c) = phase 3 (2,3 return to 90), (d) = phase 4 (1,4 return to 90).

Yes! That matches perfectly: the described "forward step" is phase 1 where servo2=140 and servo3=40, and the "backward push" is phase 2 where servo1=40 and servo4=140. And phases 5-8 then are a second half-cycle (legs 1,4 step, then 2,3) — the wiki text seems to describe only half the cycle or the description is loose.

Hmm, but that means: "legs 2 and 3 step forward" is achieved by servo2→140 and servo3→40 — OPPOSITE values. So servo2 and servo3 must be mounted mirrored relative to each other (or the linkage mirrors them). So the answer to Q3 is: MIRRORED/complementary — in front(), the legs commanded in the same phase receive 40 and 140 (mirrored around 90), not the same number.

And "legs 1 and 4 push back" = servo1→40, servo4→140 — also mirrored.

So the group structure: {2,3} together = {1,4} later; each group internally mirrored; and {1,3} share values while {2,4} share values (as an algebraic fact of the numbers).

So: servo1 = servo3 (same), servo2 = servo4 (same), and the two groups complementary. Under the official description, the "walking" groups are {2,3} and {1,4} (diagonals), each internally mirrored → consistent with the servos being mounted in a mirrored arrangement where diagonally opposite legs are mounted the same way and adjacent legs mirrored.

Hmm. Honestly, the cleanest defensible statement:
- In front(), the four legs are never all the same. At each step two servos get 40 and two get 140 (i.e., ±50° from the 90° neutral), and the values are complementary/mirrored (40 vs 140).
- Algebraically: servo1 and servo3 always carry the same number; servo2 and servo4 always carry the same number. The two groups are always opposite.
- The official wiki states the forward step is legs 2 and 3 moving together, receiving OPPOSITE commands (140 on servo2, 40 on servo3) → so the same-number-vs-mirrored answer is: mirrored (complementary) for concurrently-moving legs.

For Q4: I could not find explicit docs on mounting orientation. The closest evidence: the 360° version's comments label drive directions "+30C"/"-30C" (clockwise/counterclockwise) and, in a given step, servo2 is driven +30°CW while servo3 is −30°CCW, and servo1 is −CCW while servo4 is +CW. If the two legs in a step swing the same way mechanically, these servos must be mounted in opposite (mirrored) orientations. Also, which value swings a leg forward: per the wiki, the forward step is servo2 = +30C (>1500, or 140 in the 180° version) and servo3 = −30C (<1500, or 40). So for servo2/4 (one orientation group), >90 (i.e., 140) = forward; for servo1/3 (the other group), <90 (i.e., 40) = forward. Hmm — careful: in phase 1 servo3 = 40 = "forward" per the wiki, and in phase 2 (the "push back" phase) servo1 = 40 = backward and servo4 = 140 = backward. So the same number 40 means "forward" for servo3 but "backward" for servo1 — which is consistent with mirrored mounting of 1 vs 3, and same mounting of 1 and 4? Hmm, but 4 = 140 = backward in phase 2, and 2 = 140 = forward in phase 1 — mirrored for 2 vs 4? That contradicts "same mounting" unless the gait is diagonal-trot where opposite diagonal legs are in anti-phase.

Hmm, this is getting complicated and speculative. Let me be disciplined:

FACTS (verifiable):
1. front() numbers as given; the algebraic invariants (1≡3, 2≡4, groups complementary) — verifiable by reading code.
2. Official wiki text: "先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出" — legs 2&3 step forward, then legs 1&4 push back.
3. 360° version comments: "+30C" for the servo2/servo3 step (servo2 driven >1500 i.e. CW, servo3 <1500 i.e. CCW), and the offsets include both "left" and "right" compensation per servo (engineN offsetleftpwm / offsetrightpwm), used with opposite signs.

INFERENCE (mark as such): since legs 2 and 3 step forward together while receiving opposite drive directions (140 vs 40; or +30°CW vs −30°CCW), and legs 1 and 4 likewise, the servos in each stepping pair are mounted in opposite/mirrored orientations. Under that reading, for the servo mounted like #2/#4 (the "plus" group), >90 swings forward; for the servo mounted like #1/#3 (the "minus" group), <90 swings forward. But I did not find an explicit statement of mounting orientation in the original documentation, so treat that mapping as an inference.

Hmm, actually, is there any chance the two legs in a stepping pair are the SAME side (front+rear)? The user's question 3 presupposes that "left-side and right-side legs" is the relevant grouping. If the local labels are right (1=RF, 2=RR, 3=LF, 4=LR), then stepping pairs {2,3} = {RR, LF} = diagonal and {1,4} = {RF, LR} = diagonal. Diagonal pairs with opposite drive = TROT gait (diagonal legs move together) ✓ which is the most natural quadruped gait, and each diagonal pair would need mirrored mounting if the legs mirror across the body... hmm, a diagonal pair (e.g., right-rear and left-front) — mirrored? Perhaps.

And in that case, left side = {3, 4} = {LF, LR}: in phase 1-2, servo3 = 40 and servo4 = 140 → opposite values → within the left side, the front and rear legs are opposite (as needed for a trot: left-front and left-rear are in anti-phase). Right side = {1,2} = {RF, RR}: servo1 = 40 and servo2 = 140 → also opposite ✓. So under the trot reading, left side and right side receive IDENTICAL values (servo1=servo3=40 for the "front-diagonal"... hmm, servo1 (RF) = 40 and servo3 (LF) = 40 ✓; servo2 (RR) = 140, servo4 (LR) = 140 ✓). So left/right are the SAME (not mirrored), and the mirror relation is front-vs-rear!

Ugh — so the answer to Q3 depends on the leg labeling:
- If {1,3} = both front (as local labels say): left/right receive the SAME numbers; front/rear mirrored.
- If instead the stepping pairs {2,3} and {1,4} are the diagonals (as local labels say: 2=RR, 3=LF is indeed a diagonal ✓, 1=RF, 4=LR is indeed a diagonal ✓): then again left/right = same values, front/rear = mirrored.

Both readings agree! Under local labels: left/right get the same values; the mirroring is ALWAYS between front and rear legs within each side (RF=40/LF=40 vs RR=140/LR=140). 

But the official wiki says legs 2 and 3 step forward TOGETHER, and legs 1 and 4 push back together — i.e., the pairing for stepping is {2,3} = {RR, LF} and {1,4} = {RF, LR}. Under local labels, {2,3} = one diagonal, {1,4} = the other diagonal. For a trot, diagonal pairs move together — ✓ consistent. But then a "forward swing" for the diagonal requires servo2 (RR) = 140 while servo3 (LF) = 40, i.e., mirrored drive for a diagonal pair. That means the mounting is not simply "all four identical"; it's mirrored between diagonal members... which is exactly consistent with local labels IF the servos are mounted with left side mirrored (LF mirrored vs RF) AND front mirrored vs rear (RR mirrored vs RF)... 

Let's test: mirrored mounting means "left legs mirror right legs" AND "front legs mirror rear legs"? If a leg's forward swing requires +X when mounted one way and −X when mounted mirrored. For RF (servo1): forward = ? For LF (servo3): mirrored → forward = opposite of RF's. For RR (servo2): mirrored across front/rear vs RF → forward = opposite of RF's. So LF and RR both = opposite of RF → LF and RR drive the SAME direction for a forward swing ✓ matches phase 1 (servo2=140, servo3=40)? No! Phase 1 has servo2=140 and servo3=40 — OPPOSITE. ✗

Hmm. So under local labels, phase 1 has servo2 and servo3 opposite, and the wiki says 2 and 3 both step FORWARD. So servo2 and servo3 must NOT be mirror-mounted: they must be SAME-mounted. So {2,3} are same-mounted and {1,4} are same-mounted, and the two groups are mirror-mounted relative to each other. Under local labels, {2,3} = {RR, LF} same-mounted = a diagonal; {1,4} = {RF, LR} = the other diagonal, also same-mounted internally. So diagonal legs mount the same, anti-diagonal legs mount mirrored. That's exactly the "trot with mirrored diagonals" arrangement... plausible physically? Meh, unusual.

I think the cleanest way to report this is to give the FACTS and explicitly flag the interpretation as uncertain, since the original does not document leg labeling or mounting orientation. The user wants to know whether numbers are same or mirrored: answer = COMPLEMENTARY (40 vs 140) for the two legs that move together in the official described step, and the algebraic grouping is {1≡3} and {2≡4}. And I should be explicit that the original never assigns left/right labels to servo1..4, so "left vs right" cannot be answered from the original alone; the only left/right labeling is in the local (modified) engine.html.

That's the honest answer. Let me also check whether the original's data folder (V1.1) has any servo->leg mapping in control.html/index.html — no, likely not.

Also let me double check the 360 version's engine.html calibration page more: it has "电机左转90度" and "电机右转90度" buttons with left90/right90 which drive all four servos one full rotation CW/CCW for 1 second. Let me check left90()/right90() implementations in the 360 version, to see the per-servo signs — that could reveal mounting orientation! If all four servos are commanded with the SAME sign in left90 (e.g., all "1500 + speed"), then all servos are mounted the same way; if signs differ, mounting differs.

That's a great test. Let me look at the 360 version's left90()/right90().

Also the 180° version (V1.1) doesn't have left90/right90 (per my extraction, they were "NOT FOUND"). Correct — the 180° version can't do continuous rotation.

Let me check the 360's left90/right90.

</details>

- 🔧 **Bash** `{"command": "S=/c/Users/UserX/AppData/Local/Temp/s4s; cd $S\nnode -e \"\nconst fs=require('fs');const s=fs.readFileSync('v360/EDA-Robot/src/main.cpp','utf8');\nfor(const n of ['left90','right90']){\n const re=new RegExp('void\\\\\\\\s+'+n+'\\\\\\\\s*\\\\\\\\(\\\\\\\\s*\\\\\\\\)\\\\\\\\s*\\\\\\\\{');\n const m=re.exec(s); if(!m){console.log(n,'NOT FOUND');continue;}\n let i=m.in …[截断,原长409]` → `left90 NOT FOUND right90 NOT FOUND`

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:45）

One key check remains: the 360° version's `left90()`/`right90()` reveal whether all four servos share a mounting orientation.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4.1-flash）</summary>

The 360 official zip's main.cpp may not have left90 - it's the older version. The wiki mentioned left90/right90. The oshwhub page showed left90/right90 exists in the updated version. Anyway I have enough.

Let me do one last check — the key question #3 and #4 about mirrored vs same numbers. In front():
- servo2.write(140), servo3.write(40) — 2 and 3 get opposite numbers
- servo1.write(40), servo4.write(140) — 1 and 4 get opposite numbers

And there's the comment in the GH mirror version: `servo3.write(40); //左前向前旋转50度` and `servo2.write(140);//右后向前旋转50度`. That's from pluckypioneer's mirror (referencing "左前" and "右后").

Let me check the local/wikis for leg-to-servo mapping. The wiki software page says "先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出" - legs 2&3 step forward, then legs 1&4 push back.

So servo1/servo4 = one diagonal pair, servo2/servo3 = the other diagonal pair. This is a trot gait diagonal pairing.

For question 4 (which value swings a leg forward): In front(), servo2 and servo3 are the first to "step forward" per wiki. servo2.write(140) and servo3.write(40). So for servo2, >90 = forward; for servo3, <90 = forward. Hmm, but that's not necessarily "forward swing" — the wiki says "2和3号腿向前迈出" then "1和4腿向后蹬出".

Actually let me reconsider: In front(), phase 1: servo2.write(140), servo3.write(40) → legs 2,3 step forward. servo2 and servo3 both >90/<90 respectively... wait that means they're mirrored relative to each other.

Phase 2: servo1.write(40), servo4.write(140) → legs 1,4 push back.

So servo1 with 40 = push back, servo4 with 140 = push back. servo2 with 140 = swing forward, servo3 with 40 = swing forward.

So for servos 1 and 3: <90 = forward swing (40), >90 = backward push (140).
For servos 2 and 4: >90 = forward swing (140), <90 = backward push (40).

Meaning servos 2,3 and 1,4 are diagonally paired but the pairing has opposite signs. Let's define: servo2 (140 fwd) pairs with servo3 (40 fwd) — same leg pair (diagonal), mirrored numbers. servo1 (40 bwd) with servo4 (140 bwd) — mirrored numbers.

Hmm wait. Phase 1 is 2&3 = forward. servo2=140, servo3=40. Both forward but opposite values ⇒ 2 and 3 are mirror-mounted. Phase 2 is 1&4 = back. servo1=40, servo4=140. Both back but opposite values ⇒ 1 and 4 are mirror-mounted. 

Also phase 3 uses 1&4 again: servo1=140, servo4=40 → these should be "forward" now (the second half of the cycle reverses).

So: servos 1,3 have the same polarity as each other; servos 2,4 have the same polarity as each other; and {1,3} is opposite to {2,4}. And 2&3 are in the same diagonal pair but opposite signs... 

Hmm, that's contradictory. Let me re-check the diagonal pairing. In a trot gait, diagonal pairs move together: FL+RR, FR+RL. The wiki says "2和3号腿" together and "1和4腿" together. So the pairs are {2,3} and {1,4}.

If {2,3} move forward together and {1,4} move back together, but 2 uses 140 and 3 uses 40, then 2 and 3 must be mirror-mounted (opposite orientations). Similarly 1=40, 4=140 for back → also mirrored.

Hmm, but then we'd have 2 and 3 mirrored, and 1 and 4 mirrored. If 1 and 3 are... let's assign: suppose left side = servos 3,4 and right side = servos 1,2 (based on the local engine.html which says 舵机1(右前腿), 舵机2(右后腿), 舵机3(左前腿), 舵机4(左后腿)).

So FR=1, RR=2, FL=3, RL=4. That's a mirror-symmetric assignment: right side = 1,2; left side = 3,4.

Tro: diagonal pairs {FL,RR} = {3,2} ✓ matches wiki's "2和3号腿". And {FR,RL} = {1,4} ✓ matches "1和4腿".

Now, if all four legs point the same way but left/right are mirrored: FL and RL (left side, 3 & 4) mirror FR and RR (1 & 2). So 3 mirrors 1, and 4 mirrors 2.

Check front(): servo2=140 for fwd, servo3=40 for fwd. If 3 mirrors 1, and 2 mirrors 4 — 2 and 3 are diagonal (FL & RR) which are NOT mirrored relative to each other in a plain left/right mirror. Hmm.

Actually, in a mirror-symmetric build, diagonal legs FL & RR have the SAME chirality (rotating both 180° about the body's vertical axis maps FL→RR). A mirror flips chirality. So FL and RR would rotate in the same direction for the same commanded angle → to both swing forward, they need the same sign. But here 2=140, 3=40, opposite signs. So either the mounting isn't a simple mirror, or the geometry works differently.

Let me be careful and not over-claim. Let me just report the facts:
- The values are numerically mirrored (complementary about 90°) in specific patterns.
- front(): {2:140, 3:40} together, then {1:40, 4:140} together.
- So within the diagonal pair {2,3}: 140 vs 40 — complementary.
- Within the diagonal pair {1,4}: 40 vs 140 — complementary.
- Also note the "neutral" is 90 for all.

So the answer to Q3 is: the numbers ARE mirrored/complementary (40 vs 140), i.e., servos within the same diagonal pair receive complementary values; they do NOT get the same number.

For Q4: I found documented evidence — the mirror repo's comment in front(): `servo3.write(40); //左前向前旋转50度` and `servo2.write(140);//右后向前旋转50度`. But that's the derivative, not the original. However the original's front() has servo2=140, servo3=40 in the same first phase with the same ordering. Wait, no — in the GH mirror, order is servo3 first then servo2, but values are identical (3:40, 2:140). So both agree.

Hmm, but I should be careful: that comment is from a derived repo which may be a different version. Let me check whether the ORIGINAL has any servo-direction comments. The original's front() comment is only "舵机2旋转至140度 / 舵机旋转至40度". The wiki says 2&3 step forward first.

So combining: servo3 (左前, FL) = 40 swings forward; servo2 (右后, RR) = 140 swings forward. And servo1 (右前, FR) = 40 = push back; servo4 (左后, RL) = 140 = push back.

That gives: for servos 1 and 3 (both front legs? no...). Hmm, 1=FR, 3=FL are both FRONT legs. Hmm interesting.

Let me redo. Phase 1 = legs 2&3 (RR, FL) step forward. servo2=140, servo3=40.
Phase 2 = legs 1&4 (FR, RL) push back. servo1=40, servo4=140.
Phase 3 = 1&4 return to neutral (90).
Phase 4 = 1&4 swing forward? servo1=140, servo4=40 — that's the opposite of phase 2. And phase 5 = 2&3 push back: servo2=40, servo3=140 — opposite of phase 1.

Yes! Phases 3-4-5-6 are the reverse half. So:
- Forward swing: servo2=140, servo3=40 (phase1); servo1=140, servo4=40 (phase4).
- Backward push: servo1=40, servo4=140 (phase2); servo2=40, servo3=140 (phase5).

So: forward for servo1 = 140 (>90), forward for servo3 = 40 (<90); forward for servo2 = 140 (>90), forward for servo4 = 40 (<90).

So servos 1,2: >90 = forward. Servos 3,4: <90 = forward.

Interesting — so left side (3,4) and right side (1,2) are mirrored. 1 & 2 are the right legs (right front/right back) and 3 & 4 are the left legs. Yes! That means: right-side servos (1=FR, 2=RR) swing forward with >90; left-side servos (3=FL, 4=RL) swing forward with <90.

That's the mirror-symmetric mounting. Excellent, this is consistent!

Let me double check with the local engine.html labels: 舵机1(右前腿), 舵机2(右后腿), 舵机3(左前腿), 舵机4(左后腿). Yes.

Let me verify with toplefthand()/toprighthand():
- toplefthand(): servo3.write(0) ... → 0 is <90, and servo3 is FL (left front). ✓ consistent (left side uses <90 for forward/lift).
- toprighthand(): servo1.write(180) ... → 180 is >90, servo1 is FR (right front). ✓ consistent (right side uses >90 for forward/lift).

This confirms the mirror hypothesis. And lie(): servo1=180, servo3=0, servo2=0, servo4=180. Under the mirror model: 1(FR)=180 (>90) = leg forward/extended; 3(FL)=0 (<90) = leg forward. And 2(RR)=0 — hmm, 2 is right side, so <90 would be backward. And 4(RL)=180, left side, >90 = backward. So in lie(), front legs go forward and rear legs go back → splayed flat/lying. Consistent.

dosleep(): servo1=0, servo3=180, servo2=180, servo4=0. Under the model: 1(FR) = 0 = backward; 3(FL) = 180 = backward; 2(RR) = 180 = forward; 4(RL) = 0 = forward. So front legs tucked back, rear legs forward → collapsed/folded. Hmm, or "sleep" = curled up. Fine.

sitdown(): servo2=140, servo4=40 → both middle-position servos... wait sitdown only uses servo2 and servo4 (the REAR legs, RR and RL). servo2(RR)=140 (>90 = forward), servo4(RL)=40 (<90 = forward). Both rear legs rotate forward → rear legs fold forward → sitting. Makes sense!

Great — everything is consistent with a mirrored assembly. Now let me note the gitee/official original also has a comment in the 360 version? Let me check if the 360 original front() has leg comments. Earlier I saw "//+30C 2/3", "//-30C 1/4", "// 0C 2/3", "// 0C 1/4". Those are servo rotation phase markers on the 360 continuous-rotation version.

OK. I have everything I need. Let me also quickly double check there's no separate "front()" in the original with different numbering — no.

One more: the task asked for the attach() lines with pulse widths from the original. Official V1.1: servo1.attach(engine1, 500, 2500) etc. Confirmed. And the 360 original: servo1.attach(engine1) with no pulse width (default 544-2400).

Now let me write the final report. Let me also list the URLs I checked.

Actually, one more consideration: is the oshwhub course-examples/bot-dog the ORIGINAL or is there an earlier one? The oshwhub page's 创建时间 is 2024-11-29, and the 360 zip files are dated 2024-12-03 to 2024-12-24. The Gitee repo was created 2025-04-25. The page says "项目来源于嘉立创平台原作者" per pluckypioneer's README, and the oshwhub page is by "course-examples" which is the 嘉立创官方教程号 (official JLC course account). So this is the official JLC training project — that IS the origin.

Actually the oshwhub project is under account "course-examples" — that's JLC's official course channel. The author attribution: the Gitee repo is JasonYANG170 (JasonYANG17). Hmm, and the 3D CAD link is 嘉立创云CAD.

So the original is the JLC official EDA-Robot course project, published at oshwhub.com/course-examples/bot-dog, with source at gitee.com/JasonYANG170/eda-robot, docs at wiki.lceda.cn. Created 2024-11-29.

Good. Let me write the report now.

Let me also capture the oshwhub "EDA-Robot机器狗" title, and note the derivative repos.

Let me compose the final answer. I should quote verbatim the requested functions. I have them from official_v11.cpp (which equals gitee). The task asked for "original bodies" — I'll give the official V1.1 text verbatim, cleaned of trailing spaces maybe... no, I should quote exactly. I'll strip trailing whitespace for readability but note it. Actually let me quote exactly as-is but without trailing spaces to be readable — I'll note that trailing whitespace was trimmed. Hmm, the instruction says "quote VERBATIM ... all servoN.write() numbers and delay()s in order". The numbers/delays order is what matters most. I'll present the code as-is (I'll trim trailing spaces which are invisible anyway, and state that).

Let me produce the final report.

Let me get `left()` and `right()` and `toprighthand()` tails that got cut off in my earlier output, to be safe. I already have them from the GITEE_ORIGINAL_180V11_gaits.txt read (full). Good.

Also I should mention the important finding that the local modified copy's gait numbers are UNCHANGED from the original — the modifications are elsewhere (LittleFS instead of SPIFFS, new engine.html servo debug page, weather API now.json + hardcoded default key, AP password 12345678, IRAM_ATTR, etc.).

Wait — one thing. The task says "so I can compare servo gait numbers with a modified copy". So the user wants the original numbers to compare. I found they're identical, which is itself the key finding. Let me make sure to state that clearly.

Hmm, but let me double-check the `speed` variable: local has `int speed = 300;` but never uses it. The 360 original uses speed in writeMicroseconds. The local is a 180° version so speed is vestigial. Fine.

Let me also double check the local `sitdown` and confirm identical to original — yes verified token-identical.

Let me write the final report.

</details>

### 🤖 助手（`zcode-general-purpose` deepseek-v4.1-flash，2026-10-09 00:46）

I have everything I need. Here is my report.

## 1. Best-matching original project

**Found it.** The original is the **嘉立创/JLC official teaching project "EDA-Robot机器狗"**:

| Resource | URL |
|---|---|
| **Original project page (oshwhub)** | `https://oshwhub.com/course-examples/bot-dog` — titled *"EDA-Robot机器狗 - 立创开源硬件平台"*, author account `course-examples` (JLC official course channel), created **2024-11-29**, ~173k views, GPL 3.0, BOM cost ~¥30 |
| **Original source repo (Gitee)** | `https://gitee.com/JasonYANG170/eda-robot` (listed on the project page as "代码仓 Gitee"; default branch `main`, tag `v1.0`) |
| **Official docs** | `https://wiki.lceda.cn/zh-hans/course-projects/smart-internet/eda-robot/eda-robot-introduce.html` (+ `-hardware`, `-software`, `-3d`, `-download`) |
| **Official binaries/sources** | oshwhub attachments (direct): `EDA-Robot(180度舵机版)_V1.1.zip` = `https://image.lceda.cn/oshwhub/project/attachments/1cbae5b1f7ed4f9d9209d771c856396a.zip`; 360° version = `.../1f105ddb15984777b02b3d6a41b089f5.zip`; training doc PDF = `.../79ea8924fab54c65a5060b3d5df74900.zip` |

What it is: ESP8266/NodeMCU desktop quadruped, PlatformIO + Arduino, 4× SG90 (pins 14/16/12/13), SSD1306/SSD1315 OLED via U8g2, ESPAsyncWebServer, `data/index.html + control.html + engine.html + setting.html`, emoji bitmaps from OpenMoji, 心知天气 (Seniverse) weather, NTP on `ntp1.aliyun.com`, 2×14500 Li-ion with AMS1117 LDOs, ADC battery divider 750k/100k (ratio 8.4). Two variants: **360° continuous-rotation** (older, needs calibration) and **180° hobby-servo** (V1.0/V1.1, current, "无需校准").

**Your local copy is a modified derivative of the 180° V1.1 line** (not of the Gitee repo directly — it is closer to the official V1.1 zip). Related/derived projects I checked and ruled out as "the original": `github.com/pluckypioneer/eda_robotR1` (a derivative; its own README says *"项目基于嘉立创 EDA 开发平台,项目来源于嘉立创平台原作者"*), `oshwhub.com/ly1919/esp8266-desktop-pet` (a replica), `oshwhub.com/course-examples/eda-robotpro` (the ESP32-S3 upgrade), `github.com/ace-trump-tech/MindPaw`, `oshwhub.com/wwwsss1234/ji-qi-gou`, `14402a/yangyangs-robot-dog`, `jamal121/hello-hachi`.

## 2. Original bodies, verbatim (official 180° V1.1 == Gitee `main`, token-identical)

Trailing whitespace trimmed; comments/numbers/order exactly as published.

```cpp
void front()
{
    servo2.write(140); //舵机2旋转至140度
    servo3.write(40);  //舵机旋转至40度
    delay(100);//延时100s
    servo1.write(40);  //内容同上
    servo4.write(140);
    delay(100);
    servo2.write(90);
    servo3.write(90);
    delay(100);
    servo1.write(90);
    servo4.write(90);
    delay(100);
    servo1.write(140);
    servo4.write(40);
    delay(100);
    servo2.write(40);
    servo3.write(140);
    delay(100);
    servo1.write(90);
    servo4.write(90);
    delay(100);
    servo2.write(90);
    servo3.write(90);
}

void back()
{
    servo3.write(140);
    servo2.write(40);
    delay(100);
    servo4.write(40);
    servo1.write(140);
    delay(100);
    servo3.write(90);
    servo2.write(90);
    delay(100);
    servo4.write(90);
    servo1.write(90);
    delay(100);
    servo4.write(140);
    servo1.write(40);
    delay(100);
    servo3.write(40);
    servo2.write(140);
    delay(100);
    servo4.write(90);
    servo1.write(90);
    delay(100);
    servo3.write(90);
    servo2.write(90);
}

void left()
{
    int num = 0;
    while (num < 3)
    {
        servo1.write(80);
        servo4.write(80);
        delay(100);
        servo3.write(120);
        servo2.write(120);
        delay(100);
        servo1.write(40);
        servo4.write(40);
        delay(100);
        servo3.write(140);
        servo2.write(140);
        delay(100);
        servo3.write(90);
        servo2.write(90);
        servo1.write(90);
        servo4.write(90);
        delay(100);
        servo1.write(100);
        servo4.write(100);
        delay(100);
        servo3.write(60);
        servo2.write(60);
        delay(100);
        servo1.write(90);
        servo4.write(90);
        delay(100);
        servo3.write(40);
        servo2.write(40);
        delay(100);
        servo3.write(90);
        servo2.write(90);
        num++;
    }
}

void right()
{
    int num = 0;
    while (num < 3)//调用一次执行3次
    {
        servo1.write(100);
        servo4.write(100);
        delay(100);
        servo3.write(60);
        servo2.write(60);
        delay(100);
        servo1.write(140);
        servo4.write(140);
        delay(100);
        servo3.write(40);
        servo2.write(40);
        delay(100);
        servo3.write(90);
        servo2.write(90);
        servo1.write(90);
        servo4.write(90);
        delay(100);
        servo1.write(80);
        servo4.write(80);
        delay(100);
        servo3.write(120);
        servo2.write(120);
        delay(100);
        servo1.write(90);
        servo4.write(90);
        delay(100);
        servo3.write(140);
        servo2.write(140);
        delay(100);
        servo3.write(90);
        servo2.write(90);
        num++;
    }
}

void sitdown()
{
    servo2.write(140);
    servo4.write(40);
    delay(3000);
    servo2.write(90);
    servo4.write(90);
}

void lie()
{
    servo1.write(180);
    servo3.write(0);
    servo2.write(0);
    servo4.write(180);
    delay(3000);
    servo1.write(90);
    servo3.write(90);
    servo2.write(90);
    servo4.write(90);
}

void toplefthand()
{
    int num = 0;
    while (num < 3)
    {
        servo3.write(0);
        delay(100);
        servo3.write(30);
        delay(100);
        num++;
    }
    servo3.write(90);
}

void toprighthand()
{
    int num = 0;
    while (num < 3)
    {
        servo1.write(180);
        delay(100);
        servo1.write(150);
        delay(100);
        num++;
    }
    servo1.write(90);
}

void dosleep()
{
    servo1.write(0);
    servo3.write(180);
    servo2.write(180);
    servo4.write(0);
}
```

Note: `toplefthand()` in the original ends with `servo3.write(30)` in-loop and a final `servo3.write(90)`; `toprighthand()` uses `servo1.write(180)/150` + final `90`. The function is `dosleep()` in the 180° version. (In the older **360°** version the same function is spelled `void dosleap()` and uses `servo1.write(0); servo4.write(0); servo3.write(180); servo2.write(180);` — note the **different servo order**, and the motion functions there use `writeMicroseconds(1500 ± speed ± engineNoffset...pwm)` with `int speed = 300; int runtime = 100;` and `delay(500-runtime)`, i.e. the 360° code has no absolute angles at all.)

**Original attach() lines (official V1.1, verbatim):**

```cpp
servo1.attach(engine1, 500, 2500); // 配置舵机PWM，500µs=0度，2500µs=180度
servo2.attach(engine2, 500, 2500);
servo3.attach(engine3, 500, 2500);
servo4.attach(engine4, 500, 2500);
```

with `int engine1 = 14; int engine2 = 16; int engine3 = 12; int engine4 = 13;` and initial `servo1..4.write(90)`. (The 360° version instead calls bare `servo1.attach(engine1);` … `servo4.attach(engine4);` — default 544–2400 µs.)

**Key result for your comparison: your local copy's nine motion functions are numerically IDENTICAL to the original.** I diffed the token stream (every `servoN.write(...)` and `delay(...)` in order): `front, back, left, right, sitdown, lie, toplefthand, toprighthand, dosleep` all match **token-for-token**, against both the official V1.1 zip and the Gitee repo. Only comments/whitespace differ. So the local copy's *gait numbers were not changed* — its modifications are elsewhere (`LittleFS` replacing `SPIFFS`; a **new `engine.html` servo-debug page + `/servo1..4?angle=` routes that do not exist in the original**; a hardcoded default weather key `SB3j4zrxZ7nuRXv8v`; AP password `12345678` vs original `""`; `weather/now.json` vs original `weather/daily.json`; `IRAM_ATTR` vs `ICACHE_RAM_ATTR`; unused `int speed = 300;`). Also `control.html` button labels differ (`回收` → `回收机器狗`, `嘉立创LOGO` → `LOGO`, emoji labels `开心(*^▽^*)` etc.).

## 3. Same numbers or mirrored?

**MIRRORED / COMPLEMENTARY — definitively not the same.** In `front()` the two diagonal leg pairs are driven with complementary values about the 90° neutral:

- Pair **{servo2, servo3}** (diagonal) → `140` vs `40`
- Pair **{servo1, servo4}** (other diagonal) → `40` vs `140`

The two servos of one diagonal pair never receive the same number; they receive values symmetric about 90 (e.g. 40/140, 80/100, 60/120). Same pattern in `back()` (`s3=140,s2=40` / `s4=40,s1=140`), `left()`, `right()`, and `sitdown()` (`s2=140, s4=40`). The official wiki confirms the pairing: *"先将机械狗的2和3号腿向前迈出，再将1和4腿向后蹬出"* — i.e. a diagonal **trot**, pairs {2,3} and {1,4}.

## 4. Servo mounting orientation and which value is "forward"

Evidence from the original author's own code + the official wiki:

- **Right-side and left-side servos are mirror-mounted (not all identical).** The 180° `engine.html`/debug page in your local copy labels the channels `舵机1 (右前腿)`, `舵机2 (右后腿)`, `舵机3 (左前腿)`, `舵机4 (左后腿)` → **1 = right-front, 2 = right-rear, 3 = left-front, 4 = left-rear**, i.e. {1,2} = right, {3,4} = left.
- Deriving swing direction from `front()`: the forward-reaching half drives `servo2=140, servo3=40` and (opposite phase) `servo1=140, servo4=40`; the rearward-push half drives `servo1=40, servo4=140` and `servo2=40, servo3=140`. Therefore:
  - **Right-side servos (1, 2): >90° swings the leg FORWARD; <90° swings it BACKWARD.**
  - **Left-side servos (3, 4): <90° swings the leg FORWARD; >90° swings it BACKWARD.** (mirrored about 90°)
- Cross-checks that fit this model exactly: `toplefthand()` lifts the left-front leg with `servo3.write(0)` (<90), while `toprighthand()` lifts the right-front leg with `servo1.write(180)` (>90); `lie()` splays with `s1=180, s3=0` (both front legs forward) and `s2=0, s4=180` (both rear legs backward) — the classic mirrored left/right layout; `sitdown()` moves only the rear pair `s2=140, s4=40` (both rear legs forward → rear collapses).
- **All four servos share the same 90° neutral rest position**, and the original 180° version explicitly requires no calibration because the servos' internal limiters define the angles (*"180度舵机自带限位器，无需校准"*; "recommended: 180° servos; the 360° program is no longer maintained").
- The original does **not** contain any explicit prose about mounting direction/mirroring anywhere I could find (searched the project page, the wiki hardware/software/3D pages, and the PDF attachment page text) — the mirroring conclusion above is inferred from the code + channel labels, and the "which value is forward" statement is **derived, not quoted** from the author. Treat it as high-confidence inference, not a verbatim author claim.

## 5. Searches performed (all engines that actually responded)

Working: **360/search.so.com**, **CSDN `so.csdn.net/api/v3/search`**, **GitHub REST API**, **Gitee REST API**, **Bilibili search API**, **cn.bing.com** (partially). Blocked/bot-walled: Baidu, Sogou (anti-spider), DuckDuckGo, Google, Brave, Startpage, searx instances, marginalia, Mojeek (403), oshwhub's internal search API (404 on all guessed endpoints — I reached the project via 360 results instead). Queries included: `"EDA-Robot" 机器狗`, `EDA-Robot ESP8266 桌面机器狗 舵机`, `立创开源 机器狗 esp8266 舵机 U8g2`, `立创 EDA-Robot 机器狗 开源`, `hello-hachi 立创 机械狗`, `"回收机器狗"`, `4497595A 机器狗`, plus GitHub/Gitee repo searches for `EDA-Robot`, `机器狗 esp8266`, `quadruped esp8266 servo`. Also fetched the Bilibili result **"EDA-Robot复刻教程" by 丶月丶初, `https://www.bilibili.com/video/BV1ksKf6QEs6`** (a replica tutorial, not the original author's video). Artifacts I left on disk (safe to ignore/delete): `C:\Users\UserX\AppData\Local\Temp\s4s\` containing `official_v11.cpp`, `gitee_main.cpp`, `local_main.cpp`, `v180/`, `v360/`, `att/`.
