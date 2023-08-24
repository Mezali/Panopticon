import bcrypt
from flask import render_template, session, flash, redirect, url_for
from pymongo.errors import PyMongoError

from aplication import app, mongo
from aplication.forms import RegisterForm


@app.route('/')
def index():
    # if 'username' in session:
    #    return flash(f"Você está logado como, {session['username']}")
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():  # To check if the form is valid
        user = mongo.db.user.find_one({'name': f'{form.username.data}'})
        if user is None:  # If there's no user in the database, it will create a new user
            email_address = form.email_address.data
            print(email_address)
            hashpass = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
            mongo.db.user.insert_one(
                {'name': f'{form.username.data}', 'password': f'{hashpass}', 'email': f'{email_address}'})
            session['username'] = user
            return redirect(url_for('index'))
        else:
            flash('Usuário já cadastrado!', 'danger')

    return render_template('register.html', form=form)


@app.route('/list')
def list_nvr():
    try:
        items_cursor = mongo.db.item.find()
        items = items_cursor
        return render_template('list.html', items=items)
    except (PyMongoError, AttributeError):
        message = 'An unexpected error occur while displaying this page :(.'
        return render_template('error.html', message=message), 500
