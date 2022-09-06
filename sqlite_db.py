"""Modules integrated with the Python interpreter"""
import sqlite3

"""Local functions"""
from useful_functions import patients_data_to_json, pharmacies_data_to_json, trasactions_information_to_json, get_one_user


def conectar_sqlite():
    try:
        conn = sqlite3.connect('backend_test.db')
    except Exception as exc:
        print(exc)
        return None
    return conn


def desconectar_sqlite(conn):
    conn.close()


def select_patients_data():
    conn = conectar_sqlite()
    if conn is None:
        dict_data = {'Error': 'Database error'}
    else:
        try:
            cursor = conn.execute('''SELECT UUID, FIRST_NAME, LAST_NAME, DATE_OF_BIRTH
                                    FROM PATIENTS''')
            dict_data = patients_data_to_json(cursor)
        except Exception as exc:
            print(exc)
            dict_data = {'Error': 'An exception occurred.'}
        desconectar_sqlite(conn)
    return dict_data


def select_pharmacies_data():
    conn = conectar_sqlite()
    if conn is None:
        dict_data = {'Error': 'Database error'}
    else:
        try:
            cursor = conn.execute('''SELECT UUID, NAME, CITY
                                    FROM PHARMACIES''')
            dict_data = pharmacies_data_to_json(cursor)
        except Exception as exc:
            print(exc)
            dict_data = {'Error': 'An exception occurred.'}
        desconectar_sqlite(conn)
    return dict_data


def select_trasactions_information():
    conn = conectar_sqlite()
    if conn is None:
        dict_data = {'Error': 'Database error'}
    else:
        try:
            cursor = conn.execute('''SELECT PA.UUID, PA.FIRST_NAME, PA.LAST_NAME, PA.DATE_OF_BIRTH,
                                    PH.UUID, PH.NAME, PH.CITY,
                                    T.UUID, T.AMOUNT, T.TIMESTAMP
                                    FROM PATIENTS AS PA, PHARMACIES AS PH, TRANSACTIONS AS T
                                    WHERE PA.UUID = T.PATIENT_UUID AND
                                    PH.UUID = T.PHARMACY_UUID''')
            dict_data = trasactions_information_to_json(cursor)
        except Exception as exc:
            print(exc)
            dict_data = {'Error': 'An exception occurred.'}
        desconectar_sqlite(conn)
    return dict_data


def select_user_by_username_pass(username='', password=''):
    conn = conectar_sqlite()
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