import datetime
from typing import Literal
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from utils.lance import Page, PageChunk
from utils.markdown_chunker import MarkdownChunker
from utils.markdown_embedder import AllMpnetEmbedder
from utils.utils import cleanup_markdown, html_to_md


class Nextjs:
    def __init__(self, *, version: str, router: Literal["app", "pages"]):
        self.id = f"nextjs_{router}_router"
        self.name = "NextJS"
        self.chunker = MarkdownChunker()
        self.version = version
        self.router = router
        self.base_url = "https://nextjs.org"

        if version.startswith("15"):
            self.base_path = f"/docs/{router}"
        elif version.startswith("14"):
            self.base_path = f"/docs/14/{router}"
        elif version.startswith("13"):
            self.base_path = f"/docs/13/{router}"
        else:
            raise ValueError(f"Invalid version: {version}")

    def _fetch(self, url: str):
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    def _get_main_content(self, url) -> str:
        html = self._fetch(url)
        soup = BeautifulSoup(html, "html.parser")
        main_content = soup.select_one("main article .prose")
        markdown = cleanup_markdown(html_to_md(str(main_content))).replace(
            "TypeScriptJavaScriptTypeScript", ""
        )
        return markdown

    def docs_urls(self) -> list[str]:
        html = self._fetch(self.base_url + self.base_path)
        soup = BeautifulSoup(html, "html.parser")
        links = []
        for a in soup.select(
            f"main div:not(.hidden) nav a[href^='{self.base_path}']:not(.font-medium)"
        ):
            url = urljoin(self.base_url, a["href"])
            links.append(url)

        return list(set(sorted(links)))

    def page(self, url):
        markdown = self._get_main_content(url)
        chunks = self.chunker.heading_chunks(markdown, 1)

        if len(chunks) != 1:
            raise ValueError(
                f"Expected a single h1 root: \n > md: {markdown}\n  > chunks: {chunks}"
            )

        return Page(
            id=self.id,
            name=self.name,
            version=self.version,
            url=url,
            created_at=datetime.datetime.now(datetime.UTC).isoformat(),
            content=chunks[0],
        )

    def page_chunks(self, url, page_content=None):
        markdown = page_content or self._get_main_content(url)
        if len(markdown) <= 50:
            return None

        chunks = self.chunker.heading_with_parents_chunks(markdown, 4)

        for chunk in chunks:
            yield (
                PageChunk(
                    id=self.id,
                    name=self.name,
                    version=self.version,
                    url=url,
                    created_at=datetime.datetime.now(datetime.UTC).isoformat(),
                    content=chunk,
                    vector=AllMpnetEmbedder().embed(chunk),
                )
            )
