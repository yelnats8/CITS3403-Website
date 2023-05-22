from flask import render_template, flash, redirect, url_for, request, session
from app import app, db, socketio
from app.forms import LoginForm, RegisterForm, ResetPassForm, EditProfileForm
from app.models import User, ChatHistory, Post, PersonalChatHistory
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime
import random
import os
from werkzeug.utils import secure_filename
import json
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
    history = ChatHistory.query.filter_by(room_code = session["room"])
    return render_template("chat.html", history = history)

@app.route('/history')
def history():
    history = PersonalChatHistory.query.filter_by(user_id = current_user.id).group_by(PersonalChatHistory.room_code).order_by(PersonalChatHistory.date.desc())
    return render_template("history.html", history = history)

@app.route('/chathistory/<username>/<room_code>')
def chathistory(username,room_code):
    history = PersonalChatHistory.query.filter_by(user_id = current_user.id, room_code = room_code)
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

@app.route('/user/<username>', methods=['GET', 'POST'])  #Adding comments
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    if request.method == 'POST':
        post_body = request.form['post_body']
        post_length = Post.get_post_length(post_body)
        if not Post.validate_post_length(post_body):
            flash(f'Post Exceeds maximum length of 200 characters. Current length: {post_length} ')
        else:
            new_post = Post(body=post_body, timestamp=datetime.utcnow(), author=current_user, profile=user)
            db.session.add(new_post)
            db.session.commit()

    posts = Post.query.filter_by(profile_id=user.id).order_by(Post.timestamp.asc()).all()
    return render_template('user.html',user=user,posts=posts)


@app.route('/user/<username>/post/<post_id>/delete', methods=['POST'])
@login_required
def delete_post(username, post_id):
    user = User.query.filter_by(username=username).first_or_404()
    post = Post.query.get(post_id)

    if post and post.author_id == current_user.id:
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('user', username=username))



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

        if form.avatar.data:
            file = form.avatar.data
            max_file_size = 10 * 1024 * 1024  # 10 MB (example value, adjust as needed)
            file_data = file.read()  # Read the file data into memory
            file_size = len(file_data)
            if file_size > max_file_size:
                flash ('File Size exceeds the allowed limit of 10mb!')
                return redirect(url_for('edit_profile'))
            else:
                file.seek(0)  #reset pointer so there are no issues

            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            current_user.avatar_path = 'avatars/' + filename
        
        db.session.commit()
        return redirect(url_for('user', username=current_user.username))   #can change to edit_profile so pop up doesnt look ugly of saved changes. or just remove the flash
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',form=form)

@app.route('/others')
def all_users():
    users = User.query.all() 
    return render_template('Others.html', users=users)

@app.route('/search', methods=['GET'])
@login_required
def search():
    search_username = request.args.get('username')
    if search_username:
        return redirect(url_for('user', username=search_username))
    else:
        flash('Please enter a username to search for.')
        return redirect(url_for('user'))

    