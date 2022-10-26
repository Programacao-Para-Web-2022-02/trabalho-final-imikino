from flask_wtf import FlaskForm #classe pronta do Flask para criação de formulários
from wtforms import StringField, PasswordField, SubmitField, BooleanField #wtforms vem junto com o flask_wtf -> estamos importando o que vamos colocar nos campos abaixo
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError  #VALIDADORES ... DataRequired -> Campo Obrigatório | Length -> Tamanho mínimo de um campo | Email -> Verificar se é um email válido | EqualTo -> Verificar se um campo é igual ao outro (no caso o de senha)
from imikino.models import Usuario


class FormCriarConta(FlaskForm):
    username = StringField('Nickname', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta =  SubmitField('Criar Conta')

    def validate_email(self, email): #obrigatoriamente tem que ser validate_ o inicio da sua função pq o validate_on_submite ele toda automaticamente todas as funções que começam  com valite_ -> Essa função faz com que valide se não tem emails repetidos no banco de dados
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Esse E-mail já foi cadastrado. Tente usar outro e-mail para continuar")
    
    def validate_username(self, username):
        usuario = Usuario.query.filter_by(username=username.data).first()
        if usuario:
            raise ValidationError("Esse nickname já foi cadastrado. Tente usar outro nick para continuar")


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados')
    botao_submit_login =  SubmitField('Fazer Login')