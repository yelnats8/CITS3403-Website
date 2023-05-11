from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm, RegisterForm, ResetPassForm
from app.models import User
from flask_login import current_user, login_user, logout_user

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'ELMO')


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
