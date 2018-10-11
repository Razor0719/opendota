from flask_restplus import Resource, Namespace, reqparse

from apis.public_matches.public_matches import PublicMatches

ns = Namespace('publicMatches')

parser = reqparse.RequestParser()
parser.add_argument('mmr_ascending', type=int, required=False,
                    help='Order by MMR ascending')
parser.add_argument('mmr_descending', type=int, required=False,
                    help='Order by MMR descending')
parser.add_argument('less_than_match_id', type=int, required=False,
                    help='Get matches with a match ID lower than this value')


@ns.route('')
@ns.param('mmr_ascending','Order by MMR ascending')
@ns.param('mmr_descending','Order by MMR descending')
@ns.param('less_than_match_id', 'Get matches with a match ID lower than this value', )
class ProPlayersView(Resource):
    @ns.doc(description='get all ProPlayers')
    def get(self):
        args = parser.parse_args()
        print(args)
        publicMatches = PublicMatches()
        return publicMatches.get_publicMatches(params=args)
