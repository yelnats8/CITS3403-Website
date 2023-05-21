from flask import render_template, session
from flask_socketio import SocketIO, send, join_room, leave_room, emit
from app import socketio, db
from app.routes import rooms, queue
from flask_login import current_user
from app.models import ChatHistory, User, PersonalChatHistory
from datetime import datetime


#WHEN USER FIRST JOINS CHAT
@socketio.on("joined", namespace="/chat")
def joined(msg):
    room = session.get("room")
    prompt = session.get("prompt")
    
    if current_user.username in rooms[room]["usernames"]:
        join_room(room)
        return
    else:
        rooms[room]["usernames"].append(current_user.username)

    join_room(room)
    connect_msg =' has entered the room.'
    emit('status', {'user': current_user.username, 'msg': connect_msg}, room=room)
    
    rooms[room]["messages"].append(connect_msg)

    history = ChatHistory(message = connect_msg, room_code = room, prompt = prompt, sender=current_user.username, date= datetime.utcnow())
    db.session.add(history)
    db.session.commit()
    rooms[room]["members"] +=1
    
    members = rooms[room]["members"]
    
    print(f"room {room} now has {members} members")
    print(f"{current_user.username} has joined room {room}")

#WHEN USER SENDS A MESSAGE
@socketio.on("text", namespace="/chat")
def text(messages):
    room = session.get("room")
    prompt = session.get("prompt")

    if current_user.username not in rooms[room]["usernames"]:
        rooms[room]["usernames"].append(current_user.username)

    msg = messages['msg']

    history = ChatHistory(message = msg, room_code = room, prompt = prompt, sender= current_user.username, date= datetime.utcnow())
    db.session.add(history)
    db.session.commit()

    rooms[room]["messages"].append(msg)
    emit('message', {'user': current_user.username,'msg': msg}, room = room)
    print(f"{msg} on room {room}")

#WHEN USER LEAVES CHAT
@socketio.on('leave', namespace="/chat")
def leave(message):
    room = session.get("room")
    prompt = session.get("prompt")
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -= 1
        members = rooms[room]["members"]
        print(f"room {room} now has {members} members")

        msg = ' has left the room'
        emit('status', {'user': current_user.username, 'msg': ' has left the room.'}, room = room)
        rooms[room]["messages"].append(current_user.username + ' has left the room.')

        history = ChatHistory(message = msg, room_code = room, prompt = prompt, sender= current_user.username, date= datetime.utcnow())
        db.session.add(history)
        db.session.commit()

        PersonalChatHistory.query.filter_by(room_code = room, username=current_user.username).delete()
        history = ChatHistory.query.filter_by(room_code = room)

        for log in history:
            personal_history = PersonalChatHistory(message = log.message, room_code = log.room_code, username = current_user.username, prompt= log.prompt, date = log.date)
            db.session.add(personal_history)
        db.session.commit()

        rooms[room]["usernames"].pop(rooms[room]["usernames"].index(current_user.username))

        if rooms[room]["members"] <= 0:
            del rooms[room]
            ChatHistory.query.filter_by(room_code = room).delete()
            db.session.commit()
            if room in queue:
                queue.pop(queue.index(room))
            print(f"room {room} has been deleted")



    
    print(f"{current_user.username} has left room {room}")
    