from flask import Flask
from flask_cors import CORS

from api.v1.api_v1 import api as api_v1
from utilities.utilities import Utils
from api.v1.sockets import socketio

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

socketio.init_app(app)
Utils.create()

app.register_blueprint(api_v1, url_prefix='/api/v1')

if __name__ == '__main__':
    #app.run()
    socketio.run(app)

