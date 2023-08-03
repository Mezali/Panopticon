from flask import render_template, url_for, redirect
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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        create_user = {
            'name': form.username.data,
            'email': form.email_address.data,
            'password': form.password.data
        }
        mongo.db.user.insert_one(create_user)
        return redirect(url_for('list_nvr'))

    if form.errors != {}:  # If there are not errors from the validation
        for err_msg in form.errors.values():
            print(f'Errors while registering user: {err_msg}')

    return render_template('register.html', form=form)
