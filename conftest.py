"""Modules integrated with the Python interpreter"""
from base64 import b64encode
import json

"""Third party functions"""
import pytest


"""Local functions"""
from bluestorm_api import create_app


@pytest.fixture
def app():
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    app.testing = True
    return app.test_client()


@pytest.fixture
def get_valid_token(client):
    credentials = b64encode(b'admin:admin').decode('utf-8')
    response = client.post('/auth', headers={'Authorization': f'Basic {credentials}'})
    data_dict = json.loads(response.data)
    return data_dict

@pytest.fixture
def get_invalid_db_path():
    return 'bluestorm_api_/backend_test.db'

@pytest.fixture
def get_invalid_db_name():
    return 'bluestorm_api/backend_test_.db'