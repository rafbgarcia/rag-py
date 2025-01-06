import time
from contextlib import contextmanager

from markdownify import markdownify


def html_to_md(html: str):
    return markdownify(
        html,
        heading_style="ATX",
        strip=["img", "a"],
    )


def cleanup_markdown(markdown: str):
    return "\n".join(line.rstrip() for line in markdown.strip().splitlines())


@contextmanager
def timer(name=""):
    start = time.time()
    yield
    end = time.time()
    print(f"{name} time: {end - start} seconds")
