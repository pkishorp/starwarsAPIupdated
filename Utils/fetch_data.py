"""
uses HTTP GET request to fetch any resource data from a given URL endpoint
"""
import logging
import requests
from typing import List, Dict, Union, Optional
from requests import Response


# logging configuration
logging.basicConfig(filename="Utils/example.log", encoding="utf-8", level=logging.INFO)


def mylogger(func):
    def wrapper(url, **kwargs):
        try:
            logging.info(f"we are hitting - {url}")
            final_output = func(url)
            logging.info(f"success - {final_output.status_code}")
        except Exception:
            logging.error("there are issues in fetching details")
        return final_output

    return wrapper


@mylogger
def hit_url(url: str) -> Optional[Response]:
    """hits the API endpoint and returns response if successful"""

    response = requests.get(url)
    print(f"[ INFO ] -> {response} - {url}")
    if response.status_code != 200:
        response.raise_for_status()
    else:
        return response


def fetch_data(urls: List) -> Union[List, Dict]:
    """fetches data from given urls"""

    data = []
    for url in urls:
        res = requests.get(url)
        data.append(res.json())

    return data


def fetch_data_new(url: str) -> Dict:
    """hits the API endpoint and returns response if successful"""

    response = requests.get(url)
    print(f"[ INFO ] {response} - {url}")
    if response.status_code != 200:
        response.raise_for_status()
    else:
        return response.json()
