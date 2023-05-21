from app.models import User



def test_new_user():
    user = User(username= "Farquaad", email = "farquaadmail@gmail.com")
    user.set_password("princessfiona")

    assert user.username == "Farquaad"
    assert user.email == "farquaadmail@gmail.com"
    assert user.password_hash != "princessfiona"