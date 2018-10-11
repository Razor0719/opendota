from flask import Flask, Blueprint
from flask_restplus import Api

from apis.players.view import ns as playersView
from apis.pro_matches.view import ns as proMatchesView
from apis.pro_players.view import ns as proPlayersView

app = Flask(__name__)
bp = Blueprint('OPEN DOTA', __name__, url_prefix='/api')
api = Api(bp, version='1.0', title='OPENDOTA API')
api.add_namespace(ns=proPlayersView)
api.add_namespace(ns=proMatchesView)
api.add_namespace(ns=playersView)
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)
