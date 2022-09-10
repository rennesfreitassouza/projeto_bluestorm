"""Modulo com diversos casos de teste para o módulo bluestorm_api.sqlite_db"""
from bluestorm_api.sqlite_db import conectar_sqlite, select_patients_data
from bluestorm_api.sqlite_db import select_pharmacies_data
from bluestorm_api.sqlite_db import select_trasactions_information, select_user_by_username_pass
from bluestorm_api.sqlite_db import insert_into_users, remove_from_users


def test_conectar_sqlite_function_none_return(get_invalid_db_path):
    """Caso de teste que verifica o retorno da função conectar_sqlite() caso
    um caminho inválido de um banco de dados for passado para a função."""
    invalid_db_path = get_invalid_db_path
    retorno = conectar_sqlite(invalid_db_path)
    assert retorno is None, print('retorno', retorno)


def test_select_patients_data_database_path_error(get_invalid_db_path):
    """Caso de teste que verifica o retorno da função select_patients_data() caso
    um caminho inválido de um banco de dados for passado para a função."""
    invalid_db_path = get_invalid_db_path
    retorno = select_patients_data(db_path=invalid_db_path)
    assert 'ERROR' in retorno, print(retorno)
    assert 'DATABASE ERROR' == retorno['ERROR'], print(retorno)


def test_select_pharmacies_data_database_path_error(get_invalid_db_path):
    """Caso de teste que verifica o retorno da função select_pharmacies_data() caso
    um caminho inválido de um banco de dados for passado para a função."""
    invalid_db_path = get_invalid_db_path
    retorno = select_pharmacies_data(db_path=invalid_db_path)
    assert 'ERROR' in retorno, print(retorno)
    assert 'DATABASE ERROR' == retorno['ERROR'], print(retorno)


def test_select_trasactions_information_database_path_error(get_invalid_db_path):
    """Caso de teste que verifica o retorno da função select_trasactions_information() 
    caso um caminho inválido de um banco de dados for passado para a função."""
    invalid_db_path = get_invalid_db_path
    retorno = select_trasactions_information(db_path=invalid_db_path)
    assert 'ERROR' in retorno, print(retorno)
    assert 'DATABASE ERROR' == retorno['ERROR'], print(retorno)


def test_select_user_by_username_pass_database_path_error(get_invalid_db_path):
    """Caso de teste que verifica o retorno da função select_user_by_username_pass()
    caso um caminho inválido de um banco de dados for passado para a função."""
    invalid_db_path = get_invalid_db_path
    retorno = select_user_by_username_pass(db_path=invalid_db_path)
    assert 'ERROR' in retorno, print(retorno)
    assert 'DATABASE ERROR' == retorno['ERROR'], print(retorno)


def test_insert_into_users_database_path_error(get_invalid_db_path):
    """Caso de teste que verifica o retorno da função insert_into_users()
    caso um caminho inválido de um banco de dados for passado para a função."""
    invalid_db_path = get_invalid_db_path
    retorno = insert_into_users(db_path=invalid_db_path)
    assert 'ERROR' in retorno, print(retorno)
    assert 'DATABASE ERROR' == retorno['ERROR'], print(retorno)


def test_remove_from_users_database_path_error(get_invalid_db_path):
    """Caso de teste que verifica o retorno da função remove_from_users()
    caso um caminho inválido de um banco de dados for passado para a função."""
    invalid_db_path = get_invalid_db_path
    retorno = remove_from_users(db_path=invalid_db_path)
    assert 'ERROR' in retorno, print(retorno)
    assert 'DATABASE ERROR' == retorno['ERROR'], print(retorno)


def test_select_patients_data_exception(get_invalid_db_name):
    """Caso de teste que verifica o retorno da função select_patients_data()
    caso um nome inválido de um banco de dados for passado para a função."""
    invalid_db_name = get_invalid_db_name
    retorno = select_patients_data(db_path=invalid_db_name)
    assert 'ERROR' in retorno, print(retorno)
    assert 'AN EXCEPTION OCCURRED' == retorno['ERROR'], print(retorno)


def test_select_pharmacies_data_exception(get_invalid_db_name):
    """Caso de teste que verifica o retorno da função select_pharmacies_data()
    caso um nome inválido de um banco de dados for passado para a função."""
    invalid_db_name = get_invalid_db_name
    retorno = select_pharmacies_data(db_path=invalid_db_name)
    assert 'ERROR' in retorno, print(retorno)
    assert 'AN EXCEPTION OCCURRED' == retorno['ERROR'], print(retorno)


def test_select_trasactions_information_exception(get_invalid_db_name):
    """Caso de teste que verifica o retorno da função select_trasactions_information()
    caso um nome inválido de um banco de dados for passado para a função."""
    invalid_db_name = get_invalid_db_name
    retorno = select_trasactions_information(db_path=invalid_db_name)
    assert 'ERROR' in retorno, print(retorno)
    assert 'AN EXCEPTION OCCURRED' == retorno['ERROR'], print(retorno)


def test_select_user_by_username_pass_exception(get_invalid_db_name):
    """Caso de teste que verifica o retorno da função select_user_by_username_pass()
    caso um nome inválido de um banco de dados for passado para a função."""
    invalid_db_name = get_invalid_db_name
    retorno = select_user_by_username_pass(db_path=invalid_db_name)
    assert 'ERROR' in retorno, print(retorno)
    assert 'AN EXCEPTION OCCURRED' == retorno['ERROR'], print(retorno)


def test_insert_into_users_exception(get_invalid_db_name):
    """Caso de teste que verifica o retorno da função insert_into_users()
    caso um nome inválido de um banco de dados for passado para a função."""
    invalid_db_name = get_invalid_db_name
    retorno = insert_into_users(db_path=invalid_db_name)
    assert 'ERROR' in retorno, print(retorno)
    assert 'AN EXCEPTION OCCURRED' == retorno['ERROR'], print(retorno)

 
def test_remove_from_users_exception(get_invalid_db_name):
    """Caso de teste que verifica o retorno da função remove_from_users()
    caso um nome inválido de um banco de dados for passado para a função."""
    invalid_db_name = get_invalid_db_name
    retorno = remove_from_users(db_path=invalid_db_name)
    assert 'ERROR' in retorno, print(retorno)
    assert 'AN EXCEPTION OCCURRED' == retorno['ERROR'], print(retorno) 


def test_select_user_by_username_pass_user_exception():
    """Caso de teste que verifica o retorno da função select_user_by_username_pass()
    caso um username e um password que não existem no banco de dados forem passados
    para a função."""
    retorno = select_user_by_username_pass(username='0000', password='1111')
    assert 'ERROR' in retorno, print(retorno)
    assert 'USER WITH THESE CREDENTIALS DOES NOT EXIST' == retorno['ERROR'], print(retorno)
