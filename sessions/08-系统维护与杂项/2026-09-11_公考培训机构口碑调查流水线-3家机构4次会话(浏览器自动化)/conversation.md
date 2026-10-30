## 👤 用户（2026-09-11 01:45）

我需要了解鲁越公考这个机构的口碑如何。请你查询各种帖子尤其是小红书，b站等，注意区分广告。提示可以到黑猫，12315等查询其是否有被投诉的记录等等。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The user wants me to research the reputation of "鲁越公考" (a civil service exam training institution in China). They want posts from Xiaohongshu, Bilibili, and complaint platforms like 黑猫投诉 (Sina Black Cat Complaints) and 12315.

This is a web research task. I have the browser-use skill available. The AGENTS.md mentions memory-web-scraping skill for Chinese sites.

Let me think about the approach. The user wants a research report on reputation. I should:
1. Use web search / browser to find info
2. Check 黑猫投诉 (tousu.sina.com.cn)
3. Check 12315 (全国12315平台 - though that requires login usually)
4. Check Xiaohongshu, Bilibili, Zhihu, Baidu Tieba

I need to be careful about the memory-web-scraping skill - it's relevant here. Let me load it.

Actually, per instructions: skills should be invoked via Skill tool when relevant. The memory-web-scraping skill description says "Use when 爬取/抓取网页内容、处理微信公众号/微博/小红书/头条/bilibili/百度系站点内容、绕 JS 渲染墙、WebFetch 失败返回环境异常、使用 playwright persistent context".

This is highly relevant. Let me invoke it.

Also the browser-use:control-browser skill - the main agent must perform browser work itself.

Let me start by loading the memory-web-scraping skill, then set up browser.

Actually let me think about efficiency. The user's instruction: "简单任务直接做并用截图/测试快速验证闭环". But this is a research task - not simple. Let me plan.

Let me first check what tools are available and load the memory skill.

Let me start.

Note: I'm on Windows, Git Bash, no python. Browser use via node_repl MCP with the browser-use skill.

Let me load memory-web-scraping skill first and the browser skill.

Also WebSearch/WebFetch tools - wait, I don't see WebSearch in my tool list. I have WebFetch. The Explore agent has WebSearch. Hmm, my available tools: WebFetch is there but no WebSearch. So I need browser automation for search.

Let me load the skills.

</details>

- 🔧 **Skill** `{"skill": "memory-web-scraping"}` → `<skill_content name="memory-web-scraping"> # Skill: memory-web-scraping # 记忆：网页爬取与内容采集（长期踩坑沉淀） ## 核心策略：两步法 1. **HTTP requests 快筛**：处理非微信/微博/头条的 URL（快，参考成功率 30/42）。 2. **playwright persistent context 兜底**：处理微信（headless=False 必免环境异常）+ 微博/头条（lo_profile）+ HTTP 失败项。 - WebFetch 在多数目标站返回「环境异常」页或混淆 JS → 直接用 playwright persiste …[截断,原长1264]`

- 🔧 **Skill** `{"skill": "browser-use:control-browser"}` → `<skill_content name="control-browser"> # Skill: control-browser # Browser automation (agent.browsers) Use this skill for browser / web-UI tasks: opening and navigating pages, inspecting or reading rendered content, testing local apps, clicking, typing, filling, taking screenshots, and verifying visible page state. If t …[截断,原长17893]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 01:45）

我先加载相关技能（网页爬取经验 + 浏览器控制），然后开始查询。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Let me plan the research. I need to search for "鲁越公考" reputation across:
1. 小红书 (Xiaohongshu) - login wall issue, may need user to scan QR
2. B站 (Bilibili)
3. 黑猫投诉 (tousu.sina.com.cn)
4. 12315
5. 知乎, 贴吧, etc.

Let me set up todos and start with the browser.

First, let me bootstrap the browser and check availability + documentation. Then start with search engines.

Actually, a good approach: use Bing/Baidu search first to find the institution, then go to specific sites.

Let me be efficient. Start with browser setup.

Note: 鲁越公考 — Let me think, "鲁越" likely a 公考 (civil service exam) training brand. Might be in Shandong (鲁) / Zhejiang (越)? Let's search.

Let me set up the todo list and start browsing.

Let me first check backend availability.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "确认机构主体（鲁越公考/鲁越教育，所属公司、地区）", "status": "in_progress", "priority": "high"}, {"content": "黑猫投诉 + 12315 投诉记录查询", "status": "pending", "priority": "high"}, {"content": "小红书口碑（区分广告/真实用户）", "status": "pending", "priority": "high"}, {"content": "B站口碑（视频+评论区）", "status": "pending", "priority": "high"}, {"content": "知乎/贴吧/百度等补充口碑", "status": "pending", "priority": …[截断,原长412]` → `{"oldTodos":[],"todos":[{"content":"确认机构主体（鲁越公考/鲁越教育，所属公司、地区）","status":"in_progress","priority":"high"},{"content":"黑猫投诉 + 12315 投诉记录查询","status":"pending","priority":"high"},{"content":"小红书口碑（区分广告/真实用户）","status":"pending","priority":"high"},{"content":"B站口碑（视频+评论区）","status":"pending","priority":"high"},{"content":" …[截断,原长511]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Now let me bootstrap the browser. First check availability with list().

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nif (!browserPluginRoot) {\n throw new Error(\"Browser plugin root is unavailable in the node_repl host\");\n}\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoo …[截断,原长409]` → `[ { "id": "iab:ff083ecd-b0d0-4cf1-beb0-e36243e254b2", "type": "iab", "name": "ZCode In-app Browser", "capabilities": { "browser": [ { "id": "visibility", "description": "Use to show or hide the browser to the user, and to determine the browser's current visibility. Keep browser work in the background unless the user as …[截断,原长637]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Only iab backend available. Let me get the browser and its documentation.

Actually the skill says: In the first browser call, run the bootstrap, select the backend, and emit the complete API guide in one go.

Let me get iab browser and documentation.

The task has target URLs (xiaohongshu, bilibili, black cat). Hmm, but multiple. Let me use getDefault() since no explicit browser choice... Actually let's just get "iab" since it's the only one. getForUrl with a target... Let's use getDefault().

Actually the skill says: "If the task has a target URL but no explicit browser choice, replace the example URL with the real target". But I have multiple target URLs. I'll use getDefault() — only iab available anyway.

Let me emit documentation.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot =\n process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst browserClientUrl = pathToFileURL(\n join(browserPluginRoot, \"scripts\", \"browser-client.mjs\"),\n).href;\nconst { setupBrowserRuntime } = await import(browserClientUr …[截断,原长410]` → `# Selected Browser - Name: ZCode In-app Browser - Type: iab - ID: iab:ff083ecd-b0d0-4cf1-beb0-e36243e254b2 Recreate this browser wrapper in every fresh Browser Use call using the same verified selection. A new user turn, fresh kernel, or tab error does not invalidate the browser backend; select another browser only whe …[截断,原长42112]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Now let me start the research. First, I need to find what 鲁越公考 is. Let me search.

Let me check the current tab list first, then do a search. Actually there are probably no tabs. Let me just create a tab and search Bing for "鲁越公考".

Given the login walls on Xiaohongshu, let me plan:
1. First search engine to establish entity: Bing search "鲁越公考"
2. 黑猫投诉: https://tousu.sina.com.cn/ search
3. Bilibili search
4. Xiaohongshu (may need login)
5. 知乎/贴吧

Let me start with a dedicated list call to follow protocol, then create tab.

Actually let me combine: list tabs first (dedicated call).

Let me be efficient — I'll do the list call.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot = process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href);\nawait setupBrowserRuntime({ globals: globalThis …[截断,原长411]` → `=> { "controlledTabs": [], "userTabs": [] } Structured content: `

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

No tabs. Let me create a tab and search. I'll use Bing which is generally more accessible in headless/IAB. Actually, let's think about which search engine works best in the IAB. Baidu is fine too. Let me try Bing first.

Let me search for "鲁越公考".

I'll create a tab and navigate to bing search.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot = process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href);\nawait setupBrowserRuntime({ globals: globalThis …[截断,原长411]` → `=> - banner: - button "跳至内容": - generic: 跳至内容 - button "辅助功能反馈": - generic: 辅助功能反馈 - link "返回到必应搜索": - /url: /?FORM=Z9FD1 - heading "返回到必应搜索" [level=1] - search: - button "搜索" - searchbox "在此处输入你的搜索 — 输入时会显示搜索建议": 鲁越公考 - complementary "帐户奖励和偏好设置": - button "Microsoft Rewards" - link "登录": - /url: javascript:void(0) - g …[截断,原长6227]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Bing gave generic results for "鲁" (the character). The search didn't find the institution. Result count 95,400 but all about 鲁 as a character. This suggests "鲁越公考" isn't a well-known indexed brand on Bing, OR Bing's Chinese index is poor.

Note: "为回应符合本地法律要求的通知，部分搜索结果未予显示" — Bing China filters.

Let me try Baidu search instead, which is better for Chinese content. Baidu may have anti-bot. Let me try.

Actually, let me reconsider: maybe the brand name is different. The user says "鲁越公考". Let me search Baidu.

Let me navigate to baidu search.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot = process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href);\nawait setupBrowserRuntime({ globals: globalThis …[截断,原长411]` → `=> - link "欢迎进入 百度一下，你就知道，盲人用户进入读屏幕模式请按快捷键Ctrl加Alt加R；阅读详细操作说明请按快捷键Ctrl加Alt加问号键。": - /url: javascript:void(0) - link "到百度首页": - /url: / - img "到百度首页" - textbox: 鲁越公考 - button "百度一下" - link "百度首页": - /url: / - link "设置": - /url: javascript:; - link "登录": - /url: https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2F …[截断,原长29472]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Interesting. The Baidu search for "鲁越公考" found mostly unrelated results. But I noticed:
1. "鲁跃公考教育" (luyue100.com) — a similar-sounding name, 深耕山东公职考试, 飞龙班. This is a paid ad (置顶推广) - it's a 百度推广 ad.
2. "公考吴越" 微博 - 跃跃公考
3. 鲁越 appears as a person's name in a 华北理工大学 case.

Hmm. So "鲁越公考" may not exist as a major brand, OR the name is slightly different. Note that 鲁跃公考 (luyue100.com) is very similar — 鲁跃 vs 鲁越. Both "luyue". This could be the same brand with a variant name, or the user misremembered.

Important: there's a real risk here. The user asked about "鲁越公考". I found "鲁跃公考教育" (luyue100.com). Let me investigate both. It's possible:
- 鲁越公考 is a small/nonexistent entity
- Or it's the same as 鲁跃

Let me search more specifically. Let me search Baidu for "鲁越公考 怎么样" and also check the 鲁跃 site.

Actually, let me be careful and methodical. Let me:
1. Search for "鲁越公考" 小红书/知乎/黑猫
2. Search 黑猫投诉 for 鲁越 / 鲁跃
3. Check luyue100.com

Let me also try Bing with quotes.

Let me do a couple of parallel investigations. Actually browser is single-tab-at-a-time sequential.

Let me first check 黑猫投诉 search for 鲁越. URL: https://tousu.sina.com.cn/index/search/?keywords=鲁越&t=1

Let me also search Bing for "鲁越公考" 公司.

Actually, an important thing: the user might be referring to a specific institution. Let me ask... no, let me research first. If ambiguous, I'll report.

Hmm, but there's a real risk of researching the wrong institution. Let me gather evidence first, then possibly ask.

Let me look at the 鲁跃公考 site to see if it's related, and search 黑猫.

Let me navigate to 黑猫投诉 search.

黑猫投诉 search URL format: https://tousu.sina.com.cn/index/search/?keywords=鲁越公考&t=1

Let me try.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot = process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href);\nawait setupBrowserRuntime({ globals: globalThis …[截断,原长411]` → `=> - generic: 扫描二维码登录 - generic: 打开微博手机APP - 我的页面 - 扫一扫 - list: - link "验证码登录": - /url: "#" - link "账号登录": - /url: "#" - button "+86": - generic: "+86" - textbox "手机号" - textbox "验证码" - generic: 获取验证码 - button "登录/注册" - text: 未注册手机验证后自动登录，注册即代表同意 - link "《用户协议》": - /url: https://m.weibo.cn/c/regagreement - link "《隐私条款》 …[截断,原长393]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 01:46）

初步搜索发现一个重要线索：百度搜「鲁越公考」大量结果其实指向**「鲁跃公考教育」(luyue100.com)**，且是竞价广告位。我先核实这两个名字是否同一家，再查投诉记录。

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

黑猫投诉 requires login. That's a login wall. Hmm.

Let me try the public search page differently. Maybe https://tousu.sina.com.cn/search?keywords=鲁越 works without login, or the company page.

Actually 黑猫投诉 (tousu.sina.com.cn) search does typically require login now. Let me check if there's a non-login path.

Alternative: use Bing search with site:tousu.sina.com.cn 鲁越公考. Or use a search engine to find 黑猫投诉 pages.

Let me try Bing for "黑猫投诉 鲁越公考".

Actually, let me reconsider the whole approach. The key issue: does "鲁越公考" exist as a brand? Let me search on Xiaohongshu and Bilibili directly, plus check the 鲁跃 site.

Let me try:
1. Bing: 鲁越公考 (with quotes maybe)
2. Bilibili search: https://search.bilibili.com/all?keyword=鲁越公考
3. Xiaohongshu search

Let me do Bilibili first (no login needed for search).

Actually, let me think about efficiency. Let me do a few searches in sequence.

Let me first try Bing with a more targeted query to find 鲁越公考's actual presence, e.g. "鲁越公考" 公务员.

Alternatively use 搜狗微信/知乎.

Let me try Bilibili search since user specifically asked.

Let me do it.

Actually wait — I should consider that the user may have the name slightly off, or that 鲁越公考 is a regional brand. Let me search 百度 with "鲁越公考" 怎么样 to see if there are 知乎/贴吧 discussions.

Let me do a combined approach: search Bing for 「鲁越公考」 知乎 OR 贴吧 OR 小红书.

Hmm, Bing gave poor results. Let me try 360 search or Sogou.

Let me try Sogou: https://www.sogou.com/web?query=鲁越公考

Let me try that. Also 搜狗 has 微信公众号 search.

Let me be systematic. I'll run several searches. Let me start with Bilibili (user explicitly asked, and it's accessible).

Plan for this call: navigate to bilibili search.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot = process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href);\nawait setupBrowserRuntime({ globals: globalThis …[截断,原长411]` → `=> - list: - link "首页": - /url: //www.bilibili.com - generic: 首页 - link "番剧": - /url: //www.bilibili.com/anime/ - link "直播": - /url: //live.bilibili.com - link "游戏中心": - /url: //game.bilibili.com/platform - link "会员购": - /url: //show.bilibili.com/platform/home.html?msource=pc_web - link "漫画": - /url: //manga.bilibili.c …[截断,原长42857]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 01:46）

黑猫投诉搜索需登录。先按用户指定的平台查 B站（搜索无需登录）：

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

B站搜索 "鲁越公考" 没有直接命中这个品牌 — 结果都是泛化的公考内容（毕仲、承鲁、沪峥、川进、昭野、荆锐、桂鸥、青尺、津橙、颜钊等 — these look like a network of regional 公考 brands, likely all ads/soft-marketing with the same template). No "鲁越公考" in the results.

Interesting: there's a "每天锐评一家公考机构之大斌公考" series by "卡卡公考站" — could be useful for finding reviews of 鲁越.

So B站 has 0 direct hits for 鲁越公考.

Key observation: The 综合 tab shows results, but there might be more precise results. Let me check the "用户" tab (0) and "专栏" (40). Actually 专栏 40 might be relevant.

Hmm, but the search seems to be doing fuzzy matching. The results show many "XX公考" regional brands.

Wait — I notice a suspicious pattern: 承鲁山东公考, 沪峥公考, 川进公考, 昭野黑龙江公考, 青尺公考, 津橙公考, 颜钊公考, 桂鸥公考, 荆锐公考, 毕仲甘肃事考... These all look like the SAME MCN/template — a wave of regional 公考 brands on B站. This is a known 抖音/B站 marketing pattern. "鲁越公考" could be one of these (鲁 = 山东). And "承鲁" = 山东 too. Hmm.

Actually, wait. Let me reconsider. These results are the fuzzy match for "公考" + something. They might all be from a similar ad network.

Let me search B站 专栏 for 鲁越 specifically, and also search for "锐评 鲁越".

Actually, more efficient: let me search on 小红书 and 知乎 directly. But 小红书 needs login.

Let me reconsider the whole thing. The user asks about "鲁越公考". I've found:
- Baidu: no direct hits; a lookalike "鲁跃公考" (luyue100.com, 山东) with a paid ad
- Bilibili: no direct hits

Let me search more specifically. Let me use Baidu search for "鲁越公考" 口碑 / 怎么样 / 退费. And check 知乎.

Hmm, also let me verify whether "鲁越公考" might exist under a company name. Let me search 天眼查/企查查 for 鲁越 教育.

Let me also try 黑猫投诉 via Bing site search.

Let me plan next calls:
1. Baidu: "鲁越公考 怎么样" or "鲁越公考 退费"
2. 知乎搜索: https://www.zhihu.com/search?type=content&q=鲁越公考 (may need login)
3. 小红书: https://www.xiaohongshu.com/search_result?keyword=鲁越公考

Let me do the Baidu one with a refined query. Actually, let me use the searchbox on Baidu to search "鲁越公考 口碑".

Hmm, but given the ambiguity, maybe I should ask the user for clarification about which institution (地区/全名). But the user asked me to research; asking might be reasonable given I found a very similar name (鲁跃). But let me gather a bit more first — maybe 鲁越公考 is indeed a thing.

Actually — important insight: I should search 抖音 too (公考机构 heavily marketed there). And 黑猫.

Let me try a different search engine that might index better: 搜狗 or 360. Let me try Sogou.

Actually, let me try Bing with the site: operator for 黑猫投诉 and 知乎.

Let me do: Bing search "鲁越公考 投诉".

Let me run a Baidu search for 「"鲁越公考"」 with quotes to force exact match.

Baidu URL: https://www.baidu.com/s?wd=%22%E9%B2%81%E8%B6%8A%E5%85%AC%E8%80%83%22

Let me do that.

Actually let me combine: I'll navigate to Baidu and search exact phrase. Also let me check whether 鲁越公考 has a 官网.

Let me do it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot = process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href);\nawait setupBrowserRuntime({ globals: globalThis …[截断,原长411]` → `正在搜索 鲁越公考 和 鲁跃公考 区别 大家还在搜 公务员报考条件 公务员怎么考 考公务员需要什么学历 粉笔公考和中公哪个好 公基考什么 公考是什么意思 粉笔公考 公考论坛qzzn 公考资讯网 公考面试 考公务员难吗 粉笔公考怎么样 线上公考机构怎么选?鲁跃、观鲁、燕诺测评来揭秘 0个回复最近更新于: 2026年01月15日 1楼: 缺点:333 百度贴吧 鲁跃公考教育 - 山东本土公考辅导_省考选调生事业单位面试培训... 鲁跃公考教育深耕山东本土考情,只做山东人自己的公考辅导,专注山东公务员、选调生、事业单位、遴选、教师编、警法考试等公职考试培训。依托山东本土教研团队,紧跟考试政策、考情变化与命题趋势,打造鲁跃飞龙班系列课程,涵 …[截断,原长1557]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 01:46）

B站无「鲁越公考」直接命中。用精确匹配再查百度，确认主体是否存在：

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Now this is very informative. Baidu's own "大家还在搜" shows: **"鲁越公考 和 鲁跃公考 区别"** — so Baidu recognizes both and people are searching for the difference. This confirms 鲁越公考 exists as a search term, and 鲁跃公考 is a related/competing brand.

Results show:
- 百度贴吧: "线上公考机构怎么选?鲁跃、观鲁、燕诺测评来揭秘" — 0条回复
- 鲁跃公考教育 luyue100.com — 山东本土
- 观鲁公考 — 山东
- 鲁公社 — 山东
- 浙江考公考编笔试班怎么选 (zjsxgk)

So there's a cluster of Shandong 公考 brands: 鲁跃, 观鲁, 鲁公社, 燕诺, and possibly 鲁越. This looks like a highly competitive, SEO/软文-polluted niche.

Important: the search results are dominated by 软文 (SEO articles) — 百度知道 answers, 商业信息/菏泽广电网 (a low-quality syndicated content farm), 山东鲁公社小路 (小红书-style), etc. Classic 公考机构 marketing.

Now I need to specifically find 鲁越公考. Let me search Baidu for "鲁越公考" 退费 / 投诉, and 知乎.

Also let me try 小红书 direct.

Let me search Baidu: 「鲁越公考 和 鲁跃公考 区别」 to see what comes up — that's a real user query.

Actually that was Baidu's suggestion, not a clickable search... but I can search it.

Let me do: Baidu search "鲁越公考 鲁跃公考 区别".

Hmm, but more valuable: search 黑猫投诉 for 鲁越, and 小红书.

Let me think about which is highest value:
1. 黑猫投诉 — user explicitly asked. Need to get past login. Let me try the company search API endpoint or a Google/Bing site search.
2. 小红书 — user explicitly asked.

Let me try 黑猫投诉 again with a different URL. The 黑猫投诉 has a public search at https://tousu.sina.com.cn/index/search/?keywords=xxx&t=1 but it forced login. 

Alternative: 黑猫投诉 has company pages: https://tousu.sina.com.cn/company/view/?couid=xxx

Maybe I can use Bing search with site:tousu.sina.com.cn 鲁越.

Let me try Bing: https://www.bing.com/search?q=site%3Atousu.sina.com.cn+%E9%B2%81%E8%B6%8A

Hmm, Bing China filtered. Let me try.

Actually, let's try the 黑猫投诉 mobile site or the API: https://tousu.sina.com.cn/api/index/s?keywords=鲁越 ... probably needs login too.

Let me try 小红书 first since it's explicitly requested and I have a strategy (login wall acknowledged). Let me check if 小红书 search page loads any content.

Let me navigate to xiaohongshu search.

Actually, wait. Let me be smart: use Baidu to find 小红书 posts about 鲁越公考. Baidu indexes 小红书 notes. Query: 鲁越公考 小红书 site:xiaohongshu.com → or just "鲁越公考 小红书".

Hmm.

Let me do a focused round:
Step A: Baidu search "鲁越公考 退费" (to find complaints)
Step B: 小红书 direct search
Step C: 黑猫 via Bing/other

Let me start with Baidu "鲁越公考 退费 投诉" since it may surface 黑猫/贴吧/知乎 complaints all at once.

Let me do it.

Actually — a thought: I should also consider that "鲁越公考" might be a brand in a specific province, e.g., 山东 (鲁) — the "-越" part is odd. Or it might be 鲁越 = combination. Let me just search.

Let me search Baidu for "鲁越公考" 退费.

Actually, let me instead search 知乎 directly and 小红书 directly, plus a targeted Baidu. Let me sequence:

Call 1: Baidu "鲁越公考 退费 投诉 骗局"
Call 2: 知乎 search
Call 3: 小红书 search
Call 4: 黑猫

Let me do Call 1.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot = process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href);\nawait setupBrowserRuntime({ globals: globalThis …[截断,原长411]` → `正在搜索 鲁越公考 机构 真实情况 退费政策 大家还在搜 12328投诉驾校退费 鸭题库不过退费班是真的吗 12315培训退费支招 驾校退费投诉电话 投诉教练的后果 驾校不退钱找哪个部门投诉 怎么投诉培训机构不退款 驾校不退费向谁投诉 考公机构可以全额退款了?千万别忙着冲!_澎湃号·政务_澎湃新闻... 2026年5月17日对方自称是某公考机构的客服,说现在可以办理课程退款,让他添加企业微信。 程某添加后,对方发来链接让他下载一款名为“谷*小二”的APP。注册后,客服指导他办理退费,程某提供了自己的银行卡号。不久,他的银行账户收到了131元转账。 客服接着说,可以做一个“手动增值基金盈利垫资方案”,购买100元,完成后可以提现220 …[截断,原长1831]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 01:46）

百度联想词确认存在「鲁越公考 和 鲁跃公考 区别」——说明鲁越公考确实是个搜索词，且和山东系（鲁跃/观鲁/鲁公社）混在一起。现在查投诉与口碑：

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

The Baidu search for 鲁越公考 + 退费/投诉/骗局 returned general articles about 公考 training scams, but nothing specifically about 鲁越公考. This is a signal: no indexed complaints specifically about 鲁越公考.

Note the 人民网领导留言板 result about 领*公考 (领创/领航公考?) in 山东 — not 鲁越.

Now, I've established:
- 鲁越公考 has essentially no substantive indexed content on Baidu except the "和鲁跃公考区别" suggestion.

Let me now check:
1. 小红书 (direct)
2. 黑猫投诉 (need workaround)
3. 知乎

Let me try 小红书 direct search. It'll probably require login. Let me try.

Actually, let me reconsider. Given the strong similarity to 鲁跃公考 (luyue100.com), and that Baidu auto-suggests "鲁越公考 和 鲁跃公考 区别", it's likely that:
- 鲁越公考 is either a smaller/newer brand
- or a variant name of 鲁跃

Let me check 鲁跃's site and its 备案 to get the company name, then search that company on 黑猫/12315.

Actually, the user asked about 鲁越公考. Let me focus on finding 鲁越公考 specifically. Let me:

1. Search 小红书: https://www.xiaohongshu.com/search_result?keyword=鲁越公考
2. Search 知乎: https://www.zhihu.com/search?type=content&q=鲁越公考
3. 黑猫: try https://tousu.sina.com.cn/ search via a different entry

Let me also try 抖音 web search: https://www.douyin.com/search/鲁越公考

And 微博: https://s.weibo.com/weibo?q=鲁越公考

Let me batch these. Browser is sequential but I can navigate one at a time.

Let me start with 小红书.

Let me update todos too.

Let me do 小红书 now.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "确认机构主体（发现同名近似品牌鲁跃公考 luyue100.com，需甄别）", "priority": "high", "status": "in_progress"}, {"content": "小红书口碑（区分广告/真实用户）", "priority": "high", "status": "in_progress"}, {"content": "B站口碑（已查：搜「鲁越公考」无直接命中）", "priority": "high", "status": "completed"}, {"content": "黑猫投诉 + 12315 投诉记录（需绕过登录墙）", "priority": "high", "status": "pending"}, {"content": "知乎/贴吧/微博/抖音补充口碑 …[截断,原长412]` → `{"oldTodos":[{"content":"确认机构主体（鲁越公考/鲁越教育，所属公司、地区）","status":"in_progress","priority":"high"},{"content":"黑猫投诉 + 12315 投诉记录查询","status":"pending","priority":"high"},{"content":"小红书口碑（区分广告/真实用户）","status":"pending","priority":"high"},{"content":"B站口碑（视频+评论区）","status":"pending","priority":"high"},{"content":"知乎/贴吧/百度等补充 …[截断,原长968]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Let me now do 小红书 search.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot = process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href);\nawait setupBrowserRuntime({ globals: globalThis …[截断,原长411]` → `登录后查看搜索结果 可用 小红书 或 微信 扫码 小红书如何扫码 手机号登录 +86 获取验证码 登录 我已阅读并同意《用户协议》《隐私政策》《儿童/青少年个人信息保护规则》 新用户可直接登录 创作中心 业务合作 发现 RED 直播 发布 通知 消息 登录 沪ICP备13030189号 | 营业执照 | 2026沪公网安备31010102002533号 | 增值电信业务经营许可证：沪B2-20150021 | 医疗器械网络交易服务第三方平台备案：(沪)网械平台备字[2019]第00006号 | 互联网药品信息服务资格证书：(沪)-经营性-2023-0144 | 违法不良信息举报电话：4006676810 | 上海市互联网举报中心 | …[截断,原长855]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

小红书 requires login ("登录后查看搜索结果"). This is a login wall as my memory skill noted. I need the user to log in (scan QR).

Let me try a workaround: Baidu indexes 小红书 notes. Let me search Baidu for "鲁越公考" site:xiaohongshu.com, or use the 小红书 mobile web (www.xiaohongshu.com is the main).

Alternatively, use 百度 with "鲁越公考" 小红书.

Also there's a trick: 小红书 notes are indexed by search engines; the note pages are viewable without login sometimes.

Let me do Baidu: 鲁越公考 小红书.

Actually — let me step back and think about whether I should ask the user. The 小红书 login wall requires user action. Per my memory skill: "登录墙站点（微信、小红书）需要用户先扫码/点击验证 → 预留交互".

Before asking the user to log in, let me exhaust the no-login sources: 
- 知乎 (may need login)
- 微博 search (s.weibo.com needs login often)
- 抖音 web (needs login)
- 黑猫 (needs login)
- 贴吧 (no login for reading)
- 百度/搜狗/360

Let me check 贴吧 and 知乎.

Also — very important — let me verify the actual identity. Let me search 企查查/爱企查 for "鲁越" 教育 companies. Actually 爱企查 (Baidu) is accessible.

Hmm, but "鲁越公考" might not be a registered company name; it's a brand.

Let me reconsider: The user might actually be asking about a specific well-known thing. Let me search 抖音 and 知乎 quickly, then decide.

Let me try 知乎 search first.

Actually, let me try Sogou which has better coverage of 微信公众号 and 小红书-ish content. https://www.sogou.com/web?query=鲁越公考

Let me do that.

Hmm, I'm using a lot of context. Let me be more economical: use `#content_left` innerText slices, and keep them short.

Let me try 搜狗 and 知乎 in sequence.

Let me do 知乎 first: https://www.zhihu.com/search?type=content&q=鲁越公考

Actually, 知乎 search requires login now too (since 2023 知乎 blocks 未登录). Let me test.

Let me try 搜狗 instead — better ROI.

Actually, let me reconsider: maybe I should search for the specific term on multiple engines in one go using a search aggregator. But let's just do Sogou.

Let me do Sogou.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot = process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href);\nawait setupBrowserRuntime({ globals: globalThis …[截断,原长411]` → `返回首页>> IP：112.224.13.205 访问时间：2026.09.11 01:47:12 SourceVerifyCode：b5e12bfc4c3c From：www.sogou.com 此验证码用于确认这些请求是您的正常行为而不是自动程序发出的，需要您协助验证。 验证码： 请依次点击【堪,邯,乔,楷】 提交 提交后没解决问题？欢迎反馈。 企业推广关于搜狗免责声明意见反馈 © 2026 Sogou Inc. - 京ICP证050897号 - 京公网安备110000000025号 Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-11 01:47）

小红书需要登录（符合已知特性）。先用免登录渠道继续挖，稍后再请您扫码。试搜狗（对公众号/小红书内容覆盖更好）：

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Sogou has a CAPTCHA. Let's skip Sogou.

Let me try 360 search (so.com): https://www.so.com/s?q=鲁越公考

Let me also try 知乎.

Let me do 360.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot = process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href);\nawait setupBrowserRuntime({ globals: globalThis …[截断,原长411]` → `搜索 为您推荐 · 反馈 鲁跃公考官网十大公考机构实力排名博越公考官网齐麟公考官网齐麟公考刷题组电子版观鲁公考官网齐麟公考鲁信教育官网山东公考培训机构排名前十十大公考培训机构排名山东公务员培训机构排名前十山东省公考培训机构排名一览表 反馈 设置 登录 网页 AI问答 图片 视频 资讯 地图 文库 百科 翻译 软件 良医 为您推荐 · 反馈 鲁跃公考官网十大公考机构实力排名博越公考官网齐麟公考官网齐麟公考刷题组电子版观鲁公考官网齐麟公考鲁信教育官网山东公考培训机构排名前十十大公考培训机构排名山东公务员培训机构排名前十山东省公考培训机构排名一览表 鲁越是谁的化名 他一生使用过140多个笔名, 鲁越 是其中之一.鲁越 是鲁迅的化名之一。鲁 …[截断,原长2067]`

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

Now key finding from 360 search AI answer:

"临沂市兰山区鲁越教育培训学校：位于临沂市兰山区红旗路与羲之路交汇西100米路北"

So there IS a "临沂市兰山区鲁越教育培训学校" — a 鲁越 education school in Linyi, Shandong. But that's "鲁越教育" (general education), not necessarily "鲁越公考".

Also 360 recommends a cluster: 鲁跃公考, 博越公考, 齐麟公考, 观鲁公考, 鲁信教育 — all Shandong 公考 brands.

Hmm, "博越公考" — another similar name.

Also "鲁越醉蟹" — a 抖音 account (南昌压缩车? weird SEO spam).

So the picture: "鲁越" is a common-name element. There's:
- 临沂市兰山区鲁越教育培训学校 (institution in Linyi)
- 鲁跃公考 (luyue100.com, Shandong, 飞龙班)
- 博越公考
- 观鲁公考
- 鲁公社
- 鲁信教育

The user asks about "鲁越公考". It's plausible that:
(a) 鲁越公考 is a real but small/regional brand with little online footprint
(b) The user means 鲁跃公考 (very similar, and Baidu suggests "区别")

I need to search more precisely. Let me look for 抖音/小红书/知乎 for "鲁越公考".

Actually — very important: 360's AI answer gave "临沂市兰山区鲁越教育培训学校". Let me investigate that entity. It's in 临沂 (Linyi, Shandong). Let me search for it.

But that's "鲁越教育" not "鲁越公考".

Hmm, let me try 抖音 web search for 鲁越公考 — 公考机构 market heavily on 抖音.

Also let me search 爱企查 for "鲁越" 公考/教育 to enumerate companies.

Let me try 抖音: https://www.douyin.com/search/鲁越公考 — will likely need login.

Alternatively, search 360/百度 for "鲁越公考" 抖音.

Hmm.

Let me think about the most likely reality: 鲁越公考 might be a brand that operates mostly on 抖音/小红书/微信 with little web presence. Or it might be a 山东 regional brand.

Let me try 黑猫投诉. The user explicitly wants that. Let me find a way.

黑猫投诉 public search: Let me try https://tousu.sina.com.cn/index/search/?keywords=%E9%B2%81%E8%B6%8A&t=1 → it showed a login modal. Maybe the modal is dismissible or the results are behind it. Earlier snapshot showed ONLY the login modal, no results. Hmm.

Alternative: 黑猫投诉 company search via Bing: site:tousu.sina.com.cn 鲁越

Or use the 黑猫投诉 API: https://tousu.sina.com.cn/api/index/s?keywords=鲁越 ... let me try. Actually there's a public JSON API: https://tousu.sina.com.cn/api/company/search?keywords=鲁越

Hmm, guessing endpoints is discouraged.

Better: 12315 (全国12315平台) requires login + captcha. Not feasible.

Alternative complaint platforms: 
- 黑猫投诉
- 聚投诉 (21CN, now defunct?)
- 12315
- 天眼查/企查查 风险信息
- 中国裁判文书网 (legal disputes)
- 信用中国 / 国家企业信用信息公示系统 (经营异常)

Let me try 爱企查 (accessible) for the company, then check 天眼查 for 投诉/诉讼.

OK let me prioritize. Given the ambiguity about the entity, and that 小红书 requires the user to log in, I think the right move now is:

1. Do a couple more targeted searches (抖音/知乎/微博 via 百度 site search) to pin down 鲁越公考.
2. Then ask the user to log into 小红书 if needed, and clarify the entity.

Actually, let me try a smarter search: use 百度 with site: operators for the platforms:
- 鲁越公考 site:xiaohongshu.com
- 鲁越公考 site:zhihu.com
- 鲁越公考 site:tousu.sina.com.cn
- 鲁越公考 site:douyin.com

Let me do a combined Baidu query. Hmm, site: works on Baidu.

Let me try: 百度 "鲁越公考" (site:xiaohongshu.com OR site:zhihu.com) — Baidu supports site:.

Let me just do: https://www.baidu.com/s?wd=%E9%B2%81%E8%B6%8A%E5%85%AC%E8%80%83%20site%3Axiaohongshu.com

Hmm that's one at a time. Let me instead search "鲁越公考" alone (exact) and look at all results — I did that partly, and only got the 鲁跃 ad + unrelated.

Let me try Baidu exact phrase without 怎么样:
https://www.baidu.com/s?wd=%22%E9%B2%81%E8%B6%8A%E5%85%AC%E8%80%83%22

Let me do that and read #content_left.

Actually I realize the earlier exact search "鲁越公考 怎么样" returned pages about 鲁跃/观鲁/鲁公社 — i.e., Baidu found no exact-match page for 鲁越公考 either. The 百度知道/贴吧 results were about 观鲁, not 鲁越.

Hmm wait, one result: "线上公考机构怎么选?鲁跃、观鲁、燕诺测评来揭秘" 百度贴吧, and "对比了十几家公考班,为什么蕞终选择了鲁公社?" (山东鲁公社小路), "浙江考公考编笔试班怎么选" (zjsxgk), "2026年山东公考培训机构实力测评及报考避坑指南 - 商业信息 菏泽广电网".

These are ALL 软文 (SEO/marketing). None mention 鲁越.

So: 鲁越公考 appears to have very low web visibility. This itself is a finding.

But wait — maybe I'm wrong about the name. Let me double check by searching 抖音. Actually, let me search 微博: https://s.weibo.com/weibo?q=鲁越公考 — 微博 search may work without login for the first page.

Let me try 微博.

Also let me try 贴吧 search: http://tieba.baidu.com/f/search/res?qw=鲁越公考

Let me do 贴吧 (no login).

Let me do both.

Actually — I want to reconsider: is it possible the user means "鲁越公考" which is actually a known 抖音公考网红's brand? E.g., "鲁越" might be a person (老师). Hmm.

Let me search 抖音 web for 鲁越公考.

Let me try: https://www.douyin.com/search/%E9%B2%81%E8%B6%8A%E5%85%AC%E8%80%83

抖音 web usually requires login for search now.

OK, let me be pragmatic and run: 
1. 贴吧 search
2. 微博 search

Then summarize and ask user to log into 小红书 + confirm entity.

Let me do 贴吧 first.

Actually, let me combine into fewer calls to save context. Let me do 微博 search which is more likely to have 公考机构 chatter.

Hmm, 微博 s.weibo.com requires login for search results usually (it redirects to passport). Let me test quickly.

Let me instead use 百度 site: search for the platforms in ONE query:
`鲁越公考 site:xiaohongshu.com OR site:zhihu.com OR site:tousu.sina.com.cn`

Baidu may not handle OR well. Let me try just: 鲁越公考 site:xiaohongshu.com

Let me run that.

Actually, better: let me check 爱企查 for "鲁越" 教育/公考 companies — that pins the legal entity, then I can check 法院/风险. This is high value for "是否有被投诉记录".

Let me do 爱企查: https://aiqicha.baidu.com/s?q=鲁越公考

Let me do that. Actually 爱企查 search URL: https://aiqicha.baidu.com/s?q=%E9%B2%81%E8%B6%8A%E5%85%AC%E8%80%83&t=0

Let me try.

Hmm, 爱企查 also may need login.

Let me try 天眼查 search? Also login.

Hmm. Let me try the 国家企业信用信息公示系统? Heavy captcha.

OK. Let me do a Baidu site: query for xiaohongshu and zhihu, which is cheap.

Let me do two things in one browser session sequentially? The tool call is one navigation. Let me just do the site:xiaohongshu one.

Actually let me do a smarter single query on Baidu: `鲁越公考 小红书` — Baidu will return 小红书 pages if indexed.

Let me do that.

Wait, I already have limited signal. Let me consider asking the user now — but I'd rather have a bit more.

Let me try 贴吧 search since it's login-free and 公考贴吧 is active.

tieba search URL: https://tieba.baidu.com/f/search/res?ie=utf-8&qw=鲁越公考

Let me do it.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot = process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href);\nawait setupBrowserRuntime({ globals: globalThis …[截断,原长411]` → `1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 发贴 登录 首页 我的 大家都在逛的吧 抗压背锅 吧 三角洲行动陪玩 吧 孙笑川 吧 bilibili 吧 lol陪玩 吧 第五人格交易 吧 尐家军 吧 三角洲行动 吧 原神内容讨论 吧 绝区零内鬼 吧 崩坏星穹铁道内鬼 吧 cs赛事 吧 虎牙直播 吧 艾欧尼亚 吧 奥比交易 吧 2ch 吧 ns 吧 明日方舟 吧 网球风云 吧 kpl 吧 鸣潮爆料 吧 王者荣耀 吧 有男不玩ml 吧 无畏契约陪玩 吧 碧蓝航线 吧 综合 贴 吧 人 相关吧 查看更多 公考吧 关注 19.2W 粉笔公考吧 关注 7.9W 公考资料吧 关注 9468 公考干货吧 关注 2.9W  …[截断,原长1141]`

### 🤖 助手（deepseek-v4-flash，2026-09-11 01:47）

360 的 AI 结果给出关键线索：「**临沂市兰山区鲁越教育培训学校**」（山东临沂）。同时该列出的一堆山东公考品牌（鲁跃/博越/齐麟/观鲁/鲁信）说明这是个软文极密集的赛道。继续查贴吧：

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

贴吧搜索 "鲁越公考" returned no results (no 贴 posts). It just showed the generic 贴吧 sidebar. "已加载全部" — so 0 results.

So 贴吧 has no mention of 鲁越公考.

Now let me confirm: the entity might be under a different name. Let me check the 临沂 鲁越教育培训学校 and also search 抖音.

Hmm. Let me step back and reconsider the strategy. I've checked:
- Bing: nothing
- Baidu: nothing direct (only 鲁跃 ad + unrelated)
- Bilibili: nothing
- 小红书: login wall
- 贴吧: nothing
- 360: found 临沂市兰山区鲁越教育培训学校 (as AI answer)
- 搜狗: captcha

Let me now:
1. Check 抖音 web search for 鲁越公考 (公考机构主战场)
2. Check 黑猫投诉 (user asked)
3. Check 知乎

And then ask the user to log in to 小红书.

Actually, maybe I should ask the user a clarifying question now, because there's genuine ambiguity: 鲁越公考 vs 鲁跃公考 vs 鲁越教育(临沂). This affects the entire research. But the user might not know more than the name.

Hmm, the AGENTS.md says "Minimize interruptions. For an underspecified but safe request, try the best evidence-backed path before asking."

Let me try 抖音 and 黑猫 first, then decide.

Let me try 抖音: https://www.douyin.com/search/%E9%B2%81%E8%B6%8A%E5%85%AC%E8%80%83

Let me test.

Actually — thinking about it more: The heavy presence of "鲁跃公考" as a paid ad for the exact query "鲁越公考" on Baidu is itself notable: 鲁跃公考 buys the "鲁越公考" keyword. That suggests either (a) 鲁越公考 is a competitor, or (b) 鲁越公考 is a common misspelling/alias of 鲁跃公考.

Given Baidu autosuggest "鲁越公考 和 鲁跃公考 区别", it's likely a competitor relation.

Let me look at 鲁跃's website to understand, and check if it mentions 鲁越. Also let me get 鲁跃's company (备案 = 山东鲁跃教育?).

But user asked about 鲁越, not 鲁跃. Hmm.

Let me try 抖音 search. If 抖音 shows 鲁越公考 account, we're set.

Let me do it.

Let me also consider 微信 search: 搜狗微信 (weixin.sogou.com) — captcha'd probably.

Let me do 抖音.

</details>

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot = process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href);\nawait setupBrowserRuntime({ globals: globalThis …[截断,原长411]` → `开启读屏标签 读屏标签已关闭 搜索 充钻石 通知 消息 投稿 登录 综合 视频 用户 直播 登录后即可搜索更多精彩视频 扫码登录 如何扫码 打开「抖音APP」点击左上角 扫一扫 验证码登录 密码登录 获取验证码 登录 登录即代表同意用户协议和隐私政策 Structured content: `

### 🤖 助手（deepseek-v4-flash，2026-09-11 01:47）

贴吧 0 结果。查抖音（公考机构主战场）：

<details><summary>💭 思考链（deepseek-v4-flash）</summary>

抖音 also requires login.

OK. Both 小红书 and 抖音 require login. And 黑猫投诉 requires login.

Current status: no-login sources (Bing, Baidu, 360, Bilibili, 贴吧, 知乎?) show essentially NO content about "鲁越公考".

I should:
1. Try 知乎 (may work).
2. Try 微博 (may work).
3. Ask user to log into 小红书/抖音/黑猫 for the platforms that need it.

Actually — I have an important idea. Let me check whether the entity is real at all via 爱企查/企查查. And let me directly look at the 鲁跃公考 site to see if 鲁越 is mentioned (they might be the same company with a rebrand, which is common: 鲁跃 rebranded from 鲁越?).

Actually! That's a strong hypothesis: 鲁越 → 鲁跃 rename. Brands sometimes change one character. Or "鲁越" is the misspelling.

Let me check luyue100.com and look for 鲁越 mentions / company name / 备案.

Let me fetch luyue100.com via WebFetch (might work) or browser.

Let me use browser and read the page + look at 关于我们/备案号.

Actually WebFetch on a simple corporate site should be fine and cheaper. Let me use WebFetch for luyue100.com asking about company name, 备案, 鲁越 mentions.

But careful — the user asked about 鲁越公考, and I shouldn't over-invest in 鲁跃. Still, establishing the relation is key.

Let me do WebFetch on luyue100.com.

Hmm, but WebFetch may fail. Let me just use the browser (already have it). Actually WebFetch is cheaper. Let me try WebFetch in parallel with a 知乎 check? They're different tools, can run in parallel.

Let me do:
- WebFetch luyue100.com — get company name, whether 鲁越 mentioned
- Browser: 知乎 search

These are independent. Let me issue both in one block.

Actually the browser call and WebFetch are independent — yes, parallel.

Let me write the 知乎 navigation call.

知乎 search URL: https://www.zhihu.com/search?type=content&q=%E9%B2%81%E8%B6%8A%E5%85%AC%E8%80%83

Let me do both.

</details>

- 🔧 **WebFetch** `{"url": "https://www.luyue100.com/", "prompt": "这个网站是哪家机构？公司全称是什么？ICP备案主体是哪家公司？网站里是否出现过「鲁越」两个字？是否提到曾用名、改名、或其他品牌名（如鲁跃、观鲁、鲁公社）？请摘录页脚备案信息和关于我们内容。"}` → ``

- 🔧 **mcp__node_repl__js** `{"code": "const browserPluginRoot = process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;\nconst { join } = await import(\"node:path\");\nconst { pathToFileURL } = await import(\"node:url\");\nconst { setupBrowserRuntime } = await import(pathToFileURL(join(browserPluginRoot, \"scripts\", \"browser-client.mjs\")).href);\nawait setupBrowserRuntime({ globals: globalThis …[截断,原长411]` → ``

### 🤖 助手（deepseek-v4-flash，2026-09-11 01:48）

抖音、小红书、黑猫三处都要登录。先并行核实「鲁跃」是否与「鲁越」同源，同时试知乎：
