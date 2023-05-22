from app.models import User, Post, ChatHistory, PersonalChatHistory
from datetime import datetime
import hashlib



def test_new_user():
    user = User(username= "Bowie_on_Fire", email = "davidbowie@gmail.com")
    user.set_password("catpeople")

    assert user.username == "Bowie_on_Fire"
    assert user.email == "davidbowie@gmail.com"
    assert user.password_hash != "catpeople"
    assert user.check_password("catpeople") == True
    assert user.check_password("loveyoutilltuesday") != True

def test_avatar():
    user = User(username="Bowie_on_Fire", email="davidbowie@gmail.com")
    assert user.avatar(128) == 'https://www.gravatar.com/avatar/{}?d=identicon&s=128'.format(
        hashlib.md5(user.username.lower().encode('utf-8')).hexdigest()
    )
    
def test_post():
    post = Post(body="Hello, world!", author_id=1, profile_id=1)
    assert post.body == "Hello, world!"
    assert post.author_id == 1
    assert post.profile_id == 1

def test_post_length():
    post = Post(body="a" * 200, author_id=1, profile_id=1)
    assert Post.validate_post_length(post.body) == True
    post = Post(body="a" * 201, author_id=1, profile_id=1)
    assert Post.validate_post_length(post.body) == False

def test_chat_history():
    chat = ChatHistory(sender="Bowie_on_Fire", sender_id=1, room_code="1234", 
                       message="Hello, chat!", message_type=1, prompt="Hello?")
    assert chat.sender == "Bowie_on_Fire"
    assert chat.sender_id == 1
    assert chat.room_code == "1234"
    assert chat.message == "Hello, chat!"
    assert chat.message_type == 1
    assert chat.prompt == "Hello?"

def test_personal_chat_history():
    chat = PersonalChatHistory(room_code="1234", prompt="Hello?", 
                               username="Bowie_on_Fire", user_id=1, 
                               message="Hello, chat!", message_type=1, 
                               date=datetime.utcnow())
    assert chat.room_code == "1234"
    assert chat.prompt == "Hello?"
    assert chat.username == "Bowie_on_Fire"
    assert chat.user_id == 1
    assert chat.message == "Hello, chat!"
    assert chat.message_type == 1