"""Módulo utilizado para iniciar a execução da API."""
from flask import Flask
from bluestorm_api.auth_functions import generate_a_secret_key


def create_app(test_config=None):
    """Função cria um app Flask"""
    app = Flask(__name__)
    app.secret_key = generate_a_secret_key()

    from . import bluestorm_api
    app.register_blueprint(bluestorm_api.bp)

    return app