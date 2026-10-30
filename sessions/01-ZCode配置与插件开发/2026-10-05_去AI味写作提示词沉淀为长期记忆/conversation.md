## 👤 用户（2026-10-05 13:28）

我觉得ai写的文档，报告，教程等，在语言结构和句子上就是一坨屎，看得我非常难受。现在请你参考以下这些建议或ai常见句式，总结一个精简但是有效的提示词并写入长期记忆。ai味很浓的常见句式：说实话…、A的本质是B、不是…而是…、先…再…、让我们…、如果…就…、只有…、意味着…、唯一…、无论…都…、要么…要么…、我的建议是…、记住…、就算…也…、全文、一句话、之所以…是因为…、说白了…

> 📎 附件: image/png

<details><summary>💭 思考链（GLM-5.3-Flash）</summary>

The user wants me to summarize a concise but effective prompt for removing AI-flavored writing, based on:
1. The list of common AI sentence patterns they listed
2. The image they provided (which contains advice about writing with judgment, avoiding filler, etc.)

Then write it into long-term memory (the memory directory).

Let me first look at the image content carefully. The image says (in Chinese):

"你是一位对自己判断负责的作者。你的任务是形成清楚的判断，并用必要的信息把它讲清楚。不要扮演一个试图讨好读者、面面俱到、自动平衡所有观点的助手。写作意味着做出选择：什么值得说，什么可以省略，什么证据足以支持判断，什么只是填充。

动笔前先想清楚三个问题：这一段要回答什么问题，我的判断是什么，我凭什么这样判断。想清楚以后再写。没有足够依据的地方，不要用抽象概念、套话和修辞掩盖。每一段承担一个主要任务，段落之间依靠问题、判断和证据自然推进，不要为了形式完整机械安排结构。

正面立论。确定判断后直接陈述，再给依据。不要预设不存在的反对者，不要为了制造张力人为构造对立。不要使用"不是……而是……"的句式，直接写你真正想表达的判断。竞争性解释、理论边界和限制，只在它们真正影响当前判断时讨论。观点可以有边界，但边界应来自理论和证据，不要习惯性使用"可能""一定程度上""值得..."(被遮挡)

每句话都应增加新的信息。删掉一句以后，如果读者的理解没有发生变化，这句话通常没有必要存在。优先使用具体事实、数据、机制、行为、案例和可观察现象。不要为了显得完整补充与当前论证无关的背景，也不要换一种说法重复已经说清楚的判断。一个判断提出以后，后面的文字应该继续提供证据、机制、推论或边界。

使用成熟作者自然使用的语言。句子服从意思，不追求整齐。长短可以变化，段落结构也可以变化。少用"值得注意的是""需要指出的是""从某种意义上说"等没有信息增量的起手式。不要机械使用"首先、其次、最后""一方面、另一方面"等模板。不要为了显得深刻制造空洞的比喻、排比、转折和拔高。一个段落完成论证后可以直接结束，不需要再补一句总结意义。

不要反复给自己的判断加保险。有充分依据时，用正常的陈述句承担判断；证据只能支持有限结论时，准确说明边界。区分真正的证据限制和作者对判断的不自信。不要提前回应尚未出现的质疑，也不要把大量防御性表述塞进正文。真正重要的替代解释，在需要处理的位置集中讨论。"

So the task: create a concise but effective prompt (提示词) that combines:
1. The user's list of AI-flavored sentence patterns to avoid: 说实话…、A的本质是B、不是…而是…、先…再…、让我们…、如果…就…、只有…、意味着…、唯一…、无论…都…、要么…要么…、我的建议是…、记住…、就算…也…、全文、一句话、之所以…是因为…、说白了…
2. The image's advice (which is a good writing philosophy: responsible author, direct judgment, evidence, no filler, no mechanical structure, no hedging, etc.)

And there's also an existing skill `paper-resume-writing` which covers 论文 Introduction 七步法 + 简历去 AI 味五特征. This new request is more general — 文档、报告、教程 (documents, reports, tutorials). The memory note says the paper-resume-writing skill is constrained to ≤600 chars.

The user says: "总结一个精简但是有效的提示词并写入长期记忆" — summarize a concise but effective prompt and write it into long-term memory.

Where should this go? The memory directory: `C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory\`. That's the auto-memory. But the user also has `~/.zcode/AGENTS.md` (user default instructions) and `~/.zcode/memory/` for their own curated memories. Hmm.

The "长期记忆" here — the user's own memory system at `~/.zcode/memory/` has files like `output-preferences.md`, `python-envs.md`, etc. The AGENTS.md says "做汇报/PPT、物理数学讲义或教学工具前，必读 ~/.zcode/memory/output-preferences.md".

But the system prompt defines my auto-memory at `C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory\`. The instruction says "写入长期记忆" — write into long-term memory. There are two candidate places:

1. My auto-memory directory (system-managed): `C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory\`
2. The user's own memory: `~/.zcode/memory/` (e.g. a new file like `de-ai-writing-prompt.md`) — this one gets loaded via AGENTS.md index, which the user maintains manually.

The user said "写入长期记忆" without specifying. Given the user's AGENTS.md pattern, they maintain an index of memories at ~/.zcode/memory/ and reference them from AGENTS.md. But the auto-memory is what I control directly and "persists across conversations".

Hmm, the paper-resume-writing skill is at `~/.zcode/skills/paper-resume-writing/SKILL.md` — that's a skill, 558 chars, for papers and resumes specifically. The user now wants a general-purpose de-AI prompt for 文档、报告、教程.

Considering: the memory instruction in my system prompt says to use my memory directory at `C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory\` and write files with frontmatter, then update MEMORY.md index.

But wait — there's an important nuance: a "提示词" (prompt) that should apply to future document writing. If it's buried in auto-memory, it will be recalled only when relevant. The user's AGENTS.md mechanism is loaded every session (user default instructions). Actually the user's own memory index in AGENTS.md is the "每会话生效" mechanism.

Let me think about what the user wants pragmatically: They want this prompt to be applied when I write documents/reports/tutorials in the future. The most reliable place would be:
- Option A: my auto-memory (guaranteed loaded index MEMORY.md, and files recalled by relevance)
- Option B: ~/.zcode/memory/ + AGENTS.md index line (loaded every session via AGENTS.md)

The user said "写入长期记忆" — in previous sessions, we've saved things like output-preferences.md into ~/.zcode/memory/. The AGENTS.md says "做汇报/PPT、物理数学讲义或教学工具前，必读 ~/.zcode/memory/output-preferences.md". So there's precedent for output style preferences living in ~/.zcode/memory/.

Hmm, but I should be careful: the user's AGENTS.md is their file; editing it requires care. The memory index table there lists content → location. Adding a line would modify their instructions file. The system prompt for my auto-memory says I should write memories to my own directory. The user's request "写入长期记忆" is ambiguous between the two, but given the established pattern (AGENTS.md index points to ~/.zcode/memory/*.md files, and output-preferences.md is already the "排版/配图/配色/动画" preferences file), the natural move might be to either:
- Add to ~/.zcode/memory/ as a new file and add an index row in AGENTS.md
- Or write into my auto-memory.

Actually, let me re-read the user's AGENTS.md: "## 产出偏好 - 做汇报/PPT、物理数学讲义或教学工具前，**必读 ~/.zcode/memory/output-preferences.md**（排版/配图/配色/动画等硬要求）。" — This covers PPT/讲义/教学工具. The new prompt is about 文档、报告、教程 language style (去 AI 味). This is complementary.

I think the cleanest approach respecting both systems:
1. Write the distilled prompt into my auto-memory directory as a `feedback` type memory (this is my persistent memory per system instructions).
2. ALSO, since the user's workflow relies on ~/.zcode/memory/ + AGENTS.md for "每会话生效", consider whether to add there.

Hmm wait. Actually, let me reconsider. The user's phrase "写入长期记忆" — in this environment, "长期记忆" most directly maps to my memory system (the auto-memory described in my system prompt: "You have a persistent file-based memory"). The user knows about this system (MEMORY.md index is shown in context). The user's own ~/.zcode/AGENTS.md is separately maintained — they curate it themselves, though in past sessions I may have helped.

Given the ambiguity, the safest and most useful: write to my auto-memory (primary), and mention to the user that if they want it to apply every session regardless of recall, we could also add a line in AGENTS.md pointing to a file — but actually per autonomous operation guidance, I shouldn't ask; I should decide. Hmm, but modifying the user's own AGENTS.md is a change to their instructions file — I'd rather do the auto-memory write (clearly sanctioned by the system prompt and the request), and optionally suggest the AGENTS.md hook-up as a follow-up.

Wait, but actually — there's a subtlety. The auto-memory is project-scoped: `projects/default-291edf811f114b36`. It says "persists across conversations" for this project (default workspace). The user works in this default workspace mostly. Fine.

But hmm, the user's history shows they keep curated memories in ~/.zcode/memory/ and I've created skills there too (paper-resume-writing at ~/.zcode/skills/). The paper-resume-writing skill already covers "简历去 AI 味" for resumes. Now they want a general document de-AI prompt. Should it be a skill? The user explicitly said "提示词...写入长期记忆" — a prompt into long-term memory, not a skill. OK.

Decision: Write to auto-memory directory. Type: feedback (guidance on how I should work). Also update MEMORY.md index.

Actually, let me reconsider once more whether to also update the user's ~/.zcode/AGENTS.md. The user's request: "现在请你参考以下这些建议或ai常见句式，总结一个精简但是有效的提示词并写入长期记忆。" — "写入长期记忆" = write into long-term memory. My system prompt's memory is exactly "a persistent file-based memory... MEMORY.md is the index loaded into context each session". So writing there satisfies "长期记忆" directly. The AGENTS.md route would make it apply every session unconditionally — but the user maintains that file's structure themselves and the AGENTS.md header says "用户长期记忆（每会话生效）". Hmm, that's literally called "用户长期记忆" too!

Ugh, both are "长期记忆". Let me think about which is more robust for the user's goal: they want AI-flavor-free documents in future tasks. 

- Auto-memory: MEMORY.md index loaded each session; individual files recalled by relevance. The index line would be visible each session. For writing tasks, the relevant memory would likely be recalled. But recall is not guaranteed.
- AGENTS.md: loaded fully every session. But it's the user's file; they listed an index table pointing to ~/.zcode/memory/ files. Adding a new memory file there + index row follows their established pattern (python-envs.md, office-doc-toolchain.md, etc. — these were clearly written by me or with me in past sessions, per the notes).

Given past sessions produced files in ~/.zcode/memory/ (per the AGENTS.md index, e.g. "office-doc-toolchain.md" also appears in my auto-memory MEMORY.md — interesting, both exist!). Looking at auto-memory MEMORY.md: "[Word/PDF 文档工具链本机环境](office-doc-toolchain.md)" — so the auto-memory has a file with the same name. And the user's AGENTS.md references ~/.zcode/memory/office-doc-toolchain.md. So both systems coexist; some content lives in both or the user copied.

Simplest robust solution that serves the user: 
1. Create the distilled prompt file in the user's ~/.zcode/memory/ (e.g. `de-ai-writing.md`) — because that's where their "每会话生效" output preferences live, and the user's request emphasizes they hate AI-flavored docs generally.
2. Add an index line to AGENTS.md under 产出偏好, mirroring the output-preferences.md pattern: e.g. "写文档/报告/教程/任何成文产出前，必读 ~/.zcode/memory/de-ai-writing.md（去 AI 味提示词）。"
3. Also save to my auto-memory per system instructions (type: feedback) so it's recalled even outside this workspace.

Hmm, is that overkill? The system prompt says: "Before saving, check for an existing file that already covers it — update that file rather than creating a duplicate". The paper-resume-writing skill covers 论文+简历 de-AI; this is 文档/报告/教程 — related but different scope. There's also output-preferences.md which I haven't read. Let me read it first — maybe the de-AI prompt belongs there? The AGENTS.md says output-preferences.md is about 排版/配图/配色/动画 (layout/images/colors/animation) — visual output. Language style is different, but it's the closest "产出偏好" file. Let me read it to check.

Also should read the paper-resume-writing skill to align/avoid contradiction and possibly cross-link.

Plan:
1. Read ~/.zcode/memory/output-preferences.md (required by AGENTS.md anyway when doing output-preference work, and to check overlap).
2. Read ~/.zcode/skills/paper-resume-writing/SKILL.md (to align and cross-reference).
3. Compose the distilled prompt (concise, effective) — in Chinese, since user writes Chinese docs.
4. Write to:
   - ~/.zcode/memory/de-ai-writing.md (user's curated memory) 
   - Edit AGENTS.md index to add a row/line.
   - Auto-memory file + MEMORY.md line (my persistent memory, type: feedback).

Wait — "重大流程修改（skill/脚本/自动化/生成流程）先出方案 → 确认 → 执行。" — Is this a major process change? It's adding a memory file + one line in AGENTS.md. The user explicitly asked to "写入长期记忆" — that's direct instruction, so execution is authorized. Editing AGENTS.md itself though... the user asked to write into long-term memory; AGENTS.md is arguably part of that. I think adding to AGENTS.md is within scope since that's their "每会话生效" mechanism. But to be careful, I could put the file in ~/.zcode/memory/ and add the 必读 line in AGENTS.md under 产出偏好 — following the exact existing pattern. That's not a "流程修改" (no skill/script/automation change), just a memory addition. Proceed.

Actually hold on, let me reconsider scope again. The instruction "重大流程修改（skill/脚本/自动化/生成流程）先出方案 → 确认 → 执行" — writing a prompt into memory is not a process modification. Direct execution is fine.

Now, the core intellectual work: distill the advice into a concise but effective prompt. Let me analyze.

User's AI-flavor blacklist (句式):
说实话…、A的本质是B、不是…而是…、先…再…、让我们…、如果…就…、只有…、意味着…、唯一…、无论…都…、要么…要么…、我的建议是…、记住…、就算…也…、全文、一句话、之所以…是因为…、说白了…

Hmm, some of these are over-broad as absolute bans ("如果…就…", "先…再…", "只有…" are normal Chinese constructions — banning them outright would damage natural writing). The image's philosophy is "句子服从意思" — sentences serve meaning. So the prompt should treat the blacklist as "high-risk patterns: don't use habitually/mechanically; each use must earn its place" — or group them. Actually the user explicitly wants these avoided; but a good prompt should be effective, not harmful. Let me think.

The image key points:
1. 对自己判断负责的作者；不讨好、不面面俱到、不自动平衡；写作=选择（什么值得说/省略）。
2. 动笔前想清楚：这段回答什么问题、我的判断、凭什么。无依据处不用抽象概念/套话/修辞掩盖。每段一个主要任务，段落靠问题/判断/证据推进，不为形式完整机械安排结构。
3. 正面立论：直接陈述判断再给依据；不预设反对者、不人为构造对立；禁"不是…而是…"；竞争性解释只在真正影响判断时讨论；边界来自理论和证据，不习惯性用"可能""一定程度上""值得注意"。
4. 每句话增加新信息；删掉后读者理解不变的句子删掉；优先具体事实/数据/机制/行为/案例/可观察现象；不补无关背景、不换说法重复；判断提出后，后文给证据/机制/推论/边界。
5. 成熟作者的自然语言：句子服从意思不追求整齐；长短/段落结构可变；少用"值得注意的是""需要指出的是""从某种意义上说"起手式；不机械用"首先/其次/最后""一方面/另一方面"；不制造空洞比喻/排比/转折/拔高；段落论证完直接结束，不补总结句。
6. 不给自己的判断反复加保险：有依据用正常陈述句；证据有限就准确说边界；区分证据限制与不自信；不提前回应未出现的质疑；替代解释在需要处集中讨论。

Now distill. The user wants "精简但是有效" (concise but effective). Target maybe 300-500 chars? The paper-resume-writing skill is 558 chars with a ≤600 constraint. For a memory file, I can afford a bit more, but the prompt itself should be tight since it'll be injected into future writing contexts.

Let me think about the structure of the distilled prompt. It should be phrased as instructions to the writer (me/agent) for 文档/报告/教程.

Key failure modes of AI Chinese writing (combining user's list + image):
1. 空洞判断句: "A的本质是B"、"X意味着Y"、"X是关键/核心/唯一" — grand-sounding claims without evidence.
2. 对立框架: "不是A而是B"、"要么A要么B"、"无论…都…" — manufactured tension/false dichotomy.
3. 口语化填充/说教腔: "说实话"、"说白了"、"一句话"、"记住"、"让我们"、"我的建议是" — conversational filler, preachy.
4. 条件式说教: "如果…就…"、"只有…才…"、"就算…也…" — prescriptive conditional chains that pad tutorials.
5. 顺序模板: "先…再…"、"首先/其次/最后"、"一方面/另一方面" — mechanical scaffolding.
6. 元话语: "全文"、"本文将"、"总之"、"如上所述" — talking about the text instead of the subject.
7. 归因模板: "之所以…是因为…" — mechanical causality framing.
8. Hedging: "可能"、"一定程度上"、"值得注意的是" — insurance language.
9. Deeper principles: 每句有新信息；具体事实/数据/机制优先；删掉不影响理解的句子删；直接陈述判断再给依据；段落论证完直接结束；句子长短服从意思。

Now how to phrase the prompt concisely. Draft:

---
写文档/报告/教程时，像对判断负责的作者那样写，不像助手那样堆话：

**立论**：先想清楚这段回答什么问题、我的判断、凭什么。直接陈述判断再给依据；证据不足处不用抽象概念和套话掩盖。不预设反对者，不人为制造对立。少用"可能/一定程度上/值得注意"给自己上保险；证据有限就准确说边界。

**信息密度**：每句话都要让读者多知道一件事。删掉后理解不变的句子一律删。优先写具体事实、数据、机制、步骤结果；不补无关背景，不换说法重复，段落论证完直接结束，不补总结拔高句。

**句式禁令**：不用"说实话/说白了/一句话/记住/让我们/我的建议是"这类口播腔；不用"A的本质是B/X意味着Y"这类空判断；不用"不是…而是…/要么…要么…/无论…都…"制造张力；不用"之所以…是因为…"套壳归因；"首先/其次/一方面"和"先…再…"只在真实步骤时用。句子长短和段落形状服从内容，不为整齐对仗。
---

Hmm, that's pretty good. Let me count roughly... ~380 chars. 

But wait — I should double check the blacklist handling. The user listed: 说实话…、A的本质是B、不是…而是…、先…再…、让我们…、如果…就…、只有…、意味着…、唯一…、无论…都…、要么…要么…、我的建议是…、记住…、就算…也…、全文、一句话、之所以…是因为…、说白了…

I covered: 说实话✓、说白了✓、一句话✓、记住✓、让我们✓、我的建议是✓、A的本质是B✓、意味着✓、不是…而是…✓、要么…要么…✓、无论…都✓、之所以…是因为✓、先…再✓、首先/其次（related）✓. Missing: 如果…就…、只有…、唯一…、就算…也…、全文.

"如果…就…"、"只有…才"、"就算…也" — these are conditional constructions; in tutorials they're sometimes legitimate (real conditionals). The AI-flavor usage is: using them for emphasis/padding ("如果只有一行代码，就不需要抽象类" style... actually that's fine). The AI-ish usage is more like "如果你想…，就需要…" (the classic "如果...那么..." hedged instruction). And "唯一" — "唯一的区别是…" is actually informative sometimes; AI uses "X是唯一的Y" for grandiosity. Hmm.

Let me add a line: "'如果…就/只有…才/就算…也'这类条件句只写真条件，不用来强调和铺垫" and "'全文/本文'这类元话语少说，直接讲内容".

Actually, let me reconsider — maybe organize the blacklist by function rather than listing every pattern, since a prompt that's a giant blacklist is less effective than one organized by *why* the pattern is bad + what to do instead. The image's philosophy is exactly that: positive principles + targeted bans. Effective prompt design: give the model the underlying taste, plus the most-triggered specific bans.

The user's request: "参考以下这些建议或ai常见句式，总结一个精简但是有效的提示词" — reference both the advice (image) and the AI patterns (list). So the prompt should include both: principles (from image) and pattern bans (from list).

One more consideration: the "no-overdefense" spirit — keep the prompt lean. And there's the existing paper-resume-writing skill — I should cross-link in memory ("related: [[paper-resume-writing-skill]]" in auto-memory; and in the user-facing file mention it complements the skill for papers/resumes).

Now, where exactly to write:

1. Auto-memory: `C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory\de-ai-writing-prompt.md` with frontmatter type: feedback, then add line to MEMORY.md.

2. User memory: `C:\Users\UserX\.zcode\memory\de-ai-writing.md` + AGENTS.md line.

Hmm, wait. Should I really do both? Duplication risk: two copies drift. But precedent shows both systems coexist (office-doc-toolchain in both). The user's explicit "每会话生效" mechanism is AGENTS.md; my system's mechanism is auto-memory. The user said "写入长期记忆" — they probably mean "so that it sticks across sessions". The most user-visible, user-controlled place is ~/.zcode/memory/ + AGENTS.md. My auto-memory is for me.

Let me look at what's in ~/.zcode/memory/ first and read output-preferences.md (mandatory read per AGENTS.md for output preference work, and it may already contain language-style items to avoid duplication). Also read paper-resume-writing SKILL.md to avoid contradiction.

Actually — do I need to read output-preferences.md? AGENTS.md says 必读 before 做汇报/PPT/讲义/教学工具 — this task is writing a prompt, not producing those outputs. But checking it for overlap is prudent. It's cheap. Yes, read it.

Also, the image — I can read it directly (it's cached at a path). I already have its content transcribed in the conversation? Actually no — the image was shown to me as an attachment. Let me check: the user message includes "[Image: source: ...image-3ab807b07ce5afc7fdeb59c1d8621693.png]" — as a multimodal input I should be able to see it. Hmm, in this text-only rendering I described it above from... Actually I generated that transcription in my thinking — wait, can I actually see the image? The user message contains an image attachment. In ZCode, images in user messages are visible to me. The content I described — I should verify by actually reading the image file to make sure my transcription is accurate, since my thinking block's "transcription" needs to come from actually seeing the image. Since the image is attached to the user message, I have seen it. But to be careful and accurate (the user's instruction: 禁编造), let me re-read the image file with the Read tool to make sure I capture all details correctly before distilling. That's a legitimate use.

Wait, the user message shows the image was included. If I can see it, great. The transcript above in my thinking is my reading of it. To be safe, I'll Read the image file once to confirm details. Actually — the Read tool supports images. The path: C:\Users\UserX\.zcode\cli\image-cache\sess_22db4c09-fb98-42bd-8d4a-b2ce8d3fc07a\image-3ab807b07ce5afc7fdeb59c1d8621693.png. Reading it costs little and prevents misquoting. Do it.

Plan of tool calls:
1. Read image (confirm content) — parallel with:
2. Read ~/.zcode/memory/output-preferences.md
3. Read ~/.zcode/skills/paper-resume-writing/SKILL.md
4. List ~/.zcode/memory/ to see existing files (avoid duplicate file names).

Then compose, write files, edit AGENTS.md, update MEMORY.md, report.

Let me also double-check: is there an existing memory in my auto-memory dir about writing style? MEMORY.md index shows: paper-resume-writing-skill, vi-lab-explanation-style (教材类讲解偏好 — course content for 小白). The vi-lab-explanation-style is about teaching style (补前置概念、参数讲为什么、给走查数字与排错表) — that's about content depth, not language flavor. Complementary, no conflict.

Now let me draft the final prompt carefully. It needs to be 精简 (lean) but 有效 (effective). Effectiveness for an LLM prompt: concrete bans + positive direction + a few examples. Avoid making it so long it gets ignored.

Draft v2 (the actual prompt content, to be stored):

# 去 AI 味写作提示词（文档/报告/教程通用）

写任何成文产出（文档、报告、教程、讲义）时按此执行：

**像作者，不像助手。** 动笔前想清楚三件事：这段回答什么问题、我的判断是什么、凭什么。判断直接说出来，再给依据；依据不足的地方不用套话和修辞掩盖。不预设反对者，不为张力制造对立。

**每句话都要有信息增量。** 删掉后读者的理解不变，这句就删。优先写具体事实、数据、机制、操作和结果，不写与论证无关的背景，不换说法重复已说清的判断。段落论证完直接结束，不加总结句、不拔高。

**句子服从意思。** 长短句自然变化，不追求排比工整；不用空比喻和空洞升华。不给自己反复上保险：少用"可能""一定程度上""值得注意"；证据只够有限结论时，准确说边界即可，不提前回应没出现的质疑。

**句式黑名单（出现即改写）：**
- 口播腔：说实话 / 说白了 / 一句话 / 记住 / 让我们 / 我的建议是 / 全文（元话语）
- 空判断：A 的本质是 B / X 意味着 Y / X 是唯一… / 之所以…是因为…
- 假对立：不是…而是… / 要么…要么… / 无论…都… / 就算…也…
- 模板化：首先其次最后 / 一方面另一方面 / 先…再…（只用于真实操作步骤）/ 如果…就…、只有…才（只用于真实条件）

改写方向：把句式拆掉，直接写要表达的那个判断。

Hmm, length ~450 chars. Good. Let me refine wording.

Actually, about "先…再…" — in tutorials, "先做A再做B" is often genuinely procedural. The user listed it as AI-flavor though. I'll keep "只用于真实步骤" qualifier — effective, not blanket-harmful. Same for 如果/只有. This matches "有效" — a blanket ban on 条件句 would wreck tutorial writing. I'll note this in my final message so the user understands the design choice.

Wait, but the user explicitly listed them as "ai味很浓的常见句式". They want them gone. The qualifier approach still honors that: the AI-flavor usage is when they're used as rhetorical padding. I'll keep qualifiers but make the default "avoid". Let me phrase: "先…再…/如果…就/只有…才/就算…也：只在真实步骤或真实条件用，不用来铺垫强调".

Hmm "就算…也" — "就算报错也不要慌" — that's preachy padding in docs. Real concessive usage is rare in docs. Fine under the same rule.

Also "一句话" — as in "一句话总结：" — filler. ✓.

Now the storage format.

For auto-memory file (my system's format):

```markdown
---
name: de-ai-writing-prompt
description: 用户痛恨AI味文风；去AI味写作提示词（文档/报告/教程通用），写成文产出前执行
metadata:
  type: feedback
---

用户明确表示 AI 写的文档/报告/教程"语言结构和句子就是一坨屎"，要求所有成文产出执行以下提示词（2026-10-05 沉淀，源自用户提供的写作建议+AI句式黑名单）：

<the prompt>

**Why:** ...
**How to apply:** ...
```

Wait the frontmatter format for feedback: "for feedback/project, follow with **Why:** and **How to apply:** lines". The prompt itself is the content; Why/How to apply explain. Let me structure: the memory body = the fact (user hates AI flavor + the distilled prompt), then Why and How to apply.

Hmm, actually for a feedback memory, the "fact" IS the guidance. I'll write: the user's stance (one line), then the prompt in a code block or as body text so it's copy-pasteable, then Why/How.

Should the prompt be in a code block? For memory recall purposes, plain text is fine; a code block makes the boundary clear. I'll use a fenced block maybe. Or just structured markdown. Keep it simple — structured markdown with bold headers works and renders in recall.

For the user's ~/.zcode/memory/de-ai-writing.md: user-facing file, clean markdown, the prompt + one line provenance. 

For AGENTS.md edit: under "## 产出偏好", add a bullet:
"- 写文档/报告/教程/任何成文产出前，**必读 ~/.zcode/memory/de-ai-writing.md**（去 AI 味写作提示词，句式黑名单）。"

Need to Read AGENTS.md first (I have its content in context from system reminder, but Edit requires Read in conversation). Yes, must Read the file first.

Also check ~/.zcode/memory/ directory listing to confirm de-ai-writing.md doesn't exist.

Let me also reconsider the name. User's files: output-preferences.md, python-envs.md, office-doc-toolchain.md, ppt-master-project.md, teaching-workspace.md, verification-notes.md. English kebab names. "de-ai-writing.md" fits. Good.

Now let me also think: should the prompt mention "不使用 emoji" or markdown structure rules? The image doesn't cover that; user didn't ask. Keep scope: language structure & sentences. Don't bloat. Actually the user's complaint: "在语言结构和句子上" — language structure and sentences. So focus there. Good, my draft does.

One more element from the image worth keeping: "每一段承担一个主要任务，段落之间依靠问题、判断和证据自然推进，不要为了形式完整机械安排结构" — paragraph-level structure. My draft has paragraph-end rule but not the "每段一个任务" bit. Add compactly: "每段只讲一件事，段落靠问题和判断推进，不为形式完整硬凑结构。" — worth one line since user complained about "语言结构".

Also from image: "写作意味着做出选择：什么值得说，什么可以省略" — the selection principle. Covered implicitly by 信息增量. OK.

Also: "优先使用具体事实、数据、机制、行为、案例和可观察现象" ✓.

Let me finalize the prompt text:

---
写文档、报告、教程等成文内容时，按以下规则执行。

**立论方式**：动笔前想清楚这段回答什么问题、我的判断是什么、凭什么。判断直接陈述，再给依据；依据不足的地方不用抽象概念和套话掩盖。不预设不存在的反对者，不为制造张力人为构造对立。证据只够有限结论时准确说边界，不用"可能""一定程度上"反复加保险，不提前回应未出现的质疑。

**信息密度**：每句话都要带来新信息——删掉后读者理解不变的句子一律删掉。优先写具体事实、数据、机制、操作和结果，不补与论证无关的背景，不换说法重复已说清的内容。每段只承担一个任务，论证完直接结束，不补总结句、不拔高意义。

**语言**：句子长短服从意思，不追求排比工整，不造空比喻。段落结构自然变化，不用模板化骨架。

**句式黑名单（出现即重写，把句式拆掉直接写判断）**：
1. 口播/说教腔：说实话、说白了、一句话、记住、让我们、我的建议是；
2. 元话语：全文、本文、值得一提的是；
3. 空判断：A 的本质是 B、X 意味着 Y、唯一、之所以…是因为…；
4. 假对立/假让步：不是…而是…、要么…要么…、无论…都…、就算…也…；
5. 模板骨架：首先/其次/最后、一方面/另一方面；先…再…、如果…就…、只有…才——后三个只在真实操作步骤或真实条件分支使用，不用于铺垫和强调。
---

Hmm wait, "值得一提的是" wasn't in the user list but is in the image ("值得注意"). The image bans "值得注意的是""需要指出的是""从某种意义上说" as 起手式. I merged as 元话语. Fine — but keep it tight. Actually let me fold "值得注意的是/需要指出的是" into 元话语 category. And drop "本文" — "全文" was user's; "本文将介绍" is the same family. Keep both, one word each.

Length check: this is ~500 chars. Acceptable for a "精简" prompt? The user said 精简但有效. I could trim further. Let me see what to cut. 

Actually I think structuring as: 3 principles (each 1-2 sentences) + blacklist (5 compact categories) is the right size. ~450-500 Chinese chars is genuinely lean for covering this much. The image is ~1200 chars. We compressed 3x while keeping all operational content.

Could trim: "**语言**" section is thin — merge into 信息密度 or keep as one line. Keep one line; it carries "长短服从意思/不排比/不空比喻".

Final check on wording precision:
- "把句式拆掉直接写判断" — from image: 不要使用"不是…而是…"的句式，直接写你真正想表达的判断. ✓ good actionable advice.
- "唯一" as bare word is odd in blacklist; phrase as "『唯一』式断言（X 是唯一的 Y）". Hmm, keep simple: "唯一…（绝对化断言）". Let me write "空判断/绝对化：A 的本质是 B、X 意味着 Y、X 是唯一…、之所以…是因为…".

- 就算…也 — put in 假对立/假让步: "不是…而是…、要么…要么…、无论…都…、就算…也…" ✓.

Also should I include "少用设问自问自答"? Not in source material. Skip — 禁编造, stick to given material.

Provenance: The prompt distills (a) user's pattern list, (b) the screenshot's writing advice, (c) my grouping. In the memory files I'll note source briefly.

Now also: update auto-memory MEMORY.md index with one line: "- [去AI味写作提示词](de-ai-writing-prompt.md) — 文档/报告/教程成文前执行：立论三问+信息增量+句式黑名单".

And link from the new auto-memory to related: [[paper-resume-writing-skill]] (skill for papers/resumes) and [[vi-lab-explanation-style]] (teaching style). The skill itself — should I update paper-resume-writing SKILL.md to reference it? The user said the skill is ≤600 chars constraint. Don't touch the skill — user asked only for memory. Mention cross-ref in memory text only.

Also the user-facing file ~/.zcode/memory/de-ai-writing.md could mention "论文/简历另有 paper-resume-writing skill，本文件管其余成文产出" — helpful routing note. Good.

Execution order:
1. Read image (verify content). [parallel]
2. Read AGENTS.md, output-preferences.md, paper-resume-writing SKILL.md; list ~/.zcode/memory/. [parallel]
3. Write ~/.zcode/memory/de-ai-writing.md
4. Edit AGENTS.md (add 产出偏好 bullet)
5. Write auto-memory file + Edit MEMORY.md
6. Final report.

Actually wait — one consideration on AGENTS.md edit. The AGENTS.md content shown in system reminder is at C:\Users\UserX\.zcode\AGENTS.md. I need to Read it before Edit. The 产出偏好 section currently has one bullet. I'll add mine after it.

Bullet text: "- 写任何文档/报告/教程/说明文前，**必读 ~/.zcode/memory/de-ai-writing.md**（去 AI 味提示词：立论、信息增量、句式黑名单）。论文/简历仍走 paper-resume-writing skill。"

Hmm, keep it short like existing style. Existing: "- 做汇报/PPT、物理数学讲义或教学工具前，**必读 ~/.zcode/memory/output-preferences.md**（排版/配图/配色/动画等硬要求）。"

Mine: "- 写文档/报告/教程等成文内容前，**必读 ~/.zcode/memory/de-ai-writing.md**（去 AI 味：句式黑名单+立论规则；论文简历另有 skill）。"

Good.

Now, do I show the user the prompt in my final message? Yes — absolutely, they need to review it. Final message: the prompt itself (concise), where it was saved (3 places), and the one design decision (conditional patterns get "real-condition-only" qualifier instead of blanket ban, so tutorials stay writable). Also mention核实建议? Not needed here — no external facts. 

Let me also double check the image reading. I'll read it now. Actually, since the image is already attached to the user message, I have seen it — my transcription above came from that. But let me still re-read to be safe? Hmm. If I can see it, re-reading wastes a call but is cheap insurance for exact wording. Actually, I genuinely cannot be 100% sure my perception was complete (there was a text-selection popup covering part of line 3: "值得..." got cut by the "要求更改 Ctrl+K" popup). Reading the file again won't reveal the covered text either (same image). So re-reading adds nothing — the popup occlusion is in the image itself. Skip the re-read? 

Hmm, wait — do I actually have vision of it? The user message includes the image attachment, which in ZCode gets passed to me as an image block. My thinking contains a detailed transcription, which suggests I did see it. I'll trust it but let me do one quick Read of the image file to double-check the occluded parts and exact phrases — cheap and prevents misattribution. Actually you know, the Read tool renders the image to me again — same occlusion. No new info. Skip it. I have enough: the visible content is sufficient and I noted where text was occluded ("值得…" cut off — clearly "值得注意" family).

Hmm, but one risk: if my transcription is a hallucination... Let me just do the Read. It's one cheap call, run in parallel with the other reads. If it matches my memory, proceed confidently. OK include it.

File path for image: C:\Users\UserX\.zcode\cli\image-cache\sess_22db4c09-fb98-42bd-8d4a-b2ce8d3fc07a\image-3ab807b07ce5afc7fdeb59c1d8621693.png

Parallel batch 1:
- Read image
- Read C:\Users\UserX\.zcode\AGENTS.md
- Read C:\Users\UserX\.zcode\memory\output-preferences.md
- Read C:\Users\UserX\.zcode\skills\paper-resume-writing\SKILL.md
- Bash: ls ~/.zcode/memory/

Then writes.

For the Bash ls: use `ls "C:\Users\UserX\.zcode\memory"` — in Git Bash, path C:/Users/UserX/.zcode/memory. Fine.

Let me now also prepare: what if output-preferences.md already contains language-style rules? Then I'd merge/reference instead of duplicating. I'll adapt after reading.

One more thought on the auto-memory file name: de-ai-writing-prompt.md. Description: "用户反感AI味文风；写文档/报告/教程前执行的去AI味提示词". Type: feedback. Body: the stance + prompt + Why/How.

Actually, hmm, do both copies need to exist? Risk of drift: if user later edits ~/.zcode/memory/de-ai-writing.md, my auto-memory copy goes stale. Mitigation: in my auto-memory, point to the canonical file (~/.zcode/memory/de-ai-writing.md) and note "canonical there". But then recall depends on that file being readable — it is, same machine. Actually simpler: my auto-memory holds the full prompt (self-contained, since that's what memory is for), and notes the user-side copy path. If user edits theirs, next session's recall of mine could conflict — acceptable; I'll note "if user edits, update this too". Eh, keep it simple: full prompt in auto-memory, one line noting the canonical copy lives at ~/.zcode/memory/de-ai-writing.md (user-maintained). 

Wait, actually — is double-writing overengineering? Let me weigh: The user's request "写入长期记忆". Their AGENTS.md index table maps content → ~/.zcode/memory files. From the user's perspective, "长期记忆" likely = their ~/.zcode/memory system (they built it, they reference it in AGENTS.md as 用户长期记忆). My auto-memory is a system-level feature they may not think about. Writing only to auto-memory risks the user not finding it where they expect. Writing only to their memory leaves my recall thinner. Both is safest and cheap. Precedent exists (office-doc-toolchain in both). Go with both + AGENTS.md line.

Alright, also the memory note at top of my system prompt: "This directory already exists — write to it directly with the Write tool (do not run mkdir or check for its existence)". For ~/.zcode/memory/, it exists too (files referenced). Write directly.

Now compose final prompt text (canonical version, user-facing):

```markdown
# 去 AI 味写作提示词（文档 / 报告 / 教程通用）

> 来源：用户提供的写作建议截图 + AI 高频句式清单，2026-10-05 沉淀。
> 论文（Introduction 七步法）与简历的去 AI 味另见 skill：paper-resume-writing。

写任何成文内容（文档、报告、教程、讲义、README）时执行：

## 三条原则

1. **像对判断负责的作者，不像讨好读者的助手。** 动笔前想清楚：这段回答什么问题、我的判断是什么、凭什么这样判断。判断直接说出来，再给依据；依据不足的地方，不用抽象概念、套话和修辞掩盖。不预设不存在的反对者，不为制造张力人为构造对立。

2. **每句话都要有信息增量。** 删掉一句话后读者的理解不变，这句话就删。优先写具体事实、数据、机制、操作步骤和可观察结果；不补与当前论证无关的背景，不换一种说法重复已说清的判断。每段只承担一个主要任务，论证完直接结束——不补总结句，不拔高意义。

3. **句子服从意思，不追求整齐。** 长短句自然变化，段落结构允许不匀；不造空洞的比喻、排比和升华。不反复给自己的判断上保险：少用"可能""一定程度上""值得注意"；证据只够有限结论时，准确说出边界即可，不提前回应还没出现的质疑。

## 句式黑名单（出现即重写）

重写方法：把句式拆掉，直接写出真正想表达的那个判断。

| 类型 | 句式 |
|---|---|
| 口播说教腔 | 说实话… / 说白了… / 一句话… / 记住… / 让我们… / 我的建议是… |
| 元话语 | 全文 / 本文将 / 值得注意的是 / 需要指出的是 / 从某种意义上说 |
| 空判断·绝对化 | A 的本质是 B / X 意味着 Y / X 是唯一… / 之所以…是因为… |
| 假对立·假让步 | 不是…而是… / 要么…要么… / 无论…都… / 就算…也… |
| 模板骨架 | 首先其次最后 / 一方面另一方面；先…再…、如果…就…、只有…才 —— 仅限真实操作步骤或真实条件分支，不用于铺垫强调 |
```

That's the canonical. ~550 chars body. Good.

Hmm — one refinement on #3's blacklist mention: "可能" — wait, "可能" is a normal word; the image says 不习惯性使用"可能""一定程度上". My principle 3 covers it. Fine.

Also should the title say 提示词 or 规则? User asked for 提示词. Keep.

Table vs list in user file — table is compact, fine. But for MY auto-memory, tables render fine too. However, for prompt-injection effectiveness (when recalled into a future session), a table is compact and readable. Keep table in both.

Auto-memory version: add frontmatter + Why/How to apply + link [[paper-resume-writing-skill]] and [[vi-lab-explanation-style]].

Why: 用户对 AI 味句式强烈反感（"语言结构和句子就是一坨屎"）；默认生成的文档普遍带这些模式，必须在成文产出前主动规避。
How to apply: 写/改任何成文产出（文档、报告、教程、讲义、README）前先按此自检；成文后可用黑名单逐条 grep 复查。论文/简历场景叠加 [[paper-resume-writing-skill]]；教学讲义同时满足 [[vi-lab-explanation-style]]（内容上）与本规则（语言上）。

Good. Also add "canonical copy: ~/.zcode/memory/de-ai-writing.md（用户侧，AGENTS.md 索引指向它）".

MEMORY.md line: "- [去 AI 味写作提示词](de-ai-writing-prompt.md) — 文档/报告/教程成文前必执行：判断先行+信息增量+句式黑名单；用户对 AI 味文风强烈反感"

Now AGENTS.md bullet — insert after the output-preferences bullet:

"- 写文档/报告/教程等成文内容前，**必读 `~/.zcode/memory/de-ai-writing.md`**（去 AI 味提示词：三条原则+句式黑名单）。"

Match style of existing bullets (they use **必读 ~/.zcode/memory/...** without backticks actually: "**必读 ~/.zcode/memory/output-preferences.md**（排版/配图/配色/动画等硬要求）"). Mirror exactly: "- 写文档/报告/教程等成文内容前，**必读 ~/.zcode/memory/de-ai-writing.md**（去 AI 味：判断先行、信息增量、句式黑名单）。"

OK. Let me also double-check there's no existing de-ai file in ~/.zcode/memory — will confirm via ls.

Also: the user's instruction "有答案文件禁提前偷看" — not relevant. "重大流程修改先出方案" — this is a memory write, explicitly requested; proceed. Though — editing AGENTS.md... The AGENTS.md IS the user's instruction file; adding one bullet following their established pattern is the mechanism by which "每会话生效" works. The user asked to "写入长期记忆" — I interpret AGENTS.md edit as authorized and necessary for the memory to actually fire every session. I'll report it clearly so they can revert if they disagree.

Alright, execute. First parallel reads.

Then writes. Then final message with the prompt shown in full (user must be able to review it), plus locations + the one design decision explained (条件句不是一刀切，避免教程写不了；一刀切的代价说明), plus note that they can tune.

Actually one more thing — final message language: Chinese (user writes Chinese). Yes.

Let me write out everything now. First the parallel reads.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\cli\\image-cache\\sess_22db4c09-fb98-42bd-8d4a-b2ce8d3fc07a\\image-3ab807b07ce5afc7fdeb59c1d8621693.png"}` → `[Attached image/jpeg: Read image]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\AGENTS.md"}` → `1 # 用户长期记忆（每会话生效） 2 3 ## 工作风格 4 - 简单任务直接做，截图/测试快速验证闭环。 5 - 错误报告须含根因 + 可验证改进建议，基于实际对比数据，禁编造。 6 - 有答案文件禁提前偷看：先独立完成再对比。 7 - 重大流程修改（skill/脚本/自动化/生成流程）先出方案 → 确认 → 执行。 8 - 可能虚构文献/外部事实 → 提醒用户核实。 9 10 ## 产出偏好 11 - 做汇报/PPT、物理数学讲义或教学工具前，**必读 `~/.zcode/memory/output-preferences.md`**（排版/配图/配色/动画等硬要求）。 12 13 ## 本机环境要点（UserX / Wind …[截断,原长1243]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\memory\\output-preferences.md"}` → `1 # 产出偏好（详细）— 汇报/PPT、教学内容 2 3 > 由 `~/.zcode/AGENTS.md` 索引。**做汇报/PPT、物理数学讲义或教学工具前必读本文件。** 4 5 > **2026-09-29 更新**：PPT 出现新的已验收默认风格——**浅色纸感编辑风**（暖纸底 #FAF6EE + 墨字 + 霞鹜文楷 + 装帧双线框/回纹角花/印章 + 三语义色 + 页底阶段轨），用户全片验收通过。其完整规约与可复用 spec_lock 契约见 `~/.zcode/skills/ppt-master/projects/ai_agent_evolution_ppt169_20260928/spec_lock.md`。本节下 …[截断,原长2874]`

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\skills\\paper-resume-writing\\SKILL.md"}` → `1 --- 2 name: paper-resume-writing 3 description: 写或改论文（尤其 Introduction/引言）与简历时必读：论文七步法防 AI 跳跃写作，简历去 AI 味。触发词：论文、Introduction、引言、研究背景、简历、求职、润色、AI 味、改简历。 4 --- 5 6 # 论文与简历写作 7 8 ## 论文 Introduction：七步法（general→specific） 9 让 AI 按步逐级写，人工补步骤间衔接——AI 惯用 bullet 思考，最易丢过渡： 10 1 领域背景：用读者熟悉的内容确立话题 11 2 研究现状：先承认前人工作，建立可信度 12 3 gap： …[截断,原长609]`

- 🔧 **Bash** `{"command": "ls \"C:/Users/UserX/.zcode/memory/\"", "description": "List existing memory files in user's memory directory"}` → `README.md office-doc-toolchain.md output-preferences.md ppt-master-project.md python-envs.md teaching-workspace.md verification-notes.md`

### 🤖 助手（GLM-5.3-Flash，2026-10-05 13:28）

我先把截图、你的 AGENTS.md、已有的 output-preferences 和论文/简历去 AI 味 skill 都读一遍，确认没有重复或冲突，再动笔总结。

<details><summary>💭 思考链（GLM-5.3-Flash）</summary>

Confirmed:
1. Image content matches my transcription. Good.
2. AGENTS.md structure confirmed — 产出偏好 section at line 10-11.
3. output-preferences.md is visual/layout (排版/配图/配色/动画) — no language-style overlap. One related line: "简洁不 AI、不过度口语化" in 教学内容 — consistent with my prompt, no conflict.
4. paper-resume-writing skill covers papers/resumes — my new prompt is for 文档/报告/教程 general writing. Complementary. I'll cross-reference.
5. ~/.zcode/memory/ has no de-ai file yet. Create de-ai-writing.md.

Now write:
1. ~/.zcode/memory/de-ai-writing.md (canonical, user-facing)
2. Edit AGENTS.md — add bullet under 产出偏好
3. Auto-memory file + MEMORY.md line

Let me finalize the prompt text. From the image, key content I should distill (verified against image now):

Para 1: 对自己判断负责的作者；形成清楚的判断并用必要的信息讲清楚；不扮演讨好读者、面面俱到、自动平衡所有观点的助手；写作=选择：什么值得说、什么可省略、什么证据足以支持判断、什么只是填充。

Para 2: 动笔前三个问题：这段回答什么问题、我的判断是什么、凭什么这样判断。依据不足不用抽象概念、套话、修辞掩盖。每段承担一个主要任务，段落靠问题/判断/证据推进，不为形式完整机械安排结构。

Para 3: 正面立论：确定判断后直接陈述再给依据。不预设不存在的反对者，不为制造张力人为构造对立。不用"不是……而是……"句式，直接写真正想表达的判断。竞争性解释、理论边界只在真正影响当前判断时讨论。边界来自理论和证据，不习惯性用"可能""一定程度上""值得…"（被弹窗遮挡，应为"值得注意"类）。

Para 4: 每句话都应增加新信息；删掉后理解不变就没必要存在。优先具体事实、数据、机制、行为、案例、可观察现象。不为显得完整补无关背景，不换说法重复。判断提出后，后面继续给证据、机制、推论或边界。

Para 5: 成熟作者自然语言。句子服从意思不追求整齐；长短可变、段落结构可变。少用"值得注意的是""需要指出的是""从某种意义上说"起手式。不机械用"首先、其次、最后""一方面、另一方面"模板。不为显得深刻制造空洞比喻、排比、转折、拔高。段落论证完直接结束，不补总结意义。

Para 6: 不反复加保险。有充分依据用正常陈述句承担判断；证据只能支持有限结论时准确说明边界。区分真正的证据限制和作者对判断的不自信。不提前回应尚未出现的质疑，不把大量防御性表述塞进正文。真正重要的替代解释在需要处理的位置集中讨论。

Plus user's blacklist: 说实话…、A的本质是B、不是…而是…、先…再…、让我们…、如果…就…、只有…、意味着…、唯一…、无论…都…、要么…要么…、我的建议是…、记住…、就算…也…、全文、一句话、之所以…是因为…、说白了…

Now final canonical file content. I drafted it already; refine:

# 去 AI 味写作提示词（文档 / 报告 / 教程通用）

> 来源：用户提供的写作建议截图 + AI 高频句式清单，2026-10-05 沉淀。
> 适用范围：文档、报告、教程、讲义、README 等成文产出。论文/简历另有 `paper-resume-writing` skill，两者叠加使用。

## 三条原则

1. **像对判断负责的作者，不像讨好读者的助手。** 写作是选择：什么值得说、什么可以省略、什么证据足以支持判断。动笔前想清楚三件事——这段回答什么问题、我的判断是什么、凭什么这样判断。判断直接说出来，再给依据；依据不足的地方不用抽象概念、套话和修辞掩盖。不预设不存在的反对者，不为制造张力人为构造对立。

2. **每句话都要有信息增量。** 删掉一句话后读者的理解不变，这句话就删。优先写具体事实、数据、机制、操作步骤、案例和可观察结果；不补与当前论证无关的背景，不换一种说法重复已说清的判断。每段只承担一个主要任务，段落靠问题和判断自然推进；论证完直接结束——不补总结句、不拔高意义。

3. **句子服从意思，不追求整齐。** 长短句自然变化，段落结构允许不匀，不造空洞的比喻、排比、转折和升华。不反复给自己的判断上保险：不用"可能""一定程度上"等习惯性弱化；证据只够有限结论时，准确说出边界即可；不提前回应还没出现的质疑，防御性表述不进正文。

## 句式黑名单（出现即重写）

重写方法：把句式拆掉，直接写出真正想表达的那个判断。

| 类型 | 句式 |
|---|---|
| 口播说教腔 | 说实话… / 说白了… / 一句话… / 记住… / 让我们… / 我的建议是… |
| 元话语 | 全文 / 本文将 / 值得注意的是 / 需要指出的是 / 从某种意义上说 |
| 空判断·绝对化 | A 的本质是 B / X 意味着 Y / X 是唯一的… / 之所以…是因为… |
| 假对立·假让步 | 不是…而是… / 要么…要么… / 无论…都… / 就算…也… |
| 模板骨架 | 首先其次最后 / 一方面另一方面；先…再…、如果…就…、只有…才 —— 后三个仅限真实操作步骤或真实条件分支，不用于铺垫强调 |

---

Wait — "先…再…" 仅限真实操作步骤 — hmm, "先…再…" IS the natural way to describe real procedure. And in tutorials that's most of its usage. The AI-flavor usage is rhetorical: "我们先明确概念，再逐步深入" as structural filler. OK my qualifier handles it. Similarly 如果…就/只有…才 for real conditionals. Good.

One thing: the table "模板骨架" cell got long. Maybe split the conditional ones into their own row? Keep as is — one row, with the qualifier. Fine.

Also, should the header mention 自检 method? "成文后可按黑名单逐条检索复查" — add a one-line 使用说明 at the end? The AGENTS.md bullet says 必读 — enough. Add small line at bottom: 成文后自检：按黑名单逐条扫一遍正文，命中即重写；再抽查每句删掉后是否损失信息。Good, actionable.

Now AGENTS.md bullet. Insert after line 11:

- 写文档/报告/教程等成文内容前，**必读 `~/.zcode/memory/de-ai-writing.md`**（去 AI 味提示词：判断先行、信息增量、句式黑名单）。

Hmm existing bullet uses backticks around path: "**必读 `~/.zcode/memory/output-preferences.md`**". Yes with backticks. Match.

Also update 记忆索引 table? The index table lists content→location. The 产出偏好 section is where 必读 items live; output-preferences.md is not in the index table either (it's referenced in 产出偏好 section). So just the bullet. Consistent.

Auto-memory file: de-ai-writing-prompt.md with frontmatter, prompt body, Why/How to apply, links.

Description: "写文档/报告/教程等成文产出前必执行的去 AI 味提示词（判断先行+信息增量+句式黑名单）；用户对 AI 味文风强烈反感"

Body: 用户 2026-10-05 明确表示 AI 写的文档/报告/教程"在语言结构和句子上"难以忍受，要求沉淀精简提示词。规范文件（canonical）：~/.zcode/memory/de-ai-writing.md，AGENTS.md 产出偏好已挂必读。内容如下：... (the prompt) ... then Why / How to apply.

Actually for auto-memory, per format: the fact, then **Why:** and **How to apply:**. The prompt IS the operative content. Structure:

---
name: de-ai-writing-prompt
description: ...
metadata:
  type: feedback
---

用户对 AI 味文风强烈反感（原话：AI 写的文档/报告/教程"在语言结构和句子上就是一坨屎"）。2026-10-05 沉淀了通用去 AI 味提示词，canonical 版在 `~/.zcode/memory/de-ai-writing.md`（AGENTS.md「产出偏好」已挂必读），内容：

<prompt body — maybe slightly condensed>

**Why:** 默认成文产出普遍带 AI 句式（空判断、假对立、模板骨架、防御性弱化），用户看到即负面；此规则是用户对"怎么写"的硬性要求，不是建议。

**How to apply:** 写/改任何文档、报告、教程、讲义、README 前先按三条原则构思，成文后按句式黑名单逐条自检重写；与 [[vi-lab-explanation-style]]（教学内容要求讲透原理）叠加：内容按它，语言按本规则。论文/简历场景另叠加 paper-resume-writing skill。

Good. Should I inline the full prompt in auto-memory or just point to canonical? Self-contained is better for recall (memory should stand alone), but drift risk. Compromise: inline full prompt (it's short), note canonical path. If user edits theirs, I'd notice via AGENTS.md difference. Fine.

MEMORY.md line: - [去AI味写作提示词](de-ai-writing-prompt.md) — 文档/报告/教程成文前必执行：判断先行+信息增量+句式黑名单；canonical 在 ~/.zcode/memory/de-ai-writing.md

Need to Read MEMORY.md first before editing (Edit requires Read). Path: C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory\MEMORY.md. Hmm — the system prompt says the memory dir is `C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory/`... wait, actually it says "C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory/" — let me copy exactly: `C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory/`. Hmm the system prompt text: "persistent file-based memory at `C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory/`". Wait, actually it says "default-291edf811f114b36"? Let me re-read: "C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory/". Hmm, in the system prompt it's written as `C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory/`. Actually exact string from system prompt: "C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory/" — I need to be careful. The system prompt says:

"You have a persistent file-based memory at `C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory/`."

Hmm wait, it actually says "default-291edf811f114b36"? Looking at the original: `C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory/` — no wait. Original text: "persistent file-based memory at `C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory/`". 

I can't scroll perfectly; the system prompt says: `C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory/`. Hmm, actually it says "default-291edf811f114b36" or "default-291edf811f114b36"? The MEMORY.md context block says "Contents of C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory\MEMORY.md". Wait no — it says "C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory\MEMORY.md (user's auto-memory...)". 

Let me look at the exact strings in the conversation:
- System prompt: "persistent file-based memory at `C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory/`"
- Context block: "Contents of C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory\MEMORY.md"

Both show "default-291edf811f114b36"... actually the context block reads "default-291edf811f114b36" — hmm, I see "default-291edf811f114b36" in system prompt and "default-291edf811f114b36" in context. They should be identical. To be safe, I'll ls the projects dir to get the exact path rather than guessing a long hex string. Cheap insurance.

Actually wait, from the conversation I can read: system prompt says "C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory/" — hmm I literally cannot verify char-by-char. The context block says "projects\default-291edf811f114b36\memory\MEMORY.md". Both contain "291edf811f114b36". I'll trust "default-291edf811f114b36". But a quick `ls` costs nothing and guarantees Write goes to the right dir. Do: ls C:/Users/UserX/.zcode/cli/memories/projects/ — then Read MEMORY.md at the exact path found.

Sequence now:
Batch A (parallel): Write ~/.zcode/memory/de-ai-writing.md; Bash ls memories/projects dir.
Then: Edit AGENTS.md; Read MEMORY.md (exact path).
Then: Write auto-memory file; Edit MEMORY.md.

Actually Edit AGENTS.md can go in batch A too (independent). And Read MEMORY.md needs the path from ls — dependent. So:

Batch A: Write canonical file, Edit AGENTS.md, Bash ls projects dir.
Batch B: Read MEMORY.md.
Batch C: Write auto-memory file, Edit MEMORY.md.

Wait, Edit AGENTS.md — I've read it. old_string: "- 做汇报/PPT、物理数学讲义或教学工具前，**必读 `~/.zcode/memory/output-preferences.md`**（排版/配图/配色/动画等硬要求）。" → new_string adds my bullet after. Unique match. Good.

Let me write out the canonical file content final version. One more pass on wording quality — this file will be read every future session, so it must be crisp and itself free of AI 味 (meta!).

Check my own text for AI patterns: "像对判断负责的作者，不像讨好读者的助手" — this is "像…不像…" comparative, borderline but it's a direct distillation of the image's opening and it's a real instruction, keep. No "本质是", no "不是…而是…" — wait: "不为显得完整补无关背景" fine. "不是建议" in the Why — "是用户对'怎么写'的硬性要求，不是建议" — ha, that's an "是…不是…" inversion in my own memory note. It's in the Why metadata, not user-facing output. Acceptable but let me rephrase to avoid the smell: "用户对'怎么写'的硬性要求"。Fine.

In the canonical file, avoid "值得注意" etc. Check blacklist compliance of my own prompt text: 
- "动笔前想清楚三件事" — fine (from image).
- "删掉一句话后读者的理解不变，这句话就删" — fine.
- No 首先/其次. Numbered list 1/2/3 is fine (it's a spec document, not prose).
- Table is fine (spec format).

One more consideration: the prompt's scope line says "文档、报告、教程、讲义、README 等成文产出" — also conversational answers? The user's complaint was about 文档/报告/教程. Chat replies are different (dialogue). Keep scope as 成文产出, mention that in final message? Not necessary. Keep.

Also should the canonical file carry a "版本/日期" line? The > 来源 line has 2026-10-05. Good enough.

Final canonical content:

```markdown
# 去 AI 味写作提示词（文档 / 报告 / 教程通用）

> 2026-10-05 沉淀，来源：用户提供的写作建议 + AI 高频句式清单。
> 适用：文档、报告、教程、讲义、README 等成文产出；论文/简历另走 `paper-resume-writing` skill，两套叠加。

## 三条原则

1. **像对判断负责的作者，不像讨好读者的助手。** 写作是选择：什么值得说、什么可以省略、什么证据足以支撑判断。动笔前想清楚三件事——这段回答什么问题、我的判断是什么、凭什么这样判断。判断直接说出来，再给依据；依据不足的地方，不用抽象概念、套话和修辞掩盖。不预设不存在的反对者，不为制造张力人为构造对立。

2. **每句话都要有信息增量。** 删掉一句话后读者的理解不变，这句话就删。优先写具体事实、数据、机制、操作步骤、案例和可观察结果；不补与当前论证无关的背景，不换一种说法重复已说清的判断。每段只承担一个主要任务，段落靠问题和判断自然推进；论证完直接结束，不补总结句、不拔高意义。

3. **句子服从意思，不追求整齐。** 长短句自然变化，段落结构允许不匀，不造空洞的比喻、排比、转折和升华。不反复给自己的判断上保险：不用"可能""一定程度上"习惯性弱化；证据只够有限结论时，准确说出边界即可；不提前回应还没出现的质疑，防御性表述不进正文。

## 句式黑名单（命中即重写）

重写方法：把句式拆掉，直接写出真正想表达的那个判断。

| 类型 | 句式 |
|---|---|
| 口播说教腔 | 说实话… / 说白了… / 一句话… / 记住… / 让我们… / 我的建议是… |
| 元话语 | 全文 / 本文将 / 值得注意的是 / 需要指出的是 / 从某种意义上说 |
| 空判断·绝对化 | A 的本质是 B / X 意味着 Y / X 是唯一的… / 之所以…是因为… |
| 假对立·假让步 | 不是…而是… / 要么…要么… / 无论…都… / 就算…也… |
| 模板骨架 | 首先其次最后 / 一方面另一方面；先…再…、如果…就…、只有…才（后三个仅限真实操作步骤或真实条件分支，不用于铺垫强调） |

## 成文后自检

1. 按黑名单逐条扫正文，命中即重写；
2. 抽查句子：删掉后读者的理解不变，就删；
3. 每段只讲一件事，段末没有总结拔高句。
```

Good. Now auto-memory file body — inline the same content. And frontmatter.

Alright, execute batch A now. Actually also need to double check: "shell 里输出中文可能间歇性乱码→中文内容一律用 Read/Write 工具读写" — I'm using Write tool for Chinese files. ✓ (ls output is ASCII filenames, fine.)

</details>

- 🔧 **Write** `{"file_path": "C:\\Users\\UserX\\.zcode\\memory\\de-ai-writing.md", "content": "# 去 AI 味写作提示词（文档 / 报告 / 教程通用）\n\n> 2026-10-05 沉淀，来源：用户提供的写作建议 + AI 高频句式清单。\n> 适用：文档、报告、教程、讲义、README 等成文产出；论文/简历另走 `paper-resume-writing` skill，两套叠加。\n\n## 三条原则\n\n1. **像对判断负责的作者，不像讨好读者的助手。** 写作是选择：什么值得说、什么可以省略、什么证据足以支撑判断。动笔前想清楚三件事——这段回答什么问题、我的判断是什么、凭什么这样判断。判断直接说出来，再给依据；依据不足的地方，不用抽象概念、套话和修辞掩盖。不预设不存在的 …[截断,原长413]` → `File created successfully at: C:\Users\UserX\.zcode\memory\de-ai-writing.md (file state is current in your context — no need to Read it back)`

- 🔧 **Edit** `{"file_path": "C:\\Users\\UserX\\.zcode\\AGENTS.md", "old_string": "- 做汇报/PPT、物理数学讲义或教学工具前，**必读 `~/.zcode/memory/output-preferences.md`**（排版/配图/配色/动画等硬要求）。", "new_string": "- 做汇报/PPT、物理数学讲义或教学工具前，**必读 `~/.zcode/memory/output-preferences.md`**（排版/配图/配色/动画等硬要求）。\n- 写文档/报告/教程等成文内容前，**必读 `~/.zcode/memory/de-ai-writing.md`**（去 AI 味提示词：判断先行、信息增量、句式黑名单）。"}` → `The file C:\Users\UserX\.zcode\AGENTS.md has been updated successfully. (file state is current in your context — no need to Read it back)`

- 🔧 **Bash** `{"command": "ls \"C:/Users/UserX/.zcode/cli/memories/projects/\"", "description": "Get exact auto-memory project directory name"}` → `_-_-3d78dd3bbe323572/ cad-799c56b5ed2ddf1d/ default-291edf811f114b36/ local-ocr-083d245cd91c7428/ minecraft-crawl-grammer-86ca118d2a797bad/ minimind-master-a0c542043ef95cac/ ppt-master-image-api-patch-2459e3675e4ae8de/ project-8b54cbaf7ad4a442/ project-c2401ae78819a002/ project-e3578785365396c1/ project-e622068416c46d4 …[截断,原长411]`

### 🤖 助手（GLM-5.3-Flash，2026-10-05 13:32）

都对上了：截图内容完整可读，`~/.zcode/memory/` 里还没有去 AI 味相关文件，output-preferences.md 只管排版配图（视觉），paper-resume-writing skill 只管论文/简历——语言层面的通用规则确实是空白，不重复。现在写入三处：你的记忆库、AGENTS.md 必读钩子、我的自动记忆。

<details><summary>💭 思考链（GLM-5.3-Flash）</summary>

The Write succeeded but the path I used was `C:\Users\UserX\.zcode\memory\de-ai-writing.md` — wait, the output shows "File created successfully at: C:\Users\UserX\.zcode\memory\de-ai-writing.md" — hmm, actually it shows "de-ai-writing.md" at `C:\Users\UserX\.zcode\memory\`? Let me re-read: "File created successfully at: C:\Users\UserX\.zcode\memory\de-ai-writing.md". Yes, good — that's the canonical location I intended.

The AGENTS.md edit succeeded.

The ls shows the memories projects dir: `default-291edf811f114b36` — wait, it shows "default-291edf811f114b36/"? The output says `default-291edf811f114b36/`. Hmm, actually it reads "default-291edf811f114b36/" — let me look: "default-291edf811f114b36/". The system prompt said "default-291edf811f114b36". OK so the path is:

C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory\

Hmm wait, the ls output shows "default-291edf811f114b36/" — actually it literally shows "default-291edf811f114b36/". Let me trust the tool output: `default-291edf811f114b36/`. Hmm, but I typed "default-291edf811f114b36" in my head... the output is authoritative: `default-291edf811f114b36/`. Wait, actually reading the raw output again: "default-291edf811f114b36/". OK.

Hmm, but the system prompt path was "C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory/" and context block said "C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory\MEMORY.md". The ls output confirms "default-291edf811f114b36". Good — consistent.

Wait, actually I need to double check: ls output shows "default-291edf811f114b36/" — the exact string. Fine: `C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory\`.

Now:
1. Write the auto-memory file there: de-ai-writing-prompt.md
2. Read + Edit MEMORY.md there.

Batch: Write file + Read MEMORY.md (independent). Then Edit MEMORY.md.

For the auto-memory file content — self-contained with the full prompt, Why/How, links to [[paper-resume-writing-skill]] and [[vi-lab-explanation-style]], and note canonical path.

</details>

- 🔧 **Read** `{"file_path": "C:\\Users\\UserX\\.zcode\\cli\\memories\\projects\\default-291edf811f114b36\\memory\\MEMORY.md"}` → `1 - [2027 推免项目进度](baoyan-2027-project.md) — 用户在跑 2027 级保研选导师，已做保研网筛选、北理工经济学院、西安交大经金学院 2 - [轮式机器人指导书小白详解项目](wheeled-robot-guide-interpretation.md) — 168 页讲义已交付；md→docx 管线可复用；子代理并发2/配额/visual-judge 供应商三坑 3 - [中文口碑/官网检索 playbook](cn-web-research-playbook.md) — 导师评价网（脱敏+微信墙）、百度/知乎/贴吧可见性、WebFetch 踩坑 4 - [保研信息网站点笔记](baoyanwa …[截断,原长1941]`

- 🔧 **Write** `{"file_path": "C:\\Users\\UserX\\.zcode\\cli\\memories\\projects\\default-291edf811f114b36\\memory\\de-ai-writing-prompt.md", "content": "---\nname: de-ai-writing-prompt\ndescription: 用户强烈反感AI味文风；写文档/报告/教程等成文产出前必执行的去AI味提示词（判断先行+信息增量+句式黑名单）\nmetadata:\n type: feedback\n---\n\n用户原话：AI 写的文档/报告/教程\"在语言结构和句子上就是一坨屎\"，看到就难受。2026-10-05 已把去 AI 味提示词沉淀为 canonical 文件 `~/.zcode/memory/de-ai …[截断,原长412]` → `File created successfully at: C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory\de-ai-writing-prompt.md (file state is current in your context — no need to Read it back)`

### 🤖 助手（GLM-5.3-Flash，2026-10-05 13:33）

写入成功。现在补我的自动记忆（含 MEMORY.md 索引）。

<details><summary>💭 思考链（GLM-5.3-Flash）</summary>

Add the index line to MEMORY.md.

</details>

- 🔧 **Edit** `{"file_path": "C:\\Users\\UserX\\.zcode\\cli\\memories\\projects\\default-291edf811f114b36\\memory\\MEMORY.md", "old_string": "- [论文/简历写作 skill](paper-resume-writing-skill.md) — paper-resume-writing skill（~/.zcode/skills，558 字）：Introduction 七步法+简历去 AI 味五特征；约束 skill ≤600 字\n", "new_string": "- [论文/简历写作 skill](paper-resume-writing-skill.md) — paper-resume-writing skill（~/.zcode/s …[截断,原长412]` → `The file C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory\MEMORY.md has been updated successfully. (file state is current in your context — no need to Read it back)`

<details><summary>💭 思考链（GLM-5.3-Flash）</summary>

Wait — the Edit result shows the path as "C:\Users\UserX\.zcode\cli\memories\projects\default-291edf811f114b36\memory\MEMORY.md" but I wrote old_string/new_string about "论文/简历写作 skill — paper-resume-writing skill"... hold on. My edit content was wrong! Let me look at what I actually submitted:

old_string: "- [论文/简历写作 skill](paper-resume-writing-skill.md) — paper-resume-writing skill（~/.zcode/skills，558 字）：Introduction 七步法+简历去 AI 味五特征；约束 skill ≤600 字"
new_string: adds my line after.

But the actual MEMORY.md line 18 (from my Read) was:
"- [论文/简历写作 skill](paper-resume-writing-skill.md) — paper-resume-writing skill（~/.zcode/skills，558 字）：Introduction 七步法+简历去 AI 味五特征；约束 skill ≤600 字"

Hmm wait, the Read output line 18 says: "- [论文/简历写作 skill](paper-resume-writing-skill.md) — paper-resume-writing skill（~/.zcode/skills，558 字）：Introduction 七步法+简历去 AI 味五特征；约束 skill ≤600 字"

And my old_string matched it (the edit succeeded), so fine. The new line I appended: "- [去 AI 味写作提示词](de-ai-writing-prompt.md) — 文档/报告/教程成文前必执行：判断先行+信息增量+句式黑名单；用户对 AI 味文风强烈反感；canonical 在 ~/.zcode/memory/de-ai-writing.md"

Hmm wait, in my actual tool call the new_string was:
"- [论文/简历写作 skill](paper-resume-writing-skill.md) — paper-resume-writing skill（~/.zcode/skills，558 字）：Introduction 七步法+简历去 AI 味五特征；约束 skill ≤600 字\n- [去 AI 味写作提示词](de-ai-writing-prompt.md) — 文档/报告/教程成文前必执行：判断先行+信息增量+句式黑名单；canonical 在 ~/.zcode/memory/de-ai-writing.md"

The tool result says updated successfully. 

Also there's a system-reminder at the top of this conversation saying the auto-memory MEMORY.md already contains "[去AI味写作提示词](de-ai-writing-prompt.md) — 文档/报告/教程成文前必执行：判断先行+信息增量+句式黑名单；canonical 在 ~/.zcode/memory/de-ai-writing.md" — that matches what I just added. Consistent.

Everything is done:
1. ✓ Canonical file ~/.zcode/memory/de-ai-writing.md
2. ✓ AGENTS.md 必读 bullet under 产出偏好
3. ✓ Auto-memory file + MEMORY.md index

Now the final message to the user:
- Lead with outcome: prompt written to long-term memory, three places.
- Show the prompt itself (they need to review).
- Explain the one design decision: 条件句/顺序词不是一刀切（真实步骤和真实条件保留），否则教程没法写；口播腔、元话语、空判断、假对立是一刀切。
- Note where each file lives and how it fires (AGENTS.md 必读钩子 = 每会话生效；我的自动记忆 = 相关时召回).
- Keep it in Chinese, readable, no AI 味 in my own message (practice what I preach!).

Let me check my own final message for blacklist compliance: no 说实话/本质/不是而是/首先其次/值得注意/总结拔高. Write plainly.

</details>

### 🤖 助手（GLM-5.3-Flash，2026-10-05 13:34）

完成。提示词已写入三处长期记忆，下个会话起自动生效。

## 提示词全文

**三条原则**

1. **像对判断负责的作者，不像讨好读者的助手。** 动笔前想清楚：这段回答什么问题、我的判断是什么、凭什么。判断直接说出来再给依据；依据不足不用抽象概念、套话和修辞掩盖。不预设反对者，不为张力人为构造对立。
2. **每句话要有信息增量。** 删掉后读者理解不变的句子一律删。优先写具体事实、数据、机制、操作步骤、案例、可观察结果；不补无关背景，不换说法重复已说清的判断。每段只承担一个主要任务，论证完直接结束，不补总结句、不拔高意义。
3. **句子服从意思。** 长短句自然变化，段落结构允许不匀；不造空洞比喻、排比、升华。少用“可能”“一定程度上”“值得注意”给自己上保险；证据只够有限结论时准确说边界，不提前回应未出现的质疑。

**句式黑名单（出现即重写，重写 = 把句式拆掉直接写那个判断）**

- 口播说教腔：说实话 / 说白了 / 一句话 / 记住 / 让我们 / 我的建议是
- 元话语：全文 / 本文将 / 值得注意的是 / 需要指出的是 / 从某种意义上说
- 空判断·绝对化：A 的本质是 B / X 意味着 Y / X 是唯一… / 之所以…是因为…
- 假对立·假让步：不是…而是… / 要么…要么… / 无论…都… / 就算…也…
- 模板骨架：首先其次最后 / 一方面另一方面；先…再…、如果…就…、只有…才

## 一处有意的设计

“先…再…、如果…就…、只有…才”没有一刀切，加了限定“仅限真实操作步骤或真实条件分支”——教程里“先编译再烧录”是正常表达，全禁会导致教程没法写；要禁的是拿它们做铺垫强调的用法。口播腔、元话语、空判断、假对立这四类是一刀切。如果你想让这几条也无条件禁止，改 canonical 文件里那一行就行。

## 写入位置

- [de-ai-writing.md](C:\Users\UserX\.zcode\memory\de-ai-writing.md) — canonical 版，你随时可改
- [AGENTS.md](C:\Users\UserX\.zcode\AGENTS.md) — 产出偏好下加了一行“写文档/报告/教程前必读”，保证每会话生效
- 我的自动记忆 — 存了全文副本，标注以你的 canonical 为准

和已有的 paper-resume-writing skill（论文/简历专用）是叠加关系，语言层面走这份，内容层面各走各的。
