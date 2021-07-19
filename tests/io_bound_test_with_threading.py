import time
import requests
import logging
from concurrent import futures

logging.basicConfig()
logger = logging.getLogger("Threading")
logger.setLevel(logging.INFO)


def fetch_url(im_url):
    try:
        resp = requests.get(im_url)
    except Exception as e:
        logger.info("could not fetch {}".format(im_url))
    else:
        return resp.content


def fetch_all(url_list):
    with futures.ThreadPoolExecutor() as executor:
        responses = executor.map(fetch_url, url_list)
    return responses


if __name__ == '__main__':
    url = "http://127.0.0.1:9999/"

    for ntimes in [1, 10, 100, 500, 1000]:
        start_time = time.time()
        responses = fetch_all([url] * ntimes)
        logger.info('Fetch %s urls takes %s seconds', ntimes, time.time() - start_time)
