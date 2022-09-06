"""Modules integrated with the Python interpreter"""
import random
import string
from functools import wraps
from datetime import datetime, timedelta

"""Third party modules"""
import jwt
from flask import request, jsonify

"""Local functions"""
from sqlite_db import select_user_by_username_pass


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
        auth_error = {'message': 'Could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}
        return jsonify(auth_error), 401
    
    user_data = select_user_by_username_pass(auth.username, auth.password)
    if 'Error' in user_data.keys():
        auth_error = {'message': user_data['Error'], 'data': {}}
        return jsonify(auth_error), 401
    elif ('uuid' in user_data.keys() and
          'username' in user_data.keys() and
          'password' in user_data.keys()):
          exp = datetime.now() + timedelta(hours=12)
          token = jwt.encode({ 'username': user_data['username'], 'exp': exp }, SECRET_KEY, algorithm="HS256")
          auth_validated = {'message': 'Validated successfully', 'token': token, 'exp': exp}
          return auth_validated
    
    auth_error = {'message': 'Could not verify', 'WWW-Authenticate': 'Basic auth="Login Required"'}
    return jsonify(auth_error), 401
    

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            error_message = {'message': 'token is missing', 'data': {}}
            return jsonify(error_message), 401
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except Exception as exc:
            error_message = {'message': 'token is invalid or expired', 'data': {}}
            return jsonify(error_message), 401
        return func()
    return decorated
