---
name: local-ocr
description: 批量 OCR：处理较多页数的、以文本为主的扫描版 PDF（先渲染成图片再逐页识别），或批量纯文字图片（试卷/文档截图/书页照片等需要查看具体文字内容的图片）。注意是纯文字图片——只提取图中文字、公式（LaTeX）、表格（Markdown），不能理解几何图形和图表结构。当前模型无视觉能力而任务需要读图文字时也用它。触发词：OCR、识别图片、批量识别、提取文字、扫描件、读 PDF 内容。
---

# Local OCR（LM Studio + PaddleOCR-VL-1.5）

通过本地 LM Studio 的 OpenAI 兼容 API 调用 **PaddleOCR-VL-1.5** 模型做 OCR。纯本地离线，单页约 1–8 秒。脚本 `ocr.py` 仅用 Python 标准库，无需 pip 安装。

## 何时用 / 何时不用

**✅ 用**：
- 批量处理**页数较多的文本为主扫描 PDF**（论文、讲义、试卷扫描件）——先渲染成图片，逐页识别，最后合并
- 批量**纯文字图片**（多张截图、拍照的文档/试卷），需要拿到其中的文字、公式、表格内容
- 当前模型没有视觉能力（纯文本 LLM），任务需要读图里的文字

**❌ 不用**（或用了也要说明局限）：
- 图片的核心是**几何图形/图表/电路图/光路图**：OCR 只能拿到图中印刷的文字和符号，**拿不到图形的空间结构**（三角形形状、点的位置、曲线走势）。无法据此解题。如实告诉用户："我能读出图中的文字，但看不到图形本身。"
- 少量图片且当前模型有视觉能力 → 直接用视觉更快
- 表格结构要求高的页面 → 裁出表格区域单独用 `--prompt "Table Recognition:"`

## 快速开始

```bash
# 0. 健康检查（每次会话首次使用前跑一次）
python "<SKILL_DIR>/ocr.py" --check

# 1. 单张图片
python "<SKILL_DIR>/ocr.py" -i "C:\path\to\image.png"

# 2. 结果存文件 / JSON 输出（含 tokens、耗时、退化标志）
python "<SKILL_DIR>/ocr.py" -i image.png -o result.txt
python "<SKILL_DIR>/ocr.py" -i image.png --json
```

`<SKILL_DIR>` = 本技能目录（ZCode: `C:\Users\UserX\.zcode\skills\local-ocr`）。

## 扫描 PDF 批量流程（核心用法）

```python
# 第 1 步：PDF → PNG（用 conda opencv 环境的 python，含 pymupdf）
import fitz
doc = fitz.open(r"C:\path\to\scan.pdf")
for i, page in enumerate(doc):
    page.get_pixmap(dpi=150).save(f"pages/page{i+1}.png")   # 150 DPI 足够
```

```bash
# 第 2 步：逐页识别（bash 循环）
for f in pages/page*.png; do
  python "<SKILL_DIR>/ocr.py" -i "$f" -o "text/$(basename "$f" .png).txt"
done
# 第 3 步：按页码顺序合并所有 txt
```

**公式密集的页面**（论文/讲义）：加 `--passes 2` 或 `3`——模型偶发提前停止导致静默漏掉一栏/一节（约 30% 概率，无任何报错），多跑几次取最长结果能找回，代价约 3 倍时间。普通文字页不需要。

## 任务 Prompt（官方训练格式，冒号不能省）

| 任务 | `--prompt` 值 |
|---|---|
| 一般文字（默认） | `OCR:` |
| 数学公式 | `Formula Recognition:` |
| 表格 | `Table Recognition:` |
| 图表 | `Chart Recognition:` |

## 输出格式

- 纯文本原样输出；数学公式为 LaTeX（`\(x^2\)`、`\[\frac{a}{b}\]`、`\tag{编号}`）
- 表格为 Markdown 或线性化文本（整页小表格可能丢结构——重要表格请裁剪后单独识别）
- 中文、英文、混排均可靠；参考文献 URL/DOI 可逐字正确
- **LaTeX 语法质量**：约 1% 的数学片段有机械性语法缺陷（下标漏花括号、定界符未闭合等）。若输出将喂给 LaTeX 渲染器，加 `--fix-latex` 自动修复（2400+ 片段 KaTeX 验证：缺陷 24→1）；不加则保持模型原始输出。

## 可靠性机制（内置，无需干预）

- **重复/退化守卫**：输出自动筛查（字符级循环、段落级重复、token 封顶），检出即自动换温度+seed 重试，返回最干净的一次；仍可疑时 stderr 打 `[WARN]`、JSON 加 `"degenerate": true`——此时结果不可信，建议裁剪图片或换区域 prompt。
- **截断预防**：模型需以 ≥16384 上下文加载（已在本机 `~/.lmstudio/settings.json` 持久化）。若输出在 ~1200 token 处莫名截断，检查 LM Studio 加载上下文。

## 环境变量（可覆盖默认）

| 变量 | 默认 | 说明 |
|---|---|---|
| `LMSTUDIO_OCR_API` | `http://127.0.0.1:1234/v1/chat/completions` | API 端点 |
| `LMSTUDIO_OCR_MODEL` | `paddleocr-vl-1.5` | 模型 ID |
| `LMSTUDIO_OCR_PROMPT` | `OCR:` | 默认 prompt |
| `LMSTUDIO_OCR_TEMPERATURE` | `0.45` | 采样温度 |
| `LMSTUDIO_OCR_RETRIES` | `2` | 退化时额外重试次数 |
| `LMSTUDIO_OCR_PASSES` | `1` | 每图运行次数，取最长结果 |
| `LMSTUDIO_OCR_FIX_LATEX` | `0` | 置 1 启用 LaTeX 语法后处理（等价 `--fix-latex`） |
| `LMSTUDIO_OCR_TIMEOUT` | `180` | 超时（秒） |

## 故障排查

| 症状 | 处理 |
|---|---|
| `Connection refused` | LM Studio 未启动或 Local Server 未开（Developer → Start Server） |
| `Model not found` | My Models 里加载 PaddleOCR-VL-1.5 |
| `HTTP 400: Model does not support images` | mmproj 文件缺失/命名不对，见 INSTALL.md |
| 输出中途截断 | 加载上下文 <16k，重载模型 |
| `[WARN]` 重复告警 | 裁剪图片/换任务 prompt；必要时 `lms runtime update` |
| 慢（>10s） | GPU Offload 设 Max；触发重试时耗时翻倍属正常 |

详细安装/回滚见 INSTALL.md，其他编辑器接入见 CROSS_EDITOR.md。
