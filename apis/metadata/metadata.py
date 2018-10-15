from apis.client import Client, api_builder
from apis.entity import Entity


class MetadataEntity(Entity):
    pass


class Metadata(object):
    def __init__(self):
        self.client = Client()
        self.uri = api_builder().metadata()

    def get_metadata(self):
        uri = self.uri.path()
        result = self.client.get(uri)

        return result
