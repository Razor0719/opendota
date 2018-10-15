from flask_restplus import Namespace, Resource

from apis.health.health import Health

ns = Namespace('health')


@ns.route('')
class HealthView(Resource):
    @ns.doc(description='Get service health data')
    def get(self):
        health = Health()
        return health.get_health()
