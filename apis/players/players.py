from apis.entity import Entity
from apis.client import Client, api_builder


class Player(Entity):
    pass


class Players(object):
    def __init__(self, account_id=None):
        self.client = Client()
        self.account_id = account_id
        self.root_uri = api_builder().players(int(self.account_id))

    def get_player(self):
        uri = self.root_uri.path()
        player = self.client.get(uri)
        print(player)
        return player

    def get_player_wl(self, params=None):
        uri = self.root_uri.wl.path()
        player_wl = self.client.get(uri, params)
        print(player_wl)
        return player_wl

    def get_player_recentMatches(self):
        uri = self.root_uri.recentMatches.path()
        player_recentMatches = self.client.get(uri)
        print(player_recentMatches)
        return player_recentMatches

    def get_player_matches(self, params=None):
        uri = self.root_uri.matches.path()
        player_matches = self.client.get(uri, params)
        print(player_matches)
        return player_matches

    def get_player_heroes(self, params=None):
        uri = self.root_uri.heroes.path()
        player_heroes = self.client.get(uri, params)
        print(player_heroes)
        return player_heroes

    def get_player_peers(self, params=None):
        uri = self.root_uri.peers.path()
        player_peers = self.client.get(uri, params)
        print(player_peers)
        return player_peers

    def get_player_pros(self, params=None):
        uri = self.root_uri.pros.path()
        player_pros = self.client.get(uri, params)
        print(player_pros)
        return player_pros

    def get_player_totals(self, params=None):
        uri = self.root_uri.totals.path()
        player_totals = self.client.get(uri, params)
        print(player_totals)
        return player_totals

    def get_player_counts(self, params=None):
        uri = self.root_uri.totals.path()
        player_counts = self.client.get(uri, params)
        print(player_counts)
        return player_counts

    def get_player_histograms(self, field, params=None):
        uri = self.root_uri.histograms(field).path()
        player_histograms = self.client.get(uri, params)
        print(player_histograms)
        return player_histograms

    def get_player_wardmap(self, params=None):
        uri = self.root_uri.wardmap.path()
        player_wardmap = self.client.get(uri, params)
        print(player_wardmap)
        return player_wardmap

    def get_player_wordcloud(self, params=None):
        uri = self.root_uri.wordcloud.path()
        player_wordcloud = self.client.get(uri, params)
        print(player_wordcloud)
        return player_wordcloud

    def get_player_ratings(self):
        uri = self.root_uri.ratings.path()
        player_ratings = self.client.get(uri)
        print(player_ratings)
        return player_ratings

    def get_player_rankings(self):
        uri = self.root_uri.rankings.path()
        player_rankings = self.client.get(uri)
        print(player_rankings)
        return player_rankings

    def post_player_refesh(self):
        uri = self.root_uri.refresh.path()
        player_refresh = self.client.post(uri)
        print(player_refresh)
        return player_refresh
