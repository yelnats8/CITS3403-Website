from app.models import User



def test_new_user():
    user = User(username= "Bowie_on_Fire", email = "davidbowie@gmail.com")
    user.set_password("catpeople")

    assert user.username == "Bowie_on_Fire"
    assert user.email == "davidbowie@gmail.com"
    assert user.password_hash != "catpeople"
    assert user.check_password("catpeople") == True
    assert user.check_password("loveyoutilltuesday") != True