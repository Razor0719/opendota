from apis.client import Client, api_builder
from apis.entity import Entity


class ExplorerEntity(Entity):
    pass


class Explorer(object):
    def __init__(self):
        self.client = Client()
        self.uri = api_builder().explorer()

    def to_explorer(self):
        uri = self.uri.path()
        result = self.client.get(uri)
        print(uri)
        return result
