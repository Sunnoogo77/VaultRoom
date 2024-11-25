from flask_socketio import SocketIO, emit, join_room, leave_room
from app import socketio

@socketio.on('join_room')
def handle_join_room_event(data):
    app.logger.info(f"{data['username']} joined room {data['room']}")
    join_room(data['room'])
    emit('join_room_announcement', data, to=data['room'])

@socketio.on('send_message')
def handle_send_message_event(data):
    app.logger.info(f"{data['username']} sent message to room {data['room']}: {data['message']}")
    emit('receive_message', data, to=data['room'])
