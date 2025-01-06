from bs4 import BeautifulSoup
from markdown_it import MarkdownIt
from sentence_transformers import SentenceTransformer


class AllMpnetEmbedder:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
        return cls._instance

    def _preprocess(self, markdown: str) -> str:
        html = MarkdownIt().render(markdown)
        text = BeautifulSoup(html, "html.parser").get_text()
        return text.strip()

    def embed(self, markdown: str):
        text = self._preprocess(markdown)
        return self.model.encode(text)
