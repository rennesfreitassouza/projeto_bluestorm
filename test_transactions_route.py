"""Modulo com diversos casos de teste para o endpoint '/transactions'"""
import json


def test_transactions_route_http_get_method_without_token(client):
    """Caso de teste que verifica o retorno da rota /transactions caso
    uma requisição HTTP GET sem token for feita para este endpoint."""
    response = client.get('/transactions')
    data_dict = json.loads(response.data)
    assert {} == data_dict['DATA'], print(data_dict)
    assert 'TOKEN IS MISSING' == data_dict['MESSAGE'], print(data_dict)


def test_transactions_route_http_get_method_with_invalid_token(client, get_valid_token):
    """Caso de teste que verifica o retorno da rota /transactions caso
    uma requisição HTTP GET com token inválido for feita para este endpoint."""
    data_dict = get_valid_token
    route_with_token = f'/transactions?token={data_dict["TOKEN"] + "a"}'
    response = client.get(route_with_token)
    data_dict = json.loads(response.data)
    assert {} == data_dict['DATA'], print(data_dict)
    assert 'TOKEN IS INVALID OR EXPIRED' == data_dict['MESSAGE'], print(data_dict)


def test_transactions_route_http_get_method_with_valid_token(client, get_valid_token):
    """Caso de teste que verifica os dados relativos a uma transação retornados pela
    rota /transactions caso uma requisição HTTP GET com um token válido for feita
    para este endpoint."""
    data_dict = get_valid_token
    route_with_token = f'/transactions?token={data_dict["TOKEN"]}'
    response = client.get(route_with_token)
    data_dict = json.loads(response.data)

    assert 'TRAN0031' in data_dict.keys(), print(data_dict)
    assert 'ID DA FARMACIA' in data_dict['TRAN0031'].keys(), print(data_dict)
    assert 'ID DA TRANSACAO' in data_dict['TRAN0031'].keys(), print(data_dict)
    assert 'ID DO PACIENTE' in data_dict['TRAN0031'].keys(), print(data_dict)
    assert 'CIDADE DA FARMACIA' in data_dict['TRAN0031'].keys(), print(data_dict)
    assert 'DATA DA TRANSACAO' in data_dict['TRAN0031'].keys(), print(data_dict)
    assert 'DATA DE NASCIMENTO DO PACIENTE' in data_dict['TRAN0031'].keys(), print(data_dict)
    assert 'NOME DA FARMACIA' in data_dict['TRAN0031'].keys(), print(data_dict)
    assert 'NOME DO PACIENTE' in data_dict['TRAN0031'].keys(), print(data_dict)
    assert 'QUANTIDADE DA TRANSACAO' in data_dict['TRAN0031'].keys(), print(data_dict)
    assert 'SOBRENOME DO PACIENTE' in data_dict['TRAN0031'].keys(), print(data_dict)


def test_transactions_route_http_get_method_with_valid_token_and_pa_first_name_and_ph_name_params(client, get_valid_token):
    """Caso de teste que verifica os dados relativos a uma transação retornados pela
    rota /transactions caso uma requisição HTTP GET com um token válido e com
    um parâmetro pa_first_name igual a JOanÁ e parâmetro ph_name igual a MAIS
    for feita para este endpoint."""
    data_dict = get_valid_token
    route_with_param = f'/transactions?token={data_dict["TOKEN"]}&pa_first_name=JOanÁ&ph_name=MAIS'
    response = client.get(route_with_param)
    data_dict = json.loads(response.data)

    assert 'TRAN0081' in data_dict.keys(), print(data_dict)
    assert 'PHARM0006' == data_dict['TRAN0081']['ID DA FARMACIA'], print(data_dict)
    assert 'TRAN0081' == data_dict['TRAN0081']['ID DA TRANSACAO'], print(data_dict)
    assert 'PATIENT0001' == data_dict['TRAN0081']['ID DO PACIENTE'], print(data_dict)
    assert 'SAO PAULO' == data_dict['TRAN0081']['CIDADE DA FARMACIA'], print(data_dict)
    assert ('2020-12-21 06:08:47.000000' ==
             data_dict['TRAN0081']['DATA DA TRANSACAO']), print(data_dict)
    assert ('1996-10-25 00:00:00.000000' ==
     data_dict['TRAN0081']['DATA DE NASCIMENTO DO PACIENTE']), print(data_dict)
    assert 'DROGA MAIS' == data_dict['TRAN0081']['NOME DA FARMACIA'], print(data_dict)
    assert 'JOANA' == data_dict['TRAN0081']['NOME DO PACIENTE'], print(data_dict)
    assert str(17.05) == data_dict['TRAN0081']['QUANTIDADE DA TRANSACAO'], print(data_dict)
    assert 'SILVA' == data_dict['TRAN0081']['SOBRENOME DO PACIENTE'], print(data_dict)


def test_transactions_route_http_get_method_with_valid_token_and_pa_first_name_and_ph_name_params_no_data(client, get_valid_token):
    """Caso de teste que verifica os dados relativos a uma transação retornados pela
    rota /transactions caso uma requisição HTTP GET com um token válido e com
    um parâmetro pa_first_name igual a NONAME e parâmetro ph_name igual a NONAME
    for feita para este endpoint."""
    data_dict = get_valid_token
    route_with_param = f'/transactions?token={data_dict["TOKEN"]}&pa_first_name=NONAME&ph_name=NONAME'
    response = client.get(route_with_param)
    data_dict = json.loads(response.data)

    assert 'ERROR' in data_dict.keys(), print(data_dict)
    assert 'NO DATA FOUND' == data_dict['ERROR'], print(data_dict)
