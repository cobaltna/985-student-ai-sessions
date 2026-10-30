# highlights — 从会话里沉淀出的可复用成果

这些是本人在会话中做出的、可独立拿出来用的东西，全部来自上方 `sessions/` 对应会话（每个子目录的来源会话在括号里）。

## skills/（ZCode 技能包，放在 `~/.zcode/skills/` 即被自动发现）

| 目录 | 用途 | 来源会话 |
|---|---|---|
| `local-ocr/` | 本地批量 OCR（PaddleOCR + LM Studio），无多模态模型也能读扫描件/图片文字，含 LaTeX 后处理 | 2026-09-30_PaddleOCR重复字符优化 |
| `docx-inplace-modify/` | 程序化原地修改已有 Word 文档并保留格式（python-docx + lxml） | 2026-09-12 多个文档会话逐步沉淀 |
| `paper-resume-writing/` | 论文 Introduction 七步法 + 简历去 AI 味（HR 一眼假五特征） | 2026-10-02_paper-resume-writing去AI味skill创建 |
| `minecraft-bedrock-dev/` | 基岩版模组开发：先查本地 900 篇爬取的官方文档，再上网兜底 | 2026-09-30_minecraft-bedrock-dev本地文档检索skill编写 |
| `openfilm/` | OpenFilm 网页视频剪辑控制 | 2026-10-23_OpenFilm接入ZCode |
| `web-search/` | AnySearch 搜索 + Firecrawl 抓全文（含 PDF），替代内置搜索 | 2026-10-20_ZCode内置搜索质量改善 |
| `github-machine/` | 本机 GitHub 工具链约定（代理/gh/大包推送/设备码授权） | 2026-09-30_幸运方块地图README与开源 |
| `memory-office-docs/` · `memory-web-scraping/` | 记忆型 skill：把本机环境/爬虫经验固化成按需加载的技能 | 2026-09-09_长期记忆体系搭建 |

第三方安装的 `ppt-master` / `ppt-master-pro` / `ui-ux-pro-max`（复试 PPT、去AI味 PPT 会话用到）体积大且非本人创作，未收录，见对应会话。

## hooks-and-plugins/

- `delete-guard-hook/` — 拦截高危删除命令（rm --no-preserve-root、删 Windows 目录等）的 PreToolUse 钩子，59 项自测；配 `tests/`。（来源：2026-09-30 危险删除命令审查钩子）
- `no-overdefense-plugin/` — 「防过度防御性编程」插件：1 个 skill + 3 组钩子，阻止 AI 写没人要的安全检测/哈希对比/冒烟自检。是「痛点→skill→hook→插件」的完整样例。（来源：2026-10-05_no-overdefense插件开发）

## openfilm-bridge/

把 ZCode（ACP 协议）接入 OpenFilm 剪辑软件的桥接器：`bridge.mjs` 主桥、`acp-test.mjs` 验证脚本、`install.mjs` 安装器。（来源：2026-10-23_OpenFilm接入ZCode）

## cot-peek/

ZCode 思维链机翻悬浮球：监听 transcript 增量文件 → 免费机翻 → 深色小窗显示，支持划词翻译、中断/回溯补翻、多会话适配。不注入提示词、不污染模型上下文。（来源：2026-10-30_ZCode思维链机翻悬浮小窗开发）
