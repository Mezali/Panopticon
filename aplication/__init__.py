from flask import Flask
from flask_pymongo import PyMongo

# Import configuration variables from config.py
from config import VARS

app = Flask(__name__)
app.config['MONGO_URI'] = VARS.MONGO_URI
app.config['SECRET_KEY'] = VARS.SECRET_KEY
mongo = PyMongo(app)

from aplication import routes
