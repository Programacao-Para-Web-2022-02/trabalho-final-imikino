from flask import render_template, flash, redirect, url_for, request
from imikino import app, database, bcrypt
from imikino.forms import FormLogin, FormCriarConta, FormEditarPerfil
from imikino.models import Usuario
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os
from PIL import Image #vamos usar para reduzir o tamanho da imagem

@app.route('/')
def home():
    if current_user.is_authenticated:
        foto_perfil = url_for('static', filename='foto_perfil/{}'.format(current_user.foto_perfil))
        return render_template('home.html', foto_perfil=foto_perfil)
    return render_template('home.html')


@app.route('/sobre')
def sobre():
    if current_user.is_authenticated:
        foto_perfil = url_for('static', filename='foto_perfil/{}'.format(current_user.foto_perfil))
        return render_template('sobre.html', foto_perfil=foto_perfil)
    return render_template('sobre.html')


@app.route('/usuarios')
@login_required #precisa estar logado para acessar essa página
def usuarios():
    if current_user.is_authenticated:
        foto_perfil = url_for('static', filename='foto_perfil/{}'.format(current_user.foto_perfil))
        return render_template('usuarios.html', foto_perfil=foto_perfil)
    return render_template('usuarios.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()

    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        # verificar se o usuario e a senha estão corretas
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            # fazer o login
            login_user(usuario, remember=form_login.lembrar_dados.data)
            # fez login com sucesso
            # exibir mensagem de sucesso -> flash
            flash(f'Login feito com sucesso para o e-mail {form_login.email.data}', 'alert-primary')  # .data serve para pegar o que a pessoa escreveu no campo de texto
              
            #verificar se existie o parâmetro next (caso ele tenha tentado acessar uma página que só é permitida estando logado então ele ganha o parâmetro next=página que ele tentou acessar e ao fazer login ele em vez de ir para a home ele vai para o next)
            par_next = request.args.get('next') #pegando o valor do parâmetro next e colocando em uma variável
            if par_next:
                return redirect(par_next)
            # redirecionar para a home page -> redirect
            else:
                return redirect(url_for('home'))
        else:
            flash(f'Falha no Login. E-mail ou Senha Incorretos', 'alert-danger')
    return render_template('login.html', form_login=form_login)


@app.route('/criar-conta', methods=['GET', 'POST'])
def criarConta():
    form_criarconta = FormCriarConta()

    if form_criarconta.validate_on_submit():
        # criptografar a senha
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        # criar o Usuario
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        # adicionar a sessão
        database.session.add(usuario)
        # commitar a sessão
        database.session.commit()
        # -----------------------
        # fez login com sucesso
        # exibir mensagem de sucesso -> flash
        flash(f'Bem-vindo(a) ao time, {form_criarconta.username.data}!! Conta criada com sucesso', 'alert-primary')  # .data serve para pegar o que a pessoa escreveu no campo de texto
        # redirecionar para a home page -> redirect
        return redirect(url_for('login'))
    return render_template('criarConta.html', form_criarconta=form_criarconta)


@app.route('/sair')
@login_required #precisa estar logado para acessar essa página
def sair():
    logout_user()
    flash(f'Logout feito com sucesso, até logo', 'alert-primary')
    return redirect(url_for('home'))


@app.route('/perfil')
@login_required #precisa estar logado para acessar essa página
def perfil():
    foto_perfil = url_for('static', filename='foto_perfil/{}'.format(current_user.foto_perfil))
    return render_template('perfil.html', foto_perfil=foto_perfil)


def salvar_imagem(imagem):
    #adicionar um código aleatório no nome da imagem para evitar que duas imagens tenham o mesmo nome
    codigo = secrets.token_hex(6)
    nome, extensao = os.path.splitext(imagem.filename)
    nome_arquivo = nome + codigo + extensao

    caminho_completo = os.path.join(app.root_path, 'static/foto_perfil', nome_arquivo) #caminho da pasta imikino

    #reduzir o tamanho da imagem
    tamanho = (400, 400)
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(tamanho)

    #salvar a imagem na pasta fotos_perfil
    imagem_reduzida.save(caminho_completo)
    return nome_arquivo

@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required #precisa estar logado para acessar essa página
def editar_perfil():
    form = FormEditarPerfil()

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        if form.foto_perfil.data:
            #mudar o campo foto_perfil do usuario para o novo nome da imagem
            nome_imagem = salvar_imagem(form.foto_perfil.data)
            current_user.foto_perfil = nome_imagem
        database.session.commit()
        flash(f'Perfil atualizado com Sucesso', 'alert-primary')
        return redirect(url_for('perfil'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    foto_perfil = url_for('static', filename='foto_perfil/{}'.format(current_user.foto_perfil))
    return render_template('editarperfil.html', foto_perfil=foto_perfil, form=form)
