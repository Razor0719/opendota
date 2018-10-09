

from apis.client import Client, api_builder
from apis.entity import Entity




class ProPlayer(Entity):
    pass


class ProPlayers(object):
    def __init__(self):
        self.client = Client()
        self.uri = api_builder().proPlayers.path()

    def get_all(self):
        players = self.client.get(self.uri)
        for player in players:
            # TODO save data
            p = ProPlayer(player)

        return players
