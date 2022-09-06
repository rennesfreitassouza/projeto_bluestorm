"""Third party functions"""
from flask import request, jsonify, Blueprint

"""Local functions"""
from bluestorm_api.sqlite_db import select_patients_data, select_pharmacies_data, select_trasactions_information
from bluestorm_api.auth_functions import auth, token_required, generate_a_secret_key


bp = Blueprint('bluestorm_api', __name__)


@bp.route('/patients', methods=['GET'])
@token_required
def patients_endpoint():
    """Endpoint onde serão listadas as informações dos pacientes."""
    if request.method == 'GET':
        json_data = jsonify(select_patients_data())
        return json_data
    else:
        return 'Request method not allowed'


@bp.route('/pharmacies', methods=['GET'])
@token_required
def pharmacies_endpoint():
    """Endpoint onde serão listadas as informações das farmácias."""
    if request.method == 'GET':
        json_data = jsonify(select_pharmacies_data())
        return json_data
    else:
        return 'Request method not allowed'


@bp.route('/transactions', methods=['GET'])
@token_required
def transactions_endpoint():
    """Endpoint onde serão listadas as informações das transações."""
    if request.method == 'GET':
        json_data = jsonify(select_trasactions_information())
        return json_data
    else:
        return 'Request method not allowed'


@bp.route('/auth', methods=['POST'])
def authenticate():
    """Endpoint onde a autenticação é realizada."""
    if request.method == 'POST':
        data = auth(request.authorization)
        return data
    else:
        return 'Request method not allowed'