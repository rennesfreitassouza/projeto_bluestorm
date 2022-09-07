"""Modules integrated with the Python interpreter"""
import json


def test_pharmacies_route_http_get_method_without_token(client):
    response = client.get('/pharmacies')
    data_dict = json.loads(response.data)
    assert {} == data_dict['data'], print(data_dict)
    assert 'token is missing' == data_dict['message'], print(data_dict)


def test_pharmacies_route_http_get_method_with_invalid_token(client, get_valid_token):
    data_dict = get_valid_token
    route_with_token = f'/pharmacies?token={data_dict["token"] + "a"}'
    response = client.get(route_with_token)
    data_dict = json.loads(response.data)
    assert {} == data_dict['data'], print(data_dict)
    assert 'token is invalid or expired' == data_dict['message'], print(data_dict)


def test_pharmacies_route_http_get_method_with_valid_token(client, get_valid_token):
    data_dict = get_valid_token
    route_with_token = f'/pharmacies?token={data_dict["token"]}'
    response = client.get(route_with_token)
    data_dict = json.loads(response.data)

    assert 'PHARM0001' in data_dict.keys(), print(data_dict)
    assert 'Cidade' in data_dict['PHARM0001'].keys(), print(data_dict)
    assert 'ID' in data_dict['PHARM0001'].keys(), print(data_dict)
    assert 'Nome' in data_dict['PHARM0001'].keys(), print(data_dict)
