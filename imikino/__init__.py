import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy #-> para criar o banco de dados
from flask_bcrypt import Bcrypt #-> para criptografar a senha do usuário

app = Flask(__name__)

app.config['SECRET_KEY'] = '4df2fe84ce1de11eff62613706100034' #token gerado aleatoriamente pelo secrets para proteger o formulário
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///imikino.db' #criar o arquivo do banco de dados (o sqlite serve para ele criar o banco de dados no mesmo local do arquivo main)

database = SQLAlchemy(app)
bcrypt = Bcrypt(app) #auando fazemos isso só o nosso site é capaz de entender a criptografia da senha, ninugém de fora consegue pegar (foi aplicado no routes)


from imikino import routes