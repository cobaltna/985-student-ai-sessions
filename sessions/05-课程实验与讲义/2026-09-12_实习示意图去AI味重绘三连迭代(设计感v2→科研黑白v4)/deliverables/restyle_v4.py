# -*- coding: utf-8 -*-
"""5 张示意图重制 v4 —— 严谨科研论文插图风。

风格规约（用户 2026-09-13 确认）：
  · 只用黑白灰：块体浅灰填充 + 细实线描边，无圆角、无阴影、无渐变、无装饰线条
  · 强调靠明度与字重（关键数据加粗近黑），不用色相
  · 主线 = 实线框 + 实线箭头；支线（副产物）= 虚线框 + 虚线箭头
  · 图内无大标题：标题移到图下，期刊式「图 N　标题」+「注：…」
  · 字体：黑体 SimHei（中文期刊插图标配）
  · 输出 PNG(300dpi) + SVG 双份，并做文字越界校验
"""
from pathlib import Path
import math
import re
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib import ft2font
from matplotlib.patches import Rectangle, Polygon, Wedge
from matplotlib.font_manager import FontProperties

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '修改版_v4'
OUT.mkdir(exist_ok=True)

FONT_PATH = 'C:/Windows/Fonts/simhei.ttf'
plt.rcParams['svg.fonttype'] = 'path'
plt.rcParams['axes.unicode_minus'] = False

# ── 中性阶：层次靠灰度与字号，不靠色相 ───────────────────────────────
INK = '#1A1A1A'          # 主文字
INK_2 = '#454545'        # 次级文字
INK_3 = '#6E6E6E'        # 注释 / 脚注
EDGE = '#2E2E2E'         # 主线块描边
EDGE_2 = '#8A8A8A'       # 支线块描边
FILL = '#F2F2F2'         # 主线块填充
FILL_2 = '#FBFBFB'       # 支线块填充
FILL_HDR = '#DCDCDC'     # 阶段头填充
HAIR = '#CFCFCF'         # 表格细线
ARROW = '#5A5A5A'        # 箭头

# ── 强调：只用黑白灰，靠明度 + 字重分级，不用色相 ────────────────────
EMPH = '#111111'         # 关键数据 / 关键节点（近黑）

# ── 线宽 / 字号（统一刻度，期刊插图要求线宽一致）────────────────────
LW_BLOCK = 0.8           # 主线块
LW_SUB = 0.6             # 支线块（虚线）
LW_ARROW = 0.9
LW_HAIR = 0.7
FS_BLOCK = 11.5
FS_SUB = 10.0
FS_LBL = 9.5             # 分栏小标签
FS_HDR = 14.0            # 阶段头
FS_NUM = 9.5             # 阶段编号
FS_CAP = 11.0            # 图注标题
FS_NOTE = 8.5            # 图注 / 脚注

X0, X1 = 0.60, 9.60      # 内容左右边界
BODY = (X0 + X1) / 2     # 视觉中线

F_R = FontProperties(fname=FONT_PATH)                  # 黑体（中文）
F_A = FontProperties(fname='C:/Windows/Fonts/arial.ttf')  # Arial（纯拉丁/数字）
BOLD_LW = 0.42           # 伪粗体描边线宽
CJK = re.compile(r'[\u2010-\u203b\u2190-\u21ff\u3000-\u303f\u4e00-\u9fff'
                 r'\uff00-\uffef]')
checks = []              # (text_artist, fig, box|None)


def _boldfx(color):
    """黑体无粗体字重，用同色描边等效加粗（白色字便用白色描边）。"""
    return [pe.withStroke(linewidth=BOLD_LW, foreground=color)]


def font_of(s):
    """含中文（含全角标点/箭头）用黑体，纯拉丁数字用 Arial（黑体的句点间距过大）。"""
    return F_R if CJK.search(s) else F_A


_FT = {}


def text_w(s, fp, size):
    """字符串的前进宽度，换算为坐标单位（1 坐标单位 = 1 英寸 = 72 pt）。

    用 FT2Font 的真实 advance 而非 TextPath 的墨迹包围盒——否则全角空格
    （U+3000）与行尾空格的宽度会被算成 0，中英混排时字距被吃掉。
    """
    f = _FT.get(fp.get_file())
    if f is None:
        f = _FT[fp.get_file()] = ft2font.FT2Font(fp.get_file())
    f.set_size(size, 72)
    f.set_text(s, 0, flags=ft2font.LoadFlags.NO_HINTING)
    return f.get_width_height()[0] / 64 / 72


def canvas(w, h):
    fig = plt.figure(figsize=(w, h), dpi=100, facecolor='white')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set(xlim=(0, w), ylim=(h, 0))
    ax.axis('off')
    return fig, ax


def T(ax, x, y, s, size=FS_BLOCK, ha='left', va='center', color=INK, ls=1.55,
      bold=False):
    t = ax.text(x, y, s, fontsize=size, fontproperties=font_of(s), ha=ha, va=va,
                color=color, linespacing=ls, zorder=5,
                path_effects=_boldfx(color) if bold else None)
    checks.append((t, ax.figure, None))
    return t


def mt(ax, x, y, parts, size=FS_BLOCK, ha='center', color=INK, gap=0.02,
       bold=False):
    """混排一行：parts = [(文字, 字体), …]，中英各自用对的字体，按量测宽度排布。"""
    ws = [text_w(s, fp, size) for s, fp in parts]
    total = sum(ws) + gap * (len(parts) - 1)
    cur = x if ha == 'left' else (x - total if ha == 'right'
                                  else x - total / 2)
    for (s, fp), w in zip(parts, ws):
        t = ax.text(cur, y, s, fontsize=size, fontproperties=fp, ha='left',
                    va='center', color=color, zorder=5,
                    path_effects=_boldfx(color) if bold else None)
        checks.append((t, ax.figure, None))
        cur += w + gap


def fit(ax, x, y, w, h, s, size=FS_BLOCK, color=INK, ls=1.55):
    """块内居中文字 + 越界登记。"""
    t = T(ax, x + w / 2, y + h / 2, s, size, ha='center', color=color, ls=ls)
    checks[-1] = (t, ax.figure, (x, y, w, h))
    return t


def blk(ax, x, y, w, h, fill=FILL, edge=EDGE, lw=LW_BLOCK, dashed=False):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=fill, edgecolor=edge,
                           linewidth=lw, zorder=2,
                           linestyle=(0, (3.2, 2.2)) if dashed else 'solid'))


def head(ax, x, y, w, h, num, name):
    """阶段头：深一阶灰底 + 细描边；序号退到次级灰，名称加粗——无任何装饰线条。"""
    blk(ax, x, y, w, h, FILL_HDR, EDGE, LW_BLOCK)
    cx = x + w / 2
    T(ax, cx, y + h / 2 - 0.15, num, FS_NUM, ha='center', color=INK_3)
    T(ax, cx, y + h / 2 + 0.17, name, FS_HDR, ha='center', color=INK, bold=True)


def arrow(ax, p1, p2, color=ARROW, lw=LW_ARROW, dashed=False, scale=0.085):
    """直线箭头：细杆 + 实心三角头（几何绘制，避免描边式箭头尖发虚）。"""
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    L = math.hypot(dx, dy)
    if L < 1e-6:
        return
    ux, uy = dx / L, dy / L
    hd = min(scale, L * 0.55)
    half = hd * 0.42
    back = (p2[0] - ux * hd, p2[1] - uy * hd)
    ln, = ax.plot([p1[0], back[0]], [p1[1], back[1]], color=color, lw=lw,
                  solid_capstyle='butt', zorder=3)
    if dashed:
        ln.set_linestyle((0, (3.0, 2.2)))
    ax.add_patch(Polygon([p2, (back[0] - uy * half, back[1] + ux * half),
                          (back[0] + uy * half, back[1] - ux * half)],
                         facecolor=color, edgecolor='none', zorder=3))


def elbow(ax, pts, color=ARROW, lw=LW_ARROW, dashed=False, scale=0.085):
    """折线箭头：逐段折线，末段加三角头。"""
    for i in range(len(pts) - 2):
        ax.plot([pts[i][0], pts[i + 1][0]], [pts[i][1], pts[i + 1][1]],
                color=color, lw=lw, solid_capstyle='butt',
                solid_joinstyle='miter', zorder=3,
                linestyle=(0, (3.0, 2.2)) if dashed else 'solid')
    arrow(ax, pts[-2], pts[-1], color, lw, dashed, scale)


def rule(ax, y, x0=X0, x1=X1, color=HAIR, lw=LW_HAIR):
    ax.plot([x0, x1], [y, y], color=color, lw=lw, solid_capstyle='butt', zorder=1)


def caption(ax, y, num, title, notes=()):
    """期刊式图注：「图 N　标题」居中，注文左对齐置于其下。"""
    mt(ax, BODY, y, [(f'图 {num}　', F_R), (title, F_R)], FS_CAP, ha='center',
       color=INK, bold=True)
    yy = y + 0.40
    for n in notes:
        T(ax, X0, yy, n, FS_NOTE, color=INK_3)
        yy += 0.30
    return yy


def save(fig, name):
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    for t, f, box in checks:
        if f is not fig:
            continue
        b = t.get_window_extent(r)
        (ax0, ay0), (ax1, ay1) = t.axes.transData.inverted().transform(
            [[b.x0, b.y0], [b.x1, b.y1]])
        tx0, tx1 = min(ax0, ax1), max(ax0, ax1)
        ty0, ty1 = min(ay0, ay1), max(ay0, ay1)
        assert (fig.bbox.x0 <= b.x0 and b.x1 <= fig.bbox.x1
                and fig.bbox.y0 <= b.y0 and b.y1 <= fig.bbox.y1), \
            f'文字越出画布: {t.get_text()!r}'
        if box is None:
            continue
        x, y, w, h = box
        assert (tx0 >= x - 1e-6 and tx1 <= x + w + 1e-6
                and ty0 >= y - 1e-6 and ty1 <= y + h + 1e-6), \
            (f'文字溢出块: {t.get_text()!r}  '
             f'text=({tx0:.3f},{ty0:.3f})-({tx1:.3f},{ty1:.3f})  '
             f'box=({x:.3f},{y:.3f})-({x + w:.3f},{y + h:.3f})')
    written = []
    for suffix, kw in (('.png', dict(dpi=300)), ('.svg', {})):
        path = OUT / f'{name}{suffix}'
        written.append(_savefig(fig, path, **kw))
    plt.close(fig)
    retry = f'（{written[0]} 次重试）' if written[0] > 1 else ''
    print(f'  {name}  PNG(300dpi) + SVG  边界校验通过{retry}')


def _savefig(fig, path, attempts=8, wait=0.5, **kw):
    """写盘并容忍 Windows 上查看器/索引器造成的瞬时占用（OSError 22 / 13）。

    保存目标常被刚刚打开过的看图进程短暂持句柄，重试即可；超限才真报错。
    """
    for i in range(attempts):
        try:
            fig.savefig(path, facecolor='white', **kw)
            return i + 1
        except OSError as exc:
            if exc.errno not in (13, 22) or i == attempts - 1:
                raise
            time.sleep(wait)
    raise AssertionError('unreachable')


# ══════════════════════════════════════════════════════════════════
# 图 1  联合收获机作业工艺流程
# ══════════════════════════════════════════════════════════════════
def combine():
    W = 10.2
    n, gap = 5, 0.30
    w = (X1 - X0 - gap * (n - 1)) / n
    pitch = w + gap
    h = 0.84

    y1, y2 = 0.92, 2.62
    yc, hc = 3.95, 1.02
    capy = 5.55
    H = 6.95
    fig, ax = canvas(W, H)

    T(ax, X0, 0.55, '物料主流程：割台 → 脱粒 → 分离 → 清选 → 集粮',
      FS_LBL, color=INK_2)

    row1 = ['分禾、拨禾\n（拨禾轮）', '切割器切割', '割台搅龙输送',
            '倾斜输送\n（过桥）', '脱粒\n（滚筒＋凹板）']
    row2 = ['分离\n（逐稿器/轴流）', '清选\n（风机＋振动筛）', '粮箱集粮', '卸粮装车']

    for i, item in enumerate(row1):
        x = X0 + i * pitch
        crit = (i == len(row1) - 1)                 # 脱粒 = 关键节点，加粗框线
        blk(ax, x, y1, w, h, FILL, EMPH if crit else EDGE,
            1.25 if crit else LW_BLOCK)
        fit(ax, x, y1, w, h, item)
        if i < len(row1) - 1:
            arrow(ax, (x + w + 0.03, y1 + h / 2), (x + pitch - 0.03, y1 + h / 2))

    for i, item in enumerate(row2):
        x = X0 + i * pitch
        blk(ax, x, y2, w, h, FILL, EDGE, LW_BLOCK)
        fit(ax, x, y2, w, h, item)
        if i < len(row2) - 1:
            arrow(ax, (x + w + 0.03, y2 + h / 2), (x + pitch - 0.03, y2 + h / 2))

    # 脱粒 → 分离：主线回流（物料下行），灰实线折线
    xe, xs = X0 + 4 * pitch + w / 2, X0 + w / 2
    elbow(ax, [(xe, y1 + h), (xe, 2.16), (xs, 2.16), (xs, y2)])

    # 副产物去向：支线（虚线框 + 虚线箭头）
    T(ax, X1, 3.58, '副产物去向', FS_LBL, ha='right', color=INK_2)
    cards = [('茎秆', '切碎抛撒还田\n或集草打捆离田', 0, 1.56, True),
             ('杂余', '经复脱装置\n返回脱粒滚筒再脱', 1, 1.56, True),
             ('茎秆与杂余进入秸秆综合利用环节',
              '（肥料化、饲料化、燃料化等，见第六章）', 2, 5.34, False)]
    for title, body, ci, cw, down in cards:
        x = X0 + ci * pitch
        blk(ax, x, yc, cw, hc, FILL_2, EDGE_2, LW_SUB, dashed=True)
        if down:
            arrow(ax, (x + cw / 2, y2 + h), (x + cw / 2, yc - 0.02),
                  EDGE_2, LW_SUB, dashed=True, scale=0.075)
            T(ax, x + cw / 2, yc + 0.30, title, FS_BLOCK, ha='center')
            T(ax, x + cw / 2, yc + 0.68, body, FS_SUB, ha='center', color=INK_2)
        else:
            T(ax, x + 0.30, yc + 0.34, title, FS_BLOCK)
            T(ax, x + 0.30, yc + 0.72, body, FS_SUB, color=INK_2)

    caption(ax, capy, 1, '联合收获机作业工艺流程', [
        '注：逐稿器式（切流脱粒＋键式逐稿器）与轴流式（切流/单纵轴流）为两类主流脱粒分离方案；',
        '割茬高度、前进速度、滚筒转速、风机风量与筛片开度共同决定收获损失率与含杂率。'])
    save(fig, 'fig_combine_flow')


# ══════════════════════════════════════════════════════════════════
# 图 2  全程农机作业托管服务流程
# ══════════════════════════════════════════════════════════════════
def service():
    W = 10.2
    hd_w, hd_h = 1.95, 0.98
    sx, gap = 2.85, 0.24
    span = X1 - sx
    y0, pitch = 0.55, 1.34
    capy = 4.72
    H = 5.35
    fig, ax = canvas(W, H)

    rows = [('01', '服务前端',
             ['农户、村集体\n签约土地托管', '地块测绘、\n作业与农艺方案',
              '农资集中采购\n与统一供应']),
            ('02', '全程作业',
             ['耕整地', '精量播种', '田间管理', '机械收获', '秸秆处理']),
            ('03', '产后服务',
             ['粮食烘干\n与仓储', '统一销售\n（订单收购）', '作业结算\n与收益分配'])]

    for ri, (num, name, steps) in enumerate(rows):
        y = y0 + ri * pitch
        head(ax, X0, y, hd_w, hd_h, num, name)
        if ri < len(rows) - 1:
            arrow(ax, (X0 + hd_w / 2, y + hd_h), (X0 + hd_w / 2, y + pitch))
        sw = (span - gap * (len(steps) - 1)) / len(steps)
        for si, s in enumerate(steps):
            x = sx + si * (sw + gap)
            blk(ax, x, y, sw, hd_h, FILL, EDGE, LW_BLOCK)
            fit(ax, x, y, sw, hd_h, s)
            if si < len(steps) - 1:
                arrow(ax, (x + sw + 0.02, y + hd_h / 2),
                      (x + sw + gap - 0.02, y + hd_h / 2))

    caption(ax, capy, 2, '全程农机作业托管服务流程')
    save(fig, 'fig_service_flow')


# ══════════════════════════════════════════════════════════════════
# 图 3  农作物秸秆综合利用途径（扇形图 + 图例表）
# ══════════════════════════════════════════════════════════════════
def straw():
    W = 10.2
    CX, CY, R = 2.80, 2.85, 1.75          # 扇形圆心 / 半径
    SWX, NWX, PX = 5.30, 5.62, X1         # 图例色块 / 名称 / 比例 三列
    SW, RY0, RP = 0.20, 1.00, 0.68        # 色块边长 / 首行 y / 行距
    capy, H = 5.30, 6.35
    fig, ax = canvas(W, H)

    # 五个扇区：灰阶按占比降序取深浅（越大越深），与色相无关
    #   (名称, 占比, 填充, 文字色, 说明文字)
    sv = [('肥料化', 57.6, '#2b2b2b', '#ffffff', '粉碎直接还田、堆沤腐熟还田'),
          ('饲料化', 20.7, '#5e5e5e', '#ffffff', '青贮、黄贮、打捆饲喂牛羊'),
          ('燃料化', 8.3, '#c0c0c0', '#111111', '成型颗粒、直燃发电、沼气'),
          ('原料化＋基料化', 1.5, '#e6e6e6', '#111111', None),
          ('未利用', 11.9, '#909090', '#111111', '（未纳入上述五类利用途径）')]

    tot = sum(v for _, v, _, _, _ in sv)
    assert abs(tot - 100.0) < 1e-9, f'扇区占比合计 {tot}，不是 100%'

    # ── 扇形：自 12 点起顺时针；画布 y 轴向下，故起始角取 270 并递增 ──
    a0 = 270.0
    mids = []
    for name, v, fill, tc, _ in sv:
        sweep = v / tot * 360.0
        ax.add_patch(Wedge((CX, CY), R, a0, a0 + sweep, facecolor=fill,
                           edgecolor='#ffffff', linewidth=1.0, zorder=2))
        mids.append((name, v, tc, a0 + sweep / 2, sweep))
        a0 += sweep

    for name, v, tc, mid, sweep in mids:
        rad = math.radians(mid)
        ux, uy = math.cos(rad), math.sin(rad)
        if sweep >= 25.0:                       # 够宽：数值直接落在扇区内
            T(ax, CX + ux * R * 0.64, CY + uy * R * 0.64, f'{v}%', FS_BLOCK,
              ha='center', color=tc, bold=True)
        else:                                   # 过窄：引线拉到圆外标注
            ax.plot([CX + ux * R * 1.02, CX + ux * R * 1.20],
                    [CY + uy * R * 1.02, CY + uy * R * 1.20],
                    color=EDGE_2, lw=LW_SUB, solid_capstyle='butt', zorder=4)
            T(ax, CX + ux * R * 1.32, CY + uy * R * 1.32, f'{v}%', FS_BLOCK,
              ha='center', color=EMPH, bold=True)

    # ── 图例表 ──────────────────────────────────────────────────────
    T(ax, NWX, 0.50, '利用途径', FS_LBL, color=INK_2)
    T(ax, PX, 0.50, '占秸秆总产生量比例', FS_LBL, ha='right', color=INK_2)
    rule(ax, 0.74, SWX, X1)

    legend = [('肥料化', '粉碎直接还田、堆沤腐熟还田', 57.6, '#2b2b2b'),
              ('饲料化', '青贮、黄贮、打捆饲喂牛羊', 20.7, '#5e5e5e'),
              ('燃料化', '成型颗粒、直燃发电、沼气', 8.3, '#c0c0c0'),
              ('原料化', '造纸、人造板、生物基材料', None, '#e6e6e6'),
              ('基料化', '食用菌栽培基质、菌糠还田', None, '#e6e6e6'),
              ('未利用', '（未纳入上述五类利用途径）', 11.9, '#909090')]

    for i, (name, desc, pct, fill) in enumerate(legend):
        ry = RY0 + i * RP
        if name not in ('原料化', '基料化'):     # 这两行共用色块与占比，见下
            blk(ax, SWX, ry - SW / 2, SW, SW, fill, EDGE_2, LW_SUB)
            T(ax, PX, ry, f'{pct}%', FS_BLOCK, ha='right', color=EMPH, bold=True)
        T(ax, NWX, ry, name, FS_BLOCK)
        T(ax, NWX, ry + 0.30, desc, FS_NOTE + 1.0, color=INK_2)

    # 原料化＋基料化 是同一个扇区：色块竖向合并，占比跨两行居中
    blk(ax, SWX, RY0 + 3 * RP - SW / 2, SW, RP + SW, '#e6e6e6', EDGE_2, LW_SUB)
    mt(ax, PX, RY0 + 3.5 * RP, [('两项合计 ', F_R), ('1.5%', F_A)], FS_BLOCK,
       ha='right', color=EMPH, bold=True)

    rule(ax, RY0 + 5 * RP + 0.52, SWX, X1)
    caption(ax, capy, 3, '农作物秸秆综合利用途径', [
        '注：比例为全国口径（2024年），以秸秆总产生量为基数；五类利用途径合计 88.1%，余 11.9% 为未利用部分；',
        '　　北京市秸秆综合利用率保持在99%以上，以肥料化利用为主。'])
    save(fig, 'fig_straw_util')


# ══════════════════════════════════════════════════════════════════
# 图 4 / 图 5  装配工艺流程（三阶段并列）
# ══════════════════════════════════════════════════════════════════
def assembly(name, num, cap, cols, capnote=None):
    W = 10.2
    n, gap = 3, 0.42
    cw = (X1 - X0 - gap * (n - 1)) / n
    hd_h, sh, vg = 0.62, 0.60, 0.26
    hy, top = 0.55, 1.45
    pitch = sh + vg
    tallest = max(len(s) for _, s in cols)
    bottom = top + tallest * sh + (tallest - 1) * vg
    capy = bottom + 0.52
    H = capy + (0.35 if not capnote else 0.75) + 0.30

    fig, ax = canvas(W, H)
    colx = [X0 + ci * (cw + gap) for ci in range(n)]

    for ci, (col, steps) in enumerate(cols):
        label = col.split('、', 1)[1] if '、' in col else col
        x = colx[ci]
        head(ax, x, hy, cw, hd_h, f'{ci + 1:02}', label)

        for si, s in enumerate(steps):
            y = top + si * pitch
            blk(ax, x, y, cw, sh, FILL, EDGE, LW_BLOCK)
            fit(ax, x, y, cw, sh, s, ls=1.42)
            if si < len(steps) - 1:
                arrow(ax, (x + cw / 2, y + sh), (x + cw / 2, y + pitch),
                      scale=0.078)

        # 跨阶段衔接：本列末块 → 下一列首块（正交折线，始终落在块上）
        if ci < n - 1:
            y_here = top + (len(steps) - 1) * pitch + sh / 2
            y_next = top + sh / 2
            mx = x + cw + gap / 2
            arrow(ax, (x + cw, y_here), (mx + 0.01, y_here), scale=0.072)
            ax.plot([mx, mx], [y_here, y_next], color=ARROW, lw=LW_ARROW,
                    solid_capstyle='butt', zorder=3)
            arrow(ax, (mx, y_next), (colx[ci + 1] - 0.01, y_next), scale=0.072)

    caption(ax, capy, num, cap, [capnote] if capnote else [])
    save(fig, name)


def main():
    print('渲染中：')
    combine()
    service()
    straw()
    assembly('fig_tractor_flow', 4, '拖拉机装配工艺流程', [
        ('一、部件准备与部装', ['零部件入厂检验', '底盘机架上线\n（定位、找正）',
                               '前桥、后桥与\n传动系部装', '发动机总成部装\n（含后处理系统）']),
        ('二、总装装配', ['发动机与底盘合装', '变速箱/CVT、液压\n系统装配',
                         '驾驶室与操纵\n机构装配', '电气线束、仪表\n与传感器装配',
                         '轮胎、配重与\n工作装置装配']),
        ('三、检测与出厂', ['油液加注、启动\n与磨合运转',
                           '整机性能检测\n（PTO、液压提升）',
                           '涂装补漆、标识\n与铭牌', '出厂检验、包装\n与发运'])])
    assembly('fig_harvester_flow', 5, '联合收获机装配工艺流程', [
        ('一、部件准备与部装', ['零部件配套\n与入厂检验', '脱粒机体\n（机架）上线',
                               '脱粒分离装置装配\n（滚筒、凹板、逐稿器）',
                               '清选装置装配\n（筛箱、风机、抖动板）']),
        ('二、总装装配', ['割台与拨禾轮\n（摘穗台）装配', '输送槽（过桥）\n与喂入装置装配',
                         '发动机与传动\n系统合装', '粮箱与卸粮\n搅龙装配',
                         '驾驶室、操纵\n与电气装配', '行走底盘装配\n（轮式/履带）']),
        ('三、调试与出厂', ['整机空运转与磨合', '性能试验（喂入、\n脱粒、清选、损失率）',
                           '涂装、标识与\n安全装置检查', '出厂检验、包装\n与发运'])])
    print(f'输出目录：{OUT}')


if __name__ == '__main__':
    main()
