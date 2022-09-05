"""Third party functions"""
from flask import Flask, request, jsonify

"""Local functions"""
from sqlite_db import select_patients_data, select_pharmacies_data, select_trasactions_information


app = Flask(__name__)


@app.route('/patients', methods=['GET'])
def patients_endpoint():
    """Endpoint onde serão listadas as informações dos pacientes."""
    if request.method == 'GET':
        json_data = jsonify(select_patients_data())
        return json_data
    else:
        return 'Request method not allowed'


@app.route('/pharmacies', methods=['GET'])
def pharmacies_endpoint():
    """Endpoint onde serão listadas as informações das farmácias."""
    if request.method == 'GET':
        json_data = jsonify(select_pharmacies_data())
        return json_data
    else:
        return 'Request method not allowed'


@app.route('/transactions')
def transactions_endpoint():
    """Endpoint onde serão listadas as informações das transações."""
    if request.method == 'GET':
        json_data = jsonify(select_trasactions_information())
        return json_data
    else:
        return 'Request method not allowed'

