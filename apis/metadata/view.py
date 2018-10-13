from flask_restplus import Namespace, Resource

from apis.metadata.metadata import Metadata

ns = Namespace('metadata')


@ns.route('')
class MetadataView(Resource):
    @ns.doc(description='Site metadata')
    def get(self):
        metadata = Metadata()
        return metadata.get_metadata()
