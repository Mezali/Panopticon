from flask import render_template

from aplication import app, mongo


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/market')
def market():
    items_cursor = mongo.db.item.find()
    items = list(items_cursor)

    return render_template('market.html', items=items)
