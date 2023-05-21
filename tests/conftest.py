import pytest
from app import create_app

@pytest.fixture()
def client(app):
    client = create_app('config.py')
    client.config.update({"TESTING": True,})

    yield client