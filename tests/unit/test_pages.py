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

def test_registration():
    client = app.test_client()

    register = client.get("/register")

    # Assuming registration page exists and returns status code 200
    assert register.status_code == 200

def test_user_profile():
    client = app.test_client()

    # Assuming the user profile page is at /user/<username>
    profile = client.get("/user/Bowie_on_Fire")

    # This should return a 500 or 404 as the user does not exist
    assert profile.status_code == 401

def test_post_view():
    client = app.test_client()

    # Assuming the post view page is at /post/<post_id>
    post_view = client.get("/post/1")

    # This should return a 500 or 404 as the post does not exist
    assert post_view.status_code in [404, 500]

def test_error_page():
    client = app.test_client()

    # This page doesn't exist, so should return a 404 error
    not_exist = client.get("/thispagedoesnotexist")

    assert not_exist.status_code == 404
