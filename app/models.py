from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
from datetime import datetime


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow())
    

    def __repr__(self):
        return '<User {}>'.format(self.username)    
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
            return check_password_hash(self.password_hash, password)
    def avatar(self, size):
         digest = md5(self.username.lower().encode('utf-8')).hexdigest()
         return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)   
    
class ChatHistory(db.Model):
    chat_id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(64))
    room_code = db.Column(db.String(4))
    message = db.Column(db.String(500))
    prompt= db.Column(db.String(100))

class PersonalChatHistory(db.Model):
    chat_id = db.Column(db.Integer, primary_key=True)
    room_code = db.Column(db.String(4))
    prompt = db.Column(db.String(100))
    username = db.Column(db.String(64))
    message = db.Column(db.String(500))