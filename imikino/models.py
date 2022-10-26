#Aqui é onde irão ficar minhas tabelas do banco de dados
from imikino import database


#Tabela usuário
class Usuario(database.Model):
    #colunas do banco de dados
    id = database.Column(database.Integer, primary_key=True) 
    username = database.Column(database.String, nullable=False, unique=True) #nullable=False -> É obrigatório | unique=True -> Tem que ser único
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')