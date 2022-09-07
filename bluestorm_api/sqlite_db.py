"""Modules integrated with the Python interpreter"""
import sqlite3

"""Local functions"""
from bluestorm_api.useful_functions import patients_data_to_json, pharmacies_data_to_json, trasactions_information_to_json, get_one_user


DATABASE_PATH = 'bluestorm_api/backend_test.db'


def conectar_sqlite(db_path=None):
    try:
        if db_path is None:
            db_path = DATABASE_PATH 
        conn = sqlite3.connect(db_path)
    except Exception as exc:
        print(exc)
        return None
    return conn


def desconectar_sqlite(conn):
    conn.close()


def select_patients_data(first_name='', db_path=None):
    conn = conectar_sqlite(db_path)
    if conn is None:
        dict_data = {'Error': 'Database error'}
    else:
        try:
            cursor = conn.execute(f'''SELECT UUID, FIRST_NAME, LAST_NAME, DATE_OF_BIRTH
                                          FROM PATIENTS
                                          WHERE FIRST_NAME LIKE "%{first_name}%"''')
            dict_data = patients_data_to_json(cursor)
        except Exception as exc:
            print(exc)
            dict_data = {'Error': 'An exception occurred.'}
        desconectar_sqlite(conn)
    return dict_data


def select_pharmacies_data(name='', db_path=None):
    conn = conectar_sqlite(db_path)
    if conn is None:
        dict_data = {'Error': 'Database error'}
    else:
        try:
            cursor = conn.execute(f'''SELECT UUID, NAME, CITY
                                    FROM PHARMACIES
                                    WHERE NAME LIKE "%{name}%"''')
            dict_data = pharmacies_data_to_json(cursor)
        except Exception as exc:
            print(exc)
            dict_data = {'Error': 'An exception occurred.'}
        desconectar_sqlite(conn)
    return dict_data


def select_trasactions_information(pa_first_name='', ph_name='', db_path=None):
    conn = conectar_sqlite(db_path)
    if conn is None:
        dict_data = {'Error': 'Database error'}
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
        except Exception as exc:
            print(exc)
            dict_data = {'Error': 'An exception occurred.'}
        desconectar_sqlite(conn)
    return dict_data


def select_user_by_username_pass(username='', password='', db_path=None):
    conn = conectar_sqlite(db_path)
    if conn is None:
        dict_data = {'Error': 'Database error'}
    else:
        try:
            cursor = conn.execute(f'''SELECT U.UUID, U.USERNAME, U.PASSWORD
                                      FROM USERS AS U
                                      WHERE U.USERNAME = "{username}" AND
                                      U.PASSWORD = "{password}"''')
            
            dict_data = get_one_user(cursor)
        except Exception as exc:
            print(exc)
            dict_data = {'Error': 'An exception occurred.'}
        desconectar_sqlite(conn)
    return dict_data

