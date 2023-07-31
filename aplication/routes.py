from flask import render_template
from pymongo.errors import PyMongoError

from aplication import app, mongo
from aplication.forms import RegisterForm


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/list')
def list_nvr():
    try:
        items_cursor = mongo.db.item.find()
        items = items_cursor
        return render_template('list.html', items=items)
    except (PyMongoError, AttributeError):
        message = 'An unexpected error occur while displaying this page :(.'
        return render_template('error.html', message=message), 500


@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)
