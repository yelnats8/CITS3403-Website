from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
from datetime import datetime
from flask import url_for



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
    avatar_path = db.Column(db.String(200))

    posts = db.relationship('Post', backref='author', foreign_keys='Post.author_id')
    profile_posts = db.relationship('Post', backref='profile',foreign_keys ='Post.profile_id')

    @property
    def last_seen_formatted(self):
         return self.last_seen.strftime('%Y-%m-%d %H:%M:%S')
    

    def __repr__(self):
        return '<User {}>'.format(self.username)    
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
            return check_password_hash(self.password_hash, password)
    def avatar(self, size):
         if self.avatar_path:
              return url_for('static', filename=self.avatar_path)
         else:
            digest = md5(self.username.lower().encode('utf-8')).hexdigest()
            return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)   

#This is a temporary table that is always changing as rooms are created and destroyed
class ChatHistory(db.Model):
    chat_id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(64))
    sender_id = db.Column(db.Integer)
    room_code = db.Column(db.String(4))
    message = db.Column(db.String(500))
    message_type = db.Column(db.Integer)
    prompt= db.Column(db.String(100))
    date = db.Column(db.DateTime)

#This is a more permanent database that stores all of a user's chat history before the room code gets overwritten with new ones
class PersonalChatHistory(db.Model):
    chat_id = db.Column(db.Integer, primary_key=True)
    room_code = db.Column(db.String(4))
    prompt = db.Column(db.String(100))
    username = db.Column(db.String(64))
    user_id = db.Column(db.Integer)
    message = db.Column(db.String(500))
    message_type = db.Column(db.Integer)
    date = db.Column(db.DateTime)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    profile_id = db.Column(db.Integer, db.ForeignKey('user.id'))





    def __repr__(self):
        return f"<Post(id={self.id}, body='{self.body}', timestamp={self.timestamp}, author_id ={self.author_id} profile_id={self.profile_id})>"
    
    def validate_post_length(post_body):
        return len(post_body) <= 200
    
    def get_post_length(post_body):
        return len(post_body)


        