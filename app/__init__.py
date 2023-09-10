# app/__init__.py

from flask import Flask
from flask_pymongo import PyMongo
from config import MONGO_URI

app = Flask(__name__)
app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)

# Register blueprints (controllers)
from app.controllers import user_controller
app.register_blueprint(user_controller.user_bp)
