from imikino import app

if __name__ == '__main__':
    app.run(debug=True)


'''
Passo a passo de downloads e comandos:

pip install Flask

pip install flask-wtf (Criação de formulários com FlaskForm)
#Temos que baixar o Email do wtforms (por alugm motivo ele não vem junto)
pip install email_validator

#Agora temos que baixar o sql alchemy que vai ser o nosso banco de dados
pip install sqlalchemy
pip install flask-sqlalchemy

#como criar e consultar o banco de dados
from main import database
from models import Usuario 
database.create_all()

comandos para mexer no banco de dados:
#criar usuário
usuario = Usuario(username='Leo', email='leo@gmail.com', senha='123123')
usuario2 = Usuario(username='Lucas', email='lucas@gmail.com', senha='123123')

#registrar o usuário dentro do banco de dados (add and commit)
database.session.add(usuario)
database.session.add(usuario2)
database.session.commit()

#visualizar os usuários (query serve para consultar o banco de dados | pegar uma informação de lá)
Usuario.query.all() -> vai me dar todas as informações da tabela Usuario
Usuario.query.first() -> vai me dar o primeiro cara do meu banco de dados

usuario_teste = Usuario.query.first() -> armazenando o primeiro cara em uma variável
usuario_teste.email
usuario_teste.username
usuario_teste.id
usuario_teste.foto_perfil

usuario_lucas = Usuario.query.filter_by(email='lucas@gmail.com') #filtrar por email
usuario_lucas = Usuario.query.filter_by(email='lucas@gmail.com').first() #mas tem que pegar o primeiro pra pegar o primeiro item da lista
usuario_lucas
usuario_lucas.email...

#deletar o bd
database.drop_all()
#recriar
database.create_all()

#Agora o BD vai estar vazio



-----------------------------
Para conferir se deu certo

from imikino import database
from imikino.models import Usuario

Usuario.query.all() -> ver os usuários do site
usuario = Usuario.query.first()
usuario.username
usuario.email
usuario.senha

usuario2 = Usuario.query.filter_by(username='leozin2').first()
usuario2.senha -> b'$2b$12$Sjt1VqGrBW34pRJfzFaC4uSrCFbKtGL6Mc7PVIucHT.k0Xw1Nr/jy' #a senha está criptografada
'''

'''
#baixar o que iremos usar para criptografar a senha
pip install flask-bcrypt

-----------------
#baixar o que iremos usar para fazer o login no site
pip install flask-login
'''

