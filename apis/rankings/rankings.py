from apis.client import Client, api_builder
from apis.entity import Entity


class Ranking(Entity):
    pass


class Rankings(object):
    def __init__(self):
        self.client = Client()
        self.uri = api_builder().rankings()

    def get_rankings(self, params=None):
        uri = self.uri.path()
        result = self.client.get(uri, params=params)

        return result
