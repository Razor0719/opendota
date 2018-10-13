from flask_restplus import Namespace, Resource, reqparse

from apis.benchmarks.benchmarks import Benchmarks

ns = Namespace('benchmarks')
parser = reqparse.RequestParser()
parser.add_argument('hero_id', required=True,
                    help='Hero ID')


@ns.route('')
@ns.param('hero_id', 'Hero ID', required=True)
class BenchmarksView(Resource):
    @ns.doc(description='Benchmarks of average stat values for a hero')
    def get(self):
        args = parser.parse_args()
        benchmarks = Benchmarks()
        return benchmarks.get_benchmarks(params=args)
