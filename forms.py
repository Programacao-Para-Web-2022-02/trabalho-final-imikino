from flask_wtf import FlaskForm #classe pronta do Flask para criação de formulários
from wtforms import StringField, PasswordField, SubmitField, BooleanField #wtforms vem junto com o flask_wtf -> estamos importando o que vamos colocar nos campos abaixo
from wtforms.validators import DataRequired, Length, Email, EqualTo  #VALIDADORES ... DataRequired -> Campo Obrigatório | Length -> Tamanho mínimo de um campo | Email -> Verificar se é um email válido | EqualTo -> Verificar se um campo é igual ao outro (no caso o de senha)


class FormCriarConta(FlaskForm):
    username = StringField('Nickname', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta =  SubmitField('Criar Conta')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados')
    botao_submit_login =  SubmitField('Fazer Login')