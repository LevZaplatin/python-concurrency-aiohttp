import logging
import time

import aiohttp
import asyncio

logging.basicConfig()
logger = logging.getLogger("Async")
logger.setLevel(logging.INFO)


async def fetch_url(session, url):
    async with session.get(url) as response:
        await response.text()


async def fetch_all(urls):
    connector = aiohttp.TCPConnector(limit=None)
    async with aiohttp.ClientSession(connector=connector) as session:
        await asyncio.gather(
            *[fetch_url(session, url) for url in urls]
        )


if __name__ == '__main__':
    url = "http://127.0.0.1:9999/"
    loop = asyncio.get_event_loop()

    for ntimes in [1, 10, 100, 500, 1000]:
        start_time = time.time()
        loop.run_until_complete(fetch_all([url] * ntimes))
        logger.info('Fetch %s urls takes %s seconds', ntimes, time.time() - start_time)
