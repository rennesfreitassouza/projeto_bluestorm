"""Modulo com diversos casos de teste para o endpoint '/patients'"""
import json


def test_patients_route_http_get_method_without_token(client):
    """Caso de teste que verifica o retorno da rota /patients caso
    uma requisição HTTP GET sem token for feita para este endpoint."""
    response = client.get('/patients')
    data_dict = json.loads(response.data)
    assert {} == data_dict['DATA'], print(data_dict)
    assert 'TOKEN IS MISSING' == data_dict['MESSAGE'], print(data_dict)


def test_patients_route_http_get_method_with_invalid_token(client, get_valid_token):
    """Caso de teste que verifica o retorno da rota /patients caso
    uma requisição HTTP GET com token inválido for feita para este endpoint."""
    data_dict = get_valid_token
    route_with_token = f'/patients?token={data_dict["TOKEN"] + "a"}'
    response = client.get(route_with_token)
    data_dict = json.loads(response.data)
    assert {} == data_dict['DATA'], print(data_dict)
    assert 'TOKEN IS INVALID OR EXPIRED' == data_dict['MESSAGE'], print(data_dict)


def test_patients_route_http_get_method_with_valid_token(client, get_valid_token):
    """Caso de teste que verifica os dados de um paciente retornados pela
    rota /patients caso uma requisição HTTP GET com um token válido for feita
    para este endpoint."""
    data_dict = get_valid_token
    route_with_token = f'/patients?token={data_dict["TOKEN"]}'
    response = client.get(route_with_token)
    data_dict = json.loads(response.data)

    assert 'PATIENT0001' in data_dict.keys(), print(data_dict)
    assert 'DATA DE NASCIMENTO' in data_dict['PATIENT0001'].keys(), print(data_dict)
    assert 'ID' in data_dict['PATIENT0001'].keys(), print(data_dict)
    assert 'NOME' in data_dict['PATIENT0001'].keys(), print(data_dict)
    assert 'SOBRENOME' in data_dict['PATIENT0001'].keys(), print(data_dict)


def test_patients_route_get_method_with_valid_token_and_first_name_param(client, get_valid_token):
    """Caso de teste que verifica os dados de um paciente retornados pela
    rota /patients caso uma requisição HTTP GET com um token válido e com
    um parâmetro first_name igual a jôánA for feita para este endpoint."""
    data_dict = get_valid_token
    route_with_param = f'/patients?token={data_dict["TOKEN"]}&first_name=jôánA'
    response = client.get(route_with_param)
    data_dict = json.loads(response.data)

    assert 'PATIENT0001' in data_dict.keys(), print(data_dict)
    assert '1996-10-25 00:00:00.000000' == data_dict['PATIENT0001']['DATA DE NASCIMENTO'], print(data_dict)
    assert 'PATIENT0001' == data_dict['PATIENT0001']['ID'], print(data_dict)
    assert 'JOANA' == data_dict['PATIENT0001']['NOME'], print(data_dict)
    assert 'SILVA' == data_dict['PATIENT0001']['SOBRENOME'], print(data_dict)


def test_patients_route_get_method_with_valid_token_and_first_name_param_no_data(client, get_valid_token):
    """Caso de teste que verifica os dados retornados pela
    rota /patients caso uma requisição HTTP GET com um token válido e com
    um parâmetro first_name igual a NONAME for feita para este endpoint."""
    data_dict = get_valid_token
    route_with_param = f'/patients?token={data_dict["TOKEN"]}&first_name=NONAME'
    response = client.get(route_with_param)
    data_dict = json.loads(response.data)

    assert 'ERROR' in data_dict.keys(), print(data_dict)
    assert 'NO DATA FOUND' == data_dict['ERROR'], print(data_dict)
    