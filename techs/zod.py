import datetime

import requests
from bs4 import BeautifulSoup

from utils.lance import Page, PageChunk
from utils.markdown_chunker import MarkdownChunker
from utils.markdown_embedder import AllMpnetEmbedder
from utils.utils import cleanup_markdown, html_to_md


class Zod:
    def __init__(self, *, version: str):
        self.id = "zod"
        self.name = "Zod"
        self.version = version
        self.url = f"https://github.com/colinhacks/zod/blob/v{version}/README.md"

        self.llmstxt_chunker = MarkdownChunker()
        self.page_chunker = MarkdownChunker(
            ignore_headings={
                2: ["Sponsors", "Table of contents", "Introduction", "Comparison", "Changelog"]
            }
        )

    def _fetch(self, url: str):
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    def _get_main_content(self, url) -> str:
        html = self._fetch(url)
        soup = BeautifulSoup(html, "html.parser")
        main_content = soup.select_one("article.markdown-body")
        markdown = cleanup_markdown(html_to_md(str(main_content)))

        return markdown

    def docs_urls(self):
        return ["https://github.com/colinhacks/zod/blob/main/README.md"]

    def page(self, url):
        markdown = self._get_main_content(url)
        chunks = self.llmstxt_chunker.heading_chunks(markdown, 1)

        if len(chunks) != 1:
            raise ValueError(f"Expected a single h1 root: {markdown} {chunks}")

        return Page(
            id=self.id,
            name=self.name,
            version=self.version,
            url=url,
            content=chunks[0],
            created_at=datetime.datetime.now(datetime.UTC).isoformat(),
        )

    def page_chunks(self, url, page_content=None):
        markdown = page_content or self._get_main_content(url)
        chunks = self.page_chunker.heading_chunks(markdown, 3)

        for chunk in chunks:
            yield (
                PageChunk(
                    id=self.id,
                    name=self.name,
                    version=self.version,
                    url=url,
                    content=chunk,
                    created_at=datetime.datetime.now(datetime.UTC).isoformat(),
                    vector=AllMpnetEmbedder().embed(chunk),
                )
            )
