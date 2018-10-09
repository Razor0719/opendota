from flask_restplus import Resource, Namespace

from apis.pro_matches.pro_matches import ProMatches

ns = Namespace('proMatches')


@ns.route('/')
class ProPlayersView(Resource):
    @ns.doc(description='get all ProPlayers')
    def get(self):
        proPlayers = ProMatches()
        return proPlayers.get_all()
