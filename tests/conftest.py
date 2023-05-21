import pytest
from app import create_app
from app import app as flask_app

@pytest.fixture()
def app():
    client = create_app()
    client.config.update({"TESTING": True,})

    print("yahoo")

    yield client


@pytest.fixture()
def client(app):
    return app.test_client()