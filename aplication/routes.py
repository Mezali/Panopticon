import bcrypt
from flask import render_template, session, flash, redirect, url_for
from pymongo.errors import PyMongoError

from aplication import app, mongo
from aplication.forms import RegisterForm, LoginForm


@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():  # Checar a porra do login
        user = mongo.db.user.find_one({'name': f'{form.username.data}'})

        if user is None:  # Se não houver usuário cadastrado ele vai cadastrar
            hashpass = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
            mongo.db.user.insert_one(
                {'name': f'{form.username.data}', 'password': f'{hashpass}'})
            session['username'] = form.username.data

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
        message = 'Um erro ocorreu em quanto essa pagina carregava 🙁'
        return render_template('error.html', message=message), 500
