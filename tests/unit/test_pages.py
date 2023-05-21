from tests.conftest import client


def test_landing(client):
    landing = client.get("/")
    print("hi")