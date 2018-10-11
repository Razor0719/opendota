from apis.entity import Entity
from apis.client import Client, api_builder


class Match(Entity):
    pass


class Matches(object):
    def __init__(self, match_id = None):
        self.client = Client()
        self.match_id = match_id
        self.uri = api_builder().matches(int(self.match_id))

    def get_match(self):
        uri = self.uri.path()
        match = self.client.get(uri)
        print(match)
        return match
