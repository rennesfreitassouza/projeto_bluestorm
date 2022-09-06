"""Modules integrated with the Python interpreter"""
from base64 import b64encode
import json

"""Local functions"""
from bluestorm_api.sqlite_db import DATABASE_PATH


def test_auth_route_http_get_method(client):
    response = client.get('/auth')
    assert b'Request method not allowed' == response.data, print(response.data)


def test_auth_route_http_post_method_with_no_credentials(client):
    credentials = b64encode(b'admin:').decode('utf-8')
    response = client.post('/auth', headers={'Authorization': f'Basic {credentials}'})
    data_dict = json.loads(response.data)
    assert 'Basic auth="Login required"' == data_dict['WWW-Authenticate'], print(data_dict)
    assert 'Could not verify' == data_dict['message'], print(data_dict)


def test_auth_route_http_post_method_with_invalid_credentials(client):
    credentials = b64encode(b'admin:adminNO').decode('utf-8')
    response = client.post('/auth', headers={'Authorization': f'Basic {credentials}'})
    data_dict = json.loads(response.data)
    assert 'User with these credentials does not exist.' == data_dict['message'], print(data_dict)
    assert {} == data_dict['data'], print(data_dict)


def test_auth_route_http_post_method_with_invalid_database(client):
    """Caso de teste que cobriria o caso do banco de dados não poder ser criado e não existir. Para fazer este teste, trocar o nome da pasta do caminho para o banco de dados que está contido na variável global DATABASE_PATH no módulo bluestorm_api.sqlite_db. Apenas o teste manual é possivel."""
    # credentials = b64encode(b'admin:admin').decode('utf-8')
    # response = client.post('/auth', headers={'Authorization': f'Basic {credentials}'})
    # data_dict = json.loads(response.data)
    """Aqui fica a representação em comentário em um assert do que deveria estar nos dados retornados em caso de o fluxo de código ter encontrado uma excessão devido ao problema no banco de dados já mencionado."""
    # assert 'Database error' == data_dict['message'], print(data_dict)
    pass


def test_auth_route_http_post_method_with_valid_credentials(get_valid_token):
    data_dict = get_valid_token
    assert 'exp' in data_dict.keys(), print(data_dict)
    assert 'Validated successfully' == data_dict['message'], print(data_dict)
    assert 'token' in data_dict.keys(), print(data_dict)
