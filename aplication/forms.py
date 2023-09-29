from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('Nome:', validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField('Senha:', validators=[DataRequired(), Length(min=6)])
    password_confirmation = PasswordField('Confirmar senha:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Registar')


class LoginForm(FlaskForm):
    username = StringField('Nome:', validators=[DataRequired()])
    password = PasswordField('Senha:', validators=[DataRequired()])
    submit = SubmitField(label='Entrar')
