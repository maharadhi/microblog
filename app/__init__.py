from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

# setup DB
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# module declaration at bottom to avoid circular dependency
from app import routes, models
