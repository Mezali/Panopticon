from flask import Flask
from flask_pymongo import PyMongo

# Import configuration variables from config.py
from config import VARS

app = Flask(__name__)
app.config.from_object(VARS)
mongo = PyMongo(app)

from aplication import routes

