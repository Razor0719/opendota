from flask_restplus import Namespace, Resource

from apis.distributions.distributions import Distributions

ns = Namespace('distributions')


@ns.route('')
class DistributionsView(Resource):
    @ns.doc(description='Distributions of MMR data by bracket and country')
    def get(self):
        distributions = Distributions()
        return distributions.get_distributions()
