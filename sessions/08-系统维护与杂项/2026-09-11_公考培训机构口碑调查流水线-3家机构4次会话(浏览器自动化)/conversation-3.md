## 👤 用户（2026-09-11 02:17）

我需要了解北京古今好客教育这个机构的口碑如何。请你查询各种帖子尤其是小红书，b站等，注意区分广告。提示可以到黑猫，12315等查询其是否有被投诉的记录等等。当遇到需要登录的情况，请给我时间，我帮你登录。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The user wants me to research the reputation of an education institution "北京古今好客教育" (Beijing Gujin Haoke Education). They want me to check various posts especially Xiaohongshu (小红书), Bilibili, etc., and distinguish ads. Also check 黑猫投诉 (Black Cat Complaints), 12315 for complaint records.

This is a web scraping/research task. I should load the memory-web-scraping skill since it's relevant. Also I have browser-use skill available.

The user says if login is needed, give them time to log in.

Let me start by invoking the relevant skill. The memory-web-scraping skill seems highly relevant.

Let me first load the skill to get the accumulated experience about scraping.

Actually, let me think about the workflow. I need to:
1. Search web for the institution's reputation
2. Check Xiaohongshu, Bilibili
3. Check 黑猫投诉, 12315

Let me load the memory-web-scraping skill first.

Per the harness instruction: "When the user types /<skill-name>, invoke it via Skill. Only use skills listed..." — the user didn't type a slash command, but the skill is relevant. The Skill tool description says: "When users ask you to perform tasks, check if any of the available skills match." So I should invoke memory-web-scraping.

Let me do that.

Also per AGENTS.md: 简单任务直接做并用截图/测试快速验证闭环. And 有答案文件禁提前偷看 — not relevant here.

Let me start.

</details>

- 🔧 **Skill** `{"skill": "memory-web-scraping", "args": "调查北京古今好客教育机构口碑，需检索小红书、B站、知乎、黑猫投诉、12315等平台"}` → `<skill_content name="memory-web-scraping"> # Skill: memory-web-scraping # 记忆：网页爬取与内容采集（长期踩坑沉淀） ## 核心策略：两步法 1. **HTTP requests 快筛**：处理非微信/微博/头条的 URL（快，参考成功率 30/42）。 2. **playwright persistent context 兜底**：处理微信（headless=False 必免环境异常）+ 微博/头条（lo_profile）+ HTTP 失败项。 - WebFetch 在多数目标站返回「环境异常」页或混淆 JS → 直接用 playwright persiste …[截断,原长1264]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:17）

我来帮你调查"北京古今好客教育"的机构口碑。这类网络调查任务，我先加载沉淀的爬取经验，然后开始多平台检索。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Now I have the scraping skill. The environment: no python mentioned in AGENTS.md ("无 python"). Hmm, but the web-scraping skill mentions playwright persistent context with python probably. Wait, AGENTS.md says "无 python：docx/PDF 验证链 = soffice..." — that's about the doc verification chain. Let me check if python exists.

Actually, the skill mentions playwright. Let me check the environment first — what tools are available. The user mentioned browser-use skill. Let me check what's available.

Let me check the verification notes and whether node/playwright/python exist.

Let me start with some quick reconnaissance:
1. Check available runtimes (python, node, playwright)
2. Do a web search for the institution

Let me use WebSearch... wait, do I have WebSearch? Looking at my tools: I have WebFetch but not WebSearch listed. Hmm. Actually the Explore agent has WebSearch. But I'm the main agent. Let me check my tool list again: Agent, AskUserQuestion, Bash, CronCreate, CronDelete, CronList, CronUpdate, Edit, EnterPlanMode, ExitPlanMode, Read, Skill, TaskOutput, TaskStop, TodoRead, TodoWrite, WebFetch, Write, SendMessage, ReadSessionContext, mcp__solidworks__*, mcp__node_repl__*.

No WebSearch tool directly. But the browser-use skill allows me to control a browser via node_repl. Hmm, but the browser-use skill says "Main-agent-only Browser Use. The main agent must perform browser work itself."

Actually, wait. The node_repl tool description says "Browser Use only. Run JavaScript in a fresh Node-backed kernel ... to control a browser."

So I can use browser-use to control a browser and search. Let me load the browser-use skill.

Actually, let me first check the environment and think about the approach. Let me also read the verification-notes memory.

Let me do parallel: check python/node, and load browser-use skill? Skill loading should probably be separate. Let me first check environment.

Actually, let me load the browser-use skill since that's likely the key tool for this task (searching Bing/Baidu, visiting Xiaohongshu, Bilibili, 黑猫投诉).

Let me be efficient. First, check environment + read verification notes.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\memory\\verification-notes.md"}` → `1 # 通用验证手段（专案/跨域记忆） 2 3 ## Chrome headless 截图验证 4 - 命令：`"C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --screenshot ...` 5 - **必须绝对路径**（相对路径拒绝执行）。 6 - 中文路径的 file:// URL 需先 URL 编码。 7 - `--virtual-time-budget` 可模拟动画时间。 8 - canvas 动画测试：注入 JS 设 `curStep=末态 / animProg=1 / animating=false` 再截图（虚拟时间 bu …[截断,原长1027]`

- 🔧 **Bash** `{"command": "echo \"--- python ---\"; python --version 2>&1 | head -3; python3 --version 2>&1 | head -3; echo \"--- node ---\"; node --version 2>&1; echo \"--- npm ---\"; npm --version 2>&1", "description": "Check available runtimes"}` → `--- python --- /usr/bin/bash: line 3: python: command not found /usr/bin/bash: line 3: python3: command not found --- node --- v24.13.0 --- npm --- 11.6.2`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

No python available. Node v24 available. I'll use browser-use via node_repl.

Let me load the browser-use skill.

</details>

- 🔧 **Skill** `{"skill": "browser-use:control-browser", "args": "检索北京古今好客教育口碑：小红书、B站、知乎、黑猫投诉、12315"}` → `<skill_content name="control-browser"> # Skill: control-browser # Browser automation (agent.browsers) Use this skill for browser / web-UI tasks: opening and navigating pages, inspecting or reading rendered content, testing local apps, clicking, typing, filling, taking screenshots, and verifying visible page state. If t …[截断,原长17893]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:17）

环境确认：无 python，有 Node v24。这类需要登录墙（小红书）和 JS 渲染站（B站/知乎/黑猫）的调查，我用浏览器自动化来做。先加载浏览器能力说明。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Now let me start the browser. First bootstrap and select backend, get the API documentation.

Let me plan the investigation:

1. **Baidu search** for "北京古今好客教育" + 投诉/口碑/骗子 — get overview
2. **Xiaohongshu** search (needs login likely)
3. **Bilibili** search
4. **知乎** search
5. **黑猫投诉** (tousu.sina.com.cn) — search for the company
6. **12315** — 全国12315平台 (www.12315.cn) — search

Let me set up a todo list first, then start browsing.

Let me create todos.

Actually per guidance, keep it moving. Let me start the browser and do a Baidu search first.

Let me bootstrap.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "搜索引擎初筛：百度/必应检索机构口碑概况", "status": "in_progress", "priority": "high"}, {"content": "黑猫投诉检索投诉记录", "status": "pending", "priority": "high"}, {"content": "12315 平台检索被投诉/处罚记录", "status": "pending", "priority": "high"}, {"content": "小红书检索真实用户评价（区分广告）", "status": "pending", "priority": "high"}, {"content": "B站/知乎检索评价与曝光内容", "status": "pending", "priority": "medi …[截断,原长412]` → `{"oldTodos":[],"todos":[{"content":"搜索引擎初筛：百度/必应检索机构口碑概况","status":"in_progress","priority":"high"},{"content":"黑猫投诉检索投诉记录","status":"pending","priority":"high"},{"content":"12315 平台检索被投诉/处罚记录","status":"pending","priority":"high"},{"content":"小红书检索真实用户评价（区分广告）","status":"pending","priority":"high"},{"content":"B站/知乎检索 …[截断,原长582]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Now bootstrap the browser and search on Baidu.

Let me do the first browser call: bootstrap + get browser + documentation.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nif (!browserPluginRoot) {\n throw new Error(\"Browser plugin root is unavailable in the node_repl host\");\n}\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoo …[截断,原长409]` → `[ { "id": "iab:ff083ecd-b0d0-4cf1-beb0-e36243e254b2", "type": "iab", "name": "ZCode In-app Browser", "capabilities": { "browser": [ { "id": "visibility", "description": "Use to show or hide the browser to the user, and to determine the browser's current visibility. Keep browser work in the background unless the user as …[截断,原长42729]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:17）

开始检索。先做搜索引擎初筛。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Now let me open Baidu and search. First a new tab with Baidu search.

Let me search Baidu for the institution name. Actually, Baidu search results are heavily SEO'd. Let me use Baidu first, then Bing.

Let's navigate.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `=> - link "欢迎进入 百度一下，你就知道，盲人用户进入读屏幕模式请按快捷键Ctrl加Alt加R；阅读详细操作说明请按快捷键Ctrl加Alt加问号键。": - /url: javascript:void(0) - link "到百度首页": - /url: / - img "到百度首页" - textbox: 北京古今好客教育 - button "百度一下" - link "百度首页": - /url: / - generic: 通知 - link "设置": - /url: javascript:; - link "159******72": - /url: https://www.baidu.com/my/index - …[截断,原长32859]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:17）

浏览器已就绪（ZCode 内置浏览器）。先做搜索引擎初筛。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

I have the basic info. Key finding:
- 北京古今好课教育科技有限公司 (note: 好课 not 好客 — likely user mis-remembered the name, or it's a variant). Also known as 古今好课. 曾用名: 北京凯德新传国际文化传媒有限公司. Founded 2014-07-25. Legal rep: 曾庆庚. Registered capital 100万. Address: 北京市朝阳区汤立路201号院3号楼17层2单元2002-2. 参保人数 3人 (only 3 employees insured!). Subsidiary: 好课带学(山东)信息科技发展有限公司.

Important note: The user said "古今好客教育" but the actual company is "古今好课教育". However, there's also a possible "好客" company. Let me note both. Actually "客" vs "课" — pinyin same "ke". The company found is 北京古今好课教育科技有限公司. This is likely what the user means. But I should verify — there might also be a "北京古今好客教育科技有限公司". Let me keep this in mind.

Note the search also showed a map result "北京古今好课教育科技有限公司 1条评论" — interesting.

Also note: the search results are mostly 企查查/爱企查 business info — that's not reputation. I need to search for complaints.

Now let me be careful about "好客" vs "好课". Let me check if a "好客" entity exists too. Actually, the user's phrase "北京古今好客教育" might be a typo. Let me search both.

Let me now do targeted searches:
1. 黑猫投诉: search "古今好课" on tousu.sina.com.cn
2. Search baidu for "古今好课 投诉", "古今好课 骗", "古今好课 退款"
3. 小红书上搜

Let me do the 黑猫 search. The 黑猫投诉 search URL: https://tousu.sina.com.cn/index/search/?keywords=古今好课&t=1

Let me first do Baidu searches with negative keywords since that's fast and revealing. Let me open a new tab for "古今好课 投诉 骗局".

Actually, let me be efficient: run several searches. But each is a browser call. Let me do the 黑猫投诉 search first since it's high-value.

Let me navigate to tousu.sina.com.cn search.

Actually, let me think about which searches give most info:
- Baidu "古今好课 骗" / "古今好课 投诉" / "古今好课 退款"
- 黑猫投诉 site search
- 小红书 search
- B站 search
- 知乎 search
- 12315

Let me do them in parallel where possible? The browser is a single shared thing; but I can do multiple goto's in one cell if I use multiple tabs. Actually let me do a few sequential searches in one JS cell to be efficient — but the skill says at most one state-changing action per observation cycle. However for reading multiple search pages, I can navigate multiple tabs in one cell and snapshot at the end. Hmm, but snapshots would be huge.

Better approach: do one search at a time but extract only relevant text using locator reads rather than full snapshot, to save context.

For search result pages, I could use a targeted read. But the snapshot is the ground truth. Let me instead use a compact approach: navigate to search, then read the results container's innerText. That's a read-only locator read — allowed. Let me identify the container from the first snapshot though.

Actually for Baidu, I already got the structure. The results are under specific divs. Using locator('div#content_left').innerText() would work. But the skill says construct locators only from snapshot facts. In the snapshot, I didn't see explicit ids. Hmm. But `#content_left` is a well-known Baidu id... The skill says never guess selectors. However, I could use a generic approach.

Alternative: rather than fight, note that domSnapshot gives the aria tree which for Baidu search results is verbose. Let me instead use `tab.playwright.locator(...)`? Risky.

Hmm. Actually a cleaner approach for search engines: use Bing or a mobile-friendly search that yields compact DOM. Or use Baidu's "note" search (笔记) which searches 小红书-like content.

Let me reconsider. A very effective approach for this kind of research: use Bing (cn.bing.com) which has cleaner result markup, and search with site: filters.

Actually, let me just use the full domSnapshot but be selective — Baidu results were parseable, just long. The issue is context. Each full snapshot ~4000 tokens. I have budget.

Let me consider using a more compact extraction. I can use `tab.playwright.locator("css=...")`. To comply, I should get a snapshot first and identify a stable selector. In the Baidu snapshot, there were `<h3>` headings with links. The results seem to be in a generic container. I could use `getByRole('heading', {level:3})` and `.allTextContents()` — that gives all result titles compactly! That's a locator built from snapshot facts (headings level 3 existed). And then get the URLs via getAttribute('href').

That's a great compact approach: collect h3 titles across the page. Let me do that for each search engine.

Actually even better: for gathering a broad picture, I can grab all h3 text (result titles) which tells me what content exists. Then drill into the interesting ones.

Let me do that for Baidu search of negative keywords.

Plan:
- Cell A: navigate to Baidu search "古今好课 投诉", return h3 allTextContents + count
- Then drill.

Let me also handle the 好客/好课 ambiguity. Let me quickly check whether "北京古今好客教育" as a distinct entity exists via a Bing search. Hmm, but Baidu search for exactly that returned only 好课 results, suggesting 好客 is a typo/mishearing. I'll note it.

Let me also verify: is there "古今好课" official site? The company does 教育咨询. Likely an online course/教育机构 selling courses (带学 = "guided learning" - 好课带学). This looks like it could be an online education/course-selling company, possibly related to 考研/自考/职业培训.

Let me search for complaints.

Let me do the next cell: Baidu search "古今好课 投诉 退款 骗" and extract h3 titles.

Actually, let me do a combined approach — navigate to Baidu and read h3 titles.

Let me write the cell:

```js
const browser = ...getForUrl(...);
const tab = await browser.tabs.new();
await tab.goto("https://www.baidu.com/s?wd=" + encodeURIComponent("古今好课 投诉 退款 骗局"));
await tab.playwright.waitForLoadState({state:"domcontentloaded"});
await tab.playwright.waitForTimeout(1200);
const h3 = tab.playwright.getByRole("heading", {level:3});
const n = await h3.count();
const texts = await h3.allTextContents();
({n, texts});
```

Hmm but Baidu may show a verification page. Let's try.

Wait — there's a subtlety. In the Baidu snapshot, the news hotlist items were links, and result titles were h3. The hotlist "习近平对青岛货轮火灾..." were links not headings. Good. So h3 should be results (plus maybe some). Let me go.

Let me do this and also get the URLs. I'll collect hrefs too. Actually `allTextContents` then for hrefs I'd need per-element. Let me just get text first.

Let me proceed. Also I want to save the tab id for later. The tabs persist.

Let me run it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `=> { "kw": "古今好课 投诉 退款 骗局", "n": 8, "titles": [ "培训服务与承诺不符要求退款-消费保 ", "培训机构退费骗局全拆解:别为了退学费,反而被骗光积蓄", "网课机构主动要求退费?小心被骗!", "交了学费还能“退”? 西青蜀黍:能有这", "好课在线是骗局吗?查清资质、投诉与退款真相,一文说透 - 百度文库", "网课退费遇坑 假客服 质量差 内容旧 三起真实案例教你咋要回钱", "公考机构真实反馈!线上公考机构古今好课到底怎么样?推荐还是避雷?线...", "警惕!杭州一女子“网课退款”差点被骗100万" ] } Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:17）

已确认机构基本盘，注意一个关键点：**真实名称是"古今好课"（不是"好客"）**。这是一家线上教育/带学公司。现在查投诉与负面评价。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Interesting. Key result: "公考机构真实反馈!线上公考机构古今好课到底怎么样?推荐还是避雷?线..."

So 古今好课 is a 公考 (civil service exam) institution! That's important context. Also "好课在线是骗局吗" — but "好课在线" might be a different company (好课在线 is a known 在线教育 company). Need to distinguish.

Let me look at the "公考机构真实反馈" result — that's a direct evaluation post. Let me get URLs.

Also note the first result "培训服务与承诺不符要求退款-消费保" — 消费保 is a complaint platform! Let me check that.

Let me get URLs of these results. Let me re-read the h3 links' hrefs.

Let me extract hrefs for h3 anchors.

Actually simpler: let me search the specific direct-comparison query on 小红书/知乎/B站.

Let me first get the URL of the 公考机构真实反馈 result and the 消费保 result. Let me do a locator read: h3 → the link inside. Use `tab.playwright.getByRole('heading',{level:3}).nth(i).getByRole('link')`? Or just get the parent link.

Let me get all hrefs from links that contain h3. Hmm.

Alternative: use `tab.playwright.locator('h3 a')` — selector guessing. The skill discourages, but h3 is now snapshot-proven. A selector `h3` is derived from snapshot facts (level 3 headings exist). I think using `h3 a` is acceptable as it's grounded in the observed structure. But to be safe, let me use getByRole chain:

`const links = tab.playwright.getByRole('heading',{level:3}).getByRole('link')` — hmm, that's a descendant combinator via getByRole scoping. Actually PlaywrightLocator.getByRole searches descendants. So h3.getByRole('link') gives the anchor inside each heading. Then allTextContents... but I need hrefs. I can iterate .all() and getAttribute('href').

Let me do that. But careful with strict mode — getByRole('link') inside h3 might match 1. Should be fine.

Let me get hrefs.

Actually, more efficient: let me use the Approach of visiting the promising results directly. The "公考机构真实反馈" one is likely a 知乎/小红书/B站 post. Let me get its URL.

Let me run the href extraction.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长411]` → `=> { "count": 8, "out": [ { "t": "培训服务与承诺不符要求退款-消费保", "h": "http://www.baidu.com/link?url=lhusYEtVYO9ShTGSYeo5GrHsPc4qJAbK7DX_xxkhsAFqhwINV8WdHWvOO5qnojIq" }, { "t": "培训机构退费骗局全拆解:别为了退学费,反而被骗光积蓄", "h": "http://www.baidu.com/link?url=lhusYEtVYO9ShTGSYeo5GxIl_j328Q6ocFcMd9y_j35HYhgRCul1bIj3f1cMKQi1jALZjEuzyKgmQB-Qqul3rsyo …[截断,原长1820]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:17）

公考培训机构——这是关键定性。且出现了"消费保"投诉平台和一篇"真实反馈/避雷"对比帖。提取这些结果链接。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The 消费保 result is very relevant — it's a complaint platform. Let me open it. And the 公考机构真实反馈 result.

Baidu redirect links need to be followed. Let me open the 消费保 one and the 公考 one in separate tabs.

Let me open both, wait, and snapshot. But snapshots are big. Let me open one at a time.

Priority order:
1. 消费保 (培训服务与承诺不符要求退款) — complaint record
2. 公考机构真实反馈 (comparison post)
3. 黑猫投诉 direct search
4. 小红书

Let me open the 消费保 one first. Actually, let me instead go directly to 消费保/黑猫 search pages for the brand, which is more systematic.

消费保: https://www.xfb315.com/ — search. 黑猫: https://tousu.sina.com.cn/

Let me do 黑猫投诉 first: https://tousu.sina.com.cn/search?keywords=古今好课 — hmm, actual URL format. 黑猫投诉 search URL is like https://tousu.sina.com.cn/search/?keywords=xxx&t=1 . Let me just navigate to tousu.sina.com.cn and use its search UI. Actually a direct URL guess may fail. The skill says one focused direct attempt derived from verified facts is allowed, but don't iterate guesses.

Better: navigate to the 消费保 baidu result (verified link) — that's grounded.
And navigate to https://tousu.sina.com.cn/ home then use its search box.

Let me do the 消费保 link first since it's a verified result.

Let me navigate the existing tab (reuse) to the 消费保 link. Actually better to open a new tab so I keep the Baidu results tab.

Let me open new tab, goto the baidu link, wait load, snapshot. The landing might be 消费保 homepage or a specific complaint. Baidu links redirect. Let me snapshot to see.

Given snapshots are large, let me limit: after load, get `document.title`-ish via tab.title() and a compact read. Hmm, I need content. Let me snapshot but the page might be small.

Let me do it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `=> { "url": "https://www.xfb365.com/tousu/100223411", "title": "培训服务与承诺不符要求退款 - 其它 - 消费保" } Structured content: `

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

消费保 (xfb365.com) complaint #100223411 "培训服务与承诺不符要求退款". Let me read the content to see if it's about 古今好课.

Let me snapshot.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `=> - link: - /url: /about - link "消费投诉与法律服务平台": - /url: /about - button "投诉": 投诉 - textbox "搜索相关内容" - generic:  - generic: 登录/注册 - list: - link "首页": - /url: / - link "集体投诉": - /url: /tousu/collective/list - link "法律服务": - /url: /law - link "服务榜单": - /url: /brands/rank - link "企业服务": - /url: /saas - link "行业数据": - /ur …[截断,原长2208]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:18）

命中消费保投诉单。读取内容确认是否涉及该机构。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Excellent! This is a real, detailed complaint. Key facts:
- 2025-07-12 enrolled in 北京古今好课教育科技有限公司 公务员培训课程, paid 9580元
- Complaint: services not as promised (daily planning/supervision, monthly guidance x2, 行测申论答疑, 套卷精练), poor quality, no self-owned copyright courses (only forwarded 网红老师 recorded links), 师资承诺不实 (claimed "体制内老师"), class size promised ≤20 but then said 25
- Requested full refund, refused the 虚高单价 (200元/篇申论批改) deduction
- Status: 已完结 2026-02-10 — auto-closed because 品牌方 never responded ("未获得投诉品牌方的有效回复")
- 1 comment: another user "网友保保_PPK4r8Ja" 7个月前: "啊啊啊，可以和投诉人联系嘛，我在考虑这个机构，看是小公司所以害怕😱"

This is strong evidence: brand refuses to respond to complaints, small company, high price 9580元.

Now, 消费保 is a platform. Let me search 消费保 for all complaints about 古今好课. And 黑猫投诉.

Let me search 消费保 by company/keyword. The search box "搜索相关内容" exists. Let me use it. Or try direct URL pattern for brand search: /brands/... Hmm.

Actually a better systematic approach: 消费保 search URL. Let me use the search box in the UI — type "古今好课" and press Enter.

Let me also do 黑猫投诉.

Let me first search 消费保 for the keyword to count complaints.

Let me do: find the search textbox, fill "古今好课", press Enter.

The textbox "搜索相关内容" — getByPlaceholder? Snapshot shows `textbox "搜索相关内容"` which is accessible name. Use getByRole('textbox', {name:'搜索相关内容'}). Count should be 1.

Let me do it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长411]` → `=> { "url": "https://www.xfb365.com/tousu/100223411", "title": "培训服务与承诺不符要求退款 - 其它 - 消费保" } Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:18）

实锤投诉：9580元公务员培训，机构未回应导致投诉自动关闭。现在系统检索该平台全部相关投诉。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The Enter didn't navigate. Maybe the search requires clicking a button or the Enter key triggers a JS search that opened a new tab. Let me observe tabs.

Let me check controlled + user tabs.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `=> { "controlledTabs": [ { "id": "iab-tab:90e3ac98-44c4-4d7e-991e-873c47f3026e", "viewport": { "width": 1280, "height": 720 }, "title": "北京古今好客教育_百度搜索", "url": "https://www.baidu.com/s?wd=%E5%8C%97%E4%BA%AC%E5%8F%A4%E4%BB%8A%E5%A5%BD%E5%AE%A2%E6%95%99%E8%82%B2" }, { "id": "iab-tab:63171db0-f08b-451f-85be-c214b7d9389b", …[截断,原长782]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Search didn't navigate. Perhaps 消费保 search opens a results page via a specific URL. Let me try the site's own search URL pattern. Common: https://www.xfb365.com/search?keyword=... Hmm, guessing is discouraged.

Alternative: use the "企业" brand page search. Actually 消费保 has a brand search: /brands?keyword=...

Let me instead check the "服务榜单" or use the site's search results. Actually, maybe pressing Enter requires the input to be a form submit. Let me instead look for a search button. The snapshot showed `button "投诉"` and `generic` then textbox. There might be a magnifier icon button (the empty `generic: ` after textbox).

Let me re-snapshot after fill to see if a dropdown/suggestion appeared, or if there's a submit button.

Hmm, this is getting slow. Let me pivot: 黑猫投诉 is the more important platform the user explicitly named. And 消费保 I already have one strong complaint. Let me try 消费保 search via a plausible direct URL once (allowed: one focused attempt), else move on.

Actually — a smarter approach: search Baidu with site: operator to find all 消费保 and 黑猫 complaints.

Let me do Baidu search: `古今好课 黑猫投诉` and `site:tousu.sina.com.cn 古今好课`.

Let me also directly go to 黑猫投诉 search. 黑猫投诉 search URL is typically:
https://tousu.sina.com.cn/index/search/?keywords=%E5%8F%A4%E4%BB%8A%E5%A5%BD%E8%AF%BE&t=1

I'm fairly confident about /index/search/ path from memory of the site. But guessing... The skill allows one focused attempt. Let me instead go to the homepage and use its search UI which is robust.

Actually, 黑猫投诉 site search requires login for some functionality but search is public. Let me navigate to https://tousu.sina.com.cn/ and snapshot to find the search box.

Let me do both: first a Baidu site: search (fast, informative), then 黑猫.

Let me run Baidu searches for:
- "古今好课 黑猫投诉"
- "古今好课 知乎"
- "古今好课 怎么样"

And extract h3 titles. I can do multiple tabs in one cell sequentially and collect only h3 titles (compact). That's efficient. The "one state-changing action per observation cycle" is about avoiding ambiguity; here each navigation is followed by a read in the same cell which is fine for read-only gathering. Let me be pragmatic and gather.

Actually careful: doing multiple navigations in one cell makes it harder to attribute. But I'll return a structured object keyed by keyword. That's fine and efficient.

Let me do that: loop over keywords, for each new tab goto baidu search, wait, extract h3 titles, close tab. Return map.

That's a state-changing action (navigate) per iteration but the observation is captured per iteration in the same cell, attributed by keyword. Acceptable.

Let me include keywords:
1. 古今好课 黑猫投诉
2. 古今好课 知乎 怎么样
3. 古今好课 小红书
4. 古今好课 骗 退费
5. 古今好课教育 评价

Let me run.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长411]` → `=> { "古今好课 黑猫投诉": [ "好课在线_黑猫投诉_新浪网", "烟台 黑猫网投诉-24小时在线咨询,点击进入", "培训服务与承诺不符要求退款-消费保 ", "网课一年不退费能通过黑猫投诉追回吗", "湖南好课优选教育科技有限公司_黑猫投诉_新浪网", "投诉好课在线_黑猫投诉_新浪网", "高考后好课在线拒绝退款,联系不上客服_K12培训投诉_黑猫投诉_新浪网", "河南好课教育信息咨询有限公司 - 百度百科", "库课网校_黑猫投诉_新浪网" ], "古今好课 知乎 怎么样": [ "公考机构真实反馈!线上公考机构古今好课到底怎么样?推荐还是避雷?线...", "历史老师被学生戏称“内阁首辅”|历史老师|知乎_新浪新 …[截断,原长1446]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:18）

搜索框未跳转，改用百度 site 检索 + 多关键词情报收集。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Key finding: The "公考机构真实反馈!线上公考机构古今好课到底怎么样?推荐还是避雷?" appears multiple times — likely a 知乎/B站 post. Let me open it.

Also: BOSS直聘 and 职友集 have employee reviews of 北京古今好课教育科技. Those are valuable (employee perspective).

Notably, there's NO 黑猫投诉 result for "古今好课" specifically — the 黑猫 results are for 好课在线 (different company), 湖南好课优选, 河南好课教育, 库课网校. So 古今好课 may not have 黑猫 records. But I should search 黑猫 directly to confirm.

Important: I must distinguish 古今好课 from 好课在线/湖南好课优选 etc. Different entities.

Let me now:
1. Open the "公考机构真实反馈" post
2. Open 职友集 / BOSS直聘 for 古今好课
3. Directly search 黑猫投诉

Let me open the 公考机构真实反馈 post first. I need its URL. Let me re-run that search and get the href.

Actually, hmm — this "公考机构真实反馈!...推荐还是避雷?线..." might itself be an SEO/ad post by the company (title pattern "推荐还是避雷" is a common 知乎 marketing title). I'll need to judge.

Let me get its URL. Let me search again and capture hrefs of that specific result.

Let me do: goto the same search "古今好课 知乎 怎么样", get h3 links with hrefs.

Actually more direct: search "公考机构真实反馈 古今好课" and get hrefs.

Let me combine: run the search and return hrefs for all h3 links, so I can pick.

Let me do it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长411]` → `=> { "out": [ { "t": "公考机构真实反馈!线上公考机构古今好课到底怎么样?推荐还是避雷?线...", "h": "http://www.baidu.com/link?url=dZ5sKuBJOzZ5v_h-TBckZLLw5cfW23PSrlxXREAE_3g3HbnNpYtZePP5LNK3-FJlKqNZqcTwY5AiLYdRmBmWg_" }, { "t": "公考机构真实反馈!线上公考机构古今好课到底怎么样?推荐还是避雷?线上公...", "h": "http://www.baidu.com/link?url=J4aZuSkgmxNNbQrBGkvwcPFBI3ybwVnasJq_HAWDs5j5uQB …[截断,原长2894]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

There's a very relevant result: "被投诉最多的三家线上公考机构,避雷避雷避... 来自公考柿子学姐避..." — a Weibo post from "公考柿子学姐避坑". And "普通家庭就别报这两家公考机构了最近... 来自公考柿子学姐避坑...". These 小红书/微博 posts could name 古今好课.

Let me open these:
1. "被投诉最多的三家线上公考机构,避雷避雷避" (公考柿子学姐避坑)
2. "...粉笔、大斌、蓝图、金标尺等50家公考机构靠谱吗(含100%真实吐槽)" — a 50-institution roundup, very relevant
3. The 古今好课 evaluation post

Let me open a few in parallel tabs and snapshot. But content might be long. Let me open them one by one but read titles/compact.

Hmm, this is getting long. Let me be strategic. Let me open the "50家公考机构靠谱吗(含100%真实吐槽)" — could contain 古今好课 mention. And the 公考柿子学姐 posts.

These are likely 微博 or 小红书 posts. Let me open and see.

Let me open 3 tabs in one cell: goto each, wait, then read title + body text via locator('body')? That's guessing. Hmm. Actually reading body innerText is a locator read on a snapshot-proven role... `body` isn't in snapshot as a role. 

Let me instead just snapshot each — but that's heavy. 

Alternative: get the final URL + title for each, then decide. The final URL tells me the platform (weibo/xiaohongshu/zhihu). Let me do that first — cheap.

Let me open the 5 candidate links and report final url+title.

Links:
a) 公考机构真实反馈... 古今好课 (dZ5sKuBJ...)
b) 被投诉最多的三家线上公考机构 (3_-EpSV6aVtvFbd46sA6yqji8zSWRCf8-IDxIWRB7yxiFIsA73EbYGss-AUkBa8S)
c) 普通家庭就别报这两家公考机构 (3_-EpSV6aVtvFbd46sA6yqji8zSWRCf8-IDxIWRB7yw4c4mEXanw-kpqSaINodcw)
d) 50家公考机构靠谱吗 (J4aZuSkgmxNNbQrBGkvwcX_90vyvBf886WJm5innHd7Q7VbmYn5whvPK6ar0-N38oMvK4ud7ziLryADmnAmnZhBoF3NOcYjmql-yHbtJM2W)
e) 避雷!江苏公考机构 (mdINB0WRrlX4JNlSvRtYbh_3CIQxn8HPoQ9HsJfz3ASh8UmRh3ZFOpCjKRpjT3a_myp7qZ8ttgVVQ0FC7_qWha)

Let me open a,b,c,d and report url+title.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长411]` → `=> { "gongkao_feedback": { "url": "https://zhuanlan.zhihu.com/p/1911808521881785146", "title": "公考机构真实反馈！线上公考机构古今好课到底怎么样？推荐还是避雷？线上公考机构哪家强？ - 知乎" }, "the3": { "url": "https://weibo.com/5829052784/OFVWR8Pti", "title": "微博正文 - 微博" }, "two": { "url": "https://weibo.com/5829052784/OBFYkmWYx", "title": "微博正文 - 微博" }, "fifty" …[截断,原长466]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Now:
- zhihu article about 古今好课 (likely SEO/marketing — "推荐还是避雷" title with keyword stuffing = classic 知乎 SEO ad by the company)
- 2 weibo posts from 公考柿子学姐避坑 — possible real exposure
- 知乎 50家公考机构真实吐槽 roundup

Let me read the two weibo posts and the 知乎 50家 article. Weibo posts might be the key negative evidence. Also the zhihu 古今好课 article to assess if it's an ad.

Let me read the weibo ones first — they're short. Weibo may require login for full content; my memory skill says playwright persistent context works for weibo without login. Here I'm using the IAB.

Let me snapshot the two weibo tabs. Actually weibo often shows "登录" wall for detail pages. Let me try.

Let me do them one at a time to manage context. First "被投诉最多的三家线上公考机构".

I'll snapshot. Let me get the two weibo tabs' ids first... I can find by URL contains weibo.com/5829052784.

Let me snapshot both weibo pages in one cell? That could be heavy if login walls. Let me do one.

Actually, let me be smart: read a compact text extraction. I'll take a snapshot since it's the ground truth. Weibo detail page snapshot should be moderate.

Let me do the "被投诉最多的三家" one.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `=> - navigation: - link "Weibo": - /url: / - link "首页": - /url: / - generic "首页": - link "推荐": - /url: /hot - generic "推荐": - link "视频": - /url: /tv - generic "视频": - link "消息": - /url: /at/weibo - generic "消息": - generic: "1" - link "用户8233874623": - /url: /u/8233874623 - generic "用户8233874623": - img "profile" - link …[截断,原长7354]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Analysis: This 公考柿子学姐避坑攻略 weibo post is a MARKETING/引流 post — it does NOT name 古今好课 by name. It says "某公考", "避雷ji构1️⃣/2️⃣/3️⃣", and ends with "如果你害怕踩雷，被坑，可以找我聊聊" + "刘岩你想了解的机构，我应该可以帮你避开公考报班90%以上的坑！" — Classic lead-generation (引流) account. 5.1万 fans, 2750 posts, posts tons of "避雷" content to attract DMs. The "网页链接" t.cn/A6T5OYXE is likely a lead form.

So this is an example of the "fake 避雷" content the user wants me to identify as ads/引流. It does NOT name 古今好课. Good — I can note that many "避雷" posts are actually 引流 account ads.

Now the second weibo post (普通家庭就别报这两家公考机构了) — probably also from the same account. Likely also 引流.

Let me check the 知乎 50家 roundup and the 知乎 古今好课 article.

The 知乎 "公考机构真实反馈！线上公考机构古今好课到底怎么样？推荐还是避雷？线上公考机构哪家强？" — title is极度关键词堆砌 = almost certainly SEO soft-ad by 古今好课 或 its 推广代理. But I must read it to judge (it might contain real negatives).

Let me read it. Zhihu 专栏 articles are readable without login usually (zhuanlan.zhihu.com/p/...).

Let me snapshot that tab.

Let me find the tab with zhuanlan.zhihu.com/p/1911808521881785146.

Context is getting large. Let me be efficient: read only the article body. I'll snapshot — zhihu article page snapshot should be moderate.

Let me go.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `=> - link "欢迎进入 公考机构真实反馈！线上公考机构古今好课到底怎么样？推荐还是避雷？线上公考机构哪家强？ - 知乎,盲人用户使用操作智能引导，请按快捷键Ctrl+Alt+R；阅读详细操作说明请按快捷键Ctrl+Alt+问号键。": - /url: javascript:void(0) - banner: - link "知乎": - /url: https://www.zhihu.com - navigation: - link "关注": - /url: https://www.zhihu.com/signin?next=%2Ffollow - generic: 关注 - link "推荐": - /url: http …[截断,原长11447]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:19）

这篇微博"避雷榜"实为**引流号**（不点名机构，结尾引导私聊/查口碑）。现在读知乎那篇对比帖判断性质。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

This 知乎 article is CLEARLY an ad/引流文:
- Account "海鸥公考测评" with matching "考公上岸喵上岸版" persona in text (inconsistent — copy-paste template)
- Title: keyword-stuffed with "古今好课" + "推荐还是避雷" + "线上公考机构哪家强"
- Content: all positive/generic ("虽未公开名师阵容，但教学聚焦实战"), no real negatives
- "❌不足之处：扣11并直接点击↓卡片零取" — this is a classic "扣11" (comment "11") engagement-bait to get a lead form link (wjx.cn = 问卷星 form!) 
- Ends with generic tips + wjx.cn questionnaire link = lead collection
- 0 赞同, 11 followers, 49 articles — a content farm account posting 49 similar articles
- Published 2025-05-30 from 内蒙古

So: this is a paid/SEO soft article, NOT a real user review. Important to flag.

Also there was "推荐阅读" with similar 公考网课推荐 articles — the whole niche is full of SEO.

Now let me check the 知乎 50家 roundup (1997634658591061603) — it claims "100%真实吐槽". Need to check whether it's real and whether 古今好课 is mentioned.

Also key platforms still to check:
- 小红书 (needs login — user offered help)
- B站
- 黑猫投诉 (direct search)
- 12315
- 工商 (企查查/爱企查: 经营异常, 诉讼, 行政处罚)
- BOSS直聘/职友集 (employee reviews)

Let me update todos and proceed.

Let me now do the 黑猫投诉 direct search, since it's a user-named priority. And check 职业 reviews.

Let me be efficient with context. For 黑猫, navigate to tousu.sina.com.cn and search.

Actually, let me reconsider the approach for 黑猫. The direct search URL pattern: I recall 黑猫投诉 search is https://tousu.sina.com.cn/index/search/?keywords=xxx&t=1 . Let me try one focused attempt. If it fails, use the UI.

Let me try it, and also in the same cell do the 知乎 50家 article read? No, separate.

Let me try 黑猫.

Actually — better idea: 黑猫投诉 has a company/brand page. But to find it I'd search. Let me just try the search URL.

Let me do: goto https://tousu.sina.com.cn/index/search/?keywords=古今好课&t=1, wait, report url+title, and if it looks like results, snapshot.

Let me combine url/title report first.

Also let me search B站 via its search API-ish page: https://search.bilibili.com/all?keyword=古今好课 — that's a well-known URL. And 知乎 search: https://www.zhihu.com/search?q=古今好课. And 小红书: https://www.xiaohongshu.com/search_result?keyword=古今好课 — needs login.

Let me do 黑猫 + bilibili in one cell (report url/title), then drill.

Let me update the todo first.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "搜索引擎初筛：确认机构为线上公考培训机构“古今好课”", "priority": "high", "status": "completed"}, {"content": "黑猫投诉检索投诉记录", "priority": "high", "status": "in_progress"}, {"content": "12315 平台检索被投诉/处罚记录", "priority": "high", "status": "pending"}, {"content": "小红书检索真实用户评价（需登录，待用户协助）", "priority": "high", "status": "pending"}, {"content": "B站/知乎检索评价（已确认知乎软广，待查B站与真实知乎问答）", "priority …[截断,原长412]` → `{"oldTodos":[{"content":"搜索引擎初筛：百度/必应检索机构口碑概况","status":"in_progress","priority":"high"},{"content":"黑猫投诉检索投诉记录","status":"pending","priority":"high"},{"content":"12315 平台检索被投诉/处罚记录","status":"pending","priority":"high"},{"content":"小红书检索真实用户评价（区分广告）","status":"pending","priority":"high"},{"content":"B站/知乎检索评价与曝光内容","s …[截断,原长1180]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:19）

这篇知乎文是**典型软广**（账号"海鸥公考测评"49篇同质文、"扣11领取"、问卷星引流、0赞同）。继续查黑猫与B站。

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长411]` → `=> { "heimao": { "url": "https://tousu.sina.com.cn/index/search/?keywords=%E5%8F%A4%E4%BB%8A%E5%A5%BD%E8%AF%BE&t=1", "title": "黑猫投诉_网上投诉_新浪旗下消费者服务平台" }, "bili": { "url": "https://search.bilibili.com/all?keyword=%E5%8F%A4%E4%BB%8A%E5%A5%BD%E8%AF%BE", "title": "古今好课-哔哩哔哩_bilibili" } } Structured content: `

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Both loaded. Let me read them. Let me read the 黑猫 search results first (most important for the user).

Let me snapshot the 黑猫 tab. Hmm, 黑猫 search page might be heavy. Let me snapshot.

Actually, to save context, let me try to read a compact portion. But snapshot is required as ground truth. Let me just snapshot the 黑猫 page; if it's just the search box + empty, I'll know there are no results.

Let me do it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `=> - heading "315黑猫投诉-新浪旗下消费者服务平台" [level=1]: - link "315黑猫投诉-新浪旗下消费者服务平台": - /url: / - link: - /url: //weibo.com/ - option "投诉" [selected] - option "商家" - generic: 投诉 - textbox "请输入关键字搜索" - link "消息": - /url: /user/message - navigation: - list: - link "首页": - /url: / - link "集体投诉": - /url: /grp_comp/index - link "红黑榜" …[截断,原长6783]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

黑猫投诉: "共有0条投诉中包含搜索词古今好课" — ZERO complaints on 黑猫 for "古今好课".

This is important but nuanced: 0 complaints could mean (a) genuinely clean, or (b) too small/unknown a company that consumers don't know to file there, or (c) they use different name. Let me also search "古今好课教育" and the company full name "北京古今好课教育科技" to be thorough. Also maybe "好课" is too generic.

Let me also search 黑猫 for "古今好课教育" and for the brand "古今好课教育科技". And "好课带学".

Let me do that. Also, the "商家" tab search (企业) — 黑猫 has a 商家列表 where companies register; if 古今好课 isn't registered, complaints can't be routed.

Let me do 2 more keyword searches on 黑猫 in one cell. I can change the URL keywords.

Also let me read the B站 search results.

Let me do the 黑猫 variant searches + read bilibili in one cell? Context heavy. Let me do 黑猫 variants compactly: I only need the count sentence. I can navigate and read that paragraph's text. The paragraph is like "共有0条投诉中包含搜索词古今好课". I could read it via getByText? Let me just navigate and snapshot... heavy.

Alternative: I can extract via a locator read on the text. Hmm. Let me use a targeted approach: after navigation, use `tab.playwright.getByText(/共有\d+条投诉/)` and textContent. Is `getByText` with regex ok? Yes, TextMatcher accepts RegExp. But is the locator grounded in snapshot? I have snapshot ground truth from the previous page for the same template: the paragraph "共有0条投诉中包含搜索词古今好课". So the pattern is snapshot-proven. Using getByText with a regex for the count is fine.

Let me do that for the variant keywords.

Let me run: keywords = ["古今好课教育", "古今好课教育科技", "好课带学", "北京古今好课"]. For each, goto search URL and read the count text.

Careful: URL encode. Let me build.

Let me run.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长411]` → `=> { "古今好课教育": "共有0条投诉中包含搜索词古今好课教育", "北京古今好课": "共有0条投诉中包含搜索词北京古今好课", "好课带学": "共有0条投诉中包含搜索词好课带学", "古今好课教育科技": "共有0条投诉中包含搜索词古今好课教育科技" } Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:19）

黑猫显示 **0 条投诉**。需交叉验证（换关键词 + 查商家库），避免因名称差异漏检。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Confirmed: 黑猫投诉 has 0 records for all name variants.

Now let me read the B站 search results. Let me snapshot the bili tab.

Then: 12315, 小红书, 工商.

Let me read B站.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `=> - list: - link "首页": - /url: //www.bilibili.com - generic: 首页 - link "番剧": - /url: //www.bilibili.com/anime/ - link "直播": - /url: //live.bilibili.com - link "游戏中心": - /url: //game.bilibili.com/platform - link "会员购": - /url: //show.bilibili.com/platform/home.html?msource=pc_web - link "漫画": - /url: //manga.bilibili.c …[截断,原长44541]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:20）

黑猫全变体均为 0 条。现在看 B站。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

B站 findings: Videos mentioning 古今好课:
1. "古今好课，研学，国图，乐学，高途这些公考机构怎么选靠谱？" — 152 views, 0 comments, UP: 关关上岸版, 2025-07-17, 2:46
2. "带学机构哪家强？上岸时刻，古今好课，好课带学，必腾公考怎么选？" — 48 views, 0 comments, UP: 上岸咨询师小水, 05-13, 2:17
3. "公考机构测评合集之必过，古今好课，慧恒教育，乐学公考哪家值得报？" — 154 views, 0 comments, UP: 考公机构咨询站, 2025-07-25, 1:57

All three are nearly identical format (2 min videos, near-zero views, "怎么选/哪家值得报", UP names like "关关上岸版"/"上岸咨询师小水"/"考公机构咨询站") — clearly a MATRIX of 引流/广告 accounts (机构测评软广), NOT genuine user reviews. Pattern: 公考机构测评 SEO matrix videos.

So B站 has no genuine user reviews of 古今好课 — only marketing matrix content.

Let me verify by checking one of these video pages' descriptions for a contact/lead. Actually the pattern is strong enough, but let me check one to confirm (the 好课带学 one is most relevant since 好课带学 is the subsidiary).

Actually, let me be efficient. I'll note the pattern. But confirming one would strengthen the report. Let me open "带学机构哪家强？上岸时刻，古今好课，好课带学，必腾公考怎么选？" BV1WZ5k6eEj7 and check the description/UP.

Hmm, that costs context. Let me instead prioritize the remaining important items: 12315, 小红书, 工商/诉讼.

Given the user explicitly asked for 12315 and 小红书, and offered login help, let me do those.

For 小红书: needs login. Let me try the search page and see what happens. Per memory skill, xiaohongshu returns ~77 chars without login → login wall. I should open it, confirm the login wall, then ask the user to log in.

Actually — the user said "当遇到需要登录的情况，请给我时间，我帮你登录。" So I should set up the 小红书 page and tell the user to log in. The IAB is visible to the user, so they can scan QR.

Let me also do 12315 (全国12315平台 www.12315.cn) — it requires login too typically for querying. Actually 12315.cn has a public "消费投诉公示" section: https://www.12315.cn/cuser/portal/tscase/... Hmm. There's 全国12315消费投诉信息公示平台 at https://www.12315.cn/ with 公示查询. It may require login.

Let me try 12315 public 公示 search.

Let me do these steps:
1. Open 小红书 search for 古今好课 (to trigger login wall)
2. Open 12315 公示 page
3. Check 工商/诉讼 via 爱企查 or 天眼查 (may need login), or use 国家企业信用信息公示系统 (gsxt.gov.cn) — has captcha.

Let me first do 小红书 + 12315 in one cell (report url/title/compact state).

Let me think about 12315 URL. The 全国12315平台 is https://www.12315.cn/. There's a public 投诉公示 at https://www.12315.cn/cuser/portal/tscase/tscasequery? Hmm guessing.

Actually the official 消费投诉信息公示 platform: https://www.12315.cn/ then 我要查 → 投诉公示. Let me just navigate to https://www.12315.cn/ and snapshot to find the 公示 entry.

Let me do 小红书 first (needs user action, so start it early) and 12315 home.

Let me do it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长411]` → `browser 命令 playwright 超时（32000ms） Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:20）

B站结果为**机构测评引流矩阵号**（2分钟视频、几十播放、0评论、"哪家值得报"模板）。现在打开小红书（预计需登录）和 12315 平台。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Timed out. Possibly one of the navigations hung. Let me check tab state.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `=> [ { "id": "iab-tab:90e3ac98-44c4-4d7e-991e-873c47f3026e", "url": "https://www.baidu.com/s?wd=%E5%8C%97%E4%BA%AC%E5%8F%A4%E4%BB%8A%E5%A5%BD%E5%AE%A2%E6%95%99%E8%82%B2", "title": "北京古今好客教育_百度搜索" }, { "id": "iab-tab:63171db0-f08b-451f-85be-c214b7d9389b", "url": "https://www.baidu.com/s?wd=%E5%8F%A4%E4%BB%8A%E5%A5%BD%E8 …[截断,原长2402]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

All 3 tabs opened successfully (the timeout was just the JS call, but tabs exist). 
- 小红书 search tabs loaded with titles "古今好课 - 小红书搜索" and "古今好课避雷 - 小红书搜索" — titles show, but content likely blocked/limited (needs login).
- 12315 loaded.

Let me read the 小红书 tab to see if login is needed. Let me snapshot.

Note: 小红书 search_result pages without login typically show a login modal. Let me check.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `=> - banner: - link: - /url: /explore?channel_type=web_search_result_notes - textbox "搜索小红书": 古今好课 - img "搜索" - button "创作中心": - generic: 创作中心 - button "业务合作": - generic: 业务合作 - list: - link "发现": - /url: /explore?channel_id=homefeed_recommend - generic: 发现 - link "RED": - /url: /red_video - generic: RED - link "直播": - …[截断,原长13444]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

小红书 IS accessible — the user is LOGGED IN (notification count "2", messages "1", "我" profile link exists → logged in as user 66a356b8000000001d023058). So no login needed! 

Now I can read the content. The search results show (titles):
- "快开学了 好慌" (07-28) 19 likes
- "哆啦宝" 34
- "小浮在备考（上岸版" 21
- "ing" 5
- "の" 12
- "带学喜报+1+1…" by 古今好课带学萌萌 (07-16) 1
- "北京古今好课求信息分享" by 發啊發 (07-08) 4 likes ← this looks like a genuine question
- "古今好课｜成功学员的感谢" by 古今好课教育带学 (05-07) 6 ← official/marketing account
- "用心服务用心带学才是最优解" by 古今好课带学萌萌 赞
- "如何挑选合适的机构～" by 古今好课带学萌萌 赞
- "带学对大家的帮助是实实在在的～" by 古今好课带学萌萌 赞
- "带学的备考指导日常" by 古今好课教育带学 1
- "小红薯6836DF2B" 1
- "猴头菇口服液" 45
- "求推荐考公机构" 1
- "灰灰" 25
- "喜欢睡觉的懒羊羊" 39
- "momo" 4
- "球球老老鼠" 7
- etc.

Note: titles are truncated/noise. The search results don't show note text, only first line sometimes. I need to open the relevant notes to read content.

Key ones to open:
1. "北京古今好课求信息分享" (發啊發, 07-08, 4 likes) — likely a genuine question with answers/comments
2. "带学喜报+1+1…" 
3. "古今好课｜成功学员的感谢" (official marketing)
4. The generic-looking ones (灰灰, 喜欢睡觉的懒羊羊, momo, 球球老老鼠, 哆啦宝, 快开学了 好慌) — unknown content, could be reviews mentioning 古今好课.

Note the search "古今好课避雷" tab — let me also read that.

The titles shown are the first line of the note. Many are just usernames because the layout shows user name link then note link. Actually the structure: `link /search_result/<id>` (the note, no text) then `link "username date"` then count. Some have note titles.

Hmm, actually I mis-read. The pattern is:
- link (note, url /search_result/xxx) — no accessible name (image card)
- link "发啊發 07-08" (user)
- "4" (likes)

So the note titles that appear (like "北京古今好课求信息分享") are the ALT/aria for the image card. Good — those with names are informative.

So results with note titles:
1. "快开学了 好慌" 19
2. "哆啦宝" 34 — hmm, that's a name not a title... Actually "哆啦宝" is the username, meaning the note card had no title (video?). Wait no, the link "哆啦宝 01-07" is the user link. And there's no title. Confusing.

Let me re-read: 
```
- link: /url: /search_result/6a685423000000001d00ea7e...   <- note card (no text = image note)
- link "快开学了 好慌 07-28":  /url: /user/profile/618bf3cc...  <- username
- generic: "19"  <- likes
```
Wait, "快开学了 好慌" is the username?? Then the note has no title. Hmm, but then for:
```
- link: /search_result/6a585dd4000000001100575a
- link "带学喜报+1+1…": /url: /search_result/6a585dd400...   <- this is the NOTE (title "带学喜报+1+1…")
- link "古今好课带学萌萌 07-16": /url: /user/profile/...  <- username
- generic: "1"
```
Yes! So some notes have a titled link (the note's first text line) and others are image cards with no text.

So titled notes:
- "带学喜报+1+1…" — 古今好课带学萌萌 (07-16) 1 like
- "北京古今好课求信息分享" — 發啊發 (07-08) 4
- "古今好课｜成功学员的感谢" — 古今好课教育带学 (05-07) 6
- "用心服务用心带学才是最优解" — 古今好课带学萌萌 赞
- "如何挑选合适的机构～" — 古今好课带学萌萌 06-17 赞
- "带学对大家的帮助是实实在在的～" — 古今好课带学萌萌 06-11
- "带学的备考指导日常" — 古今好课教育带学 09-01 1
- "求推荐考公机构" — 爱吃木瓜 04-23 1
- "这祸害学生数学学习的有毒视频为什么会走红" — 职业数学家在民间 04-28 1001 (irrelevant)

So on 小红书, the top results are dominated by the company's OWN accounts: "古今好课带学萌萌" and "古今好课教育带学" — posting self-promotional content ("带学喜报", "成功学员的感谢", "用心服务"). This is the company's own 小红书 矩阵账号.

The genuine-looking one: "北京古今好课求信息分享" by 發啊發 — a person asking for info. Let me open it and read comments (comments are where the real signal is).

Also "求推荐考公机构" by 爱吃木瓜.

Let me open "北京古今好课求信息分享" note and read.

Note: opening 小红书 note pages shows content + comments. Comments may need login (we are logged in). Let me open it.

Let me get its URL: /search_result/6a4e44b8000000000f031f25?xsec_token=ABkNVTgbDWrftmYI1g1fcmOxMpB8Kbs0-RQi-EG0CF41g=&xsec_source=

I need the full URL with domain: https://www.xiaohongshu.com/search_result/6a4e44b8000000000f031f25?xsec_token=...&xsec_source=

Let me navigate a new tab there. Actually clicking the link is better (preserves referrer). Let me click the link with that href.

Hmm, clicking: the link text "北京古今好课求信息分享". Let me use getByRole('link', {name:'北京古今好课求信息分享'})? That name is the note title link. count should be 1. Then click.

Actually simpler and safer: navigate directly to the full URL (derived from verified page facts = allowed).

Let me do that. The xsec_token is required.

URL: https://www.xiaohongshu.com/search_result/6a4e44b8000000000f031f25?xsec_token=ABkNVTgbDWrftmYI1g1fcmOxMpB8Kbs0-RQi-EG0CF41g=&xsec_source=

Let me open and read.

Also let me read the 避雷 tab, and open the note "求推荐考公机构".

Let me do the "北京古今好课求信息分享" first — highest value.

Let me also consider: the search results are sorted by 综合. Let me also search 小红书 for "古今好课 怎么样" and "古今好课 退费" to find negative notes. And check the 避雷 tab.

Let me be efficient: open the key note + read the 避雷 search tab.

Let me do two things in one cell:
1. new tab → the 求信息分享 note URL, wait, snapshot
2. Can't easily also snapshot the other. 

Let me just do the note now.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `=> { "url": "https://www.xiaohongshu.com/explore/6a4e44b8000000000f031f25?xsec_token=ABkNVTgbDWrftmYI1g1fcmOxMpB8Kbs0-RQi-EG0CF41g=&xsec_source=pc_feed", "title": "北京古今好课求信息分享 - 小红书" } Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:20）

小红书已登录可直接读取。顶部结果多为机构自有账号（"古今好课带学萌萌"等矩阵号）。打开一条真实求助帖看评论区。

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `=> - banner: - link: - /url: /explore?channel_type=web_note_detail_r10 - textbox "手串弹力绳打结教程" - img "搜索" - button "创作中心": - generic: 创作中心 - button "业务合作": - generic: 业务合作 - list: - link "发现": - /url: /explore?channel_id=homefeed_recommend - generic: 发现 - link "RED": - /url: /red_video - generic: RED - link "直播": - /url: …[截断,原长25885]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Excellent! This is genuine 小红书 content. Note: "北京古今好课求信息分享" by 發啊發 (07-08), 13 comments, 4 likes, 1 collect.

Note body: "别人安利的机构，自己是自律比较一般的，带学会更适合我，但是古今好课的信息有点少了，想问问有没有友友报过了解过的，怎么样啊 求求" Tags: #国考 #省考 #教育与教育学 #课程辅导 #北京古今好课 #公考机构 #教育学

Comments (13):
1. "M" (07-13 湖北): "我准备报了" (4 likes)
2. "拾染" (07-20 四川): "我也" + 展开3条回复
3. "电瓶车" (07-08 山东): "去年跟的还行" (1)
4. "咖啡" (07-15 山东): "想问一下宝宝你报的哪个老师啊" (reply)
5. "咸蛋黄芋泥窝窝头" (07-09 湖北): "还行 排的你根本没空玩" (1)
6. "ddd" (08-04 河南): "蹲蹲报了吗"
7. "我是一只柚子🐶" (07-09 云南): "我觉得挺不错的"
8. "策舆" (08-27 四川): "蹲蹲 报了吗 感觉好贵啊"  ← mentions expensive
9. "一怒之下抠掉脚皮贴在了溃疡上" (07-09 山东): "带学？"
10. "北半球的南极企鹅" (07-09 山东): "我报的考研带学辅导"

Key signals:
- Genuine post asking for info, indicating "古今好课的信息有点少了" (little info available) — confirms low online footprint
- Comments are mostly positive/neutral: "去年跟的还行", "还行 排的你根本没空玩" (schedule is packed), "我觉得挺不错的", "我准备报了", "我也"
- One mentions "感觉好贵啊" (feels expensive)
- Many comments from 山东/湖北/四川 — 
- Warning sign: the positive comments could be 水军 (the company's own accounts). Given the company runs 小红书 matrix accounts ("古今好课带学萌萌", "古今好课教育带学"), astroturfing is plausible. But can't prove.

Now let me read the 避雷 search tab (古今好课避雷) to find negative notes. That's the key: are there any 避雷 posts about 古今好课?

Let me read that tab: iab-tab:04763b59-2f73-4297-b7ef-43a188a0c0eb

Also, I should search more specific queries: "古今好课 退费", "古今好课 骗子", "古今好课 靠谱吗", "古今好课带学".

Let me read the 避雷 tab first.

Also note the "猜你想搜: 北京古今好课教育科技有限公司" — so 小红书 links the brand to the company.

Let me read the 避雷 tab.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长411]` → `- banner: - link: - /url: /explore?channel_type=web_search_result_notes - textbox "搜索小红书": 古今好课避雷 - img "搜索" - button "创作中心": - generic: 创作中心 - button "业务合作": - generic: 业务合作 - list: - link "发现": - /url: /explore?channel_id=homefeed_recommend - generic: 发现 - link "RED": - /url: /red_video - generic: RED - link "直播": -  …[截断,原长11534]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:21）

真实帖子：13条评论多为"还行/挺不错/我准备报了"，也有人问"感觉好贵啊"。现在看"避雷"搜索结果有无负面。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The 避雷 search didn't yield specific negative notes about 古今好课 — the results are mostly unrelated (拼多多/欧迪芬/古今内衣 brand confusion — note "古今" is also an underwear brand! "古今拼多多和淘宝区别", "古今和欧迪芬哪个好" — so "古今" causes noise).

Notably there's NO 避雷 note about 古今好课 (the search for 古今好课避雷 returns generic results, not targeted negative posts). One relevant-ish: "攥着父母血汗钱报的考研，就是一场笑话" (162 likes) — but that's likely about 考研 generally, not specifically 古今好课. And "26应届生济南工作".

Let me update todos and do remaining key items:
1. 12315 platform (tab already open) — check it
2. 工商核验: 经营异常/诉讼/处罚 — via 爱企查 (already have some info: 参保3人, 曾用名, 子公司)
3. Check the 小红书 note "古今好课怎么样" search to see if there are more real reviews
4. Check 消费保 for more complaints (their site search)

Let me prioritize: 12315 (user asked), 工商 (user asked), and a couple more 小红书 searches for negatives.

Let me first read the 12315 tab.

Let me update todo list.

Actually, let me be efficient with context. The remaining high-value items:
- 12315 公示 (public complaint disclosure) — search for the company
- 工商: 经营异常名录、行政处罚、诉讼 — 爱企查 page (needs login?) — I have basic info. Let me try 国家企业信用信息公示系统? Captcha heavy. 爱企查 detail page shows 经营异常/行政处罚 if any.
- 小红书: search "古今好课 退费" / "古今好课 怎么样" for more notes.

Let me do 12315 next.

Let me update todos first, then read 12315.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "搜索引擎初筛：确认机构为线上公考培训机构“古今好课”", "priority": "high", "status": "completed"}, {"content": "黑猫投诉：全名称变体均为 0 条", "priority": "high", "status": "completed"}, {"content": "消费保：命中1条9580元投诉（机构未回应自动关闭）", "priority": "high", "status": "completed"}, {"content": "小红书检索：已登录，读取真实求助帖+评论", "priority": "high", "status": "completed"}, {"content": "12315 平台检索被投诉/处罚记录", "priori …[截断,原长412]` → `{"oldTodos":[{"content":"搜索引擎初筛：确认机构为线上公考培训机构“古今好课”","status":"completed","priority":"high"},{"content":"黑猫投诉检索投诉记录","status":"in_progress","priority":"high"},{"content":"12315 平台检索被投诉/处罚记录","status":"pending","priority":"high"},{"content":"小红书检索真实用户评价（需登录，待用户协助）","status":"pending","priority":"high"},{"content":"B站/知乎 …[截断,原长1359]`

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `=> - link "热线办理进度查询": - /url: casualuser/ - text: 热线办理进度查询 - link "请登录": - /url: cuser/ - generic: 2026年09月11日 星期五 - text: 投诉公示 - text: 企业服务 - paragraph: - text: 您购买商品或接受服务 - text: 认为经营者侵犯您的合法权益 - link "我要投诉": - /url: cuser/portal/tscase/notice - text: 我要投诉 - paragraph: - text: 您发现违反 - text: 市场监管法律法规的行为 - link "我要举报":  …[截断,原长1108]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

12315 platform: has "投诉公示" section. The 投诉公示 (complaint disclosure) is a public search — usually at https://www.12315.cn/cuser/portal/tspub/... or via the 投诉公示 tab. The snapshot shows text "投诉公示" and "企业服务" as generic text (not links captured). Let me look for the 投诉公示 link/button.

The snapshot shows `text: 投诉公示` and `text: 企业服务` — these are probably tabs. Let me click "投诉公示".

Let me find it: it's a generic text "投诉公示". I can use getByText("投诉公示") and click. count should be 1.

Let me do that and then see the disclosure search.

Note: 全国12315平台的"投诉公示"页面网址通常是 https://www.12315.cn/cuser/portal/tspub/index — let me just click.

Let me click it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `=> { "url": "https://www.12315.cn/", "title": "全国12315平台" } Structured content: `

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Click didn't navigate. Maybe 投诉公示 opens a new tab. Let me observe tabs.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `=> { "controlled": [ { "id": "iab-tab:11a3f635-fb5e-49c7-8c97-b171710d8784", "viewport": { "width": 1280, "height": 720 }, "title": "全国12315平台", "url": "https://www.12315.cn/" } ], "user": [ { "id": "browser:c6011228-aed4-4746-8310-35d38e15d689", "title": "全国12315消费投诉信息公示平台", "url": "https://tsgs.12315.cn/#/viewport" } …[截断,原长345]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The 投诉公示 opened a USER tab: "全国12315消费投诉信息公示平台" at https://tsgs.12315.cn/#/viewport

Let me claim that user tab and use it to search for the company.

Let me claim it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `=> - generic: 各位消费者、经营者、网友朋友们： - generic: 为减少消费领域信息不对称、优化消费环境，市场监管总局现上线全国12315消费投诉信息公示平台，实现全国市场监管部门处理消费者投诉信息的集中、统一公示。 - generic: 平台公示遵循“谁处理、谁公示”原则，由具体处理投诉的市场监管部门审核发布。公示信息按办结时间、行政区划、行业类别、商品服务类别、问题类别等客观维度自动统计或者排序，公示期限为1年。公众可以查询特定商家投诉情况、掌握实时投诉热点、浏览本地最新投诉。企业可以通过电子营业执照登录平台“企业服务”板块，查看本企业投诉情况。 - generic: 公示平台网址为tsgs.12315.cn， …[截断,原长6297]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:21）

12315 公示平台已打开，接管并检索该机构。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The 12315 public disclosure platform is functional. It defaults to 济南市 region. I need to search for the company name. Search box "请输入企业名称、商品/服务等关键字" + "查询" button.

Note it's region-filtered (济南市). I should switch region to 北京 or search nationwide. Let me first search the company name; if the region filter blocks it, switch to 北京.

Let me fill the search box with "古今好课" and click 查询.

Let me do it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长411]` → `search box count=2 Structured content: `

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Two placeholders match /请输入企业名称/ — there may be a header search and a body search. Let me use a more specific approach: take a fresh snapshot to see the two, or filter.

Let me filter to visible ones. Actually let me scope: maybe one is hidden (in a modal). Let me use `.filter({visible:true})`? LocatorFilterOptions supports visible. Let me try.

Actually, let me get both and check visibility. Let me just snapshot to see. But context…

Let me try: box.filter({visible:true}) then count.

Hmm, filter with hasNotText won't help. Let me use `.nth()` — but skill discourages positional shortcuts. However, filtering by visible is legitimate.

Let me try filter({ visible: true }).

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `Browser tab 'iab-tab:noop' is unavailable Structured content: `

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Oops, that was a mistake — I sent a placeholder call. Let me redo properly: find the tsgs tab in controlled tabs and use filter visible.

Actually the tsgs tab I claimed earlier — after claiming, is it in controlled tabs? Let me list and check.

Let me do a proper call.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `=> [ { "id": "browser:c6011228-aed4-4746-8310-35d38e15d689", "url": "https://tsgs.12315.cn/#/viewport" } ] Structured content: `

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Hmm, the tsgs tab id is "browser:c6011228-..." — it appears in tabs.list() but with a "browser:" prefix (claimed user tab). Let me try tabs.get with that id. Earlier I used browser.tabs.get(info.id) where info was from tabs.list()... Actually earlier when I searched, the tsgs tab was found in tabs.list() with id "browser:c6011228-aed4-4746-8310-35d38e15d689"? No — earlier the search-box fill worked (count=2), so tabs.get succeeded with whatever id I used... wait, in that call I used `list.find(t => t.url.includes("tsgs.12315.cn"))` then `browser.tabs.get(info.id)`. It worked (got to the fill step). So the id works.

Let me now use that id and filter visible.

Let me do: box.filter({visible:true}).count().

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `=> { "count": 2, "info": [ { "i": 0, "visible": true }, { "i": 1, "visible": false } ] } Structured content: `

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Index 0 is visible, index 1 is hidden. Filtering by visible works. Let me use filter({visible:true}).

Let me fill and search.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长411]` → `=> { "matches": 12 } Structured content: `

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

12 matches for "古今好课" — but this could include the search box text itself. Let me read the result list to see actual complaint records. Let me snapshot the results area.

Hmm, careful: the search box now contains "古今好课" which is 1 match; the input's value may not count as text. 12 matches suggests actual results OR the search suggestions.

Let me snapshot to read.

Let me limit context by slicing.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `- generic: 我要投诉 - generic: 全国12315消费投诉信息公示平台 - textbox "请输入企业名称、商品/服务等关键字": 古今好课 - generic:  - button "查询" [active] --- - generic: 更多... - generic: 全国公示信息 - generic: 北京古今好课教育科技有限公司 - generic: 投诉内容：2026年06月09日，消费者周**（手机尾号 3592，用户ID ****7722）反映其于2026年06月09日在小红书通过网购购买网上教育。可能存在售后服务->其他售后服务问题，要求退赔费用。 - button " 详情": --- - …[截断,原长1241]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

MAJOR FINDING: 12315 全国公示信息 — 北京古今好课教育科技有限公司 has **5 条投诉公示** (publicly disclosed complaints):

1. 2026-06-09 消费者周** (手机尾号3592) 在小红书通过网购购买网上教育，售后服务->其他售后服务问题，要求退赔费用 — 公示时间 2026-08-17 14:48:17
2. 公示时间 2026-07-10 09:55:05
3. 公示时间 2026-03-12 14:58:27
4. 公示时间 2026-03-05 10:51:08
5. 公示时间 2026-01-27 09:37:56

Note: The 公示时间 is when published; the actual complaint dates may differ (公示期限1年). Only the first one's 投诉内容 was captured. I need to expand the others. Note that 12315 公示 only covers complaints that were 办结 and 公示 — and 公示 is by 市场监管部门. Also note: 公示 covers recently-closed ones; the earliest here is 2026-01-27 (公示), so this only covers ~1 year (公示期限1年).

Wait — the tooltip says 企业名称中含"古今好课"的结果共5条. So 5 complaints publicly disclosed in the last year. That's much more significant than 黑猫's 0.

I should expand the other 4 entries to read details. Let me click "详情" for each, or scroll and read the full text.

Let me read the full snapshot region for the results. Better: let me get the innerText of the results container. Hmm.

Alternative: the complaint content might be in a tooltip/collapsed. The first entry showed 投诉内容. Others showed only 公示时间 — meaning their 投诉内容 was truncated in my filtered extraction because my filter grabbed lines around matches. Let me redo with a filter that captures all "投诉内容" lines.

Let me just slice the snapshot around "全国公示信息" to the end of results.

Let me do that.

Also note: this 12315 data is important — 5 public complaints. Let me capture all details.

Let me extract a broader window.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `全国公示信息 - generic: 北京古今好课教育科技有限公司 - generic: 投诉内容：2026年06月09日，消费者周**（手机尾号 3592，用户ID ****7722）反映其于2026年06月09日在小红书通过网购购买网上教育。可能存在售后服务->其他售后服务问题，要求退赔费用。 - button " 详情": - generic:  - text: 详情 - generic "公示时间":  - text: 公示时间：2026-08-17 14:48:17 - generic: 北京古今好课教育科技有限公司 - generic: 投诉内容：2026年07月01日，消费者蔡**（手机尾号 3759，用户ID * …[截断,原长1920]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:22）

**重要发现**：12315 公示平台上该机构有 **5 条已办结投诉公示**。提取全部细节。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Excellent! Full 12315 public disclosure data — 5 complaints:

1. 投诉日期 2026-06-09，消费者周**（尾号3592），小红书网购"网上教育"，问题：售后服务->其他售后服务问题，要求退赔费用。公示 2026-08-17
2. 投诉日期 2026-07-01，消费者蔡**（尾号3759），其他平台网购"大学教育服务"，问题：质量->不具备产品应当具备的使用性能而事先未作说明，要求赔偿损失、退赔费用。公示 2026-07-10
3. 投诉日期 2025-12-31（购买 2025-05-31），消费者张**（尾号9305），现场购买"应试培训服务"，问题：合同->经营者利用合同格式条款加重消费者责任，要求退赔费用。公示 2026-03-12
4. 投诉日期 2025-12-26，消费者肖**（尾号1154），电视电话购物及邮购购买"应试培训服务"，问题：合同->其他合同问题，要求退赔费用。公示 2026-03-05
5. 投诉日期 2026-01-19（购买 2025-09-24），消费者邱**（尾号6151），其他平台网购"其他技能培训服务"，问题：合同->经营者拒不履行合同约定，要求停止侵权、核定侵权责任、退赔费用。公示 2026-01-27

This is strong, official, verifiable evidence: 5 public complaints within ~1 year, mostly 合同纠纷/退费, plus 售后服务 and 质量 problems. Consistent with the 消费保 complaint pattern (服务与承诺不符, 要求退款).

Note: 12315 公示 shows only 办结 complaints and 公示期限1年, so the actual number of complaints filed is likely higher.

Now let me do the 工商核验 (business registration): 经营异常, 行政处罚, 诉讼, and employee reviews. Let me also do additional 小红书 searches.

Let me update todos and continue.

For 工商, let me try 爱企查 detail page for the company. I need the URL. Let me search 爱企查 or just navigate to the 爱企查 page found earlier via Baidu. Actually, easier: use the 国家企业信用信息公示系统 (gsxt.gov.cn) — but it has captcha. 爱企查/企查查 detail pages often require login for full data but show 经营异常/行政处罚 in summary.

Let me do: Baidu search "北京古今好课教育科技有限公司 经营异常 行政处罚 诉讼" to find any such records, and open 爱企查.

Actually, a cleaner approach: search 中国裁判文书网 (wenshu.court.gov.cn) for the company — but that requires login now.

Let me use 爱企查 (aiqicha.baidu.com) which is accessible without login for basic info. Let me try its search.

Alternatively 天眼查/企查查 pages can be opened but often gated.

Let me do a Baidu search for the negatives about the company: "北京古今好课教育科技有限公司 行政处罚" and "北京古今好课教育科技有限公司 诉讼".

Let me combine with 小红书 additional searches. Actually let me prioritize:

A) 工商: 经营异常/行政处罚/诉讼 → Baidu search + 爱企查 page
B) 小红书: search "古今好课 退费" and "古今好课带学 怎么样"
C) 员工评价: 职友集/BOSS直聘 (low priority but quick via Baidu)

Let me do A via a targeted 爱企查 visit. Let me get the 爱企查 company page. I'll search Baidu for it.

Let me do a combined Baidu search cell with h3 titles for:
- "北京古今好课教育科技有限公司 行政处罚 经营异常"
- "古今好课 诉讼 裁判文书"
- "古今好课带学 怎么样 知乎"
- "北京古今好课教育科技有限公司 拖欠 工资"

Let me run that, then drill into 爱企查.

Actually, more efficient: go directly to 爱企查's company detail page. Let me find its URL via Baidu. Let me do the Baidu searches and grab hrefs for 爱企查/企查查/天眼查.

Let me run the multi-keyword search with hrefs.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "搜索引擎初筛：确认机构为线上公考培训机构“古今好课”", "priority": "high", "status": "completed"}, {"content": "黑猫投诉：全名称变体均为 0 条", "priority": "high", "status": "completed"}, {"content": "消费保：命中1条9580元投诉（机构未回应自动关闭）", "priority": "high", "status": "completed"}, {"content": "小红书检索：读取真实求助帖+评论", "priority": "high", "status": "completed"}, {"content": "12315 公示：官方 5 条已办结投诉（合同/售后/质量）", …[截断,原长412]` → `{"oldTodos":[{"content":"搜索引擎初筛：确认机构为线上公考培训机构“古今好课”","status":"completed","priority":"high"},{"content":"黑猫投诉：全名称变体均为 0 条","status":"completed","priority":"high"},{"content":"消费保：命中1条9580元投诉（机构未回应自动关闭）","status":"completed","priority":"high"},{"content":"小红书检索：已登录，读取真实求助帖+评论","status":"completed","priority":"high"},{"c …[截断,原长1443]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:22）

12315 官方公示 **5 条投诉**全部拿到。现在做工商核验与补充检索。

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长411]` → `=> { "北京古今好课教育科技有限公司 行政处罚 经营异常": [ "北京古今好课教育科技有限公司怎么样 - 爱企查", "古今- 北京古今好课教育科技有限公司 - 法定代表人/高管/股东...", "北京古今好课教育科技有限公司_主要人员_董事_监事_公司查询...", "北京古今好课教育科技有限公司_主要人员 - 企查查", "北京古今好课教育科技有限公司_古今好课官网_在线技术研发企业...", "北京古今好课教育科技有限公司 - 企业信息", "北京古今好课教育科技有限公司-企业工商信用信息,电话,地址,法人-阿里巴...", "「北京古今好课教育科技怎么样」在公司从工作以来,最...-BOSS直聘" ], "古今好课 诉 …[截断,原长923]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

No specific 行政处罚/诉讼 records surfaced (the 诉讼 search returned generic content about ancient 裁判文书 — no match). This suggests no notable litigation/penalties publicly indexed, OR they're on gated platforms.

Note: "「北京古今好课教育科技怎么样」在公司从工作以来,最...-BOSS直聘" — employee review. Let me check that.

Let me now:
1. Open BOSS直聘 employee review (via Baidu link)
2. Open 爱企查 company page for 经营异常/行政处罚 status
3. Additional 小红书 searches

Let me get the 爱企查 and BOSS直聘 URLs. Let me search and grab hrefs.

Actually, let me directly use 爱企查: https://aiqicha.baidu.com/s?q=北京古今好课教育科技有限公司 . That's a plausible search URL. Hmm, guessing. Let me instead get the URL from Baidu results (verified).

Let me get hrefs for the 爱企查 and BOSS直聘 results.

Let me run a search and extract hrefs for those two.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长411]` → `=> { "out": [ { "txt": "北京古今好课教育科技有限公司怎么样 - 爱企查", "h": "http://www.baidu.com/link?url=KsXnXbuvE-vcWYx9SFDJhTne_yGlQFNcJpgwvPaognozaypJgfDSiCrp6VUPwqEUW6YD3qUXgOw21X6_UQLQLxIZnPIeEBBNgGw4wTYr3cO" }, { "txt": "「北京古今好课教育科技怎么样」在公司从工作以来,最...-BOSS直聘", "h": "http://www.baidu.com/link?url=INsbOkTqCG-IdmAjcFT-HFJQer1wK112Tm0iAD …[截断,原长1587]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Let me open the 爱企查 page and the BOSS直聘 page. Both are valuable:
- 爱企查: 经营异常/行政处罚/参保人数/风险信息
- BOSS直聘: employee review («在公司从工作以来,最...» — a review snippet!)

Let me open both and read. Let me do 爱企查 first.

Let me open both in tabs, then read one at a time.

Let me open 爱企查 + BOSS直聘 + 职友集.

Then read.

Let me do it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长411]` → `=> { "aiqicha": { "url": "https://aiqicha.baidu.com/company_comment_29020189269323", "title": "北京古今好课教育科技有限公司怎么样 - 爱企查" }, "boss": { "url": "https://www.zhipin.com/gongsi/review/40dff379b3f7072d03V_2t69E1A~/SFg4jC7Ix3g5Sj5aGtK0Pw~~.html?_security_check=1_1789064600141", "title": "「北京古今好课教育科技怎么样」在公司从工作以来，最...-BOSS直聘" }, …[截断,原长441]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Let me read the 爱企查 company_comment page (employee/company reviews) and 职友集. 

Actually, "aiqicha.com/company_comment_..." is 爱企查's 评价 page — likely 员工评价/企业评价.

Let me read 爱企查 first.

Let me snapshot the 爱企查 tab.

Note: 爱企查 may require login to see details. Let me see.

Let me read it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `- banner: - link: - /url: / - text:  - textbox "请输入企业名称、品牌名称、核心人员姓名等关键词。如“百度”" - button "查一下" - text: 查企业 - generic:  - text: APP - link "159******72": - /url: //qiye.baidu.com/usercenter/personalcenter?fr=c1009 - generic: 159******72 - link "vip专区": - /url: /usercenter/member?tab=svip&entry=2314002 - img "vip专区" - t …[截断,原长3946]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

爱企查 key data:
- 企业风险: 自身风险 0, 关联风险 0, 提示信息 13
- 参保人数: 3人 (very small)
- 法定代表人: 曾庆庚 (财务负责人、执行董事、经理); 古今 (监事)
- 16个注册商标
- 地址: 北京市朝阳区汤立路201号院3号楼17层2单元2002-2
- 经营范围: 技术推广服务...教育咨询(不含出国留学咨询及中介服务); 计算机技术培训... 出版物零售; 互联网信息服务; 经营电信业务
- 联系电话 <手机号> / <手机号>

Important: 自身风险 0 (no 行政处罚/经营异常 disclosed by 爱企查), but 提示信息 13. No litigation risk flagged.

Note: "小微企业", 参保3人 — a very small company selling 9580元 courses. This matters for risk assessment: small company, low registered capital (100万), only 3 insured employees, yet selling ~1万元 courses. Financial stability risk.

Now let me read the BOSS直聘 employee review and 职友集. These give employee perspective (e.g., 拖欠工资, 离职率).

Let me read the BOSS直聘 one.

Note the BOSS直聘 URL had "_security_check=1" — might show a verification page.

Let me read it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `- banner: - link "BOSS直聘": - /url: https://www.zhipin.com/ - list: - link "首页": - /url: https://www.zhipin.com/yantai/ - link "职位": - /url: https://www.zhipin.com/web/geek/jobs - list: - link "公司": - /url: https://www.zhipin.com/gongsi/ - list: - link "校园": - /url: https://www.zhipin.com/school/ - link "海归": - /url: ht …[截断,原长5691]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:23）

工商核验：自身风险 0、参保仅 3 人、小微企业。现在看员工侧评价。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

BOSS直聘 employee reviews (5 reviews, all from HR/recruiting staff):
1. 高女士 人事经理·2年: glowing (踏实、温暖、有归属感) 
2. 张女士 人事·1年: very long "企业初心" statement - reads like official HR recruitment copy (100%真实透明, 无KPI, 双休...)
3. 马女士 人力招聘专员·2年: "团队氛围轻松愉悦，都是00后...五险一金，双休，年假，不定时下午茶、团建"
4. 桂先生 行政人力总监·9个月: describes interview process, "最后就要运营自己的小红书账号了，只要主动沟通，每天都会有新的学习机会" — **KEY: employees are required to operate their own 小红书 accounts**! This confirms the 小红书 matrix accounts ("古今好课带学萌萌" etc.) are run by employees — i.e., the positive 小红书 content is company-generated marketing (员工运营小红书号). Salary 6k-10k, "对工作会相对更严格，达到标准的成熟员工，一般都不加班".

This is highly relevant to "区分广告": the company explicitly has employees run 小红书 accounts to do marketing. Combined with the 小红书 results showing accounts "古今好课带学萌萌" and "古今好课教育带学" posting promotional content — those are employee-run marketing accounts, not customer reviews.

Also: 未融资, 20-99人 (but 社保参保 3人 — inconsistent; 20-99人 is likely inflated/self-reported), 培训/辅导机构, 26 在招职位 (heavy recruiting — consistent with high turnover / 引流 sales org).

Also note: reviews are all HR/招聘 roles (人事经理, 人事, 人力招聘专员, 行政人力总监) — only HR posting reviews, no 带学老师/销售 reviews. That's a pattern of curated reviews.

Now let me check 职友集 for salary/employee data, and do the remaining 小红书 searches.

Let me read 职友集 quickly.

Actually, let me prioritize 小红书 supplementary search since the user emphasized 小红书. Let me search 小红书 for:
- "古今好课 退费"
- "古今好课 怎么样"
- "古今好课带学"

And check for 避雷/负面 notes.

Let me do the 小红书 searches. I'll do multiple search tabs and extract note titles + usernames compactly.

For 小红书 search results, the note titles are inconsistent. Let me instead collect: all links matching /search_result/ with their accessible names (note titles) and the user names. Compact approach: getByText? Hmm.

Let me just get all links whose href includes "/search_result/" and whose accessible name is non-empty — that gives note titles. Plus links to /user/profile/ give usernames.

Actually simpler: let me extract the snapshot but sliced to the results region, per search.

Hmm, context. Let me do a smarter extraction: use locator to get all element texts of the note-card titles. In the earlier snapshot, note titles appeared as `link "北京古今好课求信息分享"` with href containing /search_result/. So: `tab.playwright.locator('a[href*="/search_result/"]')` — selector guess. Alternatively getByRole('link') then filter by href.

Let me do: all links, then filter those with href containing /search_result/ and non-empty text.

Let me implement and run for 3 keywords.

Let me run.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长411]` → `=> { "古今好课 退费": [ "北京古今好课教育怎么样啊", "教育机构退费而已，你越淡定，反而退的越快", "2026年2月新规，机构退费不退也得退😡", "北京古今好课求信息分享", "避雷某二字考研班，全是套路哈。", "有时候无语的时候，自己会先笑！", "呵呵，某考研线上班吃相怎么这么难看", "2026年4月起，教育机构不退费不用再要了", "带学喜报+1+1…", "原来发疯能让教育机构退费，哈哈哈😁", "教育机构就是不见棺材不落泪，投诉就退费了" ], "古今好课 怎么样": [ "北京古今好课教育怎么样啊", "北京古今好课求信息分享", "带学喜报+1+1…", "用心服务用心带学才是最优解", "古今好 …[截断,原长562]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:23）

员工评价确认了关键机制：**员工须运营自己的小红书账号做营销**。这解释了小红书的"好评"来源。现在补搜小红书负面关键词。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Key new finding: "北京古今好课教育怎么样啊" — appears in both 退费 and 怎么样 searches. Let me open that note — it might be a complaint/review.

Also note the 退费 search surfaces generic 退费攻略 content (some may be 退费中介 ads: "教育机构退费而已，你越淡定，反而退的越快", "2026年2月新规，机构退费不退也得退", "原来发疯能让教育机构退费" — these are 退费代理/维权引流 content, common noise).

Relevant notes to open:
1. "北京古今好课教育怎么样啊" ← most important
2. "不做大班课，我们公考带学都包含什么？" (self-promo)

Let me open "北京古今好课教育怎么样啊".

I need its URL. Let me redo the 怎么样 search and grab the href for that note.

Let me do a search and get hrefs mapping titles→hrefs.

Let me run.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长411]` → `=> { "notes": [ { "txt": "北京古今好课求信息分享", "h": "/search_result/6a4e44b8000000000f031f25?xsec_token=ABkNVTgbDWrftmYI1g1fcmOxMpB8Kbs0-RQi-EG0CF41g=&xsec_source=" }, { "txt": "带学喜报+1+1…", "h": "/search_result/6a585dd4000000001100575a?xsec_token=ABRlpdzh-mimOx5s2xv1xrSRw04-Tdm6_LXntyvRA6d_M=&xsec_source=" }, { "txt": "古今好课｜成 …[截断,原长1198]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Hmm — "北京古今好课教育怎么样啊" as a keyword didn't return a note with that exact title; the results are the same set. So "北京古今好课教育怎么样啊" was probably the search suggestion text, not a note (the earlier extraction picked up the "猜你想搜"/suggestion keyword as a link with /search_result/ href). Indeed the hrefs for suggestions are /search_result?keyword=... which includes "/search_result/"? No — "search_result?keyword" contains "search_result" but I filtered "/search_result/" with trailing slash. A suggestion link would be "/search_result?keyword=..." which does NOT contain "/search_result/". Hmm.

Wait — earlier in the "古今好课 怎么样" search, the first entry was "北京古今好课教育怎么样啊" and it appeared where suggestions normally appear (before other notes). It's likely the "猜你想搜" keyword chip rendered as a link to search_result?keyword=... Let me check: chips like "北京古今好课教育" appeared as `generic` not link. Hmm.

Actually in the very first 小红书 search snapshot, there was:
```
- generic: 大家都在搜
- generic: 北京古今好课教育
- generic: 古今好课考公
```
as generic, not links. So suggestions are generic.

But the extraction here found "北京古今好课求信息分享" first — a real note. So "北京古今好课教育怎么样啊" in the previous run must have been a note in the 退费/怎么样 search results. Since I filtered href includes "/search_result/" — a note card link is "/search_result/<id>?xsec_token=..." → contains "/search_result/". A keyword suggestion would be "/search_result?keyword=..." → does NOT contain "/search_result/" (it's "search_result?"). So "北京古今好课教育怎么样啊" was a real note!

But when I searched exactly that phrase, it didn't appear. Possibly the note is a video note (no title) that got its title from... hmm. Or the search for that exact keyword ranked differently and the note is beyond the extracted count (I sliced 20 but only got 8).

Let me instead search "北京古今好课教育怎么样啊" and take a broader extraction, or search the 退费 keyword again and capture hrefs to find that note.

Let me redo the "古今好课 怎么样" search and grab hrefs.

Let me run that.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长411]` → `=> { "count": 28, "notes": [ { "txt": "(无标题)", "h": "/search_result/695e2d8b000000001a033975?xsec_token=ABSegRhDpfMa7Louw5S3LtY7PqinfAk36SVH8l_P1ZKI4=&xsec_source=" }, { "txt": "(无标题)", "h": "/search_result/6a685423000000001d00ea7e?xsec_token=ABLHk8qdcOaipwyOCsVqo_ikY2ed7fuHiazaEarjXb2NA=&xsec_source=" }, { "txt": "(无标 …[截断,原长3124]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The 小红书 note set for this brand is stable — the same ~8-10 notes, dominated by the company's own accounts. No 避雷 negative notes about 古今好课 on 小红书.

Let me open a couple more to check if they're negative or positive:
- 695e2d8b000000001a033975 (哆啦宝) — unknown
- 6a685423000000001d00ea7e (快开学了 好慌) — unknown
- 6962285b000000002103f044 (小浮在备考（上岸版) — unknown
- 69cd45b2000000001a031233 (ing) — unknown
- 697042aa000000000b009986 (の) — unknown
- 6a4e3b8d000000000f02a488 (小红薯6836DF2B) — unknown
- 694a2968000000001e026a35 (猴头菇口服液) — 45 likes
- 685a635b000000001c037b9a (喜欢睡觉的懒羊羊) — 39
- 6948a3f5000000001e00aad3 (灰灰) — 25
- 6a9524800000000020036251 (momo) — 赞
- 6948... 

These are image/video notes with no title. They may be the real reviews. Let me open a few of the higher-engagement ones: 猴头菇口服液 (45), 喜欢睡觉的懒羊羊 (39), 灰灰 (25).

Actually, these unknown-title notes are probably not about 古今好课 at all — they likely matched because 小红书's search is fuzzy. Hmm, but they appear consistently in this brand search.

Let me open 2-3 of them to check. Let me open the 猴头菇口服液 one (45 likes) and 喜欢睡觉的懒羊羊 (39) and 灰灰 (25).

Hmm, context cost. Let me open them but only read the note body + comments, sliced.

Actually, a more efficient approach: open them in sequence and extract just the heading (title) and the first text block. Let me do 3 tabs in one cell, each reading the h1 + a bit.

Let me be careful: these notes might be irrelevant (fuzzy match). Let me check the top ones quickly.

Actually, let me reconsider: The search "北京古今好课教育怎么样啊 口碑" returned these as top results, meaning 小红书 ranks them for this query. The ones without titles are likely video notes where the "title" is in the image.

Let me open the 3 with notable engagement and read h1 + text.

Let me do it efficiently: for each, goto, then get the h1 text (getByRole('heading', level 1)) and the first few paragraphs.

Let me implement.

Actually — I worry about over-spending. Let me do 2: 猴头菇口服液(45) and 喜欢睡觉的懒羊羊(39), plus 灰灰(25).

Let me go.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长411]` → `=> { "猴头菇口服液": { "title": "", "body": "沪ICP备13030189号 | 营业执照 | 2026沪公网安备31010102002533号 | 增值电信业务经营许可证：沪B2-20150021 | 医疗器械网络交易服务第三方平台备案：(沪)网械平台备字[2019]第00006号 | 互联网药品信息服务资格证书：(沪)-经营性-2023-0144 | 违法不良信息举报电话：4006676810 | 上海市互联网举报中心 | 网上有害信息举报专区 | 自营经营者信息 | 网络文化经营许可证：沪网文[2021]1545-113号 | 个性化推荐算法 网信算备310101216601302230019号  …[截断,原长1341]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:24）

小红书该品牌下仅 ~10 条笔记，无避雷贴。抽查几条高互动笔记确认性质。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The direct /explore/ URLs redirected to the homepage (only footer content captured) — probably the xsec_token needs to be URL-encoded (the "=" at the end). Or the notes are gone.

Note: xsec_token contains "=" which in a URL query is fine but as a value "AB4A1oRTe57IXT02uUHENIJqsT3gn7otb2bp1l5qAETus=" — the trailing "=" should be encoded as %3D. In the earlier successful note open, the token was "ABkNVTgbDWrftmYI1g1fcmOxMpB8Kbs0-RQi-EG0CF41g=" and it worked... Hmm, that one also had trailing "=". And it worked. So encoding isn't the issue.

Maybe these notes are 视频 notes and the page didn't load in 2400ms, or the notes were deleted.

Rather than chase these, let me pivot: I have enough. These untitled notes are likely fuzzy matches unrelated to the brand (小红书 search often pads results).

Actually — let me reconsider. The key remaining question: are there genuine NEGATIVE user reviews on 小红书? Evidence so far: no 避雷 posts about 古今好课; the main note is a genuine question with mostly mild-positive/neutral comments and one "感觉好贵啊". Search for 退费 returns generic 退费攻略 content. So 小红书 shows: no organized negative wave, but also almost no independent reviews — content is dominated by the company's own employee-run accounts.

I think I have enough for a solid report. Let me do a couple more quick checks to round out:

1. 消费保: are there more complaints? Let me search 消费保 properly. Earlier the search box Enter didn't work. Let me try the 消费保 brand/company page or search via URL. Actually I could search Baidu for site:xfb365.com 古今好课.

2. 知乎: real Q&A (not the SEO article) — search 知乎 for 古今好课. The 知乎 search page requires login for full results but may show some.

3. Check the 微博 second post (普通家庭就别报这两家公考机构了) — likely same 引流 account. Skip.

Let me do:
- Baidu site search: "site:xfb365.com 古今好课" and "古今好课 消费保" to count complaints
- 知乎 search for 古今好课

Let me do these two in one cell.

Also worth checking: 小红书 是否有 "古今好课" 负面 via a different angle: search "古今好课 坑" / "古今好课 后悔". Let me include.

Let me run a combined cell.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长410]` → `=> { "site:xfb365.com 古今好课": [], "古今好课 消费保 投诉": [ "▶想在此推广您的产品吗?", "专业退款机构,维权追回,全额退费,免费咨询", "消费维权电话-点击进入", "培训服务与承诺不符要求退款-消费保 ", "消费保投诉帮助中心|投诉流程、常见问题与维权指引", "不用起诉!一个电话让教育机构主动给你退费", "河南好课教育信息咨询有限公司(公司) - 百度百科", "‎消费保-消费投诉与法律服务平台 App - App Store", "内蒙古自治区消费者协会", "📚教育机构退费攻略:消费保平台操作指南📲", "投诉好课在线怎么投诉" ], "古今好课 后悔 坑 不退": [ "上 …[截断,原长602]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The negative keyword searches return only generic 退费/维权 content and other companies (好课在线, 河南好课教育) — no specific 古今好课 negative articles. Confirms: no organized negative PR / no scandal content specifically about 古今好课. Note "好课课程坑了多少人" and "好课在线" refer to different companies (好课在线 = a different online education brand).

I now have a solid evidence base. Let me finish the todos and write the report.

Let me do one last quick check: the 职友集 page for salary/员工规模 (and to see if there's 员工评价 with negatives). And maybe check 消费保 more. Actually the 消费保 search on-site failed; and Baidu site: search returned nothing (Baidu doesn't index it well). I found 1 complaint via the specific Baidu result. It's possible there are more 消费保 complaints. Let me try the 消费保 search once more using a different approach — click the search icon instead of Enter, or navigate to the site's search URL.

Let me try 消费保's search results URL pattern. Hmm, guessing. Let me instead re-open the 消费保 page and look for a "投诉列表" or brand page. Actually, the complaint page showed brand "其它" with link /brands/0 — not helpful.

Alternative: 消费保 has a company search API. Let me just try filling the search box and clicking the magnifier icon (the empty generic after the textbox). Earlier the textbox had a sibling generic that might be the search button.

Hmm, but earlier the fill+Enter didn't navigate. Maybe the search needs the 搜索 icon click. Let me try: fill then look for button near it.

Let me do a quick attempt: snapshot the 消费保 header to find the search button.

Actually, given time/context, and that I already have 12315 (5 official complaints) + 消费保 (1 detailed) + 小红书 + B站 + 知乎 + 黑猫(0) + 工商 + BOSS直聘, I have a comprehensive picture. One more 消费保 attempt is worth it since complaint volume matters.

Let me try the 消费保 search via the magnifier icon. Let me snapshot just the header area first... or try clicking the image/generic right after the textbox.

Let me try: after fill, press the search icon. In the earlier snapshot:
```
- button "投诉": 投诉
- textbox "搜索相关内容"
- generic: 
```
The `generic:` after textbox is likely the search icon (magnifier img/generic). Let me find it — it might be a clickable div. Hmm, no role.

Let me instead try typing and pressing Enter again but wait longer, or check if a dropdown appeared with suggestions then press Enter again.

Alternatively, use the URL: 消费保 search results maybe at https://www.xfb365.com/search?keyword=古今好课 . One focused attempt is allowed. Let me try it.

Let me do that. If it fails, move to report.

Also let me quickly read 职友集 for salary info + 员工评价.

Let me do both in one cell.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(\n pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href\n);\nawait setupBrowserRuntime({ globals: glo …[截断,原长411]` → `=> { "xfbSearch": { "url": "https://www.xfb365.com/search?keyword=%E5%8F%A4%E4%BB%8A%E5%A5%BD%E8%AF%BE", "title": "消费保投诉-消费投诉与法律服务平台" }, "xfbText": "", "jobui": "\":\n - /url: https://www.jobui.com\n - text: 找客户\n- emphasis\n- text: 公司\n- emphasis: \"|\"\n- emphasis\n- textbox \"输入公司关键词\"\n- button \"Submit\"\n- generi …[截断,原长2968]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

职友集 data:
- 规模: 少于50人 (民营公司)
- 成立12年
- 行业: 教育/培训/院校
- 工资: 91.6%的岗位拿4.5-15K
- 招聘: 2026年较2025年增长200% (2025年3个 → 2026年9个)
- 学历: 本科83.3%; 经验1-3年 58.3%
- 地区: 郑州83.3%, 济南16.7% — 招聘岗位主要在郑州和济南! (interesting — Beijing registered, recruiting in 郑州/济南)
- 点评 "+200%" — there are 点评 (reviews)? The link "+200% 点评" is odd.

Note: 职友集 says 少于50人 while BOSS直聘 says 20-99人 (self-reported). 爱企查 social insurance: 3人.

消费保 search URL didn't work (generic page, no results text).

OK. I have a comprehensive picture. Let me also quickly verify the 好课带学(山东) subsidiary and note that the company recruits in 济南/郑州 — 济南 is where 山东子公司 is.

I think I have enough. Let me finalize todos and write the report.

Let me do one final check that could be valuable: 小红书 note "不做大班课，我们公考带学都包含什么？" — company marketing. And whether there are reviews from actual students. I have enough.

One more consideration: the user asked about "北京古今好客教育" — I should confirm the name mapping (好客 vs 好课). Baidu search for 好客 returned only 好课 results. Let me note that clearly. Also there's "北京好课优选科技有限公司" (different). And "河南好课教育信息咨询有限公司" (different). I should explicitly warn about name confusion.

Also I should note: the institution's official name 北京古今好课教育科技有限公司, brand "古今好课", subsidiary 好课带学(山东)信息科技发展有限公司, 曾用名 北京凯德新传国际文化传媒有限公司.

Let me write the report now. Let me mark todos complete.

Report structure:
1. 机构身份确认（名称纠偏）
2. 结论速览（口碑总体判断）
3. 证据分层：
   A. 官方投诉数据（12315 5条、黑猫0条、消费保1条）— 硬证据
   B. 社交平台真实用户声音（小红书、微博、B站、知乎）
   C. 广告/引流内容识别（重点：如何区分）
   D. 工商与雇员面（风险）
4. 关键风险点
5. 给用户的建议 / 待办（让用户可在登录态继续深挖）

Let me be careful about accuracy: 
- 12315: 5 条公示 (企业名称中含"古今好课"共5条), all 北京古今好课教育科技有限公司. 公示期限1年 so covers ~2025-2026.
- 黑猫: 0 条 (all variants)
- 消费保: 1 条 found (9580元, 2025-07-12报名, 投诉2025-12-27, 自动完结2026-02-10 因品牌方未回应). Note: 消费保 is a commercial platform; 1 complaint found via Baidu. I couldn't搜索全站, so may be more.

Let me be honest about limitations.

- 小红书: logged in as the user's account (note: I used the user's 小红书 login — that's their browser session; fine). Findings: ~10 notes; dominated by 公司自有账号 (古今好课带学萌萌, 古今好课教育带学); 1 genuine 求助帖 with 13 comments mostly mild positive/neutral; no 避雷 posts. Employee job description confirms employees run 小红书 accounts.
- 微博: "公考柿子学姐避坑攻略" 避雷帖不点名机构，是引流号 (收费咨询/查口碑)，不能作为对古今好课的负面证据 (它没提).
- B站: 3-4 条"机构测评"视频，全部是引流矩阵号 (关关上岸版/上岸咨询师小水/考公机构咨询站)，播放量48-154，0评论。
- 知乎: 1 篇软广 (海鸥公考测评, 49篇文章, "扣11领卡片"+问卷星), 0赞同。另有"50家公考机构靠谱吗"聚合文 — 我未展开，可后续看。
- 工商: 自身风险0, 参保3人, 小微, 注册资本100万, 16商标, 法人曾庆庚.
- 雇佣: BOSS直聘5条评价均HR岗, 桂先生明确说员工要运营自己小红书账号, 薪资6-10k, 20-99人(自报). 职友集: 少于50人, 招聘岗位83%在郑州.

Key risks to flag:
1. 合同/退费纠纷为主要投诉类型（12315: 合同格式条款加重责任、拒不履行合同约定；消费保: 服务与承诺不符、虚高单价扣费）→ 签约前务必看清退费条款
2. 机构对小额高频高价课程（9580元）的履约能力与售后：消费保投诉品牌方"未有效回复"→ 售后响应差
3. 师资承诺"体制内老师兼职"（消费保投诉称涉嫌违规）→ 若属实涉及违规
4. 规模小（社保3人）+ 大量招聘 + 郑州为主 → 销售/引流驱动模式，离职率高，服务交付依赖人
5. 网上好评来源可疑：公司自有员工运营小红书账号 → 小红书好评≠真实学员评价
6. 网络公开独立评价极少（"信息有点少"是连潜在学员都这么说的）→ 无正面口碑积累，也无大规模负面曝光

Also very important caveat: 12315公示只有1年期限且只公示办结的，实际投诉量>5。

Let me also mention: 投诉内容显示购买渠道为"小红书"、"电视电话购物及邮购"、"其他平台"→ 主要线上成交。

Let me write it. Use tables. Keep it organized and evidence-based with links.

Let me provide the source URLs:
- 消费保: https://www.xfb365.com/tousu/100223411
- 12315公示: https://tsgs.12315.cn/ (搜索"古今好课")
- 黑猫: https://tousu.sina.com.cn/index/search/?keywords=古今好课&t=1
- 小红书求助帖: https://www.xiaohongshu.com/explore/6a4e44b8000000000f031f25
- 知乎软广: https://zhuanlan.zhihu.com/p/1911808521881785146
- B站: BV1WZ5k6eEj7, BV18ebSz5EPY, BV1NxgAzbEGS
- 微博引流: https://weibo.com/5829052784/OFVWR8Pti
- 爱企查: https://aiqicha.baidu.com/company_detail_29020189269323
- BOSS直聘: https://www.zhipin.com/gongsi/review/40dff379b3f7072d03V_2t69E1A~.html
- 职友集: https://www.jobui.com/company/24742195/

Let me finalize todos then write.

I should also mention the name correction prominently since the user typed 好客.

Also note I should mention the 小红书 login: it turned out the user's browser was already logged in, so no interruption needed — good.

Let me write the final answer. Should be thorough but organized. This is a research report, data must be complete (per user preference: 数据必须完整展示).

Length: moderate-long is appropriate here given they asked for a thorough investigation. Let me use tables and clear sections.

Let me mark all todos completed first.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "确认机构身份与名称（好课≠好客）", "priority": "high", "status": "completed"}, {"content": "黑猫投诉：全名称变体均为0条", "priority": "high", "status": "completed"}, {"content": "12315公示：官方5条已办结投诉（合同/售后/质量）", "priority": "high", "status": "completed"}, {"content": "消费保：1条9580元投诉详情", "priority": "high", "status": "completed"}, {"content": "小红书：真实求助帖+评论（已登录读取）", "priority": "high", "s …[截断,原长412]` → `{"oldTodos":[{"content":"搜索引擎初筛：确认机构为线上公考培训机构“古今好课”","status":"completed","priority":"high"},{"content":"黑猫投诉：全名称变体均为 0 条","status":"completed","priority":"high"},{"content":"消费保：命中1条9580元投诉（机构未回应自动关闭）","status":"completed","priority":"high"},{"content":"小红书检索：读取真实求助帖+评论","status":"completed","priority":"high"},{"conte …[截断,原长1424]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Now write the report. Note: 小红书 was already logged in, so no login interruption needed. I should mention that.

Let me write a comprehensive report.

</details>

- 🔧 **mcp__node_repl__js** `{"source": "browser_turn_end"}` → ``

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:25）

调查完成。整个过程中**小红书已是登录态，无需你协助登录**，所以没有打扰你。

---

# 北京"古今好课"教育 口碑调查

## 〇、先纠一个名：不是"好客"，是"好课"

你给的是"古今好**客**教育"，实际机构全称是 **北京古今好课教育科技有限公司**（品牌"古今好课"）。百度按"好客"搜出来的结果全部指向"好课"，说明"好客"是记误。

> ⚠️ 同时注意重名干扰：**好课在线**、**湖南好课优选**、**河南好课教育**、**北京好课优选**、**库课网校** 都是**完全不同的公司**。网上大量"好课退款难"的帖子说的是"好课在线"，**不能算到古今好课头上**。反过来"古今"还是一家内衣品牌，也会污染搜索结果。

**工商侧信息**（爱企查/职友集）：

| 项目 | 内容 |
|---|---|
| 全称 | 北京古今好课教育科技有限公司 |
| 曾用名 | 北京凯德新传国际文化传媒有限公司（2014 年成立） |
| 法定代表人 | 曾庆庚；股东：古今 99%、曾庆庚 1% |
| 注册资本 | 100 万；**社保参保仅 3 人** |
| 规模 | 小微企业（BOSS 自称 20-99 人，职友集记"少于 50 人"） |
| 地址 | 北京市朝阳区汤立路 201 号院 3 号楼 17 层 2 单元 2002-2 |
| 业务定性 | **线上公考培训**（公务员/军队文职/事业单位），另做"带学"服务 |
| 子公司 | 好课带学（山东）信息科技发展有限公司（100%） |
| 风险 | 爱企查"自身风险 0、关联风险 0"，提示信息 13 条；未见行政处罚、经营异常、诉讼记录 |

---

## 一、客观结论

> **这不是骗局，但是一家"小作坊式的线上公考带学机构"：官方渠道有 5 条已办结投诉（以合同与退费类为主），售后响应差；网上几乎找不到独立真实好评，能看到的好评大多来自它自己员工运营的账号；没有任何官方处罚或大规模翻车。适合当"低价试错"，但 1 万元级别的课要特别当心合同与退费条款。**

---

## 二、硬证据：官方投诉记录（这是最有价值的部分）

### 1. 12315 全国消费投诉信息公示平台 —— 5 条已办结投诉 ✅ 官方

在 `tsgs.12315.cn` 用"古今好课"检索，**企业名称命中 5 条**（品牌命中 1 条），主体全部是"北京古今好课教育科技有限公司"：

| # | 投诉日期 | 购买渠道/类型 | 问题性质（官方分类） | 诉求 | 公示时间 |
|---|---|---|---|---|---|
| 1 | 2026-06-09 | 小红书网购"网上教育" | 售后服务 → 其他售后服务问题 | 退赔费用 | 2026-08-17 |
| 2 | 2026-07-01 | 其他平台网购"大学教育服务" | 质量 → 不具备应有使用性能而事先未说明 | 赔偿损失、退赔费用 | 2026-07-10 |
| 3 | 2025-12-31（2025-05-31 购买） | 现场购买"应试培训服务" | 合同 → **利用合同格式条款加重消费者责任** | 退赔费用 | 2026-03-12 |
| 4 | 2025-12-26 | 电视电话购物及邮购"应试培训服务" | 合同 → 其他合同问题 | 退赔费用 | 2026-03-05 |
| 5 | 2026-01-19（2025-09-24 购买） | 其他平台网购"其他技能培训服务" | 合同 → **经营者拒不履行合同约定** | 停止侵权、核定侵权责任、退赔费用 | 2026-01-27 |

**怎么读这 5 条：**
- 全部诉求都指向**退费**，性质集中在**合同纠纷**（格式条款加重责任、拒不履行约定）+ 售后服务 + 质量。
- 公示期限只有 1 年，且只公示**已办结**的投诉 → **实际投诉量必然高于 5 条**。
- 购买渠道是小红书 / 电视电话 / 其他平台 → **基本靠线上成交、电销/网销驱动**。

### 2. 黑猫投诉 —— 0 条 ⚠️ 需正确理解

`tousu.sina.com.cn` 分别检索"古今好课""古今好课教育""北京古今好课""好课带学""古今好课教育科技"，**全部为 0 条**。

> 这**不能**当作"清白证明"。该机构在黑猫**没有注册商家**（黑猫很多投诉需要品牌方入驻才能流转），且知名度极低，学员未必知道去黑猫投诉。这与 12315 有 5 条并不矛盾——**12315 才是权威口径**。

### 3. 消费保 —— 1 条，细节最完整 ✅ 信息量最大

`消费保` 投诉单 #100223411（2025-12-27，2026-02-10 已完结）：

- 学员 2025-07-12 报名**公务员培训课程，缴费 9580 元**。
- 指控要点：
  1. **核心服务缺失**——合同承诺的"全程每日规划与督促""每月备考指导两次""行测申论答疑""套卷精练计划"，自 2025 年 9 月下旬起基本未提供；
  2. **服务质量低劣**——"阶段性检测"题目重复、形式敷衍；申论批改不清晰、难查阅；督学内容笼统无个性化；
  3. **课程内容不符**——**未提供自有版权课程，仅转发市面流通的"网红老师"录播课链接**；
  4. **师资承诺不实**——宣传"体制内老师"兼职，"涉嫌违规"；
  5. **班级人数前后不一**——报名前说"不超过 20 人"，报名后说"一般 25 人"。
- 要求全额退款，**不接受机构提出的虚高单价扣费**（如按 200 元/篇申论批改扣）。
- **结局：因"未获得投诉品牌方的有效回复"，平台自动关闭该投诉** ← 售后不响应。
- 唯一评论（另一用户，7 个月前）："啊啊啊，可以和投诉人联系嘛，我在考虑这个机构，**看是小公司所以害怕**😱"

---

## 三、社交平台真实用户声音（重点：怎么分辨）

### 小红书（我用了你的登录态，已能看到全文与评论）

搜"古今好课 / 古今好课带学 / 古今好课 退费 / 怎么样"——**这个品牌在小红书总共只有约 10 条笔记**，而且**没有一条"避雷"贴**。

结果分布很说明问题：

| 笔记 | 发布者 | 性质 |
|---|---|---|
| 带学喜报+1+1…、用心服务用心带学才是最优解、如何挑选合适的机构～、带学对大家的帮助是实实在在的～ | **古今好课带学萌萌** | 🚩 机构自有账号（营销） |
| 古今好课｜成功学员的感谢、带学的备考指导日常、不做大班课，我们公考带学都包含什么？ | **古今好课教育带学** | 🚩 机构自有账号（营销） |
| **北京古今好课求信息分享** | 發啊發 | ✅ **真实求助帖** |

**那条真实求助帖值得细看**（07-08，4 赞 / 13 评论）：
- 正文："别人安利的机构…**但是古今好课的信息有点少了**，想问问有没有友友报过了解过的，怎么样啊 求求"
- 评论区（按原样）：
  - "我准备报了"（湖北，07-13，4 赞）
  - "我也"（四川，07-20）→ 下挂 3 条回复
  - "去年跟的还行"（山东，07-08）
  - "还行 排的你根本没空玩"（湖北，07-09）→ **暗示排课很满/强度大**
  - "我觉得挺不错的"（云南，07-09）
  - **"蹲蹲 报了吗 **感觉好贵啊**"（四川，08-27）**
  - "蹲蹲报了吗"（河南，08-04）
  - "我报的考研带学辅导"（山东，07-09）

> **评价：** 没有一条实锤差评，但**也没有一条来自高信任度的独立深度评价**。整体是"信息极少 + 轻量好评"，且好评无法排除是员工号。用一句评论里的话最准确——**"古今好课的信息有点少了"**。

### B 站 —— 只有引流矩阵号，无真实测评 🚩

搜"古今好课"命中的 3 条"机构测评"视频，**是同一个模板批量生产的引流号**：

| 视频 | UP 主 | 数据 |
|---|---|---|
| 古今好课，研学，国图，乐学，高途这些公考机构怎么选靠谱？ | **关关上岸版** | 152 播放 / **0 评论** |
| 带学机构哪家强？上岸时刻，古今好课，好课带学，必腾公考怎么选？ | **上岸咨询师小水** | 48 播放 / **0 评论** |
| 公考机构测评合集之必过，古今好课，慧恒教育，乐学公考哪家值得报？ | **考公机构咨询站** | 154 播放 / **0 评论** |

特征一模一样：2 分钟左右、标题塞满机构名、"哪家值得报"、近乎零播放零评论、UP 主号名带"上岸/咨询/测评"。**结论：B 站没有真实用户测评，只有获客软广。**

### 知乎 —— 软广，可直接判为广告 🚩

《公考机构真实反馈！线上公考机构古今好课到底怎么样？推荐还是避雷？线上公考机构哪家强？》(zhuanlan.zhihu.com/p/1911808521881785146)：

- 账号"**海鸥公考测评**"：**0 赞同、11 粉丝、49 篇文章**（同质批量发文）。
- 内容**全是正面/空话**（"虽未公开名师阵容，但教学聚焦实战"），**通篇无一条缺点**。
- 关键破绽：正文写"❌不足之处：**扣11并直接点击↓卡片零取**"——"扣 11"是骗评论互动的话术，后面挂的是 **wjx.cn 问卷星表单**（收集线索）。文内还自称"我是考公上岸喵上岸版"，与账号名"海鸥公考测评"对不上，属**复制粘贴模板**。
- **判定：付费 SEO 软文，不是口碑。**

### 微博 —— "避雷帖"其实是卖咨询的引流号 🚩

《被投诉最多的三家线上公考机构，避雷避雷避》(weibo.com/5829052784/OFVWR8Pti)：

- 账号"**公考柿子学姐避坑攻略**"（5.1 万粉 / 2750 条微博），**全文只说"某公考""避雷机构1️⃣2️⃣3️⃣"，一个机构名都没点**；
- 结尾话术："如果你害怕踩雷、被坑，**可以找我聊聊**"+"帮你避开公考报班 90% 以上的坑"+ 外链短网址。
- **判定：典型"制造焦虑→私聊转化"的引流号，对古今好课没有任何指名指控，不能当负面证据，也不该采信它的任何"榜单"。**

---

## 四、员工侧信息：重要的一条因果线索 🔍

BOSS 直聘该司"工作感受"（共 5 条，**全部是 HR/招聘岗**发的）：

- 人事经理、人事、人力招聘专员 3 条：正面套话（"踏实、温暖、有归属感""00 后团队、双休、下午茶、团建"）。
- **行政人力总监（9 个月）**这条最实，直接说明：
  > "入职有考情考务培训…**最后就要运营自己的小红书账号了**"
  > "达到标准的成熟员工一般都不加班，每个月都能拿到 6k-10k"
  > 面试"业务负责人来聊"

👉 **这解释了小红书上的"好评"从哪来：员工必须运营自己的小红书账号做营销。** 所以小红书里那些"带学喜报""成功学员的感谢""用心服务"，**是员工 KPI 产物，不是学员口碑**。

配合其他信号：职友集显示招聘岗位 **83.3% 在郑州、16.7% 在济南**（注册地却在北京）、2026 年招聘量同比 +200%、大量"人力/招聘专员"岗 → **销售/引流驱动、人员流动性大的典型结构**。

---

## 五、风险清单（按严重度排序）

| # | 风险 | 依据 |
|---|---|---|
| 1 | **退费/合同是主要雷区**：格式条款加重消费者责任、拒不履行合同约定 | 12315 第 3、5 条 |
| 2 | **合同承诺与实际服务不符**，且机构提出**虚高单价扣费**（200 元/篇申论批改） | 消费保 #100223411 |
| 3 | **售后不响应**：消费保投诉因"品牌方未有效回复"被迫自动关闭 | 消费保 #100223411 |
| 4 | **课程非自有版权**，疑似转卖"网红老师"录播链接 | 消费保 #100223411 |
| 5 | **宣传"体制内老师兼职"**，被指涉嫌违规（若属实是硬伤，但仅为单方面指控） | 消费保 #100223411 |
| 6 | **公司极小**：社保 3 人、注册资本 100 万，却卖 9580 元/单的课 → 履约与退款能力风险高 | 爱企查 |
| 7 | **网上好评不可信**：员工须运营小红书账号做营销，好评=自产 | BOSS 直聘员工自述 |
| 8 | 网上**独立评价几乎为零**，无正面口碑沉淀 | 小红书仅约 10 条笔记 |

**唯一"正面"的客观信号**：12315 有 5 条办结记录（说明投诉走了正规流程并被受理公示，不是跑路型机构）；爱企查无行政处罚、经营异常、诉讼记录；公司已存续 12 年。

---

## 六、给你的行动建议

1. **报名前必做**：要求先看**空白合同全文**，重点抠——① 退费条款与扣费单价；② 是否写死"每日督学/每月指导 2 次/答疑"等具体交付项与频次；③ 班级人数上限是否写进合同。
2. **付款**：**只走对公账户/官方平台**（该机构投诉里就有"电视电话购物及邮购"这类高风险渠道），拒绝对私转账，保留聊天记录与宣传截图（销售承诺不写进合同的，截图就是证据）。
3. **最低成本试错**：先报**最小额度**课程，验证交付质量后再考虑上万的套餐。评论区"感觉好贵啊"值得当真。
4. **要不要报**：这是一家**无黑料、但也无口碑**的小机构。如果你极需"有人盯着学"的外部约束，可以小额试；如果指望师资/教研（它有投诉直指无自有版权课），预期要放低。
5. **万一出问题**：直接上 **12315 平台（tsgs.12315.cn 查+投诉）** 走市场监管投诉，比黑猫有效（该机构在黑猫无商家、不响应消费保）。保留"小红书成交"的链路截图。

## 七、本次调查的局限（如实说明）

- **12315 公示期限仅 1 年、只公示已办结件**，所以 5 条是**下限**，不是总量。
- **消费保站内搜索未成功**（该站搜索接口没跳转），那 1 条是通过搜索引擎找到的，**可能还有更多**。
- 知乎那篇《50 家公考机构靠谱吗（含 100% 真实吐槽）》我打开了但未逐条读完，**如果里面有古今好课的条目可以再挖**。
- 小红书那几条无标题的视频笔记（如"猴头菇口服液"45 赞、"喜欢睡觉的懒羊羊"39 赞）直链已失效/跳首页，**没读到正文**，无法确认是否相关。
- "体制内老师兼职涉嫌违规"是**投诉人单方指控**，未经核实。

需要我继续的话，可以：① 逐条读完知乎那篇 50 家吐槽；② 换个方式再攻消费保站内搜索补全投诉量；③ 去抖音/贴吧/上岸论坛再扫一轮。要哪个我接着做。
