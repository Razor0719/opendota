from flask_restplus import Namespace, Resource

from apis.status.status import Status

ns = Namespace('status')


@ns.route('')
class StatusView(Resource):
    @ns.doc(description='Get current service statistics')
    def get(self):
        status = Status()
        return status.get_status()

# @ns.route('/admin/apiMetrics')
# class ApiMetricsView(Resource):
#     @ns.doc(description='Get API request metrics')
#     def get(self):
#         status = Status()
#         return status.get_apiMetrics()
