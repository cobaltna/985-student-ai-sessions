# 子代理会话 sess_subagent_agent_4f14195b-af8b-4a0c-96f8-ad220bd6dcb8

模型: ?

## 👤 用户（2026-09-11 13:47）

今天是 2026-09-11。任务：用 WebSearch / WebFetch 联网检索，找出**985 高校**中「2026 年秋季预推免（面向 2027 年入学研究生）」报名/申请**尚未截止**（截止日期 >= 2026-09-11，或通知写明"正在报名""持续接收"）的学校，重点是 C9 + 华五 + 中坚九校等：清华、北大、复旦、上海交大、浙大、中科大、南大、西安交大、哈工大、同济、东南、北航、北理、天大、南开、武大、华科、中大、华南理工、川大、电子科大、重庆大学、湖南大学、中南、大连理工、东北大学、吉大、兰大、西北工大、西北农林、中国农大、北师大、中央民大、中国海洋、山大、厦门大学、华东师大、国防科大。

检索建议关键词（多试几组，中文为主）：
- "2026年预推免"、"2026 预推免 通知"、"2027级推免生 预报名"、"接收推免生 预报名 2026"、"推免生 申请 截止 2026年9月"
- 具体学校名 + "预推免" / "推免生接收" / "夏令营/预推免 报名系统"
- site: 各校研究生院 (yz.xxx.edu.cn / graduate.xxx.edu.cn)、各院系官网
- 也可搜索保研论坛 eeban.com、研招网、知乎/微信公众号聚合文章

要求：
1. 必须返回**可核验的原始证据**：学校、院系/研究生院、通知标题、发布日期、报名截止日期、原文 URL。不要只给结论。
2. 明确区分：① 截止日期在 2026-09-11 之后（仍未截止）；② 截止日期早于 2026-09-11（已截止，剔除）；③ 日期不明/表述模糊（单独列出并注明不确定）。
3. 凡是你没能在网页原文中看到明确日期的，标注"未核实"，**绝对不要编造截止日期或链接**。
4. 最终用 Markdown 表格汇总：学校 | 层次(985) | 通知/院系 | 报名截止 | 原文URL | 证据强度。
5. 如果搜索工具受限或结果大量是往年信息，请如实说明，并列出你实际拿到的原始链接。

请尽量多轮搜索（至少 10 次不同关键词），覆盖面优先于深度。

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

The user wants me to search the web for 2026 fall 预推免 (pre-recommendation admission) announcements for 985 universities for 2027 enrollment, and find which ones have deadlines >= 2026-09-11.

I have WebFetch but no WebSearch tool listed. Let me check available tools... I have WebFetch. No WebSearch tool in the function list. Hmm. The task says "用 WebSearch / WebFetch 联网检索". There's no WebSearch tool available. But maybe I can use WebFetch on search engine URLs like Bing.

Let me try WebFetch with search URLs. Note WebFetch converts page to markdown and answers a prompt with a small model. Search engines may block or return JS-heavy content. Let me try Bing search.

Actually, there's a caveat: "Fails on authenticated/private URLs". Search engines might work.

Let me try multiple Bing searches. Also the node_repl browser use skill — but that's main-agent-only and I'm a subagent, so I must not use it.

Let me try WebFetch on bing.com/search?q=... Let's do it.

Actually, given today's date is 2026-09-11 per the context, and the model's knowledge is older — I need real web access. Let me try.

Let me start with several parallel WebFetch calls.

Note that WebFetch cross-host redirects are returned rather than followed. Bing might redirect. Let's try.

I'll try:
- https://www.bing.com/search?q=2026年预推免+报名截止
- https://cn.bing.com/search?q=...
- https://www.baidu.com/s?wd=...
- https://duckduckgo.com/html/?q=...

Let me do a bunch in parallel.

</details>

- 🔧 **WebFetch** `{"url": "https://www.bing.com/search?q=2026%E5%B9%B4%E9%A2%84%E6%8E%A8%E5%85%8D%20%E6%8A%A5%E5%90%8D%E6%88%AA%E6%AD%A2%202027%E7%BA%A7", "prompt": "List all search results: titles, URLs, and snippets. Focus on 2026 预推免 / 推免生接收 notices with dates."}` → `REDIRECT DETECTED: The URL redirects to a different host. Original URL: https://www.bing.com/search?q=2026%E5%B9%B4%E9%A2%84%E6%8E%A8%E5%85%8D%20%E6%8A%A5%E5%90%8D%E6%88%AA%E6%AD%A2%202027%E7%BA%A7 Redirect URL: https://cn.bing.com/search?q=2026%E5%B9%B4%E9%A2%84%E6%8E%A8%E5%85%8D%20%E6%8A%A5%E5%90%8D%E6%88%AA%E6%AD%A2 …[截断,原长723]`

- 🔧 **WebFetch** `{"url": "https://duckduckgo.com/html/?q=2026%E5%B9%B4%E9%A2%84%E6%8E%A8%E5%85%8D+%E9%80%9A%E7%9F%A5+%E6%88%AA%E6%AD%A2", "prompt": "List all search results: titles, URLs, and snippets about 2026 预推免 notices."}` → ``

- 🔧 **WebFetch** `{"url": "https://www.baidu.com/s?wd=2026%E5%B9%B4%E9%A2%84%E6%8E%A8%E5%85%8D%20%E6%8A%A5%E5%90%8D", "prompt": "List all search results: titles, URLs, and snippets about 2026 预推免."}` → `The provided page contains no search results or content about 2026 预推免, so there are no titles, URLs, or snippets to list.`

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-11 13:47）

I'll start by testing which search endpoints are reachable via WebFetch.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Let me try cn.bing.com. Also try other search engines.

</details>

- 🔧 **WebFetch** `{"prompt": "List all search results: titles, URLs, and snippets. Focus on 2026 预推免 / 推免生接收 notices with dates.", "url": "https://cn.bing.com/search?q=2026%E5%B9%B4%E9%A2%84%E6%8E%A8%E5%85%8D%20%E6%8A%A5%E5%90%8D%E6%88%AA%E6%AD%A2%202027%E7%BA%A7"}` → `结论：以上内容中没有出现“2026年预推免”或“推免生接收”的通知及报名截止日期；可见结果主要与日历、节假日、政府报告、亚运会等相关。搜索页显示“约 2,610,000 个结果”，并提示部分结果未予显示。 可见自然结果如下（摘要为转述）： 1. “2026年日历全年完整图_带农历节假日放假安排_高清可打印 ...” URL: https://rili.zzhuangli.com/year/2026 摘要：全年日历，含农历、节气、传统节日、周数、调休，支持主题、下载和A4打印。 2. “第20届亚运会_体育_央视网 (cctv.com)” URL: https://yayun.cctv.com/2026/index.shtml 摘要： …[截断,原长1432]`

- 🔧 **WebFetch** `{"prompt": "List all search results: titles, URLs, and snippets mentioning 预推免 2026.", "url": "https://search.marcia.workers.dev/search?q=%E9%A2%84%E6%8E%A8%E5%85%8D"}` → ``

- 🔧 **WebFetch** `{"prompt": "List all search results with titles, URLs, snippets.", "url": "https://html.duckduckgo.com/html/?q=2026%E5%B9%B4%E9%A2%84%E6%8E%A8%E5%85%8D%E9%80%9A%E7%9F%A5"}` → ``

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Bing works but the search results are polluted. Let me refine the query. Bing's search seems to work with cn.bing.com. Let me try more specific queries with quotes and site restrictions.

Also, the query with "预推免" got interpreted weirdly. Let me use more exact phrases and maybe add "研究生院".

Let's try several bing searches.

</details>

- 🔧 **WebFetch** `{"prompt": "列出所有搜索结果的标题、URL和摘要。重点找2026年预推免、推免生接收的通知和截止日期。", "url": "https://cn.bing.com/search?q=%222026%E5%B9%B4%E9%A2%84%E6%8E%A8%E5%85%8D%22"}` → `以下为页面中列出的全部搜索结果（标题、URL、摘要均来自该页；未发现与“2026年预推免”“推免生接收通知/截止日期”匹配的结果）： 1. **标题**：“2026年日历全年完整图_带农历节假日放假安排_高清可打印 ...” **URL**：https://rili.zzhuangli.com/year/2026 **摘要**：“2026年日历全年完整图，带农历、二十四节气、传统节日、周数和放假调休安排，支持30套主题、图片下载及A4年历打印。” 2. **标题**：“第20届亚运会_体育_央视网 (cctv.com)” **URL**：https://yayun.cctv.com/2026/index.shtml **摘要**：“ …[截断,原长1852]`

- 🔧 **WebFetch** `{"prompt": "列出所有搜索结果的标题、URL和摘要。重点找2026年接收推荐免试研究生预报名的通知和截止日期。", "url": "https://cn.bing.com/search?q=%E6%8E%A8%E5%85%8D%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D+2026+%E6%88%AA%E6%AD%A2%E6%97%A5%E6%9C%9F"}` → `页面当前展示的搜索结果均与“推免生预报名 2026 截止日期”无关；没有出现接收推荐免试研究生预报名的通知或截止日期。 1. 标题：“推（汉语文字）_百度百科” URL：https://baike.baidu.com/item/%E6%8E%A8/8047564 摘要：介绍“推”的字义，包括物理推动和抽象引申，如礼让、选拔、探究等。 2. 标题：“推特网页版入口:x.com 登录与下载(原Twitter) · 读懂马斯克” URL：https://www.readmusk.com/x 摘要：称推特网页版入口为 x.com，旧域名会自动跳转，手机端为 X App，并汇总相关官方内容。 3. 标题：“推 tuī - 汉典” URL：ht …[截断,原长1136]`

- 🔧 **WebFetch** `{"prompt": "列出所有搜索结果的标题、URL和摘要。重点找2026年9月预推免报名截止的相关通知。", "url": "https://cn.bing.com/search?q=%E9%A2%84%E6%8E%A8%E5%85%8D+%E6%88%AA%E6%AD%A2+2026%E5%B9%B49%E6%9C%88"}` → `根据页面，约 91,300 个结果；本页显示 9 条。页面另注明“部分搜索结果未予显示”。直接相关的只有第 4 条知乎文章，但其摘要未列出 2026 年 9 月预推免报名截止的具体日期或通知。 | # | 标题 | URL | 摘要概述 | |---|---|---|---| | 1 | “预_百度百科” | https://baike.baidu.com/item/%E9%A2%84/4942379 | 解释“预”的形容词、动词义及通假关系，并提到《康熙字典》。 | | 2 | “预的意思,预的解释,预的拼音,预的部首,预的笔顺-汉语国学” | https://www.hanyuguoxue.com/zidian/zi-39044 …[截断,原长981]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-11 13:47）

Bing (cn.bing.com) is reachable. Let me run targeted queries.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

cn.bing.com is returning very generic results, seemingly not finding specific Chinese university pages. It seems Bing is serving degraded results. Interesting: the third query returned a zhihu article about 2026 预推免/九推/十推 published 2025-09-14. That suggests the current "real" date is around Sept 2025? Wait, the article was published 2025-09-14 and the context says today is 2026-09-11. Hmm, the article title mentions 2026年预推免 and published 2025-09-14 — that's consistent: in Sept 2025, students prepare for the 2026 enrollment 预推免 (i.e., 保研 for entering in Sept 2026).

Wait — important! The user's task says "2026 年秋季预推免（面向 2027 年入学研究生）". Hmm, actually the naming convention: 预推免 in Fall 2026 is for students entering in 2027 (2027级). So the notices would be published Aug-Sep 2026. Today is 2026-09-11.

Hmm, but the zhihu article "一文讲清楚2026年预推免、九推、十推流程" published 2025-09-14 would be about the 2026 enrollment cycle. Confusing. Actually that article might have been updated/published date misread.

Anyway. The key issue: cn.bing.com gives poor results. Let me try different approaches:
1. Try Bing with site: operators.
2. Try fetching university graduate school websites directly.
3. Try so.com (360), sogou.

Let me test sogou and 360 search.

Also try Bing's exact search on known URL patterns.

Let me try:
- https://www.sogou.com/web?query=...
- https://www.so.com/s?q=...
- https://cn.bing.com/search?q=site%3Ayz.tsinghua.edu.cn+预推免

Let's test connectivity of multiple.

</details>

- 🔧 **WebFetch** `{"prompt": "列出所有搜索结果的标题、URL和摘要。", "url": "https://www.sogou.com/web?query=2026%E5%B9%B4%E9%A2%84%E6%8E%A8%E5%85%8D%E9%80%9A%E7%9F%A5"}` → `REDIRECT DETECTED: The URL redirects to a different host. Original URL: https://www.sogou.com/web?query=2026%E5%B9%B4%E9%A2%84%E6%8E%A8%E5%85%8D%E9%80%9A%E7%9F%A5 Redirect URL: http://www.sogou.com/antispider/?m=1&antip=web_hd&from=%2Fweb%3Fquery%3D2026%25E5%25B9%25B4%25E9%25A2%2584%25E6%258E%25A8%25E5%2585%258D%25E9%2 …[截断,原长779]`

- 🔧 **WebFetch** `{"prompt": "列出所有搜索结果的标题、URL和摘要，重点是与预推免相关的。", "url": "https://www.so.com/s?q=2026%E5%B9%B4%E9%A2%84%E6%8E%A8%E5%85%8D%E9%80%9A%E7%9F%A5"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "列出所有搜索结果的标题、URL和摘要。", "url": "https://cn.bing.com/search?q=site%3Ayz.tsinghua.edu.cn+%E6%8E%A8%E5%85%8D"}` → `WebFetch completed, but the extraction model returned no text.`

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-11 13:48）

Bing results are poor quality. Let me test other search engines and site-restricted queries.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Search engines are largely blocked or degraded. The Bing site: query returned nothing extracted.

Let me think about what's actually happening. The environment claims today is 2026-09-11, but this is a simulated/future date. The web content available is real-world current content. The actual real-world date might be... let me check by fetching a page that displays current date. The zhihu article from "2025-09-14" and gov.cn content about 2026 holidays published 2025-11-04 suggests the real current date is later than 2025-11. Actually gov.cn 2026 holiday notice published 2025-11-04 means real date > 2025-11-04. Hmm, but that would be the actual current date in reality. Let me check a news page for today's date.

Actually, the key question: can I find 2026 预推免 notices? If real date is e.g. 2026-09, then yes such notices exist. Let me check what the real date is by fetching something with a live date, e.g., a news homepage.

Let me try fetching baidu news or a page. Actually the bing results showed "5 天之前" for 2026 公平竞争政策宣传周 — that event is in September, and "5 days ago" suggests current date ~ mid-September. Also "2026年4月18日" for toolight calendar. Hmm.

The gov.cn 2026 holiday notice dated 2025-11-04. And the samr 2026 公平竞争宣传周 "5天之前". The 公平竞争政策宣传周 is typically held in September. So real current date is likely around September 2026! That matches the task date 2026-09-11.

OK so the real world (in this environment's index) is ~Sept 2026. So 2026 预推免 notices for 2027 enrollment should exist.

Wait, but the zhihu article "一文讲清楚2026年预推免、九推、十推流程" published 2025-09-14 — that would be about 2026 入学 cycle, published in 2025. Hmm, that's plausible if the naming is by enrollment year: "2026年预推免" = 预推免 for 2026 entry, held Sept 2025. Then for 2027 entry held Sept 2026, it'd be called "2026年预推免" too (the event year). Confusing naming. Actually common usage: 预推免 held in Sept 2026 for 2027 entry is often called "2026年预推免" by the event date, or "2027级推免". The task explicitly says "2026 年秋季预推免（面向 2027 年入学研究生）", i.e., held autumn 2026.

So I need notices from Aug-Sep 2026.

Let me try harder. Bing seems to only return generic results for these queries — possibly Bing is not indexing or the extraction model is failing. Let me try Bing with more specific queries and see.

Actually the issue may be that cn.bing.com returns a page whose results are heavily "calendar" spam because Bing's Chinese index is poor. Let me try a completely different query format, e.g., use quotes around "接收推荐免试研究生" or search for specific school + 预推免.

Let me try:
- https://cn.bing.com/search?q=%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6+2026+%E9%A2%84%E6%8E%A8%E5%85%8D
- https://cn.bing.com/search?q=%E5%A4%8D%E6%97%A6%E5%A4%A7%E5%AD%A6+%E6%8E%A8%E5%85%8D%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D
- also try Bing with &setmkt=zh-CN and &ensearch=0

Maybe the problem is Bing serving a "no results" fallback. Let me also try Yandex? Probably blocked.

Let me try the Bing news search or use a different Bing endpoint like https://cn.bing.com/search?q=...&format=rss — RSS might give cleaner results! Bing supports RSS output: append &format=rss. Let me try that.

Also try Google via a proxy? Google is likely blocked (timeouts). Let's test google.com/search.

Let me try Bing RSS.

</details>

- 🔧 **WebFetch** `{"prompt": "List the RSS items: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E9%A2%84%E6%8E%A8%E5%85%8D+2026+%E6%88%AA%E6%AD%A2&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List the RSS items: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D&format=rss"}` → `1. Title: “全国推荐免试攻读研究生（免初试、转段）” Link: https://yz.chsi.com.cn/tm/index Description: Describes the national unified recommendation-exemption service system, covering qualification review, application, admission, and public filing; notes candidates may fill multiple parallel choices from Sept. 22 to Oct. 20, 2025. pubDate …[截断,原长3208]`

- 🔧 **WebFetch** `{"prompt": "List the RSS items: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%22%E9%A2%84%E6%8E%A8%E5%85%8D%22+site%3Aedu.cn&format=rss"}` → `1. Title: "全国推荐免试攻读研究生（免初试、转段）信息公开管理 ..." Link: https://yz.chsi.com.cn/tm/ Description: Describes a unified national platform for recommendation-exempt graduate admissions, covering qualification review, registration, admission, and public records. PubDate: 周四, 10 9月 2026 23:20:00 GMT 2. Title: "一文讲清楚2026年预推免、九推、十推流程 - …[截断,原长1076]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-11 13:48）

Let me try Bing's RSS output and direct school-site queries.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Excellent! Bing RSS output works great. Real current date confirmed: pubDates show 周四, 10 9月 2026 and 周五, 11 9月 2026. So today is indeed around 2026-09-11. 

Now I can search effectively. Let me use Bing RSS with many queries.

Key findings so far:
- 江南大学 (not 985, 211) 2027 预推免: system open Sept 1–17, 2026
- 东北大学 (985) 2027 接收推免工作办法: yz.neu.edu.cn/2026/0720/... no explicit deadline yet
- 山东大学 (985): 2027 预报名 www.yz.sdu.edu.cn/info/1022/1463.htm
- 南京大学 (985): 2027 预报名通知 https://yzb.nju.edu.cn/d4/57/c47868a840791/page.htm published Aug 3 2026
- 同济大学 (985): 各学院2027 预报名汇总 https://yz.tongji.edu.cn/info/1010/4220.htm
- 华南理工 (985): https://yz.scut.edu.cn/2026/0828/c30108a633884/page.htm published Aug 28, 2026
- 中山大学 (985): https://graduate.sysu.edu.cn/zsw/article/538
- 南京航空航天大学 (211)
- 北京协和医学院: Aug 10-23 2026 (already closed)

Now I need to fetch each notice to get the deadline. Let me do a comprehensive series of searches and then fetch pages.

Let me plan searches (need at least 10 different keywords):
1. 清华大学 2027 推免 预报名
2. 北京大学 2027 接收推免生
3. 复旦大学 2027 预推免
4. 上海交通大学 2027 推免生
5. 浙江大学 2027 预推免
6. 中国科学技术大学 2027 推免
7. 西安交通大学 2027 预推免
8. 哈尔滨工业大学 2027 推免
9. 北京航空航天大学 2027 预推免
10. 北京理工大学 2027 推免
11. 天津大学 2027 推免
12. 南开大学 2027 预推免
13. 武汉大学 2027 推免
14. 华中科技大学 2027 推免
15. 四川大学 2027 推免
16. 电子科技大学 2027 推免
17. 重庆大学 2027 推免
18. 湖南大学 2027 推免
19. 中南大学 2027 推免
20. 大连理工 2027 推免
21. 吉林大学 2027 推免
22. 兰州大学 2027 推免
23. 西北工业大学 2027 推免
24. 西北农林 2027 推免
25. 某985高校 2027 推免
26. 北京师范大学 2027 推免
27. 中央民族大学 2027 推免
28. 中国海洋大学 2027 推免
29. 厦门大学 2027 推免
30. 华东师范大学 2027 推免
31. 国防科技大学 2027 推免
32. 东南大学 2027 推免
33. 中国科学技术大学

That's a lot. Let me batch several RSS queries per call round, maybe 3-4 at a time to be safe.

Let me do batches of 4.

Batch 1: 清华, 北大, 复旦, 上交
Batch 2: 浙大, 中科大, 西安交大, 哈工大
Batch 3: 北航, 北理, 天大, 南开
Batch 4: 武大, 华科, 川大, 电子科大
Batch 5: 重庆大学, 湖南大学, 中南, 大连理工
Batch 6: 吉大, 兰大, 西北工大, 西北农林
Batch 7: 中国农大, 北师大, 中央民大, 中国海洋
Batch 8: 山大, 厦大, 华东师大, 国防科大
Plus 东南 already need.

Also queries for general aggregators: 保研通知网, eeban.

Let me go. I'll use Bing RSS with query = 学校名 + 2027 + 预推免 / 接收推免.

Let me be careful with URL encoding. I'll just put Chinese directly? The tool takes URL string; better URL-encode. Actually the previous calls I used %-encoding. Let me write a helper mentally. Simpler: I can include Chinese characters directly in the URL and the fetch may handle. Let me test with one direct Chinese query to save effort. Actually risky. Let me just use encodeURIComponent-style encoding.

Let me write out encodings for common terms:
- 清华大学 = %E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6
- 北京大学 = %E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6
- 复旦大学 = %E5%A4%8D%E6%97%A6%E5%A4%A7%E5%AD%A6
- 上海交通大学 = %E4%B8%8A%E6%B5%B7%E4%BA%A4%E9%80%9A%E5%A4%A7%E5%AD%A6
- 浙江大学 = %E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6
- 中国科学技术大学 = %E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E6%8A%80%E6%9C%AF%E5%A4%A7%E5%AD%A6
- 西安交通大学 = %E8%A5%BF%E5%AE%89%E4%BA%A4%E9%80%9A%E5%A4%A7%E5%AD%A6
- 哈尔滨工业大学 = %E5%93%88%E5%B0%94%E6%BB%A8%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6
- 北京航空航天大学 = %E5%8C%97%E4%BA%AC%E8%88%AA%E7%A9%BA%E8%88%AA%E5%A4%A9%E5%A4%A7%E5%AD%A6
- 北京理工大学 = %E5%8C%97%E4%BA%AC%E7%90%86%E5%B7%A5%E5%A4%A7%E5%AD%A6
- 天津大学 = %E5%A4%A9%E6%B4%A5%E5%A4%A7%E5%AD%A6
- 南开大学 = %E5%8D%97%E5%BC%80%E5%A4%A7%E5%AD%A6
- 武汉大学 = %E6%AD%A6%E6%B1%89%E5%A4%A7%E5%AD%A6
- 华中科技大学 = %E5%8D%8E%E4%B8%AD%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6
- 四川大学 = %E5%9B%9B%E5%B7%9D%E5%A4%A7%E5%AD%A6
- 电子科技大学 = %E7%94%B5%E5%AD%90%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6
- 重庆大学 = %E9%87%8D%E5%BA%86%E5%A4%A7%E5%AD%A6
- 湖南大学 = %E6%B9%96%E5%8D%97%E5%A4%A7%E5%AD%A6
- 中南大学 = %E4%B8%AD%E5%8D%97%E5%A4%A7%E5%AD%A6
- 大连理工大学 = %E5%A4%A7%E8%BF%9E%E7%90%86%E5%B7%A5%E5%A4%A7%E5%AD%A6
- 吉林大学 = %E5%90%89%E6%9E%97%E5%A4%A7%E5%AD%A6
- 兰州大学 = %E5%85%B0%E5%B7%9E%E5%A4%A7%E5%AD%A6
- 西北工业大学 = %E8%A5%BF%E5%8C%97%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6
- 西北农林科技大学 = %E8%A5%BF%E5%8C%97%E5%86%9C%E6%9E%97%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6
- 某985高校 = %E4%B8%AD%E5%9B%BD%E5%86%9C%E4%B8%9A%E5%A4%A7%E5%AD%A6
- 北京师范大学 = %E5%8C%97%E4%BA%AC%E5%B8%88%E8%8C%83%E5%A4%A7%E5%AD%A6
- 中央民族大学 = %E4%B8%AD%E5%A4%AE%E6%B0%91%E6%97%8F%E5%A4%A7%E5%AD%A6
- 中国海洋大学 = %E4%B8%AD%E5%9B%BD%E6%B5%B7%E6%B4%8B%E5%A4%A7%E5%AD%A6
- 厦门大学 = %E5%8E%A6%E9%97%A8%E5%A4%A7%E5%AD%A6
- 华东师范大学 = %E5%8D%8E%E4%B8%9C%E5%B8%88%E8%8C%83%E5%A4%A7%E5%AD%A6
- 国防科技大学 = %E5%9B%BD%E9%98%B2%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6
- 东南大学 = %E4%B8%9C%E5%8D%97%E5%A4%A7%E5%AD%A6
- 山东大学 = %E5%B1%B1%E4%B8%9C%E5%A4%A7%E5%AD%A6
- 2027 = 2027
- 预推免 = %E9%A2%84%E6%8E%A8%E5%85%8D
- 接收推免 = %E6%8E%A5%E6%94%B6%E6%8E%A8%E5%85%8D
- 推免生 = %E6%8E%A8%E5%85%8D%E7%94%9F

This is very laborious. Alternative: maybe WebFetch handles raw Chinese in URL. Let me test one quickly. I'll do batch with raw Chinese.

Let me test one raw Chinese query alongside two encoded.

Actually, I can just try it — worst case it fails.

Let me do batch 1 with raw Chinese.

</details>

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=清华大学+2027年+预推免+接收推荐免试&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=北京大学+2027年+推免生+预报名&format=rss"}` → `以下为全部 RSS 条目；描述为简述，非逐字引用。 1. **标题**："北京市_百度百科" **链接**：https://baike.baidu.com/item/%e5%8c%97%e4%ba%ac%e5%b8%82/126069 **描述**：人口在2025年底约2180万；位于华北平原北端，与天津、河北接壤，坐标约东经116°20′、北纬39°56′；西北高东南低，三面环山，东南部平原向渤海缓倾。 **pubDate**：周四, 10 9月 2026 23:35:00 GMT 2. **标题**："Beijing - 北京市人民政府门户网站" **链接**：https://www.beijing.gov.cn/ **描述** …[截断,原长906]`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=复旦大学+2027年+预推免+报名&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=上海交通大学+2027年+推免生+预报名&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-11 13:48）

Bing RSS works and returns clean results. Confirmed the live date is ~2026-09-11. Let me run broad batches.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Raw Chinese in URL gives poor results (Bing probably didn't treat it as intended). The + separating might be an issue too. Earlier successful queries used %-encoded with + between. Actually the successful one was:
https://cn.bing.com/search?q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D&format=rss

So %-encoding works. Raw Chinese gave garbage. So I must %-encode.

Let me build encoded queries. This is laborious but doable. Alternatively use a simpler approach: use general queries that are already encoded, plus query with fewer terms.

Better idea: Query with %-encoded school name + 2027 + %E9%A2%84%E6%8E%A8%E5%85%8D (预推免) or %E6%8E%A8%E5%85%8D (推免).

Let me create encodings. I'll construct carefully.

School name encodings (UTF-8 percent):
清 = E6 B8 85
华 = E5 8D 8E
清华大学 = %E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6

北京大学 = 北(E5 8C 97)京(E4 BA AC)大(E5 A4 A7)学(E5 AD A6) = %E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6

复旦大学 = 复(E5 A4 8D)旦(E6 97 A6)大 学 = %E5%A4%8D%E6%97%A6%E5%A4%A7%E5%AD%A6

上海交通大学 = 上(E4 B8 8A)海(E6 B5 B7)交(E4 BA A4)通(E9 80 9A)大(E5 A4 A7)学(E5 AD A6) = %E4%B8%8A%E6%B5%B7%E4%BA%A4%E9%80%9A%E5%A4%A7%E5%AD%A6

浙江大学 = 浙(E6 B5 99)江(E6 B1 9F)大 学 = %E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6

中国科学技术大学 = 中(E4 B8 AD)国(E5 9B BD)科(E7 A7 91)学(E5 AD A6)技(E6 8A 80)术(E6 9C AF)大 学 = %E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E6%8A%80%E6%9C%AF%E5%A4%A7%E5%AD%A6

西安交通大学 = 西(E8 A5 BF)安(E5 AE 89)交通 大学 = %E8%A5%BF%E5%AE%89%E4%BA%A4%E9%80%9A%E5%A4%A7%E5%AD%A6

哈尔滨工业大学 = 哈(E5 93 88)尔(E5 B0 94)滨(E6 BB A8)工(E5 B7 A5)业(E4 B8 9A)大 学 = %E5%93%88%E5%B0%94%E6%BB%A8%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6

北京航空航天大学 = 北京 + 航(E8 88 AA)空(E7 A9 BA)航(E8 88 AA)天(E5 A4 A9)大 学 = %E5%8C%97%E4%BA%AC%E8%88%AA%E7%A9%BA%E8%88%AA%E5%A4%A9%E5%A4%A7%E5%AD%A6

北京理工大学 = 北京 + 理(E7 90 86)工(E5 B7 A5)大 学 = %E5%8C%97%E4%BA%AC%E7%90%86%E5%B7%A5%E5%A4%A7%E5%AD%A6

天津大学 = 天(E5 A4 A9)津(E6 B4 A5)大 学 = %E5%A4%A9%E6%B4%A5%E5%A4%A7%E5%AD%A6

南开大学 = 南(E5 8D 97)开(E5 BC 80)大 学 = %E5%8D%97%E5%BC%80%E5%A4%A7%E5%AD%A6

武汉大学 = 武(E6 AD A6)汉(E6 B1 89)大 学 = %E6%AD%A6%E6%B1%89%E5%A4%A7%E5%AD%A6

华中科技大学 = 华(E5 8D 8E)中(E4 B8 AD)科技 大学 = %E5%8D%8E%E4%B8%AD%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6

四川大学 = 四(E5 9B 9B)川(E5 B7 9D)大 学 = %E5%9B%9B%E5%B7%9D%E5%A4%A7%E5%AD%A6

电子科技大学 = 电(E7 94 B5)子(E5 AD 90)科技 大学 = %E7%94%B5%E5%AD%90%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6

重庆大学 = 重(E9 87 8D)庆(E5 BA 86)大 学 = %E9%87%8D%E5%BA%86%E5%A4%A7%E5%AD%A6

湖南大学 = 湖(E6 B9 96)南(E5 8D 97)大 学 = %E6%B9%96%E5%8D%97%E5%A4%A7%E5%AD%A6

中南大学 = 中(E4 B8 AD)南(E5 8D 97)大 学 = %E4%B8%AD%E5%8D%97%E5%A4%A7%E5%AD%A6

大连理工大学 = 大(E5 A4 A7)连(E8 BF 9E)理(E7 90 86)工(E5 B7 A5)大 学 = %E5%A4%A7%E8%BF%9E%E7%90%86%E5%B7%A5%E5%A4%A7%E5%AD%A6

吉林大学 = 吉(E5 90 89)林(E6 9E 97)大 学 = %E5%90%89%E6%9E%97%E5%A4%A7%E5%AD%A6

兰州大学 = 兰(E5 85 B0)州(E5 B7 9E)大 学 = %E5%85%B0%E5%B7%9E%E5%A4%A7%E5%AD%A6

西北工业大学 = 西北 + 工(E5 B7 A5)业(E4 B8 9A)大 学 = %E8%A5%BF%E5%8C%97%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6

西北农林科技大学 = 西北 + 农(E5 86 9C)林(E6 9E 97)科技 大学 = %E8%A5%BF%E5%8C%97%E5%86%9C%E6%9E%97%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6

某985高校 = 中国 + 农(E5 86 9C)业(E4 B8 9A)大 学 = %E4%B8%AD%E5%9B%BD%E5%86%9C%E4%B8%9A%E5%A4%A7%E5%AD%A6

北京师范大学 = 北京 + 师(E5 B8 88)范(E8 8C 83)大 学 = %E5%8C%97%E4%BA%AC%E5%B8%88%E8%8C%83%E5%A4%A7%E5%AD%A6

中央民族大学 = 中(E4 B8 AD)央(E5 A4 AE)民(E6 B0 91)族(E6 97 8F)大 学 = %E4%B8%AD%E5%A4%AE%E6%B0%91%E6%97%8F%E5%A4%A7%E5%AD%A6

中国海洋大学 = 中国 + 海(E6 B5 B7)洋(E6 B4 8B)大 学 = %E4%B8%AD%E5%9B%BD%E6%B5%B7%E6%B4%8B%E5%A4%A7%E5%AD%A6

厦门大学 = 厦(E5 8E A6)门(E9 97 A8)大 学 = %E5%8E%A6%E9%97%A8%E5%A4%A7%E5%AD%A6

华东师范大学 = 华(E5 8D 8E)东(E4 B8 9C)师(E5 B8 88)范(E8 8C 83)大 学 = %E5%8D%8E%E4%B8%9C%E5%B8%88%E8%8C%83%E5%A4%A7%E5%AD%A6

国防科技大学 = 国(E5 9B BD)防(E9 98 B2)科技 大学 = %E5%9B%BD%E9%98%B2%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6

东南大学 = 东(E4 B8 9C)南(E5 8D 97)大 学 = %E4%B8%9C%E5%8D%97%E5%A4%A7%E5%AD%A6

山东大学 = 山(E5 B1 B1)东(E4 B8 9C)大 学 = %E5%B1%B1%E4%B8%9C%E5%A4%A7%E5%AD%A6

Terms:
预推免 = %E9%A2%84%E6%8E%A8%E5%85%8D
推免 = %E6%8E%A8%E5%85%8D
推免生 = %E6%8E%A8%E5%85%8D%E7%94%9F
接收 = %E6%8E%A5%E6%94%B6
报名 = %E6%8A%A5%E5%90%8D
截止 = %E6%88%AA%E6%AD%A2
2027 = 2027
通知 = %E9%80%9A%E7%9F%A5

OK. Let me batch 4 queries at a time. I could reduce by using query like "SCHOOL 2027 预推免" encoding school + "2027+" + %E9%A2%84%E6%8E%A8%E5%85%8D.

Let me go with batches of 4.

Batch A: 清华, 复旦, 上交, 浙大 — note 清华 raw failed; use encoded.
Batch B: 中科大, 西安交大, 哈工大, 北航
Batch C: 北理, 天大, 南开, 武大
Batch D: 华科, 川大, 电子科大, 重庆大学
Batch E: 湖南大学, 中南, 大连理工, 吉大
Batch F: 兰大, 西北工大, 西北农林, 中国农大
Batch G: 北师大, 中央民大, 中国海洋, 厦大
Batch H: 华东师大, 国防科大, 东南, 山大

Plus 北大 (raw failed) — included? I'll add 北大 encoded in batch A or separately. Let me do batch A: 清华, 北大, 复旦, 上交. Batch B: 浙大, 中科大, 西交, 哈工大. And so on shifting.

Let me start.

Actually, note the search term "2027年" — should I encode 年? 年 = E5 B9 B4. I'll just use "2027" alone.

Let me construct URLs.

Batch A:
1. https://cn.bing.com/search?q=%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6+2027+%E9%A2%84%E6%8E%A8%E5%85%8D&format=rss
2. https://cn.bing.com/search?q=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6+2027+%E6%8E%A5%E6%94%B6%E6%8E%A8%E5%85%8D&format=rss
3. https://cn.bing.com/search?q=%E5%A4%8D%E6%97%A6%E5%A4%A7%E5%AD%A6+2027+%E9%A2%84%E6%8E%A8%E5%85%8D&format=rss
4. https://cn.bing.com/search?q=%E4%B8%8A%E6%B5%B7%E4%BA%A4%E9%80%9A%E5%A4%A7%E5%AD%A6+2027+%E9%A2%84%E6%8E%A8%E5%85%8D&format=rss

Let me go.

</details>

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6+2027+%E9%A2%84%E6%8E%A8%E5%85%8D&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6+2027+%E6%8E%A5%E6%94%B6%E6%8E%A8%E5%85%8D&format=rss"}` → `There are 10 RSS items. 1. **Title:** “北京市_百度百科” **Link:** https://baike.baidu.com/item/%e5%8c%97%e4%ba%ac%e5%b8%82/126069 **Description:** 介绍北京的人口、地理位置、地形等概况，提及2025年末常住人口数据。 **PubDate:** 周四, 10 9月 2026 23:35:00 GMT 2. **Title:** “Beijing - 北京市人民政府门户网站” **Link:** https://www.beijing.gov.cn/ **Description:** 首都之窗作为市政府网上 …[截断,原长1800]`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E5%A4%8D%E6%97%A6%E5%A4%A7%E5%AD%A6+2027+%E9%A2%84%E6%8E%A8%E5%85%8D&format=rss"}` → `Descriptions below are shortened/paraphrased to stay within the quote limit. 1. **Title:** “复旦大学招收2027级推荐免试研究生报名通知” **Link:** https://gsao.fudan.edu.cn/fb/0b/c15014a785163/page.htm **Description:** 说明有意申请者须在规定时段通过复旦研究生报考服务系统报名；各院系通常为7月6日10:00至8月10日17:00，个别有调整，临床医学院预计8月底开放。 **PubDate:** 周四, 10 9月 2026 17:22:00 GMT 2. ** …[截断,原长1348]`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E4%B8%8A%E6%B5%B7%E4%BA%A4%E9%80%9A%E5%A4%A7%E5%AD%A6+2027+%E9%A2%84%E6%8E%A8%E5%85%8D&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-11 13:49）

%-encoded queries work. Running school-by-school batches via Bing RSS.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Some queries work, some return "no text" (extraction model returned nothing). It seems intermittent — maybe the RSS returned but extraction failed, or the query returned zero results. Let me retry failed ones. Also 北大 query got polluted by "北京" — need better query e.g. include "研究生院" or "推免生" plus "北大". Actually the issue is "北京大学" tokenized as 北京+大学. Let me use "北大" or add a distinctive term.

Let me note progress:
- 复旦: 报名通知 https://gsao.fudan.edu.cn/fb/0b/c15014a785163/page.htm — 各院系通常 7月6日-8月10日, 部分延长至8月17日. So likely已截止. Need to verify.
- 上海交大: extraction failed, retry.
- 清华: retry.

Let me retry the failed three plus continue with next batch.

Strategy: to reduce failures, maybe use simpler queries. Let me retry with slightly different phrasing.

Let me now do a batch: 清华, 上交, 浙大, 中科大.

URLs:
清华: 清华大学+2027+推免 — maybe the issue is the query. Let me try "清华大学 2027 接收推免生".
清华 = %E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6
接收推免生 = %E6%8E%A5%E6%94%B6%E6%8E%A8%E5%85%8D%E7%94%9F

上交: 上海交通大学+2027+推免生 — use %E6%8E%A8%E5%85%8D%E7%94%9F
浙大: 浙江大学+2027+预推免
中科大: 中国科学技术大学+2027+预推免

Let me run.

</details>

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6+2027+%E6%8E%A5%E6%94%B6%E6%8E%A8%E5%85%8D%E7%94%9F&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E4%B8%8A%E6%B5%B7%E4%BA%A4%E9%80%9A%E5%A4%A7%E5%AD%A6+2027+%E6%8E%A8%E5%85%8D%E7%94%9F&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6+2027+%E9%A2%84%E6%8E%A8%E5%85%8D&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E6%8A%80%E6%9C%AF%E5%A4%A7%E5%AD%A6+2027+%E9%A2%84%E6%8E%A8%E5%85%8D&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

All four failed. Possibly rate limiting, or Bing RSS returning empty for these. Let me test whether Bing RSS is throttled now by re-running a query that worked before.

Actually the pattern: earlier batch of 4 had 1 success (复旦), 1 polluted (北大), 2 fail. Then all 4 fail. Might be rate limiting / caching. WebFetch caches for 15 min per URL, so repeating the same URL returns cached (should be fine). Let me spread out and try fewer per call, and vary queries.

Alternatively, the extraction model "returned no text" may mean the RSS was empty because Bing found no results for those exact queries. Hmm, but 清华 2027 接收推免生 should have results.

Let me try Bing web (non-RSS) for one query to compare. And try a different RSS query.

Let me do 2 calls: one RSS for 浙江大学 2027 推免, one plain web for 清华大学 2027 预推免.

Actually maybe the issue: Bing RSS with multiple %-encoded terms sometimes returns an error page. Let me test with a known-good query from earlier to check whether Bing is still working: the 江南大学 one. Re-fetch (cached) — that wouldn't test. Let me run a slightly different query.

Let me try a batch of 2-3.

</details>

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E6%B5%99%E5%A4%A7+2027+%E6%8E%A8%E5%85%8D%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6%E7%A0%94%E7%A9%B6%E7%94%9F%E6%8B%9B%E7%94%9F+%E6%8E%A8%E5%85%8D&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Still failing. Possibly Bing has rate-limited. Let me wait / try a different search source. Let me try:
- Bing news RSS: https://www.bing.com/news/search?q=...&format=rss
- Or use a different search engine that works, e.g., "search.marcia" timed out earlier. Let me try lite.duckduckgo.com, or startpage, or ecosia, brave.

Let me test a few search endpoints in parallel.

Options:
- https://lite.duckduckgo.com/lite/?q=...
- https://search.brave.com/search?q=...
- https://www.ecosia.org/search?q=...
- https://www.mojeek.com/search?q=...
- https://search.marginalia.nu/search?query=...
- https://www.qwant.com/?q=...

Also Chinese: https://www.chinaso.com/search/..., https://so.toutiao.com/search?keyword=...

And for Chinese academic info aggregators directly:
- 保研通知网 (baoyan...)
- eeban.com

Let me test mojeek and brave and lite ddg for the 清华 query.

Also, maybe Bing rate limit is temporary. Let me test one Bing again after a bit, in the same batch.

Let me run: mojeek, lite.ddg, brave (3-4 calls).

</details>

- 🔧 **WebFetch** `{"prompt": "List search results: title, URL, snippet.", "url": "https://lite.duckduckgo.com/lite/?q=%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6+2027+%E9%A2%84%E6%8E%A8%E5%85%8D"}` → ``

- 🔧 **WebFetch** `{"prompt": "List search results: title, URL, snippet.", "url": "https://www.mojeek.com/search?q=%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6+2027+%E9%A2%84%E6%8E%A8%E5%85%8D"}` → `The server returned HTTP 403 Forbidden. The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.`

- 🔧 **WebFetch** `{"prompt": "List search results: title, URL, snippet.", "url": "https://search.brave.com/search?q=%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6+2027+%E9%A2%84%E6%8E%A8%E5%85%8D"}` → ``

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://www.bing.com/news/search?q=%E9%A2%84%E6%8E%A8%E5%85%8D+2027&format=rss"}` → `REDIRECT DETECTED: The URL redirects to a different host. Original URL: https://www.bing.com/news/search?q=%E9%A2%84%E6%8E%A8%E5%85%8D+2027&format=rss Redirect URL: https://cn.bing.com/news/search?q=%E9%A2%84%E6%8E%A8%E5%85%8D+2027&format=rss Status: 302 Found To complete your request, I need to fetch content from the  …[截断,原长539]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-11 13:50）

Bing may be rate-limiting. Testing alternate search engines.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Let me set up a todo list and continue. Bing RSS seems intermittent. The redirect to cn.bing.com news search — let me try that. Also retry Bing web search RSS.

Let me create todos.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "Confirm working search endpoint (Bing RSS intermittent)", "status": "in_progress", "priority": "high"}, {"content": "Search all C9 + 华五 + 中坚九校 etc. for 2027 预推免 notices", "status": "pending", "priority": "high"}, {"content": "Fetch each notice page to extract exact deadline", "status": "pending", "priority": "high"}, {"content": "Compile Markdown table w …[截断,原长412]` → `{"oldTodos":[],"todos":[{"content":"Confirm working search endpoint (Bing RSS intermittent)","status":"in_progress","priority":"high"},{"content":"Search all C9 + 华五 + 中坚九校 etc. for 2027 预推免 notices","status":"pending","priority":"high"},{"content":"Fetch each notice page to extract exact deadline","status":"pending"," …[截断,原长497]`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/news/search?q=%E9%A2%84%E6%8E%A8%E5%85%8D+2027&format=rss"}` → `No RSS items are present in the provided content. It appears to contain only a Microsoft Bing search page title and footer/legal links, so there are no titles, links, descriptions, or pubDates to list.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E6%8E%A8%E5%85%8D%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D+%E9%80%9A%E7%9F%A5+2027&format=rss"}` → `1. Title: “推（汉语文字）_百度百科” Link: https://baike.baidu.com/item/%E6%8E%A8/8047564 Description: Character entry covering physical pushing and extended senses like yielding, selecting, and investigating. pubDate: 周四, 10 9月 2026 14:23:00 GMT 2. Title: “推特网页版入口:x.com 登录与下载(原Twitter) · 读懂马斯克” Link: https://www.readmusk.com/x De …[截断,原长1995]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

The query with 推免生+预报名+通知+2027 got garbage — Bing tokenized "推免生" poorly. But earlier "接收推荐免试研究生 预报名" worked great. So the key is using full phrases that Bing understands. Let me use "接收推荐免试研究生" as the anchor phrase plus school names? But adding school names may dilute.

Better: use queries like "<school> 接收推荐免试研究生" (full phrase). Let me try encoded:
接收推荐免试研究生 = %E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F
预报名 = %E9%A2%84%E6%8A%A5%E5%90%8D

Earlier successful query: "接收推荐免试研究生 预报名" gave 10 good results including many 985s. Let me leverage general queries like:
- "2027年接收推荐免试研究生" 
- "2027年预推免"
- "2027级推免生预报名"

Since the task wants coverage, general aggregator queries may be more efficient than per-school. Let me run several general queries.

Also 保研通知网 appeared in results. Let me find it.

Let me run a batch of 4 general queries:
1. q="2027年接收推荐免试研究生"&format=rss  → %222027%E5%B9%B4%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F%22
Hmm 年 = %E5%B9%B4. Actually quoting may help.
2. q="2027级推免生预报名"
3. q="2027年预推免报名"
4. q="预推免报名通知 2027"

Let me also try site queries:
- q=site%3Aedu.cn 2027 预推免

Let me batch.

Encodings:
"2027年接收推荐免试研究生" = %222027%E5%B9%B4%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F%22
"2027级推免生预报名" = 2027%E7%BA%A7(%E7%BA%A7=级)%E6%8E%A8%E5%85%8D%E7%94%9F%E9%A2%84%E6%8A%A5%E5%90%8D → %222027%E7%BA%A7%E6%8E%A8%E5%85%8D%E7%94%9F%E9%A2%84%E6%8A%A5%E5%90%8D%22
"2027年预推免" = %222027%E5%B9%B4%E9%A2%84%E6%8E%A8%E5%85%8D%22
"预推免报名通知" = %22%E9%A2%84%E6%8E%A8%E5%85%8D%E6%8A%A5%E5%90%8D%E9%80%9A%E7%9F%A5%22

Let me run.

</details>

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%222027%E5%B9%B4%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F%22&format=rss"}` → `共 9 项： 1. **标题：** “2027年_百度百科” **链接：** https://baike.baidu.com/item/2027%E5%B9%B4/7710238 **描述：** 介绍2027年农历特点，涉及春节、除夕、立春及节日与节气重合等情况。 **pubDate：** 周四, 10 9月 2026 15:56:00 GMT 2. **标题：** “2027日历表｜2027年日历、农历、节气、周末” **链接：** https://chinacalendar.app/zh-cn/2027-calendar **描述：** 提供全年逐月日期，并附农历、节气和周末标记；因官方假期安排尚未发布，不列放假调休。 **pu …[截断,原长1550]`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%222027%E7%BA%A7%E6%8E%A8%E5%85%8D%E7%94%9F%E9%A2%84%E6%8A%A5%E5%90%8D%22&format=rss"}` → `Descriptions are summarized to stay within the quote limit. 1. **Title:** "2027年_百度百科" **Link:** https://baike.baidu.com/item/2027%E5%B9%B4/7710238 **Description:** Covers 2027 lunar-calendar traits: Spring Festival on Feb 6, New Year’s Eve on the 29th of the 12th month, five straight years without a 30th day, and Feb  …[截断,原长2135]`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%222027%E5%B9%B4%E9%A2%84%E6%8E%A8%E5%85%8D%22&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%22%E9%A2%84%E6%8E%A8%E5%85%8D%22+%E6%8A%A5%E5%90%8D+%E6%88%AA%E6%AD%A2+985&format=rss"}` → `1. Title: “预_百度百科”; Link: https://baike.baidu.com/item/%E9%A2%84/4942379; Description: Baidu Baike entry on the character, covering adjective/verb senses, classical interchangeable forms, and dictionary explanations. PubDate: 周四, 10 9月 2026 21:19:00 GMT 2. Title: “预的意思,预的解释,预的拼音,预的部首,预的笔顺-汉语国学”; Link: https://www.hanyu …[截断,原长529]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-11 13:51）

General-phrase queries work better than school names. Running aggregator-style searches.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

The quoted queries fail because Bing treats 2027 as a calendar term. Hmm.

The most successful query was: 接收推荐免试研究生 预报名 (no school, no year) which returned many 2027 school notices. Let me run more variants of that:
- 接收推荐免试研究生 预报名 2027
- 2027 接收推荐免试研究生 通知
- 推荐免试研究生 预报名 通知
- 接收推免生 预报名 公告

Let me run those. Also, importantly, the successful query's results were ranked by relevance and the "pubDate" was crawl date (always ~10 Sep 2026), not the notice date. Fine.

Let me do batch:
1. q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D+2027
2. q=%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D+%E9%80%9A%E7%9F%A5
3. q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E5%85%8D%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D+%E5%85%AC%E5%91%8A
4. q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D (repeat? cached, avoid)

Let me instead pick #4 = 预推免 接收推免生 通知 研究生院

Anchors that worked: "接收推荐免试研究生" phrase.

Batch:
1. 接收推荐免试研究生 预报名 2027
2. 接收推荐免试研究生 预报名 通知 (may return same set, but more)
3. 接收推免生 预报名 截止
4. 2027 推免 预报名 研究生院

Let me encode:
1. %E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D+2027
2. %E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D+%E9%80%9A%E7%9F%A5
3. %E6%8E%A5%E6%94%B6%E6%8E%A8%E5%85%8D%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D+%E6%88%AA%E6%AD%A2
4. 2027+%E6%8E%A8%E5%85%8D+%E9%A2%84%E6%8A%A5%E5%90%8D+%E7%A0%94%E7%A9%B6%E7%94%9F%E9%99%A2

Let me go.

</details>

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D+2027&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D+%E9%80%9A%E7%9F%A5&format=rss"}` → `1. **Title:** “接收_百度百科” **Link:** https://baike.baidu.com/item/%E6%8E%A5%E6%94%B6/11013187 **Description:** Chinese-term entry; explains senses like receiving/seeing/hearing and passive acceptance, with a text-message example. **PubDate:** 周四, 10 9月 2026 17:29:00 GMT 2. **Title:** “接收与接受的区别在哪里？_百度知道” **Link:** https:// …[截断,原长3021]`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E5%85%8D%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D+%E6%88%AA%E6%AD%A2&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=2027+%E6%8E%A8%E5%85%8D+%E9%A2%84%E6%8A%A5%E5%90%8D+%E7%A0%94%E7%A9%B6%E7%94%9F%E9%99%A2&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

The results are highly variable. Adding extra terms causes Bing to drop the phrase. The one query that worked great was:
"接收推荐免试研究生 预报名" (11 chars + space + 3 chars)

Hmm, but now "接收推荐免试研究生 预报名 2027" fails and "接收推荐免试研究生 预报名 通知" fails. Interesting. Maybe Bing is rate-limiting successful repeated patterns, or the extraction model is flaky.

Actually — the "no text" result may just be the extraction model failing intermittently on a valid page. Let me retry those exact URLs; WebFetch caches 15 min, so retry returns cached content, and the extraction model may succeed this time. Let me retry the failed ones.

Actually if it's cached from a failed extraction, re-calling might re-run extraction. Let me retry.

Let me retry the 3 failed plus rerun the known-good query slightly modified.

Known good (cached): https://cn.bing.com/search?q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D&format=rss

Let me retry:
1. same as above but I'll re-call it to get full listing (it gave 10 items).
Actually the earlier answer gave 10 items but truncated? It listed 10. Good.

Let me now pivot: Instead of fighting search, go directly to known aggregator sites and university grad school news pages via WebFetch. E.g.:
- yz.chsi.com.cn/tm/ 
- 保研通知网 (need URL)
- Each school's 研究生院 news list.

But the most efficient: use the search to find the notice URL, then WebFetch the notice itself.

Let me retry the failed searches, and also try the query "2027年接收推荐免试研究生工作办法" style.

Actually, let me reconsider: the extraction failures might be because Bing returned a page with ~10 results but no clear text. Hard to know.

Let me try a different tactic: use Bing RSS with the query "接收推荐免试攻读研究生 预报名" or use per-school queries with the full anchor "接收推荐免试研究生" which Bing understands:
e.g. q=清华大学+接收推荐免试研究生

Let me test that pattern for a few schools. Encoding 清华大学 + %E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F.

Let me batch 4 schools: 清华, 北大, 上海交大, 浙大.

Encodings:
清华 = %E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6
北大 = %E5%8C%97%E5%A4%A7
上海交大 = %E4%B8%8A%E6%B5%B7%E4%BA%A4%E5%A4%A7
浙大 = %E6%B5%99%E5%A4%A7
anchor = %E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6+%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E5%8C%97%E5%A4%A7+%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+2027&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E4%B8%8A%E6%B5%B7%E4%BA%A4%E9%80%9A%E5%A4%A7%E5%AD%A6+%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F&format=rss"}` → `1. Title: “上海市人民政府” Link: https://www.sh`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6+%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F&format=rss"}` → `RSS 条目共 10 条；以下描述为简要转述，标题按原文用引号。 1. 标题："浙江省_百度百科" 链接：https://baike.baidu.com/item/%e6%b5%99%e6%b1%9f%e7%9c%81/190275 描述：介绍浙江得名与钱塘江有关；地形常被概括为多山少水少田，岛屿数量全国最多，海岸线总长全国第一；气候为亚热带季风湿润型；陆域约 10.55 万平方千米，海域约 26 万平方千米。 pubDate：周四, 10 9月 2026 01:45:00 GMT 2. 标题："浙江省人民政府" 链接：https://www.zj.gov.cn/ 描述：页面列出多项动态，包括首次小时级绿电交易、“法治浙江建设20年 …[截断,原长1959]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Adding school names mostly fails — Bing returns region encyclopedia entries. The search quality is very inconsistent.

New approach: Rather than relying on Bing web search, fetch the university graduate admission websites directly and look at their news lists. But that's a lot of sites, and I need to find the specific notice.

Alternatively, use the successful pattern: the query "接收推荐免试研究生 预报名" returned 10 excellent results. Let me get MORE pages from that same query by paginating (first=11, first=21, etc. for Bing). Also try related anchor phrases that Bing handles:
- "推荐免试研究生预报名"
- "接收推荐免试研究生预报名"

Let me try the Bing pagination on that query and also try the exact phrase query.

Bing pagination: add &first=11 to RSS? RSS may not support pagination. Hmm.

Let me instead try variations:
- q=%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F%E9%A2%84%E6%8A%A5%E5%90%8D (推荐免试研究生预报名, no space)
- q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F%E9%A2%84%E6%8A%A5%E5%90%8D (接收推荐免试研究生预报名)

These exact phrases might hit the notice titles directly.

Also try:
- "预推免 报名" (space)
- "推免 预报名 系统"

And Chinese aggregator: 保研通知网. Let me search "保研通知网 预推免".

Let me batch:
1. %E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F%E9%A2%84%E6%8A%A5%E5%90%8D
2. %E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F%E9%A2%84%E6%8A%A5%E5%90%8D
3. %E9%A2%84%E6%8E%A8%E5%85%8D+%E6%8A%A5%E5%90%8D+%E7%B3%BB%E7%BB%9F
4. %E4%BF%9D%E7%A0%94%E9%80%9A%E7%9F%A5%E7%BD%91+%E9%A2%84%E6%8E%A8%E5%85%8D

Go.

Encoding check:
接收推荐免试研究生预报名 = %E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F%E9%A2%84%E6%8A%A5%E5%90%8D
推荐免试研究生预报名 = %E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F%E9%A2%84%E6%8A%A5%E5%90%8D
预推免 = %E9%A2%84%E6%8E%A8%E5%85%8D; 报名 = %E6%8A%A5%E5%90%8D; 系统 = %E7%B3%BB%E7%BB%9F
保研通知网 = %E4%BF%9D%E7%A0%94%E9%80%9A%E7%9F%A5%E7%BD%91

</details>

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F%E9%A2%84%E6%8A%A5%E5%90%8D&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F%E9%A2%84%E6%8A%A5%E5%90%8D&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E9%A2%84%E6%8E%A8%E5%85%8D+%E6%8A%A5%E5%90%8D+%E7%B3%BB%E7%BB%9F&format=rss"}` → `1. “全国推荐免试攻读研究生（免初试、转段）信息公开管理 ...” - link: https://yz.chsi.com.cn/tm/ - description: 全国统一的推免信息备案公开与报名录取平台，推免生资格审核、报名、录取及备案公开均通过该系统。 - pubDate: 周三, 09 9月 2026 22:24:00 GMT 2. “入口 - 研究生招生平台” - link: https://enroll.sysu.edu.cn/ - description: 中山大学研究生招生平台入口，提及其综合性学府与治学传统。 - pubDate: 周四, 10 9月 2026 15:28:00 GMT 3. “华南理工大学推免 …[截断,原长1639]`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E4%BF%9D%E7%A0%94%E9%80%9A%E7%9F%A5%E7%BD%91+%E9%A2%84%E6%8E%A8%E5%85%8D&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Progress. I now have:
- 北京理工大学 yz.bit.edu.cn/yzbm/logon (预报名系统)
- 中山大学 enroll.sysu.edu.cn
- 华南理工 system

Let me now try to fetch key aggregator pages and the found notices. But I still need the actual notices with dates.

New idea: There's a "保研通知网" that aggregates. Let me find its URL. Also eeban.com. Let me WebFetch eeban directly: https://www.eeban.com/ and see if there's a 预推免 board.

Also 研招网 yz.chsi.com.cn/tm/ shows the national system timeline.

Actually, a much better approach for comprehensive coverage: use the school's own 研究生院 news page. But finding the exact notice URL requires search.

Let me try to leverage Bing RSS more effectively with query patterns that work. Notably "预推免 报名 系统" worked (returned school systems). Let me try "2027年预推免 通知" etc. But quoted 2027 fails.

Let me try queries with the exact string "2027年" appended to 预推免 but without quotes: e.g. "预推免 2027年 招生" 
Hmm earlier "2027年预推免" quoted failed; unquoted "2026年预推免" returned calendar stuff.

The tokenizer treats 2027年 as a year. Best to avoid year and rely on the fact that current results are 2027-cycle. The query "预推免 报名 系统" returned 2027 notices.

Let me run more no-year / phrase queries:
- "夏令营 预推免 2027" 
- "预推免 通知 截止"
- "推免生预报名 截止时间"
- "预推免 报名截止时间"

And also fetch eeban.com.

Let me batch:
1. q=%E9%A2%84%E6%8E%A8%E5%85%8D+%E9%80%9A%E7%9F%A5+%E6%88%AA%E6%AD%A2
2. q=%E9%A2%84%E6%8E%A8%E5%85%8D+%E6%8A%A5%E5%90%8D%E6%88%AA%E6%AD%A2%E6%97%B6%E9%97%B4
3. q=%E6%8E%A8%E5%85%8D%E7%94%9F%E9%A2%84%E6%8A%A5%E5%90%8D+%E6%88%AA%E6%AD%A2%E6%97%B6%E9%97%B4
4. eeban.com homepage

Go.

Encoding:
预推免 通知 截止: %E9%A2%84%E6%8E%A8%E5%85%8D+%E9%80%9A%E7%9F%A5+%E6%88%AA%E6%AD%A2
预推免 报名截止时间: %E9%A2%84%E6%8E%A8%E5%85%8D+%E6%8A%A5%E5%90%8D%E6%88%AA%E6%AD%A2%E6%97%B6%E9%97%B4
推免生预报名 截止时间: %E6%8E%A8%E5%85%8D%E7%94%9F%E9%A2%84%E6%8A%A5%E5%90%8D+%E6%88%AA%E6%AD%A2%E6%97%B6%E9%97%B4
报名截止时间 = %E6%8A%A5%E5%90%8D%E6%88%AA%E6%AD%A2%E6%97%B6%E9%97%B4
截止时间 = %E6%88%AA%E6%AD%A2%E6%97%B6%E9%97%B4

</details>

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E9%A2%84%E6%8E%A8%E5%85%8D+%E9%80%9A%E7%9F%A5+%E6%88%AA%E6%AD%A2&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E9%A2%84%E6%8E%A8%E5%85%8D+%E6%8A%A5%E5%90%8D%E6%88%AA%E6%AD%A2%E6%97%B6%E9%97%B4&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E6%8E%A8%E5%85%8D%E7%94%9F%E9%A2%84%E6%8A%A5%E5%90%8D+%E6%88%AA%E6%AD%A2%E6%97%B6%E9%97%B4&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List forum boards and any 预推免/推免 notice links with titles and dates.", "url": "https://www.eeban.com/"}` → `WebFetch completed, but the extraction model returned no text.`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Everything failing now. Likely rate-limited by Bing, and eeban.com may be blocked/JS.

Let me pause and think. The failures might be transient. Let me try a single query to test.

Actually, let me reconsider the pattern: calls that "returned no text" might be because the extraction model received content but deemed it had no answer... no, the prompt is explicit "List every RSS item". Earlier failures returned "no text" while successes returned items. Possibly Bing sometimes returns an empty RSS (no results) and sometimes returns a CAPTCHA/error.

Let me test with the known-good URL again (cached) to see if extraction works.

Actually more useful: try fetching the actual notice pages I've already found. Those are university sites, not search engines — likely to work. Let me fetch:
1. https://yzb.nju.edu.cn/d4/57/c47868a840791/page.htm (南大)
2. https://yz.tongji.edu.cn/info/1010/4220.htm (同济)
3. https://yz.scut.edu.cn/2026/0828/c30108a633884/page.htm (华南理工)
4. https://www.yz.sdu.edu.cn/info/1022/1463.htm (山大)

Let me do these 4 and extract deadlines. These are high-value.

Also:
5. https://yz.neu.edu.cn/2026/0720/c5932a458191/page.htm (东北大学)
6. https://graduate.sysu.edu.cn/zsw/article/538 (中大)
7. https://gsao.fudan.edu.cn/fb/0b/c15014a785163/page.htm (复旦)

Let me batch 4 first.

</details>

- 🔧 **WebFetch** `{"prompt": "Extract: notice title, publishing date, the exact application/registration deadline date(s), any system open/close dates, and any statement about whether applications are still open. Quote the original Chinese sentences containing dates.", "url": "https://yzb.nju.edu.cn/d4/57/c47868a840791/page.htm"}` → `- **Notice title:** “南京大学2027年接收推荐免试研究生预报名通知” - **Publishing date:** “发布时间：2026-08-03浏览次数：10” - **Application/registration deadline:** None stated in the provided content. - **System open/close dates:** None stated. - **Whether applications are still open:** No statement provided.`

- 🔧 **WebFetch** `{"prompt": "Extract: notice title, publishing date, the exact application/registration deadline date(s), system open/close dates, and any statement about whether applications are still open. Quote the original Chinese sentences containing dates.", "url": "https://yz.tongji.edu.cn/info/1010/4220.htm"}` → `标题原文：“各学院2027年接收推荐免试研究生（含直接攻博）预报名通知汇总（更新中）” 发布日期原文：“发布日期: 2026-07-06” 系统开放/关闭日期：本页未给出具体日期。仅提示“按照院系通知的时间节点在我校研究生报考服务系统中进行预报名”。 是否仍开放：标题注明“更新中”，正文称“预报名工作现已启动”；但页面没有逐学院说明是否仍开放。 各学院报名截止时间原文短引： - “010-建筑与城市规划学院”：“2026年8月14日17:00” - “020-土木工程学院”：“2026年8月5日23:59” - “030-机械工程与机器人学院”：“2026年9月1日12:00” - “040-经济与管理学院（学术学位）”：“2026 …[截断,原长781]`

- 🔧 **WebFetch** `{"prompt": "Extract: notice title, publishing date, the exact application/registration deadline date(s), system open/close dates, and whether applications are still open. Quote the original Chinese sentences containing dates.", "url": "https://yz.scut.edu.cn/2026/0828/c30108a633884/page.htm"}` → `- 标题：**“华南理工大学接收2027年推荐免试研究生预报名通知”** - 发布/落款日期：页面显示**“发布管理员 2026-08-28”**；文末为**“华南理工大学研究生招生办公室 2026年8月28日”**。 - 明确报名截止：**“请意向申请考生务必在9月15日前在我校预报名系统完成报名工作。”** 原文未写年份，仅写“9月15日前”。 - 其他相关日期：**“我校各学院（系）将于9月中旬起陆续开始复试资格审核”**；**“申请人可于9月中下旬起陆续在我校预报名系统查询是否获得复试资格。”** - 系统开通/关闭日期：通知仅称**“现开通”**预报名系统，未给出具体开通日；也未给出系统关闭日。 - 当前是否仍开放：仅凭该 …[截断,原长378]`

- 🔧 **WebFetch** `{"prompt": "Extract: notice title, publishing date, the exact application/registration deadline date(s), system open/close dates, and whether applications are still open. Quote the original Chinese sentences containing dates.", "url": "https://www.yz.sdu.edu.cn/info/1022/1463.htm"}` → `- 标题：“山东大学2027年接收推荐免试硕士研究生和本科直博生预报名通知” - 页面时间：“更新时间：2026-08-28”；落款日期：“2026年8月28日”。 - 系统开放起点：“系统开放时间：2026年9月1日09:00，具体报名开始时间和截止时间由我校各招生单位自主确定，请登录系统后查看。” - 统一截止/关闭日期：通知未给出。具体截止时间由各招生单位自行设定，需登录系统查询。 - 其他日期提示：“我校各招生单位将于9月中旬起择优通知考生参加考核。” - 当前是否仍可申请：页面未说明此刻开放状态，无法仅凭该页判断；只给出了开放起点，截止由各单位安排。`

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-11 13:53）

Let me fetch the actual notice pages already discovered — these are university sites, more reliable than search.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Good progress. Now I have:
- 南京大学: notice published 2026-08-03, no deadline on page — need more. Maybe the notice links to departments. Mark 未核实.
- 同济大学: 各学院截止 dates; most used up by Sep 8, etc. 数学科学学院 2026-09-08 12:00 — past. 机械 2026-09-01 12:00 — past. So 同济 mostly closed by 9/8. But "更新中" means some学院 may have later deadlines. Need to check remaining list (cut off).
- 华南理工: "9月15日前" — deadline >= 2026-09-11 → OPEN. Good, strong evidence.
- 山东大学: system opened 2026-09-01 09:00, deadlines per unit, not uniform → likely still open for some. 未核实 exact.

Now, this approach (search → fetch) works. But search is unreliable. Let me try to get more search results. Perhaps Bing rate-limits and I should space out calls or use a different query each time.

Let me retry Bing RSS now with a fresh query. If still failing, I'll switch strategy: fetch each school's graduate admission news list page directly (I know common URLs):
- 清华: yz.tsinghua.edu.cn
- 北大: admission.pku.edu.cn / grs.pku.edu.cn
- 复旦: gsao.fudan.edu.cn (found: 报名通知 fb/0b/c15014a785163)
- 上交: yzb.sjtu.edu.cn
- 浙大: grs.zju.edu.cn / yjsy.zju.edu.cn
- 中科大: yz.ustc.edu.cn
- 南大: yzb.nju.edu.cn (found)
- 西交: yz.xjtu.edu.cn
- 哈工大: yzb.hit.edu.cn
- 北航: yzb.buaa.edu.cn
- 北理: yz.bit.edu.cn
- 天大: yzb.tju.edu.cn
- 南开: yzb.nankai.edu.cn
- 武大: gs.whu.edu.cn
- 华科: gszs.hust.edu.cn
- 中大: graduate.sysu.edu.cn
- 华南理工: yz.scut.edu.cn
- 川大: yz.scu.edu.cn
- 电子科大: yz.uestc.edu.cn
- 重庆大学: yz.cqu.edu.cn
- 湖南大学: yjsy.hnu.edu.cn
- 中南: gra.csu.edu.cn
- 大连理工: gs.dlut.edu.cn
- 东北大学: yz.neu.edu.cn
- 吉大: yjsy.jlu.edu.cn
- 兰大: yjs.lzu.edu.cn
- 西北工大: yzb.nwpu.edu.cn
- 西北农林: yz.nwsuaf.edu.cn
- 中国农大: yz.cau.edu.cn
- 北师大: yzb.bnu.edu.cn
- 中央民大: yz.muc.edu.cn
- 中国海洋: yz.ouc.edu.cn
- 山大: yz.sdu.edu.cn (found)
- 厦大: gs.xmu.edu.cn
- 华东师大: yjszs.ecnu.edu.cn
- 国防科大: yz.nudt.edu.cn

Fetching each homepage may give news lists with the 2027 预推免 notice. That's ~35 fetches. Doable but heavy. WebFetch does conversion + small model extraction. Let me prioritize.

But first, let me retry Bing search; if it works, it's much more efficient.

Let me test 2 queries.

Actually, a smarter move: Use the Bing RSS search but with a unique query each time to avoid rate limit. Possible the "no text" is due to simultaneous 4 parallel requests. Earlier the successful ones were in batches of 4 too though.

Hmm, looking at pattern: batch of 4 → sometimes 1-2 succeed. It seems random. Let me just keep trying with more batches; success rate ~50%.

Let me run another batch of 4 general queries with distinct phrasing:
1. 预推免 招生 公告
2. 接收推免生 预报名 公告
3. 2027 推免 申请 截止 9月
4. 研究生院 预推免 报名

Encoding:
1. %E9%A2%84%E6%8E%A8%E5%85%8D+%E6%8B%9B%E7%94%9F+%E5%85%AC%E5%91%8A
2. %E6%8E%A5%E6%94%B6%E6%8E%A8%E5%85%8D%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D+%E5%85%AC%E5%91%8A
3. 2027+%E6%8E%A8%E5%85%8D+%E7%94%B3%E8%AF%B7+%E6%88%AA%E6%AD%A2+9%E6%9C%88
4. %E7%A0%94%E7%A9%B6%E7%94%9F%E9%99%A2+%E9%A2%84%E6%8E%A8%E5%85%8D+%E6%8A%A5%E5%90%8D

Also let me fetch 复旦 notice and 东北大学 notice in this batch? No, keep search.

Actually let me split: 2 search + 2 notice fetches (more productive). Let me fetch 复旦 and 东北大学 notices, plus 2 searches.

Wait, 复旦 notice: 各院系通常 7月6日10:00至8月10日17:00, 个别调整; 药学院延长至8月17日. So likely closed. Let me fetch to confirm and see if any院系 still open.

Batch:
1. fetch 复旦 https://gsao.fudan.edu.cn/fb/0b/c15014a785163/page.htm
2. fetch 东北大学 https://yz.neu.edu.cn/2026/0720/c5932a458191/page.htm
3. search 预推免 招生 公告
4. search 接收推免生 预报名 公告

</details>

- 🔧 **WebFetch** `{"prompt": "Extract: notice title, publishing date, exact registration deadline dates for each college/school (院系), whether applications are still open. Quote original Chinese sentences with dates.", "url": "https://gsao.fudan.edu.cn/fb/0b/c15014a785163/page.htm"}` → `- 通知标题：“复旦大学招收2027级推荐免试研究生报名通知” - 发布日期：页面仅显示“2026-07-03浏览次数：10” - 各院系报名截止日期：所给内容中没有列出任何院系的具体截止日期，无法提取。 - 申请是否仍开放：页面未说明报名状态或截止说明，无法判断。 可用原文日期片段仅有一处：“2026-07-03浏览次数：10”。除此之外，未见含院系报名截止日期的原文句子。`

- 🔧 **WebFetch** `{"prompt": "Extract: notice title, publishing date, exact registration deadline dates, system open/close dates, whether applications are still open. Quote original Chinese sentences with dates.", "url": "https://yz.neu.edu.cn/2026/0720/c5932a458191/page.htm"}` → `- 通知标题：“东北大学2027年接收推荐免试研究生工作办法” - 发布日期：“发布时间：2026-07-20” - 报名截止日期：页面未给出具体日期，只写“报名截止时间及审核时间请咨询各学院”。 - 系统开通/关闭日期：未提供具体时间。仅提到“教育部‘推免服务系统’开通之前”可预报名，以及待录取后须“规定时间内确认”，但没有开通或关闭的准确日期。 - 是否仍开放申请：依据该页面无法判断，因为缺少明确截止日和系统时间；需按原文咨询各学院。`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E9%A2%84%E6%8E%A8%E5%85%8D+%E6%8B%9B%E7%94%9F+%E5%85%AC%E5%91%8A&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E5%85%8D%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D+%E5%85%AC%E5%91%8A&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Search still failing. Let me try a different approach for search: Bing RSS with simpler single-keyword queries that Bing ranks by recency. Or use Bing's site: operator.

Actually, wait. Maybe the "no text" is because the extraction model gets an empty RSS (0 results) for those queries. The queries with more words may yield 0 results. Earlier "接收推荐免试研究生 预报名" yielded 10; "预推免 报名 系统" yielded 9. Those are 2-3 token queries. The failing ones are also short though ("预推免 通知 截止").

Hmm, random.

Let me try the two exact queries that worked before but with slight modifications to get NEW results (pagination via &first=):

For RSS, Bing might honor &first=11? Let me try:
https://cn.bing.com/search?q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D&format=rss&first=11

Let me test.

Also try &count=30.

Let me do:
1. known-good query + &first=11
2. known-good query with count=30
3. new query: 预推免 报名 通知 研究生院 — no.
3. new query: 推免 预报名 通知 985
4. new query: 2027级 推免 预报名 (2027级 = 2027%E7%BA%A7)

Go.

Encoding: 2027级 推免 预报名 = 2027%E7%BA%A7+%E6%8E%A8%E5%85%8D+%E9%A2%84%E6%8A%A5%E5%90%8D

</details>

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D&format=rss&first=11&count=30"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E9%A2%84%E6%8E%A8%E5%85%8D+%E6%8A%A5%E5%90%8D+%E7%B3%BB%E7%BB%9F&format=rss&first=11&count=30"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=2027%E7%BA%A7+%E6%8E%A8%E5%85%8D+%E9%A2%84%E6%8A%A5%E5%90%8D&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List every RSS item: title, link, description, pubDate.", "url": "https://cn.bing.com/search?q=%E6%8E%A8%E5%85%8D+%E9%A2%84%E6%8A%A5%E5%90%8D+%E9%80%9A%E7%9F%A5+985&format=rss"}` → `WebFetch completed, but the extraction model returned no text.`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

All fail. Bing is likely rate-limited now (or blocked). Let me switch strategy to direct fetching of school grad-school news pages.

Let me consider: The task is big (39 schools). Direct fetching 39 homepages is a lot but feasible if I batch 4 at a time (~10 rounds). However, homepages may not directly link the 2027 预推免 notice, and the extraction model may not surface it.

Alternative: use known aggregator. Let me find a working aggregator via direct URL guesses:
- https://www.baoyan.com.cn/
- http://www.eeban.com/forum.php?mod=forumdisplay&fid=... 
- https://yz.chsi.com.cn/tm/ (national system)

Also 研招网 (yz.chsi.com.cn) has 推免 service. The national "推免服务系统" opens ~Sept 22. Not per-school.

Let me try fetching some school grad school "推免" news list pages directly. Many use a search/tzgg list. Let me try:

清华: https://yz.tsinghua.edu.cn/  (maybe /zsxx/tms.htm)
Actually Tsinghua 研究生招生: yz.tsinghua.edu.cn. Their 推免 (推荐免试) page: https://yz.tsinghua.edu.cn/zsxx/tjszs/tmszs.htm? unknown.

Let me just fetch homepages of grad admission sites in batches and ask the extraction model to find any 2027 推免/预推免 notice link + date. If homepage doesn't list it, I'll need the news list page.

Better: use Bing RSS once it recovers. Let me wait a bit by doing useful direct fetches, then retry search.

Let me try a batch of direct grad-school sites known to host notice lists:
1. https://yz.tsinghua.edu.cn/  (清华研招)
2. https://admission.pku.edu.cn/ (北大招生)
3. https://yzb.sjtu.edu.cn/ (上交研招)
4. https://grs.zju.edu.cn/ (浙大研究生)

Hmm, asking extraction model "find 2027 推免 notice link" on a homepage might work.

Actually, a more reliable route: many of these notices are on 院系 sites, and the graduate school 招生 page has a "通知公告" list. Let me fetch and ask for the notice list.

Let me also reconsider: maybe use WebFetch on Bing normal (not RSS) — earlier one normal Bing worked partially. Try https://cn.bing.com/search?q=... with a good query and no format=rss. Earlier the non-RSS "2026年预推免 报名截止 2027级" returned generic calendar. But "接收推荐免试研究生 预报名" non-RSS might return proper results. Let me try that.

Batch:
1. non-RSS Bing: https://cn.bing.com/search?q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D&count=30
2. https://yz.tsinghua.edu.cn/
3. https://yzb.sjtu.edu.cn/
4. https://grs.zju.edu.cn/

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "List search results: title, URL, snippet. Focus on 2027 推免/预推免 notices.", "url": "https://cn.bing.com/search?q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D&count=30"}` → `以下为页面中与 2027 推免/预推免相关的搜索结果： - “全国推荐免试攻读研究生（免初试、转段）” — https://yz.chsi.com.cn/tm/index — “全国推荐免试攻读研究生（免初试、转段）信息公开管理服务系统”（简称“推免服务系统”）是全国统一的推免工作信息备案公开平台 … - “江南大学接收2027年推荐免试研究生预报名公告-江南大学研究 ...” — https://yz.jiangnan.edu.cn/info/1012/3864.htm — “2026年8月31日 · 江南大学从即日起接收2027年推免生预报名，获得就读本科高校推荐资格且有意申请免试攻读我校研究生的同学， …” - “东北大学20 …[截断,原长1569]`

- 🔧 **WebFetch** `{"prompt": "Find and list any notice links (标题+URL+日期) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Also give the site's news-list page URL if present.", "url": "https://yz.tsinghua.edu.cn/"}` → `相关公告（页面“最新公告”区）： - “清华大学2027年接收推荐免试研究生办法”｜日期：032026.07｜URL：`info/1024/3251.htm` - “清华大学2027年博士研究生招生专业目录_推荐免试”｜日期：302026.06｜URL：`https://yzbm.tsinghua.edu.cn/publish/s01/s0103/detail/2ede1fca-d9a0-407a-9d68-3475494848b7/2` - “清华大学2027年硕士研究生招生专业目录_推荐免试”｜日期：302026.06｜URL：`https://yzbm.tsinghua.edu.cn/publish/s01/s0103/det …[截断,原长458]`

- 🔧 **WebFetch** `{"prompt": "Find and list any notice links (标题+URL+日期) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Also give the news-list page URL.", "url": "https://yzb.sjtu.edu.cn/"}` → `No matching notice links with 标题+URL+日期 for 2027年接收推荐免试研究生 / 推免生 / 预推免 are present in the provided page content. Related navigation links only: - “预推免” — http://ga.sjtu.edu.cn/zsgl/ytmgl/ — 无日期 - “预推免报名” — http://ga.sjtu.edu.cn/zsgl/ytmgl/ — 无日期 - “预推免公示” — /xxgs/ytmgs — 无日期 Closest news-list page URL: /xxgs/ytmgs`

- 🔧 **WebFetch** `{"prompt": "Find and list any notice links (标题+URL+日期) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Also give the news-list page URL.", "url": "https://grs.zju.edu.cn/"}` → ``

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-11 13:54）

Bing RSS is throttled. Switching to direct university-site fetches plus non-RSS Bing.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Non-RSS Bing works now! Good. Let me use non-RSS Bing with the working query and also school-specific queries.

Key new findings:
- 清华: 清华大学2027年接收推荐免试研究生办法 info/1024/3251.htm dated 2026-07 (July 3?) — need deadline.
- 上交: 预推免 system ga.sjtu.edu.cn/zsgl/ytmgl/

Let me now use non-RSS Bing for school-specific searches. It seems non-RSS is more reliable. Let me run batches of 4 with school queries using the phrase that works.

Query pattern: <school> 2027年接收推荐免试研究生 — maybe works better now. Let me test with several schools.

Encodings again. Let me use "接收推荐免试研究生" anchor + school:
- 清华大学接收推荐免试研究生 → 清华大学+2027+接收推荐免试研究生
Actually earlier "清华大学 接收推荐免试研究生" via RSS failed, but non-RSS may work.

Let me try non-RSS for:
1. 浙江大学 2027 推免
2. 中国科学技术大学 2027 推免
3. 西安交通大学 2027 推免
4. 哈尔滨工业大学 2027 推免

Encodings:
浙江大学 = %E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6
中国科学技术大学 = %E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E6%8A%80%E6%9C%AF%E5%A4%A7%E5%AD%A6
西安交通大学 = %E8%A5%BF%E5%AE%89%E4%BA%A4%E9%80%9A%E5%A4%A7%E5%AD%A6
哈尔滨工业大学 = %E5%93%88%E5%B0%94%E6%BB%A8%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6
接收推荐免试研究生 = %E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F
2027年 = 2027%E5%B9%B4

Let me build: q=<school>+2027%E5%B9%B4+%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F

Go with non-RSS (no format=rss).

</details>

- 🔧 **WebFetch** `{"prompt": "List search results: title, URL, snippet. Focus on 2027 推免/预推免 notices.", "url": "https://cn.bing.com/search?q=%E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6+2027%E5%B9%B4+%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F"}` → `根据页面内容，未出现“2027年接收推荐免试研究生”或“预推免”的专门通知。与浙江大学直接相关的仅一条： - 标题：“浙江大学” URL: https://www.zju.edu.cn 摘要：“浙江大学（Zhejiang University），简称“浙大”，位于浙江省杭州市，是中华人民共和国教育部直属的综合性全国重点大学， …” 其余结果多为浙江省、政府、旅游、杭州百科等内容，与2027推免/预推免无关。`

- 🔧 **WebFetch** `{"prompt": "List search results: title, URL, snippet. Focus on 2027 推免/预推免 notices.", "url": "https://cn.bing.com/search?q=%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E6%8A%80%E6%9C%AF%E5%A4%A7%E5%AD%A6+2027%E5%B9%B4+%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F"}` → `“中国科学技术大学 2027年 接收推荐免试研究生”搜索结果中未见2027推免/预推免通知。所列结果均与该校招生无关，具体如下： 1. “中华人民共和国_百度百科” — https://baike.baidu.com/item/中华人民共和国/106554 — “中华人民共和国（the People's Republic of China），简称“中国”，成立于1949年10月1日，位于亚洲东部，太平洋西岸，是工人阶级 …” 2. “中国（世界四大文明古国之一）_百度百科” — https://baike.baidu.com/item/中国/1122445 — “中国各族人民共同创造了光辉灿烂的文化，具有光荣的革命传统。 中国是以汉 …[截断,原长1258]`

- 🔧 **WebFetch** `{"prompt": "List search results: title, URL, snippet. Focus on 2027 推免/预推免 notices.", "url": "https://cn.bing.com/search?q=%E8%A5%BF%E5%AE%89%E4%BA%A4%E9%80%9A%E5%A4%A7%E5%AD%A6+2027%E5%B9%B4+%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F"}` → `按“2027 推免/预推免通知”筛选：**无匹配项**。给定页面中的结果均与西安市、旅游或政府信息相关，未出现西安交通大学接收推荐免试研究生内容。 | 标题 | URL | 摘要 | |---|---|---| | 西安市_百度百科 | https://baike.baidu.com/item/%E8%A5%BF%E5%AE%89%E5%B8%82/1002501 | “1949年5月20日，西安市解放。 1954年6月19日，西安市成为陕西省辖市。 西安市还是“丝绸之路”的起点，中华文明和中华民族的发 …” | | 强烈推荐20个去西安必打卡的景点，感受千年古都的韵味！ | https://zhuanlan.zhihu.com/p …[截断,原长1617]`

- 🔧 **WebFetch** `{"prompt": "List search results: title, URL, snippet. Focus on 2027 推免/预推免 notices.", "url": "https://cn.bing.com/search?q=%E5%93%88%E5%B0%94%E6%BB%A8%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6+2027%E5%B9%B4+%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F"}` → `相关 2027 推免/预推免通知：**未在页面中发现**。以下结果均与哈尔滨工业大学 2027 年接收推免/预推免无关，主要是哈尔滨城市、旅游、政府等内容。 | # | 标题 | URL | 摘要 | |---|---|---|---| | 1 | “哈尔滨市_百度百科” | https://baike.baidu.com/item/%E5%93%88%E5%B0%94%E6%BB%A8%E5%B8%82/129324 | “播报 编辑 先秦时期 早在22000年前（旧石器时代 晚期），哈尔滨地区就已经有人类活动。 大约5000年前，哈尔滨地区进入 新石器时 …” | | 2 | “黑龙江哈尔滨旅游必去十大景点游玩攻略，2026年4 …[截断,原长1633]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-11 13:54）

Non-RSS Bing works reliably. Running school-specific queries.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

School-name queries fail badly (Bing treats school names as geographic). The generic phrase query "接收推荐免试研究生 预报名" works. So I should stick to generic queries and mine results, and use site:-restricted queries perhaps.

Let me try site-restricted Bing queries for each graduate admission domain, which should avoid the geographic pollution:
q=site%3Ayz.xxx.edu.cn+推免

Earlier site:yz.tsinghua.edu.cn 推免 (RSS) failed. Let me try non-RSS.

Let me construct site queries for many domains:
- site:yz.tsinghua.edu.cn 推免
- site:admission.pku.edu.cn 推免
- site:yzb.sjtu.edu.cn 推免
- site:gsao.fudan.edu.cn 推免
- site:grs.zju.edu.cn 推免  (cert expired for direct fetch, but search index ok)
- site:yz.ustc.edu.cn 推免
- site:yzb.nju.edu.cn 推免
- site:yz.xjtu.edu.cn 推免
- site:yzb.hit.edu.cn 推免
- site:yzb.buaa.edu.cn 推免
- site:yz.bit.edu.cn 推免
- site:yzb.tju.edu.cn 推免
- site:yzb.nankai.edu.cn 推免
- site:gs.whu.edu.cn 推免
- site:gszs.hust.edu.cn 推免
- site:graduate.sysu.edu.cn 推免
- site:yz.scut.edu.cn 推免
- site:yz.scu.edu.cn 推免
- site:yz.uestc.edu.cn 推免
- site:yz.cqu.edu.cn 推免
- site:yjsy.hnu.edu.cn 推免
- site:gra.csu.edu.cn 推免
- site:gs.dlut.edu.cn 推免
- site:yjsy.jlu.edu.cn 推免
- site:yjs.lzu.edu.cn 推免
- site:yzb.nwpu.edu.cn 推免
- site:yz.nwsuaf.edu.cn 推免
- site:yz.cau.edu.cn 推免
- site:yzb.bnu.edu.cn 推免
- site:yz.muc.edu.cn 推免
- site:yz.ouc.edu.cn 推免
- site:yz.sdu.edu.cn 推免
- site:gs.xmu.edu.cn 推免
- site:yjszs.ecnu.edu.cn 推免
- site:yz.nudt.edu.cn 推免
- site:yzb.seu.edu.cn 推免

I'm not 100% sure of all domains. Some may be wrong. Let me instead do a generic site query: site:edu.cn + 2027 + 预推免? Or site:*.edu.cn.

Better: Use query "2027年接收推荐免试研究生" as a quoted exact phrase — Bing may then find titles. Earlier quoted "2027年接收推荐免试研究生" returned calendar. Hmm.

Alternatively use the generic working query and mine the 10 results — but limited.

Let me test a site: query. If site: works, I can iterate.

Actually, a cleverer approach: use Bing with query "接收推荐免试研究生 预报名" but add "site:edu.cn" to bias toward university sites. Let me test:
q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D+site%3Aedu.cn

And also test a specific site query for 清华.

Let me update todos too.

Let me run batch:
1. q=接收推荐免试研究生 预报名 site:edu.cn
2. q=site:yz.tsinghua.edu.cn 推免
3. q=site:yzb.sjtu.edu.cn 推免
4. q=预推免 报名 site:edu.cn

Encodings:
site%3Aedu.cn
site%3Ayz.tsinghua.edu.cn
site%3Ayzb.sjtu.edu.cn

Go.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "Confirm working search endpoint (Bing non-RSS + generic phrase queries)", "priority": "high", "status": "completed"}, {"content": "Search site: queries across 985 grad-school domains for 2027 预推免/推免 notices", "priority": "high", "status": "in_progress"}, {"content": "Fetch each notice page to extract exact deadline", "priority": "high", "status": "pendin …[截断,原长412]` → `{"oldTodos":[{"content":"Confirm working search endpoint (Bing RSS intermittent)","status":"in_progress","priority":"high"},{"content":"Search all C9 + 华五 + 中坚九校 etc. for 2027 预推免 notices","status":"pending","priority":"high"},{"content":"Fetch each notice page to extract exact deadline","status":"pending","priority":" …[截断,原长947]`

- 🔧 **WebFetch** `{"prompt": "List search results: title, URL, snippet.", "url": "https://cn.bing.com/search?q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D+site%3Aedu.cn"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List search results: title, URL, snippet.", "url": "https://cn.bing.com/search?q=site%3Ayz.tsinghua.edu.cn+%E6%8E%A8%E5%85%8D"}` → `The page reports about 21,400 results. Visible result entries: 1. Title: "全国推荐免试攻读研究生（免初试、转段）" URL: https://yz.chsi.com.cn/tm/ Snippet: "推免服务系统是全国统一的推免工作信息备案公开平台和推免生网上报名录取系统。 推免生（含推免硕士生和直博生）资格审核确认 …" 2. Title: "推免录取信息公开_全国推荐免试攻读研究生（免初试、转段 ..." URL: https://yz.chsi.com.cn/tm/lqmd/index Snippet: "推免服务系统是全国统一的推免工作信息备案公开平台 …[截断,原长340]`

- 🔧 **WebFetch** `{"prompt": "List search results: title, URL, snippet.", "url": "https://cn.bing.com/search?q=site%3Ayzb.sjtu.edu.cn+%E6%8E%A8%E5%85%8D"}` → `以下为页面所示结果： 1. Title: “全国推荐免试攻读研究生（免初试、转段）” URL: https://yz.chsi.com.cn/tm/ Snippet: “推免服务系统是全国统一的推免工作信息备案公开平台和推免生网上报名录取系统。 推免生（含推免硕士生和直博生）资格审核确认 …” 2. Title: “推免录取信息公开_全国推荐免试攻读研究生（免初试、转段 ...” URL: https://yz.chsi.com.cn/tm/lqmd/index Snippet: “推免服务系统是全国统一的推免工作信息备案公开平台和推免生网上报名录取系统。 推免生（含推免硕士生和直博生）资格审核确认 …” 3. Title: “推免 …[截断,原长775]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

site: operator isn't respected well (results are generic). Bing site search returns irrelevant.

OK. Different plan: Directly fetch each university's 研究生招生 site and navigate to the "推免" or "通知公告" section. The extraction model worked for 清华 (found notice link + zxgg.htm list page). Let me do this for all schools. I'll fetch homepages or the 通知公告 list pages.

But that's ~35 fetches with uncertain extraction. Let me be strategic: fetch the "招生公告/通知" list page for each school's grad admission site, asking for links mentioning 推免/免试/预推免.

I know some URLs:
- 清华: https://yz.tsinghua.edu.cn/zxgg.htm (最新公告)
- 北大: https://admission.pku.edu.cn/ (招生网) 
- 复旦: https://gsao.fudan.edu.cn/ (研招)
- 上交: https://yzb.sjtu.edu.cn/ (found, has 预推免 link http://ga.sjtu.edu.cn/zsgl/ytmgl/)
- 南大: https://yzb.nju.edu.cn/ 
- 同济: https://yz.tongji.edu.cn/
- 华南理工: https://yz.scut.edu.cn/
- 山大: https://www.yz.sdu.edu.cn/
- 东北大学: https://yz.neu.edu.cn/
- 中大: https://graduate.sysu.edu.cn/zsw
- 北理: https://yz.bit.edu.cn/

Let me batch-fetch 4 list pages at a time. Actually, to maximize info, let me fetch the notices themselves where I have URLs, plus list pages for others.

Priority: get deadlines. Known notices needing deadline checks:
- 清华: info/1024/3251.htm → https://yz.tsinghua.edu.cn/info/1024/3251.htm
- 上交: ga.sjtu.edu.cn/zsgl/ytmgl/ (system)
- 中大: https://graduate.sysu.edu.cn/zsw/article/538
- 南航 (not 985, skip)
- 江南 (not 985, skip)

Let me fetch:
1. https://yz.tsinghua.edu.cn/info/1024/3251.htm
2. https://graduate.sysu.edu.cn/zsw/article/538
3. https://yz.tsinghua.edu.cn/zxgg.htm (list, to find more)
4. https://yzb.nju.edu.cn/ (list)

Go.

Also I should try the generic search again to find more schools. Let me mix: 2 fetches + 2 searches.

Batch:
1. fetch 清华 notice
2. fetch 中大 notice
3. search generic "预推免 报名 截止 9月" (non-RSS)
4. search generic "接收推荐免试研究生 预报名 2027" (non-RSS)

Encoding for searches:
预推免 报名 截止 9月: %E9%A2%84%E6%8E%A8%E5%85%8D+%E6%8A%A5%E5%90%8D+%E6%88%AA%E6%AD%A2+9%E6%9C%88
接收推荐免试研究生 预报名 2027: %E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D+2027

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "Extract: notice title, publishing date, exact application deadline date(s), system open/close dates, whether still open. Quote original Chinese sentences containing dates.", "url": "https://yz.tsinghua.edu.cn/info/1024/3251.htm"}` → `- Notice title: “清华大学2027年接收推荐免试研究生办法” - Publishing date shown: “032026.07” (appears to be 2026-07-03 based on the site’s date format, but the page text does not spell this out) - Exact application deadline date(s): Not present in the provided content. No date-bearing sentence about a deadline is included. - System ope …[截断,原长581]`

- 🔧 **WebFetch** `{"prompt": "Extract: notice title, publishing date, exact application deadline date(s), system open/close dates, whether still open. Quote original Chinese sentences containing dates.", "url": "https://graduate.sysu.edu.cn/zsw/article/538"}` → `- **通知标题**：“中山大学2027年接收优秀应届本科毕业生推荐免试攻读研究生报名的通知” - **发布日期**：“发布日期：2026-07-30” - **申请截止日期**：页面未给出统一的具体截止日；仅说明“各招生单位的报名、确认复试和确认待录取通知的截止时间不尽相同”。 - **系统开放/关闭日期**：未提供具体日期；只要求“申请者须于教育部规定时间内在“推免服务系统”完成网上注册相关操作”。 - **其他含日期信息**：“10月下旬前，完成拟录取名单网上公示。” 这不是申请截止日期。 - **是否仍开放**：无法从本页判断；页面没有明确当前是否仍可报名，也没有统一的报名起止日期。`

- 🔧 **WebFetch** `{"prompt": "List search results: title, URL, snippet. Focus on 2027 预推免/推免 notices with deadlines.", "url": "https://cn.bing.com/search?q=%E9%A2%84%E6%8E%A8%E5%85%8D+%E6%8A%A5%E5%90%8D+%E6%88%AA%E6%AD%A2+9%E6%9C%88"}` → `未发现 2027 年预推免/推免截止通知。唯一与推免相关的结果是 2026 年文章，且摘要未给出截止日期： - Title: “一文讲清楚2026年预推免、九推、十推流程 - 知乎” - URL: https://zhuanlan.zhihu.com/p/1946621251717144598 - Snippet: “2025年9月14日 · Hi各位小伙伴，针对评论区大家常问的问题，我来集中解答一下保研的预推免、九推和十推。 我会尽量把每个阶段 …” 其他结果多为字典释义、食品备案或百科内容，与 2027 预推免截止无关。`

- 🔧 **WebFetch** `{"prompt": "List search results: title, URL, snippet. Focus on 2027 推免 notices.", "url": "https://cn.bing.com/search?q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D+2027"}` → `基于所给页面，**未发现 2027 推免预报名相关通知**。页面显示约 49,100 个结果，但可见条目均围绕“接收/接受”或 receive 的词典释义、短信接收等。 | 标题 | URL | Snippet（概述） | |---|---|---| | “接收_百度百科” | https://baike.baidu.com/item/%E6%8E%A5%E6%94%B6/11013187 | 解释“接收”的汉语词义，含收到、看到、听到等。 | | “接收与接受的区别在哪里？_百度知道” | https://zhidao.baidu.com/question/658810490377242805.html | 2023-08-27， …[截断,原长1226]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Search is extremely unreliable now. The exact query "接收推荐免试研究生 预报名" (which worked) needs to be reused to mine more. But cached returns same 10.

Let me change approach more decisively: fetch university notice pages directly. I already have a set of notice URLs. For the remaining schools, I'll fetch their grad admission site's news list and ask for 推免-related links.

But the extraction model on a homepage might miss. Let me instead try fetching known "推免" specific pages.

Alternatively — leverage a Chinese aggregator site directly. Let me try:
- 中国教育在线 (eol.cn) 考研频道 推免 栏目: https://kaoyan.eol.cn/... 
- 考研帮 
- 保研岛 / baoyan
- 研招网 推免自主服务: yz.chsi.com.cn/tm/

Let me try fetching eeban.com with different URL (www.eeban.com timed out/no text). Try http://www.eeban.com/forum.php.

Also try 知乎专栏 article and sohu aggregator.

Actually, let me try Sogou's WeChat search: https://weixin.sogou.com/weixin?type=2&query=... (may be blocked).

Let me try a few aggregator URLs:
1. https://www.eeban.com/forum.php
2. https://kaoyan.eol.cn/tuimian/
3. https://yz.chsi.com.cn/tm/ (to get national timeline)
4. https://www.gaokao.cn/... no.

Hmm.

Better: Let me directly fetch the graduate admission sites' notice lists in batches. I'll ask extraction for links containing 推免/免试/预推免 with dates. Let me try with a set of list URLs I can guess. Even if some fail, others work.

Let me define list pages:
- 北大: https://admission.pku.edu.cn/zsxx/sszs/tjms/index.htm ? unknown. Try https://admission.pku.edu.cn/
- 浙大: https://grs.zju.edu.cn/ had cert expired. Try http://grs.zju.edu.cn/ (http) or https://yjsy.zju.edu.cn/
- 中科大: https://yz.ustc.edu.cn/
- 西交: https://yz.xjtu.edu.cn/
- 哈工大: https://yzb.hit.edu.cn/
- 北航: https://yzb.buaa.edu.cn/
- 北理: https://yz.bit.edu.cn/
- 天大: https://yzb.tju.edu.cn/
- 南开: https://yzb.nankai.edu.cn/
- 武大: https://gs.whu.edu.cn/
- 华科: https://gszs.hust.edu.cn/
- 川大: https://yz.scu.edu.cn/
- 电子科大: https://yz.uestc.edu.cn/
- 重庆大学: https://yz.cqu.edu.cn/
- 湖南大学: https://yjsy.hnu.edu.cn/
- 中南: https://gra.csu.edu.cn/
- 大连理工: https://gs.dlut.edu.cn/
- 吉大: https://yjsy.jlu.edu.cn/
- 兰大: https://yjs.lzu.edu.cn/
- 西北工大: https://yzb.nwpu.edu.cn/
- 西北农林: https://yz.nwsuaf.edu.cn/
- 中国农大: https://yz.cau.edu.cn/
- 北师大: https://yzb.bnu.edu.cn/
- 中央民大: https://yz.muc.edu.cn/
- 中国海洋: https://yz.ouc.edu.cn/
- 厦大: https://gs.xmu.edu.cn/
- 华东师大: https://yjszs.ecnu.edu.cn/
- 国防科大: https://yz.nudt.edu.cn/
- 东南: https://yzb.seu.edu.cn/
- 同济: https://yz.tongji.edu.cn/
- 华南理工: https://yz.scut.edu.cn/

That's a lot. Given time, let me prioritize the C9+华五+中坚九校 (user says重点).

C9: 清华, 北大, 复旦, 上交, 浙大, 中科大, 南大, 西交, 哈工大
华五: 复旦, 上交, 浙大, 中科大, 南大
中坚九校 (民间说法): 武大, 华科, 中大, 西安交大, 哈工大, 北理, 天大, 东南, 厦大 (varies). Another: 哈工大、西安交大、中山大学、武汉大学、华中科技大学、北京理工大学、天津大学、东南大学、厦门大学.

So重点: 清华 北大 复旦 上交 浙大 中科大 南大 西交 哈工大 武大 华科 中大 北理 天大 东南 厦大. Plus 同济 (already found).

Let me focus on these 16 + compile others found via generic searches.

Plan: fetch list pages for: 北大, 浙大, 中科大, 西交, 哈工大, 武大, 华科, 北理, 天大, 东南, 厦大. Plus fetch systems/notices for 上交.

Let me start with 4: 北大, 浙大, 中科大, 西交.

Ask: "List any notice links with titles and dates about 2027年接收推荐免试研究生/推免生/预推免, and give direct URLs."

Let me go.

</details>

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免 / 夏令营. Also give the news/notice list page URL. If none, say so.", "url": "https://admission.pku.edu.cn/"}` → `Dated notice found: - “北京大学2027年接收推荐免试研究生办法（校本部）” — docs/20260831123041610549.pdf — 2026-08-31 No separate 2027 预推免 notice appears. For 夏令营, only a navigation link “夏令营” to xly/index.htm, with no date/title in a notice list. Notice list page URL: tzgg/index.htm`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Also give the notice list page URL.", "url": "https://yjsy.zju.edu.cn/"}` → `No notice links about 2027年接收推荐免试研究生 / 推免生 / 预推免 are present in the provided content. The only visible text is the title “研究生教育管理信息系统” and the loading message “正在加载浙江大学研究生教育管理信息系统,请耐心等待.” Notice list page URL: not provided.`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Also give the notice list page URL.", "url": "https://yz.ustc.edu.cn/"}` → `Notice list page: `/column/182?num=-1` (also `/column/182` appears in the duplicate menu). The supplied text does not include individual notice URLs. 2027推免-related notices shown: - `09.08 2026` — “中国科学技术大学2027年推免生（推荐）名单公示” — URL not provided - `09.03 2026` — “中国科学技术大学2027年推免生接收办法” — URL not provided - `09.03 2026` — “ …[截断,原长504]`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Also give the notice list page URL.", "url": "https://yz.xjtu.edu.cn/"}` → `WebFetch completed, but the extraction model returned no text.`

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-11 13:55）

Search is unreliable for school names. I'll fetch each university's graduate-admission site directly.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Good:
- 北大: 北京大学2027年接收推荐免试研究生办法（校本部）PDF at docs/20260831123041610549.pdf, dated 2026-08-31. Need deadline.
- 中科大: 2027年推免生接收办法 09.03.2026 on /column/182. Need URL + deadline.
- 浙大: system page, no data.
- 西交: failed.

Let me fetch:
1. 北大 PDF: https://admission.pku.edu.cn/docs/20260831123041610549.pdf — WebFetch converts PDF? Possibly. Let me try.
2. 中科大 list: https://yz.ustc.edu.cn/column/182 — get notice URLs.
3. 西交 retry / other.
4. 哈工大.

Let me batch 4.

Note: WebFetch on PDF may work (converts to markdown). Let's try.

</details>

- 🔧 **WebFetch** `{"prompt": "Extract the exact application deadlines, system open/close dates, and any statement about timing for 2027 接收推荐免试研究生. Quote original Chinese sentences with dates.", "url": "https://admission.pku.edu.cn/docs/20260831123041610549.pdf"}` → ``

- 🔧 **WebFetch** `{"prompt": "List all notice items with titles, full URLs and dates, especially 2027年推免生接收办法 and 预选拔.", "url": "https://yz.ustc.edu.cn/column/182"}` → `URLs are not present in the supplied page content, so full URLs cannot be listed. The page repeats the same notice list twice; below is de-duplicated. | Title | Date | |---|---| | "中国科学技术大学2027年推免生（推荐）名单公示" | 2026-09-08 | | "中国科学技术大学2027年推免生接收办法" | 2026-09-03 | | "中国科学技术大学2027年推免生推荐办法" | 2026-09-03 | | "中国科学技术大学2027年工程 …[截断,原长361]`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Also give the notice list page URL.", "url": "https://yzb.hit.edu.cn/"}` → `Dated matching notices: - “哈尔滨工业大学关于2027年接收优秀应届本科毕业生免试攻读研究生报名的通知” — 2026-07-19 — https://yzb.hit.edu.cn/2026/0717/c22276a397589/page.htm - “2027年接收优秀应届本科毕业生免试攻读研究生报名通知汇总” — 2026-07-28 — https://yzb.hit.edu.cn/2026/0721/c22276a397947/page.htm Notice list page: https://yzb.hit.edu.cn/ssgg_22276/list.htm No dated “预推免” no …[截断,原长357]`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Also give the notice list page URL.", "url": "https://gs.whu.edu.cn/"}` → `No notices about **2027年接收推荐免试研究生 / 推免生 / 预推免** appear in the provided content. Notice list pages: - 招生通知公告: `tzgg/zs.htm` - 全部通知公告: `tzgg/qb.htm``

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Getting more URLs. Let me fetch:
- 哈工大 notice: https://yzb.hit.edu.cn/2026/0717/c22276a397589/page.htm → deadline
- 中科大: need individual URL. The page didn't give URLs. Try fetching /column/182 again? It said no URLs. Maybe the extraction missed. Let me try a different approach: the notice "中国科学技术大学2027年推免生接收办法" — search via Bing? Or fetch https://yz.ustc.edu.cn/ homepage (already did, gave dates but no URLs). Hmm. Maybe list page uses JS. Let me try the article URL pattern: yz.ustc.edu.cn/2026/0903/cXXXXaXXXXXX/page.htm — unknown.

Let me proceed and gather URLs for other schools; for 中科大 I'll mark 未核实 deadline but note notice exists.

Let me batch fetch:
1. 哈工大 notice page
2. 武大 tzgg/zs.htm list
3. 华科 gszs.hust.edu.cn/
4. 北理 yz.bit.edu.cn/

Go.

Also 西交 retry with list page maybe https://yz.xjtu.edu.cn/ failed; try http.

Let me include 西交 in place of one.

Batch:
1. https://yzb.hit.edu.cn/2026/0717/c22276a397589/page.htm
2. https://gs.whu.edu.cn/tzgg/zs.htm
3. https://gszs.hust.edu.cn/
4. https://yz.xjtu.edu.cn/index.htm

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "Extract exact application deadline date(s), system open/close dates, and whether still open. Quote original Chinese sentences containing dates.", "url": "https://yzb.hit.edu.cn/2026/0717/c22276a397589/page.htm"}` → `- 报名截止日期：文中未写明。 - 系统开放日期：原文称：“我校将于2026年7月20日起开通“推免生信息采集系统”，接受预计获得推免资格的应届本科毕业生报名。” - 系统关闭日期：文中未写明。 - 发布日：文末署“哈尔滨工业大学研究生院 2026年7月19日”。 - 另一处日期：“此项工作一般在十月底前完成，具体时间安排以各学院通知为准。”但该处指拟录取后的审核，不是申请截止。 - 是否仍开放：仅据此页无法判断，因为只有开通起始时间，没有截止或关闭时间。`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免.", "url": "https://gs.whu.edu.cn/tzgg/zs.htm"}` → `No notice links about **2027年接收推荐免试研究生 / 推免生 / 预推免** appear in the provided page content. The listed 招生 notices are for 2026 and earlier admissions matters (e.g., 博士、硕士、港澳台), with no 2027 推免/预推免 items.`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://gszs.hust.edu.cn/"}` → `公告通知列表页：`zsxx/ggtz.htm`（完整可拼为 `http://gszs.hust.edu.cn/zsxx/ggtz.htm`） 匹配通知： - “华中科技大学关于开展2027年接收推荐免试研究生（含直博生）预报名及复试工作安排的通知” — 2026-09-09 — `http://gszs.hust.edu.cn/info/1106/4142.htm` - “华中科技大学‘国家优秀中小学教师培养计划’2027年接收推荐免试硕士研究生工作细则” — 2026-09-09 — `http://gszs.hust.edu.cn/info/1106/4013.htm``

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yz.xjtu.edu.cn/index.htm"}` → `WebFetch completed, but the extraction model returned no text.`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

- 哈工大: system opened 2026-07-20, no deadline. 未核实.
- 华科: 华中科技大学关于开展2027年接收推荐免试研究生（含直博生）预报名及复试工作安排的通知 — 2026-09-09 — http://gszs.hust.edu.cn/info/1106/4142.htm → fetch for deadline. Likely still open or deadline soon.
- 西交: failed.

Let me batch:
1. 华科 notice 4142
2. 西交 retry alternate URL: https://yz.xjtu.edu.cn/ 
3. 天大 https://yzb.tju.edu.cn/
4. 厦大 https://gs.xmu.edu.cn/

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "Extract exact application deadline date(s), system open/close dates, whether still open. Quote original Chinese sentences containing dates.", "url": "http://gszs.hust.edu.cn/info/1106/4142.htm"}` → `- **系统开放/预报名开始日期**：仅明确为 **2026年9月9日**。 原文：“预报名开始时间：2026年9月9日” - **申请截止/系统关闭日期**：本页未给出统一截止日，明确由各院系自定。 原文：“预报名截止时间：各院系报名截止时间和具体要求，详见各院系发布的接收推免生工作细则。” 原文：“预报名阶段，院系可根据申请情况，自主确定接受预报名的截止时间，具体以院系复试细则通知为准，请有意者务必尽早报名。” - **目前是否仍开放**：仅凭本页无法判断，因为截止/关闭时间取决于各院系细则；需查看具体院系通知。`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yz.xjtu.edu.cn/"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yzb.tju.edu.cn/"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://gs.xmu.edu.cn/"}` → `No notice links for “2027年接收推荐免试研究生”、“推免生” or “预推免” appear in the provided content. Visible list/entry links: - “资讯中心” — https://gs.xmu.edu.cn/zxzx.htm - “信息动态” — https://gs.xmu.edu.cn/xxfw/xxdt.htm - “招生信息” — https://zs.xmu.edu.cn/ No matching title, URL, or date was shown for those topics.`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Some pages fail. Let me continue with other schools and retry.

Let me try a different pattern: many universities post 预推免 on the 研究生院 "招生" list. Let me fetch more homepages:
- 西交: try https://yz.xjtu.edu.cn/zsxx/tms.htm? unknown. Retry homepage.
- 天大: retry https://yzb.tju.edu.cn/ (failed).
- 东南: https://yzb.seu.edu.cn/
- 北理: https://yz.bit.edu.cn/
- 川大: https://yz.scu.edu.cn/
- 电子科大: https://yz.uestc.edu.cn/
- 重庆大学: https://yz.cqu.edu.cn/
- 湖南大学: https://yjsy.hnu.edu.cn/
- 中南: https://gra.csu.edu.cn/
- 大连理工: https://gs.dlut.edu.cn/
- 吉大: https://yjsy.jlu.edu.cn/
- 兰大: https://yjs.lzu.edu.cn/
- 西北工大: https://yzb.nwpu.edu.cn/
- 西北农林: https://yz.nwsuaf.edu.cn/
- 中国农大: https://yz.cau.edu.cn/
- 北师大: https://yzb.bnu.edu.cn/
- 中央民大: https://yz.muc.edu.cn/
- 中国海洋: https://yz.ouc.edu.cn/
- 华东师大: https://yjszs.ecnu.edu.cn/
- 国防科大: https://yz.nudt.edu.cn/
- 复旦: gsao.fudan.edu.cn (already have notice, no deadlines)
- 上交: https://yzb.sjtu.edu.cn/ (have 预推免 system link)
- 南大: yzb.nju.edu.cn (notice, no deadline)

Let me batch 4 at a time. Given failures are ~50%, I'll keep going.

Batch: 东南, 北理, 川大, 电子科大.
URLs:
东南: https://yzb.seu.edu.cn/
北理: https://yz.bit.edu.cn/
川大: https://yz.scu.edu.cn/
电子科大: https://yz.uestc.edu.cn/

Go.

Also, to be efficient, maybe I should fetch the school sites' list pages found: 武大 tzgg/zs.htm had nothing; maybe the 推免 notices are under a different list. 

Let me also try a broad aggregator search once more later.

Proceeding.

</details>

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yzb.seu.edu.cn/"}` → `列表页 URL：http://yzb.seu.edu.cn/6676/list.htm 相关通知： - “东南大学2027年推免专项报名通知” — 2026-08-31 — http://yzb.seu.edu.cn/2026/0831/c6676a580992/page.htm - “东南大学部分学院2027年接收推荐免试研究生报名通知（第二批）” — 2026-08-28 — http://yzb.seu.edu.cn/2026/0828/c6676a580682/page.htm - “东南大学各院、系（所）2027年接收推荐免试研究生报名通知汇总” — 2026-07-07 — http://yzb.seu.edu.cn/2 …[截断,原长462]`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yz.bit.edu.cn/"}` → `No notice links for 2027年接收推荐免试研究生 / 推免生 / 预推免 appear in the provided content, so no titles, URLs, or dates can be listed. A notice-list page URL is also not present. The only URLs shown are role entry links: https://yz.bit.edu.cn/yzgl and https://yz.bit.edu.cn/yzbm.`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yz.scu.edu.cn/"}` → `Relevant 2027 推免/免试 notices from 公告通知: 1. “2027年‘四川大学-南方电网’联合培养项目推荐免试研究生招生简章” — `/zsxx/Details/1b2831ad-f372-4084-8462-3b739189cf94` — 2026/9/10 2. “四川大学2027年推荐免试研究生招生章程” — `/zsxx/Details/0f4bc2fc-e7d8-455d-b0e3-8ad680196df1` — 2026/9/8 3. “四川大学2027年各招生院系所接收优秀应届本科毕业生免试攻读研究生（含直博生）的通知” — `/zsxx/Details/08ab7f58-bed0-4f46 …[截断,原长390]`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yz.uestc.edu.cn/"}` → `相关条目在“重要通知”栏，列表页：`index/zytz.htm` 1. “转发（持续更新）：各学院2027年接收优秀应届本科毕业生免试攻读研究生...” URL：`info/1081/5576.htm` 日期：2026.09.04 2. “电子科技大学接收2027年优秀应届本科毕业生免试攻读研究生（含直博生）...” URL：`info/1081/5939.htm` 日期：2026.09.04 页面中未见单独标注为“预推免”的其他通知条目。`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Excellent. Now I have:
- 东南大学: 2027 推免专项报名通知 2026-08-31; 第二批 2026-08-28 → fetch for deadlines. Likely still open (第二批).
- 川大: 2027年推荐免试研究生招生章程 2026-09-08; 各院系所接收通知 2026-09-08 → likely still open.
- 电子科大: 接收2027年免试 2026-09-04 → fetch.
- 北理: homepage didn't show; maybe need list page.

Let me fetch deadlines for 东南(专项报名 580992 + 第二批 580682), 川大章程, 电子科大.

Batch of 4:
1. http://yzb.seu.edu.cn/2026/0831/c6676a580992/page.htm
2. http://yzb.seu.edu.cn/2026/0828/c6676a580682/page.htm
3. https://yz.scu.edu.cn/zsxx/Details/0f4bc2fc-e7d8-455d-b0e3-8ad680196df1
4. https://yz.uestc.edu.cn/info/1081/5939.htm

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "Extract exact application deadline date(s), system open/close dates, whether still open. Quote original Chinese sentences containing dates.", "url": "http://yzb.seu.edu.cn/2026/0831/c6676a580992/page.htm"}` → `- 研究生支教团类别：开放/截止为“研支团专项：8月31日17:00 —9月1日下午17:00”。 - 其他专项类别：开放/截止为“其他专项：9月1日上午10:00 —9月4日下午17:00”。 - 上述日期行未写年份；通知标注“发布时间：2026-08-31”，据此应指 2026 年。 是否仍开放：网页未提供实时状态。若按系统当前日期 2026-05-09 对照，这些时段尚未开始；仅凭该页面本身无法确认实时是否开放。`

- 🔧 **WebFetch** `{"prompt": "Extract exact application deadline date(s), system open/close dates, whether still open. Quote original Chinese sentences containing dates.", "url": "http://yzb.seu.edu.cn/2026/0828/c6676a580682/page.htm"}` → `Based on the page: - 土木工程学院: application period is “8月28日中午12:00-9月1日中午12:00” — deadline Sep 1, 2026, noon. - 材料科学与工程学院: application period is “8月28日中午12:00-9月3日中午12:00” — deadline Sep 3, 2026, noon. - Year inference: “发布时间：2026-08-28” indicates the listed dates are in 2026. - No separate system open/close dates are pr …[截断,原长492]`

- 🔧 **WebFetch** `{"prompt": "Extract exact application deadline date(s), system open/close dates, whether still open. Quote original Chinese sentences containing dates.", "url": "https://yz.scu.edu.cn/zsxx/Details/0f4bc2fc-e7d8-455d-b0e3-8ad680196df1"}` → `Based only on the provided page: - **Application deadline:** No exact deadline date is given. It only says formal registration/acceptance must be done in the prescribed period: “推免生正式报名和录取工作须在规定的时间内通过全国推免服务系统（网址：https://yz.chsi.com.cn/tm）进行。” - **System open/close dates:** Not specified. The page says: “全国推免服务系统的开通时间以教 …[截断,原长639]`

- 🔧 **WebFetch** `{"prompt": "Extract exact application deadline date(s), system open/close dates, whether still open. Quote original Chinese sentences containing dates.", "url": "https://yz.uestc.edu.cn/info/1081/5939.htm"}` → `- **申请截止日期**：未给出具体日期。页面仅要求“在规定时间内填写报名信息”，具体截止时间需看各学院通知。 - **系统开放/关闭日期**：未给出。页面只提到通过“全国推荐免试攻读研究生(免初试、转段)信息公开管理服务系统”发送待录取通知。 - **是否仍开放**：无法仅凭本页判断，因为缺少具体时间窗口。 - **页面中出现的相关日期**：“发布时间：2026-09-04”；“2026年9月4日”。`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Findings:
- 东南: 推免专项 windows ended 9/4; 第二批 ended 9/1-9/3. So 东南 likely ALREADY CLOSED (all listed deadlines < 9/11). Mark as 已截止 (based on available notices). But there may be a 第三批. Note.
- 川大: no deadline, 未核实.
- 电子科大: no deadline, 未核实.

Let me keep collecting. Remaining: 复旦(need院系 deadlines), 上交, 南大, 浙大, 中科大, 西交, 北大(deadline), 清华(deadline), 人大(not requested), 天大, 南开, 武大, 华科(got), 中大(got), 华南理工(got: 9/15), 川大(got), 电子科大(got), 重庆大学, 湖南大学, 中南, 大连理工, 东北大学(got), 吉大, 兰大, 西北工大, 西北农林, 中国农大, 北师大, 中央民大, 中国海洋, 山大(got: 单位自定), 厦大, 华东师大, 国防科大, 同济(got), 东南(got), 北航, 北理, 哈工大(got).

Let me batch more homepages: 北航, 南开, 重庆大学, 湖南大学.

URLs:
北航: https://yzb.buaa.edu.cn/
南开: https://yzb.nankai.edu.cn/
重庆大学: https://yz.cqu.edu.cn/
湖南大学: https://yjsy.hnu.edu.cn/

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yzb.buaa.edu.cn/"}` → `符合2027年推免主题的通知： - “北航各学院接收推免攻读2027年研究生（含博士）相关通知（2026年9月10日更新）” — `info/1036/3610.htm` — 09-05 - “北航接收推荐免试攻读2027年研究生（含博士）复试考场规则” — `info/1036/3607.htm` — 09-03 - “北航接收推荐免试攻读2027年研究生（含博士）诚信复试承诺书” — `info/1036/3604.htm` — 09-03 - “北航接收推荐免试攻读2027年研究生（含博士）相关要求” — `info/1036/3601.htm` — 09-03 通知列表页：`zxsd/dtxx.htm`（“动态消息”更多链接 …[截断,原长322]`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yzb.nankai.edu.cn/"}` → `未找到与“2027年接收推荐免试研究生 / 推免生 / 预推免”相关的通知链接（无标题、URL、日期）。 相关通知列表入口为“推荐免试”：`/2583/list.htm`。`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yz.cqu.edu.cn/"}` → `相关公告仅找到 1 条： - 日期：2026-06 - 标题："重庆大学2027年推荐免试研究生（含直博生）招生预报名公告.." - 链接：https://yz.cqu.edu.cn/news/2026-06/2553.html 通知列表页（首页“通知公告”栏目）：https://yz.cqu.edu.cn/index.html`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yjsy.hnu.edu.cn/"}` → ``

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

- 北航: 北航各学院接收推免攻读2027年研究生相关通知 (2026年9月10日更新) → very fresh, likely still open. Fetch info/1036/3610.htm.
- 南开: /2583/list.htm → fetch list.
- 重庆大学: 2027 推免招生预报名公告, 2026-06, https://yz.cqu.edu.cn/news/2026-06/2553.html → fetch deadline.
- 湖南大学: domain wrong. Try https://yjsy.hnu.edu.cn/ failed DNS. Maybe http://yjsy.hnu.edu.cn or 研究生院 https://gra.hnu.edu.cn/. Actually 湖南大学研究生院 = https://yjsy.hnu.edu.cn/ maybe blocked. Try https://gra.hnu.edu.cn/.

Batch:
1. https://yzb.buaa.edu.cn/info/1036/3610.htm
2. https://yzb.nankai.edu.cn/2583/list.htm
3. https://yz.cqu.edu.cn/news/2026-06/2553.html
4. https://gra.hnu.edu.cn/

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "List each 学院 notice with title, URL and its application deadline date. Quote Chinese sentences with dates.", "url": "https://yzb.buaa.edu.cn/info/1036/3610.htm"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生.", "url": "https://yzb.nankai.edu.cn/2583/list.htm"}` → `根据所给页面，没有 2027 年接收推免研究生的通知。 现有相关列表仅含 2026 年两条： - “南开大学接收2026年推荐免试（含直博）生招生工作办法” — `/2025/0914/c2583a577579/page.htm` — 2025-09-14 - “南开大学2026年接收优秀应届本科毕业生免试攻读研究生预报名的通知” — `/2025/0706/c2583a574948/page.htm` — 2025-07-07`

- 🔧 **WebFetch** `{"prompt": "Extract exact application deadline date(s), system open/close dates, whether still open. Quote original Chinese sentences containing dates.", "url": "https://yz.cqu.edu.cn/news/2026-06/2553.html"}` → `- 统一系统开放：2026年6月23日10:00；统一关闭/截止：2026年9月30日18:00。原文：“重庆大学研究生招生服务系统开放时间为2026年6月23日10:00至2026年9月30日18:00。” - 各学院具体起止时间可能不同，应以系统内设置及学院通知为准。原文：“各学院接收推免预报名的具体起止时间，请以“重庆大学研究生招生服务系统”内各学院设置和学院发布的相关通知为准。” - 是否仍开放：按当前日期2026年5月7日看，尚未开放；预计到2026年6月23日10:00才开放，至2026年9月30日18:00关闭。`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://gra.hnu.edu.cn/"}` → `- 招生信息列表页：`index/zsxx.htm` 相关通知： - “湖南大学2027年接收推荐免试研究生（含直博...” — `info/1075/10560.htm` — 2026-08-28 另：报名系统中有“推免生预报名”链接：`https://yjszsxt.hnu.edu.cn/zsxt/tmsgl/default.aspx`，但这不是通知，且无日期。`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Excellent!
- 重庆大学: system open 2026-06-23 10:00 to 2026-09-30 18:00 → OPEN (deadline 9/30). Strong evidence! (Note the extraction model said "current date 2026-05-07" — it's hallucinating the date; ignore.)
- 湖南大学: notice info/1075/10560.htm 2026-08-28 → fetch deadline; system link.
- 南开: no 2027 notice found on that list (only 2026). Maybe not yet published or elsewhere. Mark 未找到.
- 北航: extraction failed; retry.

Let me batch:
1. 湖南大学 notice https://gra.hnu.edu.cn/info/1075/10560.htm
2. 北航 retry https://yzb.buaa.edu.cn/info/1036/3610.htm
3. 大连理工 https://gs.dlut.edu.cn/
4. 中南 https://gra.csu.edu.cn/

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "Extract exact application deadline date(s), system open/close dates, whether still open. Quote original Chinese sentences containing dates.", "url": "https://gra.hnu.edu.cn/info/1075/10560.htm"}` → `- 明确申请截止日期：页面未给出具体日期。原文仅写：“报名截止时间以学院通知为准。” - 预报名系统起始：原文称：“申请人8月28日起可登录湖南大学接收推免生报名信息采集系统，填写有关信息、上传附件材料并提交申请。”未给关闭日期。 - 国家系统开放/关闭：原文称：“服务系统开放时间请关注中国研究生招生信息网相关公告。”无具体开闭日期。 - 通知自身日期：“发布时间：2026-08-28” - 是否仍开放：仅凭该页无法确认。它没有统一截止日或关闭日，需看各学院后续说明及中国研招网公告。`

- 🔧 **WebFetch** `{"prompt": "List each 学院 notice with title, URL and its application deadline date. Quote Chinese sentences with dates.", "url": "https://yzb.buaa.edu.cn/info/1036/3610.htm"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://gs.dlut.edu.cn/"}` → `- “关于大连理工大学各院系接收2027年推荐免试研究生预报名陆续...” — URL: `info/1173/51492.htm` — 日期: 2026-07-14 - 通知列表页（招生）: `http://gs.dlut.edu.cn/yjszs.htm``

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://gra.csu.edu.cn/"}` → `在提供的内容中，未发现关于“2027年接收推荐免试研究生 / 推免生 / 预推免”的通知链接。 研究生院通知列表页链接为：`yjsytz.htm`（页面中“MORE +”指向该地址）。若按站点域名推断，也可写为：`https://gra.csu.edu.cn/yjsytz.htm`。`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Continue. Remaining schools to check: 大连理工 (notice found info/1173/51492.htm — "陆续..." no deadline), 中南 (list yjsytz.htm), 吉大, 兰大, 西北工大, 西北农林, 中国农大, 北师大, 中央民大, 中国海洋, 华东师大, 国防科大, 浙大, 中科大, 西交, 上交, 复旦(院系), 南大, 北大(deadline), 清华(deadline), 天大, 武大, 北理, 厦大, 北航.

Let me prioritize deadlines for schools with open-ish notices: 北大 PDF (can't fetch pdf), 北航 (retry), 中科大, 西交, 上交.

Let me also get 中南 list, 吉大, 兰大.

Batch:
1. https://gra.csu.edu.cn/yjsytz.htm (中南)
2. https://yjsy.jlu.edu.cn/ (吉大)
3. https://yjs.lzu.edu.cn/ (兰大)
4. https://yzb.nwpu.edu.cn/ (西北工大)

Go.

Also try 北航 notice via a different phrasing later.

</details>

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免.", "url": "https://gra.csu.edu.cn/yjsytz.htm"}` → `No notice links about 2027年接收推荐免试研究生、推免生或预推免 appear in the provided content.`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yjsy.jlu.edu.cn/"}` → `Based on the provided content, there are **no notice links** about **2027年接收推荐免试研究生 / 推免生 / 预推免**. 通知公告列表页 URL：`tzgg.htm``

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yjs.lzu.edu.cn/"}` → `The server returned HTTP 412 Precondition Failed. The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yzb.nwpu.edu.cn/"}` → `- “西北工业大学2027年接收推荐免试研究生预报名的通知” | `info/1174/10478.htm` | 2026-09-04 Notice list page: `new/sszs/zsgg.htm`（硕士招生公告） There is also a “推免生预报名” application entry, but it is not a dated notice.`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

- 西北工大: notice info/1174/10478.htm 2026-09-04 → fetch deadline.
- 中南/吉大: nothing on homepage lists (may need deeper).
- 兰大: 412 blocked.

Batch:
1. https://yzb.nwpu.edu.cn/info/1174/10478.htm
2. https://yzb.buaa.edu.cn/info/1036/3610.htm (retry)
3. https://yzb.nankai.edu.cn/ (maybe 2027 notice elsewhere; skip) → instead 北师大 https://yzb.bnu.edu.cn/
4. https://yz.ouc.edu.cn/ (中国海洋)

Go.

Actually 北师大 grad admission: https://yz.bnu.edu.cn/ or https://yzb.bnu.edu.cn/. Let me try https://yz.bnu.edu.cn/.

Let me do:
1. 西北工大 notice
2. 北航 retry
3. https://yz.bnu.edu.cn/
4. https://yz.ouc.edu.cn/

</details>

- 🔧 **WebFetch** `{"prompt": "Extract exact application deadline date(s), system open/close dates, whether still open. Quote original Chinese sentences containing dates.", "url": "https://yzb.nwpu.edu.cn/info/1174/10478.htm"}` → `- The pre-registration window in the notice is quoted as: “预报名时间：9月4日15:00—9月20日18:00，具体时间以各学院公布为准。” - Therefore the listed system opening is “9月4日15:00”; the listed deadline/close is “9月20日18:00”. Each college’s schedule may differ. - Page publication timestamp: “2026年09月04日 09:27”. - Whether it is still open: the pag …[截断,原长457]`

- 🔧 **WebFetch** `{"prompt": "List each 学院 notice with title, URL and its application deadline date. Quote Chinese sentences with dates.", "url": "https://yzb.buaa.edu.cn/info/1036/3610.htm"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yz.bnu.edu.cn/"}` → `通知列表页： - 硕士招生公告：https://yz.bnu.edu.cn/list/master - 博士招生公告：https://yz.bnu.edu.cn/list/doctor 2027年推荐免试相关公告（页面未显示发布日期）： - “北京师范大学各院（系）2027年推荐免试综合考核实施细则（持续更新中）” https://yz.bnu.edu.cn/detail/46676d55-68bc-4a9c-946a-f8c978939c05 日期：未显示 - “北京师范大学关于接收2027年‘国优计划’推荐免试研究生的通知” 硕士公告：https://yz.bnu.edu.cn/detail/0b4b344f-b5c3-4ecc …[截断,原长619]`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yz.ouc.edu.cn/"}` → `- “中国海洋大学2027年接收推荐免试研究生预报名通知” — 2026-07-23 — /2026/0723/c31626a534920/page.htm 通知公告列表页：/tzgg/list.htm`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Great:
- 西北工大: 预报名 9月4日15:00—9月20日18:00 → OPEN (deadline 9/20). Strong.
- 北师大: notices exist, no dates shown. Need to fetch one for deadline. URL: https://yz.bnu.edu.cn/detail/be0e6268-0bfd-4a34-aa31-e72207bf2577 (招生录取工作办法) — fetch.
- 中国海洋: 2027 预报名通知 2026-07-23 → fetch for deadline.
- 北航: retry.

Batch:
1. https://yz.bnu.edu.cn/detail/be0e6268-0bfd-4a34-aa31-e72207bf2577
2. https://yz.ouc.edu.cn/2026/0723/c31626a534920/page.htm
3. https://yzb.buaa.edu.cn/info/1036/3610.htm (retry) — maybe use the other 北航 notice info/1036/3601.htm (相关要求)
4. https://yjszs.ecnu.edu.cn/ (华东师大)

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "Extract exact application deadline date(s), system open/close dates, whether still open. Quote original Chinese sentences containing dates.", "url": "https://yz.bnu.edu.cn/detail/be0e6268-0bfd-4a34-aa31-e72207bf2577"}` → `本页未载明具体申请截止日期，也未载明系统开放或关闭日期；因此仅凭本页无法判断是否仍开放。相关原句： - “各院（系）的网上申请截止日期在网上申请系统公告，截止日期可能会提前或推后，请注意查阅。” - “所有申请人（包括夏令营营员和我校本科生）于规定时间内登录我校推免申请系统” - “接收为硕士或博士的申请人，须在院（系）规定时间内，登录全国推免服务系统” - “规定时间内未确认待录取通知者视为自动放弃拟录取资格。” 含日期的原句： - “发布时间：2026-09-02 阅读 109113 次” - “北京师范大学2027年推荐免试硕士／博士研究生招生录取工作办法” - “若2027招生年度上级教育主管部门出台新的招生政策，我校将做相 …[截断,原长371]`

- 🔧 **WebFetch** `{"prompt": "Extract exact application deadline date(s), system open/close dates, whether still open. Quote original Chinese sentences containing dates.", "url": "https://yz.ouc.edu.cn/2026/0723/c31626a534920/page.htm"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "Extract any application deadline dates or application period mentioned. Quote Chinese sentences with dates.", "url": "https://yzb.buaa.edu.cn/info/1036/3601.htm"}` → `未提及具体的申请截止日期或申请时间段。页面日期为“2026-09-03”，但这不是申请截止日期；申请时间由各学院安排：“各学院可根据申请情况分批次组织相关工作，具体见相关学院网站的通知。” 另有两处带2027年的要求，但属于入学/保留资格事项，不是申请截止日期：“2027年入学报到前未取得本科毕业证书。”以及“若想保留入学资格，且不能在2027年秋季开学时报到”。`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yjszs.ecnu.edu.cn/"}` → `相关条目： 1. “华东师范大学2027年接收优秀应届本科毕业生免试攻读研究生（含本科直博）工作办法” — 2026-09-04 — http://yjszs.ecnu.edu.cn/d3/d1/c43264a775121/page.htm 2. “华东师范大学2027年各院系接收优秀应届本科毕业生免试攻读研究生（含本科直博）预报名通知（陆续更新）” — 2026-07-24 — http://yjszs.ecnu.edu.cn/c3/cb/c43264a771019/page.htm 3. “关于华东师范大学2027年接收优秀应届本科毕业生免试攻读研究生（含本科直博） 预报名的通知（增加中法联培项目）” — 2026-07-24  …[截断,原长726]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

- 北师大: no deadline, per院系. 未核实.
- 中国海洋: retry.
- 北航: no fixed deadline, per学院. 未核实.
- 华东师大: 预报名通知(陆续更新) 2026-07-24 → fetch the 陆续更新 page to get院系 deadlines. URL http://yjszs.ecnu.edu.cn/c3/cb/c43264a771019/page.htm

Batch:
1. 华东师大 预报名陆续更新 http://yjszs.ecnu.edu.cn/c3/cb/c43264a771019/page.htm
2. 中国海洋 retry https://yz.ouc.edu.cn/2026/0723/c31626a534920/page.htm
3. 大连理工 notice https://gs.dlut.edu.cn/info/1173/51492.htm
4. 中科大 search for 接收办法 URL — try fetching https://yz.ustc.edu.cn/column/182 again won't give URLs. Alternative: try direct guess? Skip; instead fetch 西交 via different path https://yz.xjtu.edu.cn/ retry.

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "List each 院系预报名 notice with title, URL and application deadline date. Quote Chinese sentences with dates.", "url": "http://yjszs.ecnu.edu.cn/c3/cb/c43264a771019/page.htm"}` → `页面内容只列通知链接，未给出各通知的申请截止日期；下表“截止日期”均标为“未列出”。页面可见日期信息有：“发布时间：2026-07-24浏览次数：40356”。总标题为：“华东师范大学2027年各院系接收优秀应届本科毕业生免试攻读研究生（含本科直博）预报名通知（陆续更新）”。 | 标题 | URL | 申请截止日期 | |---|---|---| | "101 中国语言文学系" | https://zhwx.ecnu.edu.cn/c3/b6/c28583a770998/page.htm | 未列出 | | "102 历史学系" | https://history.ecnu.edu.cn/c3/c1/c33433a771009/pa …[截断,原长453]`

- 🔧 **WebFetch** `{"prompt": "Extract exact application deadline date(s), system open/close dates. Quote original Chinese sentences containing dates.", "url": "https://yz.ouc.edu.cn/2026/0723/c31626a534920/page.htm"}` → `- **预报名开放/截止：** 7月23日开放，9月14日17点截止。 原文：“7月23日—9月14日17点，考生登录“中国海洋大学研究生考生服务平台”（[点击进入](https://stuouc.molstone.cn/)）进行报名，……” - **教育部推免服务系统：** 页面未给出具体开放/关闭日期，仅说明： “推免服务系统开放时间请关注中国研究生招生信息网相关公告。” - **页面/通知日期：** “发布时间：2026-07-23”。`

- 🔧 **WebFetch** `{"prompt": "List each 院系预报名 notice with title, URL and application deadline date. Quote Chinese sentences with dates.", "url": "https://gs.dlut.edu.cn/info/1173/51492.htm"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yz.xjtu.edu.cn/index.htm"}` → `“推免生”列表页：`index/tms.htm` 相关 2027 年条目： - “西安交通大学2027年推荐免试研究生招生章程” — `xjtutjms_2027.pdf` — 2026-09-02 - “西安交通大学各学院（部、中心）2027年招收推免生实施细则” — `info/1082/4399.htm` — 2026-09-03（另有 `info/1083/4400.htm`、`info/1086/4391.htm`） - “西安交通大学2027年‘工程硕博士培养改革专项试点’ 研究生（全日制）招生简章” — `info/1082/4396.htm` — 2026-09-07（另有 `info/1083/4397.htm`、 …[截断,原长362]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

- 中国海洋: 7月23日—9月14日17点 → OPEN (deadline 9/14). Strong!
- 西交: 各学院实施细则 info/1082/4399.htm → fetch for deadlines. Also 招生章程 pdf.
- 华东师大: no per-院系 dates on summary; individual dept pages have them. 未核实 (but likely some open).
- 大连理工: retry.

Batch:
1. https://yz.xjtu.edu.cn/info/1082/4399.htm
2. https://gs.dlut.edu.cn/info/1173/51492.htm retry
3. 中国农大 https://yz.cau.edu.cn/
4. 中央民大 https://yz.muc.edu.cn/

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "List each 学院 notice with title, URL and application deadline date. Quote Chinese sentences with dates.", "url": "https://yz.xjtu.edu.cn/info/1082/4399.htm"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List each 院系预报名 notice with title, URL and application deadline date. Quote Chinese sentences with dates.", "url": "https://gs.dlut.edu.cn/info/1173/51492.htm"}` → `提供内容中仅见一个总通知，标题为“关于大连理工大学各院系接收2027年推荐免试研究生预报名陆续开放的通知”；其URL未在正文中给出。除“（主校区）控制科学与工程”外，各院系行没有单独标题或URL。以下为各单位及表中时间引文（含截止日期）： 1. “（主校区）数学科学学院” — “2026年7月14日00：00--9月15日12：00” 2. “（主校区）物理学院” —`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yz.cau.edu.cn/"}` → `相关通知： 1. “关于某985高校2027年接收优秀应届本科毕业生免试攻读研究生报名的通...” | 2026-07-14 | https://mp.weixin.qq.com/s/Dg2gtsrnbZR8ITomDN4ZoQ 2. “某985高校面向本校2027年推免生开展工程硕博士...” | 2026-08-28 | /art/2026/8/28/art_41742_1134422.html 3. “某985高校各院系2027年接收推荐免试研究生工作...” | 2026-07-20 | /art/2026/7/20/art_41742_1123106.html 通知列表页： - “通知公告”：/col/col41740/i …[截断,原长378]`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yz.muc.edu.cn/"}` → ``

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

- 大连理工: 数学科学学院 2026-07-14 00:00 -- 9月15日12:00 → OPEN. Other院系 cut off; but at least some院系 deadline 9/15. Good. (Note: the extraction gave only partial. I can cite the summary page 51492 with math dept 9/15.)
- 中国农大: notices found; need deadline. /art/2026/7/20/art_41742_1123106.html (各院系) and /art/2026/8/28/... Let me fetch.
- 中央民大: DNS fail. Skip (mark 未核实/未能访问).
- 西交: retry.

Batch:
1. https://yz.xjtu.edu.cn/info/1082/4399.htm retry
2. https://yz.cau.edu.cn/art/2026/7/20/art_41742_1123106.html
3. 中国海洋 done. 
3. https://yz.cau.edu.cn/art/2026/8/28/art_41742_1134422.html
4. 国防科大 https://yz.nudt.edu.cn/

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "List each 学院 notice with title, URL and application deadline date. Quote Chinese sentences with dates.", "url": "https://yz.xjtu.edu.cn/info/1082/4399.htm"}` → `页面可见日期`

- 🔧 **WebFetch** `{"prompt": "List each 院系 notice with title, URL and application deadline date. Quote Chinese sentences with dates.", "url": "https://yz.cau.edu.cn/art/2026/7/20/art_41742_1123106.html"}` → `提供的页面只列出各院系链接及URL，未给出各通知的申请截止日期。页面标题引用： “某985高校各院系2027年接收推荐免试研究生工作实施细则（陆续更新中）” 页面发布信息引用： “发布日期：2026-07-20” | 标题（仅页面链接文字） | URL | 申请截止日期 | |---|---|---| | “301农学院” | https://cab.cau.edu.cn/art/2026/7/16/art_48176_1122696.html | 未在提供内容中给出 | | “302生物学院” | https://cbs.cau.edu.cn/art/2026/7/21/art_8729_1123189.html | 未在提供内容 …[截断,原长2041]`

- 🔧 **WebFetch** `{"prompt": "Extract exact application deadline date(s), system open/close dates. Quote original Chinese sentences containing dates.", "url": "https://yz.cau.edu.cn/art/2026/8/28/art_41742_1134422.html"}` → `文中未给出具体申请截止日，也未列出系统开放/关闭日期；仅用“规定时间内”表述： - “符合条件的学生应于规定时间内在学校系统中报名，并上传相关证明材料。” - “须在于规定时间内在教育部推免服务系统中填报某985高校。” 可确认的日期为文件发布/落款日期：“发布日期：2026-08-28”；“2026年8月28日”。`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yz.nudt.edu.cn/"}` → ``

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

- 中国农大: per-院系 notices no dates in summary; individual pages would have. 未核实.
- 国防科大: DNS fail. 未核实.
- 西交: retry failed again.

Let me now check the remaining important ones: 上交 (system), 复旦 (院系), 浙大, 中科大, 南大 (deadline), 北大 (deadline), 清华 (deadline), 天大, 武大, 北理, 厦大, 人大(not in list), 湖南大学(done 未核实), 中南, 吉大, 兰大, 西北农林.

Let me try direct URLs:
- 上交 预推免 system: http://ga.sjtu.edu.cn/zsgl/ytmgl/ — maybe a page with dates.
- 浙大: try https://grs.zju.edu.cn/ (cert expired) → try http://grs.zju.edu.cn/ or https://yjs.zju.edu.cn/
- 中科大: try to find article URL. Search non-RSS Bing for "中国科学技术大学2027年推免生接收办法".
- 北大 PDF can't be fetched.
- 清华 notice has no deadline (per method, deadline from 院系).
- 天大: retry https://yzb.tju.edu.cn/
- 武大: maybe notices under a 推免 column. Try https://gs.whu.edu.cn/tzgg/qb.htm
- 北理: https://yz.bit.edu.cn/yzbm (system). Notices maybe at https://yz.bit.edu.cn/tzgg or /index.htm
- 厦大: notice at zs.xmu.edu.cn maybe.
- 西北农林: https://yz.nwsuaf.edu.cn/

Let me batch:
1. http://ga.sjtu.edu.cn/zsgl/ytmgl/
2. https://grs.zju.edu.cn/  (may fail)
3. https://yzb.tju.edu.cn/ retry
4. https://yz.nwsuaf.edu.cn/

Go.

Actually, let me reconsider efficiency and time. I've done many rounds. The user asked at least 10 different keyword searches. I've done many Bing queries (though many failed). Let me do a few more generic searches to try to surface remaining schools, and finish with direct fetches.

Let me mix: 2 direct fetches + 2 generic search queries.

Search queries (non-RSS, generic phrases that worked):
- "接收推荐免试研究生 预报名" (worked) — reuse gives cached 10. 
- New: "推免生 预报名 通知" 
- "2027年推免 报名通知"
- "预推免 报名截止"

Let me try "预推免报名通知" and "2027级推免生 预报名".

Hmm, given reliability issues, direct fetch may be better.

Let me do batch:
1. http://ga.sjtu.edu.cn/zsgl/ytmgl/
2. https://yzb.tju.edu.cn/
3. https://yz.nwsuaf.edu.cn/
4. https://yz.bit.edu.cn/index.htm  (北理)

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "Extract any application open/close date, registration period, or notice about 2027 预推免. Quote Chinese text with dates.", "url": "http://ga.sjtu.edu.cn/zsgl/ytmgl/"}` → `No application open/close dates, registration periods, or 2027 预推免 notice appear in the provided content. The page only shows garbled navigation links and current-location text, with no date-bearing Chinese text to quote.`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yzb.tju.edu.cn/"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yz.nwsuaf.edu.cn/"}` → `Relevant notice in the provided content: - Title: “关于西北农林科技大学2027年招收推荐免试研究生预报名...” - Date shown: 102026-09 - URL: `/tzgg/efc5ad22976f45b595487499b6c39d8e.htm` Likely full URL: `https://yz.nwafu.edu.cn/tzgg/efc5ad22976f45b595487499b6c39d8e.htm` Notice list page URL: `/tzgg/index.htm` Likely full URL: `https://yz.nwafu.e …[截断,原长402]`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yz.bit.edu.cn/index.htm"}` → `No notice links about “2027年接收推荐免试研究生 / 推免生 / 预推免” are present in the provided content, and no notice list page URL is given. The only links shown are: - “教职工” → https://yz.bit.edu.cn/yzgl - “考 生” → https://yz.bit.edu.cn/yzbm`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

- 西北农林: 2027 预报名 notice, 2026-09-10 (10 2026-09?) → fetch deadline. URL https://yz.nwafu.edu.cn/tzgg/efc5ad22976f45b595487499b6c39d8e.htm
- 上交: no dates in system page.
- 天大: fail.
- 北理: no notices on homepage.

Batch:
1. https://yz.nwafu.edu.cn/tzgg/efc5ad22976f45b595487499b6c39d8e.htm
2. https://yzb.tju.edu.cn/ retry
3. 武大 https://gs.whu.edu.cn/tzgg/qb.htm
4. 厦大 https://zs.xmu.edu.cn/

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "Extract exact application deadline date(s), system open/close dates. Quote original Chinese sentences containing dates.", "url": "https://yz.nwafu.edu.cn/tzgg/efc5ad22976f45b595487499b6c39d8e.htm"}` → `- **系统开放/关闭**：2026年9月10日至9月20日 - **申请截止**：没有全校统一日期，各学院另行通知 - **原文引用**：“我校2027年招收推免生预报名系统将于2026年9月10日至9月20日向考生开放，各学院申报截止时间由学院通知为准。”`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yzb.tju.edu.cn/index.htm"}` → `未发现 2027 年接收推荐免试研究生、推免生或预推免相关通知链接；页面中的推免类通知集中在 2017/2018 年。 相关通知列表页 URL：`./xwzx/tkss_xw/`（“统考硕士”栏目）。 另可查看通用公告列表：`./xwzx/zxxx/`、`./xwzx/tztg/`。`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免.", "url": "https://gs.whu.edu.cn/tzgg/qb.htm"}` → `No matching notice links about “2027年接收推荐免试研究生 / 推免生 / 预推免” appear in the provided page content.`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://zs.xmu.edu.cn/"}` → `WebFetch completed, but the extraction model returned no text.`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

- 西北农林: system 2026-09-10 至 9-20 → OPEN (deadline 9/20). Strong.
- 天大: no 2027 notice found on homepage.
- 武大: nothing on that list.

Time to consolidate. But let me try a few more schools and get remaining deadlines: 清华, 北大, 复旦, 上交, 浙大, 中科大, 南大, 北理, 天大, 武大, 厦大, 中南, 吉大, 兰大, 中国农大, 华东师大, 国防科大, 中央民大.

For deadlines, the trend: many schools have 院系-specific deadlines. I have concrete deadlines for: 华南理工(9/15), 重庆大学(9/30), 中国海洋(9/14), 西北工大(9/20), 西北农林(9/20), 大连理工(some dept 9/15), 同济(mostly past, but "更新中"), 东南(past).

Let me try to get 中科大, 上交, 浙大, 复旦 details via targeted Bing searches (non-RSS) with specific notice titles, which may work better:
- "中国科学技术大学2027年推免生接收办法"
- "上海交通大学2027年推免生 预推免"
- "浙江大学2027年推免生"

Actually school-name queries failed. Hmm.

Let me instead fetch 上交 预推免公示/list: https://yzb.sjtu.edu.cn/xxgs/ytmgs ?
And 浙大: try https://grs.zju.edu.cn/ again (might work now) or http://grs.zju.edu.cn/.

Let me also fetch 中科大's notice list alternate: https://yz.ustc.edu.cn/column/182?num=-1 — same. Maybe the article URLs are like https://yz.ustc.edu.cn/article/xxxx. Let me fetch homepage https://yz.ustc.edu.cn/ and ask for full URLs.

Batch:
1. https://yz.ustc.edu.cn/ (ask for article URLs)
2. https://yzb.sjtu.edu.cn/xxgs/ytmgs (上交 预推免公示)
3. https://grs.zju.edu.cn/ retry
4. https://yz.bnu.edu.cn/ done. Instead 中南: https://gra.csu.edu.cn/yjsytz.htm returned none. Try https://gra.csu.edu.cn/zsgz.htm? unknown. Let me try https://yz.csu.edu.cn/.

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "Give the full article URLs (href) for the notices 中国科学技术大学2027年推免生接收办法 and 各学院2027年接收推免生通知. Quote the href attributes.", "url": "https://yz.ustc.edu.cn/"}` → `The provided page content lists the notice “中国科学技术大学2027年推免生接收办法,” but it does not include any `href` attributes or full article URLs. Also, “各学院2027年接收推免生通知” does not appear in the content above. Therefore, I cannot quote the requested hrefs from the given material.`

- 🔧 **WebFetch** `{"prompt": "List any notices with titles, URLs and dates about 2027 预推免.", "url": "https://yzb.sjtu.edu.cn/xxgs/ytmgs"}` → `根据所给内容，未发现标注“2027”的预推免通知，也没有日期信息。现有预推免相关入口仅为： - “预推免活动办法”：http://ga.sjtu.edu.cn/zsgl/ytmgl/ - “名单公示”：http://ga.sjtu.edu.cn/zsgl/xxgs/ytmfsmdgs.aspx - “结果公示”：http://ga.sjtu.edu.cn/zsgl/xxgs/ytmkhjggs.aspx 这些页面均未显示日期或“2027”年份。`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免.", "url": "https://grs.zju.edu.cn/"}` → ``

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yz.csu.edu.cn/"}` → `Found one relevant notice: - “中南大学关于2027年接收优秀应届本科毕业生免试攻读硕士研究生预报名的通知” — `info/1009/1528.htm` — 2026.08.28（页面显示日期） Notice list page URL(s) shown: `sszs/tzgg.htm`（硕士招生-通知公告）；also listed under `zxgg.htm`（最新公告更多）.`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

- 中南: notice info/1009/1528.htm 2026-08-28 → fetch deadline. Domain yz.csu.edu.cn (not gra.csu).
- 上交: entry "预推免活动办法" ga.sjtu.edu.cn/zsgl/ytmgl/ — no dates, but implies 预推免 ongoing.
- 浙大: cert expired.
- 中科大: homepage no hrefs extracted.

Let me fetch 中南 notice, and try to find 浙大/中科大/上交/北理/天大/武大/厦大/吉大/兰大 via other means.

Batch:
1. https://yz.csu.edu.cn/info/1009/1528.htm
2. 吉大: https://yjsy.jlu.edu.cn/tzgg.htm (list)
3. 兰大: https://yjs.lzu.edu.cn/ was 412. Try https://yz.lzu.edu.cn/ or http.
4. 北理: https://yz.bit.edu.cn/yzbm (system) — skip. Instead try 武大 推免 list: https://gs.whu.edu.cn/tzgg/zs.htm (done, nothing). Try https://gs.whu.edu.cn/ homepage again? Already nothing.
   Instead 厦大: https://zs.xmu.edu.cn/ retry.
   Let me do: https://zs.xmu.edu.cn/ retry.

Batch:
1. https://yz.csu.edu.cn/info/1009/1528.htm
2. https://yjsy.jlu.edu.cn/tzgg.htm
3. https://zs.xmu.edu.cn/
4. https://yz.lzu.edu.cn/

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "Extract exact application deadline date(s), system open/close dates. Quote original Chinese sentences containing dates.", "url": "https://yz.csu.edu.cn/info/1009/1528.htm"}` → `未公布统一的申请截止日期或系统关闭日期。 - 系统开始报名时间：原文称“8月28日开始可通过“中南大学推免生服务系统”进行网上报名。” - 截止时间：原文仅称“各二级单位报名截止时间详见二级单位官方通知。” - 教育部推免服务系统开放时间：原文称“推免服务系统开放时间请关注中国研究生招生信息网相关公告。” - 通知发布/落款日期：“发布时间：2026-08-28”；落款为“中南大学研究生招生办公室 2026年8月28日”。`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免.", "url": "https://yjsy.jlu.edu.cn/tzgg.htm"}` → `No matching notice links about 2027年接收推荐免试研究生、推免生或预推免 appear in the provided page content.`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://zs.xmu.edu.cn/"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yz.lzu.edu.cn/"}` → `The server returned HTTP 412 Precondition Failed. The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

I have enough for a substantial answer, but let me try to fill a few more: 清华, 北大, 复旦, 上交, 浙大, 中科大, 南大, 吉大, 兰大, 武大, 天大, 北理, 厦大, 华东师大, 中国农大, 国防科大, 中央民大, 湖南大学(done).

Let me do a couple more targeted attempts:

1. 清华: The 办法 (info/1024/3251.htm) had no deadline. Tsinghua 预推免 deadlines are per 院系. There may be a "各院系推免接收" page. Try https://yz.tsinghua.edu.cn/zxgg.htm to list all notices.
2. 北大: PDF unfetchable. Maybe there's an HTML page. Try https://admission.pku.edu.cn/tzgg/index.htm.
3. 复旦: 报名通知 page didn't show院系 deadlines; maybe attachments. Try 复旦 各院系 list: https://gsao.fudan.edu.cn/ (homepage listed items). 
4. 南大: notice had attachments (FAQ PDF). Per院系 deadlines unknown. Try 南大 各院系预报名汇总: maybe on yzb.nju.edu.cn homepage.
5. 中科大: try https://yz.ustc.edu.cn/column/182? — no URLs. Try guessing article URL via Bing search "中科大 2027 推免生接收办法".

Let me also try 天大 via 研招网 list: https://yzb.tju.edu.cn/xwzx/zxxx/ and 武大 homepage.

Let me do batch:
1. https://yz.tsinghua.edu.cn/zxgg.htm
2. https://admission.pku.edu.cn/tzgg/index.htm
3. https://yzb.nju.edu.cn/
4. https://gsao.fudan.edu.cn/

Go.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "Confirm working search endpoint (Bing non-RSS + generic phrase queries)", "priority": "high", "status": "completed"}, {"content": "Collect 2027 预推免/推免 notices from 985 grad-school sites", "priority": "high", "status": "completed"}, {"content": "Fill remaining schools (清华/北大/复旦/上交/浙大/中科大/南大/吉大/兰大/武大/天大/北理/厦大)", "priority": "high", "status": "in_progress"} …[截断,原长412]` → `{"oldTodos":[{"content":"Confirm working search endpoint (Bing non-RSS + generic phrase queries)","status":"completed","priority":"high"},{"content":"Search site: queries across 985 grad-school domains for 2027 预推免/推免 notices","status":"in_progress","priority":"high"},{"content":"Fetch each notice page to extract exact …[截断,原长986]`

- 🔧 **WebFetch** `{"prompt": "List all notices (title + URL + date), especially 2027 推免/免试.", "url": "https://yz.tsinghua.edu.cn/zxgg.htm"}` → `以下为页面可见的第一页公告（页面显示“共96条”）： - 2026-07-03 — “清华大学2027年接收推荐免试研究生办法” — https://yz.tsinghua.edu.cn/info/1024/3251.htm - 2026-06-30 — “清华大学2027年博士研究生招生专业目录_推荐免试” — https://yzbm.tsinghua.edu.cn/publish/s01/s0103/detail/2ede1fca-d9a0-407a-9d68-3475494848b7/2 - 2026-06-30 — “清华大学2027年硕士研究生招生专业目录_推荐免试” — https://yzbm.tsinghua.ed …[截断,原长1335]`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免.", "url": "https://admission.pku.edu.cn/tzgg/index.htm"}` → `- “北京大学2027年接收推荐免试研究生办法（校本部）” 日期：2026-08-31 链接：`../docs/20260831123041610549.pdf` 页面中未见其他 2027 年推免/预推免相关通知。`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免, especially 各院系预报名汇总.", "url": "https://yzb.nju.edu.cn/"}` → `硕士栏目相关通知： - 日期：2026-09-08；标题：“南京大学2027年接收推荐免试研究生工作办法”；链接：https://yzb.nju.edu.cn/dd/dc/c47863a843228/page.htm - 日期：2026-08-31；标题：“南京大学2027年重要专项推荐免试研究生报名通知”；链接：https://yzb.nju.edu.cn/db/7f/c47863a842623/page.htm - 日期：2026-08-07；标题：“南京大学2027年接收推荐免试研究生预报名截止时间汇总”；链接：https://yzb.nju.edu.cn/d5/21/c47863a840993/page.htm - 日期：2 …[截断,原长775]`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年推荐免试研究生报名, especially 各院系报名 notice and their deadlines.", "url": "https://gsao.fudan.edu.cn/"}` → `Based only on the provided page content, the notices concerning 2027 推免报名 are: - “复旦大学2027年工程硕博士培养改革专项推免研究生招生报名通知” — https://gsao.fudan.edu.cn/0a/24/c15014a789028/page.htm — 2026-08-31 - “复旦大学生物技术学院2027级直博生招生报名通知” — https://mp.weixin.qq.com/s/rPWqABhXAJrS-pMbHYzy1Q — 2026-07-31 — this is the院系-level item listed - “复旦大学 …[截断,原长610]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

New:
- 清华: 关于清华大学2027年接收优秀应届本科毕业生免试攻读研究生报名的通知 2026-06-18 → fetch deadline. https://yz.tsinghua.edu.cn/info/1024/3234.htm
- 南大: 预报名截止时间汇总 2026-08-07 → https://yzb.nju.edu.cn/d5/21/c47863a840993/page.htm → fetch (this has the deadlines!). Also 工作办法 2026-09-08.
- 复旦: 工程硕博士专项 报名通知 2026-08-31 → fetch for deadline.
- 北大: only PDF.

Batch:
1. https://yzb.nju.edu.cn/d5/21/c47863a840993/page.htm
2. https://yz.tsinghua.edu.cn/info/1024/3234.htm
3. https://gsao.fudan.edu.cn/0a/24/c15014a789028/page.htm
4. 吉大/兰大: try 兰大 alternate domain https://yjs.lzu.edu.cn/ was 412; try https://ge.lzu.edu.cn/? skip. Do 中科大 via Bing search "中国科学技术大学2027年推免生接收办法". Encoding: %E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E6%8A%80%E6%9C%AF%E5%A4%A7%E5%AD%A6 2027%E5%B9%B4%E6%8E%A8%E5%85%8D%E7%94%9F%E6%8E%A5%E6%94%B6%E5%8A%9E%E6%B3%95 → earlier school query failed. Just try.

Let me run.

</details>

- 🔧 **WebFetch** `{"prompt": "List each 院系/专项 with its 预报名截止时间 date and URL. Quote Chinese sentences with dates.", "url": "https://yzb.nju.edu.cn/d5/21/c47863a840993/page.htm"}` → `基于以上内容，未出现任何“院系/专项”的预报名截止日期或对应链接，因此无法按要求列出条目。 页面仅显示标题：“南京大学2027年接收推荐免试研究生预报名截止时间汇总”，以及“发布时间：2026-08-07浏览次数：10322”。其中“2026-08-07”是发布时间，并非预报名截止时间。`

- 🔧 **WebFetch** `{"prompt": "Extract exact application deadline date(s), system open/close dates, per-院系 deadlines. Quote original Chinese sentences containing dates.", "url": "https://yz.tsinghua.edu.cn/info/1024/3234.htm"}` → `- 系统开放：2026年7月1日上午10:00。 - 申请截止/系统关闭：2026年7月28日下午15:00。原文：“申请服务系统定于2026年7月1日上午10:00开放，2026年7月28日下午15:00关闭。” - 资格复审：录取当年6月。原文：“我校将在录取当年6月对所有拟录取的推免生进行资格复审。” - 各院系截止日期：页面未列出。仅提到院系可自定标准，原文：“符合我校各拟录取院（系、所）自定的不低于学校复审要求的标准（具体咨询相应院系）。”`

- 🔧 **WebFetch** `{"prompt": "Extract exact application deadline date(s), system open/close dates. Quote original Chinese sentences containing dates.", "url": "https://gsao.fudan.edu.cn/0a/24/c15014a789028/page.htm"}` → `根据页面，系统申请窗口/截止时间仅见以下原文： “报名时间：9月1日—9月7日16:00（部分单位截止时间为9月3日16:00）” 据此：一般截止为9月7日16:00；部分单位截止为9月3日16:00。原文该句未写年份；页面标注日期为2026-08-31，按上下文应指2026年。系统开放起点未单独说明，只能按该句理解为9月1日开始。`

- 🔧 **WebFetch** `{"prompt": "List search results: title, URL, snippet. Focus on 中国科学技术大学2027年推免生接收办法.", "url": "https://cn.bing.com/search?q=%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E6%8A%80%E6%9C%AF%E5%A4%A7%E5%AD%A6+2027%E5%B9%B4%E6%8E%A8%E5%85%8D%E7%94%9F%E6%8E%A5%E6%94%B6%E5%8A%9E%E6%B3%95"}` → `WebFetch completed, but the extraction model returned no text.`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

- 清华: system 7/1-7/28 → CLOSED (past). Good, definite.
- 复旦工程硕博士专项: 9/1-9/7 16:00 → CLOSED. But main 报名 (7/3 notice) per院系; and 生物技术学院 etc. So 复旦 mainly closed; maybe some院系 still open.
- 南大: 汇总 page shows no dates (probably an attachment). Hmm. But 工作办法 2026-09-08. 南大 per院系 deadlines unknown. Mark 未核实.

I think I have enough. Let me do a final push on a few more schools with quick direct fetches: 山大 (no deadline), 华东师大 (no), 中国农大 (no), 湖南大学 (no), 中南 (no), 电子科大 (no), 川大 (no). These are all per-院系. That's fine — I'll mark them "已开始预报名/持续更新，具体截止由各院系定（未核实确切日期）".

Remaining completely unsearched: 吉大, 兰大, 武大, 天大, 北理, 厦大, 华东师大(have), 国防科大, 中央民大, 人大(not listed).

Let me try:
- 吉大: homepage had nothing; try 吉大 招生 list https://yjsy.jlu.edu.cn/zsxx/tms ... unknown. Try Bing search generic won't help. Try https://yz.jlu.edu.cn/
- 兰大: 412. Try https://yz.lzu.edu.cn/ gave 412 too.
- 武大: try https://gs.whu.edu.cn/ retry (homepage) 
- 天大: try https://yzb.tju.edu.cn/xwzx/zxxx/
- 北理: try https://yz.bit.edu.cn/yzbm (system) or search
- 厦大: try https://zs.xmu.edu.cn/ retry

Let me batch 4: 吉大, 武大, 天大, 厦大.

URLs:
吉大: https://yz.jlu.edu.cn/
武大: https://gs.whu.edu.cn/
天大: https://yzb.tju.edu.cn/xwzx/zxxx/
厦大: https://zs.xmu.edu.cn/

Go. Then final compile.

</details>

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yz.jlu.edu.cn/"}` → ``

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://gs.whu.edu.cn/"}` → `未发现符合“2027年接收推荐免试研究生”“推免生”“预推免”的公告链接（标题、URL、日期均无）。 招生通知列表页（页面内“READ MORE”链接）：`tzgg/zs.htm` 全部通知列表页：`tzgg/qb.htm``

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免.", "url": "https://yzb.tju.edu.cn/xwzx/zxxx/"}` → `WebFetch completed, but the extraction model returned no text.`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://zs.xmu.edu.cn/index.htm"}` → `**Relevant 2027 推免生 notice found:** - Title: "厦门大学关于2027年招收国家优秀中小学教师培养计划推免生的通知" - Date: 2026-08-13 - URLs (listed in two places): - https://zs.xmu.edu.cn/info/1174/36782.htm (最新公告 / homepage listing) - https://zs.xmu.edu.cn/info/1055/36772.htm (硕士研究生 section) **Notice list page URLs:** - 最新公告: https://zs.xmu.edu.cn/ (h …[截断,原长435]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Diminishing returns. Let me do one last targeted attempt at a few: 北理, 华东师大 individual dept, 中科大, 上交, 浙大. Actually, let me try a generic Bing search once more with a phrase that might surface the remaining schools' notice titles — e.g. "2027年接收推荐免试研究生预报名通知" (as a phrase). Or "2027年接收推免生预报名".

Actually earlier "接收推荐免试研究生 预报名" gave the best set. Let me just re-run it non-RSS to see if it gives a fresh/expanded list (it was RSS earlier). Non-RSS may give more results.

Let me run 2-3 searches:
1. non-RSS "接收推荐免试研究生 预报名" (count=30)
2. "推免生 预报名 通知" 
3. "预推免 报名 截止 时间"

And 1 fetch: 北理 system page? Let me skip.

Let me just do the searches, then compile.

Encoding:
1. same as before: %E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D&count=30
2. %E6%8E%A8%E5%85%8D%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D+%E9%80%9A%E7%9F%A5
3. %E9%A2%84%E6%8E%A8%E5%85%8D+%E6%8A%A5%E5%90%8D+%E6%88%AA%E6%AD%A2+%E6%97%B6%E9%97%B4

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "List all search results with title, URL, snippet, and any date. Focus on 2027 university 推免/预推免 notices.", "url": "https://cn.bing.com/search?q=%E6%8E%A5%E6%94%B6%E6%8E%A8%E8%8D%90%E5%85%8D%E8%AF%95%E7%A0%94%E7%A9%B6%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D&count=30"}` → `Found 10 organic results. Most are 2027 推免/预推免 notices. 1. Title: "全国推荐免试攻读研究生（免初试、转段）" URL: https://yz.chsi.com.cn/tm/index Snippet: "“全国推荐免试攻读研究生（免初试、转段）信息公开管理服务系统”（简称“推免服务系统”）是全国统一的推免工作信息备案公开平台 …" Date: not shown 2. Title:`

- 🔧 **WebFetch** `{"prompt": "List all search results with title, URL, snippet, and any date. Focus on 2027 university 推免/预推免 notices.", "url": "https://cn.bing.com/search?q=%E6%8E%A8%E5%85%8D%E7%94%9F+%E9%A2%84%E6%8A%A5%E5%90%8D+%E9%80%9A%E7%9F%A5&count=30"}` → `未发现任何“2027年高校推免/预推免通知”。以下为页面列出的全部搜索结果，均与2027推免无关。 1. **推（汉语文字）_百度百科** URL: https://baike.baidu.com/item/%E6%8E%A8/8047564 日期: 无 摘要: “该字语义涵盖物理推动与抽象引申：既指施加力量的行为（如推车），又衍生出礼让（推食）、选拔（推贤）、探究（推本）等用 …” 2. **推特网页版入口:x.com 登录与下载(原Twitter) · 读懂马斯克** URL: https://www.readmusk.com/x 日期: “2 天之前” 摘要: “2 天之前 · 推特网页版入口是 x.com（旧域名 twitt …[截断,原长1526]`

- 🔧 **WebFetch** `{"prompt": "List all search results with title, URL, snippet, and any date. Focus on 2027 university 预推免 deadlines.", "url": "https://cn.bing.com/search?q=%E9%A2%84%E6%8E%A8%E5%85%8D+%E6%8A%A5%E5%90%8D+%E6%88%AA%E6%AD%A2+%E6%97%B6%E9%97%B4&count=30"}` → `未发现直接涉及“2027年高校预推免截止日期”的结果。仅一条知乎结果与预推免流程有关，但摘要未给具体截止时间。 - 标题：“预_百度百科”；URL：https://baike.baidu.com/item/%E9%A2%84/4942379；日期：无；摘要：“作形容词时有预先、事先的意思，如预习、预计等；作动词时有参与的意思，如干预、参预。 ‘预’通‘与’和‘豫’。 在《康熙字典》中记 …” - 标题：“预的意思,预的解释,预的拼音,预的部首,预的笔顺-汉语国学”；URL：https://www.hanyuguoxue.com/zidian/zi-39044；日期：无；摘要：“预的拼音是yù，预字共10画，部首是页部，本页介绍预字的 …[截断,原长801]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

OK, searches exhausted. I have a good dataset. Let me try 2-3 final fetches for high-value schools: 上交 (need any date), 中科大, 浙大, 北理. And maybe 华东师大 individual dept.

Actually, let me try 中科大 via the article list with a different URL form. The 中科大 site: yz.ustc.edu.cn. The list page /column/182. Maybe article URLs are /column/182/xxxx. Let me ask Bing: search "中国科学技术大学2027年推免生接收办法 site:yz.ustc.edu.cn" — skip.

Let me instead try fetching 浙大 via a dept: Actually for 浙大 the 研究生招生 site is http://grs.zju.edu.cn/ (cert expired on https). Try http://grs.zju.edu.cn/.

And 上交's 预推免办法 page might have dates in the 通知正文: ga.sjtu.edu.cn/zsgl/ytmgl/ gave garbled. There may be a notice on yzb.sjtu.edu.cn. Let me search yzb for "2027" via homepage listing. Already homepage gave only links.

Let me do final batch:
1. http://grs.zju.edu.cn/
2. https://yz.ustc.edu.cn/column/182?num=-1 (retry, maybe gives hrefs now)
3. https://yzb.seu.edu.cn/6676/list.htm (东南 list — check for 第三批/newer notices) — actually东南 already past.
3. https://yz.bit.edu.cn/yzbm (北理 system) — skip.
3. 华东师大 院系 example: https://yjszs.ecnu.edu.cn/43264/list.htm
4. 湖南大学 system? skip.

Let me do: 浙大(http), 中科大 list, man Bet: 北理 search via Bing "北京理工大学2027年推免生 预报名", 华东师大 list.

I'll run 4:
1. http://grs.zju.edu.cn/
2. https://yz.ustc.edu.cn/column/182?num=-1
3. https://yjszs.ecnu.edu.cn/43264/list.htm
4. https://cn.bing.com/search?q=%E5%8C%97%E4%BA%AC%E7%90%86%E5%B7%A5%E5%A4%A7%E5%AD%A6+2027+%E6%8E%A8%E5%85%8D+%E9%A2%84%E6%8A%A5%E5%90%8D  (likely fails but cheap)

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免.", "url": "http://grs.zju.edu.cn/"}` → ``

- 🔧 **WebFetch** `{"prompt": "Give the full href URLs for the 2027 推免生 notices listed.", "url": "https://yz.ustc.edu.cn/column/182?num=-1"}` → `The supplied content contains no `href` values, so I can’t provide full URLs. It only shows these 2027 推免-related notices: - “中国科学技术大学2027年推免生（推荐）名单公示” — 2026-09-08 - “中国科学技术大学2027年推免生接收办法” — 2026-09-03 - “中国科学技术大学2027年推免生推荐办法” — 2026-09-03 - “中国科学技术大学2027年工程硕博士培养改革专项推免生预选拔招生简章” — 2026-09-03 - “中国科学技术大学与宁波东方理工大学2027年招收 …[截断,原长391]`

- 🔧 **WebFetch** `{"prompt": "List notice links (title + URL + date) about 2027年接收推荐免试研究生 / 预报名, and any deadlines.", "url": "https://yjszs.ecnu.edu.cn/43264/list.htm"}` → `与2027年推免/预报名相关的通知如下： - “华东师范大学2027年接收优秀应届本科毕业生免试攻读研究生（含本科直博）工作办法” URL: `/d3/d1/c43264a775121/page.htm` 日期: 2026-09-04 - “华东师范大学2027年各院系接收优秀应届本科毕业生免试攻读研究生（含本科直博）预报名通知（陆续更新）” URL: `/c3/cb/c43264a771019/page.htm` 日期: 2026-07-24 - “关于华东师范大学2027年接收优秀应届本科毕业生免试攻读研究生（含本科直博） 预报名的通知（增加中法联培项目）” URL: `/c2/c6/c43264a770758/page.htm …[截断,原长387]`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生 / 预推免. Give the notice list page URL.", "url": "https://yz.bit.edu.cn/yzbm"}` → `REDIRECT DETECTED: The URL redirects to a different host. Original URL: https://yz.bit.edu.cn/yzbm Redirect URL: http://yz.bit.edu.cn/yzbm/ Status: 302 Found To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters: - url: "http://yz.bit.edu.cn/yzbm/" -  …[截断,原长437]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

I have gathered substantial data. Let me compile now. But let me make a final attempt for a few high-profile schools via their 院系 or the 教育部推免服务系统 timeline.

Actually, one important cross-cutting fact: 教育部推免服务系统 (yz.chsi.com.cn/tm) — the national system opening time. From the first RSS result: "candidates may fill multiple parallel choices from Sept. 22 to Oct. 20, 2025" (that was 2025). For 2026, the national 推免服务系统 typically opens ~Sept 22 and closes ~Oct 20 (填报志愿). Many schools' 预推免 (school-internal) deadlines are before that, but a lot of schools accept 预报名 until mid/late Sept.

Let me fetch yz.chsi.com.cn/tm/index to get the 2026 timeline. That's valuable context.

Also try to get 中科大 article URL via the site search. Hmm.

Let me do final batch:
1. https://yz.chsi.com.cn/tm/index — national timeline
2. http://yz.bit.edu.cn/yzbm/ (北理)
3. https://yzb.sjtu.edu.cn/ (retry, ask for 2027)
4. https://yz.ustc.edu.cn/ (retry, ask for hrefs / or the 接收办法 text)

Go, then compile.

</details>

- 🔧 **WebFetch** `{"prompt": "Extract the 2026/2027 推免服务系统 timeline: opening date for 填报志愿, closing date, and any dates. Quote Chinese sentences with dates.", "url": "https://yz.chsi.com.cn/tm/index"}` → `本页未列出2026/2027年度安排；可确认的是2025年时间点。 - 志愿填报：2025年9月22日9:00开放，2025年10月20日截止。页面写明：“考生于2025年9月22日至10月20日，可自主多次平行填报多个招生单位及专业志愿。”又提到“9月22日9:00开始填报志愿”。 - 资料注册及资格查看：自2025年9月18日起。原文：“2025年9月18日起，推免生通过“推免服务系统”注册填报个人资料信息并查看本人推免资格。” - 复试与待录取确认：前者从9月23日9:00起，后者从9月25日14:00起。原文：“9月23日9:00开始接收并确认招生单位发送的复试通知；9月25日14:00开始接收并确认招生单位发送的待录取通知 …[截断,原长421]`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027年接收推荐免试研究生 / 推免生. Give the notice list page URL.", "url": "http://yz.bit.edu.cn/yzbm/"}` → `REDIRECT DETECTED: The URL redirects to a different host. Original URL: https://yz.bit.edu.cn/yzbm/ Redirect URL: http://yz.bit.edu.cn/yzbm/logon Status: 302 Found To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters: - url: "http://yz.bit.edu.cn/yzb …[截断,原长442]`

- 🔧 **WebFetch** `{"prompt": "List any notice links (title + URL + date) about 2027 预推免/推免生. Quote any dates.", "url": "https://yzb.sjtu.edu.cn/"}` → `No notice links for 2027 预推免/推免生 appear in the provided content. The only 2027-dated items are doctoral, not 推免/预推免: - “上海交通大学2027年‘医工交叉平台’博士研究生招生简章” — date “06 2026.09” - “上海交通大学2027级‘明志荣誉博士生’招生简章” — date “09 2026.07” There are generic 预推免 links (“预推免”, “预推免公示”, “预推免考生登录”), but no 2027 title or date attached.`

- 🔧 **WebFetch** `{"prompt": "Extract the full text of 中国科学技术大学2027年推免生接收办法 if present, especially any dates or deadlines. Quote Chinese sentences with dates.", "url": "https://yz.ustc.edu.cn/"}` → `页面未包含《中国科学技术大学2027年推免生接收办法》的正文，只在“通知公告”中列出标题和发布日期：“中国科学技术大学2027年推免生接收办法”，“09.03 2026”。 因此，无法从现有内容提取该办法全文、具体时间节点或截止日期。`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

I've collected a good amount. The national system page shows only 2025 dates (site not updated to 2026 yet in index). For 2026 cycle, 填报志愿 typically 9/22-ish.

Now let me compile the final report. I must be careful to:
- Clearly label evidence strength
- Distinguish ① still open (deadline >= 2026-09-11) ② closed ③ unclear
- Not fabricate dates/links

Let me organize the findings.

Schools with explicit deadline >= 2026-09-11 (STILL OPEN) — strong evidence:
1. 华南理工大学 — "请意向申请考生务必在9月15日前在我校预报名系统完成报名工作。" 发布 2026-08-28. → open until 2026-09-15. URL https://yz.scut.edu.cn/2026/0828/c30108a633884/page.htm
2. 重庆大学 — 系统 2026-06-23 10:00 至 2026-09-30 18:00. URL https://yz.cqu.edu.cn/news/2026-06/2553.html → open until 9/30.
3. 中国海洋大学 — 7月23日—9月14日17点. URL https://yz.ouc.edu.cn/2026/0723/c31626a534920/page.htm → open until 9/14.
4. 西北工业大学 — 预报名 9月4日15:00—9月20日18:00. URL https://yzb.nwpu.edu.cn/info/1174/10478.htm → open until 9/20.
5. 西北农林科技大学 — 系统 2026年9月10日至9月20日. URL https://yz.nwafu.edu.cn/tzgg/efc5ad22976f45b595487499b6c39d8e.htm → open until 9/20.
6. 大连理工大学 — 部分院系: 数学科学学院 2026-07-14 00:00–9月15日12:00; 汇总页 https://gs.dlut.edu.cn/info/1173/51492.htm → some depts open to 9/15 (partially verified, page listed more院系 but extraction truncated).

Schools with notices that opened recently and deadlines set per-院系 (likely still open, but exact date 未核实):
- 山东大学 — 系统 9/1 09:00 开放，截止由各单位定. https://www.yz.sdu.edu.cn/info/1022/1463.htm → likely open, date unclear.
- 华中科技大学 — 预报名开始 2026-09-09, 截止由院系定. http://gszs.hust.edu.cn/info/1106/4142.htm → likely open.
- 四川大学 — 2026-09-08 通知, 无统一截止. https://yz.scu.edu.cn/zsxx/Details/... → likely open.
- 电子科技大学 — 2026-09-04 通知, 无具体截止. https://yz.uestc.edu.cn/info/1081/5939.htm
- 中南大学 — 8月28日开始, 截止由二级单位定. https://yz.csu.edu.cn/info/1009/1528.htm
- 湖南大学 — 8月28日起可登录报名, 截止以学院通知为准. https://gra.hnu.edu.cn/info/1075/10560.htm
- 南京大学 — 工作办法 2026-09-08; 预报名截止时间汇总 2026-08-07 (页面无明细). https://yzb.nju.edu.cn/dd/dc/c47863a843228/page.htm
- 东北大学 — 无具体截止，咨询各学院. https://yz.neu.edu.cn/2026/0720/c5932a458191/page.htm
- 哈尔滨工业大学 — 系统 2026-07-20 起开通，无关闭日期. https://yzb.hit.edu.cn/2026/0717/c22276a397589/page.htm
- 中山大学 — 无统一截止. https://graduate.sysu.edu.cn/zsw/article/538
- 北京师范大学 — 无全校截止，院系定. https://yz.bnu.edu.cn/detail/be0e6268-...
- 北京航空航天大学 — 各学院分批次, 通知 2026-09-10 更新 → likely open. https://yzb.buaa.edu.cn/info/1036/3610.htm
- 同济大学 — 汇总页 (更新中); many 院系 deadlines 8/5–9/8 already past; 中外语 9/8 8:00, 数学 9/8 12:00 → all listed past. So 同济 likely mostly closed. Mark as 已截止 (所有已列院系) but "更新中" might add more.
- 华东师范大学 — 各院系预报名 (陆续更新) 2026-07-24; 工作办法 2026-09-04; 无统一截止. Likely some still open.
- 某985高校 — 各院系细则 (陆续更新) 2026-07-20; 无日期.
- 西安交通大学 — 各学院实施细则 2026-09-03; deadline 未核实.
- 天津大学 — 未找到 2027 通知 (homepage only old).
- 武汉大学 — 未在招生通知列表找到 2027 推免.
- 厦门大学 — only "国优计划" 2026-08-13 found.
- 中科大 — 2027年推免生接收办法 2026-09-03 (date unknown), 无 URL.
- 北京大学 — 办法 PDF 2026-08-31, no deadline fetchable.
- 复旦大学 — 主报名 7/3; 工程硕博士专项 9/1–9/7 16:00 → 已截止.
- 清华大学 — 系统 7/1–7/28 15:00 → 已截止.
- 浙江大学 — site cert expired, not retrieved.
- 吉林大学 — DNS fail.
- 兰州大学 — 412 blocked.
- 国防科技大学 — DNS fail.
- 中央民族大学 — DNS fail.
- 东南大学 — 专项报名 windows ended 9/4; 第二批 9/1–9/3 → 已截止 (as of listed).

Also note the national 推免服务系统 (yz.chsi.com.cn/tm) — 2026 dates not shown; 2025 was 9/22–10/20.

Now, the user asked specifically: schools whose 报名/申请 尚未截止 (deadline >= 2026-09-11). I'll build the table with ①②③.

I should present:
- Table 1: 明确未截止 (deadline >= 9/11) with exact quotes.
- Table 2: 已明确截止 (剔除).
- Table 3: 日期不明/表述模糊 (单独列出).
- Plus notes on search limitations.

Let me also record the national system timeline (2025 reference).

Evidence strength: 强 (原文明确日期) / 中 (原文有日期但指系统开放或需登录查) / 弱 (无日期).

Let me write the final answer in Chinese, Markdown tables.

I must include exact quotes. Let me be accurate based on what extraction returned.

Important caveat: The extraction model sometimes reported a wrong "current date" (2026-05-09 etc.) — ignore those.

Let me also mention: 江南大学 (211, not 985) open Sept 1–17, 2026 — useful but not 985; mention as bonus.

Also 北京协和医学院 (not 985) 8/10–8/23 closed.

Now, for the "still open" list, the strongest are 华南理工 (9/15), 重庆大学 (9/30), 中国海洋 (9/14), 西北工大 (9/20), 西北农林 (9/20). 大连理工 math dept 9/15.

Let me write the report. I'll keep it organized and note URLs absolute.

Also include a "not verified / could not access" list.

Let me finalize.

</details>

- 🔧 **TodoWrite** `{"todos": [{"content": "Confirm working search endpoint (Bing non-RSS + generic phrase queries)", "priority": "high", "status": "completed"}, {"content": "Collect 2027 预推免/推免 notices from 985 grad-school sites", "priority": "high", "status": "completed"}, {"content": "Fill remaining schools (清华/北大/复旦/上交/浙大/中科大/南大/吉大/兰大/武大/天大/北理/厦大)", "priority": "high", "status": "completed"},  …[截断,原长412]` → `{"oldTodos":[{"content":"Confirm working search endpoint (Bing non-RSS + generic phrase queries)","status":"completed","priority":"high"},{"content":"Collect 2027 预推免/推免 notices from 985 grad-school sites","status":"completed","priority":"high"},{"content":"Fill remaining schools (清华/北大/复旦/上交/浙大/中科大/南大/吉大/兰大/武大/天大/北理/厦 …[截断,原长983]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-11 14:05）

I have enough verified evidence. Compiling the final report.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Now write the final answer. Note: I should be honest about tool limitations (no WebSearch tool available; used WebFetch against cn.bing.com which was intermittent). And note that "2026年秋季预推免面向2027年入学" is what I searched (2027级/2027年接收推免).

Let me write it.

</details>

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-11 14:05）

# 2026年秋季（面向2027年入学）985高校预推免/推免接收情况核查

## 0. 检索环境说明（重要，先说清）

- 本会话**没有 WebSearch 工具**，只能用 WebFetch 抓网页。可用的检索入口只有 `cn.bing.com/search`，且极不稳定：**搜索学校全名时会被当成地名/百科（如"浙江大学"→浙江省旅游），加年份"2027"会被当成日历**，同一关键词批量并发时常返回空。可稳定复现的关键词只有 `接收推荐免试研究生 预报名`、`预推免 报名 系统` 这类**不含学校名、不含年份的动宾短语**。
- 因此最终有效路径 = **"通用短语搜索拿到 URL → 直接抓各校研究生院官网通知页"**。现实时间是 2026-09（Bing 返回的 pubDate 为 2026-09-10/11，与题设一致）。
- 我全程**未编造任何日期或链接**；提取不到的字段一律写"未核实"。因各校 2027 通知多为"院系自定截止/陆续更新"，很多学校**官网原文确实不写统一截止日**。

---

## 1. ① 明确仍未截止（截止日 ≥ 2026-09-11，有原文日期）

| 学校 | 层次 | 通知/院系 | 报名截止 | 原文URL | 证据强度 |
|---|---|---|---|---|---|
| 华南理工大学 | 985 | 研究生招生办《华南理工大学接收2027年推荐免试研究生预报名通知》(2026-08-28) | **2026-09-15 前**（原文："请意向申请考生务必在**9月15日前**在我校预报名系统完成报名工作。"） | https://yz.scut.edu.cn/2026/0828/c30108a633884/page.htm | 强（原文明确） |
| 重庆大学 | 985 | 研究生招生办《重庆大学2027年推荐免试研究生（含直博生）招生预报名公告》 | **2026-09-30 18:00**（原文："重庆大学研究生招生服务系统开放时间为**2026年6月23日10:00至2026年9月30日18:00**。"） | https://yz.cqu.edu.cn/news/2026-06/2553.html | 强（原文明确） |
| 中国海洋大学 | 985 | 研究生院《中国海洋大学2027年接收推荐免试研究生预报名通知》(2026-07-23) | **2026-09-14 17:00**（原文："**7月23日—9月14日17点**，考生登录'中国海洋大学研究生考生服务平台'进行报名"） | https://yz.ouc.edu.cn/2026/0723/c31626a534920/page.htm | 强（原文明确） |
| 西北工业大学 | 985 | 研究生招生办《西北工业大学2027年接收推荐免试研究生预报名的通知》(2026-09-04) | **2026-09-20 18:00**（原文："预报名时间：**9月4日15:00—9月20日18:00**，具体时间以各学院公布为准。"） | https://yzb.nwpu.edu.cn/info/1174/10478.htm | 强（原文明确，学院可微调） |
| 西北农林科技大学 | 985 | 研究生院《关于西北农林科技大学2027年招收推荐免试研究生预报名…》 | **2026-09-20**（原文："我校2027年招收推免生预报名系统将于**2026年9月10日至9月20日**向考生开放，各学院申报截止时间由学院通知为准。"） | https://yz.nwafu.edu.cn/tzgg/efc5ad22976f45b595487499b6c39d8e.htm | 强（原文明确，学院可微调） |
| 大连理工大学 | 985 | 研究生院《关于大连理工大学各院系接收2027年推荐免试研究生预报名陆续开放的通知》(2026-07-14) | 部分院系**2026-09-15 12:00**（原文表格："（主校区）数学科学学院 2026年7月14日00：00--**9月15日12：00**"；其余院系该页表格被截断，未逐一核实） | https://gs.dlut.edu.cn/info/1173/51492.htm | 中（仅核到部分院系） |

---

## 2. ② 已明确截止（截止日 < 2026-09-11，应剔除）

| 学校 | 层次 | 通知 | 截止 | 原文URL | 证据强度 |
|---|---|---|---|---|---|
| 清华大学 | 985 | 《关于清华大学2027年接收优秀应届本科毕业生免试攻读研究生报名的通知》(2026-06-18) | **2026-07-28 15:00**（原文："申请服务系统定于2026年7月1日上午10:00开放，**2026年7月28日下午15:00关闭**。"） | https://yz.tsinghua.edu.cn/info/1024/3234.htm | 强 |
| 复旦大学 | 985 | 《复旦大学2027年工程硕博士培养改革专项推免研究生招生报名通知》(2026-08-31) | **2026-09-07 16:00**（原文："报名时间：**9月1日—9月7日16:00**（部分单位截止时间为9月3日16:00）"） | https://gsao.fudan.edu.cn/0a/24/c15014a789028/page.htm | 强（专项；主报名见下） |
| 东南大学 | 985 | 《东南大学2027年推免专项报名通知》(2026-08-31) /《部分学院…第二批》(2026-08-28) | 研支团专项 **9/1 17:00**；其他专项 **9/4 17:00**；第二批土木 **9/1 12:00**、材料 **9/3 12:00** | http://yzb.seu.edu.cn/2026/0831/c6676a580992/page.htm ；http://yzb.seu.edu.cn/2026/0828/c6676a580682/page.htm | 强（列出的批次均已过；是否还有第三批未核实） |
| 同济大学 | 985 | 《各学院2027年接收推荐免试研究生（含直接攻博）预报名通知汇总（更新中）》 | 已列院系中最晚为 **2026-09-08**（外国语9/8 8:00、数学9/8 12:00；机械9/1、建筑8/14、经管8/25…） | https://yz.tongji.edu.cn/info/1010/4220.htm | 中（标题"更新中"，可能有新增批次） |

---

## 3. ③ 有 2027 通知、但截止"由各院系定/未写明确日期"——需自行登录系统或查院系（**未核实**）

以下均**已在官网原文确认存在 2027 推免/预报名通知**，但原文未给全校统一截止日，故**不能判定**是否仍开放；多数通知发布日期在 2026-08-28 ~ 09-10，**大概率仍可报名**。

| 学校 | 层次 | 通知/院系 | 截止 | 原文URL | 证据强度 |
|---|---|---|---|---|---|
| 华中科技大学 | 985 | 《关于开展2027年接收推荐免试研究生（含直博生）预报名及复试工作安排的通知》(2026-09-09) | 未核实（原文："预报名截止时间：各院系报名截止…详见各院系发布的接收推免生工作细则"） | http://gszs.hust.edu.cn/info/1106/4142.htm | 中高（09-09 刚开） |
| 山东大学 | 985 | 《2027年接收推荐免试硕士研究生和本科直博生预报名通知》(2026-08-28) | 未核实（"系统开放时间：2026年9月1日09:00，具体报名开始时间和截止时间由我校各招生单位自主确定"） | https://www.yz.sdu.edu.cn/info/1022/1463.htm | 中 |
| 四川大学 | 985 | 《四川大学2027年推荐免试研究生招生章程》/《各招生院系所接收…通知》(2026-09-08) | 未核实 | https://yz.scu.edu.cn/zsxx/Details/0f4bc2fc-e7d8-455d-b0e3-8ad680196df1 | 中 |
| 电子科技大学 | 985 | 《电子科技大学接收2027年优秀应届本科毕业生免试攻读研究生（含直博生）…》(2026-09-04) | 未核实 | https://yz.uestc.edu.cn/info/1081/5939.htm | 中 |
| 中南大学 | 985 | 《中南大学关于2027年接收优秀应届本科毕业生免试攻读硕士研究生预报名的通知》(2026-08-28) | 未核实（"8月28日开始可…网上报名；各二级单位报名截止时间详见二级单位官方通知"） | https://yz.csu.edu.cn/info/1009/1528.htm | 中 |
| 湖南大学 | 985 | 《湖南大学2027年接收推荐免试研究生（含直博…）》(2026-08-28) | 未核实（"报名截止时间以学院通知为准"；8月28日起可登录报名系统） | https://gra.hnu.edu.cn/info/1075/10560.htm | 中 |
| 南京大学 | 985 | 《南京大学2027年接收推荐免试研究生工作办法》(2026-09-08)；《…预报名截止时间汇总》(2026-08-07，页面正文无明细) | 未核实 | https://yzb.nju.edu.cn/dd/dc/c47863a843228/page.htm ；https://yzb.nju.edu.cn/d5/21/c47863a840993/page.htm | 中 |
| 东北大学 | 985 | 《东北大学2027年接收推荐免试研究生工作办法》(2026-07-20) | 未核实（"报名截止时间及审核时间请咨询各学院"） | https://yz.neu.edu.cn/2026/0720/c5932a458191/page.htm | 中 |
| 哈尔滨工业大学 | 985 | 《关于2027年接收优秀应届本科毕业生免试攻读研究生报名的通知》(2026-07-19) | 未核实（"2026年7月20日起开通'推免生信息采集系统'"；无关闭日） | https://yzb.hit.edu.cn/2026/0717/c22276a397589/page.htm | 中 |
| 中山大学 | 985 | 《中山大学2027年接收优秀应届本科毕业生推荐免试攻读研究生报名的通知》(2026-07-30) | 未核实（"各招生单位…截止时间不尽相同"） | https://graduate.sysu.edu.cn/zsw/article/538 | 中 |
| 北京航空航天大学 | 985 | 《北航各学院接收推免攻读2027年研究生（含博士）相关通知（**2026年9月10日更新**）》 | 未核实（"各学院可根据申请情况分批次组织，具体见相关学院网站"） | https://yzb.buaa.edu.cn/info/1036/3610.htm | 中高（09-10 仍在更新） |
| 北京师范大学 | 985 | 《北京师范大学2027年推荐免试硕士／博士研究生招生录取工作办法》(2026-09-02) | 未核实（"各院（系）的网上申请截止日期在网上申请系统公告"） | https://yz.bnu.edu.cn/detail/be0e6268-0bfd-4a34-aa31-e72207bf2577 | 中 |
| 华东师范大学 | 985 | 《2027年接收…工作办法》(2026-09-04)；《各院系预报名通知（陆续更新）》(2026-07-24) | 未核实（汇总页只有院系链接，无截止日） | http://yjszs.ecnu.edu.cn/d3/d1/c43264a775121/page.htm ；http://yjszs.ecnu.edu.cn/c3/cb/c43264a771019/page.htm | 中 |
| 某985高校 | 985 | 《各院系2027年接收推荐免试研究生工作实施细则（陆续更新中）》(2026-07-20) | 未核实（汇总页 20 个院系链接，均未列截止日） | https://yz.cau.edu.cn/art/2026/7/20/art_41742_1123106.html | 中 |
| 西安交通大学 | 985 | 《各学院（部、中心）2027年招收推免生实施细则》(2026-09-03)；《2027年推荐免试研究生招生章程》(2026-09-02) | 未核实（细则正文未能完整抓取） | https://yz.xjtu.edu.cn/info/1082/4399.htm | 中 |
| 厦门大学 | 985 | 《厦门大学关于2027年招收国家优秀中小学教师培养计划推免生的通知》(2026-08-13) | 未核实（仅找到"国优计划"专项，未见全校预推免通知） | https://zs.xmu.edu.cn/info/1174/36782.htm | 弱-中 |

---

## 4. 未能取得有效原文（工具受限 / 站点拒绝），**未核实，不做结论**

| 学校 | 层次 | 情况 |
|---|---|---|
| 北京大学 | 985 | 找到《北京大学2027年接收推荐免试研究生办法（校本部）》2026-08-31，但该文件是 **PDF**（`https://admission.pku.edu.cn/docs/20260831123041610549.pdf`），WebFetch 不支持 PDF 解析，**截止日未核实** |
| 浙江大学 | 985 | `grs.zju.edu.cn` 与 `yjsy.zju.edu.cn` 均返回 **证书过期/仅 JS 加载页**，未取到 2027 通知 |
| 上海交通大学 | 985 | 官网仅有"预推免"入口（http://ga.sjtu.edu.cn/zsgl/ytmgl/），**无 2027 标题/日期**，未核实 |
| 中国科学技术大学 | 985 | 列表页确认存在《中国科学技术大学2027年推免生接收办法》(2026-09-03)、《…工程硕博士专项预选拔简章》(2026-09-03) 等，但页面不暴露文章 URL，**链接与截止日未核实** |
| 吉林大学 | 985 | `yz.jlu.edu.cn` DNS 无法解析；`yjsy.jlu.edu.cn` 列表无 2027 推免条目 |
| 兰州大学 | 985 | `yjs.lzu.edu.cn` / `yz.lzu.edu.cn` 均返回 **HTTP 412** |
| 国防科技大学 | 985 | `yz.nudt.edu.cn` DNS 无法解析 |
| 中央民族大学 | 985 | `yz.muc.edu.cn` DNS 无法解析 |
| 天津大学 | 985 | 研招首页与"最新资讯"仅见 2017/2018 年推免通知，**未见 2027 条目** |
| 武汉大学 | 985 | 研究生院招生通知列表/全部通知列表均未见 2027 推免条目 |
| 北京理工大学 | 985 | 仅有预报名系统登录页（http://yz.bit.edu.cn/yzbm/logon），无公开 2027 通知列表 |

## 5. 附带发现（非 985，供参考，均可核验）

- **江南大学（211）**：《江南大学接收2027年推荐免试研究生预报名公告》，系统 **2026年9月1日—9月17日**开放 — https://yz.jiangnan.edu.cn/info/1012/3864.htm （**未截止**）
- **南京航空航天大学（211）**：《2027年接收推荐免试研究生预报名通知》(2026-07-15) — https://www.graduate.nuaa.edu.cn/2026/0715/c2145a405484/page.htm
- **北京协和医学院**：预报名系统 **2026年8月10日10:00—8月23日17:00**（**已截止**） — https://graduate.pumc.edu.cn/zsw/info/1005/2263.htm
- **教育部"推免服务系统"**：官方页 https://yz.chsi.com.cn/tm/index 目前仍显示 **2025 年**时间表（9月22日填报志愿—10月20日；9月18日起注册），**2026年时间未更新**，可作为全国时间轴参考但不能当作今年确定日期。

## 6. 结论

- **明确仍未截止的 985（截止日已核验）**：华南理工大学（9/15）、中国海洋大学（9/14）、西北工业大学（9/20）、西北农林科技大学（9/20）、重庆大学（9/30）；大连理工大学部分院系（9/15，部分核验）。
- **明确已截止的 985**：清华大学（7/28）、复旦大学工程硕博士专项（9/7）、东南大学（专项 9/1–9/4）、同济大学（已列院系最晚 9/8）。
- **最大的一块是"各院系自定 / 未写统一截止"**（华科、山大、川大、电子科大、中南、湖大、南大、东北、哈工大、中大、北航、北师大、华东师大、中国农大、西交等）——这些通知的发布日期集中在 **8月下旬至9月10日**，判断上更接近"仍开放"，但**原文没有可核验的截止日，按你的要求我标为"未核实"**，需登录各校预报名系统或查具体院系细则确认。
- 检索受工具限制较大：无 WebSearch，Bing 中文检索对"学校名+年份"几乎失效；`src/PKU-x.pdf`、浙大/上交/中科大/吉大/兰大/国防科大/中央民大等站点或格式无法解析。**以上所有链接与日期均来自实际抓取的网页原文，未抓到的部分已如实标为"未核实"。**
