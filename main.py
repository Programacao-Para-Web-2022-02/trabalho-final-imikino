from flask import Flask, render_template, url_for
from forms import FormLogin, FormCriarConta

app = Flask(__name__)

app.config['SECRET_KEY'] = '4df2fe84ce1de11eff62613706100034' #token gerado aleatoriamente pelo secrets para proteger o formulário

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    return render_template('login.html', form_login=form_login)

@app.route('/criar-conta', methods=['GET', 'POST'])
def criarConta():
    form_criarconta = FormCriarConta()
    return render_template('criarConta.html', form_criarconta=form_criarconta)

if __name__ == '__main__':
    app.run(debug=True)


'''
Passo a passo de downloads e comandos:

pip install Flask

pip install flask-wtf (Criação de formulários com FlaskForm)
#Temos que baixar o Email do wtforms (por alugm motivo ele não vem junto)
pip install email_validator
'''