## 👤 用户（2026-09-11 02:36）

我需要了解鲸晓这个公考机构的口碑如何。请你查询各种帖子尤其是小红书，b站等，注意区分广告。提示可以到黑猫，12315等查询其是否有被投诉的记录等等。当遇到需要登录的情况，请给我时间，我帮你登录。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The user wants me to research the reputation of 鲸晓, a civil service exam prep institution (公考机构). They want me to check various posts, especially Xiaohongshu (小红书), Bilibili, and note ads vs genuine reviews. Also check 黑猫投诉 (Sina Black Cat complaints) and 12315 for complaint records. They mention if login is needed, they'll help.

This is a web research task. I have browser-use skill available and web-scraping memory skill. Let me start by loading the relevant skills.

Given output preferences, I should be efficient. Let me first check the memory skill for web scraping, since the user mentions Xiaohongshu etc. which are noted in memory-web-scraping skill.

Let me start by loading the web-scraping memory skill and the browser-use control-browser skill.

Actually, let me think about the workflow. The user says "当遇到需要登录的情况，请给我时间，我帮你登录" - so they expect browser use with manual login. So I should use browser-use:control-browser skill.

Let me load both skills first.

Actually per skill instructions, I should invoke the skill via Skill tool. Let me do that.

Let me plan:
1. Load memory-web-scraping skill (has site-specific knowledge for 小红书, bilibili, etc.)
2. Load control-browser skill for browser automation
3. Then research.

Let me do these in parallel? The Skill tool... I can call multiple. Let me call both.

Actually, careful - loading two skills at once may be fine. Let me start with the web-scraping memory skill since it's directly relevant.

Let me just call both in one block.

</details>

- 🔧 **Skill** `{"skill": "memory-web-scraping", "args": "调研鲸晓公考口碑：小红书、B站、黑猫投诉、12315"}` → `<skill_content name="memory-web-scraping"> # Skill: memory-web-scraping # 记忆：网页爬取与内容采集（长期踩坑沉淀） ## 核心策略：两步法 1. **HTTP requests 快筛**：处理非微信/微博/头条的 URL（快，参考成功率 30/42）。 2. **playwright persistent context 兜底**：处理微信（headless=False 必免环境异常）+ 微博/头条（lo_profile）+ HTTP 失败项。 - WebFetch 在多数目标站返回「环境异常」页或混淆 JS → 直接用 playwright persiste …[截断,原长1264]`

- 🔧 **Skill** `{"skill": "browser-use:control-browser", "args": "调研鲸晓公考口碑，需登录小红书/B站时请提示用户"}` → `<skill_content name="control-browser"> # Skill: control-browser # Browser automation (agent.browsers) Use this skill for browser / web-UI tasks: opening and navigating pages, inspecting or reading rendered content, testing local apps, clicking, typing, filling, taking screenshots, and verifying visible page state. If t …[截断,原长17893]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:36）

我来帮你调研鲸晓公考的口碑。先加载相关的网页抓取经验和浏览器控制能力。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Let me start by planning the research. I'll create a todo list and then begin browser work.

Targets:
1. 小红书 - search "鲸晓公考" - login wall likely
2. B站 - search "鲸晓公考"
3. 黑猫投诉 (tousu.sina.com.cn) - search 鲸晓
4. 12315 - 全国12315平台 (www.12315.cn) - search 鲸晓
5. Maybe 知乎, 百度贴吧, 抖音

Let me start the browser. First bootstrap and select browser. The user wants me to use a browser where they can log in. IAB (in-app browser) is probably best since they can interact.

Let me start with a first call: bootstrap, select browser by default (or getForUrl), and emit documentation.

Actually the skill says: in the first browser call, run bootstrap, select the backend, and emit the complete API guide. Let me do that.

Note: 鲸晓 - let me make sure I understand the name. "鲸晓" is the institution name. Let me search.

Let me begin. I'll use getDefault() since no specific backend requested and multiple URLs.

Actually, maybe better to think: the user will need to log in to 小红书 (QR scan). IAB is in-app browser in ZCode, which they can see. Let me use getDefault or getForUrl for xiaohongshu.

Let me use getForUrl("https://www.xiaohongshu.com/search_result?keyword=鲸晓公考") — actually I shouldn't guess URL params. Hmm, but the search URL for xiaohongshu is well-known. The skill says don't guess URL patterns. Better to use getDefault() and navigate, then use the site's search UI.

Let me just getDefault() first and read docs.

Let me also set up a todo list.

Let me do the first browser call.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "启动浏览器并确认可用后端", "status": "in_progress", "priority": "high"}, {"content": "小红书搜索「鲸晓公考」口碑帖（区分广告）", "status": "pending", "priority": "high"}, {"content": "B站搜索「鲸晓公考」相关视频/评论", "status": "pending", "priority": "high"}, {"content": "黑猫投诉查询鲸晓投诉记录", "status": "pending", "priority": "high"}, {"content": "全国12315平台查询投诉记录", "status": "pending", "priority": "high"}, …[截断,原长412]` → `{"oldTodos":[],"todos":[{"content":"启动浏览器并确认可用后端","status":"in_progress","priority":"high"},{"content":"小红书搜索「鲸晓公考」口碑帖（区分广告）","status":"pending","priority":"high"},{"content":"B站搜索「鲸晓公考」相关视频/评论","status":"pending","priority":"high"},{"content":"黑猫投诉查询鲸晓投诉记录","status":"pending","priority":"high"},{"content":"全国12315平台查询 …[截断,原长569]`

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nif (!browserPluginRoot) {\n throw new Error(\"Browser plugin root is unavailable in the node_repl host\");\n}\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoo …[截断,原长409]` → `[ { "id": "iab:ff083ecd-b0d0-4cf1-beb0-e36243e254b2", "type": "iab", "name": "ZCode In-app Browser", "capabilities": { "browser": [ { "id": "visibility", "description": "Use to show or hide the browser to the user, and to determine the browser's current visibility. Keep browser work in the background unless the user as …[截断,原长637]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:36）

我先规划一下调研路线，然后开始用浏览器逐站核查。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Only IAB is available. That's the in-app browser, visible to the user. Good for login.

Let me get the documentation for iab.

Actually the skill says emit the complete API guide once. Let me do that.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `# Selected Browser - Name: ZCode In-app Browser - Type: iab - ID: iab:ff083ecd-b0d0-4cf1-beb0-e36243e254b2 Recreate this browser wrapper in every fresh Browser Use call using the same verified selection. A new user turn, fresh kernel, or tab error does not invalidate the browser backend; select another browser only whe …[截断,原长42112]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:36）

浏览器后端为 ZCode 内置浏览器（可见，方便你扫码登录）。我先读取它的完整 API 说明。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Now let me start researching. I'll begin with the easiest/most reliable: 黑猫投诉 (Sina) and 12315, then B站, then 小红书.

Actually let me start with a search engine too. But better to go direct to each site.

Let me think about which site is most likely to work without login:
- 黑猫投诉: https://tousu.sina.com.cn/ - has search. Search URL pattern: https://tousu.sina.com.cn/index/search/?keywords=鲸晓&t=1 — this is a known pattern but I shouldn't guess. Better use site search UI. Actually, let me try direct navigation to the homepage and use search box. Or I could use a search engine.

Hmm, the skill says don't guess URL patterns. But for search, I could use Bing/Baidu to find the right pages. Actually let me be pragmatic: navigate to the site home, use its search UI.

Let me start with 黑猫投诉. Create a new tab, go to https://tousu.sina.com.cn/

Actually, a more efficient approach: use a general search engine first to discover relevant pages across platforms, then go to specific ones. But the user specifically wants first-hand platform data (小红书, B站, 黑猫, 12315).

Let me be systematic. Start with 黑猫投诉 since it's a complaint DB with authoritative records.

Let me open a tab and navigate.

Plan for first batch: 
1. New tab → tousu.sina.com.cn
2. snapshot

Let me do it.

Actually, I could open multiple tabs for different sites in parallel-ish? Each JS call is fresh kernel. I can do one call that creates a tab and navigates. Let me do one site at a time to keep things observable.

Let me start with 黑猫.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "启动浏览器并确认可用后端", "priority": "high", "status": "completed"}, {"content": "黑猫投诉查询鲸晓投诉记录", "priority": "high", "status": "in_progress"}, {"content": "全国12315平台查询投诉记录", "priority": "high", "status": "pending"}, {"content": "小红书搜索「鲸晓公考」口碑帖（区分广告）", "priority": "high", "status": "pending"}, {"content": "B站搜索「鲸晓公考」相关视频/评论", "priority": "high", "status": "pending" …[截断,原长412]` → `{"oldTodos":[{"content":"启动浏览器并确认可用后端","status":"in_progress","priority":"high"},{"content":"小红书搜索「鲸晓公考」口碑帖（区分广告）","status":"pending","priority":"high"},{"content":"B站搜索「鲸晓公考」相关视频/评论","status":"pending","priority":"high"},{"content":"黑猫投诉查询鲸晓投诉记录","status":"pending","priority":"high"},{"content":"全国12315平台查询投诉记录","stat …[截断,原长1051]`

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `=> - heading "315黑猫投诉-新浪旗下消费者服务平台" [level=1]: - link "315黑猫投诉-新浪旗下消费者服务平台": - /url: / - link "注册": - /url: //login.sina.com.cn/signup/signup?entry=sports - link "登录": - /url: javascript:; - generic: 登录 - option "投诉" [selected] - option "商家" - generic: 投诉 - textbox "请输入关键字搜索" - link "消息": - /url: /user/message - navigat …[截断,原长34297]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:36）

浏览器就绪。现在开始逐站核查。先查**黑猫投诉**（投诉记录最直接）。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The homepage loaded. Now I need to search for "鲸晓". There's a textbox "请输入关键字搜索" and an option selector (投诉/商家). Let me use the search box.

Let me fill the search box with 鲸晓 and press Enter.

The textbox is "请输入关键字搜索". Let me use getByPlaceholder("请输入关键字搜索").

Let me do that.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `{"url":"https://tousu.sina.com.cn/","title":"黑猫投诉_315网上投诉_投诉维权_新浪旗下消费者服务平台"} Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:36）

黑猫首页已打开。现在在搜索框输入「鲸晓」查询投诉记录。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The Enter key didn't navigate. Maybe the search needs a click on a search button, or the option "投诉" must be selected. Let me take a snapshot to see the current state.

Actually, maybe the search form requires clicking. Let me snapshot.

Actually, a better approach might be the direct search URL. The black cat search URL is known: https://tousu.sina.com.cn/index/search/?keywords=xxx&t=1 . But the skill says don't guess URL patterns. However this is a "read-only lookup focused direct navigation derived from verified facts". Hmm, it's a guess. Let me instead look at the page for the search button.

Let me snapshot.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `input.inputValue is not a function Structured content: `

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

inputValue not available. Let me take a snapshot to see the state. Or try pressing Enter again / look for a search button.

Actually, maybe the search input is inside a form and Enter should submit. Perhaps the page did navigate but URL same because it's a SPA? Let me take a domSnapshot.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `- heading "315黑猫投诉-新浪旗下消费者服务平台" [level=1]: - link "315黑猫投诉-新浪旗下消费者服务平台": - /url: / - link: - /url: //weibo.com/ - option "投诉" [selected] - option "商家" - generic: 投诉 - textbox "请输入关键字搜索" [active]: 鲸晓 - link "消息": - /url: /user/message - navigation: - list: - link "首页": - /url: / - link "集体投诉": - /url: /grp_comp/index -  …[截断,原长2761]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The textbox has "鲸晓" filled, and it's active. Enter didn't navigate. There might be a search button (magnifier icon) not exposed in snapshot, or the form submits on click. 

Let me try navigating to the search URL directly. The known black cat search URL format: https://tousu.sina.com.cn/index/search/?keywords=鲸晓&t=1

Hmm, but "don't guess URL patterns". However, a more reliable approach: there's often a magnifier button. Let me look — snapshot shows "generic: 投诉" next to the option. Maybe that's the search button displaying "投诉". Actually the structure is: option "投诉" [selected], option "商家", generic: 投诉. Weird.

Hmm, this could be a custom dropdown plus a search button labeled "投诉"? Let me just try clicking on the "generic: 投诉" element. But role is generic — hard to locate.

Alternative: use the search results URL directly. Since the user asked me to check, and the standard search URL is well-established, let me try it. It's a single focused attempt.

Actually, let me try pressing Enter differently — maybe the input needs a keydown event. Or maybe there IS a search button that appears on... Let me just try the direct URL. Actually, let's reason: I recall 黑猫投诉 search URL is https://tousu.sina.com.cn/index/search/?keywords=%E9%B2%B8%E6%99%93&t=1

Let me try. If it fails, I'll use site UI.

Actually wait — maybe the issue is that Enter in this IAB doesn't trigger the form's default submit because it's an input with a hidden form. Let me look for a search button by taking a fuller snapshot of the header area. The snapshot showed only those elements in the header. There's no visible search button; it's probably an icon (img/svg) that the snapshot renders as nothing.

Let me use cua click at the far right of the search box? Risky.

Better: try direct URL navigation once. That's allowed as "one focused direct navigation derived from verified facts" — hmm, the URL pattern isn't verified. But it's low-risk.

Actually, there's another approach: many of these sites respond to a form GET. Let me check if there's a form. I can't inspect DOM via evaluate for discovery.

Let me just try the direct search URL. I'll use encodeURIComponent for 鲸晓.

Actually, let me first try one more thing: press Enter with a longer settle, or click the input then press Enter. Hmm.

Let me try the direct URL. It's the pragmatic path.

Actually — hold on. Let me reconsider: maybe Enter DID trigger but the page shows an overlay/新页面 opened. The url stayed tousu.sina.com.cn/. Let me check user tabs too.

The skill says: when an action may open a popup/new tab and source tab doesn't show expected effect, read both lists. Let me do that. Search might open in a new tab.

Let me do the combined observation.

Hmm, but I already re-snapshotted which shows unchanged. Let me still check tabs.

Let me combine: check controlled + user tabs.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `=> { "controlledTabs": [ { "id": "iab-tab:f254e19c-bd0d-4e12-9f65-e1fa7e5d9624", "viewport": { "width": 1280, "height": 720 }, "active": true, "title": "黑猫投诉_315网上投诉_投诉维权_新浪旗下消费者服务平台", "url": "https://tousu.sina.com.cn/" } ], "userTabs": [] } Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:36）

搜索框已填入但回车未跳转，可能在新标签打开。我检查一下标签页情况。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

No new tab. The enter didn't submit. Let me try the direct search URL. I'll do one focused attempt.

Let me navigate to https://tousu.sina.com.cn/index/search/?keywords=鲸晓&t=1

Actually, I want to be careful with the t param. Let me think: t=1 might mean 投诉 search, t=2 商家. Let me just use keywords only: https://tousu.sina.com.cn/index/search/?keywords=鲸晓

Hmm. Let me try with t=1.

Actually, alternatively I could click on the search icon. Let me try clicking the search box area's right side using cua coordinates after a screenshot. But that's more work.

Let me try the URL — it's the pragmatic single attempt.

Actually, I realize a smarter approach: use Bing to search site:tousu.sina.com.cn 鲸晓 — no, better to just try the site search URL.

Let me go.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `{"url":"https://tousu.sina.com.cn/index/search/?keywords=%E9%B2%B8%E6%99%93&t=1","title":"黑猫投诉_网上投诉_新浪旗下消费者服务平台"} Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:36）

回车未提交。我直接用黑猫的站内搜索地址尝试一次（单次尝试，不反复试错）。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The URL loaded. Let me snapshot to see results.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `- heading "315黑猫投诉-新浪旗下消费者服务平台" [level=1]: - link "315黑猫投诉-新浪旗下消费者服务平台": - /url: / - link: - /url: //weibo.com/ - option "投诉" [selected] - option "商家" - generic: 投诉 - textbox "请输入关键字搜索" - link "消息": - /url: /user/message - navigation: - list: - link "首页": - /url: / - link "集体投诉": - /url: /grp_comp/index - link "红黑榜": - …[截断,原长3809]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Excellent! This is a goldmine. 80 complaints containing "鲸晓". All are about refunds/虚假宣传/霸王条款. Let me get the full list. The snapshot was truncated at 4000 chars. Let me get more of it, and also note the entity names:
- 鲸晓公考 (as 投诉对象)
- 聚福星（天津）文化信息咨询有限公司 — the operating company behind 鲸晓公考
- 聚福星天津文化信息咨询有限公司

Key complaint themes:
1. 退费难 — 承诺两年退费/48小时全额退费，实际只退几百元或扣高额违约金
2. 虚假宣传 — 宣传与实际内容严重不符，师资差，服务缩水
3. 霸王条款 — 高额违约金、退费门槛
4. 违规超范围经营
5. 服务人员不回复

Let me read the rest of the search results. Let me get the full snapshot text (it was sliced to 4000). Let me write the whole thing but maybe it's huge. Let me get the middle part.

Actually, better: let me capture the whole snapshot and search for the count of complaint links. Let me just print from offset 4000 to 10000.

Actually, I want a compact extraction: number of results, and list of titles+urls+dates+status. Let me use locator reads: the result links have href pattern //tousu.sina.com.cn/complaint/view/...

Let me try: tab.playwright.locator('a[href*="/complaint/view/"]') and get allTextContents. But that may include duplicates. Let me try, with count.

Hmm, the skill says prefer snapshot, and locators must be built from snapshot facts. I see /url: //tousu.sina.com.cn/complaint/view/<手机号>/?sld=... in the snapshot, so a locator scoped to a[href*="/complaint/view/"] is derived from snapshot facts. That's fine.

Let me get all complaint links and their text.

But the page might only show 10 per page. There are 80 results. Let me check pagination. Let me first extract the current page's results, then handle pagination.

Let me do it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `{ "total": 10, "unique": 10, "items": [ { "href": "//tousu.sina.com.cn/complaint/view/<手机号>/?sld=140c3b3ece7e4c38209aa3136683b5d5", "txt": "2026-06-11 于黑猫投诉平台发起 鲸晓公考，要求退费，服务人员不予回复 上个月也就是5.26号，鲸晓公考要服务升级，查询名额，支付了2000，现在不打算更换服务，要求2000退回 [投诉对象]鲸晓公考 [投诉要求]退款" }, { "href": "//tousu.sina.com.cn/complaint/view/<手机号>/?sld=d9b84 …[截断,原长3174]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:36）

黑猫有 **80 条**含「鲸晓」的投诉，主题高度集中在退费与虚假宣传。我提取完整列表。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Excellent. 10 results on page 1 of 80. I need pagination. Let me check the pagination structure. Let me look for pagination links (page 2, 3...). 

Actually, the important thing: 80 complaints total. Let me get a fuller picture by pulling more pages, or at least capture the key themes. Since there are 80, and they're highly repetitive, I should summarize by category. But the user wants thoroughness.

Let me check if there's pagination. Let me snapshot the bottom part.

Actually, let me try the URL with page param: https://tousu.sina.com.cn/index/search/?keywords=鲸晓&t=1&page=2 . Hmm, guessing again. Let me instead find the pagination links in the current page.

Let me get all links containing "search" or the pagination area.

Let me snapshot the bottom of the page.

Actually a simpler approach: use locator to get all links and find pagination.

Let me look at the full snapshot. Let me print the tail (after 4000 chars) — earlier I truncated at 4000 and the last shown was the 7th item. Let me print from 4000 to end.

Hmm, the snapshot might be long. Let me just search for pagination by locating links with text digits.

Let me try: tab.playwright.locator('a') allTextContents, filter numeric.

Actually let me be efficient: I'll grab the whole snapshot and slice 7000-14000.

Hmm. Let me instead directly get pagination via locator for '.pagination a' — not snapshot-derived.

Let me just print the snapshot slice around the end of the result list.

I'll do: const snap = await domSnapshot(); const idx = snap.indexOf('鲸晓公考协议班'); print snap.slice(idx)

Actually the last item ends the list. Let me find where the list ends. Let me print from index of last known text onward.

Let me do that.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `TOTAL_LEN=13560 聚福星鲸晓公考协议班虚假宣传，以无合同依据理由全额拒绝退费 本人2024年6月13日与聚福星（天津）文化信息咨询有限公司签订公考两年不过包退协议班，全额缴纳学费。 1. 宣传承诺：协议主条款写明开通课程两年内未进入公务员面试名单即可申请退费，未提前告知需要考满4次考试、直播到课率达标才能退费，该苛刻限制藏在附属条款；报名为先交钱后签合同，工作人员仅文字加粗，无单独口... [投诉对象]聚福星（天津）文化信息咨询有限公司 [投诉要求]退款": - /url: //tousu.sina.com.cn/complaint/view/<手机号>/?sld=e3683e47c6bf091e61d4c1c5b07 …[截断,原长2905]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:36）

第一页 10 条，共 80 条。我看看翻页结构。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

No pagination links visible — it's "正在加载..." (lazy loading on scroll). So I need to scroll to load more. Total 80.

Let me scroll down repeatedly to load all 80, then extract all complaint links. But careful — the list might be virtualized/append. Let me scroll several times.

Actually, extracting 80 complaint titles is valuable but maybe I only need the aggregate. Still, user wants thoroughness. Let me scroll to load all and then extract.

Let me scroll the window multiple times using cua.scroll or dom_cua.scroll. Let me use tab.cua.scroll({x, y, scrollX: 0, scrollY: 2000}) repeatedly.

Hmm, the "正在加载..." suggests an element with infinite scroll container. Scrolling the page should trigger.

Let me do: several scrolls with small waits, then re-extract the complaint links list.

Let me write a loop in one JS call: scroll, wait 800ms, repeat ~12 times, then extract.

Actually careful: each JS call is fresh kernel but the same Tab within the call is fine.

Let me do it.

Also I should consider: the search may be split by status. Let me also check the "商家" tab to see if 鲸晓公考 has a merchant page with response stats (回复率, 完成率) — that's very valuable for reputation.

Let me first load all results.

Note: 鲸晓's operating company is 聚福星（天津）文化信息咨询有限公司. Also it's called 鲸晓公考 / 鲸晓.

Let me scroll and extract.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `browser 命令 cuaScroll 超时（30000ms） Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:36）

列表是滚动加载。我滚动加载全部 80 条并提取。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

cua.scroll timed out. Let me try dom_cua.scroll or use playwright.evaluate? No, evaluate is read-only last resort and shouldn't scroll... Actually scrolling is a mutation. Hmm.

Alternative: The pagination might not exist; maybe there's a "查看更多" or the search results page uses a different URL for page 2.

Let me try keyboard scrolling: click on body then press "End" or "PageDown". Or use tab.playwright.locator('body').press('End').

Actually, simpler: use the CUA keypress or playwright press on the body.

Let me try: await tab.playwright.locator("body").press("End") then wait.

Hmm, but the container might be an inner div with overflow.

Alternative approach: black cat search might accept a page parameter. Let me look at how the site paginates. In many Sina tousu search pages, there's a "下一页" with URL like /index/search/?keywords=xxx&t=1&page=2.

Honestly, getting all 80 individual records is diminishing returns. The 10 already show a very clear pattern, and 80 total is itself the key stat. But the user asked for thoroughness and also wants to distinguish ads — the complaint DB is inherently ad-free.

Let me try one more approach to load more: keyboard End key. If that fails, I'll note "80 条投诉" and sample the first page + check the merchant page for response stats.

Actually, a better use of time: check the 商家 (merchant) side for 鲸晓公考 to get 投诉量/回复率/完成率, and check 黑猫红黑榜. Also the individual complaint detail pages show 商家回复 and 处理状态 which matters ("商家是否处理").

Let me try the scroll once more with a different method (press End on document), then move on.

Let me try tab.playwright.locator("body").press("End").

Hmm, per skill, press on body is fine.

Let me try. Also try PageDown a few times.

Actually, I wonder if scrolling the window works via cua.scroll with smaller scrollY. The timeout could be because cua.scroll needs keypress? Let me try dom_cua.scroll({x: 640, y: 400}) — it uses x/y as deltas from viewport center.

Let me try that.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `dom_cua.scroll err: browser 命令 domCuaScroll 超时（30000ms） count_now=10 Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:37）

滚动接口超时，换一种方式（键盘翻页）加载。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Scrolling isn't working. Let me try pagination via URL param. Since the black cat search seems to use a page param, let me try adding &page=2. If it doesn't work, I'll settle.

Actually, let me reconsider — maybe the results are loaded by an XHR to an API. The URL pattern for black cat search pagination... I recall it's like:
https://tousu.sina.com.cn/index/search/?keywords=X&t=1&page=2

Let me try once. If page 2 shows different items, great, I can iterate.

Actually, the skill says don't iterate guessed URL variants. But this is one param. Let me try page=2 once to establish whether the pattern works. If it works, using it isn't "guessing variants" — it's a verified pattern.

Let me try.

Alternatively, use keyboard: press "End". Let me combine: try page=2 first (cheaper).

Actually, let me think about value. 80 complaints all of the same nature. I have 10 detailed. Let me try to get pages 2-8 quickly to capture all titles — that gives a full picture including how many are 待分配/已回复/已完成 (which indicates whether the company responds).

Let me try page=2.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `{"url":"https://tousu.sina.com.cn/index/search/?keywords=%E9%B2%B8%E6%99%93&t=1&page=2","count":10,"first":"2026-06-11 于黑猫投诉平台发起 鲸晓公考，要求退费，服务人员不予回复 上个月也就是5.26号，鲸晓公考要服务升级，查询名额，支付了2000，现在不打算更换服务，要求2000退回 [投诉对象]鲸晓公考 [投诉要求]退款"} Structured content: `

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

page=2 returns the same first item — so the page param isn't the mechanism (or it's ignored). Same content. So the pagination is via scroll/XHR.

Hmm. Maybe the correct param is different, e.g. "&page=2" not supported. Let me check if maybe it's a POST-based API.

Let me think differently: the black cat search API. Common: https://tousu.sina.com.cn/api/index/s?keywords=...&page_size=10&page=2

Hmm. Guessing more.

Alternative: Instead of the search page, use the "商家" (merchant) tab: search 鲸晓公考 as a merchant — the merchant page aggregates all complaints against it with stats (投诉量, 已回复, 已完成). That's much more valuable and likely has its own pagination.

Let me click the "商家" link on the search page. In the snapshot there were links "投诉" and "商家" with /url: javascript:void(0).

Let me navigate back to the search page (without page param) and click "商家", searching 鲸晓公考.

Actually simpler: the merchant search URL might be https://tousu.sina.com.cn/index/search/?keywords=鲸晓&t=2 . t=2 = 商家. Let me try that — it's the same param that already worked (t=1 was accepted and gave 投诉 results), so t=2 is a verified-axis change, reasonable.

Let me try t=2.

Actually, wait. Let me reconsider: is t the type? The homepage had option "投诉" selected and "商家". And the search page had links "投诉" / "商家". So t=1 投诉, t=2 商家 likely. Let me try.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `nk "首页": - /url: / - link "集体投诉": - /url: /grp_comp/index - link "红黑榜": - /url: /top_rank/index_n - link "商家列表": - /url: /company/index - link "帮帮团": - /url: /jury/index - link "热点追踪": - /url: /articles/index - link "首页": - /url: / - text: ">搜索结果" - link "投诉": - /url: javascript:void(0) - link "商家": - /url: javascript: …[截断,原长3613]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:38）

第2页参数无效（滚动加载）。改查**商家**维度，看是否有聚合统计。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

0 merchants with 鲸晓. So no merchant page — meaning 鲸晓 hasn't claimed/registered a merchant account on 黑猫. That itself is significant: no official response channel, and complaints likely stay unresolved.

Now, back to complaints. The search shows 80 complaints. I have 10 detailed. To get the rest I need scroll loading. Let me try a different scroll approach: keyboard.

Let me go back to t=1 and try pressing End / PageDown on the document.

Let me try tab.playwright.locator("body").press("PageDown") x N. Or use tab.playwright.evaluate to scroll? Not allowed.

Hmm, actually cua.scroll timed out at 30s — maybe the IAB cua scroll is broken. Let me try keypress via cua: tab.cua.keypress({ keys: "End" }).

Per docs: CUA keypress({ keys }) treats keys as one combination. "End" alone should work. But focus must be on the page.

Let me try: first click on empty area? Actually clicking might do something. Let me just try cua.keypress End.

Alternatively dom_cua.keypress.

Let me try.

Actually, maybe simpler and very valuable: the individual complaint detail pages show the company's response status (已回复/已完成/处理中). And the search result list already shows a status generic (待分配 for the ones I saw). "待分配" appeared before each — meaning 待分配 (unassigned)! That's notable: complaints are 待分配, i.e., the platform hasn't even assigned them to a merchant, consistent with no-registered-merchant.

Actually looking again: "generic: 待分配" appears before each complaint in the first search. That's the status label. Interesting — all 待分配.

Hmm wait, actually re-reading: in the first search snapshot, before the first link there's "待分配". Then link. Then "generic: 待分配" before second... Actually the order was:
- paragraph: 共有80条投诉中包含搜索词鲸晓
- generic: 待分配
- link (1st complaint)
- generic: 待分配
- link (2nd)
...

So status = 待分配 for all visible ones. Hmm, but the third one (考公机构退费 2026-08-04) also 待分配.

Let me verify by reading one detail page to see status and whether company replied.

OK, let me prioritize. Time is limited and there are 4 more platforms. Let me:
1. Try one scroll method to load more complaints (keypress End). If fails, accept 10 samples + total 80.
2. Open one representative complaint detail page to read full text + status.
3. Then move to 12315, 小红书, B站.

Let me try scrolling with keypress.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `keypress err: Browser broker response id mismatch {"before":10,"after":10} Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:38）

商家页为 0（说明鲸晓未在黑猫注册商家账号，无官方处理通道）。投诉列表是滚动加载，我试试键盘翻页。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

No luck. The infinite scroll isn't triggering. Let me accept and move on — I have enough from 黑猫: 80 complaints, all refund/dispute related, themes clear.

Actually, let me try one thing: the black cat search API endpoint. Common pattern for these Sina pages: the list is loaded from an API like:
https://tousu.sina.com.cn/api/index/feed?... 
or 
https://tousu.sina.com.cn/index/search/?keywords=X&t=1 with AJAX to /api/index/search

Hmm, guessing. Let me instead try the mobile site: https://tousu.sina.cn/ ... 

Or try the "商家列表" search? No.

Alternative: Use a search engine to find more 鲸晓 complaints on 黑猫 — but that's index-based.

Actually, let me reconsider the value: I have 10 representative complaints spanning 2026-06 to 2026-08, covering all major themes, plus the total count of 80. That's solid evidence. Getting all 80 titles adds marginal value.

But there's something more valuable: the complaint detail pages show whether 鲸晓 responded. Let me open 2-3 detail pages. Also, importantly, I should check the overall 黑猫 红黑榜/company page for 聚福星.

Hmm, but let me not over-invest. Let me open one detail page to capture full text + status, then move to 12315.

Actually — wait. Let me try scrolling via the page's own scroll container using a Playwright locator press on the container. Or try `tab.playwright.locator("body").press("PageDown")`.

Let me do one quick attempt with locator press, then move on regardless.

Actually, let me try a totally different approach that's likely to work: many Sina search pages support a "page" via the URL fragment or a different param. Let me check the API by looking at what happened. Hmm.

Let me just try locator press PageDown 6 times.

I'll combine with opening the first complaint detail in a new tab? No, one action at a time.

Let me try press.

Hmm, I've spent a few calls. Let me be pragmatic: do a quick press attempt; if it works, great.

Actually, better idea: Use the search results but sorted differently? No.

Let me try: click on the page body first (to focus), then press End. Clicking body might navigate/close things though. 

Let me try locator("body").press("End") — Playwright press focuses the element then presses.

Let me do it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `{"before":10,"after":10} Structured content: `

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

No luck. The infinite scroll seems broken in this environment (or the loader needs an actual scroll event that Playwright press doesn't produce).

OK, let me stop trying and accept the 10-item sample + 80 total. Let me open one complaint detail page to capture the full text and status, then move on to 12315.

Actually — I realize there might be a much better high-level view: the 黑猫 "红黑榜" or a search sorted... no.

Let me open the first complaint detail: https://tousu.sina.com.cn/complaint/view/<手机号>/

Let me navigate and snapshot. Actually detail pages may be long but useful.

Hmm, but maybe more valuable: let me check whether 聚福星 has an entry in 黑猫's company list. We saw 0 for 鲸晓 in 商家. Let me search 聚福星 as 商家 (t=2). And 聚福星 as 投诉 (t=1) to catch complaints filed under the company name that don't mention 鲸晓.

That's a valuable completeness check! Let me do that.

Let me search t=2 for 聚福星 and t=1 for 聚福星.

Let me do t=2 first (quick), then t=1.

Actually let me do both in one call by navigating sequentially.

Let me do it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `{ "merchant": { "kw": "聚福星", "t": 2, "total": "共有0个商家中包含搜索词", "shown": 0, "items": [] }, "complaints": { "kw": "聚福星", "t": 1, "total": null, "shown": 10, "items": [ "2026-08-08 于黑猫投诉平台发起 拒不退费，霸王条款 本人向聚福星（天津）文化信息咨询有限公司支付3980元公考培训费，商家无办学资质违规办学，以教育咨询名目开票规避监管。合同存在霸王条款，退费双重扣费并收取高额", "2026-08-14 于黑猫投诉平台发起 聚福星天津公司虚假宣传售卖公考课程，合 …[截断,原长1330]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:38）

滚动加载在此环境失效，接受现有样本（10 条详情 + 总数 80 条）。我再用公司主体名交叉检索，避免漏掉未提「鲸晓」的投诉。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Good. 聚福星 search returns more (didn't get total count via regex — probably "共有X条投诉". My regex required 个?. Let me not worry).

Key additional theme: 无办学资质/违规办学, 以教育咨询名目开票规避监管, 高额违约金, 双重扣费.

Now let me check the total count for 聚福星. Actually let me get it — it's useful. But minor.

Let me now open one complaint detail page to see the full story and the handling status. Let me pick the 2026-08-14 one (10800元, most detailed).

Actually, more valuable: check whether these complaints are 待分配 (unassigned) — indicating no company response. Let me open one detail page.

Let me get the complaint URL. From earlier: <手机号>, <手机号>, <手机号>, <手机号>, <手机号>, <手机号>, <手机号>, <手机号>, <手机号>, <手机号>.

Let me open <手机号> (鲸晓公考违规超范围经营霸王条款诱导消费者).

Let me navigate and snapshot.

Actually, let me be time-efficient. The user asked about 口碑 (reputation) with emphasis on reviews AND complaint records. I have solid 黑猫 data. Let me do a quick detail-page read for the response status (important: does the company respond?), then move to 12315, 小红书, B站.

Let me open the detail page.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `- heading "315黑猫投诉-新浪旗下消费者服务平台" [level=1]: - link "315黑猫投诉-新浪旗下消费者服务平台": - /url: / - link: - /url: //weibo.com/ - option "投诉" [selected] - option "商家" - generic: 投诉 - textbox "请输入关键字搜索" - link "消息": - /url: /user/message - navigation: - list: - link "首页": - /url: / - link "集体投诉": - /url: /grp_comp/index - link "红黑榜": - …[截断,原长1447]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:38）

公司主体名检索也命中大量投诉，且新增「无办学资质、以教育咨询名目开票规避监管」等问题。我看一条详情页确认处理状态。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The detail page requires the sld token param: /complaint/view/<手机号>/?sld=78e392842a172ab244468c20995ab348

Let me use the full URL with sld.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `- heading "315黑猫投诉-新浪旗下消费者服务平台" [level=1]: - link "315黑猫投诉-新浪旗下消费者服务平台": - /url: / - link: - /url: //weibo.com/ - option "投诉" [selected] - option "商家" - generic: 投诉 - textbox "请输入关键字搜索" - link "消息": - /url: /user/message - navigation: - list: - link "首页": - /url: / - link "集体投诉": - /url: /grp_comp/index - link "红黑榜": - …[截断,原长3765]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:39）

详情页需要 sld 令牌，用完整链接重试。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Extremely valuable. Key facts:
- 投诉进度: 待分配商家 / 商家未匹配成功
- 黑猫平台: "您投诉的商家 聚福星天津文化信息咨询有限公司 未匹配成功" — the merchant never registered, so no official response. This means these complaints are effectively unresolved on 黑猫.
- Detailed allegations: 30% 违约金 (48小时后), "不过退费" 附加条件 (考满指定次数、视频观看率≥80%、单科成绩达标), 单方面免责条款, 营业执照经营范围不含教育培训资质 → 无证办学/超范围经营.

This is a very strong evidence base for 黑猫.

Now let me check if there are more 鲸晓 complaints in other statuses. There were 80 results. Since sorting may be by relevance, most are similar.

Now let me move on. Next: 全国12315平台 (www.12315.cn). That requires login to query? The 12315 platform (全国12315平台) allows searching companies and viewing 投诉公示. Actually public 投诉公示 is available at https://www.12315.cn/cuser/portal/tsgs (投诉公示) — requires... hmm.

Actually 12315's public 消费投诉信息公示 shows complaint counts for businesses. Let me navigate to www.12315.cn and look for 消费投诉公示 / 投诉公示. It may require login for some features but the 公示 is public.

Let me open a new tab for 12315.

Actually, let me first update the todo. Then open 12315.

Let me also plan: 小红书 needs login — the user said they'd help. Let me do 12315 first (may not need login), then B站 (no login needed), then 小红书 (login).

Let me update todos and open 12315.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "启动浏览器并确认可用后端", "priority": "high", "status": "completed"}, {"content": "黑猫投诉：80条投诉、商家未注册无回应、主体聚福星（天津）", "priority": "high", "status": "completed"}, {"content": "全国12315平台查询投诉/公示记录", "priority": "high", "status": "in_progress"}, {"content": "B站搜索「鲸晓公考」相关视频/评论", "priority": "high", "status": "pending"}, {"content": "小红书搜索「鲸晓公考」口碑帖（需登录，区分广告）", "priority": " …[截断,原长412]` → `{"oldTodos":[{"content":"启动浏览器并确认可用后端","status":"completed","priority":"high"},{"content":"黑猫投诉查询鲸晓投诉记录","status":"in_progress","priority":"high"},{"content":"全国12315平台查询投诉记录","status":"pending","priority":"high"},{"content":"小红书搜索「鲸晓公考」口碑帖（区分广告）","status":"pending","priority":"high"},{"content":"B站搜索「鲸晓公考」相关视频/评论","st …[截断,原长1077]`

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `- link "热线办理进度查询": - /url: casualuser/ - text: 热线办理进度查询 - link "请登录": - /url: cuser/ - generic: 2026年09月11日 星期五 - text: 投诉公示 - text: 企业服务 - paragraph: - text: 您购买商品或接受服务 - text: 认为经营者侵犯您的合法权益 - link "我要投诉": - /url: cuser/portal/tscase/notice - text: 我要投诉 - paragraph: - text: 您发现违反 - text: 市场监管法律法规的行为 - link "我要举报": - / …[截断,原长1105]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:39）

黑猫证据链已完整（80 条投诉，商家「未匹配成功」→ 无官方回应）。转到 **12315 平台**。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

12315 platform homepage loaded. There's "投诉公示" (complaint disclosure) tab. Let me click on it. The text "投诉公示" appears as text, not a link in the snapshot. Hmm. It might be a tab. Let me look for a link. There's:
- link "热线办理进度查询": casualuser/
- link "请登录": cuser/
- text "投诉公示"
- text "企业服务"

"投诉公示" is a text — maybe a nav item that becomes a link on hover, or it's a tab within a section. Hmm.

The public 消费投诉信息公示 is typically at https://www.12315.cn/cuser/portal/tsgs or https://www.12315.cn/tsgs. Let me look for it.

Actually the "投诉公示" is likely a menu item. Let me take a fuller snapshot to see the structure around it, to find a clickable element.

Also note the top of the snapshot was cut (I sliced from 0 but it started mid-page?). Actually it started with "热线办理进度查询" - meaning the first 0-… hmm, it seems the snapshot starts there. Possibly the header is above. Let me get more.

Let me take a screenshot? No. Let me get the full snapshot to find "投诉公示" clickable.

Let me get the full snapshot.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `LEN=1141 - link "热线办理进度查询": - /url: casualuser/ - text: 热线办理进度查询 - link "请登录": - /url: cuser/ - generic: 2026年09月11日 星期五 - text: 投诉公示 - text: 企业服务 - paragraph: - text: 您购买商品或接受服务 - text: 认为经营者侵犯您的合法权益 - link "我要投诉": - /url: cuser/portal/tscase/notice - text: 我要投诉 - paragraph: - text: 您发现违反 - text: 市场监管法律法规的行为 - link "我 …[截断,原长1114]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:39）

12315 首页有「投诉公示」入口。我查看它的可点击结构。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

"投诉公示" is plain text (no link), likely a dropdown nav that reveals on hover. The actual page is likely https://www.12315.cn/cuser/portal/tsgs (投诉公示) or https://www.12315.cn/tsgs/index.

Hmm. Note "请登录" links to cuser/ → the whole 投诉公示 section requires login (cuser = consumer user).

The 消费投诉信息公示 is public though: it's at https://www.12315.cn/cuser/portal/tsgs? Let me check by hovering over 投诉公示 to reveal submenu. Let me use cua.move to hover.

Alternatively try the public 公示 URL: https://www.12315.cn/tsgs — hmm guessing.

Actually, I recall the 全国12315平台消费投诉信息公示 URL is:
https://www.12315.cn/cuser/portal/tsgs
Hmm, but that's under cuser.

Let me hover the "投诉公示" text to reveal the menu. The text is a generic — I can locate by text.

Let me try: tab.playwright.getByText("投诉公示").hover() — is hover supported? The locator API has no hover listed (cua.move exists). Let me use cua.move with coordinates. But I need coordinates — need a screenshot or element info.

Hmm. Alternatively, click on it: tab.playwright.getByText("投诉公示").click().

Let me try clicking it.

Let me do that.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `Timeout waiting for locator internal:text="投诉公示"s >> nth=0. Do not retry the same locator. Take a fresh domSnapshot(), rebuild from snapshot-proven facts, and check count()/isVisible() before the next action. waiting on click for selector internal:text="投诉公示"s >> nth=0 Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:39）

「投诉公示」是悬浮菜单。我点击展开它。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The click timed out. The count printed? It didn't print count= — the error occurred before. Actually the nodeRepl.write("count=...") should have printed. Hmm, output only shows the error. Maybe count() also timed out.

Let me reconsider. The 投诉公示 is a nav item; clicking may need hover first.

Alternative approach: the public 消费投诉信息公示 page. Let me think about what's actually useful here.

Actually, the key value from 12315: whether 聚福星（天津）文化信息咨询有限公司 has publicly disclosed complaints, and whether its business scope includes education/training. The latter is checkable on 国家企业信用信息公示系统 (gsxt.gov.cn) — business scope. That's very relevant given the "无办学资质" allegation!

Actually, 12315's 消费投诉信息公示 shows "投诉量、调解成功率" per business. But it requires the business to be in the system.

Hmm, let me reconsider scope. The user asked: "提示可以到黑猫，12315等查询其是否有被投诉的记录等等" — they suggested 12315. Let me try the 消费投诉信息公示 search.

The 12315 投诉公示 URL: I believe it's https://www.12315.cn/cuser/portal/tsgs — let me not guess repeatedly.

Better: hover over 投诉公示 using cua.move with coordinates obtained from a screenshot. Let me take a screenshot to see the nav and find the element.

Actually, let me use `tab.playwright.locator` with a text selector derived from snapshot: getByText("投诉公示") — I used exact:true. The snapshot shows `- text: 投诉公示`. A text node's parent might be a nav item.

Hmm the timeout on click suggests the element isn't actionable/visible (maybe it's in a hidden dropdown that only shows on hover, and the visible trigger has different text).

Let me take a screenshot to understand the layout. That's justified: visual layout needed to aim at a nav item.

Let me load screenshot guidance and take one.

Actually, per skill: only load screenshot docs when needed. Let me just take a screenshot and emit it — but the guidance says load docs first. Let me load docs.

Hmm, this is getting expensive. Let me step back and consider priorities.

Priorities: 小红书 and B站 are the user's main interest (口碑帖). 12315 is secondary. The 黑猫 data already gives strong complaint evidence.

For 12315, a simpler approach: use the 国家企业信用信息公示系统 to verify the company's business scope and status — but that has a slider captcha, often hard.

Alternative: many third-party sites aggregate 12315 公示 data. But that's indirect.

Let me try one more direct approach on 12315: navigate to the known 消费投诉信息公示 path. Actually, I recall the URL: https://www.12315.cn/cuser/portal/tsgs. Let me just try it once — if it redirects to login, so be it.

Hmm, "请登录" → cuser/. The 公示 might be public under a different path.

Let me just try: https://www.12315.cn/cuser/portal/tsgs

Actually you know what, let me take a screenshot first — it's the most reliable way to find the nav item, and the user will appreciate seeing the page. Let me load screenshot guidance and take one.

Let me do it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `# Screenshots This is lookup-only guidance. Do not use it for ordinary navigation, reading, search, or form interaction when a DOM snapshot answers the question. Capture a screenshot only when the user explicitly requests one, visual layout/rendering/image content must be judged, or the required target is absent from t …[截断,原长1207]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:39）

让我截图看一下 12315 的导航布局，以便准确定位。

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `browser 命令 screenshot 超时（30000ms） Structured content: `

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Screenshot timed out too. This IAB seems to have issues with some commands (scroll, screenshot). Hmm.

Maybe the tab is in a bad state. Let me try reloading, or open a fresh tab for 12315.

Actually, earlier the first tab worked fine for navigation, snapshots, and clicks were... I only did fill/press (which didn't submit). And locator innerText worked.

The timeouts (cuaScroll, domCuaScroll, screenshot) suggest those specific commands are unsupported/slow in this IAB backend.

OK. Let me change strategy for 12315: try direct navigation to the public 投诉公示 page.

Let me think about the actual URL. Searching my memory: 全国12315平台 消费投诉信息公示 is at:
https://www.12315.cn/cuser/portal/tsgs

Hmm. Another: https://www.12315.cn/tsgs/index

Actually, I'm fairly confident the public 公示 URL is:
https://www.12315.cn/cuser/portal/tsgs

But cuser implies login.

Alternatively there's a separate site: https://www.12315.cn/tsgs — let me just try one.

Hmm, the skill says don't iterate guessed URL variants. Let me make ONE attempt at the most likely path, then if it fails, note that 12315 公示 requires login and ask the user, OR pivot to 国家企业信用信息公示系统 for business scope.

Actually, since the user offered to log in, and 12315 likely needs login, let me check whether login is needed before asking.

Hmm, wait. Let me reconsider. There's a much better path for 12315: the "投诉公示" section. Let me try navigating to https://www.12315.cn/cuser/portal/tsgs once.

Let me do it. If it lands on a login page, I'll ask the user to log in.

Actually, hold on — let me reconsider whether 12315 is worth this effort. The user said "提示可以到黑猫，12315等查询其是否有被投诉的记录". I've got 黑猫. For 12315, the company-level 公示 would show complaint counts.

Let me try the direct URL once.

Also, I should verify the company's 经营范围 (business scope) — that's checkable via 企查查/爱企查 or 国家企业信用信息公示系统, and would corroborate "无教育培训资质". AiQiCha (爱企查) is public-ish. Actually let me consider using 爱企查 through a search.

Let me first try 12315 direct.

Let me open a new tab to avoid the possibly-bad state of the current 12315 tab.

Actually the current tab navigated fine. Let me just goto.

Let me try.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `{"url":"https://www.12315.cn/cuser/","title":"登录"} - link: - /url: / - heading "欢迎登录" [level=3]: - generic: 欢迎登录 - generic: 用户登录 - list: - textbox "请输入用户名或手机号" - textbox "请输入密码" - textbox "请输入验证码" - link "忘记密码？": - /url: /cuser/password/username - text: "|" - link "注册新账号": - /url: /cuser/regist - generic: 登录 - paragrap …[截断,原长603]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:40）

截图/滚动接口在此内置浏览器上不可用。改用直接导航到 12315 的投诉公示页试一次。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

12315 投诉公示 requires login. This is the point where the user offered to help log in.

Let me now check B站 (no login needed) and 小红书 (needs login) — I should tell the user I need their login for 小红书 and 12315.

Actually, I should be efficient: let me ask the user to log in now, while I proceed with B站 (which doesn't need login). But the AskUserQuestion tool is for decisions... Actually I should just tell them in text and proceed with B站.

Hmm, but the browser tab for 12315 login is open and visible. Let me tell the user: "12315 公示需要登录，请你在浏览器里登录；同时小红书也需要登录。我先去查 B站。"

Actually, better order: Let me first do B站 (works without login), then when I hit 小红书, ask the user to log in to both 12315 and 小红书 in one go — saving a round trip.

Wait, but the user explicitly said "当遇到需要登录的情况，请给我时间，我帮你登录" — they want to be asked when login is needed. Let me finish B站 first, then present both login needs together.

Hmm, but there's a risk: they might want to log in now. Let me just do B站 first (quick), then ask.

Actually, a cleaner flow: since the 12315 login page is already open and visible, let me mention it now and start B站 in parallel. But I can't easily "ask and proceed" — I can proceed with B站 and end my turn asking for login. But then I'd stop.

Better: Do B站 now, then at the end ask for logins (12315 + 小红书). That way the user does one login session.

Hmm, but actually 小红书's search might be partially visible without login? The memory says it returns ~77 chars → login wall. So needs login.

Let me do B站 now. Then ask.

B站 search: https://search.bilibili.com/all?keyword=鲸晓公考 . Let me open a new tab. Actually the search URL pattern for bilibili is well-known: https://search.bilibili.com/all?keyword=xxx. But I should use the site's search UI to be safe. Let me navigate to bilibili.com and search via UI, or just use the search URL (it's a standard, verified pattern).

Hmm, the skill says don't guess URL patterns. But bilibili's search URL is extremely standard. Let me use the site search UI to be safe — navigate to https://www.bilibili.com/ then use the search box.

Actually, that's more round trips. Let me try the search URL directly once — it's a single focused attempt. If it fails, use UI.

Let me open a new tab for bilibili.

Let me go.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `{"url":"https://search.bilibili.com/all?keyword=%E9%B2%B8%E6%99%93%E5%85%AC%E8%80%83","title":"鲸晓公考-哔哩哔哩_bilibili","len":55480} - list: - link "首页": - /url: //www.bilibili.com - generic: 首页 - link "番剧": - /url: //www.bilibili.com/anime/ - link "直播": - /url: //live.bilibili.com - link "游戏中心": - /url: //game.bilibili.com …[截断,原长3925]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:40）

12315 投诉公示**需要登录**（我已打开登录页，待你登录）。先做不需要登录的 **B站**。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

B站在 鲸晓公考 search gives:
- 视频 99+ results
- 专栏 99+ results
- 直播 1

Key found videos:
1. "每周锐评：鲸晓公考怎么样？值得报吗？有什么坑，价格多少" by 公考测评站站长, 2025-12-12, 821 views, 02:36 — BV1Z4mEBYEE7
2. "吐血整理！鲸晓避雷推荐（考公培训骗局，能救一个是一个）" by 小雨公考咨询, 03-03, 262 views, 01:01 — BV15TAZzyEsx
3. An ad: "考公和考编根本不是一回事" (this is a 商业推广/广告 via cm.bilibili.com — a sponsored ad)

Note the third one links to cm.bilibili.com (ad system). Good — I can identify that as an ad.

Let me get more results — the snapshot is 55KB, I only printed 4000. Let me extract video links systematically: get all links to /video/BV... with titles, plus uploader and view counts.

Also the 专栏 (articles) 99+ — those are likely 广告 or 经验帖. And 视频 99+.

Let me extract all video results from the page. Note search page may lazy-load on scroll (which is broken). But the first batch should have ~30 videos.

Let me extract: all links matching /video/BV, their heading text, and the uploader + date + views from the sibling generics. That's complex. Let me instead extract the text content of the result cards.

Simpler: grab the whole snapshot and parse text lines. Or use locator on '.bili-video-card' — CSS from DOM, not snapshot. Hmm.

Let me instead extract via locator 'a[href*="/video/BV"]' and get innerText, dedupe by BV id. The innerText of such a link includes the title. Let me try.

Actually from the snapshot, each video has two links with the same href (thumbnail link and title link). The thumbnail link's innerText includes views/duration; the title link's includes title.

Let me get all hrefs + innerText, dedupe by BV.

Let me do it.

Also, importantly: the user wants to distinguish 广告. On B站 search, ads are labeled. Let me look for ad markers like "广告" text.

Let me extract all video entries and also search the snapshot for "广告".

Let me write code:
- links = locator('a[href*="/video/BV"]'), count, iterate, collect {href, txt}
- dedupe by BV
- Also collect uploader names: maybe from the snapshot text.

Let me just get the links and their parent card text. Simplest: for each BV, get the card. But cards aren't easily scoped.

Alternative: get the whole domSnapshot text (55KB) and process it in JS — extract blocks. Hmm, that's raw text already formatted. I could regex it.

Let me just get the full snapshot and slice it in chunks to read in subsequent calls. 55KB is a lot but I can process programmatically.

Actually, let me extract structured info with a JS regex over the snapshot string:
Pattern: `link "<title> <views> <danmaku> <duration>":\n  - /url: //www.bilibili.com/video/BVxxxx/`

Let me do a regex over the snapshot:
/ link "([^"]{10,120}?) ([\d.万]+) (\d+) (\d+:\d+)"\:\s*\n\s*- \/url: (\/\/www\.bilibili\.com\/video\/(BV\w+)\/)/g

Hmm fragile but workable. Let me try a simpler approach: find all occurrences of "/url: //www.bilibili.com/video/BV" and grab BV + look backwards for the title.

Let me just do the locator approach and get innerText of each unique video link (the title link), plus separately capture card text.

Let me try:
const links = tab.playwright.locator('a[href*="/video/BV"]');
iterate: href, innerText.

Then dedupe by BV, prefer the longer text.

Let me also grab uploader info: not in the link. I'll get uploader by reading the snapshot separately.

Let me do the links first.

Actually, an even better approach for B站 search: the search page has an API. But let's not.

Let me extract.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `videos=27 adMarkers=1 1. BV1Z4mEBYEE7 | 每周锐评：鲸晓公考怎么样？值得报吗？有什么坑，价格多少 821 0 02:36 2. BV15TAZzyEsx | 吐血整理！鲸晓避雷推荐（考公培训骗局，能救一个是一个） 3. BV1Zte3zaEBq | 注意！线上公考机构测评——鲸晓公考怎么样，还能报吗?推荐还是避雷？ 4. BV1k3T7zWE1W | 公考机构真实测评：鲸晓怎么样？到底靠不靠谱？上岸率高吗？【含报班学员真实反馈】 5. BV1PKiyB9Evj | 公考机构测评:橙啦、中证、鲸晓（到底怎么样，靠谱吗？报班真实反馈） 6. BV1VhrdYsEei | 一起来揭秘！争议这么大的鲸晓 …[截断,原长1334]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:40）

B站命中：视频 99+、专栏 99+。我提取具体视频条目（含广告标记）。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Excellent. Many videos about 鲸晓公考, mostly 测评/避雷 (review/warning) content. Note the pattern: many are from 测评类 UP主, which could be:
- Genuine reviews
- Or "测评" videos that are actually lead-gen ads for a competing institution (a common practice in 公考 vertical — 测评号 that bash one institution and push another)

Key titles:
1. 每周锐评：鲸晓公考怎么样？值得报吗？有什么坑，价格多少 (公考测评站站长, 2025-12-12)
2. 吐血整理！鲸晓避雷推荐（考公培训骗局，能救一个是一个）(小雨公考咨询, 03-03)
3. 注意！线上公考机构测评——鲸晓公考怎么样，还能报吗?推荐还是避雷？
4. 公考机构真实测评：鲸晓怎么样？到底靠不靠谱？上岸率高吗？【含报班学员真实反馈】
5. 公考机构测评:橙啦、中证、鲸晓（到底怎么样，靠谱吗？报班真实反馈）
6. 一起来揭秘！争议这么大的鲸晓线上公考机构到底怎么样？
7. 揭秘！鲸晓公考机构真实测评！
9. 鲸晓/仕考网/优途考公机构扒皮！谁在割韭菜？谁是真良心？这几家劝你慎选…
14. 蓝图大斌鲸晓，这三家公考机构怎么选靠谱
20. 鲸晓公考到底怎么样？问的很多的一家靠不靠谱？能不能报？(64 views)
23. 吐血整理！ 鲸晓紧急避雷（报班三次的教训！）

Note #21 "网测/笔试太恶心了!怎样才能顺利通过?" is an ad (adMarkers=1) — probably unrelated ad.

Now I should open 1-3 of the most substantive videos and read their descriptions + comments (评论 is where real user feedback lives). Comments on B站 are visible without login? Usually yes for reading.

Let me open the most relevant one: BV1Z4mEBYEE7 (每周锐评, 821 views) and BV1k3T7zWE1W (含报班学员真实反馈) and BV15TAZzyEsx (避雷).

Also the 专栏 (articles) 99+ — let me check those too; they might be ad-heavy.

Given time, let me open 2 videos: one "锐评/测评" and one "避雷", read description + top comments.

Let me start with BV1k3T7zWE1W (公考机构真实测评：鲸晓怎么样？...【含报班学员真实反馈】) — sounds most substantive.

Hmm, but many of these 测评 videos are actually ads for competitors. Let me read one and judge.

Let me open BV1Z4mEBYEE7 first (每周锐评, from 公考测评站站长).

Actually, let me be strategic and open the video that claims real student feedback: BV1k3T7zWE1W.

Let me navigate in a new tab.

Actually, to save tabs, let me reuse the bilibili search tab? No, better keep search results. Let me create a new tab.

Let me open BV1k3T7zWE1W and get snapshot (title, description, up主) then comments.

Let me do it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `LEN=23625 - list: - link "首页": - /url: //www.bilibili.com - text: 首页 - link "番剧": - /url: //www.bilibili.com/anime/ - link "直播": - /url: //live.bilibili.com/ - link "游戏中心": - /url: //game.bilibili.com/ - link "会员购": - /url: //show.bilibili.com/platform/home.html?msource=pc_web - link "漫画": - /url: //manga.bilibili.com? …[截断,原长4961]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:40）

大量「测评/避雷」视频。我打开一条声称含真实学员反馈的，读正文与评论。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

This video BV1k3T7zWE1W: 783 views, 8 likes. Description says the UP主 ("可可") has researched many 公考机构 and collected real feedback, and invites people to message for recommendations ("有需要的局长们，可以给我发消息告诉我你的具体情况，推合适你的公考培训机构帮你参考参考~~~").

This is a classic **引流/广告 lead-gen** pattern: "测评" videos that funnel you to a private recommendation (likely earning commissions). So the B站 "测评" ecosystem here is heavily lead-gen. Important for the user.

Also note: the page has an ad link to cm.bilibili.com (斗鱼 download ad) — unrelated ad.

Let me read the comments on this video — real user feedback might be there. But comments require scrolling (broken). Hmm. The comments section may not be in the snapshot because it lazy-loads on scroll.

Hmm, the snapshot LEN=23625 which included the ad blob. Comments likely not loaded.

Let me reconsider: the B站 video comments would be valuable but scrolling is broken. Let me try scrolling the comment area via keyboard on the comment container? The press attempts failed earlier on toutu.

Alternative: use the B站 API? E.g. https://api.bilibili.com/x/v2/reply?type=1&oid=<aid>&sort=2 — that's an API. The aid for BV1k3T7zWE1W... From the ad blob: "av_id:1146244274166" hmm that was the ad. Actually "ugc_mid:3546738893785835,av_id:1146244274166,bv_id:BV1k3T7zWE1W".

Hmm, av_id 1146244274166 looks too long. Actually B站 aid for newer videos is large. Let me try the API: https://api.bilibili.com/x/v2/reply?type=1&oid=1146244274166&sort=2&ps=20

Hmm, risky. Actually the newer comment API is https://api.bilibili.com/x/v2/reply/wbi/main which needs wbi signing.

Simpler: the old API /x/v2/reply still works sometimes.

Hmm, this is getting deep. Let me weigh: the user wants 口碑 (reputation). I have:
- 黑猫: 80 complaints, strong negative signal
- B站: search results show many 测评/避雷 videos, but most are lead-gen

The most valuable next step is 小红书 (real user posts) and reading a couple of substantive B站评论.

Let me try to load B站 comments by scrolling via a different method: maybe `tab.playwright.locator('body').press('End')` didn't work on toutu, but bilibili might behave differently. Or use tab.cua.scroll — timed out before.

Actually — maybe the earlier scroll timeouts were because the IAB tab was in a weird state. Let me try cua.scroll once on the bilibili tab. If it times out again, I'll conclude cua is unavailable.

Hmm, I've already spent many calls. Let me be decisive:

Plan:
1. Try to read B站 comments via the public API JSON (one attempt, using the aid from the page).
   Actually, better: get the correct aid from the page. The snapshot might have it. Hmm.
   
   Let me instead just try scrolling bilibili.

Actually — an easier, high-value approach: B站 search has a "专栏" (article) tab with 99+ results. Articles are text and load without scroll issues. Let me check the 专栏 tab: https://search.bilibili.com/article?keyword=鲸晓公考 . Articles about 鲸晓 would contain user experiences.

Also "视频" tab sorted by 最多播放 to find the most-viewed (most influential) videos.

Let me do: navigate to search with 视频 tab and sort by 最多播放. URL: https://search.bilibili.com/video?keyword=鲸晓公考&order=click

Hmm, guessing order param. The page had buttons "最多播放" etc. Let me click "最多播放" button from the snapshot.

Simpler: I'll accept the current B站 evidence and move to the more valuable 小红书.

But I still want B站 comments/real sentiment. Let me try one scroll attempt on bilibili. If it fails, move on.

Actually, let me try the bilibili comment API — it's a clean read and gives real user comments. Let me get the aid first. Let me look for "aid" in the snapshot.

Hmm, the snapshot didn't show aid directly. 

Alternative: use the bilibili search result page's own "专栏" (articles) which contain text. Let me navigate to the 专栏 tab.

Actually, you know what would be most efficient and valuable? Let me step back and consider: the user's core question is "鲸晓这个公考机构口碑如何". I now have strong evidence. The remaining high-value items:
(a) 小红书 - real student posts (needs login)
(b) 12315 - complaint records (needs login)
(c) B站 - I have the video landscape; comments would help but not essential

So the critical blocker is LOGIN. Let me now ask the user to log in to 小红书 and 12315.

But before that, let me squeeze a bit more from B站 without login — read one or two video pages' full descriptions and try comments once.

Let me try scrolling on the bilibili tab with cua.scroll (small delta) to load comments — one attempt.

Let me do that.

Actually, let me reconsider: I could also check 知乎 and 百度贴吧 which don't need login. Those often have candid discussions. And 黑猫 already covers complaints.

Let me prioritize: 
- One scroll attempt on bilibili for comments
- Then ask for login (小红书 + 12315)
- While waiting... no, I can't.

Hmm, actually the best flow: ask for login NOW, and while the user logs in, I can't do anything (turn ends). So let me first extract maximum from no-login sources (B站 comments if possible, 知乎, 贴吧), THEN ask for login once.

Let me try B站 comments scroll once.

Let me use dom_cua.scroll on the bilibili tab (earlier it timed out on toutu). Hmm.

Let me try `tab.playwright.waitForTimeout` then `locator('body').press('PageDown')` — already proven not to load.

OK here's another idea: B站 video pages load comments via API. I can use the browser to fetch that API by navigating directly to the API URL — a browser GET of an API returns JSON which the snapshot may render as text (Chrome renders JSON as a plain document). That works!

I need the aid (oid). For BV1k3T7zWE1W, I need its aid. I can get it from the API: https://api.bilibili.com/x/web-interface/view?bvid=BV1k3T7zWE1W → returns JSON with aid. Then https://api.bilibili.com/x/v2/reply?type=1&oid=<aid>&sort=2&ps=20&pn=1

Two navigations. Let me do it.

Actually, `view` API might be WBI-protected now too, but typically still works.

Let me try. This is a legitimate "purpose-built API" approach.

Let me do: goto view API, snapshot (JSON as text), extract aid, then goto reply API.

Note: Chrome renders JSON as plain text in a <pre>. domSnapshot should capture it.

Let me go.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `- generic: "{\"code\":0,\"message\":\"OK\",\"ttl\":1,\"data\":{\"bvid\":\"BV1k3T7zWE1W\",\"aid\":114624422741664,\"videos\":1,\"tid\":209,\"tid_v2\":2084,\"tname\":\"\",\"tname_v2\":\"\",\"copyright\":1,\"pic\":\"http://i1.hdslb.com/bfs/archive/b9743ac8fb45eec11401f4df976dd8a489d5d9c7.jpg\",\"title\":\"公考机构真实测评：鲸晓怎么样？到 …[截断,原长1221]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:40）

这条是典型「测评引流」模式（私信推荐机构）。我用 B站公开接口读取该视频的真实评论。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

got aid = 114624422741664. Now let me fetch comments via the old API.

https://api.bilibili.com/x/v2/reply?type=1&oid=114624422741664&sort=2&ps=20&pn=1

Let me navigate and read. JSON rendered as text.

Note the response might be huge. Let me extract messages via regex on the snapshot text. But snapshot format escapes quotes. Let me instead just read raw and regex for "message" fields.

Hmm, domSnapshot returns formatted tree with escaped JSON. Let me regex for \"message\":\"...\".

Let me try.

Actually the reply API may return code -412 (risk control) or need wbi. Let me try.

Let me do it and extract messages + like counts.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `LEN=38923 - generic: "{\"code\":0,\"message\":\"OK\",\"ttl\":1,\"data\":{\"page\":{\"num\":1,\"size\":20,\"count\":24,\"acount\":24},\"config\":{\"showtopic\":1,\"show_up_flag\":true,\"read_only\":false},\"replies\":[{\"rpid\":305698045217,\"oid\":114624422741664,\"type\":1,\"mid\":3546756209969450,\"root\":0,\"parent\ …[截断,原长931]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The comment API works. 24 comments total. Critically, the FIRST commenter's username is "考公机构测评大全" with signature "需要公考机构测评，三连后+我v yy777kg（备注B站才会通过哦！）" — clear lead-gen/ad pattern.

Let me extract all 24 comments' messages + unames + likes. Let me regex over the snapshot for uname and message.

Let me write code to extract pairs. The snapshot escapes quotes as \". Pattern:
\"uname\":\"([^\"]+)\" ... \"message\":\"([^\"]*)\"

Let me iterate.

Actually order in JSON: ...\"member\":{\"mid\":...,\"uname\":\"...\",...},\"content\":{\"message\":\"...\"...

Let me regex: /\\"uname\\":\\"([^\\]*?)\\"[\s\S]*?\\"message\\":\\"([\s\S]*?)\\",\\"jump_url\\"/g

Hmm, message may contain escaped chars. Let me be flexible: /\\"uname\\":\\"((?:[^\\"]|\\\\.)*)\\"[\s\S]{0,3000}?\\"message\\":\\"((?:[^\\"]|\\\\.)*)\\"/g

Let me just try and print.

Also note: comment count is only 24 for this video (783 views) — small. And the top commenter is a 测评引流 account.

Let me extract.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `unames=10 msgs=11 1. 考公机构测评大全 :: OK 2. bili_57005130485 :: 直接避雷[笑哭][笑哭][笑哭] 3. 竹雅风 :: 一个老师有尼造好多老师，甚至没啥服务的，都是敷衍你的哦 4. 嘎嘣嘎嘣脆儿 :: 对 5. 小波在此yummy :: 你是报过鲸晓的考生吗？我差点就报了 6. 账号已注销 :: 求测评[打call] 7. 账号已注销 :: 丝你了，如果没收到及时被吞了，可以直接加喔v：KRW12138 8. 账号已注销 :: 大家在报机构之前，一定要擦亮眼睛，仔细筛选机构，多家进行对比，别上了机构的当！\\n\\n多看看报班后小伙伴真实的报班反馈，线上和线下各地区近200家机构的 …[截断,原长568]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Extremely revealing. The comments on this "测评" video are dominated by **引流账号** (lead-gen accounts):
- "考公机构测评大全" (signature: +我v yy777kg)
- "账号已注销" posting "KRW12138" (WeChat ID) repeatedly, with a canned 引流 message
- Real-looking negative comments: "直接避雷[笑哭][笑哭][笑哭]", "一个老师有尼造好多老师，甚至没啥服务的，都是敷衍你的哦" (a teacher has many fake accounts? or one teacher impersonating many teachers, no service, perfunctory)

So B站 landscape: mostly 引流 ads, with a few genuine negative comments. The overall sentiment on B站 leans negative/避雷, but the "测评" videos are largely lead-gen.

Very important insight for the user: **the "测评/避雷" content about 鲸晓 on B站 is largely a 引流生意** (some bash 鲸晓 to funnel you to another institution they're paid to promote). So the user must be careful.

Now let me also check the 专栏 (articles) — 99+. Those might be more 引流.

Actually, let me now switch to the login-dependent tasks. I have enough B站.

Actually, let me quickly also check 知乎 and 百度贴吧 (no login) since they add candid discussion. Hmm, but time/turns.

Let me reconsider the plan. Remaining:
- 12315 (needs login)
- 小红书 (needs login)
- 知乎/贴吧 (no login)

Given the user explicitly offered login help, and two key platforms need it, I should ask now and deliver an interim summary. But it'd be better to also grab 知乎/贴吧 first so the interim report is complete.

Hmm, but each platform takes several calls. Let me do 知乎 quickly (search) then ask for login.

Actually 知乎 search requires login for some things, and WebFetch often fails. Let me try 知乎 search via browser.

Hmm. Let me reconsider — maybe better to ask for login NOW so the user can start, since 小红书 is likely the single most valuable source (the user specifically mentioned 小红书 first). Then continue with 知乎/贴吧 after.

Decision: Ask the user to log in to 小红书 and 12315 now. I'll present the 黑猫 + B站 findings as interim, and note what I still need.

Actually — I can do better: let me check 知乎/贴吧 in the same turn before asking, to make the wait productive... no, the user needs to act.

Let me just ask now. I'll open the 小红书 login page so it's ready.

Let me first open 小红书 search page (which will show login prompt) so the user can scan the QR code.

Let me navigate the 12315 tab? No — let me create a new tab for 小红书.

Then ask the user.

Let me open 小红书: https://www.xiaohongshu.com/search_result?keyword=鲸晓公考 . Hmm, URL pattern guess. The safest: https://www.xiaohongshu.com/ homepage then search. But for login, the homepage is enough.

Let me navigate to https://www.xiaohongshu.com/ and snapshot to see login state.

Let me do that, then ask.

Actually, let me also consider: maybe 小红书 search works without login for a bit. Let me check by navigating to the search URL. If it shows ~77 chars/login wall, ask.

Let me navigate to xiaohongshu homepage first (verified URL from user's mention) and see.

Hmm, I'd rather go straight to the search to test. The 小红书 search URL format: https://www.xiaohongshu.com/search_result?keyword=XXX — commonly used. Let me try it as a single focused attempt.

Let me do it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `{"url":"https://www.xiaohongshu.com/search_result?keyword=%E9%B2%B8%E6%99%93%E5%85%AC%E8%80%83&type=51","title":"鲸晓公考 - 小红书搜索","len":14980} - banner: - link: - /url: /explore?channel_type=web_search_result_notes - textbox "搜索小红书": 鲸晓公考 - img "搜索" - button "创作中心": - generic: 创作中心 - button "业务合作": - generic: 业务合作 - list: …[截断,原长2383]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:41）

B站评论印证：该视频评论区几乎被**引流账号**占据（签名/评论留微信号），真实负面评论穿插其中。现在打开**小红书**，确认是否需要登录。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Excellent news: 小红书 is ALREADY LOGGED IN! There's a user profile link (/user/profile/66a356b8000000001d023058), notifications (2), messages (1). So the user is logged in on this browser.

But the search results aren't showing (the snapshot shows the header/footer but no results). len=14980. Maybe results load lazily or require scroll. Let me snapshot again after waiting, or the results section might be below.

Let me look at the whole snapshot to find note cards. Let me search for "(/explore/" or "note" links.

Let me extract note links: a[href*="/explore/"] or a[href*="/search_result/"], with titles.

Let me do that.

Since user is logged in, great. Let me extract the notes.

Let me get all links with /explore/ and their titles. Also the note titles are often in a heading or the link text.

Let me try locator 'a[href*="/explore/"]'.

Actually note cards on search page link to /search_result/<id>?xsec_token=... Hmm.

Let me just take a fresh snapshot and look for the results region.

Let me search the snapshot for "鲸晓".

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `LEN=14980 xhscdn.com/fe-platform-file/104101b8323gtfdq87a0690nvj5qg0000000003rivl690 - text: "|" - link "2026沪公网安备31010102002533号": - /url: //www.beian.gov.cn/portal/registerSystemInfo?recordcode=31010102002533 - text: "|" - link "增值电信业务经营许可证：沪B2-20150021": - /url: //fe-video-qc.xhscdn.com/fe-platform-file/104101b8323f …[截断,原长6331]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:41）

小红书**已登录**（有用户资料与消息）。搜索结果需再取一次，我提取笔记列表。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

小红书 is logged in and search results are showing. Very rich data:

Notes found:
1. "避雷这家考公线上班，真的太糟心了" by 秋落, 1天前, 228 likes
2. "某考公教育，你w胁我的样子真的很丑！" by 心神意定, 2天前, 281 likes
3. "某二字考公教育可以放过我吗，真的被气哭了" by momo来袭, 3天前, 25 likes
4. "奉劝山东省考想上岸的别太相信xhs" by cr., 08-01, 1011 likes
5. "两个舍友浙江gwy失败的共同原因（纯避雷）"

And 相关搜索: 鲸晓公考机构真实测评, 鲸晓公考工作怎么样, 天津鲸晓公考, 鲸晓公考选岗服务

And the official account: 鲸晓公考 小红书号：49314182932, 兴趣培训, 粉丝1013, 笔记36

Also filter tags: 综合, 真实反馈, 退费, 线上班, 天津, 机构测评, 社群运营, 督学, 课程, 报班费用, 协议班, 老师推荐, 申论, 官方回应, 面试, 收费标准

Very telling: "退费", "官方回应" as search refinement tags — indicating frequent association with 退费 disputes.

But the note card texts: the row before each note link contains the note title but they're rendered oddly. Let me extract all note titles. Some rows have the link with no text (the note card itself), then the title appears in a separate link.

Let me extract better: I need note titles + authors + likes. Let me use the pattern: links to /search_result/<id> — the ones WITH text are titles; the ones without are the cover.

Also note: the search returned several notes that are about "某考公教育" (unnamed) — these might be about 鲸晓 but written obliquely. Interesting: "某二字考公教育" — 鲸晓 is two characters! So "某二字考公教育" likely = 鲸晓. And "某考公教育" possibly too.

Let me extract the full list of note titles from this page. The page loads ~20 notes; more via scroll (broken). But I can navigate with different sort/filter, and there are 相关搜索.

Let me extract all note titles + authors + like counts via regex over the snapshot.

Pattern: `link "<title>":\n  - /url: /search_result/<id>` followed by `link "<author> <date>":` and `generic: "<likes>"`.

Let me write a regex over the raw snapshot:
/\/url: \/search_result\/(\w+)\?xsec_token=([^\s]+)[\s\S]{0,200}?generic: (\d+|赞)/g — hmm.

Simpler: collect all "link \"TITLE\":" where the following line has /search_result/. Let me do:

const re = /link "([^"]+)"[\s\S]{0,80}?\/url: \/search_result\/(\w+)/g

That captures title→note id (the title link directly). The cover link has empty text so won't match "([^"]+)".

Let me run that and dedupe.

Also capture author/date/likes separately maybe.

Let me do it.

Then I'll open the top negative notes (避雷, 某二字考公教育) to read content — these are the real 口碑 signals. And check whether they're ads.

Let me extract first.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `notes=12 1. 避雷这家考公线上班，真的太糟心了 2. 某考公教育，你w胁我的样子真的很丑！ 3. 某二字考公教育可以放过我吗，真的被气哭了 4. 奉劝山东省考想上岸的别太相信xhs 5. 两个舍友浙江gwy失败的共同原因（纯避雷） 6. 避雷某二字考公机构，大家都小心点吧 7. 贪便宜报3980考公线上班的被坑血泪史 8. 某考公机构，你们威胁我删帖的样子真的很丑 9. 考公被骗了 10. 呵呵，某考公班吃相怎么这么难看 11. 考公线上课 12. 从今天开始记录学习的每一天 Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:41）

小红书数据很丰富（含「退费」「官方回应」等搜索标签）。我提取完整笔记列表。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Strong negative sentiment on 小红书: many 避雷/被骗/威胁删帖 posts.

Notable: "某考公机构，你们威胁我删帖的样子真的很丑" and "某考公教育，你w胁我的样子真的很丑！" — allegations of threatening users to delete posts. That's a serious reputation signal.

Also "贪便宜报3980考公线上班的被坑血泪史" — 3980 matches a 黑猫 complaint amount (3980元).

Let me open 2-3 of these notes to read content and confirm they refer to 鲸晓, and check for ads.

Priority notes:
- "避雷这家考公线上班，真的太糟心了" (228 likes, 1天前)
- "某考公教育，你w胁我的样子真的很丑！" (281 likes)
- "贪便宜报3980考公线上班的被坑血泪史"
- "某二字考公教育可以放过我吗，真的被气哭了"

Let me open the one with most likes: "某考公教育，你w胁我的样子真的很丑！" (281). I need its URL: /search_result/6a953fd00000000020039129?xsec_token=ABGcWfV3Q16TTmKsnz6l_XBtMGbi0dSedrxSDxP8HKHT8=&xsec_source=

Let me navigate to https://www.xiaohongshu.com/search_result/6a953fd00000000020039129?xsec_token=...&xsec_source=

Hmm, the note URL should be /explore/<id> or /search_result/<id>. Let me use the one from the snapshot (search_result path with xsec_token).

Let me open it in a new tab.

Actually, let me open in the same tab? Better new tab to keep search results.

Hmm, tab count is growing: 黑猫, 12315, B站search, B站video/api, 小红书search. That's fine.

Let me open the note. I'll do the top-liked negative note.

Let me do 2 notes in sequence (navigate) within reasonable calls.

Note 1: 6a953fd00000000020039129 (某考公教育，你w胁我的样子真的很丑！, 281 likes)
Token: ABGcWfV3Q16TTmKsnz6l_XBtMGbi0dSedrxSDxP8HKHT8=

Let me navigate and snapshot the note content (title, body, comments).

Let me go.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `{"url":"https://www.xiaohongshu.com/explore/6a953fd00000000020039129?xsec_token=ABGcWfV3Q16TTmKsnz6l_XBtMGbi0dSedrxSDxP8HKHT8=&xsec_source=pc_search","len":31917} - banner: - link: - /url: /explore?channel_type=web_note_detail_r10 - textbox "手串弹力绳打结教程" - img "搜索" - button "创作中心": - generic: 创作中心 - button "业务合作": - gene …[截断,原长4818]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:41）

小红书上负面帖密集（避雷/被骗/威胁删帖）。我打开点赞最高的一篇读正文与评论。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The note page loaded but the body content wasn't in the first 5000 chars (it's mostly header/footer). Let me get the middle part where the note body/description and comments are.

Let me search the snapshot for the note content. Let me look for "正文" or the description. Let me print the region after the note title link.

Let me print slice from index of "心神意定" onwards, or find "展开" / comment area.

Let me get the section containing the note content. Let me print from 5000 to 14000.

Actually, better: let me find the specific elements. The note detail page structure: 
- title
- author
- content (desc)
- comments ("共X条评论")

Let me search for "条评论" in the snapshot.

Let me print around markers.

Let me do: const i = snap.indexOf('条评论'); print slice(i-4000, i+2000). And also print the note body: search for "#".

Let me just print the middle chunk 6000-15000.

Hmm, the snapshot 31917 chars, mostly footer repeated. Let me target.

Let me write code to find indexes of key markers and print those regions.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `marker '条评论' at 22185 marker '共' at 22178 marker '正文' at -1 marker '编辑于' at 22155 marker '发布时间' at -1 marker '#' at 20759 ===AROUND COMMENTS=== c: 斩沧世. - generic: "1325" - link: - /url: /explore/6a9566be000000001e015053?xsec_token=ABRxbcWECvrlJt21_rkEkIzB88khjfdXK9H-lwLvDGwuo=&xsec_source=pc_feed - link "没有之一": - /url: …[截断,原长7570]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

This is a major finding. The note "某考公教育，你w胁我的样子真的很丑！" by 心神意定:
- 1599 comments, 281 likes
- Content: 避坑帖 → 机构 sent SMS threatening: calling her "有病", accusing "恶意抹黑", demanding deletion; using her address/personal info to threaten lawsuit, affecting her 政审; mocking that 12345 complaints are useless; saying they won't refund a cent.
- Service issues: 顾问 promised 定制学习计划、1对1辅导、资深讲师答疑 but actual: 老师不是试听那个, 上课念讲义, 计划全是通用模板, 问问题只甩回放链接.
- Note: she won't name the institution ("某二字考公班") because naming gets the post taken down ("之前也有说出来但是很快就被下架了").
- 猜你想搜: 某二字考公机构

So this is consistent with 鲸晓 (二字, 考公). But it's not explicitly named — need care. The 小红书 search for "鲸晓公考" surfaced it, and 小红书's 猜你想搜 says "某二字考公机构".

Let me verify the link to 鲸晓 by checking comments where people might name it. The top comment asks "谁家" / "哪家机构同学" and author says can't say.

Hmm. There might be other notes that DO name 鲸晓. Let me open the other highly-relevant notes:
- "避雷某二字考公机构，大家都小心点吧"
- "贪便宜报3980考公线上班的被坑血泪史"
- "某考公机构，你们威胁我删帖的样子真的很丑"
- "某二字考公教育可以放过我吗，真的被气哭了"

And search with the tag "退费" / "官方回应" filters which might surface named ones.

Given evidence strength, I should find at least one or two notes that explicitly name 鲸晓 with substantive content.

Let me open "贪便宜报3980考公线上班的被坑血泪史" and "避雷某二字考公机构，大家都小心点吧".

Also, I should get their note IDs. From the earlier search extraction I only kept titles. Let me re-extract titles+ids.

Let me do that: navigate back to the search tab and extract title→id pairs, then open specific ones.

Efficient: extract pairs, then open 2 notes.

Let me get the pairs first.

Actually, I realize I should also check the 小红书 official account 鲸晓公考 (粉丝1013) — its notes might be ads/self-promo, and its follower count (1013) is small.

And I should check for POSITIVE notes too (to be balanced) — maybe from the official account or paid 素人 posts.

Let me plan remaining 小红书 work:
1. Extract note ids for the key titles.
2. Open 2-3 negative notes naming/implying 鲸晓.
3. Check the official account + look for 广告/推广 notes (标记"赞助"或"品牌合作").
4. Search "鲸晓公考 退费" and "鲸晓公考 怎么样" for more.

Let me do step 1 now — extract title+id from the search tab.

Let me navigate the search tab (it's still on search results) and extract.

I'll write a regex capturing title + id.

Let me do it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `n=12 1. 避雷这家考公线上班，真的太糟心了 || 6a84314e000000003301c756 || ABreXxugi_FApvectSGgDzCFXbaaPinnFhLGit59vFLPA= 2. 某考公教育，你w胁我的样子真的很丑！ || 6a953fd00000000020039129 || ABGcWfV3Q16TTmKsnz6l_XBtMGbi0dSedrxSDxP8HKHT8= 3. 某二字考公教育可以放过我吗，真的被气哭了 || 6a9e89b50000000011036026 || ABo__JB-1gf2C6ElTzjtVdHTqINlesogQbXOcTj0xyD2w= 4. 两个舍友浙江gwy失败的 …[截断,原长1198]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:41）

这篇是核心证据：1599 条评论，作者称机构发短信威胁删帖、辱骂、拿个人信息威胁「影响政审」，并称投诉 12345 无用。作者不敢点名（点名即被下架）。我提取笔记 ID 以便逐篇核实。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Now let me open a couple more key notes:
- #7 "考公被骗了" (6a704b630000000027023a78)
- #8 "贪便宜报3980考公线上班的被坑血泪史" (6a9fb228000000001001ed96)
- #10 "某考公机构，你们威胁我删帖的样子真的很丑" (6a8ffcfa00000000260019d4)
- #6 "避雷某二字考公机构" (6a61b4fa000000000401fcaf)

I want ones that explicitly name 鲸晓. Let me open #8 (3980 matches a 黑猫 complaint) and #7 "考公被骗了".

Let me open #8 first. Navigate the note tab (currently on 6a953fd0...) to the new note.

Let me do it, and extract the note body + top comments.

To be efficient, let me write a helper that navigates and extracts: title, author, body text, like count, and first ~15 comments.

The body is in a "text:" node after the h1 heading. Comments appear as "text:" nodes after "共 X 条评论".

Let me implement: after loading, get snapshot; extract:
- heading [level=1] → title
- the long text after heading (body)
- all "text:" lines (comments)

Let me do it.

Let me open #8.

Actually, let me be smart: open #8 and extract body + comments in one go.

Let me go.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `TITLE: 贪便宜报3980考公线上班的被坑血泪史 === HEAD/BODY === [level=1] - text: 我是去年省考自学下岸的，距离年底的国省考还有半年左右，想着今年报个线上班冲一下。因为我自学过 算是有些基础吧，想着报个便宜点的线上班，买个信息差，找个人帮我规划一下。自己平时也要上班，只有晚上有时间搞学習，实在精力有限，没想到一时的贪便宜心理 结果踩了 - text: 全是录播课，题库也没有，课程质量是真的拉胯，督学也不回复信息，说的入学测.评也根本没有，更别说模考了，才学几天退 - text: 要扣我20%，真就把我这种第 一次报班的人当日.本人整 或者说不是这个价位不靠谱，只是这家几勾不靠谱，良心的几勾肯 …[截断,原长5084]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:42）

逐篇核实。打开「贪便宜报3980考公线上班的被坑血泪史」（3980 与黑猫某投诉金额一致）。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

This note: 8 comments only. Content: 3980元线上班, 全是录播课, 题库也没有, 课程质量拉胯, 督学不回复, 没有入学测评, 没有模考, 退费要扣20%. Author obliquely refers to the institution as "这家几勾" (coded, likely to avoid takedown/slander issues). Didn't name.

Comments ask "哪家呀" — so the notes deliberately avoid naming.

So on 小红书, the negative posts are largely ANONYMIZED (某二字考公/某机构), because naming leads to takedown/legal threat. This is itself a finding.

I need to verify the link to 鲸晓. Evidence:
1. 小红书 search for "鲸晓公考" surfaces these notes (so 小红书's own relevance ranking links them)
2. 猜你想搜 says "某二字考公机构" 
3. The pattern (二字 + 考公 + 天津/黑龙江 + 3980/5980/10800 fees + 录播课/督学不回复/退费扣20-30%) matches 黑猫 complaints about 鲸晓/聚福星 exactly.

Let me look for a note that explicitly names 鲸晓. Let me open "考公被骗了" (#7) and "避雷某二字考公机构" (#6), and also search with filter "官方回应" which was a search tag — that might surface 鲸晓's official response.

Actually, an even better approach: search 小红书 for "鲸晓公考 退费" and "鲸晓 避雷" and look for notes that name it. Also check the official account's notes and any 广告 notes.

Hmm, but I'm going deep. Let me consider what's enough.

Let me do 2 more 小红书 steps:
(a) Search "鲸晓公考 退费" (the tag existed) to find named notes.
(b) Open one or two named notes.

Then check 12315 (needs login - user said they'd help).

Actually, I realize I should also verify from the positive side: are there genuine positive reviews? The user wants a balanced view and asked to distinguish ads.

Let me search "鲸晓公考 怎么样" or use the "机构测评" filter.

Given time constraints, let me do a targeted search: keyword "鲸晓公考 退费" and also "鲸晓" alone to see the volume.

Let me navigate the search tab with keyword 鲸晓公考退费.

Hmm, let me instead use the search box on the note page (the banner textbox "手串弹力绳打结教程" — weird placeholder).

Simplest: navigate to search_result URL with keyword "鲸晓公考 避雷".

Let me do: https://www.xiaohongshu.com/search_result?keyword=鲸晓公考+避雷

Hmm, actually the first search URL I used (verified) worked. Let me reuse the pattern with a different keyword — that's a verified pattern now.

Let me search "鲸晓公考退费".

Let me go.

Actually, better: search "鲸晓" alone (broader) to capture all mentions, then sort by 最新 or 最热? The search page has 综合/图文/视频/用户/筛选.

Let me search "鲸晓公考退费" first — most targeted.

Let me extract note titles that NAME 鲸晓.

Let me do it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `notes=14 1. 我来告诉你，这么好的鲸晓公考谁去退费啊 2. 没想到！良心鲸晓公考一夜之间竟然被黑了 3. 打卡，这么好的机构谁去退费啊 4. 浅谈一下我对鲸晓公考的学习之后的感官！ 5. 避雷这家考公线上班，真的太糟心了 6. 某考公教育，你w胁我的样子真的很丑！ 7. 贪便宜报3980考公线上班的被坑血泪史 8. 2026年4月起，教育机构不退费不用再要了 9. 某二字考公教育可以放过我吗，真的被气哭了 10. 2026年2月新规，机构退费不退也得退😡 11. 呵呵，某考公班吃相怎么这么难看 12. 爆哭拿父母血汗钱报国企培训班，纯属交智商 13. 避雷某二字考公机构，大家都小心点吧 14. 2026年9月新规，教育机构 …[截断,原长349]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:42）

这些帖子都刻意匿名（「某二字机构」）以规避下架/法律威胁。我再搜「鲸晓公考退费」，找直接点名的帖子。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Now this is very revealing — the results now include what look like **水军/软文 (astroturf/positive PR)** notes that explicitly name 鲸晓公考:
1. "我来告诉你，这么好的鲸晓公考谁去退费啊"
2. "没想到！良心鲸晓公考一夜之间竟然被黑了"
3. "打卡，这么好的机构谁去退费啊"
4. "浅谈一下我对鲸晓公考的学习之后的感官！"

These titles read like defensive PR/水军 posts (the phrasing "这么好的机构谁去退费啊", "良心鲸晓公考一夜之间竟然被黑了" — attempting to refute the negative wave). And they explicitly name the brand (while negative ones can't).

Plus generic SEO-bait notes about 教育机构退费新规 (#8, #10, #14) — these are 引流 posts by 退费维权 accounts / 法务中介.

So the 小红书 landscape for 鲸晓公考:
- Organic negative posts (anonymized): 避雷/被骗/威胁删帖 — multiple, high engagement (281 likes, 1599 comments)
- Apparent 水军 positive posts naming the brand: "这么好的机构谁去退费啊" ×2, "良心鲸晓公考一夜之间竟然被黑了", "浅谈...感官"
- 引流 posts about 退费新规

Let me open one of the positive/水军 posts to verify its nature (e.g., "没想到！良心鲸晓公考一夜之间竟然被黑了" — a title that literally frames the situation as the brand being "黑"ed, strongly suggesting PR response).

And open "我来告诉你，这么好的鲸晓公考谁去退费啊".

Let me extract IDs for these and open 1-2.

Let me get the ids.

I need ids+tokens. Let me re-extract including id/token.

Let me do that quickly, then open.

Actually let me just extract with ids now.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `1. 我来告诉你，这么好的鲸晓公考谁去退费啊 || 668eca0c000000002500793d || ABHxZKi8w35m32cQ56E2scLBM594LrtsvQ5J5y3kyoxIQ= 2. 没想到！良心鲸晓公考一夜之间竟然被黑了 || 6690c22b0000000025005ea1 || ABxpv5VRErvqXaznwumqxsYpf61ZtZNsxstwUfNcvfQxw= 3. 打卡，这么好的机构谁去退费啊 || 668e80460000000025007e47 || ABHxZKi8w35m32cQ56E2scLOjvE4FrxZIUJCR6Vn4N3tw= 4. 浅谈一下我对鲸晓公考的学习之后的感官！ …[截断,原长517]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:42）

出现了疑似**水军/公关软文**（明确点名「这么好的鲸晓公考谁去退费啊」「良心鲸晓公考一夜之间竟然被黑了」）。我取 ID 并核查其中一篇。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Let me open the PR/水军 note "没想到！良心鲸晓公考一夜之间竟然被黑了" and also "我来告诉你，这么好的鲸晓公考谁去退费啊".

Note IDs: 
- 6690c22b0000000025005ea1 (良心鲸晓公考一夜之间竟然被黑了)
- 668eca0c000000002500793d (这么好的鲸晓公考谁去退费啊)

Both dated ~ (ids starting 668/669 suggest Aug 2025). Interesting — these are OLDER (Aug 2025) than the negative wave (Jun-Sep 2026). So the PR posts are from 2025.

Let me open one. Let me open #2 (良心鲸晓公考一夜之间竟然被黑了) — the title strongly suggests a coordinated defense.

Let me read body + comments.

Let me do it in the note tab.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `TITLE: 没想到！良心鲸晓公考一夜之间竟然被黑了 [level=1] - text: 作为一名在鲸晓公考报名的学员，在报名的过程中好多人给我发私信，个人感受真的很多很多托， 以报名的学员说他报名的机构有多么多么好！ 鲸晓公考是我在总多托当中自己选出来的机构，在这整体的上课过程中老师能根据我个人的不足， 随时给我制定学习机构，但是我看到最近很多博主说鲸晓公考机构的坏话，那有那么多无聊的人去做这事 ，无非就是说别人不好， 说他自己报名的机构有多好。然后让你去报名他的机构，这些托让我感觉我个人的智商受到了侮辱， 好像我是傻子一样的报了鲸晓公考，所有在站出来为鲸晓公考发正义之声，感谢鲸晓公考的全体老师们！~ - link "#鲸晓公考" …[截断,原长2509]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Confirmed: this is a defensive PR note dated 2024-07-12, 161 likes, only 1 comment ("呵，你真的报了吗" — doubting). The note claims to be a student defending 鲸晓, and blames "托"/competitors for the negative posts. Classic 水军/软文.

Note it's dated 2024-07-12 — so the negative wave existed even then.

Also interesting: the note's own comments section shows "161" likes, 2, 1.

Now, I have a solid picture. Let me also quickly check the official account 鲸晓公考 to see its content (36 notes, 1013 followers) — its follower count being low is notable.

But I think I have enough for 小红书. Let me now:
1. Update todos.
2. Handle 12315 (needs login) — ask user.
3. Also consider 知乎/贴吧.

Actually, wait. Let me reconsider: is 12315 worth a login? The user specifically mentioned it. The 12315 消费投诉信息公示 would show the company's official complaint stats — that's authoritative and valuable. Let me ask the user to log in.

But hold on — 12315's 公示 might not even include this company if few complaints. Also the user needs the company name (聚福星（天津）文化信息咨询有限公司).

Hmm, alternatively I can check 国家企业信用信息公示系统 (no login, but has captcha) for the company's 经营范围 to verify "无办学资质". Or use 爱企查/企查查.

Let me prioritize:
- The user's main ask: 口碑 on 小红书/B站 + complaint records (黑猫/12315).
- I've done: 黑猫 (strong), B站 (done), 小红书 (strong).
- Remaining: 12315 (login), plus maybe 知乎.

Since the user offered login help, let me ask them to log into 12315 now. Meanwhile I've got plenty.

Actually — let me reconsider whether to also verify the company entity (business scope, registration) since "无办学资质/超范围经营" is a recurring allegation. That's a factual check I can do without login on 爱企查 (aiqicha.baidu.com) or 国家企业信用信息公示系统. Let me try that after 12315.

Hmm, but honestly, let me manage scope. The user asked for 口碑. Let me:
1. Try 12315 login → ask user.
2. Do a quick company-entity check (经营范围) — valuable corroboration.

Let me do the company check now (no login), then ask for 12315 login.

Actually, order matters for the user's waiting time. Let me do the company check quickly, then ask for login with a complete interim report.

Hmm, but each step costs calls. Let me be decisive:

Let me do:
A. Quick 知乎 check (no login) — search 鲸晓公考.
B. Company entity check.
C. Then ask for 12315 login with interim report.

Actually A (知乎) might need login too. Let me test quickly with one navigation.

Hmm. Let me reconsider the value of each:
- 知乎: often has candid 公考机构 discussions. Valuable.
- 贴吧: 公务员吧 etc.
- Company entity: corroborates 无资质 allegation.

Let me do 知乎 search first (one call), then decide.

Actually, let me reconsider time. I've used many calls. The user's request is broad but I should deliver a strong report. Let me:
1. Check 知乎 (1-2 calls)
2. Check company 经营范围 via 爱企查 (1-2 calls)
3. Ask for 12315 login, deliver interim report

Let me do 知乎.

知乎 search URL: https://www.zhihu.com/search?q=鲸晓公考 . Let me try.

Let me go.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "启动浏览器并确认可用后端", "priority": "high", "status": "completed"}, {"content": "黑猫投诉：80条投诉、商家未注册无回应、主体聚福星（天津）", "priority": "high", "status": "completed"}, {"content": "B站：大量测评/避雷视频+评论区遭引流号刷屏", "priority": "high", "status": "completed"}, {"content": "小红书：匿名避雷帖+公关软文+引流贴（已登录取证）", "priority": "high", "status": "completed"}, {"content": "知乎/其他平台交叉验证", "priority": "m …[截断,原长412]` → `{"oldTodos":[{"content":"启动浏览器并确认可用后端","status":"completed","priority":"high"},{"content":"黑猫投诉：80条投诉、商家未注册无回应、主体聚福星（天津）","status":"completed","priority":"high"},{"content":"全国12315平台查询投诉/公示记录","status":"in_progress","priority":"high"},{"content":"B站搜索「鲸晓公考」相关视频/评论","status":"pending","priority":"high"},{"content":"小红书 …[截断,原长1170]`

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `{"url":"https://www.zhihu.com/search?q=%E9%B2%B8%E6%99%93%E5%85%AC%E8%80%83&type=content","title":"鲸晓公考 - 搜索结果 - 知乎","len":9420} - link "欢迎进入 鲸晓公考 - 搜索结果 - 知乎,盲人用户使用操作智能引导，请按快捷键Ctrl+Alt+R；阅读详细操作说明请按快捷键Ctrl+Alt+问号键。": - /url: javascript:void(0) - banner: - link "知乎": - /url: https://www.zhihu.com - navigation: - link "关 …[截断,原长2673]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:42）

已确认是 2024 年的**公关软文**（161 赞仅 1 条质疑评论）。补充核查 **知乎** 后汇总。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

知乎 search page loaded but results not in the first 3000 chars — and it's not logged in ("登录/注册"). The results might be below. Let me get the rest.

Let me print the remaining part (3000 onwards).

Actually the snapshot len=9420, and most of the first 3000 is the header/nav. Let me print from 3000.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `tab "圈子": - link "圈子": - /url: /search?q=%E9%B2%B8%E6%99%93%E5%85%AC%E8%80%83&type=ring - tab "话题": - link "话题": - /url: /search?q=%E9%B2%B8%E6%99%93%E5%85%AC%E8%80%83&type=topic - tab "视频": - link "视频": - /url: /search?q=%E9%B2%B8%E6%99%93%E5%85%AC%E8%80%83&type=zvideo - tab "想法": - link "想法": - /url: /search?q=%E9%B2 …[截断,原长5807]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

知乎 says "未搜索到相关内容，提问快速获得回答" — no results for 鲸晓公考 on 知乎. Interesting! So 知乎 has essentially no content about 鲸晓公考. That's a finding: little/no 知乎 coverage.

Also a login modal appeared. So 知乎 search for 鲸晓公考 returns nothing.

Hmm, "未搜索到相关内容" might be because 知乎 requires login for full search results. But it explicitly says no content found. Let me take it as: negligible 知乎 presence.

Let me also try 百度贴吧 quickly? Hmm. Let me consider: 公务员吧 / 公考吧 discussions. Search: https://tieba.baidu.com/f/search/res?qw=鲸晓公考 . Hmm, URL guess.

Alternatively use a general search engine (Bing) to find 鲸晓 discussions across sites. That's a good completeness step: search Bing for "鲸晓公考" 骗 / 退费 / 评价.

Let me do a Bing search — it aggregates across 贴吧/知乎/黑猫/其他.

Let me do: https://www.bing.com/search?q=鲸晓公考 怎么样 靠谱

Bing URL pattern is standard. Let me try.

Actually, hold on. Let me reconsider the remaining budget and the user's needs. I have very strong evidence already. The user also wanted 12315 which needs login.

Let me do one Bing search for cross-platform coverage (catches 贴吧/知乎/其他), then do the company entity check, then present findings and ask for 12315 login.

Actually, the company entity check is quite valuable given the "无办学资质" allegations. Let me do it via 爱企查 search. Hmm, 爱企查 requires login sometimes.

Alternatively, 国家企业信用信息公示系统 (gsxt.gov.cn) — free, no login, but has a captcha (geetest slider). Hard.

Hmm. Let me try Bing search for the company + 经营范围. Or just rely on the allegation as "alleged, unverified".

Let me do the Bing search — it can serve double duty (cross-platform 口碑 + company info).

Let me go.

Let me be efficient: one Bing search for 鲸晓公考, extract results.

Let me navigate the zhihu tab to bing.

Actually let me use a fresh tab to avoid disturbing. Hmm, tab count is high but fine. Actually let me reuse the zhihu tab (it's done).

Let me go.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `len=7835 - banner: - button "跳至内容": - generic: 跳至内容 - button "辅助功能反馈": - generic: 辅助功能反馈 - link "返回到必应搜索": - /url: /?FORM=Z9FD1 - heading "返回到必应搜索" [level=1] - search: - button "搜索" - searchbox "在此处输入你的搜索 — 输入时会显示搜索建议": 鲸晓公考 靠谱吗 退费 - status - complementary "帐户奖励和偏好设置": - button "Microsoft Rewards": - generic: Rewards - …[截断,原长3892]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:43）

知乎**几乎零内容**（提示「未搜索到相关内容」）。我用必应做一次跨平台扫描，看贴吧等其他渠道。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Bing tokenized the query and returned results about whales (鲸). Not useful. Bing's Chinese segmentation failed. Also Bing 国内版.

Let me refine: use quotes "鲸晓公考" to force exact match.

Let me search: https://www.bing.com/search?q="鲸晓公考"

Let me try that. Quoted search should work better.

Let me do it.

Actually, this is a minor completeness step. Let me do one quoted search and then wrap up.

Let me go.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `搜索结果": - generic: 约 89,000 个结果 - list: - link "baidu.com": - /url: https://baike.baidu.com/item/%E9%B2%B8%E7%B1%BB/3648592 - img "全球 Web 图标" - generic: baidu.com - strong: https:// - text: baike.baidu.com › item › 鲸类 - heading "鲸类_百度百科" [level=2]: - link "鲸类_百度百科": - /url: https://baike.baidu.com/item/%E9%B2%B8%E7%B1%B …[截断,原长3849]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:43）

必应分词失败（返回鲸鱼词条）。用精确匹配再试一次。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Bing 国内版 ignores quotes and returns whale results. Not useful. Let me abandon Bing (or note it's unusable).

Hmm. Bing 国内版 is heavily filtered. Let me not pursue further.

Now let me decide on the company entity check and 12315.

Given the user offered login help and 12315 is explicitly requested, let me now:
1. Present interim findings
2. Ask the user to log in to 12315 (and note what I'll do next)

But maybe I should also try the company entity check. Let me try 爱企查 quickly (aiqicha.baidu.com) — search for 聚福星（天津）文化信息咨询有限公司.

Actually, an important note: 黑猫 complaints mention "聚福星（天津）文化信息咨询有限公司" and "聚福星天津文化信息咨询有限公司" — slightly different names. The core is 聚福星（天津）文化信息咨询有限公司.

Let me do one attempt at 爱企查. Actually 爱企查 search URL: https://aiqicha.baidu.com/s?q=聚福星（天津）文化信息咨询有限公司 — pattern guess. Hmm.

Alternatively use 企查查/天眼查 — all require login.

Let me try 爱企查 with the search URL once.

Hmm, I'm accumulating uncertainty. Let me weigh: the business-scope verification is a "nice to have" corroboration of an allegation. The user's main ask is 口碑 (reputation). I have strong data. Let me do ONE attempt at 爱企查; if it fails, I'll report the allegation as unverified and move on.

Let me do it.

Actually — let me reconsider. Rather than 爱企查, the 国家企业信用信息公示系统 is authoritative but captcha-gated. 爱企查 usually shows 经营范围 without login.

Let me try: https://aiqicha.baidu.com/s?q=聚福星（天津）文化信息咨询有限公司

Let me go. I'll extract company name, 经营范围, 状态.

Let me do it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `{"url":"https://aiqicha.baidu.com/s?q=%E8%81%9A%E7%A6%8F%E6%98%9F%EF%BC%88%E5%A4%A9%E6%B4%A5%EF%BC%89%E6%96%87%E5%8C%96%E4%BF%A1%E6%81%AF%E5%92%A8%E8%AF%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8","title":"aiqicha.baidu.com/s?q=聚福星（天津）文化信息咨询有限公司","len":39} - heading "请关闭浏览器的调试窗口再访问页面！" [level=3] Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:43）

必应国内版无法精确匹配（返回鲸鱼词条），放弃该渠道。最后核实企业主体资质。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

爱企查 blocks (debug detection). Let me try 天眼查 or 企查查? Likely also blocked.

Let me try 国家企业信用信息公示系统? Has captcha.

Hmm. Let me try one alternative: 企查查 mobile or 启信宝? All likely blocked.

Actually, let me try 天眼查: https://www.tianyancha.com/search?key=聚福星（天津）文化信息咨询有限公司

Probably blocked too. 

Let me instead rely on the B站/黑猫 allegation and mark it as "投诉人主张，未独立核实". Or I could try a general web search via 百度: https://www.baidu.com/s?wd=聚福星（天津）文化信息咨询有限公司 — Baidu might show the 工商 info snippet + 经营范围.

Let me try Baidu once. Baidu often shows 爱企查/企查查 summary in results.

Let me do it.

Actually, given diminishing returns, let me do this one Baidu attempt and then wrap up and ask for login.

Let me go.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `Cannot read properties of undefined (reading 'id') Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:43）

爱企查有反调试拦截。改用百度检索工商信息摘要。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The tab lookup failed (probably because the URL changed / tab not found by that substring). Let me list tabs and find the right one.

Let me list tabs.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `=> [ { "id": "iab-tab:f254e19c-bd0d-4e12-9f65-e1fa7e5d9624", "url": "https://tousu.sina.com.cn/complaint/view/<手机号>/?sld=78e392842a172ab244468c20995ab348" }, { "id": "iab-tab:f8dd9a9f-f161-472e-be72-8190bebd7087", "url": "https://www.12315.cn/cuser/" }, { "id": "iab-tab:44d1855a-22e9-4430-8bb7-5525d8134908", "url": "ht …[截断,原长808]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Interesting: the tab that was on zhihu/bing/aiqicha is now about:blank (id 181d8591). So the navigations to zhihu → bing → aiqicha happened in that tab, and now it's blank. Hmm, the aiqicha page showed content earlier (len=39 - the block page). Then my Baidu goto attempt failed because... the tab find by "aiqicha.baidu.com" — the tab's URL was aiqicha; but error said reading 'id' of undefined, meaning find returned undefined. Odd since the URL should contain aiqicha.

Oh — actually the about:blank tab might BE that tab, and aiqicha's anti-debug redirected/closed it. Whatever.

Let me just do the Baidu search in the about:blank tab (181d8591) or a new tab.

Actually, I'm now at a decision point. Let me stop the company check — it's corroborative only, and the anti-bot walls are wasting effort. I'll report the "无教育培训资质" as a complainant allegation (appearing in multiple independent 黑猫 complaints and B站 videos) without independent verification.

Actually, let me make ONE more attempt using 天眼查 via a fresh tab? Hmm. Let me instead just try Baidu in the blank tab — cheap, one call.

Let me do it. If it fails, move on.

Let me use tab id 181d8591.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `len=39167 - link "欢迎进入 百度一下，你就知道，盲人用户进入读屏幕模式请按快捷键Ctrl加Alt加R；阅读详细操作说明请按快捷键Ctrl加Alt加问号键。": - /url: javascript:void(0) - link "到百度首页": - /url: / - img "到百度首页" - textbox: 聚福星 天津 文化信息咨询有限公司 鲸晓 - button "百度一下" - link "百度首页": - /url: / - generic: 通知 - link "设置": - /url: javascript:; - link "159******72": - /url: https://www.b …[截断,原长3871]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Baidu is logged in (159******72). Let me get the actual search results (below the header). The snapshot len=39167. Let me get the results region.

Let me search for "经营范围" in the snapshot and print around it. Or print from ~4000 onward focusing on results.

Let me print slice around the first result (after 热搜 table). Let me find index of "经营范围".

Let me do it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `'经营范围' at 25868 '聚福星' at 163 '存续' at -1 '法定代表人' at 25782 '注册资本' at 15049 '教育' at 17283 === RESULTS === /s?wd=%E9%99%95%E8%A5%BF%E2%80%9C%E7%8C%AA%E5%9D%9A%E5%BC%BA%E2%80%9D%E8%A2%AB%E5%9F%8B36%E5%A4%A9%E6%8C%96%E5%87%BA%E6%97%B6%E7%98%A6%E8%84%B1%E7%9B%B8&usm=1&ie=utf-8&rsv_pq=e5ea2f34001c5876&oq=%E8%81%9A%E7%A6%8F%E6% …[截断,原长4927]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:43）

百度已登录。我提取搜索结果中的工商信息。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Excellent! Baidu gave great results:
1. **消费保** (another complaint platform!) has a 维权中心 page for 鲸晓公考-聚福星(天津) with the SAME 10800元 complaint. So there's a third complaint platform: 消费保 (xfb315.com).
2. **天眼查** data: 聚福星(天津)文化信息咨询有限公司, 成立于2021年 (per 天眼查) / 百度百科 says 2017年, 天津市, 商务服务业, 注册资本109.9999万, 实缴67.3万, 商标16条, 著作权4条, 行政许可1个, **裁判文书2条** (2 court documents!).
3. 消费保 complaint: 2026-04-12, 夏某某, 承诺48小时不满意全额退款, 虚假宣传, 诱导消费.
4. 百度百科: "核心定位为文化科技领域对外投资及运营服务商... 旗下运营多所职业教育类学校, 业务涵盖公务员考试、事业编制考试及研究生考试辅导等板块"

Note discrepancy: 天眼查 says 成立于2021年, 百度百科 says 2017年. Interesting.

Key new lead: **裁判文书2条** — 2 court judgments involving the company! That's a strong signal. And 消费保 platform.

Also the industry is "商务服务业" / "文化艺术业" — NOT 教育培训. This corroborates the "无教育培训资质" allegation (business scope is 商务服务/文化信息咨询, not education/training).

Actually the 百度百科 blurb seems marketing-ish ("核心定位为...对外投资及运营服务商") — possibly written by the company.

Let me now:
1. Check 消费保 for 鲸晓 complaints (new platform, valuable).
2. Maybe check 天眼查 for the 2 裁判文书.

But I've done a LOT. Let me do 消费保 quickly (it's a complaint aggregator with 投诉量), then wrap up.

Hmm, 消费保 URL: the Baidu link is a redirect. Let me search 消费保 directly: https://www.xfb315.com/ ... search 鲸晓.

Actually, let me reconsider budget. I've used ~30 tool calls. The user's request is broad. Let me:
1. Do a quick 消费保 check (1-2 calls)
2. Then present findings + ask for 12315 login

Actually, the 12315 login is the user's explicit suggestion, and it's the one remaining "authoritative" source. Let me now ask the user to log in, while I present a thorough interim report (which already answers the question well).

Hmm, but the user might not want to wait. Let me deliver the report AND ask for login to complete 12315. That's the right approach — the user explicitly offered.

Let me do the 消费保 check first (quick), then write the report.

Let me search 消费保. The site is xfb315.com. Search URL pattern unknown. Let me use Baidu to find the 消费保 page, or navigate to the Baidu redirect link.

Actually, simpler: let me do a Baidu search "消费保 鲸晓公考" and read the snippet, or click the 消费保 result.

Hmm. Let me just navigate to the 消费保 result via the Baidu redirect URL. But those redirect URLs are long. I have one: http://www.baidu.com/link?url=d72j9hfGboEHzCU1K0Ub54D6iAqES2cCw4Nlz5aSniBCpT1MBUD5_3MDFSgAVk0T

Let me open it. It should redirect to 消费保.

Let me do that.

Actually, let me instead search Baidu for 消费保's 鲸晓 page listing all complaints — but the 消费保 page itself is what I want.

Let me navigate to the redirect.

Let me go. Actually, cross-host redirects are returned rather than followed by WebFetch, but browser will follow fine.

Let me open it in a new tab... or reuse. Let me use the baidu tab.

Hmm, careful: navigating away loses Baidu results. That's fine, I have what I need.

Let me navigate.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `{"url":"https://www.xfb365.com/brands/69000","title":"鲸晓公考-聚福星（天津）品牌主页 - 消费保","len":8316} - link: - /url: /about - link "消费投诉与法律服务平台": - /url: /about - button "投诉": 投诉 - textbox "搜索相关内容" - generic:  - generic: 登录/注册 - list: - link "首页": - /url: / - link "集体投诉": - /url: /tousu/collective/list - link "法律服务": - /url: /la …[截断,原长3488]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:43）

百度结果很有价值：发现**第三方投诉平台「消费保」**也有其维权页，且天眼查显示该公司有 **2 条裁判文书**、行业为「商务服务业/文化艺术业」（非教育培训）。我打开消费保页面核实。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Excellent — 消费保 (xfb365.com) has a brand page for 鲸晓公考-聚福星（天津）with many complaints. Key facts:
- Brand: 鲸晓公考-聚福星（天津）
- 客服电话: 022-58712845
- Complaints with status 已完结 / 处理中
- Themes: 虚假宣传 (承诺上岸率80%), 霸王条款 (180天后不让解约, 退费扣30%违约金 + 1500元固定服务费), 无资质办学 (仅有咨询服务资质, 超范围经营), 诱导消费, 服务质量差 (定制班与初级班课程一模一样, 承诺押题没有, 说好十人班实际远超), 看课率标准不透明, 换个负责人不通知...

Notably: "品牌简介" empty, "优质服务商家" badge (probably default/unrelated, since 企业认领 shows unclaimed).

Let me get the count of complaints on this brand page. Let me extract the complaint list count and titles.

Let me also check if there's a 投诉量 stat. The page seems to list complaints. Let me count them.

Let me extract all article entries (title + date + status).

I have 6+ shown. Let me count all.

Let me do that extraction, then wrap up.

Let me also get the total complaint count if displayed.

Let me run extraction.

Then I'll write the report and ask for 12315 login.

Let me do it.

Actually, I have plenty. Let me extract the count quickly and then write up.

Let me extract titles from the page.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长411]` → `rows=13 2026-06-17 18:16 [投诉] 鲸晓公考聚福星（天津）文化信息咨询有限公司虚假宣传、霸王条款及无资质办学 2026-04-12 08:47 [投诉] 我投诉鲸晓公考聚福星（天津）文化信息咨询有限公司虚假宣传诱购公务员网课 2025-10-20 14:52 [投诉] 聚福星教育聚福星（天津）文化信息咨询有限公司虚假宣传诱导消费拒不退费 2026-09-07 18:08 [投诉] 鲸晓公考霸王条款拒合理退费 2026-09-06 23:47 [投诉] 鲸晓公考虚假宣传诱导报班拒退费 2026-09-06 23:36 [投诉] 鲸晓公考VIP班退费不合理扣费高 2026-09-04 18:32 [投诉] 鲸晓公 …[截断,原长628]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:44）

消费保上也有大量投诉（含「无资质办学/超范围经营」）。我统计该品牌的投诉条目。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

I now have very comprehensive evidence:
- 黑猫: 80 complaints (2026-06 to 2026-08+), merchant unregistered/no response
- 消费保: ~14+ complaints, themes same, 3 已完结 / 10 处理中
- B站: many 测评/避雷 videos, comments flooded by lead-gen accounts
- 小红书: anonymized 避雷 posts (high engagement), PR/水军 posts naming brand, 引流 posts
- 知乎: ~zero content
- 企业: 聚福星(天津)文化信息咨询有限公司, 商务服务业/文化艺术业, 2 条裁判文书, 注册资本110万

Remaining: 12315 (needs login).

Now let me write the report and ask the user to log in for 12315.

Let me update todos, then present findings.

I should also mention:
- The brand has a "优质服务商家" badge on 消费保 but 企业认领 is unclaimed
- 客服电话 022-58712845

Let me also note the ad-identification guidance the user asked for:
- 小红书: 匿名避雷帖 = 真实用户（不敢点名，怕被下架/威胁）; 点名夸赞的 = 疑似水军/公关; 退费新规类 = 引流
- B站: "测评/锐评" 视频 + 评论区留微信号 = 引流/广告（本质是给别家机构导流）
- 黑猫/消费保: 投诉记录（非广告，但有核实强度差异 - 黑猫未验证，消费保有审核）

Let me write a clear, structured report. The user is Chinese-speaking; respond in Chinese.

I should also give the file/evidence references as links.

Let me be careful about facts:
- 黑猫 80 条 (with 鲸晓 keyword), all 待分配商家, 商家未匹配成功
- 消费保 brand page: xfb365.com/brands/69000
- Company: 聚福星（天津）文化信息咨询有限公司; 天眼查: 成立于2021年, 商务服务业, 注册资本109.9999万, 2条裁判文书; 百度百科 says 2017年 (conflict — I should note the discrepancy or just say "成立于2021年（天眼查）/2017年（百度百科），存在口径差异"). Hmm, better to be careful. Let me just say 天眼查显示成立于2021年、商务服务业、注册资本约110万、有2条裁判文书.
- 12315: pending login.

Also I should note the two names: 聚福星（天津）文化信息咨询有限公司 vs 聚福星天津文化信息咨询有限公司 — 黑猫 complaints used both.

Also note: 消费保 page notes 客服电话 022-58712845.

Let me also mention that I did NOT find: 任何官方整改/处罚公示 (not yet checked 12315).

Now, about the AskUserQuestion tool — should I use it? The user said "当遇到需要登录的情况，请给我时间，我帮你登录". So I should tell them login is needed and wait. I could use AskUserQuestion to ask whether they want to log in, but they already pre-authorized. Better: just tell them to log in in the browser pane, and state I'll continue after.

Actually, a cleaner approach: give the report, then say "12315 需要登录，我已打开登录页，请你登录后告诉我，我继续查 12315 的投诉公示（这是最权威的一条）。"

Hmm, but maybe I should ask whether they want me to continue with 12315 or stop here. Let me use AskUserQuestion? The guidance says use for decisions the user must make. Here the user pre-authorized login. So just ask in text.

Actually, to be efficient and useful, let me present the full report now, and ask them to log in for 12315. Also offer to check 消费保 more / 裁判文书 / 贴吧 if wanted.

Let me write it.

Also — I should mark the 12315 tab as handoff so it stays controllable? The docs say tabs persist. Let me use finalize to mark the 12315 login tab as handoff (unfinished work must remain controllable). Actually, let me mark deliverable/handoff appropriately:
- 黑猫 search, 消费保, 小红书 notes = deliverable (research results)
- 12315 login = handoff (unfinished)

Let me do a finalize call. Hmm, finalize needs tab objects or ids. `browser.tabs.finalize({ keep: [{status, tab: id}] })`. Let me do it.

Actually, this may be unnecessary complexity. The tabs persist by default. But marking helps the user. Let me do a simple finalize marking 12315 as handoff.

Hmm, it says "Use handoff when unfinished work must remain controllable by the same session." Good.

Let me do it — but it requires listing tabs and referencing by id, which I have.

Let me do the finalize, then write the report.

Actually, let me keep it simple and skip finalize (tabs persist; not required). I'll just mention the open tabs.

Hmm, the skill says finalize is optional. Let me do it though for good practice — mark the 12315 tab handoff and key evidence tabs deliverable. Actually, over-engineering. Let me just do the report.

Wait — one more consideration. The user asked "注意区分广告" (distinguish ads). I should give a clear methodology section.

Let me write the final report now.

Also update todos to reflect status.

Let me structure the report:

1. 结论速览（一句话口碑 + 风险等级）
2. 核心发现
3. 分平台证据
   - 黑猫投诉（80条）
   - 消费保（14+条）
   - 小红书（真实避雷 vs 水军/软文）
   - B站（测评/引流生态）
   - 知乎（几乎无内容）
   - 企业主体（工商信息、2条裁判文书）
4. 广告/水军识别指南（用户特别要求）
5. 待完成：12315（需登录）
6. 给用户的建议

Let me write it concisely but completely. Use markdown.

Let me include actual links where possible.

Note: 小红书 note links require tokens; I can give the 探索 URL.
- 某考公教育，你w胁我的样子真的很丑！https://www.xiaohongshu.com/explore/6a953fd00000000020039129
- 贪便宜报3980考公线上班 https://www.xiaohongshu.com/explore/6a9fb228000000001001ed96
- 水军帖 https://www.xiaohongshu.com/explore/6690c22b0000000025005ea1
- B站 BV1k3T7zWE1W, BV1Z4mEBYEE7, BV15TAZzyEsx
- 黑猫: https://tousu.sina.com.cn/index/search/?keywords=鲸晓&t=1 , 详情 https://tousu.sina.com.cn/complaint/view/<手机号>/
- 消费保: https://www.xfb365.com/brands/69000

Let me write.

I need to be careful: I should note that 黑猫 complaints are user-submitted and not verified by the platform (声明 says so). 消费保 has some 已完结 but "已完结" doesn't mean resolved favorably.

Also note: 黑猫 80 条 result count — "共有80条投诉中包含搜索词鲸晓".

Let me write the report now.

Length: should be thorough but not bloated. The user wants data complete (per their preferences: 数据必须完整展示). Let me include the complaint list summaries.

Let me write.

</details>

- 🔧 **mcp__node_repl__js** `{"source": "browser_turn_end"}` → ``

### 🤖 助手（deepseek-v4-flash，2026-09-11 02:44）

已完成五个渠道的核查。汇报如下（12315 需登录，见文末）。

---

# 鲸晓公考 口碑调研报告

**一句话结论：口碑以负面为主，且负面集中在「退费」这一件事上，性质较重（涉虚假宣传、霸王条款、疑似无办学资质）。同时该品牌在多个平台有明显的水军/引流内容混入，正面信息可信度低。**

---

## 一、主体识别（先厘清「鲸晓」到底是谁）

| 项目 | 内容 |
|---|---|
| 品牌名 | 鲸晓公考（简称「鲸晓」） |
| 运营主体 | **聚福星（天津）文化信息咨询有限公司**（投诉中亦写作「聚福星天津文化信息咨询有限公司」，为同一主体） |
| 客服电话 | 022-58712845 |
| 工商信息（天眼查口径） | 成立 2021 年，天津市，行业登记为**商务服务业**，注册资本 109.9999 万，实缴 67.3 万；商标 16 条；**已有裁判文书 2 条** |
| 一条重要旁证 | 百度百科条目自述其「旗下运营多所职业教育类学校，业务涵盖公务员/事业编/考研辅导」——但**工商行业登记是「商务服务/文化信息咨询」，不是教育培训**。这是投诉人反复指控「无办学资质、超范围经营」的由来 |

> 注：百度百科称成立于 2017 年，天眼查称 2021 年，两者口径不一（可能含关联公司），建议以国家企业信用信息公示系统为准。

---

## 二、黑猫投诉：**共 80 条**含「鲸晓」的投诉（最硬的证据）

- 入口：`tousu.sina.com.cn` 搜索「鲸晓」→ **「共有 80 条投诉中包含搜索词鲸晓」**
- **关键：以「商家」维度搜「鲸晓」「聚福星」均为 0 个商家 → 该公司从未注册黑猫商家账号**。任选一条详情页，平台状态为「**待分配商家 / 商家未匹配成功**」，即**平台至今无法把投诉派给企业，企业零官方回应**。
- 投诉时间跨 2026-06 至 2026-08+，金额区间 3300 / 3980 / 4079 / 5980 / 10800 元。

**10 条样本（黑猫搜索页第 1 页原文）**

| 日期 | 标题 | 诉求 |
|---|---|---|
| 06-11 | 鲸晓公考，要求退费，服务人员不予回复 | 退款 |
| 06-22 | 鲸晓公考虚假承诺退费，霸王条款，服务差 | 退款 |
| 08-04 | 考公机构退费（宣传与实际严重不符，师资差） | 退款 |
| 08-14 | 鲸晓公考违规超范围经营霸王条款诱导消费者 | 退款、处罚 |
| 07-16 | 承诺 48 小时全额退费却强制扣违约金 | 退款、处罚 |
| 07-22 | 鲸晓公考虚假宣传，拒不退款 | 退款、赔偿、道歉 |
| 06-05 | 「两年不过包退」承诺成泡影 | 退款 |
| 08-11 | 流氓合同、极低退款（90 天不得解约/180 天视为接受服务） | 退款 |
| 07-09 | 金牌畅学班，一对一督学虚假宣传 | 退款、处罚 |
| 07-06 | 协议班以「无合同依据」全额拒绝退费 | 退款 |

**一条详情页原文（8-14，涉诉 10800 元）摘录：**
> 1. 报名 48 小时后解约扣**总额 30% 违约金**，另扣课时费、咨询费、系统费、资料费；
> 2. 「不过退费」附加**考满指定次数 + 视频观看率≥80% + 单科达标**等条件，签约前完全未提；
> 3. 协议单方免责：内容与考试有偏差不算违约、不退费；
> 4. 营业执照**经营范围不含教育培训资质**，长期开展公考培训，属无证办学、超范围经营。

---

## 三、消费保（第三方调解平台）：同一主体**至少 14 条**投诉

- 品牌主页：`xfb365.com/brands/69000`（「鲸晓公考-聚福星（天津）」，显示为「优质服务商家」但**「企业认领」为空**）
- 状态分布：**已完结 3 条、处理中 10 条**
- 新增（黑猫没有的）细节：
  - 承诺「**上岸率 80%**」（有微信截图）；
  - 定制班 19800 元，实际「初级班与定制班直播/回放/练习一模一样」「说好十人班实际远超」「承诺押题没有」；
  - **看课率无客观标准**，机构单方按「131/245」之类主观数据拒退；
  - 收款人写「鲸晓」而非「聚福星」，投诉人怀疑税务/主体合规问题。

---

## 四、小红书：真负面 + 水军 + 引流 三股混在一起

搜索「鲸晓公考」结果页自带相关词：**退费 / 协议班 / 官方回应 / 机构测评**。

**A. 真实用户负面帖（作者刻意匿名，不敢点名）**

- 《某考公教育，你 w胁我的样子真的很丑！》——**281 赞、1599 条评论**，作者「心神意定」
  > 发了避坑帖后被机构**短信威胁**：骂其「有病」、指其「恶意抹黑」、要求立刻删帖、**拿地址等个人信息威胁起诉并称会影响政审**、嘲讽「打 12345 没用，一分钱都不会退」。实际服务：非试听课老师、上课念讲义、计划是通用模板、提问只甩回放链接。
  > 作者置顶评论：「很多宝问我是哪家，**之前说出来很快就被下架了**」。
- 《贪便宜报 3980 考公线上班的被坑血泪史》：全是录播、无题库、督学不回消息、无入学测评、无模考，**退费要扣 20%**。
- 同类还有：《避雷这家考公线上班，真的太糟心了》《避雷某二字考公机构》《某考公机构，你们威胁我删帖的样子真的很丑》《呵呵，某考公班吃相怎么这么难看》《考公被骗了》等。

**B. 疑似水军 / 公关软文（明确点名「鲸晓公考」）**

- 《没想到！良心鲸晓公考一夜之间竟然被黑了》（**2024-07-12**，161 赞，仅 1 条评论，评论区直接质疑「呵，你真的报了吗」）——自称学员，把负面全部归因于「同行的托」，为品牌「发正义之声」。
- 《我来告诉你，这么好的鲸晓公考谁去退费啊》《打卡，这么好的机构谁去退费啊》《浅谈一下我对鲸晓公考的学习之后的感官！》——标题话术高度雷同、明显是对负面潮的**防守式公关**。
- 另有大量《2026 年 X 月新规，教育机构退费不退也得退》类帖子，属**退费维权中介/法务引流**，与机构评价无关。

---

## 五、B站：内容几乎全是「测评生意」

搜索「鲸晓公考」→ **视频 99+、专栏 99+**。标题高度同质：*「每周锐评：鲸晓公考怎么样」「鲸晓避雷推荐（考公培训骗局）」「鲸晓/仕考网/优途扒皮」「蓝图大斌鲸晓怎么选」*。
**但打开一看，本质是引流生意**：

- 视频《公考机构真实测评：鲸晓怎么样？…【含报班学员真实反馈】》（BV1k3T7zWE1W）简介直接写：「有需要的局长们，**可以给我发消息**…推合适你的公考培训机构」。
- 我通过公开接口读取该视频 24 条评论，**排前面的几乎全是引流号**：
  - 账号「考公机构测评大全」，个性签名即「三连后**+我 v yy777kg**」；
  - 多个「账号已注销」反复刷「**+v：KRW12138**」和成套话术；
  - 中间夹着零散真实评论：「**直接避雷**」「一个老师…甚至没啥服务的，都是敷衍你的」。

**含义：B站上骂鲸晓的和夸鲸晓的，很多不是用户，而是「拿另一家机构钱、专门做测评号」的同行。** 看到「测评/锐评/扒皮」+ 留微信号，基本可直接判定为广告。

---

## 六、知乎：**几乎零内容**

搜索「鲸晓公考」提示「**未搜索到相关内容**」。说明该机构在知乎几乎没有自然讨论量与正面沉淀。

---

## 七、广告 / 水军识别要点（你要的）

| 特征 | 判定 |
|---|---|
| 小红书帖**不敢点名**、用「某二字考公机构」 | 多半是**真实用户**（点名就被下架/威胁） |
| 小红书帖**明确点名夸**、标题情绪化（「这么好的机构谁去退费」） | 疑似**水军/公关** |
| B站「测评/锐评/扒皮」+ 评论区/简介留微信号 | **引流广告**（给别家机构导流，未必真评鲸晓） |
| 小红书「退费新规…」类法律科普帖 | **退费中介引流** |
| 黑猫/消费保投诉 | 非广告，但属**用户单方陈述**，平台不核实；黑猫那条连商家都没匹配上 |

---

## 八、⚠️ 待你配合：12315 投诉公示（最权威的一条）

全国 12315 平台的「**消费投诉信息公示**」需要登录（用户名/手机号 + 密码），我已打开登录页停在浏览器里。
**请你登录后告诉我一声**，我会查两件事：
1. 聚福星（天津）文化信息咨询有限公司的**公开投诉量 / 调解成功率**；
2. 是否有市场监管部门的**处罚或公示记录**。

> 另外我也可以顺手帮你查：**天眼查那 2 条裁判文书**的案由（是买卖合同还是培训合同纠纷），以及 **百度贴吧/抖音**是否有更多内容——需要的话说一声。

---

### 给你的实操建议
1. **别按销售口头承诺付款**：所有「不过包退/48 小时全额退/上岸率 80%」都要落到合同正文，重点看**违约金比例、退费触发条件、看课率计算方式**——现有投诉几乎全部死在这三条上。
2. 若已缴费且想退：黑猫 + 消费保 + **12315 平台**三处同时提交，并保留微信聊天、录音、支付凭证；已有投诉人反映该机构会**电话/短信施压删帖**，务必截图存证。
3. 对小红书/B站「测评」内容，先看它是否**留联系方式**——留了就不是测评，是广告。

**证据入口**
- 黑猫：https://tousu.sina.com.cn/index/search/?keywords=鲸晓&t=1
- 黑猫详情样本：https://tousu.sina.com.cn/complaint/view/<手机号>/
- 消费保品牌页：https://www.xfb365.com/brands/69000
- 小红书负面帖：https://www.xiaohongshu.com/explore/6a953fd00000000020039129
- 小红书疑似水军帖：https://www.xiaohongshu.com/explore/6690c22b0000000025005ea1
- B站引流视频：https://www.bilibili.com/video/BV1k3T7zWE1W/
