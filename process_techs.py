from concurrent.futures import ThreadPoolExecutor
from threading import Lock

from techs.nextjs import Nextjs
from techs.zod import Zod
from utils.lance import Lance


def process_url(url, tech, lance: Lance, lock):
    page = tech.page(url)

    with lock:
        lance.add_page(page)
        for chunk in tech.page_chunks(url, page.content):
            lance.add_page_chunks([chunk])


def insert_docs():
    lance = Lance()
    lance.count()
    techs = [
        Nextjs(version="15.1.2", router="app"),
        Nextjs(version="15.1.2", router="pages"),
        Nextjs(version="14.2.21", router="app"),
        Nextjs(version="14.2.21", router="pages"),
        Nextjs(version="13.5.8", router="app"),
        Nextjs(version="13.5.8", router="pages"),
        Zod(version="3.24.1"),
    ]
    lock = Lock()

    table = lance.db.open_table("pages")
    for tech in techs:
        urls = [url for url in tech.docs_urls() if table.count_rows(f"url = '{url}'") == 0]

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(process_url, url, tech, lance, lock) for url in urls]
            for future in futures:
                future.result()


if __name__ == "__main__":
    insert_docs()
