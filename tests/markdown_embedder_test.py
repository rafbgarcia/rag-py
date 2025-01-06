import pytest

from utils.markdown_embedder import (
    AllMpnetEmbedder,
    BaseBertEmbedder,
    LargeBertEmbedder,
    preprocess,
)


@pytest.fixture(autouse=True)
def reset_singletons():
    BaseBertEmbedder._instance = None
    LargeBertEmbedder._instance = None
    AllMpnetEmbedder._instance = None
    yield


@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("Simple text", "Simple text"),
        ("Text\nwith\nnewlines", "Text\nwith\nnewlines"),
        ("# Markdown header", "Markdown header"),
        ("## Deep header", "Deep header"),
        ("Text    with   spaces", "Text    with   spaces"),
        ("**Bold text**", "Bold text"),
        ("*Italic text*", "Italic text"),
        ("- List item", "List item"),
        ("1. Numbered item", "Numbered item"),
        ("[Link text](url)", "Link text"),
        ("```python\ncode\n```", "code"),
        ("`inline code`", "inline code"),
    ],
)
def test_preprocess_text(input_text, expected):
    processed = preprocess(input_text)
    assert processed == expected


def test_singleton_behavior():
    base1 = BaseBertEmbedder()
    base2 = BaseBertEmbedder()
    assert base1 is base2

    large1 = LargeBertEmbedder()
    large2 = LargeBertEmbedder()
    assert large1 is large2

    mpnet1 = AllMpnetEmbedder()
    mpnet2 = AllMpnetEmbedder()
    assert mpnet1 is mpnet2


def test_embed():
    text = "## Section 1"
    assert len(BaseBertEmbedder().embed(text)) == 768
    assert len(LargeBertEmbedder().embed(text)) == 1024
    assert len(AllMpnetEmbedder().embed(text)) == 768
