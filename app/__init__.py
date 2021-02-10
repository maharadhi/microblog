from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# module declaration at bottom to avoid circular dependency
from app import routes
