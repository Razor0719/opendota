from flask_restplus import Namespace, Resource, reqparse

from apis.search.search import Search

ns = Namespace('search')
parser = reqparse.RequestParser()
parser.add_argument('q', required=True,
                    help='Search string')


@ns.route('')
@ns.param('q', 'Search string', required=True)
class SearchView(Resource):
    @ns.doc(description='Search players by personaname.')
    def get(self):
        args = parser.parse_args()
        search = Search()
        return search.search(params=args)
