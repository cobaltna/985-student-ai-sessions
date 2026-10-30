# 子代理会话 sess_subagent_agent_293541a6-bf29-42dd-8acd-a26132e6dfb7

模型: ?

## 👤 用户（2026-09-27 21:38）

I need accurate, citable facts about Minecraft Bedrock Edition addon scripting (游戏版本 1.21.113, script API @minecraft/server 1.13.0). Please use WebSearch/WebFetch (Microsoft Learn docs, wiki.bedrock.dev, GitHub issues) and answer these precisely. Quote the source URL for each answer.

QUESTION 1 — "stuck movement modifier" bug.
Items using `minecraft:use_modifiers` with a `movement_modifier` (e.g. 0.5) and a huge `minecraft:use_duration` (2147483647) are used as "charge/held" items. Problem reported by players: after holding to use the item and releasing, the player STAYS slowed as if still using/charging the item, until they switch the selected hotbar slot to another item. 
- Is this a known engine bug? What exactly causes the slow to persist? 
- What is the standard/known script-side fix or workaround? (e.g. re-setting the item stack in the inventory slot, `container.setItem`, clearCooldown, changing `minecraft:use_modifiers`, using `minecraft:cooldown` interplay, etc.) Give concrete code snippets if any exist in community discussions.
- Does the interaction of `minecraft:cooldown` starting while the item is still held cause the client "in use" state to persist?
- Specifically: does `minecraft:use_duration` with a value of 2147483647 (INT32 max) cause any clamping/overflow weirdness in the client's charge state?

QUESTION 2 — ItemCustomComponent events in @minecraft/server 1.13.0 (stable).
- List which item custom component events exist in 1.13.0 stable (`onUse`, `onUseOn`, `onHitEntity`, `onBeforeDurabilityDamage`, `onConsume`, `onCompleteUse`). Which ones were added in which version? Is `onConsume` available in 1.13.0? Is `onCompleteUse`?
- For a custom item that is also `minecraft:food` (with can_always_eat and using_converts_to), do script item custom components like onUse/onConsume/onCompleteUse still fire? Any known conflicts between the `minecraft:food` component and script item components?
- Signature details of `onConsume` / `onCompleteUse` in 1.13 (event field names: itemStack, source, etc.), and whether the handler can cancel the consumption.

QUESTION 3 — Bedrock item JSON.
- In `minecraft:food`, can effects be randomized on use? Is there any `randomize` / random effect mechanism? Confirm there is none, so randomization requires script.
- What does `minecraft:cooldown` do exactly, and when does the cooldown start for a `minecraft:food` item with `use_duration`?
- Is `minecraft:use_duration: 2147483647` valid/harmful? What is the documented maximum / recommended value for "hold indefinitely" items?

QUESTION 4 — Damage of `minecraft:explosion` / `minecraft:area_attack` on entity events, and how a fireball projectile's explosion damage is calculated in Bedrock (relevant to a custom fireball with explosion power 2 that occasionally does very high damage). What are the known causes of unexpectedly high explosion damage in Bedrock (e.g. exposure/distance multiplier, `minecraft:damage` + `minecraft:explosion` stacking, `breaks_blocks`, the `damage_multiplier` in the projectile's `minecraft:projectile` component)? Keep this concise.

Be precise and mark anything you could not verify as UNVERIFIED. Do not speculate silently.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

The user wants accurate, citable facts about Minecraft Bedrock addon scripting. But wait — I'm ZCode, a coding agent. I have WebFetch. Do I have WebSearch? The tool list includes WebFetch but not WebSearch explicitly. Let me check... The tools available: AskUserQuestion, Bash, Edit, Read, Skill, TaskOutput, TaskStop, TodoRead, TodoWrite, WebFetch, Write, RespondToCoordinator, ReadSessionContext, workflow tools, ListModels, and MCP solidworks tools, node_repl.

No WebSearch tool. So I can only use WebFetch with specific URLs. The user asked to use WebSearch/WebFetch. I can use WebFetch on known doc URLs.

Also note the working directory is a Minecraft lucky block map folder. Maybe the repo contains addon files relevant. But the question is about general facts.

Let me try to fetch Microsoft Learn docs. URLs:
- https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/itemcustomcomponent
- https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/itemcomponentregistry?view=minecraft-bedrock-stable
- wiki.bedrock.dev

Let me start with several WebFetch calls in parallel.

Actually, I should be careful: WebFetch answers via a small model against the page. Cross-host redirects returned. Let me try.

Let me plan URLs:

1. ItemCustomComponent events:
https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/itemcustomcomponent?view=minecraft-bedrock-stable
Also version-specific? Microsoft Learn has versioned views for stable. There's a "1.13.0" doc? Microsoft learn uses view=minecraft-bedrock-stable and there's a changelog. Version history: https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server-changelog?view=minecraft-bedrock-stable

2. onConsume: https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/itemcustomcomponent#onconsume (anchor may not work with WebFetch; it fetches whole page).

3. ItemUseAfterEvent etc.

4. minecraft:food docs: https://learn.microsoft.com/en-us/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_food
Actually the item component reference: https://learn.microsoft.com/en-us/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_food?view=minecraft-bedrock-stable

5. use_modifiers: https://learn.microsoft.com/en-us/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_use_modifiers
6. cooldown: minecraft_cooldown

7. Explosion damage: https://learn.microsoft.com/en-us/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraft_explosion? 

8. Projectile: minecraft_projectile.
9. area_attack: minecraft_area_attack.

Also wiki.bedrock.dev items page: https://wiki.bedrock.dev/items/items-intro

Let me also consider GitHub issues search via WebFetch of github search URL — might not render. Could fetch https://github.com/Mojang/bedrock-samples ... not issues.

Let me start fetching in parallel. I'll do a batch of WebFetch calls.

Given the model answering WebFetch is small, I should ask precise prompts.

Let me begin.

Also I should check the local directory for the addon — the user has a map with a custom fireball and charge item. That could give context on actual code. Let me list files too.

Let me do: Bash ls of the directory, plus WebFetch batch.

Actually the working dir has Chinese name. Let me use Bash with the path. Use `find` maybe. Let's just ls -R limited.

Let me batch tool calls: multiple WebFetch + one Bash.

I'll start.

</details>

- 🔧 **Bash** `{"command": "find \"/c/Users/UserX/Downloads/幸运方块地图_法杖增强版_竞技场版\" -maxdepth 3 -type d | head -50", "description": "List directory structure of the addon project"}` → `/c/Users/UserX/Downloads/幸运方块地图_法杖增强版_竞技场版 /c/Users/UserX/Downloads/幸运方块地图_法杖增强版_竞技场版/behavior_packs /c/Users/UserX/Downloads/幸运方块地图_法杖增强版_竞技场版/behavior_packs/BlockArmor BP V2.1.6 /c/Users/UserX/Downloads/幸运方块地图_法杖增强版_竞技场版/behavior_packs/BlockArmor BP V2.1.6/functions /c/Users/UserX/Downloads/幸运方块地图_法杖增强版_竞技场版/behavior …[截断,原长3789]`

- 🔧 **WebFetch** `{"url": "https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/itemcustomcomponent?view=minecraft-bedrock-stable", "prompt": "List ALL item custom component events documented on this page (e.g. onUse, onUseOn, onHitEntity, onBeforeDurabilityDamage, onConsume, onCompleteUse). For each: its exact signature, the event object type and its field names (itemS …[截断,原长412]` → `--- layout: Conceptual monikers: - minecraft-bedrock-stable - minecraft-bedrock-experimental defaultMoniker: minecraft-bedrock-stable versioningType: Ranged title: minecraft/server.ItemCustomComponent Interface | Microsoft Learn canonicalUrl: https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/serve …[截断,原长5145]`

- 🔧 **WebFetch** `{"url": "https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/itemcomponentregistry?view=minecraft-bedrock-stable", "prompt": "List the ItemCustomComponent interface fields: what properties (event names like onUse, onConsume, onCompleteUse, onBeforeDurabilityDamage, onHitEntity, onUseOn) are declared, and any @beta vs stable markers. Quote exactly."}` → `--- layout: Conceptual monikers: - minecraft-bedrock-stable - minecraft-bedrock-experimental defaultMoniker: minecraft-bedrock-stable versioningType: Ranged title: minecraft/server.ItemComponentRegistry Class | Microsoft Learn canonicalUrl: https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/ …[截断,原长3630]`

- 🔧 **WebFetch** `{"url": "https://learn.microsoft.com/en-us/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_food?view=minecraft-bedrock-stable", "prompt": "Reproduce the full documentation of minecraft:food: all fields (nutrition, saturation_modifier, can_always_eat, using_converts_to, effects, cooldown, etc.), their types and defaults. Is there any randomize …[截断,原长412]` → `--- layout: Conceptual monikers: - minecraft-bedrock-stable - minecraft-bedrock-experimental defaultMoniker: minecraft-bedrock-stable versioningType: Ranged title: Items Documentation - minecraft:food | Microsoft Learn canonicalUrl: https://learn.microsoft.com/en-us/minecraft/creator/reference/content/itemreference/exa …[截断,原长4023]`

- 🔧 **WebFetch** `{"url": "https://learn.microsoft.com/en-us/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_use_modifiers?view=minecraft-bedrock-stable", "prompt": "Reproduce the full documentation of minecraft:use_modifiers: fields (use_duration, movement_modifier), types, value ranges, defaults, and any notes or warnings."}` → `--- layout: Conceptual monikers: - minecraft-bedrock-stable - minecraft-bedrock-experimental defaultMoniker: minecraft-bedrock-stable versioningType: Ranged title: Items Documentation - minecraft:use_modifiers | Microsoft Learn canonicalUrl: https://learn.microsoft.com/en-us/minecraft/creator/reference/content/itemrefe …[截断,原长27920]`

- 🔧 **WebFetch** `{"url": "https://learn.microsoft.com/en-us/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_cooldown?view=minecraft-bedrock-stable", "prompt": "Reproduce the full documentation of minecraft:cooldown: fields (category, duration), types, defaults, and when the cooldown starts (on use start vs on use complete). Any notes about food or use_duratio …[截断,原长396]` → `--- layout: Conceptual monikers: - minecraft-bedrock-stable - minecraft-bedrock-experimental defaultMoniker: minecraft-bedrock-stable versioningType: Ranged title: Items Documentation - minecraft:cooldown | Microsoft Learn canonicalUrl: https://learn.microsoft.com/en-us/minecraft/creator/reference/content/itemreference …[截断,原长3508]`

### 🤖 助手（`zcode-general-purpose` deepseek-flash，2026-09-27 21:38）

I'll research this from official docs and community sources, and also check the local addon for context.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

Interesting — the ItemCustomComponent doc includes onMineBlock too, which is newer (probably 2.x). But the user asked about 1.13.0. The current stable docs are for a later version. I need version-specific info. Microsoft Learn has a changelog page: https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server-changelog?view=minecraft-bedrock-stable — that lists historical versions and what was added. Actually, there's a page "Script API changelog" that includes all versions with "Minecraft 1.21.x - @minecraft/server 1.x" entries.

Let me fetch that. Also the per-version docs exist: ?view=minecraft-bedrock-stable but there's a moniker for each version? Actually Microsoft Learn for Minecraft script API only has two monikers: stable and experimental. Historical info is in the changelog.

Also there is a "versioned" doc via npm? The actual API reports can be found on https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server-changelog

Let me fetch.

Also need ItemComponentConsumeEvent and ItemComponentCompleteUseEvent signatures. Let me fetch those.

Also the food doc: no randomize — confirm. The doc above lists only can_always_eat, nutrition, saturation_modifier, using_converts_to, remove_effects (deprecated). Note: effects field in minecraft:food?? The doc doesn't list "effects"! Hmm, actually in Bedrock the `minecraft:food` component historically supports "effects" array. The doc above didn't list it. Let me check bedrock-samples or wiki.bedrock.dev. Actually, wait: in Bedrock, the food effects are in `minecraft:food` with "effects" array? Let me verify. In Java, food has "effects". In Bedrock... The doc omitted effects. Hmm — historically Bedrock's `minecraft:food` had an "effects" field? Let me check bedrock-samples apple.json? Actually the samples show food without effects. Let me check wiki.bedrock.dev items page.

Hmm, actually I recall Bedrock's minecraft:food does NOT support effects; you need to use `minecraft:use_modifiers`... no. Actually there IS an "effects" property in minecraft:food in Bedrock. Let me verify via bedrock-samples GitHub (chicken? no). Let's search. Actually let me check the format: in Bedrock, `minecraft:food` fields per bedrock.dev include "effects" (array of effect with name, duration, amplifier, chance). I'm fairly sure Bedrock food supports effects with `chance` (which is a probability!). That's important for Q3 — "can effects be randomized on use?" — yes, there's a `chance` field making random application. Wait, but the MS doc doesn't list effects. Hmm. Let me verify carefully.

Actually I now recall bedrock food JSON:
```
"minecraft:food": {
  "nutrition": 4,
  "saturation_modifier": "normal",
  "can_always_eat": true,
  "effects": [
    {"name": "regeneration", "duration": 6, "amplifier": 0, "chance": 1.0}
  ]
}
```
Yes! Bedrock's minecraft:food does have `effects` with `chance`. That gives randomized effects via chance. So the answer to "can effects be randomized" is YES via `chance` in effects array — that's a probability, not uniform randomization among effects, but each effect independently rolls. Let me verify via a reliable source (bedrock-samples GitHub or bedrock.dev items docs or wiki.bedrock.dev).

The MS Learn doc appears incomplete (the table omitted effects). Let me check bedrock-samples repository for an item with effects, e.g. golden_apple? Bedrock's golden_apple uses minecraft:food with effects? Actually golden apple uses "minecraft:food" with effects? In bedrock-samples, items/golden_apple.json. Let's fetch raw from GitHub.

Let me do a batch:
- MS changelog for script API
- ItemComponentConsumeEvent doc
- ItemComponentCompleteUseEvent doc
- ItemComponentUseEvent doc
- bedrock-samples golden_apple.json raw
- wiki.bedrock.dev items page

WebFetch on raw.githubusercontent works.

Let me batch these.

Also for Q1 (stuck movement modifier bug), I need community discussion. Search GitHub issues: Mojang/bedrock-samples issues. Also the Microsoft Q&A / feedback. There's a known bug tracked at bugs.mojang.com (MCPE-...). Let me try fetching a Google/Bing search? WebFetch requires a URL; search engines may be blocked or return JS. Let me try duckduckgo html: https://html.duckduckgo.com/html/?q=... That sometimes works with WebFetch.

Let me try.

Batch 1:
1. MS changelog: https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server-changelog?view=minecraft-bedrock-stable
2. ItemComponentConsumeEvent
3. ItemComponentCompleteUseEvent
4. bedrock-samples golden_apple.json
5. wiki.bedrock.dev/items/items-intro
6. duckduckgo search for stuck movement modifier

Let me be efficient. I'll do them.

Wait, changelog page might be huge. The prompt should be targeted: "List every @minecraft/server version from 1.9.0 to 1.16.0 and which item custom component events (onConsume, onCompleteUse, onHitEntity, onBeforeDurabilityDamage, onMineBlock, onUse, onUseOn) were added in each."

Let me go.

</details>

- 🔧 **WebFetch** `{"prompt": "This is the Minecraft script API changelog. Find every entry mentioning item custom components / ItemCustomComponent and its events. Specifically: in which @minecraft/server version were onConsume, onCompleteUse, onHitEntity, onBeforeDurabilityDamage, onUse, onUseOn, onMineBlock added, and in which version(s) did they move from beta to stable (1.x.x). Quote the exac …[截断,原长412]` → `The server returned HTTP 404 Not Found. The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.`

- 🔧 **WebFetch** `{"prompt": "Reproduce the full documentation of ItemComponentConsumeEvent: all properties with types and descriptions (itemStack, source, etc.). Also note any version/moniker markers (@beta or stable).", "url": "https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/itemcomponentconsumeevent?view=minecraft-bedrock-stable"}` → `--- layout: Conceptual monikers: - minecraft-bedrock-stable - minecraft-bedrock-experimental defaultMoniker: minecraft-bedrock-stable versioningType: Ranged title: minecraft/server.ItemComponentConsumeEvent Class | Microsoft Learn canonicalUrl: https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/ser …[截断,原长2607]`

- 🔧 **WebFetch** `{"prompt": "Reproduce the full documentation of ItemComponentCompleteUseEvent: all properties with types and descriptions. Also note any version/moniker markers (@beta or stable).", "url": "https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/itemcomponentcompleteuseevent?view=minecraft-bedrock-stable"}` → `--- layout: Conceptual monikers: - minecraft-bedrock-stable - minecraft-bedrock-experimental defaultMoniker: minecraft-bedrock-stable versioningType: Ranged title: minecraft/server.ItemComponentCompleteUseEvent Class | Microsoft Learn canonicalUrl: https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft …[截断,原长2490]`

- 🔧 **WebFetch** `{"prompt": "Show the raw JSON content of this file, especially the minecraft:food component block with any effects array, chance values, nutrition, saturation_modifier.", "url": "https://raw.githubusercontent.com/Mojang/bedrock-samples/main/behavior_pack/items/golden_apple.json"}` → `The file defines `minecraft:golden_apple` with a `minecraft:food` component containing `"nutrition": 4`, `"saturation_modifier": "supernatural"`, `"can_always_eat": true`, and two effects. The first effect is `"name": "regeneration"`, `"chance": 1.0`, `"duration": 5`, `"amplifier": 1`. The second is `"name": "absorptio …[截断,原长465]`

- 🔧 **WebFetch** `{"prompt": "Find any documentation of the minecraft:food component including an \"effects\" array field (with name, duration, amplifier, chance) and any randomization. Also look for minecraft:use_modifiers, minecraft:cooldown, and any notes about use_duration limits, held/chargeable items, and stuck movement/slowness bugs. Quote exact text.", "url": "https://wiki.bedrock.dev/it …[截断,原长397]` → `The page provided is only the "Intro to Items" tutorial. It does not contain documentation for `minecraft:food`, nor any "effects" array (name, duration, amplifier, chance), randomization, `minecraft:use_modifiers`, `minecraft:cooldown`, use_duration limits, held/chargeable items, or stuck movement/slowness bugs. The o …[截断,原长678]`

### 🤖 助手（`zcode-general-purpose` deepseek-flash，2026-09-27 21:39）

Now let me pull version history and the specific event interfaces, plus community sources.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

bedrock-samples golden_apple.json confirms `effects` with `chance` field in minecraft:food. Good — that answers Q3 partly: yes, effects can be randomized via `chance`. But the MS Learn doc omitted `effects`. So I should cite bedrock-samples (GitHub raw) and note MS Learn omission.

Wait, but is the golden_apple sample using `minecraft:food` with effects? The fetch says yes. Let me verify by getting the raw text directly. Actually WebFetch summarized. Good enough but let me double-check by fetching the actual raw JSON content and reading key lines. Maybe better to fetch via Bash curl? Sandbox may block network. Let's try WebFetch again with a targeted prompt to output the food block verbatim. Actually already got: nutrition 4, saturation_modifier "supernatural", can_always_eat true, effects regeneration chance 1.0 duration 5 amplifier 1, absorption chance 1.0 duration 120 amplifier 0. And `"minecraft:use_duration": 32`?? Hmm, that's odd — maybe it's "minecraft:use_duration" not use_modifiers. Hmm, actually bedrock-samples golden_apple uses "minecraft:use_modifiers"? The summary says use_duration: 32. Hmm, wait, maybe it's actually `"minecraft:use_modifiers": {"use_duration": 32}`? Hmm. Actually let me double check; golden apple in bedrock has "minecraft:use_duration": 32 in older format. Hmm.

Anyway I need to verify the effects/chance in minecraft:food — the definitive source is bedrock-samples. Also the wiki.bedrock.dev item-components page. Let me fetch https://wiki.bedrock.dev/items/item-components? The fetch said links to /items/item-components. Let me fetch that.

Now for the changelog — the URL 404'd. Let me find the correct changelog URL. Options:
- https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server-changelog
Hmm 404. Maybe it's under /creator/scriptapi/minecraft/server/... Let me search. Actually the changelog might be at https://learn.microsoft.com/en-us/minecraft/creator/documents/scriptapi/... Hmm.

Alternatively, use the npm package @minecraft/server versions? Or GitHub: https://github.com/Mojang/bedrock-samples ... The script API version history is at https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server-changelog?view=minecraft-bedrock-stable — 404 means wrong path.

Let me try WebFetch on a search engine or on learn.microsoft.com search. Actually there's a known page: "Script API Changelog" at https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server-changelog. Hmm.

Let me think: The real one might be https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/... no.

Alternative: the "Minecraft Script API" docs have a page "Script Versioning" and "Changelog" per module: e.g. https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server-changelog?view=minecraft-bedrock-experimental

Hmm. Let me instead search via DuckDuckGo html.

Also I need info on which version added onConsume/onCompleteUse stable. From my knowledge: 
- Item custom components (ItemCustomComponent) were introduced in @minecraft/server 1.10.0-beta? Actually the item custom components were released... Let me recall the actual changelog:
  - @minecraft/server 1.9.0 (Minecraft 1.21.0): item custom components? Hmm.
  
Actually I recall: ItemCustomComponent with onUse, onUseOn, onHitEntity, onBeforeDurabilityDamage arrived in @minecraft/server 1.10.0 (Minecraft 1.21.0)? And onConsume/onCompleteUse in 1.11.0? Hmm. Let me verify with docs.

Known: Minecraft 1.21.0 (June 2024) shipped @minecraft/server 1.11.0? Let me recall version mapping:
- MC 1.20.80 → @minecraft/server 1.9.0? 
- MC 1.21.0 → @minecraft/server 1.11.0
- MC 1.21.20 → 1.12.0
- MC 1.21.30 → 1.13.0
- MC 1.21.40 → 1.14.0
- MC 1.21.50 → 1.15.0
- MC 1.21.60 → 1.16.0
- MC 1.21.70 → 1.17.0
- MC 1.21.80 → 1.18.0
- MC 1.21.90 → 1.19.0?
Hmm approximately.

Wait user says 游戏版本 1.21.113, script @minecraft/server 1.13.0. Hmm, 1.21.113 is a newer game version (1.21.11x?). Actually Minecraft Bedrock 1.21.100+ ... 1.21.113 might map to server 1.19.0? But the user explicitly says script API 1.13.0. Hmm, that's suspicious. Actually no — Bedrock game version 1.21.113 wouldn't pair with server 1.13.0. Hmm. But maybe their manifest is set to 1.13.0. Hmm. Actually let me reconsider: Bedrock versions 1.21.110/1.21.113? Hmm, I don't think 1.21.113 exists. Latest as of 2026-09 could be 1.21.11x. Hmm, actually Bedrock's version after 1.21.90 → 1.21.100 → ... Today's date is 2026-09-27 in this environment, so Bedrock could be at 1.21.130 or later (docs mention "requires format version of at least 1.26.30" and "1.21.130" — those are future-ish). Hmm, the docs we fetched mention 1.26.30 which is odd.

Anyway — the user asserts game 1.21.113 with @minecraft/server 1.13.0. Hmm, 1.21.113 could be a preview-like numbering. I should note the mapping ambiguity but focus on 1.13.0 semantics. Actually wait: maybe they mean the script API version written in manifest = "1.13.0". Let me just answer about 1.13.0 and flag the game-version mapping as something to verify.

Hmm, actually Minecraft Bedrock 1.21.11 is a real version (Oct 2024) with @minecraft/server 1.16.0? Let me not guess.

Let me get the changelog. Try URL variants and DuckDuckGo.

Known Microsoft Learn changelog URL format: 
https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server-changelog?view=minecraft-bedrock-stable

Hmm that's what I used and 404. Maybe it's "changelog" singular under /creator/scriptapi/minecraft/server/... Let me search.

Alternatively the full changelog is at:
https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server-changelog

Hmm. Let me try the docs repo on GitHub: MicrosooftDocs/minecraft-creator — but the pr repo. The changelog md might be at creator/ScriptAPI/minecraft/server/... Actually changelog pages: "creator/ScriptAPI/minecraft/server/minecraft-server-changelog.md"? Hmm.

Better: search GitHub for "@minecraft/server" 1.13.0 changelog. There's the bedrock-samples repo with a "ScriptAPI" or the "MinecraftScriptAPI" repo... Actually Mojang publishes npm @minecraft/server; the version history is also in the "bedrock-samples" repo? Hmm.

Let me try DuckDuckGo html search for "onConsume added @minecraft/server version changelog". And also fetch the Learn "Script API Versioning" or the changelog index.

Actually I recall the changelog URL is:
https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server-changelog?view=minecraft-bedrock-experimental

Let me just try DuckDuckGo.

Also for Q1, search for the stuck movement modifier bug. Try DuckDuckGo html.

Let me batch:
1. DDG search: site:bugs.mojang.com movement_modifier stuck
2. DDG search: "@minecraft/server" 1.13.0 changelog onConsume
3. bedrock-samples golden_apple raw again with "print the whole file verbatim"
4. wiki.bedrock.dev/items/item-components
5. Learn search page? https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/?view=minecraft-bedrock-stable

Let me do DDG with html.duckduckgo.com/html/?q=...

I'll try.

</details>

- 🔧 **WebFetch** `{"prompt": "List the search results: titles and URLs, especially any Microsoft Learn or bugs.mojang.com or bedrock wiki pages about item custom components changelog or version history.", "url": "https://html.duckduckgo.com/html/?q=%22%40minecraft%2Fserver%22+1.13.0+changelog+ItemCustomComponent+onConsume"}` → ``

- 🔧 **WebFetch** `{"prompt": "List the search results: titles and URLs. I am looking for bug reports or forum threads about Bedrock \"movement_modifier\" slow persisting / player stuck slowed after using a chargeable item, use_duration 2147483647, or minecraft:use_modifiers issues.", "url": "https://html.duckduckgo.com/html/?q=bedrock+movement_modifier+stuck+slow+player+after+use+use_duration+21 …[截断,原长390]` → ``

- 🔧 **WebFetch** `{"prompt": "Print the full raw JSON verbatim, especially the minecraft:food block including effects array entries with name/chance/duration/amplifier, and any use_modifiers / use_duration / cooldown components.", "url": "https://raw.githubusercontent.com/Mojang/bedrock-samples/main/behavior_pack/items/golden_apple.json"}` → `The JSON structure includes `"minecraft:stacked_by_data": true` and `"minecraft:use_duration": 32`, with `"minecraft:foil": false`. The `minecraft:food` block has `"nutrition": 4`, `"saturation_modifier": "supernatural"`, and `"can_always_eat": true`. Its effects array contains two entries. The first: `"name": "regener …[截断,原长526]`

- 🔧 **WebFetch** `{"prompt": "Find documentation for minecraft:food (including effects array with chance), minecraft:use_modifiers, minecraft:cooldown, minecraft:use_duration, and any notes about held/chargeable items, slowness/movement modifier persistence, or value limits. Quote exact text.", "url": "https://wiki.bedrock.dev/items/item-components"}` → `Based on the page, here's what's documented for your requested items: **minecraft:food** — "Allows the item to be consumed when used by players." It requires the use_modifiers component "with a defined use_duration component in order to function properly." For an eating/drinking animation, also apply the use_animation  …[截断,原长2905]`

- 🔧 **WebFetch** `{"prompt": "List all modules and their versions on this page, and find any link to a \"changelog\" or version history page. Give exact URLs.", "url": "https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/?view=minecraft-bedrock-stable"}` → `The server returned HTTP 404 Not Found. The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.`

### 🤖 助手（`zcode-general-purpose` deepseek-flash，2026-09-27 21:39）

Let me locate the version changelog and community bug reports.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

DuckDuckGo timed out (network restrictions maybe). WebFetch may block search engines. Let me try Bing? Or try the GitHub CLI (gh) which is available per instructions — "Use the `gh` CLI for GitHub operations". gh can search issues via API. Let's use Bash with gh to search issues across GitHub for "movement_modifier stuck".

But network access from Bash? The sandbox may allow. Let me try `gh api` search. Also `gh search issues`.

Also for Microsoft Learn changelog: let me find the right URL. Maybe try https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/changelog?view=minecraft-bedrock-stable — or the "Minecraft Script API" versioning page. Let me try a few candidates via WebFetch. Or use gh to search MicrosoftDocs/minecraft-creator for "changelog".

Actually the docs repo is MicrosoftDocs/minecraft-creator (private PR repo may not be accessible). There's also "Mojang/bedrock-samples" which contains a "ScriptAPI" folder? Hmm. Actually! bedrock-samples has a folder with the script API type definitions? There's a repo Mojang/bedrock-script-api? Hmm. Actually @minecraft/server npm package is published publicly, and the version changelogs are on npm: https://www.npmjs.com/package/@minecraft/server — but that's stable only latest.

Better approach for version history: Microsoft Learn has per-version documentation via "?view=minecraft-bedrock-stable" only. BUT there is a well-known community mirror of the script API changelog: https://github.com/Bedrock-OSS/bedrock-wiki ... Actually there's "bedrock-wiki" docs. And "Minecraft Bedrock Script API changelog" mirrored at https://github.com/Mojang/bedrock-samples? 

Hmm. Let me try gh search for the changelog content.

Alternatively, the changelog page might be at:
https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server-changelog?view=minecraft-bedrock-stable → 404.
Maybe /creator/documents/scriptapi/... no.

I recall the actual URL: https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/changelog — no.

Hmm, maybe the changelog is not per-module but "MinecraftScriptAPIChangelog". Let me try:
https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server-changelog-experimental

Let's instead use gh to grep the docs repo MicrosoftDocs/minecraft-creator for "onConsume" changelog. But changelog content may not be in that repo.

Alternative reliable source: npm. The @minecraft/server package on npm has versions. But changelog? Not really.

Another: the "Minecraft Script API" release notes in the official changelogs at feedback.minecraft.net / minecraft.net. Each Bedrock release notes lists script API changes. E.g., "Minecraft - 1.21.30 (Bedrock)" changelog lists "Script API" additions. Hmm.

Actually! There IS a known mirror: https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server-changelog ... I keep guessing.

Let me try the Learn site search via WebFetch: https://learn.microsoft.com/api/search?search=... That's an API returning JSON. Let's try:
https://learn.microsoft.com/api/search?search=minecraft%20server%20changelog&locale=en-us

That might work with WebFetch (returns JSON).

Also for community bug: use gh search issues.

Let me batch:
1. Bash: gh search issues "movement_modifier" --limit 20 (or gh api search)
2. WebFetch Learn search API
3. WebFetch bedrock-samples apple.json (to confirm use_modifiers apple sample)
4. WebFetch https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/itemcomponentuseevent?view=minecraft-bedrock-stable

Let me run gh commands. Note Bash needs gh installed and authenticated. Let's test.

I'll run: gh --version; gh auth status.

Let me do a combined bash call.

</details>

- 🔧 **Bash** `{"command": "gh --version 2>&1 | head -3; echo \"---AUTH---\"; gh auth status 2>&1 | head -5", "description": "Check gh CLI availability and auth"}` → `/usr/bin/bash: line 3: gh: command not found ---AUTH--- /usr/bin/bash: line 3: gh: command not found`

- 🔧 **WebFetch** `{"prompt": "Return the search results as a list of title + url. I am looking for the Minecraft Bedrock \"Script API changelog\" page and pages about item custom components.", "url": "https://learn.microsoft.com/api/search?search=minecraft%20server%20changelog&locale=en-us&%24top=15"}` → `Here are the search results (title + URL): 1. **Windows client documentation** — https://learn.microsoft.com/en-us/windows/resources/ 2. **Minecraft: Bedrock Edition Creator Documentation** — https://learn.microsoft.com/en-us/minecraft/creator/ 3. **Microsoft Graph documentation** — https://learn.microsoft.com/en-us/gr …[截断,原长3101]`

- 🔧 **WebFetch** `{"prompt": "Print the raw JSON verbatim and completely.", "url": "https://raw.githubusercontent.com/Mojang/bedrock-samples/main/behavior_pack/items/apple.json"}` → ``

- 🔧 **WebFetch** `{"prompt": "Reproduce full documentation of ItemComponentUseEvent and ItemComponentUseOnEvent: all properties and types.", "url": "https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/itemcomponentuseevent?view=minecraft-bedrock-stable"}` → `--- layout: Conceptual monikers: - minecraft-bedrock-stable - minecraft-bedrock-experimental defaultMoniker: minecraft-bedrock-stable versioningType: Ranged title: minecraft/server.ItemComponentUseEvent Class | Microsoft Learn canonicalUrl: https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/ …[截断,原长2560]`

### 🤖 助手（`zcode-general-purpose` deepseek-flash，2026-09-27 21:39）

WebFetch can't reach search engines here. Let me use the GitHub CLI for issue searches and the Learn search API.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

Found: changelog pages exist per module at /creator/scriptapi/minecraft/server/changelog. Let me fetch https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/changelog?view=minecraft-bedrock-stable

That should list all versions and additions. Let me fetch it.

Also need to search community for the movement bug. gh not available. Maybe curl available in bash? Let me test network with curl to GitHub API. The sandbox may allow. Let me test: curl -s "https://api.github.com/search/issues?q=movement_modifier+repo:Mojang/bedrock-samples" — but bedrock-samples issues may be disabled. Community bug reports live at bugs.mojang.com (Jira). We could query Jira REST: https://bugs.mojang.com/rest/api/2/search?jql=... That's public. Let me try with curl.

Also Minecraft feedback site. And the bedrock-OSS discord (not fetchable).

Let me try curl for:
- api.github.com search issues q="movement_modifier"
- bugs.mojang.com REST search

Let me run bash curl tests.

Also fetch the changelog.

Batch:
1. WebFetch server changelog
2. Bash curl github search
3. Bash curl bugs.mojang.com jira search

Let me do it.

</details>

- 🔧 **WebFetch** `{"prompt": "This is the @minecraft/server changelog. For EVERY version from 1.9.0 through 1.17.0, list the version number, its Minecraft game version if shown, and any lines mentioning item custom components (ItemCustomComponent), onUse, onUseOn, onHitEntity, onBeforeDurabilityDamage, onConsume, onCompleteUse, onMineBlock, ItemComponentConsumeEvent, ItemComponentCompleteUseEven …[截断,原长412]` → `# @minecraft/server Changelog: Item Custom Component Events (1.9.0–1.17.0) **Important caveat up front:** The changelog excerpt provided contains **no explicit "Minecraft game version"** column — each version heading is simply the `@minecraft/server` module version (e.g., `1.12.0`), with no game build number shown. So  …[截断,原长5491]`

- 🔧 **Bash** `{"command": "curl -s -m 25 \"https://api.github.com/search/issues?q=movement_modifier+in:title,body&per_page=20\" 2>&1 | head -c 3000; echo; echo \"=== EXIT $? ===\"", "description": "Search GitHub issues for movement_modifier"}` → `{ "total_count": 7, "incomplete_results": false, "items": [ { "url": "https://api.github.com/repos/forkfulloffuzz/The_Blobular_Manace/issues/24", "repository_url": "https://api.github.com/repos/forkfulloffuzz/The_Blobular_Manace", "labels_url": "https://api.github.com/repos/forkfulloffuzz/The_Blobular_Manace/issues/24/ …[截断,原长2518]`

- 🔧 **Bash** `{"command": "curl -s -m 25 \"https://bugs.mojang.com/rest/api/2/search?jql=text~%22movement_modifier%22&maxResults=15&fields=key,summary,status,resolution\" 2>&1 | head -c 4000; echo; echo \"=== EXIT $? ===\"", "description": "Search Mojang bug tracker for movement_modifier"}` → `<!doctype html> <html lang="en"> <head> <meta charset="utf-8" /> <title>Mojira Public Bug Tracker</title> <base href="/" /> <meta name="viewport" content="width=device-width, initial-scale=1" /> <link rel="icon" type="image/x-icon" href="./favicon.ico" /> <script type="module" crossorigin src="./assets/index-CD-6x8-Z.j …[截断,原长713]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

Network works via curl. GitHub search API works (unauthenticated, rate-limited). The Mojira public bug tracker has a new API. Let me find its API endpoint. The new Mojira is a React SPA at bugs.mojang.com with API endpoints. Let me probe: https://bugs.mojang.com/api/... Common: https://bugs.mojang.com/rest/api/2/search was old Jira; now maybe https://bugs.mojang.com/api/issues?query=... Let me probe.

Also GitHub search: I should search in the bedrock-addons community repos. Better: search GitHub code/issues for "movement_modifier" together with minecraft. Let me refine query: `movement_modifier minecraft` in issues, and also search repos like "Bedrock-OSS/bedrock-wiki".

Actually a better source for the "stuck movement modifier" bug: the Mojang bug tracker. Let me find the new API. Try:
- https://bugs.mojang.com/api/v1/... 
- The SPA probably calls something like https://bugs.mojang.com/api/search?jql=...
Let me curl the JS bundle to find API paths? That's heavy. Alternatively, there's the legacy Jira REST still available at https://bugs.mojang.com/rest/api/2/... but returns the SPA HTML now (redirect to index). Hmm.

Let me probe a few endpoints quickly.

Also try the Minecraft feedback site? Or search via GitHub for the specific community: "bedrock" "movement_modifier" repositories/issues.

Another good source: the "Minecraft Bedrock Script API" docs changed; but the user's Q1 is about engine bug — community knowledge. Good sources: 
- GitHub issues in "Mojang/bedrock-samples" (issues may be there)
- Reddit r/MinecraftCommands (WebFetch of reddit may work)
- The "bedrock.dev" Discord (not fetchable)

Let me try GitHub search with better queries and also search code for "2147483647" use_duration.

Queries:
- `"use_duration" 2147483647` in code (needs auth for code search). Unauthenticated code search not allowed.
- issues: `"use_duration" minecraft` 
- issues: `movement_modifier`

Let me also try searching GitHub for repos of bedrock addons referencing "movement_modifier" stuck.

Also there is a well-known GitHub repo "Bedrock-OSS/bedrock-wiki" — search issues there.

Alternatively, use the Bing search via curl? Let me try curl to duckduckgo html (WebFetch failed but curl might work).

Let me batch several curl calls:
1. DDG html search (curl with UA)
2. Mojira API probe
3. GitHub issues search refined

Let me run.

</details>

- 🔧 **Bash** `{"command": "UA=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64)\"\necho \"=== DDG movement_modifier ===\"\ncurl -s -m 25 -A \"$UA\" \"https://html.duckduckgo.com/html/?q=%22movement_modifier%22+bedrock+stuck+slow+item\" 2>&1 | sed -e 's/<[^>]*>//g' | grep -v '^\\s*$' | head -60\necho \"=== EXIT $? ===\"", "description": "Search DuckDuckGo for movement_modifier stuck slow"}` → `=== DDG movement_modifier === === EXIT 0 ===`

- 🔧 **Bash** `{"command": "echo \"=== mojira probe ===\"\nfor u in \"https://bugs.mojang.com/api/issues?search=movement_modifier\" \"https://bugs.mojang.com/api/v1/issues?query=movement_modifier\" \"https://bugs.mojang.com/api/search?query=movement_modifier\" \"https://bugs.mojang.com/rest/api/2/search?jql=text~%22movement%20modifier%22&maxResults=5\"; do\n echo \"--- $u\"\n curl -s -m 15 -H …[截断,原长410]` → `=== mojira probe === --- https://bugs.mojang.com/api/issues?search=movement_modifier <!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8"> <title>Error</title> </head> <body> <pre>Cannot GET /api/issues</pre> </body> </html> --- https://bugs.mojang.com/api/v1/issues?query=movement_modifier <!DOCTYPE html> <htm …[截断,原长1127]`

- 🔧 **Bash** `{"command": "echo \"=== GH issues: movement_modifier minecraft ===\"\ncurl -s -m 25 \"https://api.github.com/search/issues?q=movement_modifier+minecraft&per_page=20\" 2>&1 | python -c \"import sys,json;d=json.load(sys.stdin);[print(i['html_url'],'|',i['title']) for i in d.get('items',[])]\" 2>&1 | head -30\necho \"=== GH issues: use_modifiers ===\"\ncurl -s -m 25 \"https://api. …[截断,原长412]` → `=== GH issues: movement_modifier minecraft === /usr/bin/bash: line 4: python: command not found === GH issues: use_modifiers === /usr/bin/bash: line 6: python: command not found`

### 🤖 助手（`zcode-general-purpose` deepseek-flash，2026-09-27 21:40）

Network works via curl. Let me search more sources.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

python not in bash PATH (per memory). Use pwsh or full conda path. Or parse with grep/sed... but instructions discourage cat/sed for reading, though for network JSON parsing it's fine-ish. Memory says: "调 python 或需中文输出一律用 pwsh". Also "有 python（非无）：docx 用 conda opencv". Let me find conda python path. Memory index file ~/.zcode/memory/python-envs.md. Let me just use `pwsh -Command` with ConvertFrom-Json, or use node which is available (node_repl is MCP but not shell?). Actually Node might be installed given browser-use. Let me try `node -e`.

Simpler: use grep on the JSON for html_url/title. But titles have unicode. Let's just use node.

Let me check node availability.

Also Mojira new API: the SPA probably uses something like /api/v1/... but maybe requires POST. Let me look at the JS bundle for API paths. Fetch the index js and grep for "api/". Could be large (~MB). Let's try grep with head.

Actually there might be a simpler approach: Mojira's new search UI URLs like https://bugs.mojang.com/browse/MCPE-xxxxx still work? The old Jira browse pages are gone now. Hmm.

Let me try the old Jira REST with a different host? Possibly bugs.mojang.com was migrated to a custom tracker. Let me grep the JS bundle.

Let me batch:
1. node availability + GH search parse
2. grep JS bundle for api endpoints

Also try DDG lite: https://lite.duckduckgo.com/lite/?q=... Curl to html.duckduckgo returned empty — maybe blocked. Try Bing? curl to www.bing.com/search?q=... with UA. Or Startpage. Let me try Bing.

Also try Google via curl (likely blocked).

Let me run.

</details>

- 🔧 **Bash** `{"command": "which node; node --version 2>&1\necho \"=== GH issues: movement_modifier minecraft ===\"\ncurl -s -m 25 \"https://api.github.com/search/issues?q=movement_modifier+minecraft&per_page=30\" -o /tmp/gh1.json 2>&1\nnode -e \"const d=require('/tmp/gh1.json');console.log('total',d.total_count);(d.items||[]).forEach(i=>console.log(i.html_url,'|',i.title))\" 2>&1 | head -40 …[截断,原长412]` → `/c/Program Files/nodejs/node v24.13.0 === GH issues: movement_modifier minecraft === node:internal/modules/cjs/loader:1424 throw err; ^ Error: Cannot find module '/tmp/gh1.json' Require stack: - C:\Users\UserX\Downloads\幸运方块地图_法杖增强版_竞技场版\[eval] at Module._resolveFilename (node:internal/modules/cjs/loader:1421:15) at de …[截断,原长1831]`

- 🔧 **Bash** `{"command": "UA=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36\"\necho \"=== BING ===\"\ncurl -s -m 25 -A \"$UA\" \"https://www.bing.com/search?q=%22movement_modifier%22+minecraft+bedrock+stuck+slow\" 2>&1 | sed -e 's/<[^>]*>/ /g' | tr -s ' \\n' ' \\n' | grep -i -E \"movement|slow|stuck\" | head -30\necho \"=== END == …[截断,原长412]` → `=== BING === === END ===`

- 🔧 **Bash** `{"command": "echo \"=== fetch mojira bundle and grep api paths ===\"\ncurl -s -m 30 \"https://bugs.mojang.com/assets/index-CD-6x8-Z.js\" -o /tmp/mojira.js 2>&1\nls -la /tmp/mojira.js\ngrep -o -E '\"/[a-zA-Z0-9_/.-]*(search|issues|api)[a-zA-Z0-9_/.-]*\"' /tmp/mojira.js 2>/dev/null | sort -u | head -40\necho \"--- base url patterns ---\"\ngrep -o -E 'https://[a-zA-Z0-9_./-]+' /tm …[截断,原长412]` → `=== fetch mojira bundle and grep api paths === -rw-r--r-- 1 user 197121 209419 Sep 27 21:42 /tmp/mojira.js --- base url patterns --- https://reactrouter.com/v6/upgrading/future https://www.atlassian.com/legal/atlassian-customer-agreement https://www.atlassian.com/legal/privacy-policy https://www.microsoft.com/en-us/pri …[截断,原长464]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

The /tmp path mismatch: curl wrote to /tmp/gh1.json in the bash (MSYS) filesystem, but node (Windows) sees /tmp as C:\... hmm actually node resolved /tmp/gh1.json relative? It said Cannot find module '/tmp/gh1.json' — node on Windows treats /tmp as C:\tmp. So use a Windows-friendly path. Let me write to the current directory or use bash-native parsing.

Simplest: have curl output to stdout and pipe to node via stdin: `node -e "let s='';process.stdin.on('data',d=>s+=d).on('end',()=>{...})"`. Or use `node --input-type=module` reading stdin. Let me do: curl ... | node -e "const fs=require('fs');const d=JSON.parse(fs.readFileSync(0,'utf8'));...".

Also check the mojira bundle for API endpoints didn't find. Let me grep for 'fetch(' or 'API' or 'graphql' or '/rest/'. Let me grep more broadly.

Actually the SPA might call https://bugs.mojang.com/api/... via relative fetch. grep found nothing for (search|issues|api). Let me grep for "/v1" or "jql" or "searchIssues". Let me grep for quoted strings containing '/'.

Alternatively, Mojira's new public tracker may have a public GraphQL. Let me search bundle for "graphql".

Let me also consider that the "stuck movement modifier" bug might be reported on the Minecraft feedback site (feedback.minecraft.net) which is Jira-based (Atlassian) at https://feedback.minecraft.net/hc/... hmm. Actually Minecraft feedback moved to a new site.

Alternative community sources reachable:
- GitHub repos of bedrock scripts (issue search)
- Reddit via old.reddit.com JSON API (curl works? reddit blocks some but JSON with UA may work)
- StackOverflow? Not much.
- The "bedrock-oss" wiki.

Let me try reddit search JSON: https://www.reddit.com/search.json?q=movement_modifier%20bedrock&limit=25 with UA.

Also search GitHub for "movement_modifier" in code (unauthenticated code search requires auth), so skip.

Let me also grep mojira bundle for endpoints.

Batch:
1. curl | node for GH searches (fix path)
2. reddit search json
3. mojira bundle grep for graphql/api

Let me go.

</details>

- 🔧 **Bash** `{"command": "P='\"per_page\":30'\nq1=\"movement_modifier+minecraft\"\nq2=\"%22use_modifiers%22\"\nq3=\"%22use_duration%22+minecraft+item\"\nfor q in \"$q1\" \"$q2\" \"$q3\"; do\n echo \"=== QUERY: $q ===\"\n curl -s -m 25 \"https://api.github.com/search/issues?q=$q&per_page=30\" | node -e \"let s='';process.stdin.on('data',d=>s+=d);process.stdin.on('end',()=>{try{const d=JSON.p …[截断,原长410]` → `=== QUERY: movement_modifier+minecraft === total 1 https://github.com/MCNeteaseDevs/SDK-Campaign/issues/143 | [Feature] 额外减速效果 === QUERY: %22use_modifiers%22 === total 22 https://github.com/Weisl/simple_collider/issues/677 | Support collider generation for Empties with Geometry Nodes geometry (Blender 5.2+) https://git …[截断,原长4368]`

- 🔧 **Bash** `{"command": "UA=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36\"\necho \"=== REDDIT search: movement_modifier ===\"\ncurl -s -m 25 -A \"$UA\" \"https://www.reddit.com/search.json?q=movement_modifier%20bedrock&limit=25&sort=relevance\" | node -e \"let s='';process.stdin.on('data',d=>s+=d);process.stdin.on('end',()=>{tr …[截断,原长413]` → `=== REDDIT search: movement_modifier === ERR === REDDIT search: use_modifiers charge === ERR`

- 🔧 **Bash** `{"command": "echo \"=== mojira endpoints ===\"\ngrep -o -E '(fetch|axios)\\([^)]{0,60}' /tmp/mojira.js | head -20\necho \"--- graphql / v1 / rest ---\"\ngrep -o -E '(graphql|/v1/[a-z-]+|/rest/[a-z0-9/]+|apiUrl|baseUrl)[^\",;)]{0,50}' /tmp/mojira.js | sort -u | head -40\necho \"--- quoted url-ish strings ---\"\ngrep -o -E '\"[a-zA-Z0-9_./-]*(search|issue|ticket|bug)[a-zA-Z0-9_./ …[截断,原长412]` → `=== mojira endpoints === fetch(e.href,n fetch({cancelRefetch:!1} fetch({cancelRefetch:!1} fetch(e,t fetch({...e}={} fetch({...e} fetch( fetch(e fetch(this.options,e fetch(void 0,n fetch(t fetch(t fetch( fetch(`${e.apiBaseUrl}/api/${Da.siteInfo}` fetch(`${e.apiBaseUrl}/api/${Da.serverTime}` fetch(e.apiBaseUrl+`/api/`+t, …[截断,原长499]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

The GitHub search results are noisy. Reddit JSON returned empty (blocked or needs different UA/headers).

Mojira new API: `${e.apiBaseUrl}/api/${siteInfo}` and POST /api/{t}. So there's an apiBaseUrl, and endpoints like /api/{something}. Let me grep for `apiBaseUrl` assignment and for POST paths. Also there might be endpoints like `/api/search-issues` or `/api/issues`. Let me grep for backtick template strings containing "/api/".

Let me grep: grep -o -E '\$\{[a-zA-Z.]*\}[^`]{0,40}/api/[^`]{0,60}' mojira.js | sort -u

Also grep for "apiBaseUrl" context.

Alternatively the new tracker may be "Mojira" open-source: the front-end repo? There is a known open-source Mojira public tracker frontend: "mojira" by ... Hmm. The new bugs.mojang.com is powered by "Atlassian"? No, it's a custom React app with title "Mojira Public Bug Tracker". Possibly powered by https://github.com/mojang/... not public.

Let me grep for the actual POST endpoint names.

Actually, a much better approach for Q1: search the community for the specific workaround. Known community resource: the Bedrock Script API community often discusses on GitHub in "Bedrock-OSS/bedrock-wiki" or the "minecraft-bedrock-scripts"? Or the bedrock.dev Discord. Another good citable source: the "Minecraft Bedrock" GitHub issue on "Mojang/bedrock-samples" — but issues might exist there. Let me check the repo's issues via API: repo:Mojang/bedrock-samples type:issue.

Also there's the official "Minecraft Feedback" / "bugs.mojang.com" — if I can find a MCPE ticket number, that's the best citation. Let me find the Mojira API.

Let me grep the bundle more.

Also try the mobile API: maybe https://bugs.mojang.com/api/searchIssues. Let's grep for strings after `/api/`.

Let me run: grep -o -E '/api/[a-zA-Z0-9_/-]+' mojira.js | sort -u

That should reveal endpoints.

Also there might be a separate chunk file. The index bundle is 209KB; endpoints might be in it.

Let me run.

</details>

- 🔧 **Bash** `{"command": "echo \"=== /api/ literals ===\"\ngrep -o -E '/api/[a-zA-Z0-9_{}$-]+' /tmp/mojira.js | sort -u | head -40\necho \"=== apiBaseUrl context ===\"\ngrep -o -E '.{80}apiBaseUrl.{120}' /tmp/mojira.js | head -10\necho \"=== POST template ===\"\ngrep -o -E '.{0,120}method:`POST`.{0,120}' /tmp/mojira.js | head -10", "description": "Extract Mojira API endpoint names from bund …[截断,原长384]` → `=== /api/ literals === ugrep: invalid option -/[a-zA-Z0-9_{}$-]+ For more help, run `ugrep --help' or `ugrep --help -/[a-zA-Z0-9_{}$-]+' === apiBaseUrl context === on Qu({config:e}){let{data:t,isLoading:n,isError:r}=St({queryKey:[`site-info`,e.apiBaseUrl],queryFn:async()=>{let t=await fetch(`${e.apiBaseUrl}/api/${Da.si …[截断,原长1126]`

- 🔧 **Bash** `{"command": "echo \"=== GH: repo:Mojang/bedrock-samples issues mentioning movement ===\"\ncurl -s -m 25 \"https://api.github.com/search/issues?q=repo:Mojang/bedrock-samples+movement_modifier\" | node -e \"let s='';process.stdin.on('data',d=>s+=d);process.stdin.on('end',()=>{const d=JSON.parse(s);console.log('total',d.total_count);(d.items||[]).forEach(i=>console.log(i.html_url, …[截断,原长413]` → `=== GH: repo:Mojang/bedrock-samples issues mentioning movement === total 0 === GH: any repo, item chargable stuck === --- chargeable+item+stuck+slow+minecraft total 0 --- item+slowness+persists+minecraft+bedrock+script total 0 --- %22movement_modifier%22+in:body total 6 https://github.com/forkfulloffuzz/The_Blobular_Ma …[截断,原长952]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

GitHub search isn't finding the Minecraft community discussion. The mojira apiBaseUrl is empty in the bundle (set at runtime via config), so the SPA posts to `/api/<something>` on the same host. Let's find the POST endpoint names: grep for the function that builds endpoints, e.g. strings in an enum Da like siteInfo/serverTime. Let me grep for `Da=` definition.

grep -o -E 'Da=\{[^}]{0,300}' mojira.js

Also grep for endpoint enum with names like `searchIssues`, `issueDetails`.

Let me try: grep -o -E '[A-Za-z]+:`[a-z-]+`' mojira.js | sort -u | head -60 → find endpoint strings.

Then try POST to https://bugs.mojang.com/api/<endpoint>.

Alternatively, maybe there is a simpler public Jira REST: The new Mojira might still proxy /rest/api/2? We saw it returns index.html. Hmm.

Let me look at the enum.

Also, an alternative citable community source for Q1: the official Minecraft bug tracker tickets can be searched via Google cache? Hmm.

Actually! I recall a very relevant, well-known Mojira ticket: MCPE-178111? Hmm, I shouldn't guess.

Let me try harder to get the Mojira API.

Also, let me reconsider Q1 sources: The user asks "Is this a known engine bug? What exactly causes the slow to persist?" Community discussions on this specific issue may be scarce. But there IS relevant known knowledge: `minecraft:use_modifiers.movement_modifier` applies while "item is in use"; the client's "in use" state for edible items is driven by `use_duration`; with a huge duration the item stays "in use" pending; releasing... Actually in Bedrock, holding right-click with a food item plays eating continuously and movement slows. If use_duration is enormous, the use never "completes". On release, the client should stop. The reported bug where the slow persists until hotbar switch smells like the client's ItemUse state not being cleared because `onCompleteUse`/stop-use doesn't fire when duration exceeds some limit, or because `minecraft:cooldown` was applied.

Hmm, I must be careful not to speculate. I'll mark causes as UNVERIFIED where I can't cite.

But I can cite documented facts:
- use_duration is "Time, in seconds, that the item takes to use" (MS Learn). 2147483647 seconds = ~68 years; as INT32 max it's likely the max accepted. Whether it overflows is UNVERIFIED. But we can note the doc has no stated max, and movement_modifier must be <= 1.
- There's also the "start_using: if_first" option (1.26.30) — interesting, not relevant.

Let me try the Mojira API enumeration, then also try fetching a known community wiki page on item components with a "held item" pattern — e.g., wiki.bedrock.dev "items/item-components" (already fetched). Also there's "bedrock.dev" docs and "wiki.bedrock.dev/items/items-1.21.60" etc.

Another important source: the official bedrock-samples "documentation" for item components? There's the "ItemComponents" doc json.

Also for Q4: minecraft:explosion, minecraft:projectile damage_multiplier, area_attack. Let me fetch those MS Learn pages:
- https://learn.microsoft.com/en-us/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraft_explosion
- .../minecraft_projectile
- .../minecraft_area_attack
- .../minecraft_damage (for "minecraft:damage" + explosion stacking)

Also the wiki.bedrock.dev entity components page and "projectiles" page.

Let me batch these WebFetch calls plus the mojira grep.

Let me do it.

</details>

- 🔧 **Bash** `{"command": "echo \"=== endpoint enum strings ===\"\ngrep -o -E '`[a-z][a-z-]{2,30}`' /tmp/mojira.js | sort -u | head -60\necho \"=== 'Da=' def ===\"\ngrep -o -E 'Da=\\{[^}]{0,400}' /tmp/mojira.js | head -3\necho \"=== assignments like X={a:\\\"..\\\"} near api ===\"\ngrep -o -E 'siteInfo[^,}]{0,40}' /tmp/mojira.js | head -5", "description": "Enumerate Mojira API endpoint ident …[截断,原长388]` → `=== endpoint enum strings === `abort` `aborted` `action` `active` `activity` `added` `all` `alt` `always` `animate` `annotation-xml` `annotation` `anonymous` `app-container` `aria-hidden` `aside` `atlassian` `attachments` `attributename` `attributes` `audio` `auto` `backward` `banner-dismiss` `banner-message` `basic-se …[截断,原长1175]`

- 🔧 **WebFetch** `{"prompt": "Reproduce the full documentation of minecraft:explosion: all fields, types, defaults, and descriptions. Include anything about damage, breaks_blocks, causes_fire, destroy_affected_by_griefing, allow_underwater, and how entity damage is calculated.", "url": "https://learn.microsoft.com/en-us/minecraft/creator/reference/content/entityreference/examples/entitycomponent …[截断,原长412]` → `The server returned HTTP 404 Not Found. The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.`

- 🔧 **WebFetch** `{"prompt": "Reproduce the full documentation of the minecraft:projectile component: all fields, especially damage_multiplier (or similar damage scaling), hit_sound, on_hit, and anything about how explosion damage from the projectile is scaled or calculated.", "url": "https://learn.microsoft.com/en-us/minecraft/creator/reference/content/entityreference/examples/entitycomponents/ …[截断,原长412]` → `The server returned HTTP 404 Not Found. The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.`

- 🔧 **WebFetch** `{"prompt": "Reproduce the full documentation of minecraft:area_attack: all fields (damage_per_tick, damage_range, entity_filter, cause) and how damage is applied.", "url": "https://learn.microsoft.com/en-us/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraft_area_attack?view=minecraft-bedrock-stable"}` → `The server returned HTTP 404 Not Found. The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

Found the Mojira endpoint enum. Key endpoints: `jql-search-get`, `jql-search-post`, `basic-search-get`, `list-issues`, etc. Let me try:

POST https://bugs.mojang.com/api/jql-search-post with body {"jql":"text ~ \"movement_modifier\""}? Need to know exact payload. Let me grep for jql-search-post usage and payload keys.

Let me grep for `jql` and `basicSearch` usage.

Also GET https://bugs.mojang.com/api/basic-search-get?query=... Let me try a few.

Meanwhile, the entity component doc URLs 404'd — need correct paths. Let me find the right URL pattern. Earlier item component URL was /creator/reference/content/itemreference/examples/itemcomponents/minecraft_food. For entity: /creator/reference/content/entityreference/examples/entitycomponents/minecraft_explosion — hmm 404. Maybe it's "entitycomponents" vs "entitycomponents"? Let me search Learn API for "minecraft:explosion".

Use https://learn.microsoft.com/api/search?search=minecraft%20explosion%20entity%20component

Let me batch:
1. curl mojira basic-search-get / jql-search
2. Learn search API for explosion/projectile/area_attack
3. grep mojira for jql payload keys

Let me run.

</details>

- 🔧 **Bash** `{"command": "grep -o -E '.{0,150}(jqlSearchPost|jql-search-post|basicSearchGet|listIssues).{0,200}' /tmp/mojira.js | head -12\necho \"=== try endpoints ===\"\nfor u in \"https://bugs.mojang.com/api/basic-search-get?query=movement_modifier\" \\\n \"https://bugs.mojang.com/api/basic-search-get?search=movement_modifier\" \\\n \"https://bugs.mojang.com/api/list-issues?query=movemen …[截断,原长396]` → `ugrep: error: error at position 135 :[^\n\x80-\xbf][\x80-\xbf]*){0,200} exceeds complexity limits___/ === try endpoints === --- https://bugs.mojang.com/api/basic-search-get?query=movement_modifier <!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8"> <title>Error</title> </head> <body> <pre>Cannot GET /api/bas …[截断,原长810]`

- 🔧 **WebFetch** `{"prompt": "Return the results as title + url list. I need the Microsoft Learn documentation pages for Minecraft Bedrock entity components: minecraft:explosion, minecraft:projectile, minecraft:area_attack, minecraft:damage (entity).", "url": "https://learn.microsoft.com/api/search?search=minecraft%20explosion%20entity%20component&locale=en-us&%24top=20"}` → `Based on the search results provided, here are the relevant Microsoft Learn documentation pages. Note that the results include an `minecraft:explode` entity component page (the component that defines how an entity explodes), but I did **not** find dedicated pages for `minecraft:projectile`, `minecraft:area_attack`, or  …[截断,原长3030]`

- 🔧 **Bash** `{"command": "grep -o -E '.{0,200}jqlSearchPost.{0,300}' /tmp/mojira.js | head -5\necho \"---\"\ngrep -o -E 'queryKey:\\[`[a-z-]+`[^]]{0,120}' /tmp/mojira.js | sort -u | head -30", "description": "Inspect Mojira JQL query construction"}` → `ugrep: error: error at position 91 n\x80-\xbf][\x80-\xbf]*){0,300} exceeds complexity limits___/ --- queryKey:[`attachments`,e.id queryKey:[`comments`,e queryKey:[`issue` queryKey:[`issue`,a,s queryKey:[`issues`,r,D,T,A,ce,le queryKey:[`issues`,r,D,T,A,ce,le,me,g.pageSize queryKey:[`server-time`,e.apiBaseUrl queryKey:[ …[截断,原长344]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

The mojira bundle has a query for `issues` with params r,D,T,A,ce,le maybe = project(s), etc. Let me find the fetch URL for issues. Grep for `/api/${Da.listIssues}` or similar. Let me grep the literal 'list-issues'.

grep -o -E '.{0,150}list-issues.{0,150}' /tmp/mojira.js — ugrep complexity error because of the pattern. Use simpler grep -F? Actually grep is ugrep aliased. Let me use `grep -o -F 'list-issues'` then use a different approach: use node to read file and slice around occurrences. That's cleaner.

Let me use node:
node -e "const s=require('fs').readFileSync('/tmp/mojira.js','utf8'); ['list-issues','jql-search-post','basic-search-get'].forEach(k=>{let i=0;while((i=s.indexOf(k,i))>=0){console.log('==',k);console.log(s.slice(Math.max(0,i-250),i+120));i+=k.length}})" — but /tmp path issue for node on Windows. Use bash to pass the file... Actually node reading '/tmp/mojira.js' fails on Windows (C:\tmp). Let me write to a Windows path: use $TEMP? Simpler: pipe file into node stdin.

cat /tmp/mojira.js | node -e "let s='';process.stdin...". That's fine.

Let me do that.

Also fetch the exploding/explode doc, projectile doc (find URL), area_attack doc.

Correct entity component URL pattern includes "minecraftcomponent_" prefix: /creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_explode. So projectile → minecraftcomponent_projectile; area_attack → minecraftcomponent_area_attack? Hmm, area_attack may not exist as a separate doc. Let me search Learn API for "minecraft projectile" and "area_attack".

Also there's the item "minecraft:damage" for items and entity "minecraft:damage"? For the fireball: `minecraft:projectile` has `damage_multiplier`? Actually the fireball entity (small_fireball / fireball) has "minecraft:projectile" with "damage_multiplier"?? Hmm. In Bedrock, fireball's explosion is via "minecraft:explode" component in the "minecraft:exploding" component group, triggered by on_hit block/entity. And there's "minecraft:damage" (?) Actually the ghast fireball's explosion power comes from "minecraft:explode": {"power": 1, "fuse_length": 0, ...}.

Wait — the user mentions a custom fireball with explosion power 2 and `minecraft:area_attack` and `minecraft:explosion`. Hmm, "minecraft:explosion" is not a real component? There's "minecraft:explode" (entity) and "minecraft:damage" ... Actually there IS a block/entity? Hmm. Let me check. The user might be using "minecraft:area_attack" (entity component that damages nearby entities each tick) and "minecraft:explode". The user wrote minecraft:explosion — probably means the explosion mechanic. I should clarify: the entity component is `minecraft:explode`; there's no `minecraft:explosion` entity component (UNVERIFIED? let me verify by searching).

Actually, in Bedrock there IS also the `minecraft:explode` behavior for entities (creeper etc.). And for projectiles, `minecraft:projectile` has fields like `hit_sound`, `on_hit` with `definition_event`/`impact_damage` etc. And crucially `impact_damage` has `damage`, `semi_random_diff_damage`, `knockback`, `channel`, `catch_fire`... And there's `damage_multiplier`? Hmm — I'm not sure. There's "damage_multiplier" in the old `minecraft:projectile` "on_hit" -> "impact_damage"?? Let me check the docs.

Let me fetch the projectile page.

Also need "minecraft:area_attack" — this is an entity component? Searching Learn.

Let me batch:
1. node slice for mojira endpoints (pipe)
2. WebFetch explode page
3. WebFetch projectile page (guess URL: .../minecraftcomponent_projectile)
4. Learn search for area_attack

Let me go.

</details>

- 🔧 **Bash** `{"command": "cat /tmp/mojira.js | node -e \"let s='';process.stdin.setEncoding('utf8');process.stdin.on('data',d=>s+=d);process.stdin.on('end',()=>{['list-issues','jql-search-post','jql-search-get','basic-search-get'].forEach(k=>{let i=0,c=0;while((i=s.indexOf(k,i))>=0&&c<3){console.log('=== '+k+' @'+i);console.log(s.slice(Math.max(0,i-260),i+160).replace(/\\n/g,' '));i+=k.leng …[截断,原长412]` → `=== list-issues @110873 ,e.value))})})]})}var Da={siteInfo:`site-info`,serverTime:`server-time`,userDetails:`user-details`,recordRating:`record-rating`,getRating:`get-rating`,listServiceDesks:`list-service-desks`,getServiceDesk:`get-service-desk`,listQueues:`list-queues`,listIssues:`list-issues`,jqlSearchGet:`jql-searc …[截断,原长1791]`

- 🔧 **WebFetch** `{"prompt": "Reproduce the full documentation of minecraft:explode: all fields (power, fuse_length, fuse_lit, causes_fire, destroy_affected_by_griefing, breaks_blocks, allow_underwater, damage_self, max_resistance, toggles, etc.), types, defaults, and the sample JSON. Include anything about how much damage the explosion deals.", "url": "https://learn.microsoft.com/en-us/minecraf …[截断,原长412]` → `--- layout: Conceptual monikers: - minecraft-bedrock-stable - minecraft-bedrock-experimental defaultMoniker: minecraft-bedrock-stable versioningType: Ranged title: Entity Documentation - minecraft:explode | Microsoft Learn canonicalUrl: https://learn.microsoft.com/en-us/minecraft/creator/reference/content/entityreferen …[截断,原长8307]`

- 🔧 **WebFetch** `{"prompt": "Reproduce the full documentation of the minecraft:projectile component: list every field with type and description, especially any damage multiplier, on_hit, impact_damage, hit_sound, shoot_sound, uncertainty, power, and anything about explosion.", "url": "https://learn.microsoft.com/en-us/minecraft/creator/reference/content/entityreference/examples/entitycomponents …[截断,原长412]` → `--- layout: Conceptual monikers: - minecraft-bedrock-stable - minecraft-bedrock-experimental defaultMoniker: minecraft-bedrock-stable versioningType: Ranged title: Entity Documentation - minecraft:projectile | Microsoft Learn canonicalUrl: https://learn.microsoft.com/en-us/minecraft/creator/reference/content/entityrefe …[截断,原长31187]`

- 🔧 **WebFetch** `{"prompt": "Return the results as title + url list. I need the Microsoft Learn page documenting the minecraft:area_attack entity component.", "url": "https://learn.microsoft.com/api/search?search=area_attack%20minecraft%20entity%20component&locale=en-us&%24top=15"}` → `**Target page:** - **Entity Documentation - minecraft:area_attack** — https://learn.microsoft.com/en-us/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_area_attack **All results (title + URL):** 1. Minecraft: Bedrock Edition Creator Documentation — https://learn.microsof …[截断,原长2616]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

I have a lot. Now I need:
- area_attack details
- The Mojira search endpoint. Let me now construct the request. The enum keys map to paths /api/<kebab>. But GET returned "Cannot GET /api/basic-search-get" — maybe POST. Let me POST to /api/jql-search-post with JSON body {"jql":"..."} — need to know body keys. Let me search mojira.js for the POST call usage: `fetch(e.apiBaseUrl+\`/api/\`+t,{method:\`POST\`...`. The function takes a path `t` and body. Let me find where it's called with Da.jqlSearchPost and what payload. Grep for "jql" occurrences.

Let me use node to slice around 'jql'.

Also check what fields/issues the search returns.

Then run the actual search to find MCPE tickets about movement_modifier / use_modifiers / stuck slowness.

Let me do node slicing around "jql" and "basicSearch".

Then POST attempts.

Meanwhile also fetch area_attack doc.

And I still need Q1's community fix. If Mojira has no ticket, I may need to rely on... Let me also check the local addon scripts (the user's project) for the actual implementation — maybe they already have a workaround, which is useful context. Let me look at the LuckyBlock scripts and items.

Let me batch:
1. node slice around jql
2. WebFetch area_attack
3. Bash: list & grep local scripts/items for use_modifiers, movement_modifier, cooldown, explosion

Let me run.

</details>

- 🔧 **Bash** `{"command": "cat /tmp/mojira.js | node -e \"let s='';process.stdin.setEncoding('utf8');process.stdin.on('data',d=>s+=d);process.stdin.on('end',()=>{['jql','basicSearch','projectSearchGet','listIssues'].forEach(k=>{let i=0,c=0;while((i=s.indexOf(k,i))>=0&&c<4){console.log('=== '+k+' @'+i);console.log(s.slice(Math.max(0,i-300),i+300).replace(/\\s+/g,' '));i+=k.length;c++}})})\"", …[截断,原长412]` → `=== jql @110886 width:`24px`}})}),e.label]},e.value))})})]})}var Da={siteInfo:`site-info`,serverTime:`server-time`,userDetails:`user-details`,recordRating:`record-rating`,getRating:`get-rating`,listServiceDesks:`list-service-desks`,getServiceDesk:`get-service-desk`,listQueues:`list-queues`,listIssues:`list-issues`,jqlS …[截断,原长4346]`

- 🔧 **WebFetch** `{"prompt": "Reproduce the full documentation of minecraft:area_attack: every field (damage_per_tick, damage_range, entity_filter, cause, use_self_as_damage_source, etc.), types, defaults, and sample JSON.", "url": "https://learn.microsoft.com/en-us/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_area_attack?view=minecraft-bedrock …[截断,原长389]` → `--- layout: Conceptual monikers: - minecraft-bedrock-stable - minecraft-bedrock-experimental defaultMoniker: minecraft-bedrock-stable versioningType: Ranged title: Entity Documentation - minecraft:area_attack | Microsoft Learn canonicalUrl: https://learn.microsoft.com/en-us/minecraft/creator/reference/content/entityref …[截断,原长7083]`

- 🔧 **Bash** `{"command": "DIR=\"/c/Users/UserX/Downloads/幸运方块地图_法杖增强版_竞技场版\"\necho \"=== item json files ===\"\nfind \"$DIR/behavior_packs\" -name \"*.json\" -path \"*items*\" | head -60\necho \"=== grep movement_modifier / use_modifiers / use_duration / cooldown ===\"\ngrep -rl -e \"movement_modifier\" -e \"use_modifiers\" -e \"cooldown\" \"$DIR/behavior_packs\" 2>/dev/null | head -40", "d …[截断,原长414]` → `=== item json files === /c/Users/UserX/Downloads/幸运方块地图_法杖增强版_竞技场版/behavior_packs/BlockArmor BP V2.1.6/items/andesite/andesite_boots.json /c/Users/UserX/Downloads/幸运方块地图_法杖增强版_竞技场版/behavior_packs/BlockArmor BP V2.1.6/items/andesite/andesite_chestplate.json /c/Users/UserX/Downloads/幸运方块地图_法杖增强版_竞技场版/behavior_packs/Block …[截断,原长7858]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

I found the local staff items. Let me read them to give specific, grounded advice. Let me read staff.json and staffs.js, and the fireball entity.

This is very relevant — the user's project likely contains the exact item with use_duration 2147483647 and movement_modifier 0.5 and the fireball with explosion power 2.

Let me read:
- behavior_packs/LuckyBlock/items/staffs/staff.json
- behavior_packs/LuckyBlock/items/staffs/ice_staff.json, flender_staff.json
- behavior_packs/LuckyBlock/scripts/staffs.js
- find fireball entity json

Let me read these.

Also, the Mojira search: I need to POST to /api/jql-search-post. The enum shows the endpoint names but the actual fetch call is elsewhere (probably in a chunk loaded lazily). The bundle is only 209KB and doesn't contain the call sites; there may be additional chunks. Let me check the index.html for modulepreload (vendor chunks) and see if there are more chunks. Actually the endpoints might be called via a separate chunk. But POST /api/jql-search-post with a JQL body is a reasonable guess. Let me try a couple of payload shapes.

Known from the old Mojira: the new public tracker has a REST at https://bugs.mojang.com/api/... Let me just attempt POST with {"jql":"text ~ \"movement_modifier\""}.

Let me batch:
1. Read staff.json, staffs.js (2 Read calls)
2. Bash POST attempts to mojira

Let me do it.

Actually let me first find the fireball entity json and read staff json. Use Bash grep to locate fireball. And Read tool for files.

Let me do multiple Reads + a Bash.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\幸运方块地图_法杖增强版_竞技场版\\behavior_packs\\LuckyBlock\\items\\staffs\\staff.json"}` → `1 { 2 "format_version": "1.21.10", 3 "minecraft:item": { 4 "description": { 5 "identifier": "lucky:staff", 6 "menu_category": { 7 "category": "equipment" 8 } 9 }, 10 "components": { 11 "minecraft:icon": { 12 "textures": { 13 "default": "lucky_staff" 14 } 15 }, 16 "minecraft:tags": { 17 "tags": [ 18 "lucky:staff" 19 ] 2 …[截断,原长856]`

- 🔧 **Bash** `{"command": "DIR=\"/c/Users/UserX/Downloads/幸运方块地图_法杖增强版_竞技场版\"\necho \"=== staff item files ===\"\nls -la \"$DIR/behavior_packs/LuckyBlock/items/staffs/\"\necho \"=== fireball / projectile entities ===\"\ngrep -rl -e \"minecraft:explode\" -e \"minecraft:projectile\" -e \"area_attack\" \"$DIR/behavior_packs/LuckyBlock/entities\" 2>/dev/null\necho \"=== scripts dir ===\"\nls -la …[截断,原长414]` → `=== staff item files === total 28 drwxr-xr-x 1 user 197121 0 Sep 27 20:26 ./ drwxr-xr-x 1 user 197121 0 Sep 27 20:26 ../ -rw-r--r-- 1 user 197121 1056 Sep 24 11:44 flender_staff.json -rw-r--r-- 1 user 197121 1048 Sep 24 11:44 ice_staff.json -rw-r--r-- 1 user 197121 1088 Sep 24 11:44 staff.json === fireball / projectile …[截断,原长3685]`

- 🔧 **Bash** `{"command": "for body in '{\"jql\":\"text ~ \\\"movement_modifier\\\"\"}' '{\"jql\":\"text ~ movement_modifier\",\"maxResults\":10}'; do\n echo \"--- POST jql-search-post: $body\"\n curl -s -m 20 -X POST \"https://bugs.mojang.com/api/jql-search-post\" -H \"Content-Type: application/json\" -H \"Accept: application/json\" -d \"$body\" | head -c 800; echo\ndone\necho \"--- GET jql …[截断,原长411]` → `--- POST jql-search-post: {"jql":"text ~ \"movement_modifier\""} {"issues":[],"isLast":true,"names":{"summary":"Summary","issuetype":"Issue Type","watches":"Watchers","customfield_10061":"Operating System Version","created":"Created","customfield_10050":"ADO","customfield_10051":"Area","description":"Description","cust …[截断,原长1873]`

### 🤖 助手（`zcode-general-purpose` deepseek-flash，2026-09-27 21:44）

Found the actual project files. Let me read them and probe the Mojira API.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

Excellent! The Mojira JQL search API works via POST /api/jql-search-post. `text ~ "movement_modifier"` returned 0 issues. Let me run better queries:

- text ~ "use_modifiers"
- text ~ "chargeable"
- summary ~ "movement"
- project = MCPE AND text ~ "slowness" ...

Let me try several. Also maybe the ticket uses wording like "player is slowed after using item" or "movement modifier".

Let me run a set of JQL queries:
1. text ~ "use_modifiers"
2. text ~ "chargeable item"
3. text ~ "use_duration"
4. summary ~ "movement modifier"
5. text ~ "slowed" AND text ~ "item"

Let me write a loop.

Also read staffs.js and the staff entity json (explode.json? flender_fireball.json) to ground the answer.

Let me batch:
- Bash: multiple jql POST queries, parse with node
- Read staffs.js
- Read flender_fireball.json / explode.json

Let me do it.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\幸运方块地图_法杖增强版_竞技场版\\behavior_packs\\LuckyBlock\\scripts\\staffs.js"}` → `1 /** 2 * 法杖系统 —— 由《更好的基岩版》迁移进幸运方块 Add-On，并做了加强。 3 * 4 * 设计说明： 5 * - 法力值复用物品耐久度：消耗法力 = 增加 durability.damage，耐久条即法力条。 6 * - 主攻击：按住使用键（itemStartUse）持续释放光束。 7 * - 二次攻击：潜行 + 点击（itemUse）。 8 * - 视觉部分全部用原版粒子沿视线绘制，不依赖 molang 变量，保证一定看得见。 9 * - 冷却：物品自带 6 秒 minecraft:cooldown（物品栏转圈），同时脚本在动作栏显示倒计时。 10 */ 11 import { 12 system, 13  …[截断,原长19207]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\Downloads\\幸运方块地图_法杖增强版_竞技场版\\behavior_packs\\LuckyBlock\\entities\\staffs\\flender_fireball.json"}` → `1 { 2 "format_version": "1.20.30", 3 "minecraft:entity": { 4 "description": { 5 "identifier": "lucky:flender_fireball", 6 "runtime_identifier": "minecraft:snowball", 7 "is_spawnable": false, 8 "is_summonable": true, 9 "is_experimental": false 10 }, 11 "component_groups": { 12 "minecraft:exploding": { 13 "minecraft:expl …[截断,原长1510]`

- 🔧 **Bash** `{"command": "q() {\n echo \"=== JQL: $1\"\n curl -s -m 20 -X POST \"https://bugs.mojang.com/api/jql-search-post\" -H \"Content-Type: application/json\" -H \"Accept: application/json\" -d \"{\\\"jql\\\":$(node -e \"console.log(JSON.stringify(process.argv[1]))\" \"$1\"),\\\"pageSize\\\":15}\" | node -e \"let s='';process.stdin.on('data',d=>s+=d);process.stdin.on('end',()=>{try{co …[截断,原长410]` → `=== JQL: text ~ "use_modifiers" === JQL: text ~ "movement_modifier" === JQL: text ~ "chargeable" AND text ~ "item" === JQL: text ~ "use_duration" === JQL: summary ~ "movement modifier" === JQL: text ~ "slowness" AND text ~ "item"`

### 🤖 助手（`zcode-general-purpose` deepseek-flash，2026-09-27 21:45）

Mojira's JQL API works. Let me query it properly and read the project scripts.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

Interesting! The local flender_fireball has power 4, not 2. And no `minecraft:area_attack`. The user mentions power 2 and area_attack, so maybe another entity. Let me check small_fireball.json, fireball.json, meteor_fireball.json, and ice_projectile.json. Also the "explode.json".

Actually the user's questions are general; but grounding with their files helps. Let me check ice_projectile.json and small_fireball.json quickly and grep for area_attack across entities (earlier grep listed files containing any of the three patterns). Let me grep specifically for area_attack and for "power": 2.

Also note: the local staff.json uses use_duration 2147483647 + movement_modifier 0.5 + cooldown 6s. And staffs.js uses afterEvents.itemStartUse/itemStopUse/itemReleaseUse and endCasting. This matches the reported bug scenario exactly.

Now, the Mojira queries returned empty output entirely (not even "===" lines?). Odd — the output shows the query headers? Actually output shows nothing at all for the q() calls! The echo "=== JQL: $1" didn't print either. Hmm, that means the function or the whole script produced no stdout? Wait, earlier output showed the headers. Now the tool result shows only the Read results and the bash produced nothing? The bash result appears empty — actually the result block for the first Bash shows nothing (empty). Hmm, it shows empty. Possibly the node -e with process.argv[1] and the quoting broke, causing... but the echo should still print.

Wait the tool result block for the first Bash is empty (no output at all). That's strange. Maybe the whole command failed silently due to the function definition? Hmm. Let me re-run more simply.

Possibly the output got consumed as "no output". Let me retry with a simpler approach, one query at a time, avoiding nested node in the -d construction. Use a here-doc file or printf.

Let me redo: use jq? Not available probably. Use node to build request via a small script file. Let me write a temp JS file with Write? Better: use curl with --data-urlencode? JQL body is JSON; I can hardcode.

Simplify: 
curl -s -X POST ... -d '{"jql":"text ~ \"use_modifiers\""}' | node -e "..."

Earlier this exact form worked (returned JSON). And I printed via head -c 800. Let me just print raw JSON with head and then parse separately.

Let me run each query and output raw compacted.

Let me do:
for jql in 'text ~ "use_modifiers"' ...; do echo "### $jql"; curl ... ; echo; done

But quoting inside single quotes is fine since the JQL contains double quotes and we wrap in single quotes for -d: '{"jql":"text ~ \"use...\" }' — inside single quotes the backslashes are literal, so JSON sees \" which is valid escaping. Good.

Let me write it carefully.

Also let me check other entity files.

Let me batch:
1. Bash: mojira queries loop (simplified)
2. Bash: grep entity files for area_attack / power 2; read ice_projectile
3. Read small_fireball.json maybe

Let me do.

</details>

- 🔧 **Bash** `{"command": "M=\"https://bugs.mojang.com/api/jql-search-post\"\nrun() {\n printf '### %s\\n' \"$1\"\n curl -s -m 20 -X POST \"$M\" -H \"Content-Type: application/json\" -H \"Accept: application/json\" --data-binary \"$1\" > /tmp/r.json\n node -e \"const s=require('fs').readFileSync(process.env.TEMP+'/r.json','utf8')\" 2>/dev/null || cp /tmp/r.json \"$TEMP/r.json\" 2>/dev/null\n …[截断,原长408]` → `### {"jql":"text ~ \"use_modifiers\"","pageSize":10} {"issues":[],"isLast":true,"names":{"summary":"Summary","issuetype":"Issue Type","watches":"Watchers","customfield_10061":"Operating System Version","created":"Created","customfield_10050":"ADO","customfield_10051":"Area","description":"Description","customfield_1005 …[截断,原长3319]`

- 🔧 **Bash** `{"command": "DIR=\"/c/Users/UserX/Downloads/幸运方块地图_法杖增强版_竞技场版/behavior_packs/LuckyBlock/entities\"\necho \"=== files containing area_attack ===\"\ngrep -rl \"area_attack\" \"$DIR\" 2>/dev/null\necho \"=== files with explode power 2 ===\"\ngrep -rl '\"power\": 2' \"$DIR\" 2>/dev/null\necho \"=== ice_projectile ===\"\ncat \"$DIR/staffs/ice_projectile.json\" 2>/dev/null | head -70 …[截断,原长414]` → `=== files containing area_attack === === files with explode power 2 === C:/Users/UserX/Downloads/幸运方块地图_法杖增强版_竞技场版/behavior_packs/LuckyBlock/entities\entity_tnt.json C:/Users/UserX/Downloads/幸运方块地图_法杖增强版_竞技场版/behavior_packs/LuckyBlock/entities\christmas_grenade.json C:/Users/UserX/Downloads/幸运方块地图_法杖增强版_竞技场版/behavior_p …[截断,原长2669]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

The Mojira JQL searches returned empty—but note cacheRefreshed:false and pageSize 25 (my pageSize ignored, and the response for the first request earlier said cacheRefreshed:true). Hmm, "issues":[] for everything including "use_modifiers" suggests either Mojira's full-text index doesn't cover these, or the query syntax is wrong (maybe `text ~` isn't supported and it silently matches nothing). Let me test with a known term that should exist, e.g. text ~ "creeper" or summary ~ "crash", to validate the query mechanism.

Let me validate: run `{"jql":"text ~ \"creeper\""}` and `{"jql":"project = MCPE"}`. If those return results, the mechanism works.

Then try other terms: "movement_modifier" may genuinely have no ticket. Try:
- text ~ "slowed" 
- summary ~ "slowness"
- text ~ "item use"
Hmm.

Better: search for the known behavior differently. Maybe the ticket title mentions "Item" and "slow". Let me first validate.

Also, the user's mention of "charge/held item" bug is plausibly a known community issue (Bedrock-OSS / bedrock.dev Discord / MCPE ticket). If Mojira has nothing, I'll mark it UNVERIFIED and rely on documented mechanics + provide a safe workaround (which I can justify from docs: movement_modifier applies "while the item is in use"; use_duration defines how long the item takes to use; cooldown interaction).

Let me validate Mojira search and also try the Minecraft feedback site? Actually feedback site tickets are separate (feedback.minecraft.net) — but they were migrated. Hmm.

Also let me try a couple more entity files: explode.json (power 2?), spiral_arrow.json.

Also: the user said "custom fireball with explosion power 2" — flender_fireball has power 4 (in this version). Whatever.

Let me now:
1. Validate Mojira search + several queries
2. Read explode.json (power 2, maybe uses area_attack? no)
3. Read the entity that has area_attack — none found, so user's "minecraft:area_attack" is hypothetical.

Let me run.

</details>

- 🔧 **Bash** `{"command": "M=\"https://bugs.mojang.com/api/jql-search-post\"\nrun() { printf '### %s\\n' \"$2\"; curl -s -m 20 -X POST \"$M\" -H \"Content-Type: application/json\" -H \"Accept: application/json\" --data-binary \"$1\" | node -e \"let s='';process.stdin.on('data',d=>s+=d);process.stdin.on('end',()=>{try{const d=JSON.parse(s);console.log('count',(d.issues||[]).length);(d.issues| …[截断,原长413]` → `### sanity: text ~ creeper count 0 ### sanity: project=MCPE count 0 ### text ~ slowness count 0 ### text ~ cooldown AND item count 0 ### text ~ use modifier count 0 ### text ~ custom item count 0`

- 🔧 **Bash** `{"command": "DIR=\"/c/Users/UserX/Downloads/幸运方块地图_法杖增强版_竞技场版/behavior_packs/LuckyBlock/entities\"\necho \"=== explode.json ===\"; cat \"$DIR/explode.json\"\necho; echo \"=== spiral_arrow.json (power 2) ===\"; head -80 \"$DIR/spiral_arrow.json\"", "description": "Read explode and spiral_arrow entity definitions"}` → `=== explode.json === { "format_version": "1.11.0", "minecraft:entity": { "description": { "identifier": "entity:explode", "runtime_identifier": "minecraft:tnt", "is_spawnable": false, "is_summonable": true, "is_experimental": false }, "components": { "minecraft:type_family": { "family": [ "effect99_entities" ] }, "mine …[截断,原长1967]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

The Mojira search returns 0 even for "creeper" — so the `text ~` operator likely isn't supported/doesn't match, OR the new tracker requires different JQL field names. Let me check the response "names" — it shows fields but no results. Possibly the tracker requires `searchIssues` with a different param. Let me test with `summary ~ "crash"` and `key = MCPE-1`. Also maybe there's a separate field `search` or the JQL must be `text ~ creeper` without quotes... I tried both. And `project = MCPE` returned 0 which is suspicious — MCPE project definitely exists.

Maybe the correct JQL usage requires `project="MCPE"`? Or the tracker's JQL supports only certain fields. Let me look at the bundle for the query field names / how the search is built (there's a "basic-search-get" and "jql-search-post"). Since the bundle doesn't have call sites (lazy chunks), let me fetch other chunks. Index.html listed modulepreload for vendor-react and vendor-mui and rolldown runtime; there may be more chunks referenced from index js. Let me grep for ".js" chunk names in mojira.js.

Actually, maybe better: use the search UI's basic search which might be a different endpoint. But GET basic-search-get returned "Cannot GET".

Alternatively, use `jql-search-post` with body {"q": "..."} or {"query":"..."}. Let me brute force a few body shapes and check if any returns non-empty for "creeper".

Actually, given time constraints, maybe the Mojira search isn't essential. But a Mojira ticket would be the strongest citation for Q1. Let me try a bit more.

Let me test response of `{"jql":"summary ~ \"creeper\""}` and `{"jql":"id = 1"}` and see. Also maybe the tracker needs `projectId`. Hmm.

Let me try the basic search via POST too: POST /api/basic-search-get? Name says GET. Maybe the path is /api/basic-search (without -get). Hmm.

Let me check chunk list: grep -o -E 'assets/[A-Za-z0-9_-]+\.js' index html had only index + vendors. The endpoints probably all in index js but the call sites are minified differently. Let me search mojira.js for "jql" occurrences more (only 4 in the enum). So the call site must be in a lazy chunk loaded on demand. Let me find chunk names in mojira.js: grep -o -E '"[A-Za-z0-9_-]+\.js"' or check for import() with dynamic names.

Let me do: node slice for 'import(' or 'chunk'.

This is getting deep. Given the primary goal is answering the 4 questions with citations, and Mojira is optional, let me time-box: one more attempt to find chunks + test search shapes; if it fails, mark UNVERIFIED for Q1 engine-bug claim and rely on documented mechanics.

Let me also validate the Microsoft Learn version-specific info: I should confirm whether onConsume/onCompleteUse are in 1.13.0. The changelog said item custom component classes added in 1.12.0. Wait — that's the module changelog version numbering; but @minecraft/server 1.12.0 corresponds to MC 1.21.50? Hmm. Actually per the changelog, ItemComponentRegistry etc. added in 1.12.0. But the user said their version is 1.13.0, so all those events exist in 1.13.0. Hmm, but wait: is that changelog the official one? The WebFetch summarizer said "Item custom component classes were introduced in 1.12.0" and "under 2.0.0 registerCustomComponent changed". Hmm, but I recall item custom components arriving in 1.10.0-beta... The changelog version headings are @minecraft/server module versions in stable. Hmm, but actually the changelog might list version 1.12.0 as the stable release where these left beta. Wait — but if onConsume was in 1.12.0 stable, that's MC 1.21.50. Hmm. Let me double check by fetching the changelog page again with a targeted question about the exact version heading text and also about "1.11.0"/"1.12.0" lines. Actually the summarizer gave the exact bullets. Good enough? It's a small model summarizing; risk of error. Let me verify by direct curl of the Learn page and grep for "ItemComponentConsumeEvent". The Learn page HTML may be large but grep is fine.

Let me curl the page and grep context.

Similarly grep for "onConsume" and version headings.

Let me do that — it's a strong verification.

Also I want the version mapping to game versions: The changelog page might show a note like "Minecraft 1.21.50". Let me grep for "Minecraft 1." near version headings.

Plan:
Bash: curl learn changelog page -> save; node script to parse headings and find "ItemComponent" occurrences with nearest preceding heading.
Also curl the itemcustomcomponent page? Already have.

Let me do the changelog parsing with node (pipe).

Let me write a node script inline that:
- reads HTML from stdin
- strips tags
- finds lines with "ItemComponent" and prints surrounding context, plus finds "## 1.x.0" headings.

The Learn page HTML is JS-rendered? Microsoft Learn renders server-side mostly. Let me try.

Let me run.

</details>

- 🔧 **Bash** `{"command": "cd /tmp 2>/dev/null\ncurl -s -m 40 \"https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/changelog?view=minecraft-bedrock-stable\" -o /tmp/chg.html\nls -la /tmp/chg.html\ncat /tmp/chg.html | node -e \"\nlet s='';process.stdin.setEncoding('utf8');process.stdin.on('data',d=>s+=d);\nprocess.stdin.on('end',()=>{\n // crude html->text\n let t= …[截断,原长411]` → `-rw-r--r-- 1 user 197121 304958 Sep 27 21:46 /tmp/chg.html HIT COUNT 22 2.10.0 >> ItemComponentTypes 2.4.0 >> ItemComponentTypes 2.3.0 >> ItemComponentTypes 2.2.0 >> ItemComponentTypes 2.0.0 >> ItemComponentRegistry 2.0.0 >> ItemCustomComponentInstance 2.0.0 >> ItemComponentTypes 1.18.0 >> ItemComponent 1.18.0 >> ItemC …[截断,原长781]`

### 🤖 助手（`zcode-general-purpose` deepseek-flash，2026-09-27 21:46）

The Mojira JQL endpoint isn't matching any terms (even "creeper"), so I'll verify the Learn changelog directly from HTML.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

Confirmed: all the ItemComponent*Event classes (including Consume, CompleteUse, MineBlock) were "Added" in @minecraft/server 1.12.0, and nothing before. So in 1.13.0 they all exist (stable). Good.

But is the changelog showing "Added" or could these be under a different subsection? The lines are the anchors. Let me confirm the 1.12.0 section says "Added". Let me grep the text around 1.12.0.

Also, I want to know the game version for @minecraft/server 1.12.0 and 1.13.0. The changelog may include a note. Let me grep for "Minecraft " near version headings, or check the module page which shows "Supported in Minecraft 1.21.x".

Let me grep /tmp/chg.html text for "1.21." occurrences near "1.12.0".

Let me also verify the "Added" status.

Additionally, I should confirm the version ↔ game mapping, e.g. @minecraft/server 1.13.0 = Minecraft 1.21.60? Let's check the module page https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server which might state the current version. Hmm, that gives latest.

The changelog likely has headings like "## 1.12.0" plus a line "Minecraft 1.21.50"? Let me search text for "1.21." lines.

Let me run a node parse printing lines around "1.12.0" and any line containing "1.21.".

Also let me confirm the "Added" wording.

Then, Q1 remains. Let me try one more Mojira approach: maybe the JQL field for full text is `text` but requires the tracker's own syntax; the fact that "creeper" returns 0 means search isn't working through this endpoint (maybe it needs auth or the index is on a different field). Let me test `{"jql":"key = MCPE-1"}` and `{"jql":"resolution = Unresolved ORDER BY created DESC","pageSize":3}` to see if any returns results. If ordering works, maybe I can page through and filter client-side, but that's huge.

Let me test `{"jql":"ORDER BY created DESC"}` or `{"jql":"*"}`.

Actually the response had "pagination" and "cacheRefreshed". Maybe the endpoint expects the JQL under a different key, e.g. {"query": "..."} or {"search":"..."}. Let me test with a body {"jql":"...", "search":"creeper"} etc. Hmm.

Let me test a few body shapes quickly and check counts.

Then decide.

Let me batch:
1. node parse of chg.html for context/version+game
2. mojira body-shape probing

Go.

</details>

- 🔧 **Bash** `{"command": "cat /tmp/chg.html | node -e \"\nlet s='';process.stdin.setEncoding('utf8');process.stdin.on('data',d=>s+=d);\nprocess.stdin.on('end',()=>{\n let t=s.replace(/<script[\\s\\S]*?<\\/script>/g,' ').replace(/<style[\\s\\S]*?<\\/style>/g,' ').replace(/<[^>]+>/g,'\\n');\n t=t.replace(/&amp;/g,'&').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&quot;/g,'\\\"');\n cons …[截断,原长409]` → `--- around 1.13.0 1.13.0 | 1.12.0 | 1.11.0 | 1.10.0 | 1.9.0 | 1.8.0 | 1.7.0 | 1.6.0 | 1.5.0 | 1.4.0 | 1.3.0 | 1.2.0 | 1.1.0 | 1.0.0 | 2.12.0-beta.1.26.60-preview.28 | Changed | AimAssistCategorySettings | Changed function | setBlockPriorities | Changed return type from | void | to | void | Changed argument | blockPrior …[截断,原长2783]`

- 🔧 **Bash** `{"command": "M=\"https://bugs.mojang.com/api/jql-search-post\"\nt() { printf '### %s -> ' \"$2\"; curl -s -m 20 -X POST \"$M\" -H \"Content-Type: application/json\" -H \"Accept: application/json\" --data-binary \"$1\" | node -e \"let s='';process.stdin.on('data',d=>s+=d);process.stdin.on('end',()=>{try{const d=JSON.parse(s);console.log('issues='+(d.issues||[]).length, 'err='+(d …[截断,原长412]` → `### key=MCPE-1 -> issues=0 err= ### order by created -> issues=0 err= ### project=MC -> issues=0 err= ### search=creeper -> issues=0 err= ### jql=* -> issues=0 err= ### text~creeper page -> issues=0 err= ### query=creeper -> issues=0 err=`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

Mojira's public API returns 0 issues for everything — the endpoint likely requires a workspace/resource-id header or the issues are gated. Actually the bundle showed POST with header "resource-id": localStorage... So maybe required header "resource-id". Let me try adding a resource-id header, e.g. "minecraft" or the site. Hmm, guessing.

Actually the response returned valid structure with "cacheRefreshed" and field names, so the API accepted the JQL but found no issues. Maybe the tracker's issue data is behind an "app" or the JQL needs `project = "MCPE"` plus the tracker is empty because the migration moved to a different dataset. Odd that key=MCPE-1 gives 0.

Hmm, maybe the field name is not "key" but the issue key is in `id`. Let me check if there's a "get issue by key" endpoint: `issue-details`? The enum had issueCommentGet, issueAttachmentGet. Let me try POST /api/issue-details? Hmm. Actually there might be an endpoint like `/api/issue/{key}`.

Alternatively, maybe the issue search requires `jql` plus `project` and the response's "issues" populates only when a valid workspace is set. 

Given diminishing returns, let me stop chasing Mojira. I'll mark Q1's "known engine bug" status as UNVERIFIED-by-official-tracker, and note that Mojira full-text search returned no ticket via the public API at this time (with the caveat that the API returned empty for all queries, so it may not be a reliable negative).

Wait — that caveat is important: since even "creeper" returns 0, I cannot conclude the bug is unreported. I should state the search method failed, i.e. INCONCLUSIVE.

Hmm, but maybe I can find the ticket another way: Google cache is blocked; but there is a mirror of Mojira tickets? There's "bugs.mojang.com/browse/MCPE-XXXX". Let me try fetching a browse URL to see if it redirects to the new SPA with the issue loaded — the SPA might fetch issue by key via a client route; the HTML would be the same. But there might be an oEmbed or a pre-render. Try https://bugs.mojang.com/browse/MCPE-178111 via WebFetch? It'd just be the SPA.

Alternatively, Mojira has an RSS/API mirror at "https://bugs.mojang.com/rest/api/2/issue/MCPE-1"? That returned the SPA earlier for search. Let me test /rest/api/2/issue/MCPE-1 quickly — if it returns the SPA, no good.

Hmm. Let me try the "resource-id" header with an empty value or "minecraft" — one quick test. And try /api/issue-details?issueKey=... Actually let me test POST /api/issue-details with {"issueId":"MCPE-1"} or similar. But guessing payloads is expensive.

Let me time-box: 1 more bash with a few probes. If nothing, move on.

Actually — better idea: The old Mojira REST API is available at a different host: "https://bugs.mojang.com/rest/api/2/search" is proxied to the SPA. But there's also the legacy "https://bugs.mojang.com/rest/api/latest/..." same thing.

Alternatively, the "Minecraft Bug Tracker" data is mirrored by third parties, e.g. "https://mojira.dev"? Hmm, there IS a community site "mojira.dev" that mirrors bugs.mojang.com. Let me try https://mojira.dev/search?q=... Hmm, or "https://bugs.mojang.com/issues/MCPE-..." Actually I recall community mirrors: "https://mojira.dev/MCPE-12345". Let me try WebFetch on https://mojira.dev/ and see.

Let me do one batch: 
- curl mojira.dev root
- curl old reddit json with proper headers (maybe reddit needs a specific UA; try "python:research:v1 (by /u/x)")
- curl api.pushshift? retired.

Let me also try searching the web via a different engine that curl can reach: e.g. "https://search.marcia"? no. Try "https://lite.duckduckgo.com/lite/?q=" with POST (DDG lite accepts POST form). Let me try POST to https://lite.duckduckgo.com/lite/ with q. Or "https://search.brave.com"? Might block. Try "https://www.mojeek.com/search?q=" (Mojeek is scraper-friendly). Let me try Mojeek and Marginalia:
- https://www.mojeek.com/search?q=%22movement_modifier%22+bedrock
- https://search.marginalia.nu/search?query=...

Let me try Mojeek.

Batch:
1. curl mojeek search for movement_modifier stuck
2. curl mojeek search for "use_modifiers" slow
3. WebFetch mojira.dev

Go.

</details>

- 🔧 **Bash** `{"command": "UA=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36\"\nstrip() { node -e \"let s='';process.stdin.on('data',d=>s+=d);process.stdin.on('end',()=>{let t=s.replace(/<script[\\s\\S]*?<\\/script>/g,' ').replace(/<[^>]+>/g,' ').replace(/&amp;/g,'&').replace(/&#x27;/g,\\\"'\\\");console.log(t.split('\\n').map(x=>x …[截断,原长412]` → `=== MOJEEK: movement_modifier bedrock === 403 - Forbidden 403 - Forbidden Sorry your network appears to be sending automated queries so we can't process your search at this time. If you are seeing this in error please contact us . === MOJEEK: item stuck slow after use bedrock === 403 - Forbidden 403 - Forbidden Sorry y …[截断,原长469]`

- 🔧 **WebFetch** `{"prompt": "What is this site? Does it mirror the Minecraft bug tracker? Give the search URL format and any results about item use_modifiers / movement_modifier.", "url": "https://mojira.dev/"}` → `This site is mojira.dev, which presents itself as a mirror/interface for the Minecraft bug tracker. It includes a disclaimer: "Not an official Minecraft website. Not approved by or associated with Mojang or Microsoft." The content shows bug listings across projects (MC, MCPE, MCL, REALMS, WEB, BDS) with filters for sta …[截断,原长559]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

mojira.dev is a mirror with a search. Let me find its search URL. Try https://mojira.dev/search?query=movement_modifier or ?q=. Let me probe with curl and also try the JSON API if any.

Let me try:
- https://mojira.dev/search?q=movement_modifier
- https://mojira.dev/?search=movement_modifier
- https://mojira.dev/api/search?q=...

Use curl and check for results.

Let me also consider that mojira.dev might expose an API like https://mojira.dev/api/v1/issues?search=.

Let me probe.

Also, I've spent a lot; let me be efficient. I'll do one bash probing mojira.dev search endpoints, then wrap up. If I find a ticket, great; else mark inconclusive.

Actually, let me reconsider the whole Q1. The user asks for "accurate, citable facts" and to "mark anything you could not verify as UNVERIFIED". It's acceptable to say the engine-bug claim is not documented and my tracker search was inconclusive, then give the documented mechanics and a robust workaround grounded in docs (which is what a good answer does). But I should try a bit harder for a community citation since they explicitly asked for "concrete code snippets if any exist in community discussions."

Let me probe mojira.dev search.

Also try the bedrock-oss wiki: https://wiki.bedrock.dev/ has a page on "Items" and maybe a page about "cooldown"/"chargeable". Also wiki.bedrock.dev/items/items-1.20.50? Hmm.

Also, there's a well-known community doc "bedrock.dev/docs/stable/Item Components" mirrored from MS docs.

Another community source: "https://learn.microsoft.com/en-us/minecraft/creator/documents/items/..." no.

Given search engines are blocked, reaching community discussions is hard. GitHub search API works — let me use it better: search for repositories with addons that work around this. Search code requires auth, but I can search issues in specific repos:
- Bedrock-OSS/bedrock-wiki issues
- Bedrock-OSS/bedrock-apis? 
- The official "Mojang/bedrock-samples" has issues disabled? It returned 0 for query but that could be because search only covers issues in repos with issues enabled.

Try: search issues with q="itemStopUse" or "itemReleaseUse" minecraft — those are script event names that devs discuss. Also q="chargeable" minecraft script.

Let me try GitHub issue search with those terms.

Batch:
1. probe mojira.dev search endpoints
2. GH issues: itemStopUse / itemReleaseUse / "movement_modifier" in various forms
3. wiki.bedrock.dev items page for cooldown/chargeable notes (already partly)

Go.

</details>

- 🔧 **Bash** `{"command": "UA=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36\"\nfor u in \"https://mojira.dev/search?q=movement_modifier\" \"https://mojira.dev/?q=movement_modifier\" \"https://mojira.dev/api/search?q=movement_modifier\" \"https://mojira.dev/issues?q=movement_modifier\"; do\n echo \"--- $u\"\n curl -s -m 20 -A \"$UA …[截断,原长410]` → `--- https://mojira.dev/search?q=movement_modifier --- https://mojira.dev/?q=movement_modifier <!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <link rel="shortcut icon" href="/static/favicon.png" type="image/png"> <title>mojira.dev</ti …[截断,原长566]`

- 🔧 **Bash** `{"command": "for q in \"itemStopUse\" \"itemReleaseUse\" \"itemStartUse+minecraft\" \"chargeable+item+minecraft+script\" \"%22use_modifiers%22+bedrock\"; do\n echo \"=== $q\"\n curl -s -m 25 \"https://api.github.com/search/issues?q=$q&per_page=12\" | node -e \"let s='';process.stdin.on('data',d=>s+=d);process.stdin.on('end',()=>{try{const d=JSON.parse(s);console.log('total',d.t …[截断,原长410]` → `=== itemStopUse total 3 https://github.com/JKaps11/BedrockLeveling/pull/3 | fixes https://github.com/SerenityJS/serenity/pull/249 | feature: added playerStartBreakingBlock and playerStopBreakingBlock events https://github.com/JKaps11/BedrockLeveling/pull/4 | Test === itemReleaseUse total 3 https://github.com/BedrockTwe …[截断,原长2437]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

No community bug ticket found. I'll mark Q1's "known engine bug" as UNVERIFIED/inconclusive and explain the mechanics from docs, giving a workaround.

But wait — I should also verify a key documented fact for Q1: does `minecraft:cooldown` start when use begins or when use completes/food consumed? The MS docs only say "Adds a cooldown to an item, preventing it from being used again for a specified duration. Items sharing the same category will enter cooldown together when any one of them is used." It doesn't specify timing. Wiki.bedrock.dev says "Determines how cooldowns are triggered for the item and how long each cooldown should last." No timing detail. So the timing on start-vs-complete is UNVERIFIED by docs.

Hmm, but there is a known behavior: for food items, cooldown applies after consumption (like chorus fruit/goat horn? no). Actually in Bedrock, `minecraft:cooldown` on food triggers... hmm. There's a known vanilla example: `minecraft:cooldown` is used by chorus fruit? No. It's used by... "wind charge"? no that's Java. In Bedrock, cooldown is used on goat horn? Hmm.

Let me check bedrock-samples for items using cooldown to cite an example. Search GitHub raw? I can use the GitHub API to list items? Hmm, that's a lot. Alternatively fetch bedrock-samples items directory listing via API: https://api.github.com/repos/Mojang/bedrock-samples/contents/behavior_pack/items — returns JSON list. Then find which files contain cooldown... can't grep contents without fetching each.

Alternatively, there is documentation in the "1.20.10/1.20.30 update notes" about cooldown. Hmm.

Given the constraints, I'll answer with what's documented and mark timing as UNVERIFIED.

Actually, wait. I can check the vanilla item that uses cooldown: In Bedrock, `minecraft:cooldown` is used by "minecraft:goat_horn"? Hmm. Let me just fetch a few candidate item JSONs from bedrock-samples: goat_horn.json, chorus_fruit.json? Actually cooldown in Bedrock is on "minecraft:goat_horn"? Not sure. Let me search GitHub code via the API without auth — code search requires auth. Alternatively, use the GitHub "raw" for a likely file.

Hmm, maybe not worth it.

Now, one more useful check for Q2: whether `onConsume` etc. fire for items that are also `minecraft:food`. Docs don't say. I'll mark UNVERIFIED but note the documented prerequisite (minecraft:food requires use_modifiers).

Also for Q2: does handler cancellation exist? The event objects are read-only with no cancel; ItemComponentConsumeEvent has only itemStack and source (read-only). So no cancellation. ItemComponentCompleteUseEvent extends ItemCompleteUseEvent — let me check ItemCompleteUseEvent properties (itemStack, source?) and whether it's cancelable. Let me fetch itemcompleteuseevent doc.

Also ItemComponentUseOnEvent and ItemComponentHitEntityEvent, ItemComponentBeforeDurabilityDamageEvent signatures — the user asked for onConsume/onCompleteUse mainly; I have those. But let me grab ItemCompleteUseEvent for completeness.

Also, for Q2 version question: I have changelog: all added in 1.12.0 stable. But I should double check that 1.12.0 is stable (not beta). The changelog lists "2.12.0-beta..." separately, and 1.x are stable. Also the "Minecraft 1.21.x" mapping — the changelog text had no 1.21 lines. Let me get the game-version mapping from the module page: https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server?view=minecraft-bedrock-stable which usually states "Supported in Minecraft 1.21.x". Hmm, that gives latest.

Actually, I recall the mapping table is on the "Script Versioning" doc: https://learn.microsoft.com/en-us/minecraft/creator/documents/scriptversioning? Hmm. Let me check. Actually there's a known page: "Minecraft Bedrock script API versions" mapping @minecraft/server 1.x to game versions:
- 1.9.0 → 1.21.0? 
Hmm.

Let me fetch https://learn.microsoft.com/en-us/minecraft/creator/documents/scriptversioning and see if it has a mapping table.

That would let me say "@minecraft/server 1.13.0 ships with Minecraft 1.21.x". But the user says game 1.21.113 — hmm, actually there's no 1.21.113? Wait, maybe there IS: Bedrock versions go 1.21.110? Hmm. Actually 1.21.11, 1.21.20, ... 1.21.100, 1.21.110, 1.21.113? The "1.21.130" mentioned in docs (cooldown type field requires 1.21.130) suggests versions beyond 1.21.113 exist. So 1.21.113 could be a real recent Bedrock version (2026). Hmm, but then @minecraft/server 1.13.0 would be way older (1.21.30ish). That mismatch is worth flagging as a caution — the user may have a manifest with an outdated API version, or they may be confusing the numbers.

Hmm, actually maybe the user's "游戏版本 1.21.113" is a typo/shorthand for 1.21.1.13? Or maybe Bedrock 1.21.113 doesn't exist. I should flag: if the game is really 1.21.113, the corresponding stable @minecraft/server is newer than 1.13.0, and some of my 1.13.0 answers (esp. availability) still hold since APIs are additive. Actually more relevant: @minecraft/server 1.13.0 corresponds to Minecraft 1.21.30-ish? Let me verify mapping via the versioning doc.

Let me fetch:
- https://learn.microsoft.com/en-us/minecraft/creator/documents/scriptversioning
- https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/itemcompleteuseevent?view=minecraft-bedrock-stable

Let me do those two WebFetch.

Then I'll compose the final answer.

Also I should verify the claim "use_duration: 2147483647" — is there any documented max? MS doc: use_duration type Decimal number, default 0, "Time, in seconds, that the item takes to use." No max. Wiki.bedrock.dev: "The time duration (in seconds) that the item must be used for to complete a single use." No max. So no documented max → mark the overflow claim UNVERIFIED but note the value is INT32 max (a common "infinite" idiom) and that 2147483647 seconds ≈ 68 years so the use never completes in practice; the client still treats the item as "in use" the whole time (which is exactly why the movement modifier stays applied while held).

Also, I realize there might be a relevant documented note: the "use_animation" component and "minecraft:food" require use_modifiers. And there's the known "itemStopUse"/"itemReleaseUse" after-events.

One more important documented mechanic for the workaround: `ItemStack` and `container.setItem`, `Player.clearCooldown`? Is there a `clearCooldown` API? Hmm — the user asked about "clearCooldown". Let me check if `Player.clearCooldown` exists in @minecraft/server. I don't think it does in 1.13. Actually there IS... hmm. Let me check the Player class doc for "Cooldown". Let me grep the Player doc page for "cooldown".

Let me fetch https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/player?view=minecraft-bedrock-stable with prompt about cooldown methods.

Let me batch:
1. scriptversioning doc
2. itemcompleteuseevent doc
3. player doc — cooldown-related methods

Go.

</details>

- 🔧 **WebFetch** `{"prompt": "Does this page contain a table mapping @minecraft/server module versions (1.9.0, 1.11.0, 1.12.0, 1.13.0, etc.) to Minecraft game versions? Reproduce that mapping exactly if present. Also summarize the rules about stable vs beta API versions and what happens when a manifest requests a version higher than the game supports.", "url": "https://learn.microsoft.com/en-us/ …[截断,原长412]` → `--- layout: Conceptual monikers: - minecraft-bedrock-stable - minecraft-bedrock-experimental defaultMoniker: minecraft-bedrock-stable versioningType: Ranged title: Script Module Versioning | Microsoft Learn canonicalUrl: https://learn.microsoft.com/en-us/minecraft/creator/documents/scripting/versioning?view=minecraft-b …[截断,原长7682]`

- 🔧 **WebFetch** `{"prompt": "Reproduce the full documentation of ItemCompleteUseEvent and ItemCompleteUseAfterEvent: all properties and types. Also note any version markers.", "url": "https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/itemcompleteuseevent?view=minecraft-bedrock-stable"}` → `--- layout: Conceptual monikers: - minecraft-bedrock-stable - minecraft-bedrock-experimental defaultMoniker: minecraft-bedrock-stable versioningType: Ranged title: minecraft/server.ItemCompleteUseEvent Class | Microsoft Learn canonicalUrl: https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/i …[截断,原长2728]`

- 🔧 **WebFetch** `{"prompt": "List every property and method of the Player class that mentions \"cooldown\" (e.g. clearCooldown, getCooldown, itemCooldown). Quote exact signatures and any version markers (@beta/experimental). Also list methods related to the selected slot / inventory and to \"isUsingItem\" or using-item state if present.", "url": "https://learn.microsoft.com/en-us/minecraft/crea …[截断,原长412]` → `--- layout: Conceptual monikers: - minecraft-bedrock-stable - minecraft-bedrock-experimental defaultMoniker: minecraft-bedrock-stable versioningType: Ranged title: minecraft/server.Player Class | Microsoft Learn canonicalUrl: https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/player?view=min …[截断,原长27734]`

### 🤖 助手（`zcode-general-purpose` deepseek-flash，2026-09-27 21:48）

Let me verify a few remaining API details.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

Important findings:
- The version mapping table on the Learn versioning page SKIPS 1.12.0: it lists 1.11.0 → 1.21.0, then 1.13.0 → 1.21.20. So there's no 1.12.0 row (the table omits it). Actually the table shows 1.11.0 | 1.21.0, then 1.13.0 | 1.21.20. Hmm, that means 1.12.0 would map to 1.21.10 (vanished), but 1.12.0 does exist per the changelog (it added ItemComponent events). So @minecraft/server 1.12.0 = Minecraft 1.21.10? Actually the changelog page listed 1.12.0 with block component events. Hmm the mapping table skips 1.12.0 — likely because 1.21.10 didn't have a new server version? But the changelog shows a 1.12.0 section. Interesting. Anyway: **@minecraft/server 1.13.0 = Minecraft 1.21.20** (per official mapping). That's a critical fact: the user's game is 1.21.113 (per their claim) but script API 1.13.0 corresponds to Minecraft 1.21.20. So their manifest pins an OLD API version. Since stable is backwards compatible, requesting 1.13.0 on a newer game means the game fulfills it with a higher version — actually the game fulfills with the latest compatible; so it's fine but they'd be getting APIs as of 1.21.20 semantics. Also important: `clearCooldown` does NOT exist; instead there are `getItemCooldown` and `startItemCooldown` (stable per this page? They are listed without moniker guards, so they appear stable now; but in 1.13.0? Need check). Hmm — startItemCooldown/getItemCooldown exist in the current stable docs. Were they in 1.13.0? Let me check the changelog for getItemCooldown/startItemCooldown.

Let me grep the changelog HTML for "Cooldown".

That's important because the user asked about "clearCooldown" — the correct API is startItemCooldown (there's no clearCooldown; setting duration 0 could clear). Let me verify.

Also for Q2, onConsume/onCompleteUse have no cancel (read-only events, return void).

Let me grep /tmp/chg.html for Cooldown and also for "onConsume"/"onCompleteUse"/"onMineBlock" (to determine if onMineBlock is in 1.13.0 — it was added in 1.12.0 per changelog, but the ItemCustomComponent interface doc includes onMineBlock; so yes available).

Wait, the user's list didn't include onMineBlock. I can mention it exists (added 1.12.0).

Let me grep changelog for "Cooldown".

Also grep for "1.12.0" not in mapping. And confirm 1.13.0 section contents (what was added in 1.13.0). Let me extract the full 1.13.0 section text.

Let me run a node parse: find the node whose text === '1.13.0' in the changelog content (the second occurrence, in the actual content) and print following ~60 tokens. Similarly for '1.12.0'.

Let me do that plus grep Cooldown.

Then compose final answer. I think I have enough for Q2/Q3/Q4. For Q1, I'll present documented mechanics + a robust workaround, clearly marked as my recommendation (not a cited fix), and mark the engine-bug status as unverified/inconclusive.

Actually, wait. Let me reconsider one Q1 mechanism that IS documentable: The docs say movement_modifier is applied "while the item is in use". And `minecraft:cooldown` "Adds a cooldown to an item, preventing it from being used again for a specified duration" and "items sharing the same category will enter cooldown together when any one of them is used." Since the staff also has cooldown 6s, and the use never completes (use_duration 2147483647), the engine likely starts cooldown immediately on use-start and keeps the "in use" state. Hmm, but that's speculation.

Let me look for the actual likely cause with a more targeted search. Since I can't reach community forums, maybe I can find something in the bedrock-samples "documentation" or in the Microsoft "1.21.x update notes" that mention a fix for item use modifiers. Let me search the Learn docs via the search API for "movement_modifier" or "use modifiers" fix. Let me use the Learn search API with search=item%20use%20modifiers. Hmm.

Actually, better: there's a known Bedrock bug where holding a chargeable item and switching... Hmm.

I think it's fine to be honest: engine-bug status UNVERIFIED (couldn't find a tracker ticket or community thread with the tools available; note search engines were blocked).

But I can strengthen with one technical, verifiable-from-docs point: the cooldown `duration` field, per wiki.bedrock.dev, "If this value is a negative number, it renders the item unusable." And MS says items sharing category enter cooldown together "when any one of them is used" — "used" implies at use, so cooldown likely starts at use-start. Hmm, "used" is ambiguous.

Let me quickly grep the changelog for Cooldown APIs and also check if there's a doc "1.21.20 update notes" mentioning cooldown/food.

Let me do the final verification bash, then answer.

Actually, one more high-value check: the `minecraft:food` "effects" array with `chance` — I have bedrock-samples golden_apple.json evidence. But is `effects` documented anywhere reliable? bedrock-samples is official sample data, which is decent evidence. Also Blockception schemas. Let me fetch the Blockception schema for minecraft:food to confirm the field list including effects/chance. URL: https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/items/minecraft_food.json? Hmm, not sure of path. Let me try the repo search API: list contents of /behavior/items? Let me use the GitHub API to find the file.

Let me do: curl api.github.com/search/code requires auth. Instead, list the repo tree: https://api.github.com/repos/Blockception/Minecraft-bedrock-json-schemas/git/trees/main?recursive=1 — big but I can grep for "food".

Let me do that in bash and grep "food".

OK final batch:
1. node parse changelog for 1.12.0/1.13.0 sections + Cooldown lines
2. github tree grep for food schema, then fetch it
3. (maybe) fetch the food schema

Let me run 1 and 2 together.

</details>

- 🔧 **Bash** `{"command": "cat /tmp/chg.html | node -e \"\nlet s='';process.stdin.setEncoding('utf8');process.stdin.on('data',d=>s+=d);\nprocess.stdin.on('end',()=>{\n let t=s.replace(/<script[\\s\\S]*?<\\/script>/g,' ').replace(/<style[\\s\\S]*?<\\/style>/g,' ').replace(/<[^>]+>/g,'\\n');\n t=t.replace(/&amp;/g,'&').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&quot;/g,'\\\"');\n cons …[截断,原长410]` → `version-line positions: [["1.13.0",52],["1.12.0",53],["1.11.0",54],["1.13.0",2135],["1.12.0",2150],["1.11.0",2307]] --- 1.13.0 section --- 1.13.0 | Changed | Dimension | Added function | getTopmostBlock | Added | EntityLeashableComponent | Added | EntityStrengthComponent | Changed enum | EntityComponentTypes | Added va …[截断,原长1639]`

- 🔧 **Bash** `{"command": "echo \"=== find food schema in Blockception repo ===\"\ncurl -s -m 30 \"https://api.github.com/repos/Blockception/Minecraft-bedrock-json-schemas/git/trees/main?recursive=1\" | node -e \"let s='';process.stdin.on('data',d=>s+=d);process.stdin.on('end',()=>{try{const d=JSON.parse(s);(d.tree||[]).filter(x=>/food/i.test(x.path)).forEach(x=>console.log(x.path))}catch(e) …[截断,原长412]` → `=== find food schema in Blockception repo === source/behavior/items/format/components/food.json`

### 🤖 助手（`zcode-general-purpose` deepseek-flash，2026-09-27 21:48）

Let me verify the cooldown APIs and the food `effects` schema.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

The Cooldown grep printed truncated lines without version context. Let me get context: which version added getItemCooldown/startItemCooldown and ItemCooldownComponent. Let me refine: print nearest preceding version heading for those lines.

Also fetch the food.json schema from Blockception to confirm effects/chance.

Let me do both.

Also, note the 1.13.0 section content shown begins with "Changed Dimension getTopmostBlock / Added EntityLeashableComponent..." — that's the 1.13.0 section. So 1.13.0 added getTopmostBlock etc. Good; it confirms the item custom component events are NOT in 1.13.0's "Added" list, consistent with them being added in 1.12.0 (so available in 1.13.0).

Wait — careful. The changelog I fetched is the CURRENT stable changelog. It lists version sections. The ItemComponent*Event entries appeared under 1.12.0 in my earlier parse. But hold on: is that "1.12.0" the 1.12.0 stable release (game 1.21.10)? And the mapping table skips 1.12.0. Hmm. Either way, 1.13.0 > 1.12.0, so all those events exist in 1.13.0. Good.

Hmm, but actually wait. Let me double-check the earlier parse: it said "1.12.0 >> ItemComponentCompleteUseEvent" etc. But we need to be sure those lines are under the "1.12.0" heading and marked "Added". The parse associated nearest preceding bare-version line. Fine. And there were 22 hits. Let me just confirm "Added" precedes ItemComponentConsumeEvent in the text.

Let me grep the text for "ItemComponentConsumeEvent" with 2 preceding tokens.

Let me do that plus version context for Cooldown, plus fetch food schema.

Then write the answer.

</details>

- 🔧 **Bash** `{"command": "cat /tmp/chg.html | node -e \"\nlet s='';process.stdin.setEncoding('utf8');process.stdin.on('data',d=>s+=d);\nprocess.stdin.on('end',()=>{\n let t=s.replace(/<script[\\s\\S]*?<\\/script>/g,' ').replace(/<style[\\s\\S]*?<\\/style>/g,' ').replace(/<[^>]+>/g,'\\n');\n t=t.replace(/&amp;/g,'&').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&quot;/g,'\\\"');\n cons …[截断,原长410]` → `--- ItemComponent event entries with preceding tokens --- 1.12.0 :: ItemCompleteUseEvent Added ItemComponentBeforeDurabilityDamageEvent 1.12.0 :: ItemComponentBeforeDurabilityDamageEvent Added ItemComponentCompleteUseEvent 1.12.0 :: ItemComponentCompleteUseEvent Added ItemComponentConsumeEvent 1.12.0 :: ItemComponentCo …[截断,原长741]`

- 🔧 **WebFetch** `{"prompt": "Reproduce the JSON schema for the minecraft:food item component: list every property it allows, especially whether it has an \"effects\" array and what fields those effect entries have (name, duration, amplifier, chance). Also list cooldown, nutrition, saturation_modifier, can_always_eat, using_converts_to if present.", "url": "https://raw.githubusercontent.com/Bloc …[截断,原长412]` → `Based only on the provided schema, the `minecraft:food` component allows these properties: - `can_always_eat` — boolean, default `false`; described as: "If true you can always eat this item (even when not hungry), defaults to false." - `nutrition` — integer, default `0`; described as how much nutrition the food gives w …[截断,原长677]`

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

Hmm, the Blockception food.json schema doesn't include effects. But bedrock-samples golden_apple.json DOES include an effects array with chance. Conflict. So `effects` in minecraft:food is real (official sample data) but not in the MS Learn table nor Blockception schema (both incomplete). Let me verify by reading the raw golden_apple.json directly to be 100% sure (the WebFetch summarizer could have hallucinated). Let me curl it and grep.

Also check another item with effects, e.g. "enchanted_golden_apple.json" and "honey_bottle"? Let me fetch raw and grep for "effects".

Also check whether the current MS Learn food doc is just missing it. The doc's table listed only 5 fields + remove_effects. Hmm.

Also there's the "minecraft:food" "effects" documented in the older bedrock.dev docs (1.16) definitely. Let me confirm with the raw sample files.

Let me curl:
- behavior_pack/items/golden_apple.json (main branch)
- behavior_pack/items/enchanted_golden_apple.json
grep for effects/chance.

Let me also double check the food schema in the official "bedrock-samples" metadata? There's a "metadata/vanilla/..." Hmm.

Also, to be safe about "randomize": the `chance` field is per-effect probability, which IS randomization. Also `minecraft:food` in Bedrock may support "effects" with "chance" — confirmed by samples. But is there a "randomize" flag? No. Let me grep the schema repo tree for "randomize" in food-related files.

Let me run bash with curl+grep (grep on JSON is fine).

Note: grep is ugrep; use -o with simple patterns.

Let me do:
curl -s raw golden_apple.json | node -e print
curl -s raw enchanted_golden_apple.json | grep -n -A20 '"minecraft:food"'
Also check honey_bottle.json (has effects? honey bottle removes poison via script/behavior).

Let me run.

</details>

- 🔧 **Bash** `{"command": "for f in golden_apple enchanted_golden_apple honey_bottle apple; do\n echo \"=== $f.json ===\"\n curl -s -m 25 \"https://raw.githubusercontent.com/Mojang/bedrock-samples/main/behavior_pack/items/$f.json\" | node -e \"let s='';process.stdin.on('data',d=>s+=d);process.stdin.on('end',()=>{const i=s.indexOf('minecraft:food');console.log(s.slice(Math.max(0,i-40), i+700) …[截断,原长409]` → `=== golden_apple.json === "minecraft:foil": false, "minecraft:food": { "nutrition": 4, "saturation_modifier": "supernatural", "can_always_eat": true, "effects": [ { "name": "regeneration", "chance": 1.0, "duration": 5, "amplifier": 1 }, { "name": "absorption", "chance": 1.0, "duration": 120, // 2 * 60 "amplifier": 0 }  …[截断,原长986]`

- 🔧 **Bash** `{"command": "echo \"=== search Blockception repo for 'chance' in item schemas ===\"\ncurl -s -m 30 \"https://api.github.com/repos/Blockception/Minecraft-bedrock-json-schemas/git/trees/main?recursive=1\" | node -e \"\nlet s='';process.stdin.on('data',d=>s+=d);process.stdin.on('end',()=>{const d=JSON.parse(s);const paths=(d.tree||[]).map(x=>x.path);\nconsole.log('food-ish:', path …[截断,原长412]` → `=== search Blockception repo for 'chance' in item schemas === food-ish: source/behavior/items/format/components/food.json`

### 🤖 助手（`zcode-general-purpose` deepseek-flash，2026-09-27 21:49）

The schema and official sample disagree on `effects` — let me read the raw sample directly.

<details><summary>💭 `zcode-general-purpose` 思考链（deepseek-flash）</summary>

Confirmed: official bedrock-samples `golden_apple.json` has `minecraft:food.effects[]` with `name`, `chance`, `duration`, `amplifier`. So randomized effects ARE possible via per-effect `chance`. The MS Learn doc table and Blockception schema both omit `effects` — worth flagging as a doc gap.

Also confirmed apple.json uses `minecraft:use_modifiers` with start_using/use_duration 1.6/movement_modifier 0.35, and `minecraft:use_animation`.

Now I have enough. Let me also quickly confirm there's no `randomize` key: samples don't have it; Blockception schema has no randomize; MS doc has no randomize. I'll state: no `randomize` flag exists — confirmed by absence in official sample data + docs; the only randomness is the per-effect `chance`.

Now Q4: fireball explosion damage. I have minecraft:explode (power = radius and damage amount; damage_scaling scale factor; knockback_scaling; max_resistance; breaks_blocks; toggles_blocks) and minecraft:projectile on_hit impact_damage (damage range min/max rolled + power_multiplier * velocity added; ceil_pre_critical_damage; max_critical_damage default 2147483647; difficulty_randomization). Also area_attack: damage_per_tick (integer!) — note that in area_attack damage_per_tick is INT but applied repeatedly (per tick) so can stack hugely; and it has damage_cooldown.

Key point for "unexpectedly high damage": 
1. `minecraft:explode.power` scales both radius and damage; default 3; a custom power 2 is not huge but...
2. `impact_damage` + `explode` can BOTH hit the same entity (the projectile deals impact damage then triggers the explosion) → stacking (documented components, but stacking behavior is implied; mark as plausible/UNVERIFIED that both apply).
3. Repeated explosion: if the explosion event isn't removed / entity re-explodes each tick (e.g., `minecraft:explode` in a component group that stays, plus fuse_length 0 and no removal), the explosion can trigger every tick → massive damage. That's a real, common cause; docs support that explode triggers on component add and fuse; if the entity isn't removed, and the group persists... Actually with fuse_lit true and fuse_length 0 it explodes immediately; after exploding, does the entity get removed? For fireball, the vanilla has "remove_on_hit"/"remove_on_hit". Hmm. In the user's flender_fireball, on_hit → definition_event "minecraft:explode" (self) which adds the exploding group; there's no remove_on_hit! So after explosion, does the projectile persist? The explode component doesn't remove the entity by itself. If the projectile isn't removed, it could explode repeatedly? Hmm, actually the vanilla fireball has "minecraft:explode" and relies on the explosion being triggered once via event_group; the entity is removed by ... hmm the ghast fireball is removed after explosion because of the "minecraft:explode" + the projectile's own removal? In bedrock-samples fireball.json there's also a "minecraft:on_hit" with "remove_on_hit"? Actually the fireball's on_hit includes "definition_event" only; and the explosion kills the fireball? Hmm, the fireball is not damaged by its own explosion... 

I should be careful. I'll present causes as documented factors + note which are inference:
- explosion damage falls off with distance/exposure (documented for Minecraft explosions generally — but Bedrock docs don't state the formula → mark UNVERIFIED for exact formula).
- power is documented as "radius in blocks and amount of damage".
- damage_scaling multiplies explosion→entity damage; defaults 1.
- impact_damage rolled range + power_multiplier*velocity → high-velocity projectiles deal more.
- area_attack damage_per_tick is per tick and applied continuously while in range (with damage_cooldown), so an entity standing in it takes multiple hits.
- Repeated/re-triggered explosion if the entity isn't removed after exploding.
- `max_critical_damage` default 2147483647 means no clamp for projectile critical damage (INT32 max again!).

That's a solid, mostly-documented answer.

Also note: for the "custom fireball with explosion power 2", if they also have `minecraft:damage` (entity's melee?) no. Actually the user wrote "`minecraft:damage` + `minecraft:explosion` stacking" — there's no `minecraft:explosion` entity component; it's `minecraft:explode`. I'll clarify naming. Also there IS an item component `minecraft:damage` (melee damage) and a block component? For entities, the closest is `minecraft:attack` (damage) — an entity component `minecraft:attack` with `damage`. So "minecraft:damage + explosion stacking" would be entity `minecraft:attack.damage` plus `minecraft:explode`. I'll note the naming.

Let me quickly verify `minecraft:attack` entity component exists (yes, standard). I won't fetch; I'll mention it as the entity attack-damage component but mark exactness. Actually better to fetch quickly? I can cite from the component list. Let me just say entity component `minecraft:attack` (damage) — I'm confident. Hmm, but "do not speculate". I'll phrase: "the entity component that sets melee damage is minecraft:attack (documented in the entity component list)". Risk is low. Actually let me not over-claim; I'll keep Q4 focused on what I fetched.

Now, about Q1: I need to give a concrete workaround. Options grounded in docs:
(a) Don't rely on movement_modifier for a "hold to charge" item: remove movement_modifier (or set 1) and apply slowness via script (addEffect/removeEffect) that you control and always clear on itemStopUse/itemReleaseUse. This is the safest: the engine state can't leak if you own the effect.
(b) Set a finite use_duration (e.g. 1–5 s, like apple 1.6) and re-trigger casting from script (re-start use) — avoids the "never completes" state.
(c) On stop-use, force the client out of the in-use state: the common script trick is to re-set the item stack in the slot (inventory.setItem(slot, itemStack)) — but that doesn't necessarily reset the client's "using" flag; the reliable known trick is to set the selected slot to a different slot and back (player.selectedSlotIndex = other; then back), which is exactly what players do manually to clear it. Since there's no cancelUse API, doing a slot round-trip on itemStopUse is a plausible workaround; mark as not officially documented.
(d) Also clear the item cooldown: Player.startItemCooldown(category, 0) / getItemCooldown(category) — documented. Note there is NO clearCooldown method; the API is getItemCooldown/startItemCooldown (added in 1.11.0 per changelog). If the stuck slow is caused by the cooldown overlay, startItemCooldown(cat, 0) clears it. But cooldown is a different thing from movement.

Also note: for their staff.json, since use_duration=2147483647 seconds means the item NEVER completes a use, `onCompleteUse` will never fire, `minecraft:cooldown` may never (or immediately) trigger depending on engine, and itemStopUse fires on release. So they should use afterEvents.itemStopUse/itemReleaseUse (which their code already does) and additionally force the client out of the using state.

Important: their staff.json has `minecraft:cooldown` duration 6 with the same category as the "use". If cooldown starts at use-start and the "use" never completes, the client's held-item in-use state may indeed persist. I'll mention this as a plausible mechanism but mark UNVERIFIED.

Also worth noting: with use_duration = 2147483647, the client shows the "eating/using" animation/slowness for the ENTIRE hold (since movement_modifier applies "while the item is in use"), which is intended. The bug is that on release the client may not clear "in use".

Now, about whether 2147483647 causes clamping/overflow: The value is INT32 max. The engine stores use_duration as a float seconds internally (docs type: Decimal number). 2147483647 s = 2^31-1 seconds ≈ 68 years = ~1.36e12 ticks. If the engine converts seconds→ticks and stores in a 32-bit signed int, 2147483647 seconds * 20 ticks = 4.29e10 ticks, which OVERFLOWS int32 → wraps to negative/undefined. That's a concrete, plausible overflow mechanism. I must mark it as inference/UNVERIFIED (no doc states the internal type), but it's a well-reasoned hypothesis and the recommendation is to avoid INT32 max and use a smaller finite value.

Actually, hmm — can I verify anything about a maximum? Let me check if there's any doc with a max. The MS doc says "Decimal number" and no bounds. Wiki.bedrock.dev says nothing. So no documented max. Good: I'll say "no documented maximum; 2147483647 is not documented as valid or invalid; recommend a finite value".

OK. Let me also mention the `start_using` field ("if_first" is now available in 1.26.30 — not in their version) — irrelevant.

One more: for Q1 I should mention that `minecraft:cooldown` "type" field ('use' default) exists only from format 1.21.130 — not relevant to 1.13/1.21.20.

Wait — but the user's game is 1.21.113 per them, and format versions up to 1.21.130 exist. Their staff.json uses format_version 1.21.10. Fine.

Now about the version mismatch: @minecraft/server 1.13.0 ↔ Minecraft 1.21.20 per the official mapping table. If their game is truly 1.21.113, then their manifest's 1.13.0 dependency is much older than the game — stable APIs are backward compatible so requesting an older minor version is satisfied (per the versioning doc: dependency on 1.3.0 "may actually have that dependency fulfilled with 1.8.0"). So the game will run it, but they'd lose access to newer APIs. Also note that the 1.13.0 docs correspond to game 1.21.20 semantics. I'll flag this.

Hmm wait, is "1.21.113" a plausible Bedrock version? Bedrock versions: 1.21.100, 1.21.110... In 2026, sure. But actually the versioning table only goes to 1.17.0 (1.21.60) and the food/cooldown docs mention "requires format version 1.21.130" and "1.26.30" — suggesting the docs now describe 1.26.x. So the game in 2026-09 might be 1.26.x! Then "1.21.113" is odd. Hmm, could the user mean game version 1.21.113? Or the doc's "1.21.130" indicates a 1.21.13x exists. Hmm, the docs said cooldown `type` "requires a format version of at least 1.21.130" — so format 1.21.130 exists (a 1.21.13x game?). And "use_modifiers.start_using requires 1.26.30". Both exist in the docs. So Bedrock versioning has both 1.21.13x and 1.26.x?? That's inconsistent unless "1.26.30" is a doc typo for "1.21.130"/"1.21.<something>". Actually the docs elsewhere mention "1.26.0", "1.26.20", "1.26.30", "1.26.40" — so the doc set (updated 2026) uses 1.26.x as the current-ish format versions. And minecraft:projectile isolated_physics "requires format version 1.26.20". So the current preview is ~1.26.x. Then a game at 1.21.113 would be old (1.21.110, 2025). And 1.26.x would be the 2026 versions. Hmm, Minecraft versioning jumped 1.21.130 → 1.26.x? That seems odd but whatever; not my concern.

Actually wait: "1.26.30" might be "1.21.130" mis-rendered? No, the page literally says 1.26.30. And the search results included "1.26.30 Update Notes" and "1.26.40 Update Notes" pages. So yes, Minecraft Bedrock reached 1.26.x. Then the user's "1.21.113" would be an actual older release (like 1.21.110/1.21.113 in the 1.21.1xx series). OK. So a game at 1.21.113 with @minecraft/server 1.13.0 is a big mismatch (1.21.113 would ship a much newer server version, e.g. 1.2x.0). Hmm, but they said 1.13.0. I'll flag the mapping and note that a manifest requesting 1.13.0 on a 1.21.113 game still works (satisfied by a higher minor).

Hmm, actually careful: Minecraft may cap how far back stable versions are supported. The versioning doc says it "may" be fulfilled. I'll note it as "normally satisfied upward".

OK, now also for Q2 "Which ones were added in which version" — answer: all ItemCustomComponent events (onBeforeDurabilityDamage, onCompleteUse, onConsume, onHitEntity, onMineBlock, onUse, onUseOn) were added in @minecraft/server 1.12.0 (stable track) per the changelog; therefore all are available in 1.13.0. Note the earlier @beta history isn't shown. I'll say: per the current stable changelog, they first appear under 1.12.0 with "Added".

Hmm, but is it possible the changelog's 1.12.0 entries reflect when they were added to that version's doc, not necessarily stable? The changelog (view=stable) is the stable changelog. Good enough, and I'll cite the URL.

Wait, one caution: the versioning mapping table has no 1.12.0 row, implying 1.12.0 might not map to a shipping game version. Regardless, 1.13.0 (1.21.20) contains them.

Q2 sub-question: does onConsume/onCompleteUse fire for items that are also minecraft:food? Docs don't address. Mark UNVERIFIED. Note the docs require minecraft:food to have use_modifiers (with use_duration) "in order to work properly" — and with use_duration 2147483647 onUse/onCompleteUse semantics change (complete never happens).

Also: can the handler cancel consumption? Both events are read-only and return void → no cancellation. Confirmed from signatures.

Now let me also mention that ItemCustomComponent is bound via ItemComponentRegistry.registerCustomComponent and referenced in the item JSON under `minecraft:custom_components`.

Let me write the final answer now. Keep it organized by question, with citations as URLs. Mark UNVERIFIED items clearly.

I should also give concrete code for the recommended workaround. I'll provide a script snippet adapted to their staffs.js (using itemStopUse to clear the slowed state) — but since movement_modifier is engine-side, the real fix is to drop movement_modifier and control slowness via effects, or to avoid 2147483647.

Let me provide:
1. Recommended: use a finite use_duration (e.g., 2–5 s) OR remove movement_modifier and apply slowness yourself.
2. If keeping movement_modifier: on itemStopUse/itemReleaseUse, force a slot round-trip (documented APIs: Player.selectedSlotIndex), and clear cooldown via startItemCooldown(category, 0).
3. Their staffs.js already clears casting on itemStopUse; add the forced reselect + cooldown clear.

Let me give a snippet:

```js
import { world, system } from "@minecraft/server";

const STAFFS = ["lucky:staff", "lucky:ice_staff", "lucky:flender_staff"];
const COOLDOWN_CATEGORY = "lucky:staff";

function forceReleaseUse(player) {
    // 1) 清掉物品冷却（setItemCooldown(0)），避免“冷却中仍被判定为使用中”
    try { player.startItemCooldown(COOLDOWN_CATEGORY, 0); } catch {}
    // 2) 强制客户端退出 “in use” 状态：把选中槽换到另一个槽再换回来
    const slot = player.selectedSlotIndex;
    try {
        player.selectedSlotIndex = (slot + 1) % 9;
        system.runTimeout(() => {
            try { player.selectedSlotIndex = slot; } catch {}
        }, 1);
    } catch {}
}
```
Note: Player.selectedSlotIndex is documented and settable (stable). startItemCooldown documented (added 1.11.0), bounds 0..32767.

And note: there is NO Player.clearCooldown in the API; the documented methods are getItemCooldown / startItemCooldown. That directly answers their "clearCooldown" question.

Also note: inventory.setItem re-set of the stack (container.setItem) is commonly suggested but I found no documentation that it clears the client "in use" state → mark UNVERIFIED.

Alright. Also mention: the user's staff.json cooldown duration 6 same category is shared across all three staffs (since all use category "lucky:staff") — actually that's a real finding: all three staffs share cooldown category, so using one puts all three on cooldown. That may be intended or not. Worth noting.

Let me now write the final answer. Keep it thorough but organized. Use headings. Include URLs.

Also I should mention the local file paths I inspected.

One more thing to verify quickly? The ItemComponentHitEntityEvent/UseOnEvent properties — user didn't explicitly ask for signatures of those, only onConsume/onCompleteUse. I have ItemComponentUseEvent (itemStack?, source: Player). Good.

Also I should mention ItemComponentConsumeEvent source is `Entity` (not Player) — from the doc: `read-only source: Entity; "The source entity that consumed the item."` Good detail.

Let me write it.

Length: this is a research answer; be reasonably complete but not bloated. I'll use compact tables/lists.

I'll note the search limitation for Q1.

Let me finalize.

</details>

### 🤖 助手（`zcode-general-purpose` deepseek-flash，2026-09-27 21:49）

I have enough verified material. Here is the report.

---

# Sources used (all fetched live)

- MS Learn `@minecraft/server` **changelog** — https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/changelog?view=minecraft-bedrock-stable (parsed the raw HTML, not a summary)
- MS Learn **Script Module Versioning** (the official `@minecraft/server` ↔ game-version table) — https://learn.microsoft.com/en-us/minecraft/creator/documents/scripting/versioning?view=minecraft-bedrock-stable
- `ItemCustomComponent`, `ItemComponentConsumeEvent`, `ItemComponentCompleteUseEvent`, `ItemComponentUseEvent`, `ItemComponentRegistry`, `Player`, `minecraft:food`, `minecraft:use_modifiers`, `minecraft:cooldown`, `minecraft:explode`, `minecraft:projectile`, `minecraft:area_attack` reference pages on Learn
- Official sample data `Mojang/bedrock-samples` (raw GitHub) — `golden_apple.json`, `honey_bottle.json`, `apple.json`
- `wiki.bedrock.dev/items/item-components`
- Mojira public API (`POST https://bugs.mojang.com/api/jql-search-post`) — see caveat in Q1

I also read your actual addon files (relevant to Q1/Q4):
- `C:\Users\UserX\Downloads\幸运方块地图_法杖增强版_竞技场版\behavior_packs\LuckyBlock\items\staffs\staff.json`
- `...\behavior_packs\LuckyBlock\scripts\staffs.js`
- `...\behavior_packs\LuckyBlock\entities\staffs\flender_fireball.json`, `...\entities\staffs\ice_projectile.json`

**Important version correction first.** The official mapping table says `@minecraft/server` **1.13.0 = Minecraft 1.21.20** (1.11.0=1.21.0; 1.13.0=1.21.20; 1.14.0=1.21.30 … 1.17.0=1.21.60). It does not list 1.12.0 at all. So "game 1.21.113 + script API 1.13.0" is a mismatch: if the game really is 1.21.113 it ships a much newer `@minecraft/server`, and your manifest is pinned to an old minor. That still runs (stable minors are backward-compatible and an older request is satisfied by a newer minor), but you are coding against 1.21.20-era semantics and lose newer APIs. Source: the versioning page above. **UNVERIFIED** whether 1.21.113 exists as a public version — I could not confirm that build number.

---

# QUESTION 1 — the "stuck movement modifier"

**Answer up front: I could NOT verify this as a documented/known engine bug. Treat the "known bug" framing as UNVERIFIED.**

What I tried and got:
- Mojira's `jql-search-post` API answered with valid JSON but returned **0 issues for every query**, including control queries (`text ~ "creeper"`, `project = MCPE`, `key = MCPE-1`). So the endpoint is reachable but returns empty for everything — my negative result is **INCONCLUSIVE**, not evidence the bug is unreported.
- DuckDuckGo / Bing / Mojeek were all blocked from this environment (timeout / 403), GitHub issue search found nothing relevant. **No citable community thread or ticket was located.**

**What IS documented (citable):**
- `movement_modifier` — "Multiplier applied to the player's movement speed **while the item is in use**. Value must be <= 1." (https://learn.microsoft.com/en-us/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_use_modifiers?view=minecraft-bedrock-stable)
- `use_duration` — "Time, in seconds, that the item takes to use." Default 0. **No documented maximum, no documented minimum, no bounds.** Same page. wiki.bedrock.dev words it identically ("The time duration (in seconds) that the item must be used for to complete a single use.") — also no max.
- `minecraft:food` "requires the following component in order to work properly: minecraft:use_modifiers" (minecraft_food page).
- `minecraft:cooldown` — "Adds a cooldown to an item, preventing it from being used again for a specified duration. Items sharing the same category will enter cooldown together when any one of them is used." (minecraft_cooldown page). **The docs do NOT state whether the cooldown starts at use-start or at use-complete.** → the specific interaction you asked about ("does cooldown starting while still held cause the client 'in use' state to persist?") is **UNVERIFIED** by any documentation; I found no source stating it.
- `minecraft:cooldown` also supports `type: use|attack` and notes "If this value is a negative number, it renders the item unusable." (wiki.bedrock.dev version; MS Learn only documents `type`, which requires format 1.21.130).

**About `use_duration = 2147483647`:**
- It is INT32_MAX. `2147483647` seconds ≈ 2^31 s ≈ **68 years** ≈ 1.36e12 ticks. Because `use_duration` is a *Decimal number of seconds*, if the engine converts seconds→ticks into a 32-bit signed int, `2147483647 * 20` overflows int32. **UNVERIFIED** — no documentation states the internal storage type or any clamp, and I will not assert overflow as fact. I can only say: no documented max exists, INT32_MAX is the classic "infinite" idiom, and a finite value is the safe choice.

**Script-side API facts you'll want (these are verified):**
- There is **no `Player.clearCooldown`**. The documented Player methods are:
  - `getItemCooldown(cooldownCategory: string): number`
  - `startItemCooldown(cooldownCategory: string, tickDuration: number): void` — `tickDuration` **bounds [`0`, `32767`]**
  Both were added in **@minecraft/server 1.11.0** (from the changelog HTML: `1.11.0 :: getGameMode Added function getItemCooldown`, `1.11.0 :: setGameMode Added function startItemCooldown`). `ItemCooldownComponent` was added in 1.10.0. So on 1.13.0 both exist; passing `0` is the documented way to zero a cooldown.
  Source: https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/player?view=minecraft-bedrock-stable
- `Player.selectedSlotIndex: number` is documented and writable (same page) — this is the only documented script lever that reproduces exactly what players do manually ("switch hotbar slot and back").
- Re-setting the stack via `container.setItem(slot, stack)` is used widely in community code, but **I found no documentation that it clears the client's "in use" state → UNVERIFIED as a fix.**

**Recommended workaround (my engineering recommendation, NOT a cited community fix — flag it as such):**
1. **Preferred: stop using `movement_modifier` for a "hold-forever" item.** Keep the item's `use_duration` finite (e.g. apple uses `1.6`, see official `apple.json`), and drive the slow yourself with `addEffect("slowness", …, {showParticles:false})` on `itemStartUse` and **always `removeEffect("slowness")` on `itemStopUse` / `itemReleaseUse`**. You then own the state and it cannot leak. (Your `staffs.js` already subscribes to `itemStopUse` *and* `itemReleaseUse` in `handleStopUse`, so this slots straight in.)
2. **If you keep `movement_modifier`:** replace `use_duration: 2147483647` with a finite value. Note that with the current value the use can literally never complete, so `onCompleteUse` can never fire and `minecraft:cooldown`'s start point is undefined.
3. **Symptom-level unstick, only if you must:** on `itemStopUse`, zero the cooldown and force the client out of the using state with a slot round-trip:

```js
import { system } from "@minecraft/server";
const COOLDOWN_CATEGORY = "lucky:staff";

function forceReleaseUse(player) {
    try { player.startItemCooldown(COOLDOWN_CATEGORY, 0); } catch {}   // documented, bounds 0..32767
    const slot = player.selectedSlotIndex;
    try {
        player.selectedSlotIndex = (slot + 1) % 9;                      // documented, writable
        system.runTimeout(() => {
            try { player.selectedSlotIndex = slot; } catch {}
        }, 1);
    } catch {}
}
```
Call it from your existing `handleStopUse`. **UNVERIFIED** that this clears the engine "in use" flag; it is the scripted equivalent of the manual workaround your players already found.

**Side finding about your item:** in `staff.json` the cooldown is `{"category": "lucky:staff", "duration": 6}`. Per the docs, *items sharing a category enter cooldown together* — and all three staffs use the same `lucky:staff` category, so casting with one staff puts all three on cooldown. If that's unintended, split the categories.

---

# QUESTION 2 — ItemCustomComponent events in 1.13.0

**Which exist, and when added.** Parsed straight from the stable changelog HTML, every item custom component class is listed as **"Added" under `1.12.0`** — there is nothing before it — so **all of them are present in 1.13.0**:

| Class (hook) | Changelog line |
|---|---|
| `ItemComponentBeforeDurabilityDamageEvent` (`onBeforeDurabilityDamage`) | `1.12.0 :: … Added ItemComponentBeforeDurabilityDamageEvent` |
| `ItemComponentCompleteUseEvent` (`onCompleteUse`) | `1.12.0 :: Added ItemComponentCompleteUseEvent` |
| `ItemComponentConsumeEvent` (`onConsume`) | `1.12.0 :: Added ItemComponentConsumeEvent` |
| `ItemComponentHitEntityEvent` (`onHitEntity`) | `1.12.0 :: Added ItemComponentHitEntityEvent` |
| `ItemComponentMineBlockEvent` (`onMineBlock`) | `1.12.0 :: Added ItemComponentMineBlockEvent` |
| `ItemComponentRegistry` | `1.12.0 :: Added ItemComponentRegistry` |
| `ItemComponentUseEvent` (`onUse`) | `1.12.0 :: Added ItemComponentUseEvent` |
| `ItemComponentUseOnEvent` (`onUseOn`) | `1.12.0 :: Added ItemComponentUseOnEvent` |

So: **`onConsume` — yes, available in 1.13.0. `onCompleteUse` — yes.** Also note you didn't list it, but **`onMineBlock` exists** too. The changelog shows no further changes in 1.13.0/1.14.0…; changes only appear at **2.0.0** (`ItemComponentRegistry.registerCustomComponent` and `ItemCustomComponentInstance`). Source: the changelog URL above.

Caveat: the changelog is the *current* stable changelog; it does not show a pre-1.12.0 `-beta` history, and it carries no explicit `@beta` marker per version. I'm quoting the stable doc's version headings verbatim.

**Signatures / fields (all read-only, all return `void` — see below):**
- `onConsume?: (arg0: ItemComponentConsumeEvent, arg1: CustomComponentParameters) => void`
  - `read-only itemStack: ItemStack` — "The item stack that was consumed."
  - `read-only source: Entity` — "The source entity that consumed the item." (note: `Entity`, not `Player`)
- `onCompleteUse?: (arg0: ItemComponentCompleteUseEvent, arg1: CustomComponentParameters) => void`
  - `ItemComponentCompleteUseEvent **extends ItemCompleteUseEvent**`, which carries
    - `read-only itemStack: ItemStack` — "the item stack that has completed charging"
    - `read-only source: Player`
- `onUse?: (arg0: ItemComponentUseEvent, …) => void` → `read-only itemStack?: ItemStack`, `read-only source: Player`
- `onBeforeDurabilityDamage`, `onHitEntity`, `onUseOn`, `onMineBlock` also all take `(eventType, CustomComponentParameters)`.

URLs: `https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/itemcustomcomponent?view=minecraft-bedrock-stable`, `.../itemcomponentconsumeevent`, `.../itemcomponentcompleteuseevent`, `.../itemcompleteuseevent`, `.../itemcomponentuseevent`, `.../itemcomponentregistry`. Registration is via `ItemComponentRegistry.registerCustomComponent(name, itemCustomComponent)` (name must be namespaced, referenced from item JSON under `minecraft:custom_components`).

**Can the handler cancel consumption? No.** Both `onConsume` and `onCompleteUse` are declared `=> void`; their event objects expose only `read-only` properties and there is no `cancel`/`setCanceled` member anywhere in the interface. **No cancellation is possible via the item custom component events in 1.13.0.** (The docs never mention a cancel mechanism; this is a "confirmed by absence in the signature" answer.)

**Do they fire for an item that is also `minecraft:food` (with `can_always_eat` / `using_converts_to`)?** **UNVERIFIED.** The docs do not state whether custom component hooks fire alongside the built-in food behavior, and I found no note about conflicts between `minecraft:food` and script item components. The only documented coupling is one-directional: `minecraft:food` *requires* `minecraft:use_modifiers` to "work properly". Two concrete, verifiable consequences of your config you should be aware of: (a) with `use_duration: 2147483647` the "use duration" never completes, so `onCompleteUse` is unreachable; (b) if you also put `minecraft:cooldown` on a food item, the cooldown is per-category and shared across every item with that category.

---

# QUESTION 3 — Item JSON

**Randomized effects in `minecraft:food`?** There is **no `randomize` flag and no "pick a random effect" mechanism**. What exists is a **per-effect probability** via `chance` — confirmed from the official sample `Mojang/bedrock-samples/behavior_pack/items/golden_apple.json`:

```json
"minecraft:food": {
  "nutrition": 4,
  "saturation_modifier": "supernatural",
  "can_always_eat": true,
  "effects": [
    { "name": "regeneration", "chance": 1.0,  "duration": 5,   "amplifier": 1 },
    { "name": "absorption",   "chance": 1.0,  "duration": 120, "amplifier": 0 }
  ]
}
```
Source: https://raw.githubusercontent.com/Mojang/bedrock-samples/main/behavior_pack/items/golden_apple.json

So each listed effect is independently rolled against its own `chance` (1.0 = always). That is the only randomness the component offers — it is *probability per effect*, not *selection among effects*. Anything beyond that (e.g. "one random effect out of N", random amplifier, random duration) requires script. **Documentation gap worth knowing:** the MS Learn `minecraft:food` table lists only `can_always_eat`, `nutrition`, `saturation_modifier`, `using_converts_to`, `remove_effects` (deprecated) — it **omits `effects`**. Blockception's `food.json` schema also omits it. The field is nonetheless present in Mojang's own sample data. `remove_effects` is documented as deprecated and non-functional after format 1.20.0 (though `honey_bottle.json` still ships it).

**`minecraft:cooldown` — what it does and when it starts.** Cited text: "Adds a cooldown to an item, preventing it from being used again for a specified duration. Items sharing the same category will enter cooldown together when any one of them is used." Fields: `category` (string, groups items), `duration` (seconds; wiki.bedrock.dev adds "If this value is a negative number, it renders the item unusable"), `type` (`use` default | `attack`, format ≥1.21.130).
**When the cooldown starts for a `minecraft:food` item with a `use_duration`: NOT DOCUMENTED → UNVERIFIED.** Neither MS Learn nor wiki.bedrock.dev says whether it starts on use-start or on consumption/use-complete. Practically: since your `use_duration` is effectively infinite, a food item can never reach the "completed" point, so the two possible semantics differ a lot — but I have no source to cite either way.

**Is `use_duration: 2147483647` valid/harmful? What's the max?**
- Documented type: **Decimal number**, default `0`, meaning seconds. **No documented maximum and no documented minimum** (MS Learn `minecraft_use_modifiers`; wiki.bedrock.dev agrees). So there is **no documented "recommended value for hold-indefinitely"** — that idiom is community practice, not documentation. → mark "official max/recommended" as **does not exist in the docs**.
- `movement_modifier` *does* have a documented constraint: **"Value must be <= 1."**
- The value being exactly INT32_MAX is suspicious (possible seconds→ticks integer overflow), but as stated in Q1 this is **UNVERIFIED**. Safe recommendation: use a finite duration.

---

# QUESTION 4 — explosion / area_attack damage (concise)

**Naming first:** there is no entity component called `minecraft:explosion`. The entity component is **`minecraft:explode`** (https://learn.microsoft.com/en-us/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_explode). Your `flender_fireball.json` uses `minecraft:explode`, and it uses `"power": 4` (not 2 — the `power: 2` files in your pack are `entity_tnt.json`, `christmas_grenade.json`, `lightning_projectile.json`, `explode.json`, `ultra_instinct_projectile.json`, `spiral_arrow.json`).

Documented `minecraft:explode` fields (defaults):
- `power` (default **3**) — "The radius of the explosion in blocks **and the amount of damage** the explosion deals" (Fireball vanilla = 1; Ender Crystal = 6).
- `damage_scaling` (default **1**) — "A scale factor applied to the explosion's damage to entities. A value of 0 prevents… damage. **Negative values cause the explosion to heal** entities instead."
- `knockback_scaling` (default 1), `breaks_blocks` (default **true**), `causes_fire` (false), `destroy_affected_by_griefing` / `fire_affected_by_griefing` (false), `max_resistance` (3.40282e+38), `negates_fall_damage`, `toggles_blocks`, `fuse_length`, `fuse_lit`.

Documented `minecraft:projectile` → `on_hit` → `impact_damage` (https://learn.microsoft.com/en-us/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_projectile):
- `damage` is a **range** `{min,max}`: "A random value in `[min,max]` is rolled **per hit** and the velocity-scaled `power_multiplier` term is added to it."
- `power_multiplier` (default 0) — "Multiplied by the projectile's velocity and added to the rolled `damage`." ← **the main "unexpectedly high damage" lever for fast projectiles.**
- `difficulty_randomization` (`none`|`additive`|`multiplicative`) — "folds the difficulty term into `power_multiplier` before scaling by velocity."
- `ceil_pre_critical_damage` — rounds projectile damage UP to the next integer **before** the crit multiplier.
- `max_critical_damage` default **`2147483647`** / `min_critical_damage` default 0 — "clamps the final damage value of critical hits" (i.e. by default there is effectively **no upper clamp** — note INT32_MAX again).
- Top-level `minecraft:projectile` also has `power` (default 1.3, = launch speed in blocks/tick), `uncertainty_base - difficultyLevel * uncertainty_multiplier`, `multiple_targets`, `hit_nearest_passenger`.

Documented `minecraft:area_attack` (https://learn.microsoft.com/en-us/minecraft/creator/reference/content/entityreference/examples/entitycomponents/minecraftcomponent_area_attack):
- `damage_per_tick` (default 2, **integer**) — "How much damage **per tick** is applied to entities that enter the damage range."
- `damage_cooldown` (default 0) — "Attack cooldown (in seconds) for how often this entity can attack a target."
- `damage_range` (default 0.2), `entity_filter`, `cause`, `use_self_as_damage_source` (default true, format ≥1.26.30).
  → Because `damage_per_tick` is applied on a tick cadence, "very high damage" from `area_attack` almost always means **many applications** (tiny/zero `damage_cooldown` + a large `damage_range` catch box), not a big number.

**Known/derivable causes of unexpectedly high explosion damage in Bedrock, ranked:**
1. **`impact_damage` and `explode` both landing on the same entity** — your `flender_fireball` triggers `minecraft:explode` via `definition_event` on hit; if the projectile also has `impact_damage`/`catch_fire`, the target can take impact damage *and* explosion damage. (Both components are documented; that they stack on one target is inference → treat the exact stacking as **UNVERIFIED**.)
2. **Repeated explosions.** With `fuse_length: 0` + `fuse_lit: true`, an `minecraft:explode` component group added more than once (or an entity that isn't removed) will detonate repeatedly. Your `flender_fireball.json` has **no `remove_on_hit`** — worth auditing; the vanilla `fireball.json` also has no `remove_on_hit`, but it relies on the `minecraft:exploding` component group being added once via the `minecraft:explode` event. Any script/JSON path that re-adds that group re-detonates.
3. **`power` is both radius and damage**, so raising radius raises damage linearly — and any nearby secondary explosion (e.g. your `lucky:ice_projectile` also uses `power: 4`, and `entity:explode` uses `power: 2`) chain-reacts.
4. **`damage_scaling` default is 1, and `max_resistance` default is 3.4e38**, i.e. nothing is clamped by default; `damage_scaling: 0` is the documented "no entity damage" switch (used by vanilla Wind Charge/Breeze).
5. **`power_multiplier` × velocity + `difficulty_randomization: multiplicative`** on the projectile's `impact_damage` — fast projectiles hit much harder on Hard.
6. **Integer/INT32 permissiveness**: `impact_damage.max_critical_damage` defaults to 2147483647 and `explode.max_resistance` to 3.4e38, so nothing stops a runaway number from being applied.
7. **Distance/exposure falloff of vanilla explosions** — the reason "sometimes" low, "sometimes" lethal. The *formula* for Bedrock's explosion damage-vs-distance/exposure is **not documented on Learn → UNVERIFIED**; do not quote a formula from me.

---

## Summary of what is UNVERIFIED (do not treat as fact)

1. Q1 — that the stuck-slow is a *known engine bug*: **inconclusive**; my bug-tracker search returned empty for every query (including controls), and all search engines were blocked. No citable community thread found.
2. Q1/Q3 — that `use_duration: 2147483647` causes client clamping/overflow weirdness: plausible, **not documented**, no source states internal storage type or any clamp.
3. Q1 — that `minecraft:cooldown` starting while the item is still held is what makes the client "in use" state persist: **no source**; the docs don't even state when a cooldown begins.
4. Q1 — that `container.setItem` or a `Player.selectedSlotIndex` round-trip clears the client "in use" flag: **not documented** (the APIs are documented; the effect on the client state is my inference).
5. Q2 — whether item custom components (`onConsume`/`onCompleteUse`) fire for an item that is also `minecraft:food`, and any food↔script conflict: **not documented**.
6. Q4 — the exact Bedrock explosion damage-vs-distance/exposure formula, and whether `impact_damage` + `explode` literally sum on one target: **not documented**.
7. The game build "1.21.113" itself — I could not confirm it exists; the official table maps script API 1.13.0 to Minecraft **1.21.20**, which conflicts with your stated pairing.
