from flask_restplus import Resource, Namespace, reqparse

from apis.players.players import Players

ns = Namespace('players')
common_parser = reqparse.RequestParser()
common_parser.add_argument('account_id', type=int, required=True,
                           help='Steam32 account ID')
common_parser.add_argument('limit', type=int, required=False,
                           help='Number of matches to limit to')
common_parser.add_argument('offset', type=int, required=False,
                           help='Number of matches to offset start by')
common_parser.add_argument('win', type=int, required=False,
                           help='Whether the player won')
common_parser.add_argument('patch', type=int, required=False,
                           help='Patch ID')
common_parser.add_argument('game_mode', type=int, required=False,
                           help='Game Mode ID')
common_parser.add_argument('lobby_type', type=int, required=False,
                           help='Lobby Type ID')
common_parser.add_argument('region', type=int, required=False,
                           help='Region ID')
common_parser.add_argument('date', type=int, required=False,
                           help='Days previous')
common_parser.add_argument('lane_role', type=int, required=False,
                           help='Lane Role ID')
common_parser.add_argument('hero_id', type=int, required=False,
                           help='Hero ID')
common_parser.add_argument('is_radiant', type=int, required=False,
                           help='Whether the player was radiant')
common_parser.add_argument('included_account_id', type=int, required=False,
                           help='Account IDs in the match (array)')
common_parser.add_argument('excluded_account_id', type=int, required=False,
                           help='Account IDs not in the match (array)')
common_parser.add_argument('with_hero_id', type=int, required=False,
                           help='Hero IDs on the player\'s team (array)')
common_parser.add_argument('against_hero_id', type=int, required=False,
                           help='Hero IDs against the player\'s team (array)')
common_parser.add_argument('significant', type=int, required=False,
                           help='Whether the match was significant for aggregation purposes')
common_parser.add_argument('having', type=int, required=False,
                           help='The minimum number of games played, for filtering hero stats')
common_parser.add_argument('sort', required=False,
                           help='The field to return matches sorted by in descending order')


@ns.route('/<int:account_id>')
class PlayersView(Resource):
    @ns.doc(description='get a player')
    def get(self, account_id):
        players = Players(account_id=account_id)
        return players.get_player()


@ns.param('limit', 'Number of matches to limit to', type=int)
@ns.param('offset', 'Number of matches to offset start by', type=int)
@ns.param('win', 'Whether the player won', type=int)
@ns.param('patch', 'Patch ID', type=int)
@ns.param('game_mode', 'Game Mode ID', type=int)
@ns.param('lobby_type', 'Lobby Type ID', type=int)
@ns.param('region', 'Region ID', type=int)
@ns.param('date', 'Days previous', type=int)
@ns.param('lane_role', 'Lane Role ID', type=int)
@ns.param('hero_id', 'Hero ID', type=int)
@ns.param('is_radiant', 'Whether the player was radiant', type=int)
@ns.param('included_account_id', 'Account IDs in the match (array, type=int)', type=int)
@ns.param('excluded_account_id', 'Account IDs not in the match (array, type=int)', type=int)
@ns.param('with_hero_id', 'Hero IDs on the player\'s team (array, type=int)', type=int)
@ns.param('against_hero_id', 'Hero IDs against the player\'s team (array, type=int)', type=int)
@ns.param('significant', 'Whether the match was significant for aggregation purposes', type=int)
@ns.param('having', 'The minimum number of games played, for filtering hero stats', type=int)
@ns.param('sort', 'The field to return matches sorted by in descending order')
class PlayersViewWithQueryParam(Resource):
    args = None
    players = None

    def get(self, account_id, parser=None):
        if parser is not None:
            self.args = parser.parse_args()
            print(self.args)
        else:
            print('this request has no parameters')
        self.players = Players(account_id=account_id)


@ns.route('/<int:account_id>/wl')
class PlayersWlView(PlayersViewWithQueryParam):
    @ns.doc(description='get a player wl')
    def get(self, account_id):
        super().get(account_id=account_id, parser=common_parser)
        return self.players.get_player_wl(params=self.args)


@ns.route('/<int:account_id>/recentMatches')
class PlayersRecentMatchesView(Resource):
    @ns.doc(description='get a player recentMatches')
    def get(self, account_id):
        players = Players(account_id=account_id)
        return players.get_player_recentMatches()


@ns.route('/<int:account_id>/matches')
@ns.param('project', 'Fields to project (array)')
class PlayersMatchesView(PlayersViewWithQueryParam):
    @ns.doc(description='get a player matches')
    def get(self, account_id):
        parser = common_parser.copy()
        parser.add_argument('project', required=False,
                            help='Fields to project (array)')
        super().get(account_id=account_id, parser=parser)
        return self.players.get_player_matches(params=self.args)


@ns.route('/<int:account_id>/heroes')
class PlayersHeroesView(PlayersViewWithQueryParam):
    @ns.doc(description='get a player heroes')
    def get(self, account_id):
        super().get(account_id=account_id, parser=common_parser)
        return self.players.get_player_heroes(params=self.args)


@ns.route('/<int:account_id>/peers')
class PlayersPeersView(PlayersViewWithQueryParam):
    @ns.doc(description='get a player peers')
    def get(self, account_id):
        super().get(account_id=account_id, parser=common_parser)
        return self.players.get_player_peers(params=self.args)


@ns.route('/<int:account_id>/pros')
class PlayersProsView(PlayersViewWithQueryParam):
    @ns.doc(description='get a player pros')
    def get(self, account_id):
        super().get(account_id=account_id, parser=common_parser)
        return self.players.get_player_pros(params=self.args)


@ns.route('/<int:account_id>/totals')
class PlayersTotalsView(PlayersViewWithQueryParam):
    @ns.doc(description='get a player totals')
    def get(self, account_id):
        super().get(account_id=account_id, parser=common_parser)
        return self.players.get_player_totals(params=self.args)


@ns.route('/<int:account_id>/counts')
class PlayersCountsView(PlayersViewWithQueryParam):
    @ns.doc(description='get a player counts')
    def get(self, account_id):
        super().get(account_id=account_id, parser=common_parser)
        return self.players.get_player_counts(params=self.args)


@ns.route('/<int:account_id>/histograms/<string:field>')
class PlayersHistogramsView(PlayersViewWithQueryParam):
    @ns.doc(description='get a player histograms')
    def get(self, account_id, field):
        super().get(account_id=account_id, parser=common_parser)
        return self.players.get_player_histograms(field=field, params=self.args)


@ns.route('/<int:account_id>/wardmap')
class PlayersWardmapView(PlayersViewWithQueryParam):
    @ns.doc(description='get a player wardmap')
    def get(self, account_id):
        super().get(account_id=account_id, parser=common_parser)
        return self.players.get_player_wardmap(params=self.args)


@ns.route('/<int:account_id>/wordcloud')
class PlayersWordCloudView(PlayersViewWithQueryParam):
    @ns.doc(description='get a player wordcloud')
    def get(self, account_id):
        super().get(account_id=account_id, parser=common_parser)
        return self.players.get_player_wordcloud(params=self.args)


@ns.route('/<int:account_id>/refresh')
class PlayersRefresh(Resource):
    @ns.doc('Refresh player match history')
    def post(self, account_id):
        players = Players(account_id=account_id)
        return players.post_player_refesh()
