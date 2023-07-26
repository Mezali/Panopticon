from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    barcode = db.Column(db.String(100), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1024), nullable=False)


db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/market')
def market():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '1', 'price': 500},
        {'id': 2, 'name': 'Tablet', 'barcode': '2', 'price': 1000},
        {'id': 3, 'name': 'Laptop', 'barcode': '3', 'price': 2000}
    ]

    return render_template('market.html', items=items)


if __name__ == '__main__':
    app.run()
