from utils.markdown_chunker import MarkdownChunker

SAMPLE_DOC = """# Title
Main content

## Section 1
Content 1

### Subsection 1.1
Content 1.1

## Section 2
Content 2"""


def test_chunk_by_heading():
    chunker = MarkdownChunker()
    h1_chunks = chunker.heading_with_parents_chunks(SAMPLE_DOC, 1)
    assert len(h1_chunks) == 1
    assert len(h1_chunks) == 1
    assert h1_chunks == [
        "# Title\n\nMain content\n\n## Section 1\n\nContent 1\n\n### Subsection 1.1\n\nContent 1.1\n\n## Section 2\n\nContent 2"
    ]

    h2_chunks = chunker.heading_with_parents_chunks(SAMPLE_DOC, 2)
    assert len(h2_chunks) == 2
    assert h2_chunks == [
        "# Title\n\n## Section 1\n\nContent 1\n\n### Subsection 1.1\n\nContent 1.1",
        "# Title\n\n## Section 2\n\nContent 2",
    ]

    h3_chunks = chunker.heading_with_parents_chunks(SAMPLE_DOC, 3)
    assert len(h3_chunks) == 2
    assert h3_chunks == [
        "# Title\n\n## Section 1\n\n### Subsection 1.1\n\nContent 1.1",
        "# Title\n\n## Section 2\n\nContent 2",
    ]

    assert any("Section 2" in chunk for chunk in h3_chunks)

    # if heading is not present, chunk by the greatest heading
    h4_chunks = chunker.heading_with_parents_chunks(SAMPLE_DOC, 4)
    assert h4_chunks == [
        "# Title\n" "\n" "## Section 1\n" "\n" "### Subsection 1.1\n" "\n" "Content 1.1",
        "# Title\n" "\n" "## Section 2\n" "\n" "Content 2",
    ]
    h5_chunks = chunker.heading_with_parents_chunks(SAMPLE_DOC, 5)
    assert h5_chunks == [
        "# Title\n" "\n" "## Section 1\n" "\n" "### Subsection 1.1\n" "\n" "Content 1.1",
        "# Title\n" "\n" "## Section 2\n" "\n" "Content 2",
    ]


# def test_find_optimal_chunks():
#     chunker = MarkdownChunker()
#     large_chunks = chunker.find_optimal_chunks(SAMPLE_DOC, 1000)
#     assert len(large_chunks) == 1

#     small_chunks = chunker.find_optimal_chunks(SAMPLE_DOC, 10)
#     assert len(small_chunks) == 2


def test_ignore_headings():
    chunker = MarkdownChunker(ignore_headings={2: ["Section 2"], 3: ["Subsection 1.1"]})

    h1_chunks = chunker.heading_with_parents_chunks(SAMPLE_DOC, 1)
    assert len(h1_chunks) == 1
    assert h1_chunks == ["# Title\n\nMain content\n\n## Section 1\n\nContent 1"]

    h2_chunks = chunker.heading_with_parents_chunks(SAMPLE_DOC, 2)
    assert len(h2_chunks) == 1
    assert h2_chunks == ["# Title\n\n## Section 1\n\nContent 1"]

    h3_chunks = chunker.heading_with_parents_chunks(SAMPLE_DOC, 3)
    assert len(h3_chunks) == 1
    assert h3_chunks == ["# Title\n\nMain content\n\n## Section 1\n\nContent 1"]


def test_code_block_with_heading():
    content = """
### Installation
Install the plugin by running the following command:

```
npm i @next/bundle-analyzer
# or
yarn add @next/bundle-analyzer
# or
pnpm add @next/bundle-analyzer
```

Then, add the bundle analyzer's settings to your `next.config.js`.
""".strip()
    chunker = MarkdownChunker()

    chunks = chunker.heading_with_parents_chunks(content, 3)
    assert len(chunks) == 1
