from app import app

def test_landing():
    client = app.test_client()

    home = client.get("/")
    login = client.get("/login")
    logout = client.get("/logout")

    chat = client.get("/chat")
    history = client.get("/history")
    
    assert home.status_code == 200
    assert login.status_code == 200
    assert logout.status_code == 302

    #None of these should pass when no credentials have been handed in
    assert chat.status_code == 500
    assert history.status_code == 500