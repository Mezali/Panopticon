from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegisterForm(FlaskForm):
    username = StringField('Nome:', validators=[DataRequired(), Length(min=2, max=50)])
    email_address = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Senha:', validators=[DataRequired(), Length(min=6)])
    password_confirmation = PasswordField('Confirmar senha:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Registar')
