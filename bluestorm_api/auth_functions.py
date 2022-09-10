"""Module with the authentication functions"""
import random
import string
from functools import wraps
from datetime import datetime, timedelta
import base64
import hashlib
import jwt
from flask import request, jsonify
from bluestorm_api.sqlite_db import select_user_by_username_pass


SECRET_KEY = ''


def base_64(message):
    """Função que gera uma str com uma chave aleatória."""
    message_bytes = message.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('utf-8')
    return base64_message


def hash_data(first_key):
    """Função que gera uma str com uma chave aleatória."""
    m1_encoded = first_key.encode('utf-8')
    m1_encoded_hex = hashlib.md5(m1_encoded).hexdigest()
    m1_encoded_hex_b64 = base_64(m1_encoded_hex)
    return m1_encoded_hex_b64


def generate_a_secret_key():
    """Função que gera uma str com uma chave aleatória."""
    random_str = string.ascii_letters + string.digits + string.ascii_uppercase
    first_key = ''.join(random.choice(random_str) for i in range(12))
    final_key = hash_data(first_key)
    return final_key


def secret_key():
    """Função que atualiza o valor de SECRET_KEY com uma
    str que corresponde a uma chave aleatória."""
    global SECRET_KEY
    SECRET_KEY = generate_a_secret_key()


def auth(authorization):
    """Função que gera um token jwt para ser retornado por meio de um dict pela função.
    Caso inconformiades com a autenticação sejam detectadas a devida mensagem de erro
    também é retornada por meio de um dict pela função."""
    if (not authorization or
        not authorization.username or not authorization.password):
        auth_error = {'MESSAGE': 'COULD NOT VERIFY',
                'WWW-AUTHENTICATE': 'BASIC AUTH="LOGIN REQUIRED"'}
        return jsonify(auth_error), 401
    user_data = select_user_by_username_pass(authorization.username, authorization.password)
    if 'ERROR' in user_data:
        auth_error = {'MESSAGE': user_data['ERROR'], 'DATA': {}}
        return jsonify(auth_error), 401
    if ('uuid' in user_data and
          'username' in user_data and
          'password' in user_data):
        exp = datetime.now() + timedelta(hours=12)
        secret_key()
        token = jwt.encode({ 'username': user_data['username'], 'exp': exp },
                             SECRET_KEY, algorithm="HS256")
        auth_validated = {'MESSAGE': 'VALIDATED SUCCESSFULLY',
                             'TOKEN': token, 'EXP': str(exp).upper()}
        return auth_validated
    auth_error = {'MESSAGE': 'COULD NOT VERIFY', 'WWW-AUTHENTICATE': 'BASIC AUTH="LOGIN REQUIRED"'}
    return jsonify(auth_error), 401


def token_required(func):
    """Função contém um decorator que realiza a decodificação de um token jwt.
    Retorna um JSON em caso de incondormidades em encontrar ou decodificar o token."""
    @wraps(func)
    def decorated():
        token = request.args.get('token')
        if not token:
            error_message = {'MESSAGE': 'TOKEN IS MISSING', 'DATA': {}}
            return jsonify(error_message), 401
        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.exceptions.InvalidSignatureError as exc:
            print(type(exc), exc)
            error_message = {'MESSAGE': 'TOKEN IS INVALID OR EXPIRED', 'DATA': {}}
            return jsonify(error_message), 401
        except jwt.exceptions.DecodeError as exc:
            print(type(exc), exc)
            error_message = {'MESSAGE': 'TOKEN IS INVALID OR EXPIRED', 'DATA': {}}
            return jsonify(error_message), 401
        except Exception as exc:
            print(type(exc), exc)
            error_message = {'MESSAGE': 'TOKEN IS INVALID OR EXPIRED', 'DATA': {}}
            return jsonify(error_message), 401
        return func()
    return decorated
