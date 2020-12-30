from flask_socketio import SocketIO, emit
import json

from utilities.token import verify

socketio = SocketIO(cors_allowed_origins="*")

#@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
@socketio.on('connect')
def connect():
    print("server connect")

@socketio.on("message")
def handle_message(message):
    print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
    authDetail = json.loads(message)

    if authDetail["type"] != "authorization":
        print("Socket server close")

    verify(authDetail["payload"]["token"])
