from flask import Flask, Blueprint
from flask_restplus import Api

from apis.matches.view import ns as matchesView
from apis.players.view import ns as playersView
from apis.pro_matches.view import ns as proMatchesView
from apis.pro_players.view import ns as proPlayersView
from apis.public_matches.view import ns as publicMatchesView
from apis.explorer.view import ns as explorerView
from apis.metadata.view import ns as metadataView
from apis.distributions.view import ns as distributionsView
from apis.search.view import ns as searchView
from apis.rankings.view import ns as rankingsView
from apis.benchmarks.view import ns as benchmarksView
from apis.status.view import ns as statusView
from apis.health.view import ns as healthView

app = Flask(__name__)
bp = Blueprint('OPEN DOTA', __name__, url_prefix='/api')
api = Api(bp, version='1.0', title='OPENDOTA API')
api.add_namespace(ns=matchesView)
api.add_namespace(ns=playersView)
api.add_namespace(ns=proPlayersView)
api.add_namespace(ns=proMatchesView)
api.add_namespace(ns=publicMatchesView)
api.add_namespace(ns=explorerView)
api.add_namespace(ns=metadataView)
api.add_namespace(ns=distributionsView)
api.add_namespace(ns=searchView)
api.add_namespace(ns=rankingsView)
api.add_namespace(ns=benchmarksView)
api.add_namespace(ns=statusView)
api.add_namespace(ns=healthView)

app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)
