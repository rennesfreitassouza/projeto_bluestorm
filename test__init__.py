"""Módulo com os casos de teste para o módulo bluestorm_api.__init__"""
from bluestorm_api import endpoints, about, adduser, removeuser
from bluestorm_api.sqlite_db import select_user_by_username_pass


def test_endpoints_function(cli_runner):
    """Caso de teste que verifica se o output retornado
    pela simulação do comando "flask endpoints" que seria executado
    via linha de comando corresponde ao esperado."""
    runner = cli_runner

    result = runner.invoke(endpoints)
    assert '''### Como fazer requisições para a API ###
Para facilitar a interação com os endpoints do projeto, recomenda-se que o software Postman seja utilizado. Uma collection com o nome Bluestorm.postman_collection.json pronta para ser utilizada pelo Postman pode ser encontrada no diretório raíz. A seguir, há uma breve explicação de como devem ser feitas as requisições para que dados válidos sejam retornados pela API REST privada.

- http://127.0.0.1:5000/auth - uma requisição POST com Basic Auth precisa ser feita para que um token seja retornado por esse endpoint. O usuário admin e a senha admin já foram inseridos na tabela USERS do banco de dados bluestorm_api/backend_test.db para que a autenticação seja considerada válida e um token seja retornado para o usuário. Após realizar essa requisição, com esse tipo de autenticação e com esse usuário e senha, armazenar o token retornado para ser utilizado nas próximas requisições.

- http://127.0.0.1:5000/patients?token= após o sinal de igual, inserir o token obtido da rota http://127.0.0.1:5000/auth. Assim, ao realizar uma requisição HTTP GET para esse endereço, dados válidos de pacientes poderão ser obtidos.
  - Opcional: adicionar o parâmetro first_name para realizar a busca no endpoint /patients por meio do nome do paciente. O endereço ficará http://127.0.0.1:5000/patients?token=&first_name=. O valor para o nome do paciente procurado deve ser adicionado após &first_name=.


- http://127.0.0.1:5000/pharmacies?token= após o sinal de igual, inserir o token obtido da rota http://127.0.0.1:5000/auth. Assim, ao realizar uma requisição HTTP GET para esse endereço, dados válidos de farmácias poderão ser obtidos.
  - Opcional: adicionar o parâmetro name para realizar a busca no endpoint /pharmacies por meio do nome da farmácia. O endereço ficará http://127.0.0.1:5000/pharmacies?token=&name=. O valor para o nome da farmácia procurada deve ser adicionado após &name=.


- 127.0.0.1:5000/transactions?token= após o sinal de igual, inserir o token obtido da rota http://127.0.0.1:5000/auth. Assim, ao realizar uma requisição HTTP GET para esse endereço, dados válidos de transações poderão ser obtidos.
  - Opcional: adicionar os parâmetros pa_first_name e ph_name para realizar a busca no endpoint /transactions, respectivamente por meio do nome do paciente e do nome da farmácia. O endereço ficará http://127.0.0.1:5000/transactions?token=&pa_first_name=&ph_name=. O valor para o nome do paciente procurado deve ser adicionado após &pa_first_name= e o valor para o nome da farmácia procurada deve ser adicionado após &ph_name=.
  
- Mais sobre a utilização da API em: https://github.com/rennesfreitassouza/projeto_bluestorm/edit/main/README.md''' in result.output, print(result.output)


def test_about_function(cli_runner):
    """Caso de teste que verifica se o output retornado
    pela simulação do comando "flask about" que seria executado
    via linha de comando corresponde ao esperado."""
    runner = cli_runner

    result = runner.invoke(about)
    assert '''### About ###
Projeto desenvolvido por: Rennes Freitas Souza
Contato: rennesfrso@gmail.com
REST API desenvolvida para vaga back-end da empresa Bluestorm.
Mais informações em: https://github.com/rennesfreitassouza/projeto_bluestorm/edit/main/README.md''' in result.output, print(result.output)



def test_adduser_function(cli_runner):
    """Caso de teste que verifica se o output retornado
    pela simulação dos comandos
    "flask adduser --user test_user --password test_password"
    e
    "flask removeuser --user test_user --password test_password"
    que seria executado via linha de comando corresponde ao esperado."""
    runner = cli_runner

    user = 'test_user'
    password = 'test_password'
    result = runner.invoke(adduser, ['--user', f'{user}', '--password', f'{password}'])
    assert str({'MESSAGE': 'USER ADDED'}) in result.output, print(result.output)
    data_dict = select_user_by_username_pass(username=user, password=password)
    assert user == data_dict['username'], print(data_dict)
    assert password == data_dict['password'], print(data_dict)

    result = runner.invoke(removeuser, ['--user', f'{user}', '--password', f'{password}'])
    assert str({'MESSAGE': 'USER DELETED'}) in result.output, print(result.output)
