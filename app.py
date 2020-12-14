from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO, emit

from api.v1.api_v1 import api as api_v1
from utilities import Utils

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['CORS_HEADERS'] = 'Content-Type'
socketi = SocketIO(app, cors_allowed_origins="*")
CORS(app)

Utils.create()

app.register_blueprint(api_v1, url_prefix='/api/v1')

@socketi.on('connect')
def test_connect():
    emit('after connect',  'abc')
    print("a")

if __name__ == '__main__':
    # app.run()
    socketi.run(app)

