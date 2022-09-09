"""Modulo com diversas funções utilizadas por diversos outros casos de teste"""
from base64 import b64encode
import json
import pytest
from bluestorm_api import create_app


@pytest.fixture
def app():
    """Função inicia a execução da API"""
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    """Função instancia valor para um atributo de app 
    relativo a testes e retorna um objeto também relativo
    a testes por meio de app.test_client()"""
    app.testing = True
    return app.test_client()


@pytest.fixture
def get_valid_token(client):
    """Função obtém um token válido do endpoint /auth utilizando Basic
    Auth. O usuário admin e a senha admin já estão presentes no
    banco de dados, assim um token válido é retornado pela função."""
    credentials = b64encode(b'admin:admin').decode('utf-8')
    response = client.post('/auth', headers={'Authorization': f'Basic {credentials}'})
    data_dict = json.loads(response.data)
    return data_dict

@pytest.fixture
def get_invalid_db_path():
    """Função que retorna um path inválido para um banco de dados."""
    return 'bluestorm_api_/backend_test.db'

@pytest.fixture
def get_invalid_db_name():
    """Função que retorna um path com um nome de banco de dados
    que não existe."""
    return 'bluestorm_api/backend_test_.db'
