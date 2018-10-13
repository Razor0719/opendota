from apis.client import Client, api_builder
from apis.entity import Entity


class SearchEntity(Entity):
    pass


class Search(object):
    def __init__(self):
        self.client = Client()
        self.uri = api_builder().search()

    def search(self, params=None):
        uri = self.uri.path()
        result = self.client.get(uri, params=params)
        print(uri)
        return result
