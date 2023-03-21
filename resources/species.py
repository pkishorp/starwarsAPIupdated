from resources.base import ResourceBase
from Utils.fetch_data import hit_url
from typing import Dict, List


class Species(ResourceBase):
    """
    film class base related functionality
    """

    def __init__(self):
        super().__init__()
        self.relative_url = "/api/species"

    def get_count(self):
        complete_url = self.home_url + self.relative_url
        response = hit_url(complete_url)
        data = response.json()
        count = data.get("count")
        return count

    def get_sample_data(self, id_: int = 1) -> Dict:
        """
        Args:
        id_: sample id of the resource
        Returns:
        data (dict): output data from API endpoint.
        """

        absolute_url = self.home_url + self.relative_url + f"/{id_}"
        response = hit_url(absolute_url)
        data = response.json()
        return data

    def get_resource_urls(self) -> List:
        urls = []
        i = 0
        absolute_url = self.home_url + self.relative_url
        response = hit_url(absolute_url)
        data = response.json()
        data_ = data.get("results")
        while i < len(data_):
            urls.append(data_[i]["url"])
            i += 1
        return urls
