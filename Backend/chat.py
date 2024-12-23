from flask_socketio import SocketIO, emit, join_room, leave_room, emit
from Backend.app1 import socketio

socketio = SocketIO()

@socketio.on("join_room")
def handle_join_room_event(data):
    username = data["username"]
    room = data["room"]
    join_room(room)
    emit("message", {"message": f"{username} a rejoint la salle {room}."}, to=room)

@socketio.on("leave_room")
def handle_leave_room_event(data):
    username = data["username"]
    room = data["room"]
    leave_room(room)
    emit("message", {"message": f"{username} a quitté la salle {room}."}, to=room)

@socketio.on("message")
def handle_message_event(data):
    room = data["room"]
    message = data["message"]
    emit("message", {"message": message}, to=room)
