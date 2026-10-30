---
name: docx-inplace-modify
description: 程序化原地修改已有 Word 文档（.doc/.docx）并保留原格式：python-docx + lxml 填表格、插图片、加段落、删章节、批量改同类文档、.doc 转 .docx。适用于改现有文档而非重建、格式复杂必须保留、改动分散在全文多处；从零创建文档用 docx skill。触发词：改 Word、填表格、插入图片、删除章节、批量修改文档、保留格式、.doc 转换、原地修改。
---

# 修改 Word 文档（python-docx + lxml）

任务是在不破坏原有格式、图片和表格样式的前提下，用脚本修改一份已存在的文档。
全程只操作工作副本，不直接改动原始文件。整个修改写成 python 脚本一次跑完，
不要在对话里多次内联执行零散代码。

## 与 docx skill 的分工

| 场景 | 用哪个 |
|---|---|
| 从零创建文档、批注、修订、 tracked changes | docx skill（docx-js 或 XML 解包重打包） |
| 填表格、插图片、加段落、删章节等结构性改动 | 本 skill（python-docx + lxml） |
| 多份同模板文档批量处理 | 本 skill，一个脚本循环处理 |

取舍：python-docx 对修订、批注这类底层 XML 细节控制力弱；但填数据、加内容、
批量结构改动时，它比手改几十个 XML 节点可靠得多。需要精细控制修订时换 docx skill。

## 环境速查

python、soffice、node 的完整路径与实测版本见 `~/.zcode/memory/office-doc-toolchain.md`，
解释器选择见 `~/.zcode/memory/python-envs.md`，bash 调用规则见 AGENTS.md。要点只有两条：

- 文档操作用 conda `opencv` 环境的 python（已含 python-docx、lxml、Pillow、PyMuPDF）。
- 脚本一律用 Write 工具写成 .py 文件再执行，不要内联（中文与引号嵌套必出事）。

## 工作流

### 第 1 步：准备工作副本

`.docx` 直接 cp 一份。`.doc` 是老二进制格式，python-docx 打不开，先转格式；
LibreOffice 转换对字体、图片、表格、版式的保留远好于用 docx-js 重建：

```bash
cp "原始文件.doc" input.doc   # 中文文件名必须先转 ASCII，否则 soffice 静默失败
"/c/Program Files/LibreOffice/program/soffice.com" --headless --convert-to docx input.doc --outdir .
```

### 第 2 步：先建元素索引，再动任何手

打开文档后第一件事是给 body 建完整索引。索引存的是 XML 元素的引用，
之后所有定位、修改、删除都只依赖它：

```python
from docx import Document
from docx.oxml.ns import qn

doc = Document('working_copy.docx')
body = doc.element.body
WP, WT = qn('w:p'), qn('w:tbl')

para_info = []   # [(body_index, element, text)]
table_info = []  # [(body_index, element, table_seq)]

for i, elem in enumerate(body):
    if elem.tag == WP:
        text = ''.join(t.text or '' for t in elem.findall('.//' + qn('w:t')))
        para_info.append((i, elem, text))
    elif elem.tag == WT:
        table_info.append((i, elem, len(table_info)))
```

为什么必须先建索引：之后任何 `add_paragraph()`、`addnext()` 都会让 body 索引
整体后移。索引只在此刻有效，先拍快照再动手，后面绝不重新 enumerate(body)。

### 第 3 步：按内容定位目标

在索引的文本上做匹配来定位章节、题号、表格归属。匹配规则因文档而异——
先打印索引通读结构，确认真实标题样式后再写正则，不要照搬任何现成正则。
表格归属用"区间包含"判断：某表格的 body_index 落在某章节的起止范围内，
就把它映射给那个章节。文档末尾的边界要显式找标记（如"附录"、落款），
默认"最后一个章节到文档末尾"会把尾部内容误圈进来。

### 第 4 步：执行修改

**填表**。表格用索引映射出的序号取，不要直接猜 `doc.tables` 的顺序
（嵌套表、错位表会让两者不一致）：

```python
table = doc.tables[tbl_idx]
cell = table.cell(row, col)
if not cell.paragraphs[0].runs:
    cell.text = value                    # 空模板格：直接赋值
else:
    cell.paragraphs[0].runs[0].text = value   # 已有内容的格：改 run，保留字体字号
```

`cell.text = value` 会把单元格重置成单个默认格式段落。要保留原格式就改 run 的文本。

**加段落**。字体字号必须写在 run 的 `w:rPr` 里——写进 `w:pPr` 只影响段落标记，
正文不会变：

```python
from lxml import etree

def make_para(text, font='SimSun', size_pt=10.5):
    p = etree.Element(qn('w:p'))
    r = etree.SubElement(p, qn('w:r'))
    rPr = etree.SubElement(r, qn('w:rPr'))
    rFonts = etree.SubElement(rPr, qn('w:rFonts'))
    rFonts.set(qn('w:ascii'), font); rFonts.set(qn('w:eastAsia'), font)
    sz = etree.SubElement(rPr, qn('w:sz')); sz.set(qn('w:val'), str(int(size_pt * 2)))
    t = etree.SubElement(r, qn('w:t')); t.text = text
    t.set(qn('xml:space'), 'preserve')
    return p

pos = anchor                       # anchor 来自第 2 步索引
for line in lines:
    new_p = make_para(line)
    pos.addnext(new_p)             # addnext 把新元素插到 pos 之后
    pos = new_p                    # 链式推进保证多行按顺序排列
```

**插图**。先在 body 末尾建段落，再整体移动到目标位置——`addnext` 对已有
元素是移动而不是复制，这正好省去手工摘除：

```python
import io
from docx.shared import Pt

def insert_image_after(anchor, img_path, width_pt=380):
    p = doc.add_paragraph()
    run = p.add_run()
    with open(img_path, 'rb') as f:
        run.add_picture(io.BytesIO(f.read()), width=Pt(width_pt))
    anchor.addnext(p._element)
```

图片用 PNG（相机直出 JPEG 常触发 `UnrecognizedImageError`）；380pt 适配 A4 正文宽度。

**删元素**。用 `id(elem)` 标记删除对象，绝不用 body 索引。前面插过内容后
索引已漂移，重新 enumerate 再按范围删会误删要保留的内容；而索引里的元素引用
永远指向老元素，新插的元素不在集合里，天然不会误删：

```python
to_delete = {id(e) for bi, e, _ in para_info if start <= bi < end}
to_delete |= {id(e) for bi, e, _ in table_info if start <= bi < end}

for elem in list(body):
    if id(elem) in to_delete:
        body.remove(elem)
```

### 第 5 步：保存与验证

保存到新文件名（工作副本保留）。用户正用 Word/WPS 开着同名文件时写入会报
EBUSY——直接换名输出（加 `_new`/`v2` 后缀），不要要求用户关闭文件。

```python
doc.save('output_new.docx')
print(len([e for e in body if e.tag == WP]), 'paragraphs',
      len([e for e in body if e.tag == WT]), 'tables')
print(len(doc.inline_shapes), 'images')
for i, table in enumerate(doc.tables):
    print(f'Table {i}: first cell = {table.cell(0, 0).text!r}')
```

段落/表格/图片计数应与预期一致；需要目检版式时转 PDF 渲染抽查，
命令与 DPI 选择见 `~/.zcode/memory/office-doc-toolchain.md`。

## 高频错误速查

| 症状 | 原因 | 处理 |
|---|---|---|
| 删多了、表格数变少 | 插入后用漂移的新索引定位删除 | 只用第 2 步索引 + `id(elem)` |
| 填错表格 | `doc.tables` 顺序与正文顺序不一致 | 用索引映射的 tbl_idx |
| 新段落字体没变 | 格式写进了 `w:pPr` 而不是 run 的 `w:rPr` | 见 make_para，rPr 在 w:r 内 |
| `UnrecognizedImageError` | 相机直出 JPEG | 转 PNG 再插 |
| `EBUSY: resource busy or locked` | 用户开着同名文件 | 换名输出，别让用户关文件 |
| soffice 无输出无报错 | 中文文件名/路径 | 先 cp 成 ASCII 文件名 |
| 尾部内容没删干净 | 末段边界默认到了文档末尾 | 显式找边界标记再定终点 |
