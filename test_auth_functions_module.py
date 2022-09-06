"""Local functions"""
from bluestorm_api.auth_functions import secret_key, SECRET_KEY


def test_secret_key_function():
    s_k = secret_key()
    assert '' == SECRET_KEY, print(SECRET_KEY)


