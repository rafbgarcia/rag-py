from urllib.parse import quote

import lancedb
from lancedb.pydantic import LanceModel, Vector

from utils.markdown_embedder import AllMpnetEmbedder


class Page(LanceModel):
    id: str
    name: str
    version: str
    url: str
    content: str
    created_at: str


class PageChunk(LanceModel):
    id: str
    name: str
    version: str
    url: str
    content: str
    created_at: str
    vector: Vector(768)


class Lance:
    def __init__(self, db_path: str = "data/docs"):
        self.db = self._initdb(db_path)

    def _initdb(self, path):
        db = lancedb.connect(path)
        db.create_table("pages", schema=Page, exist_ok=True)
        db.create_table("page_chunks", schema=PageChunk, exist_ok=True)
        return db

    def search(self, query: str, id: str, version: str):
        table = self.db.open_table("page_chunks")
        embedding = AllMpnetEmbedder().embed(query)

        rows = (
            table.search(embedding)
            .where(f"id = '{id}' AND version LIKE '{version}%'", prefilter=True)
            .select(["content"])
            .limit(2)
            .to_list()
        )

        return [row["content"] for row in rows]

    def add_page(self, page: Page):
        table = self.db.open_table("pages")

        if table.count_rows(f"content = '{quote(page.content)}'") == 0:
            table.add([page])

    def add_page_chunks(self, chunks: list[PageChunk]):
        chunk = chunks[0]
        table = self.db.open_table("page_chunks")

        if table.count_rows(f"content = '{quote(chunk.content)}'") == 0:
            table.add(chunks)
