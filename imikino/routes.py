from flask import render_template, flash, redirect, url_for
from imikino import app, database, bcrypt
from imikino.forms import FormLogin, FormCriarConta
from imikino.models import Usuario
from flask_login import login_user, logout_user


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()

    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        #verificar se o usuario e a senha estão corretas
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            #fazer o login
            login_user(usuario, remember=form_login.lembrar_dados.data)
            #fez login com sucesso
            #exibir mensagem de sucesso -> flash
            flash(f'Login feito com sucesso para o e-mail {form_login.email.data}', 'alert-primary') #.data serve para pegar o que a pessoa escreveu no campo de texto
            #redirecionar para a home page -> redirect
            return redirect(url_for('home'))
        else:
            flash(f'Falha no Login. E-mail ou Senha Incorretos', 'alert-danger')
    return render_template('login.html', form_login=form_login)

@app.route('/criar-conta', methods=['GET', 'POST'])
def criarConta():
    form_criarconta = FormCriarConta()

    if form_criarconta.validate_on_submit():
        #criptografar a senha
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        #criar o Usuario
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        #adicionar a sessão
        database.session.add(usuario)
        #commitar a sessão
        database.session.commit()
        #-----------------------
        #fez login com sucesso
        #exibir mensagem de sucesso -> flash
        flash(f'Bem-vindo(a) ao time {form_criarconta.username.data}, conta criada com sucesso', 'alert-primary') #.data serve para pegar o que a pessoa escreveu no campo de texto
        #redirecionar para a home page -> redirect
        return redirect(url_for('home'))

    return render_template('criarConta.html', form_criarconta=form_criarconta)

@app.route('/sair')
def sair():
    logout_user()
    flash(f'Logout feito com sucesso, até logo', 'alert-primary')
    return redirect(url_for('home'))

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')
