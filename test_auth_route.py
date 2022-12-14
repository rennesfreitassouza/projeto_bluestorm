"""Modulo com diversos casos de teste para o endpoint '/auth'"""
from base64 import b64encode
import json


def test_auth_route_http_get_method(client):
    """Caso de teste que verifica o retorno da rota /auth
    caso uma requisição HTTP GET for feita para ela."""
    response = client.get('/auth')
    data_dict = json.loads(response.data)
    assert {'ERROR': 'REQUEST METHOD NOT ALLOWED'} == data_dict, print(data_dict)


def test_auth_route_http_post_method_with_no_credentials(client):
    """Caso de teste que verifica o retorno da rota /auth caso
    uma requisição HTTP POST com método de autenticação Basic Auth
    com usuário admin mas sem senha for feita para ela."""
    credentials = b64encode(b'admin:').decode('utf-8')
    response = client.post('/auth', headers={'Authorization': f'Basic {credentials}'})
    data_dict = json.loads(response.data)
    assert 'BASIC AUTH="LOGIN REQUIRED"' == data_dict['WWW-AUTHENTICATE'], print(data_dict)
    assert 'COULD NOT VERIFY' == data_dict['MESSAGE'], print(data_dict)


def test_auth_route_http_post_method_with_invalid_credentials(client):
    """Caso de teste que verifica o retorno da rota /auth caso
    uma requisição HTTP POST com método de autenticação Basic Auth
    com usuário admin mas com senha senha diferente da
    presente no banco de dados for feita para este endpoint."""
    credentials = b64encode(b'admin:adminNO').decode('utf-8')
    response = client.post('/auth', headers={'Authorization': f'Basic {credentials}'})
    data_dict = json.loads(response.data)
    assert 'USER WITH THESE CREDENTIALS DOES NOT EXIST' == data_dict['MESSAGE'], print(data_dict)
    assert {} == data_dict['DATA'], print(data_dict)


# def test_auth_route_http_post_method_with_invalid_database(client):
#     Caso de teste que cobriria o caso do banco de dados não poder
#      ser criado e não existir. Para fazer este teste, trocar o nome da
#      pasta do caminho para o banco de dados que está contido na variável
#      global DATABASE_PATH no módulo bluestorm_api.sqlite_db. Apenas com 
#      o teste manual isso é possível.
#     credentials = b64encode(b'admin:admin').decode('utf-8')
#     response = client.post('/auth', headers={'Authorization': f'Basic {credentials}'})
#     data_dict = json.loads(response.data)
#     Aqui fica a representação em comentário em um assert do que deveria
#     estar nos dados retornados em caso de o fluxo de código ter encontrado
#     uma excessão devido ao problema no banco de dados já mencionado."""
#     assert 'DATABASE ERROR' == data_dict['MESSAGE'], print(data_dict)


def test_auth_route_http_post_method_with_valid_credentials(get_valid_token):
    """Caso de teste que verifica o retorno da rota /auth caso
    uma requisição HTTP POST com método de autenticação Basic Auth
    com usuário e senha correta for feita para este endpoint."""
    data_dict = get_valid_token
    assert 'EXP' in data_dict.keys(), print(data_dict)
    assert 'VALIDATED SUCCESSFULLY' == data_dict['MESSAGE'], print(data_dict)
    assert 'TOKEN' in data_dict.keys(), print(data_dict)
