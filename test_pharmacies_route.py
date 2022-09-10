"""Modulo com diversos casos de teste para o endpoint '/pharmacies'"""
import json


def test_pharmacies_route_http_get_method_without_token(client):
    """Caso de teste que verifica o retorno da rota /pharmacies caso
    uma requisição HTTP GET sem token for feita para este endpoint."""
    response = client.get('/pharmacies')
    data_dict = json.loads(response.data)
    assert {} == data_dict['DATA'], print(data_dict)
    assert 'TOKEN IS MISSING' == data_dict['MESSAGE'], print(data_dict)


def test_pharmacies_route_http_get_method_with_invalid_token(client, get_valid_token):
    """Caso de teste que verifica o retorno da rota /pharmacies caso
    uma requisição HTTP GET com token inválido for feita para este endpoint."""
    data_dict = get_valid_token
    route_with_token = f'/pharmacies?token={data_dict["TOKEN"] + "a"}'
    response = client.get(route_with_token)
    data_dict = json.loads(response.data)
    assert {} == data_dict['DATA'], print(data_dict)
    assert 'TOKEN IS INVALID OR EXPIRED' == data_dict['MESSAGE'], print(data_dict)


def test_pharmacies_route_http_get_method_with_valid_token(client, get_valid_token):
    """Caso de teste que verifica os dados de uma farmácia retornados pela
    rota /pharmacies caso uma requisição HTTP GET com um token válido for feita
    para este endpoint."""
    data_dict = get_valid_token
    route_with_token = f'/pharmacies?token={data_dict["TOKEN"]}'
    response = client.get(route_with_token)
    data_dict = json.loads(response.data)

    assert 'PHARM0001' in data_dict.keys(), print(data_dict)
    assert 'CIDADE' in data_dict['PHARM0001'].keys(), print(data_dict)
    assert 'ID' in data_dict['PHARM0001'].keys(), print(data_dict)
    assert 'NOME' in data_dict['PHARM0001'].keys(), print(data_dict)


def test_pharmacies_route_http_get_method_with_valid_token_and_name_param(client, get_valid_token):
    """Caso de teste que verifica os dados de uma farmácia retornados pela
    rota /pharmacies caso uma requisição HTTP GET com um token válido e com
    um parâmetro name igual a DRôGa MáiS for feita para este endpoint."""
    data_dict = get_valid_token
    route_with_param = f'/pharmacies?token={data_dict["TOKEN"]}&name=DRôGa MáiS'
    response = client.get(route_with_param)
    data_dict = json.loads(response.data)

    assert 'PHARM0001' in data_dict.keys(), print(data_dict)
    assert 'RIBEIRAO PRETO' == data_dict['PHARM0001']['CIDADE'], print(data_dict)
    assert 'PHARM0001' == data_dict['PHARM0001']['ID'], print(data_dict)
    assert 'DROGA MAIS' == data_dict['PHARM0001']['NOME'], print(data_dict)


def test_pharmacies_route_with_valid_token_and_name_param_no_data(client, get_valid_token):
    """Caso de teste que verifica os dados retornados pela
    rota /pharmacies caso uma requisição HTTP GET com um token válido e com
    um parâmetro name igual a NONAME for feita para este endpoint."""
    data_dict = get_valid_token
    route_with_param = f'/pharmacies?token={data_dict["TOKEN"]}&name=NONAME'
    response = client.get(route_with_param)
    data_dict = json.loads(response.data)

    assert 'ERROR' in data_dict.keys(), print(data_dict)
    assert 'NO DATA FOUND' == data_dict['ERROR'], print(data_dict)
