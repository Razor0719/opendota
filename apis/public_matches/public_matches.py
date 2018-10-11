from apis.client import Client, api_builder
from apis.entity import Entity


class PublicMatch(Entity):
    pass


class PublicMatches(object):
    def __init__(self):
        self.client = Client()
        self.uri = api_builder().publicMatches()

    def get_publicMatches(self, params=None):
        uri = self.uri.path()
        public_match = self.client.get(uri, params=params)
        print(public_match)
        return public_match
