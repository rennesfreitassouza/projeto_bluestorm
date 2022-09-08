"""Modules integrated with the Python interpreter"""
import random
import string
from functools import wraps
from datetime import datetime, timedelta

"""Third party modules"""
import jwt
from flask import request, jsonify

"""Local functions"""
from bluestorm_api.sqlite_db import select_user_by_username_pass


SECRET_KEY = ''


def generate_a_secret_key():
    random_str = string.ascii_letters + string.digits + string.ascii_uppercase
    key = ''.join(random.choice(random_str) for i in range(12))
    return key


def secret_key():
    global SECRET_KEY
    SECRET_KEY = generate_a_secret_key()
    print(SECRET_KEY)


def auth(authorization):
    auth = authorization
    if not auth or not auth.username or not auth.password:
        auth_error = {'MESSAGE': 'COULD NOT VERIFY', 'WWW-AUTHENTICATE': 'BASIC AUTH="LOGIN REQUIRED"'}
        return jsonify(auth_error), 401
    
    user_data = select_user_by_username_pass(auth.username, auth.password)
    if 'ERROR' in user_data.keys():
        auth_error = {'MESSAGE': user_data['ERROR'], 'DATA': {}}
        return jsonify(auth_error), 401
    elif ('uuid' in user_data.keys() and
          'username' in user_data.keys() and
          'password' in user_data.keys()):
          exp = datetime.now() + timedelta(hours=12)
          token = jwt.encode({ 'username': user_data['username'], 'exp': exp }, SECRET_KEY, algorithm="HS256")
          auth_validated = {'MESSAGE': 'VALIDATED SUCCESSFULLY', 'TOKEN': token, 'EXP': str(exp).upper()}
          return auth_validated
    
    auth_error = {'MESSAGE': 'COULD NOT VERIFY', 'WWW-AUTHENTICATE': 'BASIC AUTH="LOGIN REQUIRED"'}
    return jsonify(auth_error), 401
    

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            error_message = {'MESSAGE': 'TOKEN IS MISSING', 'DATA': {}}
            return jsonify(error_message), 401
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except Exception as exc:
            error_message = {'MESSAGE': 'TOKEN IS INVALID OR EXPIRED', 'DATA': {}}
            return jsonify(error_message), 401
        return func()
    return decorated
