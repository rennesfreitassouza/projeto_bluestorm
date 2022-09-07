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


def test_transactions_route_http_get_method_with_valid_token_and_pa_first_name_and_ph_name_params(client, get_valid_token):
    data_dict = get_valid_token
    route_with_param = f'/transactions?token={data_dict["token"]}&pa_first_name=JOanÁ&ph_name=MAIS'
    response = client.get(route_with_param)
    data_dict = json.loads(response.data)

    assert 'TRAN0081' in data_dict.keys(), print(data_dict)
    assert 'PHARM0006' == data_dict['TRAN0081']['ID da farmácia'], print(data_dict)
    assert 'TRAN0081' == data_dict['TRAN0081']['ID da transação'], print(data_dict)
    assert 'PATIENT0001' == data_dict['TRAN0081']['ID do paciente'], print(data_dict)
    assert 'SAO PAULO' == data_dict['TRAN0081']['cidade da farmácia'], print(data_dict)
    assert '2020-12-21 06:08:47.000000' == data_dict['TRAN0081']['data da transação'], print(data_dict)
    assert '1996-10-25 00:00:00.000000' == data_dict['TRAN0081']['data de nascimento do paciente'], print(data_dict)
    assert 'DROGA MAIS' == data_dict['TRAN0081']['nome da farmácia'], print(data_dict)
    assert 'JOANA' == data_dict['TRAN0081']['nome do paciente'], print(data_dict)
    assert 17.05 == data_dict['TRAN0081']['quantidade da transação'], print(data_dict)
    assert 'SILVA' == data_dict['TRAN0081']['sobrenome do paciente'], print(data_dict)


def test_transactions_route_http_get_method_with_valid_token_and_pa_first_name_and_ph_name_params_no_data(client, get_valid_token):
    data_dict = get_valid_token
    route_with_param = f'/transactions?token={data_dict["token"]}&pa_first_name=NONAME&ph_name=NONAME'
    response = client.get(route_with_param)
    data_dict = json.loads(response.data)

    assert 'Error' in data_dict.keys(), print(data_dict)
    assert 'No data found.' == data_dict['Error'], print(data_dict)

