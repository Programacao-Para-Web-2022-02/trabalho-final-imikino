# Aqui é onde irão ficar minhas tabelas do banco de dados
from imikino import database, login_manager
from flask_login import \
    UserMixin  # é um parametro que vai passar para a nossa classe para ele entender quem é o usuário ativo


@login_manager.user_loader
def load_usuario(id_usuario):  # vai encontrar um usuario pelo id do usuario
    return Usuario.query.get(int(id_usuario))


# Tabela usuário
class Usuario(database.Model, UserMixin):
    # colunas do banco de dados
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False,
                               unique=True)  # nullable=False -> É obrigatório | unique=True -> Tem que ser único
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
