# -*- coding: utf-8 -*-
"""5 张示意图重制 v3。

设计约束：
  · 只用 3 个语义色（松绿 / 黛蓝 / 赭石），颜色 = 阶段或类别，不做装饰性着色
  · 无渐变、无彩色描边、无大圆角；块=浅色填充，阶段头=实色填充白字
  · 层次靠字号 / 灰度 / 留白，不靠颜色数量
  · 字体：等线（DengXian），标题 Bold
"""
from pathlib import Path
import ast
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.font_manager import FontProperties

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '修改版_v3'
OUT.mkdir(exist_ok=True)

F_R = FontProperties(fname='C:/Windows/Fonts/Deng.ttf')
F_B = FontProperties(fname='C:/Windows/Fonts/Dengb.ttf')
plt.rcParams['svg.fonttype'] = 'path'

# ── 语义色：三阶递进（前段 / 中段 / 后段） ──────────────────────────
PINE, PINE_L = '#2F5D4E', '#E7EFEB'
SLATE, SLATE_L = '#3E5A6E', '#E8EEF2'
CLAY, CLAY_L = '#A85D3C', '#F6E9E2'
SAND = '#F6F1E2'

# ── 中性阶 ────────────────────────────────────────────────────────
INK, INK_SOFT, INK_FAINT = '#23282A', '#5F6B6A', '#8B9694'
HAIR, ARROW, TRACK = '#E4E8E6', '#9EA9A7', '#EFF2F1'

X0, X1 = 0.55, 9.65          # 内容左右边界
texts, blockchecks = [], []


def canvas(w, h):
    fig = plt.figure(figsize=(w, h), dpi=100, facecolor='white')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set(xlim=(0, w), ylim=(h, 0))
    ax.axis('off')
    return fig, ax


def T(ax, x, y, s, size=12, ha='left', va='center', bold=False,
      color=INK, ls=1.5, alpha=1.0):
    t = ax.text(x, y, s, fontsize=size, fontproperties=F_B if bold else F_R,
                ha=ha, va=va, color=color, linespacing=ls, zorder=5, alpha=alpha)
    texts.append((t, ax.figure))
    return t


def blk(ax, x, y, w, h, fill, r=0.05):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle=f'round,pad=0,rounding_size={r}',
                                linewidth=0, edgecolor='none', facecolor=fill, zorder=2))


def arr(ax, p1, p2, color=ARROW, lw=0.9, scale=9):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle='-|>', mutation_scale=scale,
                                 linewidth=lw, color=color,
                                 shrinkA=0, shrinkB=0, zorder=3))


def poly(ax, pts, color=ARROW, lw=0.9):
    ax.plot([p[0] for p in pts], [p[1] for p in pts], color=color, lw=lw,
            solid_capstyle='butt', solid_joinstyle='miter', zorder=3)


def rule(ax, y, x0=X0, x1=X1, color=HAIR, lw=0.8):
    ax.plot([x0, x1], [y, y], color=color, lw=lw, solid_capstyle='butt', zorder=1)


def head(ax, title, y=0.40):
    """标题 + 主色起笔的细分隔线（不整条上色，克制）。"""
    T(ax, X0, y, title, 17.5, bold=True, ls=1.2)
    rule(ax, y + 0.31, X0, X0 + 0.60, PINE, 2.2)
    rule(ax, y + 0.31, X0 + 0.72, X1, HAIR, 0.8)


def fit(ax, x, y, w, h, s, size=12.5, color=INK, ls=1.5):
    """在块内居中添加文字并记录越界校验。"""
    t = T(ax, x + w / 2, y + h / 2, s, size, ha='center', color=color, ls=ls)
    blockchecks.append((t, ax.figure, (x, y, w, h)))
    return t


def save(fig, name):
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    for t, f, box in blockchecks:
        if f is not fig:
            continue
        b = t.get_window_extent(r)
        (ax0, ay0), (ax1, ay1) = t.axes.transData.inverted().transform(
            [[b.x0, b.y0], [b.x1, b.y1]])
        x, y, w, h = box
        ok = (min(ax0, ax1) >= x - 1e-6 and max(ax0, ax1) <= x + w + 1e-6
              and min(ay0, ay1) >= y - 1e-6 and max(ay0, ay1) <= y + h + 1e-6)
        assert ok, (f'文字溢出块: {t.get_text()!r}  '
                    f'text=({min(ax0, ax1):.3f},{min(ay0, ay1):.3f})-'
                    f'({max(ax0, ax1):.3f},{max(ay0, ay1):.3f})  '
                    f'box=({x:.3f},{y:.3f})-({x + w:.3f},{y + h:.3f})')
    for t, f in texts:
        if f is not fig:
            continue
        b = t.get_window_extent(r)
        assert (fig.bbox.x0 <= b.x0 and b.x1 <= fig.bbox.x1
                and fig.bbox.y0 <= b.y0 and b.y1 <= fig.bbox.y1), \
            f'文字越出画布: {t.get_text()!r}'
    fig.savefig(OUT / f'{name}.png', dpi=230, facecolor='white')
    fig.savefig(OUT / f'{name}.svg', facecolor='white')
    plt.close(fig)
    print(f'{name}: PNG + SVG  边界校验通过')


# ══════════════════════════════════════════════════════════════════
# 1 / 5  联合收获机作业工艺流程
# ══════════════════════════════════════════════════════════════════
def combine():
    W, H = 10.2, 6.50
    fig, ax = canvas(W, H)
    head(ax, '联合收获机作业工艺流程')
    T(ax, X0, 1.02, '物料主流程：割台 → 脱粒 → 分离 → 清选 → 集粮',
      11.5, color=INK_SOFT)

    n, gap = 5, 0.30
    w = (X1 - X0 - gap * (n - 1)) / n          # 1.58
    pitch = w + gap                             # 1.88
    y1, y2, h = 1.42, 2.86, 0.82

    row1 = ['分禾、拨禾\n（拨禾轮）', '切割器切割', '割台搅龙输送',
            '倾斜输送\n（过桥）', '脱粒\n（滚筒+凹板）']
    row2 = ['分离\n（逐稿器/轴流）', '清选\n（风机+振动筛）', '粮箱集粮', '卸粮装车']
    c1 = [PINE_L] * 4 + [SLATE_L]
    c2 = [SLATE_L, SLATE_L, CLAY_L, CLAY_L]

    for y, items, cols in ((y1, row1, c1), (y2, row2, c2)):
        for i, (item, col) in enumerate(zip(items, cols)):
            x = X0 + i * pitch
            blk(ax, x, y, w, h, col)
            fit(ax, x, y, w, h, item, 12.5)
            if i < len(items) - 1:
                arr(ax, (x + w + 0.03, y + h / 2), (x + pitch - 0.03, y + h / 2))

    # 脱粒 → 分离：折线回流
    xe, xs = X0 + 4 * pitch + w / 2, X0 + w / 2
    poly(ax, [(xe, y1 + h), (xe, 2.42), (xs, 2.42)])
    arr(ax, (xs, 2.42), (xs, y2))

    # 副产物去向
    cards = [('茎秆', '切碎抛撒还田\n或集草打捆离田', 0, 1.58, 'center'),
             ('杂余', '经复脱装置\n返回脱粒滚筒再脱', 1, 1.58, 'center'),
             ('茎秆与杂余进入秸秆综合利用环节',
              '（肥料化、饲料化、燃料化等，见第六章）', 2, 5.34, 'left')]
    for title, body, ci, cw, align in cards:
        x = X0 + ci * pitch
        blk(ax, x, 4.10, cw, 0.95, SAND)
        if align == 'center':
            arr(ax, (x + cw / 2, y2 + h), (x + cw / 2, 4.10))
            T(ax, x + cw / 2, 4.42, title, 12.5, ha='center', bold=True)
            T(ax, x + cw / 2, 4.74, body, 11, ha='center', color=INK_SOFT)
        else:
            T(ax, x + 0.35, 4.42, title, 12.5, bold=True)
            T(ax, x + 0.35, 4.74, body, 11, color=INK_SOFT)

    rule(ax, 5.55)
    T(ax, X0, 5.84, '说明：逐稿器式（切流脱粒＋键式逐稿器）与轴流式（切流/单纵轴流）为两类主流脱粒分离方案；',
      10.5, color=INK_SOFT)
    T(ax, X0, 6.16, '割茬高度、前进速度、滚筒转速、风机风量与筛片开度共同决定收获损失率与含杂率。',
      10.5, color=INK_SOFT)
    save(fig, 'fig_combine_flow')


# ══════════════════════════════════════════════════════════════════
# 2 / 5  全程农机作业托管服务流程
# ══════════════════════════════════════════════════════════════════
def service():
    W, H = 10.2, 5.02
    fig, ax = canvas(W, H)
    head(ax, '全程农机作业托管服务流程')

    rows = [('服务前端', PINE, PINE_L,
             ['农户、村集体\n签约土地托管', '地块测绘、\n作业与农艺方案', '农资集中采购\n与统一供应']),
            ('全程作业', SLATE, SLATE_L,
             ['耕整地', '精量播种', '田间管理', '机械收获', '秸秆处理']),
            ('产后服务', CLAY, CLAY_L,
             ['粮食烘干\n与仓储', '统一销售\n（订单收购）', '作业结算\n与收益分配'])]

    lw_, lh_ = 1.95, 0.98
    sx, span, gap = 2.72, X1 - 2.72, 0.24
    y0, pitch = 1.12, 1.32

    for ri, (name, solid, tint, steps) in enumerate(rows):
        y = y0 + ri * pitch
        blk(ax, X0, y, lw_, lh_, solid)
        T(ax, X0 + 0.30, y + 0.30, f'{ri + 1:02}', 10.5,
          color='white', alpha=0.62, bold=True)
        T(ax, X0 + 0.30, y + 0.66, name, 15, bold=True, color='white')
        if ri < 2:
            arr(ax, (X0 + lw_ / 2, y + lh_), (X0 + lw_ / 2, y + pitch))

        sw = (span - gap * (len(steps) - 1)) / len(steps)
        for si, s in enumerate(steps):
            x = sx + si * (sw + gap)
            blk(ax, x, y, sw, lh_, tint)
            fit(ax, x, y, sw, lh_, s, 12.5)
            if si < len(steps) - 1:
                arr(ax, (x + sw + 0.02, y + lh_ / 2), (x + sw + gap - 0.02, y + lh_ / 2))
    save(fig, 'fig_service_flow')


# ══════════════════════════════════════════════════════════════════
# 3 / 5  农作物秸秆综合利用途径
# ══════════════════════════════════════════════════════════════════
def straw():
    W, H = 10.2, 5.72
    fig, ax = canvas(W, H)
    head(ax, '农作物秸秆综合利用途径')

    CB, LB, BW = 6.35, 9.65, 2.35          # 比例条列 / 数字右对齐 / 条最大长
    T(ax, X0, 1.15, '利用途径', 11.5, bold=True, color=INK_SOFT)
    T(ax, 2.10, 1.15, '主要利用方式', 11.5, bold=True, color=INK_SOFT)
    T(ax, CB, 1.15, '占秸秆利用量比例', 11.5, bold=True, color=INK_SOFT)
    rule(ax, 1.38)

    items = [('肥料化', '粉碎直接还田、堆沤腐熟还田', 57.6),
             ('饲料化', '青贮、黄贮、打捆饲喂牛羊', 20.7),
             ('燃料化', '成型颗粒、直燃发电、沼气', 8.3),
             ('原料化', '造纸、人造板、生物基材料', None),
             ('基料化', '食用菌栽培基质、菌糠还田', None)]
    rc0, rp = 1.95, 0.66
    k = BW / 57.6

    for i, (name, desc, pct) in enumerate(items):
        rc = rc0 + i * rp
        T(ax, X0, rc, name, 14, bold=True)
        T(ax, 2.10, rc, desc, 12.5, color=INK_SOFT)
        if pct is None:
            continue
        blk(ax, CB, rc - 0.09, BW, 0.18, TRACK, r=0.09)
        blk(ax, CB, rc - 0.09, max(pct * k, 0.10), 0.18, PINE, r=0.09)
        T(ax, LB, rc, f'{pct}%', 14, ha='right', bold=True, color=PINE)

    # 原料化 + 基料化 两项合计，合并单元格（对齐后两行）
    blk(ax, CB, 3.63, LB - CB, 1.26, PINE_L, r=0.06)
    T(ax, (CB + LB) / 2, 4.26, '两项合计约 1.5%', 13, ha='center', bold=True, color=PINE)

    rule(ax, 5.18)
    T(ax, X0, 5.45, '注：比例为全国口径（2024年）；北京市秸秆综合利用率保持在99%以上，以肥料化利用为主。',
      10.5, color=INK_SOFT)
    save(fig, 'fig_straw_util')


# ══════════════════════════════════════════════════════════════════
# 4·5 / 5  拖拉机 / 联合收获机 装配工艺流程
# ══════════════════════════════════════════════════════════════════
def assembly(name, caption, cols):
    n, gap = 3, 0.42
    cw = (X1 - X0 - gap * (n - 1)) / n
    hy, hh = 1.00, 0.62
    sh, vg = 0.60, 0.24
    pitch = sh + vg
    top = 1.90                                   # 列内首块顶边
    tallest = max(len(s) * sh + (len(s) - 1) * vg for _, s in cols)

    W, H = 10.2, top + tallest + 0.42            # 画布随最高列自适应
    fig, ax = canvas(W, H)
    head(ax, caption)

    solids = (PINE, SLATE, CLAY)
    tints = (PINE_L, SLATE_L, CLAY_L)

    for ci, (col, steps) in enumerate(cols):
        label = col.split('、', 1)[1] if '、' in col else col
        x = X0 + ci * (cw + gap)
        blk(ax, x, hy, cw, hh, solids[ci])
        T(ax, x + 0.30, hy + hh / 2, f'{ci + 1:02}', 10.5,
          color='white', alpha=0.62, bold=True)
        T(ax, x + 0.80, hy + hh / 2, label, 14, bold=True, color='white')
        if ci < n - 1:
            arr(ax, (x + cw + 0.03, hy + hh / 2),
                (X0 + (ci + 1) * (cw + gap) - 0.03, hy + hh / 2), lw=1.0, scale=10)

        for si, s in enumerate(steps):
            y = top + si * pitch
            blk(ax, x, y, cw, sh, tints[ci])
            fit(ax, x, y, cw, sh, s, 12, ls=1.42)
            if si < len(steps) - 1:
                arr(ax, (x + cw / 2, y + sh), (x + cw / 2, y + pitch))
    save(fig, name)


def main():
    src = Path('C:/Users/UserX/AppData/Local/Temp/flow2.py').read_text(encoding='utf-8')
    calls = [n.value for n in ast.parse(src).body if isinstance(n, ast.Expr)
             and isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Name)
             and n.value.func.id == 'columns_fig']
    for call, caption in zip(calls, ['拖拉机装配工艺流程', '联合收获机装配工艺流程']):
        assembly(Path(ast.literal_eval(call.args[0])).stem, caption,
                 ast.literal_eval(call.args[1]))
    service()
    combine()
    straw()


if __name__ == '__main__':
    main()
