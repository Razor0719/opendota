from apis.client import Client, api_builder
from apis.entity import Entity


class ProMatch(Entity):
    pass


class ProMatches(object):
    def __init__(self):
        self.client = Client()
        self.uri = api_builder().proMatches.path()

    def get_all(self, params={'less_than_match_id': None}):
        matches = self.client.get(self.uri, params)
        for match in matches:
            # TODO save data
            m = ProMatch(match)
            print(m)
        return matches
