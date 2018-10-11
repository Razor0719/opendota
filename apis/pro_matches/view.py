from flask_restplus import Resource, Namespace, reqparse

from apis.pro_matches.pro_matches import ProMatches

ns = Namespace('proMatches')

parser = reqparse.RequestParser()
parser.add_argument('less_than_match_id', type=int, required=False,
                    help='Get matches with a match ID lower than this value')


@ns.route()
@ns.param('less_than_match_id', 'Get matches with a match ID lower than this value', )
class ProPlayersView(Resource):
    @ns.doc(description='get all ProPlayers')
    def get(self):
        args = parser.parse_args()
        print(args)
        proPlayers = ProMatches()
        return proPlayers.get_all(params=args)
