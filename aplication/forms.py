from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username = StringField('Nome:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired()])
    password = PasswordField('Senha:', validators=[DataRequired()])
    password_confirmation = PasswordField('Confirmar senha:', validators=[DataRequired()])
    submit = SubmitField('Registar')
