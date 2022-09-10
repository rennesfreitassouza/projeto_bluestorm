"""Module with SQL Queries"""
import sqlite3
from bluestorm_api.useful_functions import patients_data_to_json, pharmacies_data_to_json
from bluestorm_api.useful_functions import trasactions_information_to_json, get_one_user


DATABASE_PATH = 'bluestorm_api/backend_test.db'


def conectar_sqlite(db_path=None):
    """Inicia uma conexão com o banco de dados SQLite. Retorna uma variável do tipo Connection."""
    try:
        if db_path is None:
            db_path = DATABASE_PATH 
        conn = sqlite3.connect(db_path)
    except sqlite3.OperationalError as exc:
        print(type(exc), exc)
        return None
    return conn


def desconectar_sqlite(conn):
    """Encerra a conexão com o banco de dados SQLite"""
    conn.close()


def select_patients_data(first_name='', db_path=None):
    """Faz uma consulta relativa a dados de pacientes no banco de dados SQLite.
       Retorna um dict com os dados retornados da consulta."""
    conn = conectar_sqlite(db_path)
    if conn is None:
        dict_data = {'ERROR': 'DATABASE ERROR'}
    else:
        try:
            cursor = conn.execute(f'''SELECT UUID, FIRST_NAME, LAST_NAME, DATE_OF_BIRTH
                                          FROM PATIENTS
                                          WHERE FIRST_NAME LIKE "%{first_name}%"''')
            dict_data = patients_data_to_json(cursor)
        except sqlite3.OperationalError as exc:
            print(type(exc), exc)
            dict_data = {'ERROR': 'AN EXCEPTION OCCURRED'}
        desconectar_sqlite(conn)
    return dict_data


def select_pharmacies_data(name='', db_path=None):
    """Faz uma consulta relativa a dados de farmácias no banco de dados SQLite.
       Retorna um dict com os dados retornados da consulta."""
    conn = conectar_sqlite(db_path)
    if conn is None:
        dict_data = {'ERROR': 'DATABASE ERROR'}
    else:
        try:
            cursor = conn.execute(f'''SELECT UUID, NAME, CITY
                                    FROM PHARMACIES
                                    WHERE NAME LIKE "%{name}%"''')
            dict_data = pharmacies_data_to_json(cursor)
        except sqlite3.OperationalError as exc:
            print(type(exc), exc)
            dict_data = {'ERROR': 'AN EXCEPTION OCCURRED'}
        desconectar_sqlite(conn)
    return dict_data


def select_trasactions_information(pa_first_name='', ph_name='', db_path=None):
    """Faz uma consulta relativa a dados de pacientes, farmácias e transações
       no banco de dados SQLite.
       Retorna um dict com os dados retornados da consulta."""
    conn = conectar_sqlite(db_path)
    if conn is None:
        dict_data = {'ERROR': 'DATABASE ERROR'}
    else:
        try:
            cursor = conn.execute(f'''SELECT PA.UUID, PA.FIRST_NAME, PA.LAST_NAME, PA.DATE_OF_BIRTH,
                                    PH.UUID, PH.NAME, PH.CITY,
                                    T.UUID, T.AMOUNT, T.TIMESTAMP
                                    FROM PATIENTS AS PA, PHARMACIES AS PH, TRANSACTIONS AS T
                                    WHERE PA.UUID = T.PATIENT_UUID AND
                                    PH.UUID = T.PHARMACY_UUID AND
                                    PA.FIRST_NAME LIKE "%{pa_first_name}%" AND
                                    PH.NAME LIKE "%{ph_name}%"''')
            dict_data = trasactions_information_to_json(cursor)
        except sqlite3.OperationalError as exc:
            print(type(exc), exc)
            dict_data = {'ERROR': 'AN EXCEPTION OCCURRED'}
        desconectar_sqlite(conn)
    return dict_data


def select_user_by_username_pass(username='', password='', db_path=None):
    """Faz uma consulta com o banco de dados SQLite
       Retorna um dict com os dados retornados da consulta."""
    conn = conectar_sqlite(db_path)
    if conn is None:
        dict_data = {'ERROR': 'DATABASE ERROR'}
    else:
        try:
            cursor = conn.execute(f'''SELECT U.UUID, U.USERNAME, U.PASSWORD
                                      FROM USERS AS U
                                      WHERE U.USERNAME = "{username}" AND
                                      U.PASSWORD = "{password}"''')
            dict_data = get_one_user(cursor)
        except sqlite3.OperationalError as exc:
            print(type(exc), exc)
            dict_data = {'ERROR': 'AN EXCEPTION OCCURRED'}
        desconectar_sqlite(conn)
    return dict_data


def insert_into_users(uuid='', username='', password='', db_path=None):
    """Função que insere dados de um usuário na tabela USERS do banco de dados."""
    conn = conectar_sqlite(db_path)
    if conn is None:
        dict_data = {'ERROR': 'DATABASE ERROR'}
    else:
        try:
            conn.execute(f'''INSERT INTO USERS (UUID, USERNAME, PASSWORD)
                             VALUES ("{uuid}", "{username}", "{password}" );''')
            conn.commit()
            dict_data = {'MESSAGE': 'USER ADDED'}
        except sqlite3.OperationalError as exc:
            print(type(exc), exc)
            dict_data = {'ERROR': 'AN EXCEPTION OCCURRED'}
        desconectar_sqlite(conn)
    return dict_data
    