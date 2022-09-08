"""Local functions"""
from bluestorm_api.sqlite_db import conectar_sqlite, select_patients_data, select_pharmacies_data, select_trasactions_information, select_user_by_username_pass


def test_conectar_sqlite_function_None_return(get_invalid_db_path):
    invalid_db_path = get_invalid_db_path
    retorno = conectar_sqlite(invalid_db_path)
    assert retorno is None, print('retorno', retorno)


def test_select_patients_data_database_path_error(get_invalid_db_path):
    invalid_db_path = get_invalid_db_path
    retorno = select_patients_data(db_path=invalid_db_path)
    assert 'Error' in retorno.keys(), print(retorno)
    assert 'Database error' == retorno['Error'], print(retorno)


def test_select_pharmacies_data_database_path_error(get_invalid_db_path):
    invalid_db_path = get_invalid_db_path
    retorno = select_pharmacies_data(db_path=invalid_db_path)
    assert 'Error' in retorno.keys(), print(retorno)
    assert 'Database error' == retorno['Error'], print(retorno)


def test_select_trasactions_information_database_path_error(get_invalid_db_path):
    invalid_db_path = get_invalid_db_path
    retorno = select_trasactions_information(db_path=invalid_db_path)
    assert 'Error' in retorno.keys(), print(retorno)
    assert 'Database error' == retorno['Error'], print(retorno)


def test_select_user_by_username_pass_database_path_error(get_invalid_db_path):
    invalid_db_path = get_invalid_db_path
    retorno = select_user_by_username_pass(db_path=invalid_db_path)
    assert 'Error' in retorno.keys(), print(retorno)
    assert 'Database error' == retorno['Error'], print(retorno)


def test_select_patients_data_exception(get_invalid_db_name):
    invalid_db_name = get_invalid_db_name
    retorno = select_patients_data(db_path=invalid_db_name)
    assert 'Error' in retorno.keys(), print(retorno)
    assert 'An exception occurred.' == retorno['Error'], print(retorno)


def test_select_pharmacies_data_exception(get_invalid_db_name):
    invalid_db_name = get_invalid_db_name
    retorno = select_pharmacies_data(db_path=invalid_db_name)
    assert 'Error' in retorno.keys(), print(retorno)
    assert 'An exception occurred.' == retorno['Error'], print(retorno)


def test_select_trasactions_information_exception(get_invalid_db_name):
    invalid_db_name = get_invalid_db_name
    retorno = select_trasactions_information(db_path=invalid_db_name)
    assert 'Error' in retorno.keys(), print(retorno)
    assert 'An exception occurred.' == retorno['Error'], print(retorno)


def test_select_user_by_username_pass_exception(get_invalid_db_name):
    invalid_db_name = get_invalid_db_name
    retorno = select_user_by_username_pass(db_path=invalid_db_name)
    assert 'Error' in retorno.keys(), print(retorno)
    assert 'An exception occurred.' == retorno['Error'], print(retorno)


def test_select_user_by_username_pass_user_exception():
    retorno = select_user_by_username_pass(username='0000', password='1111')
    assert 'ERROR' in retorno.keys(), print(retorno)
    assert 'USER WITH THESE CREDENTIALS DOES NOT EXIST' == retorno['ERROR'], print(retorno)


