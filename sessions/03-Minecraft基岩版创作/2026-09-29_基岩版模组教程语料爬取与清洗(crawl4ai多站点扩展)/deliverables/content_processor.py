"""
内容提取和处理器 - 将爬取的内容转换为结构化数据
"""

import re
import json
import hashlib
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class MinecraftDocPage:
    """Minecraft 文档页面结构化数据"""

    url: str
    title: str
    content_type: str  # 'tutorial', 'reference', 'schema', 'script_api', 'general'
    markdown_content: str
    code_blocks: List[Dict[str, str]]  # 提取的代码示例
    tables: List[List[str]]  # 提取的表格数据
    related_links: List[str]  # 相关链接
    metadata: Dict[str, Any] = field(default_factory=dict)
    content_hash: str = ""  # 正文指纹，用于跨页内容级去重

    def to_dict(self) -> Dict:
        """转换为字典格式，便于保存为 JSON"""
        return {
            "url": self.url,
            "title": self.title,
            "content_type": self.content_type,
            "markdown_content": self.markdown_content,
            "code_blocks": self.code_blocks,
            "tables": self.tables,
            "related_links": self.related_links,
            "metadata": self.metadata,
            "content_hash": self.content_hash,
            "crawled_at": self.metadata.get("crawled_at"),
        }


class MinecraftContentProcessor:
    """Minecraft 文档内容处理器"""

    def __init__(self):
        self.code_block_pattern = re.compile(r'```(\w+)?\n(.*?)```', re.DOTALL)

        # 前部 YAML frontmatter（站点自带时会与我们的输出格式重复）
        self.frontmatter_pattern = re.compile(r'\A---\s*\n.*?\n---\s*\n', re.DOTALL)

        # 页面噪音行（导航/页脚/编辑链接等），逐行精确匹配，避免误伤正文。
        # 注意：必须带 re.MULTILINE，否则 ^ 只匹配全文开头（曾因此整批失效）
        ML = re.MULTILINE
        self.noise_line_patterns = [
            re.compile(r'^\s*Edit this page\b.*$', ML | re.IGNORECASE),
            re.compile(r'^\s*\*?\s*Last updated\b.*$', ML | re.IGNORECASE),
            re.compile(r'^\s*\[\s*(?:Previous|Next)\s*\]\s*\(.*\)\s*$', ML | re.IGNORECASE),
            re.compile(r'^\s*\[?Previous\b(?:.*Next)?\]?\s*$', ML | re.IGNORECASE),
            re.compile(r'^\s*(?:←\s*)?Previous(?:\s*→)?\s*$', ML | re.IGNORECASE),
            re.compile(r'^\s*Licensed under\b.*$', ML | re.IGNORECASE),
            re.compile(r'^\s*Cookies help us\b.*$', ML | re.IGNORECASE),
            re.compile(r'^\s*(?:Accept|Reject)\s+(?:all\s+)?cookies\s*\.?\s*$', ML | re.IGNORECASE),
            re.compile(r'^\s*Skip to main content\s*$', ML | re.IGNORECASE),
            re.compile(r'^\s*We \w+ use cookies\b.*$', ML | re.IGNORECASE),

            # ---- MS Learn 页面家具（EN/中文双语）----
            re.compile(r'^\s*(?:Ask Learn\s*)+$', ML | re.IGNORECASE),
            re.compile(r'^\s*(?:询问 Learn\s*)+$', ML),
            re.compile(r'^\s*(?:Feedback|反馈)\s*$', ML | re.IGNORECASE),
            re.compile(r'^#{1,6}\s*(?:Feedback|反馈)\s*$', ML | re.IGNORECASE),
            re.compile(r'^\s*(?:Reading mode disabled|阅读模式已禁用)\s*$', ML | re.IGNORECASE),
            re.compile(r'^\s*Summarize this article for me\s*$', ML | re.IGNORECASE),
            re.compile(r'^\s*Suggest a fix\?\s*$', ML | re.IGNORECASE),
            re.compile(r'^\s*(?:Theme|主题)\s*$', ML | re.IGNORECASE),
            re.compile(r'^\s*\*\s*(?:Light|Dark|High contrast|亮|暗|高对比度)\s*$', ML | re.IGNORECASE),
            re.compile(r'^\s*(?:是\s+)?否(?:\s+否)?\s*$', ML),
            re.compile(r'^\s*Yes\s+No\s*$', ML | re.IGNORECASE),
            re.compile(r'^\s*\[[^\]]*(?:locale|你的隐私选择|Your Privacy Choices)[^\]]*\]\([^)]*\)\s*$', ML | re.IGNORECASE),
            re.compile(r'^\s*\[\s*\]\([^)]*\)\s*$', ML),  # 空锚点链接 [](url)
            re.compile(r'^\s*\*\s*(?:Manage [Cc]ookies|管理 ?[Cc]ookie)\s*$', ML | re.IGNORECASE),
            re.compile(r'^\s*\*\s*\[[^\]]*(?:Privacy|隐私|Contribute|参与|Terms of Use|使用条款|'
                       r'Trademarks|商标|Previous Versions|早期版本|Consumer Health|消费者健康|'
                       r'AI Disclaimer|AI 免责声明|Blog|博客|Discord|Repository)[^\]]*\]\([^)]*\)\s*$', ML | re.IGNORECASE),
            re.compile(r'^\s*\*?\s*©\s*Microsoft\s*\d{4}\s*$', ML | re.IGNORECASE),
            re.compile(r'^\s*\*?\s*"Minecraft" is a trademark of Mojang.*$', ML | re.IGNORECASE),
            re.compile(r'^\s*Bedrock Wiki\s+by\b.*$', ML | re.IGNORECASE),
            re.compile(r'^\s*Bedrock OSS, Bedrock Wiki and\b.*$', ML | re.IGNORECASE),
            re.compile(r'^\s*\[\s*Edit\s+[^\]]*\son GitHub\s*\]\([^)]*\)\s*$', ML | re.IGNORECASE),
            re.compile(r'^\s*\[\s*!\[[^\]]*\]\(https?://github\.com/[^)]*\.png[^)]*\)\].*$', ML),
            re.compile(r'^#{1,6}\s*Contributors\s*$', ML | re.IGNORECASE),
            re.compile(r'^\s*Ask Learn is an AI assistant.*$', ML | re.IGNORECASE),
            re.compile(r'^\s*Please sign in to use Ask Learn.*$', ML | re.IGNORECASE),
            re.compile(r'^#{1,6}\s*$', ML),  # 空标题（如 '## '）
        ]

        # 广告/推广类块（整块移除）
        self.ad_block_patterns = [
            re.compile(r'^\s*\[!?\[?(?:ad|advertisement|sponsor)[^\]]*\]\([^)]*\)\s*$', re.IGNORECASE | re.MULTILINE),
        ]

    # ---------- 主流程 ----------

    def process(self, crawl_result, site=None) -> MinecraftDocPage:
        """
        处理爬取结果，提取结构化信息

        Args:
            crawl_result: Crawl4AI 的爬取结果对象
            site: SiteConfig（用于最短正文门槛等站点级规则，可为 None）

        Returns:
            MinecraftDocPage: 结构化文档对象
        """
        markdown = self._extract_markdown(crawl_result)

        # 元数据标题用于垃圾头剥离定位
        meta_title = (getattr(crawl_result, "metadata", None) or {}).get("title")
        if not isinstance(meta_title, str):
            meta_title = None

        markdown = self._clean(markdown, title=meta_title, url=crawl_result.url)

        min_len = getattr(site, "min_content_length", 200) if site else 200
        if len(markdown) < min_len:
            raise ValueError(f"正文过短({len(markdown)}字符)，判定为无效页面")

        # 1. 识别内容类型
        content_type = self._detect_content_type(crawl_result.url, markdown)

        # 2. 提取代码块（JSON 配置、脚本示例等）
        code_blocks = self._extract_code_blocks(markdown)

        # 3. 提取表格（参数说明、组件列表等）
        tables = self._extract_tables(markdown)

        # 4. 提取标题
        title = self._extract_title(markdown, crawl_result.metadata)

        # 5. 提取相关链接（只保留有效内容页）
        related_links = self._extract_related_links(markdown, self_url=crawl_result.url)

        return MinecraftDocPage(
            url=crawl_result.url,
            title=title,
            content_type=content_type,
            markdown_content=markdown,
            code_blocks=code_blocks,
            tables=tables,
            related_links=related_links,
            metadata={
                "depth": (getattr(crawl_result, "metadata", None) or {}).get("depth", 0),
                "score": (getattr(crawl_result, "metadata", None) or {}).get("score", 0),
                "site": getattr(site, "name", "unknown"),
                "crawled_at": datetime.now().isoformat(),
            },
            content_hash=self._content_hash(markdown),
        )

    # ---------- 清洗 ----------

    def _clean(self, markdown: str, title: str = None, url: str = None) -> str:
        """清洗正文：去 frontmatter、噪音行、HTML 标签转 markdown（表格保留原样）"""
        text = markdown

        # crawl4ai 会把 text/plain 原文整体包进一层代码围栏，先解包
        m = re.match(r'\A```[^\n]*\n(.*)```[ \t]*\Z', text, re.DOTALL)
        if m:
            text = m.group(1)

        # 站点自带的 YAML frontmatter（我们保存时会生成自己的）
        text = self.frontmatter_pattern.sub("", text, count=1)

        # 剥离正文前的导航/横幅垃圾头（wiki 侧边栏、MS Learn cookie 横幅等）
        stripped = self.strip_junk_header(text, title=title)
        if stripped != text:
            text = stripped
        else:
            text = self._strip_nav_run(text)

        if url:
            text = self._strip_self_toc(text, url)
            text = self._clean_heading_anchors(text)

        # 尾部页脚块（"此页面是否有帮助"之后整块是 UI 家具：重复目录/主题/语言/法务列表）
        text = self._strip_footer_block(text)

        # 尾部死脚注编号（wiki 页脚注链接定义被渲染成裸数字行）
        text = self._strip_trailing_footnote_numbers(text)

        # bedrock.dev 每页顶部固定的提示行
        text = re.sub(r'^\s*>\s*Documentation index:.*$', '', text, flags=re.MULTILINE)
        text = re.sub(r'^\s*>\s*Append `\.md` to any.*$', '', text, flags=re.MULTILINE)

        # HTML 表格原位暂存（bedrock.dev 大量文档表格，转成管道表会丢结构）
        # 占位符用零填充编号，避免 _1 成为 _10.._31 的前缀导致恢复时互相污染
        table_blocks = []

        def _stash(m):
            table_blocks.append(m.group(0))
            return f"\n\nHTML_TABLE_PLACEHOLDER_{len(table_blocks) - 1:03d}\n\n"

        if "<table" in text.lower():
            text = re.sub(r'<table\b.*?</table>', _stash, text,
                          flags=re.DOTALL | re.IGNORECASE)
            text = self._html_faithful_to_md(text)  # 其余标签做保真转换
            for i, block in enumerate(table_blocks):
                text = text.replace(f"HTML_TABLE_PLACEHOLDER_{i:03d}", block)
        elif re.search(r'<(h[1-6]|p|div|li|ul|br)\b', text, re.IGNORECASE):
            # 无表格但有 HTML 结构的页面
            text = self._html_faithful_to_md(text)

        for pattern in self.noise_line_patterns:
            text = pattern.sub('', text)

        for pattern in self.ad_block_patterns:
            text = pattern.sub('', text)

        # 折叠 3 个以上连续空行
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()

    # ---------- 垃圾头剥离 ----------

    @staticmethod
    def _norm_for_match(s: str) -> str:
        """标题归一化：去后缀、去符号、小写，用于 h1 与标题匹配"""
        s = re.sub(r"\s*\|\s*microsoft learn\s*$", "", s or "", flags=re.IGNORECASE)
        return re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "", s.lower())

    def strip_junk_header(self, text: str, title: str = None) -> str:
        """
        剥离正文前的导航/横幅/cookie 横幅等垃圾头。

        wiki 每页带 ~350 行侧边栏，MS Learn 每页带 ~800 行 cookie/横幅/全局导航。
        规则：正文以与页面标题一致的 `# 标题` 行开始，剥离其之前的内容。
        安全护栏：命中标题前若存在代码围栏则不剥离（正文可能先于标题）。
        """
        nt = self._norm_for_match(title) if title else ""

        if nt:
            for m in re.finditer(r'^# (.+)$', text, re.MULTILINE):
                nh = self._norm_for_match(m.group(1))
                matched = nh == nt or (len(nh) >= 8 and (nh in nt or nt in nh))
                if matched:
                    head = text[:m.start()]
                    if "```" not in head:
                        return text[m.start():]
                    break

        # 无标题可用时的保守规则：首个 h1 之前无任何正文特征才剥离
        m = re.search(r'^# (.+)$', text, re.MULTILINE)
        if m:
            head = text[:m.start()]
            has_junk_marker = re.search(
                r'跳至主要内容|skip to main content|we use optional cookies|'
                r'this browser is no longer supported',
                head, re.IGNORECASE)
            if "```" not in head and (
                    not head.strip()
                    or has_junk_marker
                    or not re.search(r'^#{1,6} ', head, re.MULTILINE)):
                return text[m.start():]
        return text

    # MS Learn 页脚块起点标记，分两级：
    #   强标记：UI 交互文案，正文中不可能出现，任意位置命中即截断
    #   弱标记：仅标题形态（In this article 等），可能与正文标题同形，限后 50% 处
    FOOTER_STRONG_MARKERS = re.compile(
        r'^\s*(?:'
        r'Was this page helpful\?|此页面是否有帮助|'
        r'Want to try using Ask Learn|想要尝试使用 Ask Learn|'
        r'Need help with this topic\?|需要有关本主题的帮助\?|'
        r'Reading mode disabled|阅读模式已禁用'
        r')',
        re.MULTILINE | re.IGNORECASE,
    )
    FOOTER_WEAK_MARKERS = re.compile(
        r'^#{1,6}\s*(?:Feedback|反馈|Additional resources|其他资源|In this article|本文内容)\s*$',
        re.MULTILINE | re.IGNORECASE,
    )

    def _strip_footer_block(self, text: str) -> str:
        candidates = [m.start() for m in self.FOOTER_STRONG_MARKERS.finditer(text)]
        weak = [m.start() for m in self.FOOTER_WEAK_MARKERS.finditer(text)
                if m.start() > len(text) * 0.5]
        candidates += weak
        if candidates:
            cut = min(candidates)
            return text[:cut].rstrip() + "\n"
        return text

    @staticmethod
    def _strip_trailing_footnote_numbers(text: str) -> str:
        """剥离正文末尾连续的裸数字行（如脚注编号残留 '1' '2  ' '3'）"""
        lines = text.rstrip().split("\n")
        n = len(lines)
        while n > 0 and re.match(r"^\s*\d{1,3}\s*$", lines[n - 1]):
            n -= 1
        if n == 0 or n == len(lines):
            return text
        return "\n".join(lines[:n]).rstrip() + "\n"

    def _strip_self_toc(self, text: str, url: str) -> str:
        """
        剥离正文开头的“本页目录”块（wiki 的 Contents：只含指向自身 URL 锚点的链接列表）
        """
        lines = text.split('\n')
        if not lines or not lines[0].startswith('# '):
            return text

        base = url.split('#')[0].rstrip('/')
        self_link = re.compile(
            r'^\s*\*?\s*\[[^\]]*\]\(\s*' + re.escape(base) + r'(?:#[^)]*)?\s*\)\s*$')
        anchor_bullet = re.compile(
            r'^\s*\*?\s*\[[^\]]*\]\(\s*' + re.escape(base) + r'#[^)]*\s*\)\s*$')
        label = re.compile(r'^(Contents|目录|\s*(?:beginner|intermediate|advanced|guide)\s*)$', re.IGNORECASE)

        j = 1
        anchor_hits = 0
        while j < len(lines):
            l = lines[j]
            if not l.strip() or label.match(l.strip()):
                j += 1
                continue
            if anchor_bullet.match(l):
                anchor_hits += 1
                j += 1
                continue
            if self_link.match(l):
                j += 1
                continue
            break

        # 至少 2 个自页锚点链接才认定是目录块
        if anchor_hits >= 2:
            return '\n'.join([lines[0]] + lines[j:]).lstrip('\n')
        return text

    @staticmethod
    def _clean_heading_anchors(text: str) -> str:
        """去掉标题行尾部的零宽锚点链接，如 '## 标题 [​](https://...#anchor)'"""
        return re.sub(
            r'^(#{1,6} .+?)\s*\[\s*​?\s*\]\(\s*https?://[^)]+\s*\)\s*$',
            r'\1',
            text,
            flags=re.MULTILINE,
        )

    def _strip_nav_run(self, text: str) -> str:
        """无 h1 时的兜底：剥离正文开头的链接导航块（连续 ≥8 行的列表链接）"""
        lines = text.split('\n')
        nav_link = re.compile(r'^\s*(?:[-*+]|\d+\.)?\s*\[[^\]]*\]\(\s*https?://[^)]+\s*\)\s*$')
        plain_bullet = re.compile(r'^\s*(?:[-*+]|\d+\.)\s+[^|]{1,60}$')

        i = 0
        while i < len(lines) and not lines[i].strip():
            i += 1
        if i >= len(lines) or not nav_link.match(lines[i]):
            return text

        j = i
        while j < len(lines):
            l = lines[j]
            if not l.strip() or nav_link.match(l) or plain_bullet.match(l):
                j += 1
                continue
            # 无链接小节标题（后跟子弹行）也算导航
            nxt = lines[j + 1] if j + 1 < len(lines) else ''
            if re.match(r'^[^\[\]#*|>].{0,40}$', l) and (
                    nav_link.match(nxt) or plain_bullet.match(nxt) or not nxt.strip()):
                j += 1
                continue
            break

        if j - i >= 8:
            return '\n'.join(lines[j:])
        return text

    @staticmethod
    def _content_hash(markdown: str) -> str:
        """正文指纹：折叠空白后取 md5，识别不同 URL 的重复内容"""
        normalized = re.sub(r'\s+', ' ', markdown).strip().lower()
        return hashlib.md5(normalized.encode('utf-8')).hexdigest()

    # ---------- 提取 ----------

    def _extract_markdown(self, crawl_result) -> str:
        """从爬取结果中提取 Markdown 内容，兼容多种格式"""
        markdown = ""

        if hasattr(crawl_result, 'markdown') and crawl_result.markdown:
            md_obj = crawl_result.markdown

            if hasattr(md_obj, 'fit_markdown') and md_obj.fit_markdown:
                markdown = md_obj.fit_markdown
            elif hasattr(md_obj, 'raw_markdown') and md_obj.raw_markdown:
                markdown = md_obj.raw_markdown
            elif hasattr(md_obj, 'markdown') and md_obj.markdown:
                markdown = md_obj.markdown
            elif isinstance(md_obj, str):
                markdown = md_obj

        if not markdown and hasattr(crawl_result, 'cleaned_html') and crawl_result.cleaned_html:
            markdown = self._html_to_markdown(crawl_result.cleaned_html)

        if not markdown and hasattr(crawl_result, 'html') and crawl_result.html:
            markdown = self._html_to_markdown(crawl_result.html)

        return markdown.strip() if markdown else ""

    def _html_faithful_to_md(self, html: str) -> str:
        """
        保真 HTML→markdown：只做无损的结构转换，绝不全局剥标签。

        背景：bedrock.dev 的 .md 是“markdown+内嵌HTML”官方格式，正文里大量出现
        schema 角括号标注（如 <"hold_on_last_frame">、<any array element>），
        通用剥标签会把它们当 HTML 删除。此处仅转换：
          h1-h6 → # 标题；<br> 系 → 换行；<pre><code> → 围栏（实体解码）；
          <p> → 段落；行内 <code> → 反引号；HTML 实体解码。
        其余标签（表格等）原样保留，阅读器可正常渲染。
        """
        text = html

        # 1. 代码块：<pre><code> → ``` 围栏（先于其他转换，内部实体解码）
        def _pre(m):
            code = m.group(1)
            for a, b in (("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'),
                         ("&#39;", "'"), ("&amp;", "&")):
                code = code.replace(a, b)
            return f"\n```\n{code}\n```\n"

        text = re.sub(r'<pre[^>]*>\s*<code[^>]*>(.*?)</code>\s*</pre>',
                      _pre, text, flags=re.DOTALL | re.IGNORECASE)

        # 2. 标题 → markdown 标题（剥掉内部嵌套标签，如 <h1><p id="X">Y</p></h1>）
        def _heading(m):
            inner = re.sub(r'<[^>]+>', '', m.group(2)).strip()
            return f"\n{'#' * int(m.group(1))} {inner}\n"

        text = re.sub(r'<h([1-6])[^>]*>(.*?)</h\1\s*>', _heading, text,
                      flags=re.DOTALL | re.IGNORECASE)

        # 3. 换行（<br>、<br/>、<br />、</br>）
        text = re.sub(r'</?br\s*/?>', '\n', text, flags=re.IGNORECASE)

        # 4. 段落 → 文本 + 空行（内容原样保留）
        text = re.sub(r'<p[^>]*>(.*?)</p\s*>', lambda m: m.group(1) + '\n\n',
                      text, flags=re.DOTALL | re.IGNORECASE)

        # 5. 行内代码
        text = re.sub(r'<code[^>]*>(.*?)</code\s*>', r'`\1`', text,
                      flags=re.DOTALL | re.IGNORECASE)

        # 6. HTML 实体解码（正文与代码可读性）
        for a, b in (("&nbsp;", " "), ("&lt;", "<"), ("&gt;", ">"),
                     ("&quot;", '"'), ("&#39;", "'"), ("&amp;", "&")):
            text = text.replace(a, b)

        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()

    def _html_to_markdown(self, html: str) -> str:
        """简单的 HTML 转 Markdown"""
        import re

        text = html

        text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<nav[^>]*>.*?</nav>', '', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<footer[^>]*>.*?</footer>', '', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<header[^>]*>.*?</header>', '', text, flags=re.DOTALL | re.IGNORECASE)

        text = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n', text, flags=re.DOTALL)
        text = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n', text, flags=re.DOTALL)
        text = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n', text, flags=re.DOTALL)
        text = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1\n', text, flags=re.DOTALL)

        text = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', text, flags=re.DOTALL)
        text = re.sub(r'<br\s*/?>', '\n', text)

        text = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', text, flags=re.DOTALL)
        text = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', text, flags=re.DOTALL)
        text = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', text, flags=re.DOTALL)
        text = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', text, flags=re.DOTALL)
        text = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', text, flags=re.DOTALL)

        text = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', text, flags=re.DOTALL)
        text = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'```\n\1\n```', text, flags=re.DOTALL)

        text = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', text, flags=re.DOTALL)
        text = re.sub(r'<ul[^>]*>(.*?)</ul>', r'\1', text, flags=re.DOTALL)
        text = re.sub(r'<ol[^>]*>(.*?)</ol>', r'\1', text, flags=re.DOTALL)

        text = re.sub(r'<td[^>]*>(.*?)</td>', r'| \1 ', text, flags=re.DOTALL)
        text = re.sub(r'<tr[^>]*>(.*?)</tr>', r'\1|\n', text, flags=re.DOTALL)
        text = re.sub(r'<th[^>]*>(.*?)</th>', r'| \1 ', text, flags=re.DOTALL)

        text = re.sub(r'<div[^>]*>', '', text)
        text = re.sub(r'</div>', '', text)
        text = re.sub(r'<span[^>]*>', '', text)
        text = re.sub(r'</span>', '', text)
        text = re.sub(r'<section[^>]*>', '', text)
        text = re.sub(r'</section>', '', text)
        text = re.sub(r'<article[^>]*>', '', text)
        text = re.sub(r'</article>', '', text)

        text = re.sub(r'<[^>]+>', '', text)

        text = re.sub(r'&nbsp;', ' ', text)
        text = re.sub(r'&amp;', '&', text)
        text = re.sub(r'&lt;', '<', text)
        text = re.sub(r'&gt;', '>', text)
        text = re.sub(r'&quot;', '"', text)

        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r' {2,}', ' ', text)

        return text.strip()

    def _detect_content_type(self, url: str, markdown: str) -> str:
        """识别文档类型"""
        url_lower = url.lower()

        if "schemasreference" in url_lower or "schema" in url_lower:
            return "schema"
        elif "reference" in url_lower and "example" in url_lower:
            return "reference"
        elif "scriptapi" in url_lower or "minecraft-server" in url_lower:
            return "script_api"
        elif "documents" in url_lower or "tutorial" in url_lower or "/guide" in url_lower:
            return "tutorial"
        elif "/docs/" in url_lower or "bedrock.dev" in url_lower:
            return "reference"
        elif "documents" in url_lower or "tutorial" in url_lower:
            return "tutorial"
        else:
            return "general"

    def _extract_code_blocks(self, markdown: str) -> List[Dict[str, str]]:
        """提取 Markdown 中的代码块"""
        blocks = []

        # 匹配 ```json ... ``` 格式的代码块
        for match in self.code_block_pattern.finditer(markdown):
            language = match.group(1) or "text"
            code = match.group(2).strip()

            # 只保留有意义的代码块（长度>50）
            if len(code) > 50:
                blocks.append({
                    "language": language,
                    "code": code,
                    "description": self._extract_code_description(markdown, match.start())
                })

        return blocks

    def _extract_code_description(self, markdown: str, code_pos: int) -> str:
        """提取代码块前的描述文字"""
        # 获取代码块前的 200 个字符作为描述
        before = markdown[max(0, code_pos - 200):code_pos]
        lines = before.strip().split('\n')

        # 返回最后一行非空文本（通常是代码说明）
        for line in reversed(lines):
            line = line.strip()
            if line and not line.startswith('```'):
                return line[:100]  # 限制长度
        return ""

    def _extract_tables(self, markdown: str) -> List[List[str]]:
        """提取 Markdown 表格"""
        tables = []
        lines = markdown.split('\n')

        current_table = []
        for line in lines:
            # 检测表格行（包含 | 分隔符）
            if '|' in line and not line.strip().startswith('```'):
                cells = [cell.strip() for cell in line.split('|')]
                cells = [c for c in cells if c]  # 移除空单元格
                if cells:
                    current_table.append(cells)
            else:
                if len(current_table) > 1:  # 至少表头+一行数据
                    tables.append(current_table)
                current_table = []

        # 处理最后一个表格
        if len(current_table) > 1:
            tables.append(current_table)

        return tables

    def _extract_title(self, markdown: str, metadata: Dict) -> str:
        """提取页面标题"""
        # 优先从 Markdown 标题提取
        match = re.search(r'^#\s+(.+)$', markdown, re.MULTILINE)
        if match:
            title = match.group(1).strip()
            if title:
                return title[:120]

        # 其次从 metadata 提取（可能存在但为 None）
        title = (metadata or {}).get("title")
        if isinstance(title, str) and title.strip():
            return title.strip()[:120]

        # 兜底：取正文第一行"像正文"的行（跳过结构符号/HTML/代码围栏）
        for line in markdown.split('\n'):
            line = line.strip()
            if not line or line.startswith(('---', '```', '<', '>', '|', '!', '#', '[')):
                continue
            if len(line) < 4 and not line[0].isalnum():
                continue
            return line[:120]

        return "Unknown Title"

    # 无效链接特征（隐私/法务/页脚/语言切换/账号等 UI 链接）
    LINK_JUNK = re.compile(
        r"privacy|cookie|termsofuse|trademark|contribute|previous-versions|"
        r"locale|consumer\.?health|techcommunity|principles-for-ai|/users/|"
        r"/answers/|/training/|bg-p/|discord|hacktoberfest|licenses|favicon|"
        r"/legal/|go\.microsoft\.com|aka\.ms",
        re.IGNORECASE,
    )
    # 有效参考内容页（MS Learn creator 文档 / Bedrock Wiki 内容页 / bedrock.dev 文档）
    LINK_VALID = re.compile(
        r"learn\.microsoft\.com/[a-z\-]*/minecraft/creator/\S+|"
        r"wiki\.bedrock\.dev/[a-z0-9\-]+/[a-z0-9\-][^#]*$|"
        r"bedrock\.dev/docs/\S+",
        re.IGNORECASE,
    )

    def _extract_related_links(self, markdown: str, self_url: str = "") -> List[str]:
        """
        提取 Markdown 中的链接，只保留有效的参考内容页：
        丢弃纯锚点、自页链接、隐私/法务/页脚 UI 链接与无关外链。
        """
        link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
        links = []

        self_path = ""
        if self_url:
            from urllib.parse import urlparse
            _p = urlparse(self_url)
            self_path = (_p.netloc, _p.path.rstrip("/"))

        seen = set()
        for match in link_pattern.finditer(markdown):
            url = match.group(2).strip()
            if not url.startswith(("http://", "https://", "/")):
                continue
            if url.startswith("#"):
                continue
            if self_url:
                from urllib.parse import urlparse
                p = urlparse(url)
                if (p.netloc, p.path.rstrip("/")) == self_path:
                    continue  # 自页链接（含仅锚点差异）
            if self.LINK_JUNK.search(url):
                continue
            if not self.LINK_VALID.search(url):
                continue
            if url in seen:
                continue
            seen.add(url)
            links.append(url)

        return links[:20]  # 限制数量
