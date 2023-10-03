import json

import requests
import urllib3
from flask import render_template, session, flash, redirect, url_for, request, jsonify

from aplication import app, mongo
from aplication.forms import RegisterForm, LoginForm

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

        if username == user['name'] and password == user['password']:
            session['username'] = user['name']
            return redirect(url_for('index'))
        else:
            return f"não foi {password} {username} {user['password']}"
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
            url = "https://192.168.10.4:8090/portaria/v1/bravas/config/user/"

            payload = json.dumps({
                "config": {
                    "action": "getUserList",
                    "mode": 0,
                    "start": 0,
                    "size": 999999
                }
            })
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload, verify=False)

            if response.status_code == 200:
                data = json.loads(response.text)
                user = data["config"]["users"]

                return render_template("list.html", users=user)
        except requests.exceptions.RequestException as e:
            message = f"Erro na solicitação: {e}"
            return render_template('error.html', message=message), 500

    else:
        return redirect(url_for('login'))


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    data = request.get_json()
    user_id = data.get('user_id')  # Obtém o ID do usuário do JSON

    # Execute a lógica para excluir o usuário com o ID fornecido
    # Substitua esta linha pelo código real de exclusão do usuário

    # Responda com uma mensagem de confirmação ou status
    response_data = {"message": f"Usuário com ID {user_id} excluído com sucesso"}
    return jsonify(response_data)
