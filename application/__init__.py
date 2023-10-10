from flask import Flask
from flask_pymongo import PyMongo

# Import configuration variables from config.py
from config import VARS

app = Flask(__name__)
app.config['MONGO_URI'] = VARS.MONGO_URI
app.config['SECRET_KEY'] = VARS.SECRET_KEY
app.config['BRAVAS_IP'] = VARS.BRAVAS_IP
mongo = PyMongo(app)

from application import routes
