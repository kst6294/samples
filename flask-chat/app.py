from flask import Flask
from flask_socketio import SocketIO, join_room, leave_room

app = Flask(__name__)
app.secret_key = ""
socketio = SocketIO(app)


@socketio.on("message")
def handle_message(data):
    room = data.get("room")
    socketio.emit("message", data, room=room)


@socketio.on("join_room")
def handle_join_room(data):
    room = data.get("room")
    join_room(room)
    socketio.emit("join_room", data, room=room)


@socketio.on("leave_room")
def handle_leave_room(data):
    room = data.get("room")
    leave_room(room)
    socketio.emit("leave_room", data, room=room)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5100, debug=True)
