"""
数据保存模块 - 支持多种格式、URL 去重与内容级去重、增量保存
"""

import json
import hashlib
from pathlib import Path
from typing import Dict, Any
import aiofiles  # 异步文件操作


class MinecraftDataSaver:
    """Minecraft 文档数据保存器"""

    def __init__(self, output_dir: str = "minecraft_docs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

        # 创建子目录
        self.markdown_dir = self.output_dir / "markdown"
        self.json_dir = self.output_dir / "json"
        self.code_dir = self.output_dir / "code_examples"
        self.index_file = self.output_dir / "document_index.json"

        for dir_path in [self.markdown_dir, self.json_dir, self.code_dir]:
            dir_path.mkdir(exist_ok=True)

        # 加载已有索引（断点续传）
        self.existing_docs = self._load_index()
        # 内容指纹 → url，用于跨站点内容级去重
        self._hash_map: Dict[str, str] = {
            doc.get("content_hash"): url
            for url, doc in self.existing_docs["documents"].items()
            if doc.get("content_hash")
        }

    def _load_index(self) -> Dict[str, Any]:
        """加载已保存的文档索引"""
        if self.index_file.exists():
            with open(self.index_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"documents": {}, "total_count": 0}

    def is_duplicate(self, url: str) -> bool:
        """检查是否已存在（基于 URL）"""
        return url in self.existing_docs["documents"]

    def is_duplicate_content(self, content_hash: str) -> bool:
        """检查相同内容是否已保存过（基于正文指纹）"""
        return bool(content_hash) and content_hash in self._hash_map

    def _register_content_hash(self, content_hash: str, url: str):
        if content_hash:
            self._hash_map[content_hash] = url

    async def save(self, doc_page) -> Dict[str, str]:
        """
        异步保存文档页面

        Args:
            doc_page: MinecraftDocPage 对象

        Returns:
            保存的文件路径信息
        """
        url = doc_page.url
        url_hash = hashlib.md5(url.encode()).hexdigest()[:12]

        # 生成文件名
        safe_title = "".join(c if c.isalnum() else "_" for c in doc_page.title[:50])
        base_filename = f"{safe_title}_{url_hash}"

        saved_files = {}

        # 1. 保存 Markdown（人类可读）
        md_path = self.markdown_dir / f"{base_filename}.md"
        md_content = self._format_markdown(doc_page)
        async with aiofiles.open(md_path, 'w', encoding='utf-8') as f:
            await f.write(md_content)
        saved_files['markdown'] = str(md_path)

        # 2. 保存 JSON（结构化数据，用于 Skill 训练）
        json_path = self.json_dir / f"{base_filename}.json"
        async with aiofiles.open(json_path, 'w', encoding='utf-8') as f:
            await f.write(json.dumps(doc_page.to_dict(), ensure_ascii=False, indent=2))
        saved_files['json'] = str(json_path)

        # 3. 单独保存代码示例（方便查阅）
        if doc_page.code_blocks:
            for i, block in enumerate(doc_page.code_blocks):
                lang = (block['language'] or 'txt').split('.')[0]
                code_filename = f"{base_filename}_code_{i}.{lang or 'txt'}"
                code_path = self.code_dir / code_filename
                async with aiofiles.open(code_path, 'w', encoding='utf-8') as f:
                    await f.write(f"// From: {url}\n// Description: {block['description']}\n\n")
                    await f.write(block['code'])

        # 4. 更新索引
        self.existing_docs["documents"][url] = {
            "title": doc_page.title,
            "type": doc_page.content_type,
            "site": doc_page.metadata.get("site", "unknown"),
            "content_hash": doc_page.content_hash,
            "files": saved_files,
            "saved_at": doc_page.metadata.get("crawled_at"),
        }
        self.existing_docs["total_count"] = len(self.existing_docs["documents"])

        # 同步写入索引（文件小，可以直接写）
        with open(self.index_file, 'w', encoding='utf-8') as f:
            json.dump(self.existing_docs, f, ensure_ascii=False, indent=2)

        self._register_content_hash(doc_page.content_hash, url)

        return saved_files

    def _format_markdown(self, doc_page) -> str:
        """格式化 Markdown 输出"""
        lines = [
            f"---",
            f"title: {doc_page.title}",
            f"source_url: {doc_page.url}",
            f"content_type: {doc_page.content_type}",
            f"site: {doc_page.metadata.get('site', 'unknown')}",
            f"crawled_at: {doc_page.metadata.get('crawled_at', 'unknown')}",
            f"---",
            "",
            f"# {doc_page.title}",
            "",
            "## 内容",
            "",
            doc_page.markdown_content,
            "",
            "## 代码示例",
            ""
        ]

        # 添加代码块
        for i, block in enumerate(doc_page.code_blocks, 1):
            lines.extend([
                f"### 示例 {i} ({block['language']})",
                f"**说明**: {block['description']}",
                "",
                f"```{block['language']}",
                block['code'],
                "```",
                ""
            ])

        # 添加表格摘要
        if doc_page.tables:
            lines.extend([
                "## 数据表格",
                f"共发现 {len(doc_page.tables)} 个表格",
                ""
            ])

        # 添加相关链接
        if doc_page.related_links:
            lines.extend([
                "## 相关链接",
                ""
            ])
            for link in doc_page.related_links[:10]:
                lines.append(f"- {link}")
            lines.append("")

        return '\n'.join(lines)

    def get_stats(self) -> Dict[str, Any]:
        """获取保存统计"""
        type_counts = {}
        for doc in self.existing_docs["documents"].values():
            t = doc.get("type", "unknown")
            type_counts[t] = type_counts.get(t, 0) + 1

        return {
            "total_documents": self.existing_docs["total_count"],
            "by_type": type_counts,
            "output_directory": str(self.output_dir.absolute())
        }
