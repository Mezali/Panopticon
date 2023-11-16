import json

import requests
import urllib3
from flask import render_template, session, flash, redirect, url_for, request, jsonify

from application import app, mongo
from application.forms import RegisterForm, LoginForm, RegisterColaborador, EditColaborador
from application.functions import fetchbravas, insertbravas, editkit, delbravas, seluser, editbravas

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ip = app.config['BRAVAS_IP']


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


@app.route('/cad-colaborador', methods=['POST', 'GET'])
def cad_colaborador():
    if 'username' in session:
        form = RegisterColaborador()
        if form.validate_on_submit():
            nome = form.nome.data
            matricula = form.matricula.data
            cartao = form.cartao.data
            seg_sex = form.seg_sex.data
            sab = form.sab.data
            dom = form.dom.data
            cafe_manha = form.cafe_manha.data
            almoco = form.almoco.data
            cafe_pendura = form.cafe_pendura.data
            cafe_tarde = form.cafe_tarde.data
            janta = form.janta.data

            try:
                response = insertbravas(ip, nome, matricula, cartao, seg_sex, sab, dom, cafe_manha, almoco,
                                        cafe_pendura,
                                        cafe_tarde,
                                        janta)
            except requests.exceptions.RequestException as e:
                message = f"Erro na solicitação: {e}"
                return render_template('error.html', message=message), 500

            if response.status_code == 200:
                flash('Colaborador registrado com sucesso!', 'success')
            else:
                flash('Erro ao registrar colaborador! Verifique se o mesmo já foi registrado', 'danger')

        return render_template('cad-colaborador.html', form=form)
    else:
        return redirect(url_for('login'))


@app.route('/list')
def listar():
    if 'username' in session:
        try:
            response = fetchbravas(ip)

            if response.status_code == 200:
                data = json.loads(response.text)
                user = data["config"]["users"]

                return render_template("list-colaborador.html", users=user)
        except requests.exceptions.RequestException as e:
            message = f"Erro na solicitação: {e}"
            return render_template('error.html', message=message), 500

    else:
        return redirect(url_for('login'))


@app.route('/kit-colaborador', methods=['POST', 'GET'])
def kit_colaborador():
    if 'username' not in session:
        return redirect(url_for('login'))

    try:
        response = fetchbravas(ip)

        if response.status_code != 200:
            message = f"Erro na solicitação: {response.text}"
            return render_template('error.html', message=message), 500

        data = json.loads(response.text)
        users = data["config"]["users"]

        user_selections = request.form.getlist('user_selection[]')
        user_info_values = request.form.getlist('user_info[]')

        for selected, user_info in zip(user_selections, user_info_values):
            print(f'Selecionado: {selected}, User Info: {user_info}')

        return render_template("kit-colaborador.html", users=users)
    except requests.exceptions.RequestException as e:
        message = f"Erro na solicitação: {e}"
        return render_template('error.html', message=message), 500


@app.route('/kitedit', methods=['POST'])
def kitedit():
    data = request.get_json()

    for items in data:
        nome = items.get("nome")
        estado = items.get("estado")
        editkit(ip=ip, nome=nome, estado=estado)

    resposta = {'message': 'Processado com sucesso!'}
    return jsonify(resposta)


@app.route('/del-colaborador', methods=['POST'])
def delcolaborador():
    data = request.get_json()
    for items in data:
        nome = items.get("nome")
        delbravas(ip=ip, name=nome)

    resposta = {'message': 'Processado com sucesso!'}
    return jsonify(resposta)


@app.route('/user_info/<string:name>', methods=['POST', 'GET'])
def user_info(name):
    form = EditColaborador()
    info_json = seluser(ip, name)
    info = json.loads(info_json.text)

    if form.validate_on_submit():
        cartao = form.cartao.data
        seg_sex = form.seg_sex.data
        sab = form.sab.data
        dom = form.dom.data
        cafe_manha = form.cafe_manha.data
        almoco = form.almoco.data
        cafe_pendura = form.cafe_pendura.data
        cafe_tarde = form.cafe_tarde.data
        janta = form.janta.data

        response = editbravas(ip, name, tag=cartao, seg_sex=seg_sex, sab=sab, dom=dom, cafe_manha=cafe_manha,
                              almoco=almoco, cafe_pendura=cafe_pendura, cafe_tarde=cafe_tarde, janta=janta)
        if response.status_code == 200:
            flash('Colaborador atualizado com sucesso!', 'success')
        else:
            flash('Erro ao atualizar colaborador!', 'danger')

    return render_template('edit-colaborador.html', name=name, info=info, form=form)
