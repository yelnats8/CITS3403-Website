from flask import render_template, session
from flask_socketio import SocketIO, send, join_room, leave_room
from app import socketio
from app.routes import rooms
from flask_login import current_user

@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    if current_user.is_authenticated:
        name = current_user.username
    else:
        name = current_user
    if not room or not name:
        return
    if room not in rooms:
        leave_room(room)
        return
    
    join_room(room)
    send({"name": name, "message": "has entered the room"},roomCode = room, to=room)
    rooms[room]["members"] +=1
    print(f"{current_user} joined the room {room}")

   
@socketio.on("disconnect")
def disconnect ():
    room = session.get("room")
    name = current_user.username
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room]
            print(f"room {room} has been deleted")

    send({"name": name, "message": "has left the room"}, to=room)

    print(f"{current_user} left the room {room}")

@socketio.on("message")
def message(data):
    room = session.get("room")
    name = current_user.username
    if room not in rooms:
        return
    
    content = {
        "name": name,
        "message": data["data"]
    }
    send(content, to=room)
    #rooms[room]["messages"].append(content)
    print(f"{name} said: {data['data']}")