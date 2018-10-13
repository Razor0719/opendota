from flask_restplus import Namespace, Resource, reqparse

from apis.rankings.rankings import Rankings

ns = Namespace('rankings')
parser = reqparse.RequestParser()
parser.add_argument('hero_id', required=True,
                    help='Hero ID')


@ns.route('')
@ns.param('hero_id', 'Hero ID', required=True)
class RankingsView(Resource):
    @ns.doc(description='Top players by hero')
    def get(self):
        args = parser.parse_args()
        rankings = Rankings()
        return rankings.get_rankings(params=args)
