from pathlib import Path
import ast
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
from matplotlib.font_manager import FontProperties
import restyle_figures as base

base.OUT = base.ROOT / '修改版_v2'
base.OUT.mkdir(exist_ok=True)
base.FONT = FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
base.HEAD = FontProperties(fname='C:/Windows/Fonts/msyhbd.ttc')
ACCENT = '#405c58'
INK = '#272d2c'
FILL = '#f1f4f3'
CONNECT = '#71807d'
original_text = base.text
original_line = base.line


def text(ax, x, y, value, size=12, ha='left', heading=False, color=INK):
    return original_text(ax, x, y, value, size, ha, heading, color)


def line(ax, points, color=CONNECT, lw=.65):
    if color in ('#cccccc', '#aaaaaa'):
        return
    original_line(ax, points, CONNECT, 1.25)


def arrow(ax, start, end):
    # Construct arrowheads in physical axes units, avoiding tiny stroked tips.
    import math
    dx, dy = end[0]-start[0], end[1]-start[1]
    length = math.hypot(dx, dy)
    if length < .015:
        return
    ux, uy = dx/length, dy/length
    inset = min(.025, length*.08)
    tip = (end[0]-ux*inset, end[1]-uy*inset)
    head = min(.085, length*.32)
    half = head*.48
    back = (tip[0]-ux*head, tip[1]-uy*head)
    ax.plot([start[0]+ux*inset, back[0]], [start[1]+uy*inset, back[1]],
            color=CONNECT, lw=1.35, solid_capstyle='butt', zorder=1)
    ax.add_patch(Polygon([tip, (back[0]-uy*half, back[1]+ux*half),
                          (back[0]+uy*half, back[1]-ux*half)],
                         facecolor=CONNECT, edgecolor='none', zorder=1))


def node(ax, x, y, w, h, value, size=12):
    rect = Rectangle((x,y),w,h,facecolor=FILL,edgecolor='#b6c2bf',linewidth=.65,zorder=2)
    ax.add_patch(rect)
    label = text(ax,x+w/2,y+h/2,value,size,ha='center')
    base.checks.append((label,rect))


def title(ax, value, width):
    ax.add_patch(Rectangle((.4,.23),.055,.29,facecolor=ACCENT,edgecolor='none'))
    text(ax,.58,.37,value,15,heading=True)


def assembly(name, caption, cols):
    fig, ax = base.canvas(10.5,6.65)
    title(ax,caption,10.5)
    xs=[.4,3.9,7.4]
    for ci,(head,steps) in enumerate(cols):
        x=xs[ci]
        ax.add_patch(Rectangle((x,.91),2.7,.57,facecolor=ACCENT,edgecolor='none'))
        text(ax,x+1.35,1.195,head,12,ha='center',heading=True,color='white')
        if ci<2:
            arrow(ax,(x+2.84,1.195),(xs[ci+1]-.14,1.195))
        for si,step in enumerate(steps):
            y=1.77+si*.77
            node(ax,x,y,2.7,.56,step,11.25)
            if si<len(steps)-1:
                arrow(ax,(x+1.35,y+.58),(x+1.35,y+.75))
    base.save(fig,name)


def service():
    fig,ax=base.canvas(10.5,5.35)
    title(ax,'全程农机作业托管服务流程',10.5)
    rows=[('服务前端',['农户、村集体\n签约土地托管','地块测绘、\n作业与农艺方案','农资集中采购\n与统一供应']),
          ('全程作业',['耕整地','精量播种','田间管理','机械收获','秸秆处理']),
          ('产后服务',['粮食烘干\n与仓储','统一销售\n（订单收购）','作业结算\n与收益分配'])]
    for ri,(head,steps) in enumerate(rows):
        y=1.17+ri*1.39
        ax.add_patch(Rectangle((.4,y),1.48,.83,facecolor=ACCENT,edgecolor='none'))
        text(ax,.61,y+.23,f'0{ri+1}',9,color='#d1ddda')
        text(ax,.61,y+.55,head,12,heading=True,color='white')
        if ri<2:
            arrow(ax,(1.14,y+.88),(1.14,y+1.32))
        span,gap,start=7.78,.29,2.32
        w=(span-gap*(len(steps)-1))/len(steps)
        for si,step in enumerate(steps):
            x=start+si*(w+gap)
            node(ax,x,y,w,.83,step,11.5)
            if si<len(steps)-1:
                arrow(ax,(x+w+.025,y+.415),(x+w+gap-.025,y+.415))
    base.save(fig,'fig_service_flow')


def straw():
    fig,ax=base.canvas(10.5,5.6)
    title(ax,'农作物秸秆综合利用途径',10.5)
    ax.add_patch(Rectangle((.4,.94),9.7,.53,facecolor=ACCENT,edgecolor='none'))
    for x,label,align in [( .61,'利用途径','left'),(2.18,'主要利用方式','left'),(8.5,'占秸秆利用量比例','center')]:
        text(ax,x,1.205,label,11.5,ha=align,heading=True,color='white')
    items=[('肥料化','粉碎直接还田、堆沤腐熟还田','约 57.6%'),
           ('饲料化','青贮、黄贮、打捆饲喂牛羊','约 20.7%'),
           ('燃料化','成型颗粒、直燃发电、沼气','约 8.3%'),
           ('原料化','造纸、人造板、生物基材料',''),
           ('基料化','食用菌栽培基质、菌糠还田','')]
    for i,(name,desc,pct) in enumerate(items):
        y=1.56+i*.57
        ax.add_patch(Rectangle((.4,y),9.7,.52,facecolor=FILL if i%2==0 else '#fafbfa',edgecolor='none'))
        text(ax,.61,y+.26,name,11.5,heading=True,color=ACCENT)
        text(ax,2.18,y+.26,desc,11.5)
        if pct:text(ax,8.5,y+.26,pct,12,ha='center',heading=True,color=ACCENT)
    ax.add_patch(Rectangle((7.35,3.27),2.75,1.09,facecolor=FILL,edgecolor='none'))
    text(ax,8.725,3.815,'两项合计约 1.5%',11.5,ha='center',heading=True,color=ACCENT)
    text(ax,.4,4.86,'注：比例为全国口径（2024年）；北京市秸秆综合利用率保持在99%以上，以肥料化利用为主。',9.5,color='#65716e')
    base.save(fig,'fig_straw_util')


base.text=text
base.line=line
base.arrow=arrow
base.node=node
base.title=title
base.assembly=assembly
base.service=service
base.straw=straw
base.main()
