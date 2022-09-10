"""Módulo utilizado antes ou no início da execução da API."""
from getpass import getpass
import click
from flask import Flask
from bluestorm_api.auth_functions import generate_a_secret_key
from bluestorm_api.sqlite_db import insert_into_users


def create_app(test_config=None):
    """Função cria um app Flask"""
    flask_app = Flask(__name__)
    flask_app.secret_key = generate_a_secret_key()

    from . import bluestorm_api
    flask_app.register_blueprint(bluestorm_api.bp)

    return flask_app


@click.command(name='endpoints')
def endpoints():
    """Sobre os endpoints. Função criada para facilitar a utilização do serviço local."""
    print('''### Como fazer requisições para a API ###
Para facilitar a interação com os endpoints do projeto, recomenda-se que o software Postman seja utilizado. Uma collection com o nome Bluestorm.postman_collection.json pronta para ser utilizada pelo Postman pode ser encontrada no diretório raíz. A seguir, há uma breve explicação de como devem ser feitas as requisições para que dados válidos sejam retornados pela API REST privada.

- http://127.0.0.1:5000/auth - uma requisição POST com Basic Auth precisa ser feita para que um token seja retornado por esse endpoint. O usuário admin e a senha admin já foram inseridos na tabela USERS do banco de dados bluestorm_api/backend_test.db para que a autenticação seja considerada válida e um token seja retornado para o usuário. Após realizar essa requisição, com esse tipo de autenticação e com esse usuário e senha, armazenar o token retornado para ser utilizado nas próximas requisições.

- http://127.0.0.1:5000/patients?token= após o sinal de igual, inserir o token obtido da rota http://127.0.0.1:5000/auth. Assim, ao realizar uma requisição HTTP GET para esse endereço, dados válidos de pacientes poderão ser obtidos.
  - Opcional: adicionar o parâmetro first_name para realizar a busca no endpoint /patients por meio do nome do paciente. O endereço ficará http://127.0.0.1:5000/patients?token=&first_name=. O valor para o nome do paciente procurado deve ser adicionado após &first_name=.


- http://127.0.0.1:5000/pharmacies?token= após o sinal de igual, inserir o token obtido da rota http://127.0.0.1:5000/auth. Assim, ao realizar uma requisição HTTP GET para esse endereço, dados válidos de farmácias poderão ser obtidos.
  - Opcional: adicionar o parâmetro name para realizar a busca no endpoint /pharmacies por meio do nome da farmácia. O endereço ficará http://127.0.0.1:5000/pharmacies?token=&name=. O valor para o nome da farmácia procurada deve ser adicionado após &name=.


- 127.0.0.1:5000/transactions?token= após o sinal de igual, inserir o token obtido da rota http://127.0.0.1:5000/auth. Assim, ao realizar uma requisição HTTP GET para esse endereço, dados válidos de transações poderão ser obtidos.
  - Opcional: adicionar os parâmetros pa_first_name e ph_name para realizar a busca no endpoint /transactions, respectivamente por meio do nome do paciente e do nome da farmácia. O endereço ficará http://127.0.0.1:5000/transactions?token=&pa_first_name=&ph_name=. O valor para o nome do paciente procurado deve ser adicionado após &pa_first_name= e o valor para o nome da farmácia procurada deve ser adicionado após &ph_name=.
  
- Mais sobre a utilização da API em: https://github.com/rennesfreitassouza/projeto_bluestorm/edit/main/README.md''')


@click.command(name='about')
def about():
    """Sobre o autor da API. Função criada para facilitar
    o futuro desevolvimento da API por terceiros."""
    print('''### About ###
Projeto desenvolvido por: Rennes Freitas Souza
Contato: rennesfrso@gmail.com
REST API desenvolvida para vaga back-end da empresa Bluestorm.
Mais informações em: https://github.com/rennesfreitassouza/projeto_bluestorm/edit/main/README.md''')


@click.command(name='adduser')
def adduser():
    """Função faz a coleta de informações de usuário (nome e senha)
    para inserir no banco de dados. Esses dados podem ser usados para
    gerar um token com segurança."""
    print('New user:', end=' ')
    user = input()
    passworld = getpass('Password:')
    uuid = generate_a_secret_key()
    retorno = insert_into_users(uuid, user, passworld)
    print (retorno)


app = create_app()
app.cli.add_command(endpoints)
app.cli.add_command(about)
app.cli.add_command(adduser)
