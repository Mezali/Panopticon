from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
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


class RegisterColaborador(FlaskForm):
    nome = StringField('Nome:', validators=[DataRequired()])
    matricula = StringField('Matricula:', validators=[DataRequired()])
    cartao = StringField('Cartao:', validators=[DataRequired()])
    seg_sex = BooleanField('Segunda a Sexta')
    sab = BooleanField('Sábado')
    dom = BooleanField('Domingo')
    cafe_manha = BooleanField('Café da Manhã')
    cafe_tarde = BooleanField('Café da Tarde')
    almoco = BooleanField('Almoço')
    janta = BooleanField('Janta')
    submit = SubmitField('Cadastrar')
