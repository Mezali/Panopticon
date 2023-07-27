from flask import render_template
from pymongo.errors import PyMongoError

from aplication import app, mongo


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/market')
def market():
    try:
        items_cursor = mongo.db.item.find()
        items = list(items_cursor)
        return render_template('market.html', items=items)
    except PyMongoError:
        message = 'An unexpected error occur while fetching data from the database.'
        return render_template('error.html', message=message), 500
