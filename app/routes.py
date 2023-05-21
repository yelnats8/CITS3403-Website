from flask import render_template, flash, redirect, url_for, request, session
from app import app, db, socketio
from app.forms import LoginForm, RegisterForm, ResetPassForm, EditProfileForm
from app.models import User, ChatHistory, PersonalChatHistory
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime
import random
import json
import os
from string import ascii_uppercase

rooms = {} #This is a dictionary to keep track of all the chat rooms we have currently
queue = [] #This is a list that represents a queue of rooms for matchmaking to work

#this function generates a 4 letters that acts as a unique room code
def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)
        if code not in rooms:
            break
    return code

#this function generates a prompt from a json file filled with prompts
def generate_prompt():
    path = os.getcwd()+"/prompts.json"
    print(path)
    try:
        with open("prompts.json", 'r') as file:
            content = file.read()
            prompts = json.loads(content)
            prompt = prompts["prompts"][random.randint(0,len(prompts["prompts"])-1)]
        return prompt
    except:
        print("failed to open file")
        return "No prompt found"

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == "POST":

        if current_user.is_authenticated:
            name = current_user.username
            code = request.form.get("roomCode")

            join = request.form.get("join", False)
            create = request.form.get("create", False)
            questionsMode = request.form.get("questionsMode", False)

            if join != False:
                if not code:
                    flash('Please enter a room code')
                    return render_template('home.html', title = 'Home')
                elif code not in rooms:
                    flash('Room ' +code+ ' does not exist')
                    return render_template('home.html', title = 'Home')
                session["room"] = code
                session["prompt"] = ChatHistory.query.filter_by(room_code = code).first().prompt
                return redirect(url_for('chat'))
                
            room = code
            if create != False:
                room = generate_unique_code(4)
                prompt = generate_prompt()
                rooms[room] = {"members": 0, "messages": [], "usernames": [], "prompt": prompt}

                session["room"] = room
                session["prompt"] = prompt
                return redirect(url_for('chat'))
            
            if questionsMode != False:
                if len(queue) > 0:
                    room = queue[0]
                    session["room"] = room
                    session["prompt"] = rooms[room]["prompt"]
                    queue.pop(0)
                    return redirect(url_for('chat'))
                else:
                    room = generate_unique_code(4)
                    prompt = generate_prompt()
                    rooms[room] = {"members": 0, "messages": [], "usernames": [], "prompt": prompt}

                    queue.append(room)
                    session["room"] = room
                    session["prompt"] = prompt
                    return redirect(url_for('chat'))
            

        else:
            flash('Please log in')
            return render_template('home.html', title = 'Home')

    return render_template('home.html', title = 'Home')

@app.route('/chat')
def chat():
    """
    if room is None or room not in rooms:
        return redirect(url_for("home"))
    """
    history = ChatHistory.query.filter_by(room_code = session["room"])
    return render_template("chat.html", history = history)

@app.route('/history')
def history():
    history = PersonalChatHistory.query.filter_by(username = current_user.username).group_by(PersonalChatHistory.room_code).order_by(PersonalChatHistory.date.desc())
    return render_template("history.html", history = history)

@app.route('/chathistory/<username>/<room_code>')
def chathistory(username,room_code):
    history = PersonalChatHistory.query.filter_by(username = username, room_code = room_code)
    return render_template("chathistory.html", history = history)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home')) 
    return render_template('login.html', title='Log In', form=form)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username = form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created')
        return redirect(url_for('login'))
    return render_template('register.html', title ='Register', form=form)

@app.route('/reset', methods = ['GET', 'POST'])
def reset():
    form = ResetPassForm()
  
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash("Account doesn't exist")
            return redirect(url_for("home"))
        
        if not user.check_password(form.password.data):
            flash("Incorrect password")
            return redirect(url_for("reset"))

        user.set_password(form.new_password.data)
        db.session.commit()
        logout_user()
        return redirect(url_for('login'))
    
    return render_template('reset.html', title ='Register', form=form)

@app.route('/user/<username>')  #Following tutorial 
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body' : 'Test post #2'}
    ]
    return render_template('user.html',user=user,posts=posts)

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/edit_profile', methods=['GET','POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
       # flash ('Your changes have been saved.')
        return redirect(url_for('user', username=current_user.username))   #can change to edit_profile so pop up doesnt look ugly of saved changes. or just remove the flash
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',form=form)