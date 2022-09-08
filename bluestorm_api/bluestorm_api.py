"""Third party functions"""
from flask import request, jsonify, Blueprint

"""Local functions"""
from bluestorm_api.sqlite_db import select_patients_data, select_pharmacies_data, select_trasactions_information
from bluestorm_api.auth_functions import auth, token_required
from bluestorm_api.extra_args_para_busca import get_patients_args, get_pharmacies_args, get_transactions_args
from bluestorm_api.extra_sanitize import sanitize_input


bp = Blueprint('bluestorm_api', __name__)


@bp.route('/patients', methods=['GET'])
@token_required
def patients_endpoint():
    """Endpoint onde serão listadas as informações dos pacientes."""
    if request.method == 'GET':
        f_n = get_patients_args(request.args)
        first_name = sanitize_input(f_n)
        json_data = jsonify(select_patients_data(first_name=first_name))
        return json_data


@bp.route('/pharmacies', methods=['GET'])
@token_required
def pharmacies_endpoint():
    """Endpoint onde serão listadas as informações das farmácias."""
    if request.method == 'GET':
        n = get_pharmacies_args(request.args)
        name = sanitize_input(n)
        json_data = jsonify(select_pharmacies_data(name=name))
        return json_data


@bp.route('/transactions', methods=['GET'])
@token_required
def transactions_endpoint():
    """Endpoint onde serão listadas as informações das transações."""
    if request.method == 'GET':
        pa_f_n, ph_n = get_transactions_args(request.args)
        pa_first_name = sanitize_input(pa_f_n)
        ph_name = sanitize_input(ph_n)
        json_data = jsonify(select_trasactions_information(pa_first_name=pa_first_name, ph_name=ph_name))
        return json_data


@bp.route('/auth', methods=['GET', 'POST'])
def authenticate():
    """Endpoint onde a autenticação é realizada."""
    if request.method == 'POST':
        data = auth(request.authorization)
        return data
    else:
        return jsonify({'ERROR': 'REQUEST METHOD NOT ALLOWED'})

