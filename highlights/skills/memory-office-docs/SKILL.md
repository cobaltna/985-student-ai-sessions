---
name: memory-office-docs
description: Use when 创建/修改/验证 Word、Excel、PPT、PDF 等 Office 文档及生成代码：docx-js、openpyxl、python-pptx、PyMuPDF、OMML 公式、soffice/LibreOffice 转换、mupdf 渲染、批量插图、教学讲义与报告生成。遇到 docx 打开报错、Excel 写入异常、PDF/中文字体问题、文档验证超时等踩坑时使用。含用户长期沉淀的文档生成经验。
---

# 记忆：Office 文档生成与验证（长期踩坑沉淀）

## docx-js 要点
1. Math 对象可与中文 TextRun 同段落，正常。
2. TextRun 禁 spread 自定义 opts（`...opts`）→ 产生非法 XML；上/下标必须显式设 `superScript` / `subScript`。
3. 禁 `_rawXml` 注入 OMML → 中文会变空白。
4. Word 开着同名文件再写入 → EBUSY；先关文件或换名。
5. MathRadical 作 MSup 的 base 须手动构造，不能直接内嵌。
6. OMML 化学方程式：加号不能放进排除列表（否则电荷不渲染成上标）。
7. 化学式优先用 Unicode 上下标（H₂O / Na⁺ / CO₃²⁻）写在 TextRun 里，比 OMML 更实用。
8. docx 版本：9.6.1 正常，9.7.1 有 bug → 锁 9.6.1。
9. 表格内嵌 OMML 括号易错配 → SyntaxError；写完务必 `node --check`。
10. MathCurlyBrackets 做方程组大括号：每个 child 单独成 m:e 行（有 bug：可能把所有 children 塞进单个 m:e → AdmZip 后处理拆开）。
11. ImageRun 生成的 wp:docPr id 全为 "1" → AdmZip 后处理改为唯一 ID。
12. 返回 Paragraph 的函数不能直接作 P() 的 children → 非法嵌套 w:p。
13. 裸 MathRun 等无 m:oMath 包裹 → 用 eq() helper 自动包裹。
14. 批量插图：`sharp(buf).metadata()` 取宽高再建 ImageRun；>50 张生成 50+MB 属正常。
15. MathFraction 的 numerator/denominator 须传直接数组 `[new MathRun(x)]`，传 `{children: []}` 会报 children is not iterable。
16. 自定义排版函数若返回数组（如 figure()/workSpace()/emptyLine()），push 时必须 `...` 展开；漏 spread → docx 内嵌 Array → LibreOffice 报 "source file could not be loaded"（Word 能开）。
17. TableOfContents 在 LibreOffice 渲染空白属正常，Word 打开（updateFields: true）会自动填充。

## openpyxl 要点
1. 清空单元格必须 `cell.value = ''`；赋 None 旧值会残留。
2. 保存时会丢弃空字符串单元格（空 inlineStr 读回为 None）→ 与 '' 视觉等价，勿过度修复。
3. 写已被 Excel 打开的 .xlsx → PermissionError → fallback 写到 outputs 目录；写后验证必须读输出文件，别读原文件（可能仍是旧版）。
4. 跨文件对比/去重以「链接 URL」为唯一键，勿用序号/行号（序号列可能非唯一）；带发布者时按 URL/标题+发布者匹配。
5. PowerShell 跑 Python 超过 60s 必超时 → 用后台任务 + 输出重定向文件 + sleep 后 cat；Windows bash 同理：长命令用大 timeout（≥600000ms）或后台执行。

## PyMuPDF（有 python 的机器）
1. 1.28.0 移除了 `doc.insert_font()`：注册中文字体须在 `insert_text`/`insert_textbox` 里直接传 `fontfile` 参数。
2. Unicode 上/下标字符（U+2080-2089 / U+2070-207B）渲染为方框，即使用 SimHei/MsYh/Arial 也一样 → 用普通数字替代。
3. 用前先确认本机 python：**UserX 本机有 python** → `C:\Users\UserX\.conda\envs\opencv\python.exe`（PyMuPDF 1.28.2 已装）。
   调用时**必须写全路径**（`python3`/`python` 都不在 PATH）。仅解释器缺失时才退回 mupdf(node) 链。

## 文档渲染 / 验证链（本机 UserX）
- **本机工具链（实测 2026-10-07）**：LibreOffice 26.2.4.2、Python 3.12.12（conda opencv）、Node v24.13.0 均已装好；
  LibreOffice 和 conda python 不在 PATH，一律用绝对路径；node/npm 在 PATH。不要重装、不要改系统 PATH。完整表见 `~/.zcode/memory/office-doc-toolchain.md`。
- Windows bash 里 soffice 不在 PATH：全路径 `"/c/Program Files/LibreOffice/program/soffice.com" --headless --convert-to pdf`（用 `.com`，无控制台窗口）。
- 文档链验证主链路：docx → soffice 转 PDF → **PyMuPDF（`python.exe`）** 渲染 PNG；
  （旧记法「本机无 python，走 mupdf node 链」**已过期**，仅解释器缺失时才退回。）
- 无 Poppler（`pdftoppm` 不在 PATH）→ PDF 转图一律走 `pymupdf`：`page.get_pixmap(dpi=150).save(...)`。
- docx npm 锁 9.6.1；npm 依赖在 `C:\Users\UserX\node_modules` → 脚本前置 `NODE_PATH="C:/Users/UserX/node_modules"`。
- 中文字体宋体/黑体/微软雅黑/等线已装 → 勿下载字体。
- mupdf 是 ESM + 顶层 await：require 报 `ERR_REQUIRE_ASYNC_MODULE`，必须 .mjs 文件 + import。
- validate.py 在 Windows 会超时 → 走 soffice 转 PDF + PyMuPDF/mupdf 验证。
- LibreOffice 与 Word 行为不一致时（能开/不能开），以 Word 打开结果为准并说明。
- bash 里 node -e 含中文路径：用正斜杠字符串最稳。
- 图片瘦身：sharp 转 jpeg（1200px, q88）可把 56MB → 1.6MB。
- Read 工具读图片返回 AI 文字描述而非像素 → 需要精确数值时用 sharp raw() 像素分析（整刻度标签定标 + 液面行插值）。

## PPT（视觉与风格见用户画像；工程细节另见 ~/.zcode/memory/ppt-master-project.md）
- 用户 PPT 相关专案（ppt-master / gpt-image-2 代理补丁、UI/UX Pro Max 桥接）是独立工程，做 PPT 生成任务前先读该归档文件。
