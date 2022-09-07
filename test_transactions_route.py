"""Modules integrated with the Python interpreter"""
import json


def test_transactions_route_http_get_method_without_token(client):
    response = client.get('/transactions')
    data_dict = json.loads(response.data)
    assert {} == data_dict['data'], print(data_dict)
    assert 'token is missing' == data_dict['message'], print(data_dict)


def test_transactions_route_http_get_method_with_invalid_token(client, get_valid_token):
    data_dict = get_valid_token
    route_with_token = f'/transactions?token={data_dict["token"] + "a"}'
    response = client.get(route_with_token)
    data_dict = json.loads(response.data)
    assert {} == data_dict['data'], print(data_dict)
    assert 'token is invalid or expired' == data_dict['message'], print(data_dict)


def test_transactions_route_http_get_method_with_valid_token(client, get_valid_token):
    data_dict = get_valid_token
    route_with_token = f'/transactions?token={data_dict["token"]}'
    response = client.get(route_with_token)
    data_dict = json.loads(response.data)

    assert 'TRAN0031' in data_dict.keys(), print(data_dict)
    assert 'ID da farmácia' in data_dict['TRAN0031'].keys(), print(data_dict)
    assert 'ID da transação' in data_dict['TRAN0031'].keys(), print(data_dict)
    assert 'ID do paciente' in data_dict['TRAN0031'].keys(), print(data_dict)
    assert 'cidade da farmácia' in data_dict['TRAN0031'].keys(), print(data_dict)
    assert 'data da transação' in data_dict['TRAN0031'].keys(), print(data_dict)
    assert 'data de nascimento do paciente' in data_dict['TRAN0031'].keys(), print(data_dict)
    assert 'nome da farmácia' in data_dict['TRAN0031'].keys(), print(data_dict)
    assert 'nome do paciente' in data_dict['TRAN0031'].keys(), print(data_dict)
    assert 'quantidade da transação' in data_dict['TRAN0031'].keys(), print(data_dict)
    assert 'sobrenome do paciente' in data_dict['TRAN0031'].keys(), print(data_dict)
