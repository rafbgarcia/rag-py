import re
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class _Node:
    level: int
    title: str
    content: str
    children: List["_Node"]
    parent: Optional["_Node"] = None


class MarkdownChunker:
    def __init__(
        self,
        ignore_headings: dict[int, list[str]] = None,
    ):
        self._ignore_headings = ignore_headings or {}

    def _should_ignore_heading(self, level: int, title: str) -> bool:
        if level not in self._ignore_headings:
            return False
        return any(pattern in title for pattern in self._ignore_headings[level])

    def _format_section(self, node: _Node, include_parents: bool = True) -> str:
        result = []

        if include_parents:
            current = node
            ancestors = []
            while current.parent and current.parent.level > 0:
                ancestors.append(current.parent)
                current = current.parent

            for ancestor in reversed(ancestors):
                if not self._should_ignore_heading(ancestor.level, ancestor.title):
                    result.append("#" * ancestor.level + " " + ancestor.title)
                    result.append("")

        result.append("#" * node.level + " " + node.title)
        if node.content:
            result.append("")
            result.append(node.content)

        for child in node.children:
            if not self._should_ignore_heading(child.level, child.title):
                child_content = self._format_section(child, include_parents=False)
                if child_content:
                    result.append("")
                    result.append(child_content)

        return "\n".join(result)

    def _parse_markdown(self, text: str) -> _Node:
        lines = text.split("\n")
        root = _Node(0, "", "", [])
        stack = [root]
        current_content = []
        in_code_block = False

        for line in lines:
            if line.startswith("```"):
                in_code_block = not in_code_block
                current_content.append(line)
                continue

            if not in_code_block and line.startswith("#"):
                if current_content:
                    stack[-1].content = "\n".join(current_content).strip()
                    current_content = []

                level = len(re.match(r"^#+", line).group())
                title = line[level:].strip()

                while level <= stack[-1].level and len(stack) > 1:
                    stack.pop()

                node = _Node(level, title, "", [], stack[-1])
                stack[-1].children.append(node)
                stack.append(node)
            else:
                current_content.append(line)

        if current_content:
            stack[-1].content = "\n".join(current_content).strip()

        return root

    def _get_max_level(self, node: _Node) -> int:
        if not node.children:
            return node.level
        return max(self._get_max_level(child) for child in node.children)

    # def _count_tokens(self, text: str) -> int:
    #     # TODO need to implement this if going to use `find_optimal_chunks`
    #     return self._encoder.count_tokens(text)

    # def find_optimal_chunks(self, markdown: str, max_tokens: int) -> List[str]:
    #     root = self._parse_markdown(markdown)

    #     def check_level(node: _Node, level: int) -> bool:
    #         if node.level == level and not self._should_ignore_heading(level, node.title):
    #             content = self._format_section(node)
    #             return self._count_tokens(content) <= max_tokens
    #         return all(check_level(child, level) for child in node.children)

    #     max_level = self._get_max_level(root)
    #     for level in range(1, max_level + 1):
    #         if check_level(root, level):
    #             return self.heading_with_parents_chunks(markdown, level)

    #     return self.heading_with_parents_chunks(markdown, max_level)

    def heading_with_parents_chunks(self, markdown: str, heading_level: int) -> List[str]:
        root = self._parse_markdown(markdown)
        chunks = []

        def collect_chunks(node: _Node):
            if self._should_ignore_heading(node.level, node.title):
                for child in node.children:
                    collect_chunks(child)
                return

            if node.level == heading_level:
                chunks.append(self._format_section(node))
            elif node.level < heading_level:
                if not any(child.level <= heading_level for child in node.children):
                    chunks.append(self._format_section(node))
                for child in node.children:
                    collect_chunks(child)

        for child in root.children:
            collect_chunks(child)

        return chunks if chunks else [self._format_section(root.children[0])]

    def heading_chunks(self, markdown: str, heading_level: int) -> List[str]:
        root = self._parse_markdown(markdown)
        chunks = []

        def collect_chunks(node: _Node):
            if self._should_ignore_heading(node.level, node.title):
                for child in node.children:
                    collect_chunks(child)
                return

            if node.level == heading_level:
                chunks.append(self._format_section(node))
            for child in node.children:
                collect_chunks(child)

        for child in root.children:
            collect_chunks(child)

        return chunks
