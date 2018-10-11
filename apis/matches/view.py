from flask_restplus import Resource, Namespace

from apis.matches.matches import Matches

ns = Namespace('matches')


@ns.route('/<int:match_id>')
class MatchesView(Resource):
    @ns.doc(description='get all ProPlayers')
    def get(self, match_id):
        matches = Matches(match_id)
        return matches.get_match()
