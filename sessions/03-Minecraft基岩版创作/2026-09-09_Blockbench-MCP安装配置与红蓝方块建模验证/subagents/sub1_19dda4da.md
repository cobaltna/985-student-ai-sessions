# 子代理会话 sess_subagent_agent_d7e5289e-7e09-4e1d-a349-dd4919dda4da

模型: ?

## 👤 用户（2026-09-09 23:29）

Research task (web research, no code changes). The user wants to configure a "Blockbench MCP server" so an AI coding agent can create/edit Minecraft 3D models inside Blockbench (blockbench.net).

Please research the actual, currently existing solutions and report back concretely:

1. Search the web/GitHub for "Blockbench MCP" or "MCP server Blockbench". There may be one or more community projects (e.g. a GitHub repo with an MCP server that talks to Blockbench via a Blockbench plugin exposing an HTTP/WebSocket API on localhost, possibly on a port like 25456). Identify the most credible/actively maintained project(s) with exact repo URLs.
2. For the best candidate(s), report the exact architecture: (a) does the user need to install a Blockbench plugin inside Blockbench (which one, by what name, how to install from Blockbench's plugin store / Files tab)? (b) does the MCP server run via npx / uvx / docker / binary, and what is the exact command? (c) what MCP transport does it use (stdio vs HTTP/SSE), and if remote, the exact URL to configure?
3. Report prerequisites: Java? Node? Python? OS support (user is on Windows 10 x64). Which Minecraft editions supported (Java vs Bedrock)? Anything about the Blockbench WebSocket/local API plugin dependency?
4. Report the exact JSON config snippet one would put in an MCP client's config file (e.g. .mcp.json or mcp settings) for that server, including environment variables if any.
5. Note any known caveats: model formats (.bbmodel), whether the AI needs image/screenshot tooling, Windows-specific issues, firewall prompts, etc.

Return a structured summary with the repo URLs, exact commands, config JSON, and caveats. Do not guess — only report what you can verify from web sources, and clearly mark anything uncertain.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

The user wants me to research "Blockbench MCP server" solutions on the web. Let me do web research using WebFetch and possibly GitHub searches.

Let me start by searching the web for "Blockbench MCP" and checking GitHub for related repositories.

Let me plan my searches:
1. Web search for "Blockbench MCP server"
2. GitHub search for "Blockbench MCP"
3. Look at credible repos found

Let me start with parallel searches.

</details>

- 🔧 **WebFetch** `{"url": "https://www.google.com/search?q=%22Blockbench%22+MCP+server", "prompt": "List all search results about a Blockbench MCP server or MCP integration with Blockbench. Include exact URLs, repository names, and any descriptions shown."}` → ``

- 🔧 **WebFetch** `{"url": "https://github.com/search?q=blockbench+mcp&type=repositories", "prompt": "List all repositories found related to \"blockbench mcp\". Include full repo names (owner/repo), descriptions, and star counts if visible."}` → `The GitHub search for "blockbench mcp" returned 19 total repository results, with 10 visible on page 1: - **jasonjgardner/blockbench-mcp-plugin** — "Adds MCP server to Blockbench" — 420 stars - **enfp-dev-studio/blockbench-mcp** — no description listed — 30 stars - **sosadly/blockbench-mcp** — "MCP server + Blockbench  …[截断,原长1345]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-09 23:29）

I'll research this topic by searching the web and GitHub for existing "Blockbench MCP" solutions.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

The GitHub search found several results. The most promising is `jasonjgardner/blockbench-mcp-plugin` with 420 stars. Let me look at that repo in detail, plus a couple others for comparison.

Let me fetch:
1. jasonjgardner/blockbench-mcp-plugin - README
2. jasonjgardner/blockbench-mcp-project
3. Maybe sosadly/blockbench-mcp

Let me fetch the main repo README first.

</details>

- 🔧 **WebFetch** `{"prompt": "Summarize this repository: what it is, architecture (Blockbench plugin vs MCP server), installation instructions (npx/uvx/docker command), required Blockbench plugin name and how to install it, MCP transport (stdio or HTTP/SSE) and exact endpoint URL/port, prerequisites (Java/Node/Python, OS), supported Minecraft editions, and any config JSON examples for MCP client …[截断,原长412]` → `# Blockbench MCP Plugin — Repository Summary ## What It Is This project "Adds MCP server to Blockbench," letting AI clients control the Blockbench 3D modeling tool through the Model Context Protocol. It includes both a Blockbench plugin and an MCP server component. ## Architecture - **Blockbench plugin**: loaded into t …[截断,原长2524]`

- 🔧 **WebFetch** `{"prompt": "Summarize this repository: what it is, architecture (Blockbench plugin vs MCP server), installation commands, required Blockbench plugin and installation method, MCP transport and endpoint URL/port, prerequisites, supported Minecraft editions, and any config JSON examples. Quote exact commands and JSON if present.", "url": "https://github.com/sosadly/blockbench-mcp" …[截断,原长381]` → `## Summary **blockbench-mcp** is a pairing of an MCP server and a Blockbench plugin. Per the repo's About line, it is an "MCP server + Blockbench plugin — lets AI assistants control Blockbench directly." An AI assistant can create Minecraft models, textures, and animations inside a live Blockbench window without manual …[截断,原长3214]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-09 23:29）

GitHub search found candidates. The most credible is `jasonjgardner/blockbench-mcp-plugin` (420 stars). Let me examine the top repos in detail.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

Good findings. Two solid candidates:
1. `jasonjgardner/blockbench-mcp-plugin` — the whole MCP server runs inside Blockbench as a plugin (HTTP streamable transport, port 3000, endpoint /bb-mcp). 420 stars. Plugin installed from URL.
2. `sosadly/blockbench-mcp` — bridge plugin in Blockbench (HTTP on 127.0.0.1:8787) + Node MCP server (stdio) built from source. 6 stars.

Let me dig deeper to verify details for the top candidate (jasonjgardner's), and check a few things:
- Verify the exact README content for jasonjgardner's repo — including port and env vars, firewall/Windows caveats, node requirements. Also that MCP server port configurable in settings.
- Check the sample project repo jasonjgardner/blockbench-mcp-project for extra context.
- Check if the plugin repo is actively maintained (recent commits, releases).
- Also check the plugin install URL works: https://jasonjgardner.github.io/blockbench-mcp-plugin/mcp.js
- Check page 2 of GitHub search results for other candidates (maybe "WaitMyDawn", "FFriends", "vasyacullin"). The main jasonjgardner repo is dominant with 420 stars.

Let me fetch more details:
1. Raw README from jasonjgardner/blockbench-mcp-plugin to get full text, including prerequisites (Node version, OS), any caveats about Windows, firewall, screenshots tooling.
2. GitHub API for repo metadata (stars, last push, license) for the top candidates.

Let me use raw.githubusercontent.com for the README.

</details>

- 🔧 **WebFetch** `{"prompt": "Output the complete raw README content verbatim, especially sections about: prerequisites (Node version, OS support, Windows), Blockbench plugin installation, MCP configuration examples with exact JSON, environment variables, ports, firewall or Windows-specific caveats, screenshots tooling, supported Minecraft editions (Java/Bedrock), security notes, and troubleshoo …[截断,原长412]` → ``

- 🔧 **WebFetch** `{"prompt": "Return JSON fields: full_name, description, html_url, stargazers_count, forks_count, pushed_at, updated_at, created_at, license, open_issues_count, homepage, topics, default_branch.", "url": "https://api.github.com/repos/jasonjgardner/blockbench-mcp-plugin"}` → `{ "full_name": "jasonjgardner/blockbench-mcp-plugin", "description": "Adds MCP server to Blockbench", "html_url": "https://github.com/jasonjgardner/blockbench-mcp-plugin", "stargazers_count": 420, "forks_count": 48, "pushed_at": "2026-07-03T17:42:23Z", "updated_at": "2026-09-08T18:54:37Z", "created_at": "2025-05-17T23: …[截断,原长670]`

- 🔧 **WebFetch** `{"prompt": "Return JSON fields: full_name, description, html_url, stargazers_count, forks_count, pushed_at, updated_at, created_at, license, open_issues_count, homepage, topics, default_branch.", "url": "https://api.github.com/repos/sosadly/blockbench-mcp"}` → ````json { "full_name": "sosadly/blockbench-mcp", "description": "MCP server + Blockbench plugin — lets AI assistants control Blockbench directly", "html_url": "https://github.com/sosadly/blockbench-mcp", "stargazers_count": 6, "forks_count": 3, "pushed_at": "2026-09-09T10:01:09Z", "updated_at": "2026-09-09T15:24:48Z",  …[截断,原长663]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-09 23:30）

Two credible projects found. Let me get the full README of the top candidate (jasonjgardner) and repo metadata for both, plus check page 2 of the search for completeness.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

The raw README fetch failed with ECONNRESET. Let me retry, maybe with a different branch or use github.com blob page. jasonjgardner's repo was pushed 2026-07-03, updated 2026-09-08. sosadly's was pushed 2026-09-09 (very active, but only 6 stars).

Interesting: sosadly/blockbench-mcp pushed 2026-09-09T10:01:09Z which is today-ish. jasonjgardner updated_at 2026-09-08 — probably updated due to star change.

Let me retry fetching the raw README of jasonjgardner's repo.

</details>

- 🔧 **WebFetch** `{"prompt": "Output the complete README content, especially sections about: prerequisites (Node version, OS support, Windows), Blockbench plugin installation, MCP configuration JSON examples, environment variables, ports, firewall or Windows-specific caveats, screenshot tooling, supported Minecraft editions (Java/Bedrock), security notes, and troubleshooting. Preserve exact code …[截断,原长412]` → `The page shows the GitHub rendering of the README for `jasonjgardner/blockbench-mcp-plugin`. Important caveat: the sections you asked about — prerequisites/Node version, OS support, environment variables, firewall or Windows-specific caveats, screenshot tooling, Minecraft Java/Bedrock edition support, security notes, a …[截断,原长2958]`

- 🔧 **WebFetch** `{"prompt": "Summarize what this website/documentation page is about: what the blockbench-mcp-plugin provides, install steps for the Blockbench plugin, MCP endpoint and port, any JSON config for MCP clients, prerequisites, versions, release notes, or FAQ items. Quote exact URLs, ports, and commands.", "url": "https://jasonjgardner.github.io/blockbench-mcp-plugin/"}` → `This page is the **API Reference for the Blockbench MCP Plugin (v1.6.1)** — a plugin that exposes Blockbench's 3D modeling, animation, texturing, and project tools through the Model Context Protocol. It does **not** contain endpoint/port details, JSON client config, prerequisites, release notes, or FAQ content; the onl …[截断,原长1515]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-09 23:31）

Let me retry the full README for the top repo and check the plugin homepage.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

I have very solid data on jasonjgardner's plugin. There's an important gap: I should check the homepage/docs more, and verify:
- Whether the plugin runs the MCP server itself inside Blockbench (i.e., user does not need to run a separate MCP server process — but for clients without native HTTP/SSE support they use `mcp-remote` / `mcp-add` bridge).
- Node.js requirement — actually the plugin runs inside Blockbench which is an Electron app with its own Node. So no Node needed for the plugin itself. But for Claude Desktop on Windows, `npx mcp-remote` requires Node.

Now, wait: I should double check the README for details I haven't captured about the architecture on jasonjgardner's repo. The README is short. Let me look at the repo file listing and maybe check for a CONTRIBUTING.md? Not needed.

Also I want to check:
1. The GitHub search page 2 for remaining repos to be thorough.
2. Check the sample project repo jasonjgardner/blockbench-mcp-project for caveats like screenshots usage.
3. Check what tools are available in the plugin's own homepage docs — capture_screenshot exists so AI can see the model (ImageMagick-like). Actually the docs said tools include capture_screenshot, camera stuff. But how does the AI "see" a screenshot? Possibly via the mcp screenshot resource. Let me not over-fetch; note tools exist.

Let me check page 2 of the GitHub search results to see other repos, and fetch jasonjgardner/blockbench-mcp-project README. Also, look for Windows-specific caveats. Also verify the "Files > Plugins" install method name from Blockbench docs — plugin load from URL requires plugin registration; loading a plugin from URL is standard Blockbench.

Also, does the plugin need Blockbench desktop? Both projects say desktop. Let me verify claims about the jasonjgardner plugin: it's an Electron app running MCP server on localhost:3000. The first fetch (github.com main page description) said architecture: plugin runs the MCP server locally via Blockbench settings. It uses Bun/TypeScript for the repo dev.

One question: does the jasonjgardner MCP server use HTTP streamable; yes — README says "url/type http", Cline uses streamableHttp; Claude Desktop uses mcp-remote (which bridges HTTP to stdio). So the transport exposed by Blockbench plugin is HTTP streamable at localhost:3000/bb-mcp.

Wait — is it SSE or streamable HTTP? "Cline: type streamableHttp". OK.

Now the older versions of this plugin used WebSocket? Not important.

Let me quickly also check issues in jasonjgardner's repo to identify Windows caveats. 7 open issues. Maybe fetch issues list via API: https://api.github.com/repos/jasonjgardner/blockbench-mcp-plugin/issues?state=open — a quick scan for Windows/firewall related issues.

And search page 2 results.

</details>

- 🔧 **WebFetch** `{"prompt": "List all repositories found on this page related to \"blockbench mcp\". Include full repo names (owner/repo), descriptions, and star counts if visible.", "url": "https://github.com/search?p=2&q=blockbench+mcp&type=repositories"}` → `This is page 2 of the GitHub repository search for "blockbench mcp." Nine repos appear on this page: 1. **CyperNexus/blockbench-mcp** — no visible description — TypeScript — 0 stars 2. **SwagRee/BlockBenchMCP** — "Minecraft-oriented Blockbench MCP: stdio adapter + desktop plugin over loopback WebSocket" — JavaScript —  …[截断,原长1453]`

- 🔧 **WebFetch** `{"prompt": "List the open issues with their titles, numbers, and creation dates. Flag any mentioning Windows, firewall, port, localhost, permissions, CORS, or connection problems.", "url": "https://api.github.com/repos/jasonjgardner/blockbench-mcp-plugin/issues?state=open&per_page=50"}` → `Here are the open items from the page, all with state "open" (two are pull requests): - #49 — "fix: await async codec.compile in export_model" (PR) — created 2026-07-17 - #48 — "feat: 1.7.0" (PR) — created 2026-07-03 - #47 — "[Feature] Display-settings tools: get/set_display_transform + enter_display_mode (fit cosmetic …[截断,原长1611]`

- 🔧 **WebFetch** `{"prompt": "Summarize this example project README: what it shows, how the Blockbench MCP plugin is used, any notes about screenshots, model formats (.bbmodel), Minecraft Java/Bedrock editions, or prompt workflows. Quote exact text of interest.", "url": "https://github.com/jasonjgardner/blockbench-mcp-project"}` → `The repository is a template workspace that demonstrates how to set up the Blockbench MCP plugin/server for AI-assisted 3D modeling, texturing, animation, and plugin development. Key points: - **Purpose**: It shows a project structure pairing the Blockbench MCP server with IDE/agent configs. The MCP connection defaults …[截断,原长1856]`

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-09 23:32）

The top repo's README is confirmed. Let me check the remaining search results on page 2, the sample project, and scan the top repo's open issues for Windows/firewall caveats.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-v4-flash）</summary>

I now have a good overall picture. Let me gather remaining verification details:

1. Verify the plugin "Files tab" claim: Blockbench plugin installation is via `File > Plugins` in the desktop app. Both candidates confirm. jasonjgardner's also loads from URL: `https://jasonjgardner.github.io/blockbench-mcp-plugin/mcp.js`.

2. For jasonjgardner's — issue #40 "Why did my MCP disappear after closing Blockbench?" — this is an important caveat: the MCP server runs inside Blockbench; closing Blockbench kills it. That matches architecture: MCP server lives inside the plugin (Blockbench app), no separate process.

3. Check whether jasonjgardner's plugin's tools include screenshot ability (yes: capture_screenshot, Camera & Screenshots category, per the API docs). Also "risky_eval", "undo/redo", export_model.

4. Details on versions: homepage says v1.6.1 and there's a PR for 1.7.0. Tools: 106 (39 stable, 67 experimental).

Now check remaining specifics:
- What Node is needed for mcp-remote bridging in Claude Desktop (that's a general mcp-remote requirement — Node 18+).
- Confirm Windows 10 support: Blockbench runs on Windows; the plugin is an Electron-based app plugin. Both fine. jasonjgardner README provides Windows-specific Claude Desktop config with cmd /c, indicating Windows support.

Maybe also quickly check the WaitMyDawn/blockbench-mcp repo and FFriends/Blockbench-MCP (page 1 results, 0 stars) — a quick scan to note other options. Also "mcp-blockbench" by achmadawdi? These are 0-star; I'll note them briefly as alternatives without deep detail.

I could also check the Blockbench docs for how plugins are installed from the Files tab ("Load Plugin from URL"/"from file") to describe the plugin store option. Actually Blockbench plugin manager supports loading plugins from URL — this is in Blockbench wiki "Plugins" page. Let me verify quickly with the Blockbench wiki: https://www.blockbench.net/wiki/guides/using-plugins or the docs. Search: blockbench.net docs plugin installation.

Let me do a couple of final checks in parallel:
- Quick scan of WaitMyDawn/blockbench-mcp and FFriends/Blockbench-MCP (0 stars, page 1) — to give a complete list of "others" and mark credibility.
- Blockbench wiki for plugin loading instructions ("Load Plugin from URL" and plugin store).
- Maybe verify the plugin mcp.js is actually hosted at that URL (HEAD request via WebFetch on the js file? It's JS code; fetch first lines to verify exists).

Let me fetch https://jasonjgardner.github.io/blockbench-mcp-plugin/mcp.js with prompt asking to confirm content type (it will return JS). Perhaps better to use Bash curl to check HTTP status quickly. curl should be available. Use Bash: curl -sI https://jasonjgardner.github.io/blockbench-mcp-plugin/mcp.js | head. That verifies hosting.

Also verify that Blockbench plugin install in app: blockbench wiki page https://www.blockbench.net/wiki/guides/using-plugins — fetch.

Then compile final structured summary.

</details>

- 🔧 **Bash** `{"command": "curl -sI -o /dev/null -w \"stable plugin mcp.js -> HTTP %{http_code}, %{size_download} bytes, content-type %{content_type}\\n\" https://jasonjgardner.github.io/blockbench-mcp-plugin/mcp.js; curl -s https://jasonjgardner.github.io/blockbench-mcp-plugin/mcp.js | head -c 600", "description": "Check plugin download URL responds and preview content"}` → `stable plugin mcp.js -> HTTP 200, 0 bytes, content-type application/javascript; charset=utf-8 /* v1.6.1 */ let process = requireNativeModule('process');var xF=Object.create;var{getPrototypeOf:yF,defineProperty:a4,getOwnPropertyNames:gF}=Object;var hF=Object.prototype.hasOwnProperty;function fF(Q){return this[Q]}var uF, …[截断,原长694]`

- 🔧 **WebFetch** `{"prompt": "Summarize how to install plugins in Blockbench desktop app: menu path, difference between Load Plugin from File vs URL vs the plugin store/Files tab, any notes about permissions, plugin visibility, version requirements (which Blockbench versions support plugins), and whether plugins can run in the web app. Quote exact menu paths.", "url": "https://www.blockbench.net …[截断,原长412]` → `The server returned HTTP 404 Not Found. The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.`

- 🔧 **WebFetch** `{"prompt": "What is this repo (owner/name)? Summarize its architecture: MCP server process vs Blockbench plugin, transport (stdio vs HTTP) and endpoint/port, install commands, prerequisites, supported Minecraft editions, Windows notes. Quote exact commands/JSON.", "url": "https://github.com/WaitMyDawn/blockbench-mcp"}` → ``

### 🤖 助手（`zcode-general-purpose` deepseek-v4-flash，2026-09-09 23:33）

I have the core picture. Let me verify the plugin download URL is live, confirm Blockbench's official plugin-loading mechanism, and briefly scan two more 0-star candidates from page 1.

> ⚠️ 该条助手消息出错: {"name": "AiSdkModelAdapterError", "data": {"message": "Insufficient Balance", "code": "model_request_failed", "attribution": {"source": "provider", "reason": "unknown", "providerId": "dd5b8267-05de-4 …[截断,原长399]
