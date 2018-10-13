from flask_restplus import Namespace, Resource, reqparse

from apis.explorer.explorer import Explorer

ns = Namespace('explorer')
parser = reqparse.RequestParser()
parser.add_argument('sql', required=False,
                    help='The PostgreSQL query as percent-encoded string.')


@ns.route('')
@ns.param('sql', 'The PostgreSQL query as percent-encoded string.')
class ExplorerView(Resource):
    @ns.doc(description='Submit arbitrary SQL queries to the database')
    def get(self):
        explorer = Explorer()
        return explorer.to_explorer()
