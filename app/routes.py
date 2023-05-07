from flask import render_template, flash, redirect, url_for, request, session
from app import app, db, socketio
from app.forms import LoginForm, RegisterForm, ResetPassForm
from app.models import User
from flask_login import current_user, login_user, logout_user


import random
from string import ascii_uppercase
rooms = {} #This is a dictionary to keep track of all the chat rooms we have currently, we should implement this into a database at some point

def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)
        if code not in rooms:
            break
    return code

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        if current_user.is_authenticated:
            name = current_user.username
            code = request.form.get("roomCode")
            join = request.form.get("join", False)
            create = request.form.get("create", False)

            if join != False:
                """
                if not code:
                    flash('Please enter a room code')
                    return render_template('home.html', title = 'Home')
                elif code not in rooms:
                    flash('Room ' +code+ ' does not exist')
                    return render_template('home.html', title = 'Home', roomCode=code)
                """
                session["room"] = code
                return redirect(url_for('chat'))
                

            room = code
            if create != False:
                room = generate_unique_code(4)
                rooms[room] = {"members": 0, "messages": []}

                session["room"] = room
                return redirect(url_for('chat'))
            

        else:
            flash('Please log in')
            return render_template('home.html', title = 'Home')

    return render_template('home.html', title = 'Home')

@app.route('/chat')
def chat():
    room = session.get("room")
    """
    if room is None or room not in rooms:
        return redirect(url_for("home"))
    """
    return render_template("chat.html")


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

