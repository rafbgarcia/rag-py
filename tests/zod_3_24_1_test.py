import pytest

from techs.zod import Zod


@pytest.fixture
def app():
    return Zod()


def test_docs_urls(app: Zod):
    assert app.docs_urls() == ["https://github.com/colinhacks/zod/blob/main/README.md"]


def test_llms_txt(app: Zod):
    page = app.page(app.docs_urls()[0])
    assert page.id == "zod"
    assert page.name == "Zod"
    assert page.version == "3.24.1"
    assert page.url == "https://github.com/colinhacks/zod/blob/main/README.md"
    assert page.content.startswith("# Zod\n\n✨ https://zod.dev ✨")


def test_page_chunks(app: Zod):
    docs = app.page_chunks(app.docs_urls()[0])

    assert 0 == len(docs[0].content)
    assert docs[0].id == "zod"
    assert docs[0].name == "Zod"
    assert docs[0].version == "3.24.1"
    assert docs[0].url == "https://github.com/colinhacks/zod/blob/main/README.md"
    assert docs[0].content.startswith(
        "[[ ## Zod 3.24.1 documentation ]]\n\n# Zod\n\n## Installation\n\n### Requirements\n\n* TypeScript 4.5+!"
    )
