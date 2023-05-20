from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = "/Users/RatKing/CITS3403-Website/CITS3403-Website/app/static/avatars"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
socketio = SocketIO(app)

from app import routes, models, chat