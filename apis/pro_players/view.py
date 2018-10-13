from flask_restplus import Resource, Namespace

from apis.pro_players.pro_players import ProPlayers

ns = Namespace('proPlayers')


@ns.route('')
class ProPlayersView(Resource):
    @ns.doc(description='Get list of pro players')
    def get(self):
        proPlayers = ProPlayers()
        return proPlayers.get_all()
