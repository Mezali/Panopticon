import json

import requests
import urllib3
from flask import render_template, session, flash, redirect, url_for

from aplication import app, mongo
from aplication.forms import RegisterForm, LoginForm, RegisterColaborador
from aplication.functions import fetchBravas

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('listar'))
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = mongo.db.user.find_one({'name': username})

        if user is not None:  # Check if the user exists
            if username == user['name'] and password == user['password']:
                session['username'] = user['name']
                return redirect(url_for('cad_colaborador'))
            else:
                flash('Nome ou senha incorretos!', 'danger')

    return render_template('login.html', form=form)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():  # Checar a porra do login
        user = mongo.db.user.find_one({'name': f'{form.username.data}'})

        if user is None:  # Se não houver usuário cadastrado ele vai cadastrar
            mongo.db.user.insert_one(
                {'name': f'{form.username.data}', 'password': f'{form.password.data}'})
            session['username'] = form.username.data

            return redirect(url_for('index'))
        else:
            flash('Usuário já cadastrado!', 'danger')

    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    session.clear()  # Limpa a sessão do usuário
    flash('Você saiu com sucesso!', 'success')
    return redirect(url_for('login'))


@app.route('/list')
def listar():
    if 'username' in session:
        try:
            response = fetchBravas()

            if response.status_code == 200:
                data = json.loads(response.text)
                user = data["config"]["users"]

                return render_template("list-colaborador.html", users=user)
        except requests.exceptions.RequestException as e:
            message = f"Erro na solicitação: {e}"
            return render_template('error.html', message=message), 500

    else:
        return redirect(url_for('login'))


@app.route('/cad-colaborador', methods=['POST', 'GET'])
def cad_colaborador():
    form = RegisterColaborador()
    if 'username' in session:
        return render_template('cad-colaborador.html', form=form)

    else:
        return redirect(url_for('login'))


@app.route('/del-colaborador', methods=['POST', 'GET'])
def del_colaborador():
    if 'username' in session:
        try:
            response = fetchBravas()

            if response.status_code == 200:
                data = json.loads(response.text)
                user = data["config"]["users"]

                return render_template("del-colaborador.html", users=user)
        except requests.exceptions.RequestException as e:
            message = f"Erro na solicitação: {e}"
            return render_template('error.html', message=message), 500

    else:
        return redirect(url_for('login'))
