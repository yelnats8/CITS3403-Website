from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
socketio = SocketIO(app)

from app import routes, models, chat

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    #Don't do this
    db = SQLAlchemy(app)
    db.init_app(app)