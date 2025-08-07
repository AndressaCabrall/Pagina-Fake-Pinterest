# Importações

from fakepinterest import database, app
from fakepinterest.models import Usuario, Fotos


# Criando o Banco de dados
with app.app_context():
    database.create_all()