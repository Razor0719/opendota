from apis.client import Client, api_builder
from apis.entity import Entity


class DistributionsEntity(Entity):
    pass


class Distributions(object):
    def __init__(self):
        self.client = Client()
        self.uri = api_builder().distributions()

    def get_distributions(self):
        uri = self.uri.path()
        result = self.client.get(uri)

        return result
