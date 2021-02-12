from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

# setup DB
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# create login instance
login = LoginManager(app)
login.login_view = 'login'

# module declaration at bottom to avoid circular dependency
from app import routes, models, errors
