"""Modules integrated with the Python interpreter"""
import json


def test_patients_route_http_get_method_without_token(client):
    response = client.get('/patients')
    data_dict = json.loads(response.data)
    assert {} == data_dict['DATA'], print(data_dict)
    assert 'TOKEN IS MISSING' == data_dict['MESSAGE'], print(data_dict)


def test_patients_route_http_get_method_with_invalid_token(client, get_valid_token):
    data_dict = get_valid_token
    route_with_token = f'/patients?token={data_dict["TOKEN"] + "a"}'
    response = client.get(route_with_token)
    data_dict = json.loads(response.data)
    assert {} == data_dict['DATA'], print(data_dict)
    assert 'TOKEN IS INVALID OR EXPIRED' == data_dict['MESSAGE'], print(data_dict)


def test_patients_route_http_get_method_with_valid_token(client, get_valid_token):
    data_dict = get_valid_token
    route_with_token = f'/patients?token={data_dict["TOKEN"]}'
    response = client.get(route_with_token)
    data_dict = json.loads(response.data)

    assert 'PATIENT0001' in data_dict.keys(), print(data_dict)
    assert 'Data de nascimento' in data_dict['PATIENT0001'].keys(), print(data_dict)
    assert 'ID' in data_dict['PATIENT0001'].keys(), print(data_dict)
    assert 'Nome' in data_dict['PATIENT0001'].keys(), print(data_dict)
    assert 'Sobrenome' in data_dict['PATIENT0001'].keys(), print(data_dict)


def test_patients_route_http_get_method_with_valid_token_and_first_name_param(client, get_valid_token):
    data_dict = get_valid_token
    route_with_param = f'/patients?token={data_dict["TOKEN"]}&first_name=jôánA'
    response = client.get(route_with_param)
    data_dict = json.loads(response.data)

    assert 'PATIENT0001' in data_dict.keys(), print(data_dict)
    assert '1996-10-25 00:00:00.000000' == data_dict['PATIENT0001']['Data de nascimento'], print(data_dict)
    assert 'PATIENT0001' == data_dict['PATIENT0001']['ID'], print(data_dict)
    assert 'JOANA' == data_dict['PATIENT0001']['Nome'], print(data_dict)
    assert 'SILVA' == data_dict['PATIENT0001']['Sobrenome'], print(data_dict)


def test_patients_route_http_get_method_with_valid_token_and_first_name_param_no_data(client, get_valid_token):
    data_dict = get_valid_token
    route_with_param = f'/patients?token={data_dict["TOKEN"]}&first_name=NONAME'
    response = client.get(route_with_param)
    data_dict = json.loads(response.data)

    assert 'Error' in data_dict.keys(), print(data_dict)
    assert 'No data found.' == data_dict['Error'], print(data_dict)

