# CITS3403-Website
This is a repository for the CITS3403 (Agile Web Development) project. As of 23/04/2023 the website will be an **Omegle Clone**

## Members
Emily   - 

Miguel  - 22887893

Niketh  - 

Stanley - 22915411

## Progress Log

#### **(1/05/2023)** 
- Miguel has added a basic user login logout system by following the mega tutorial. If you haven't already, please have a look at it. Stanley is working on a chat feature, building on top of the code. Stanley is following [this tutorial](https://www.youtube.com/watch?v=mkXdvs8H7TA)

#### **(7/05/2023)**
- Stanley has finally finished at least a functional yet super fragile chat. You can create and join chat rooms from the home page. Creating a chat room will automatically generate you a 4 letter room code where you can join. To join a chat room, just input the room code.
    - chat as of now is super fragile, you can break it by putting in a room code that doesn't exist
    - You have to be logged in to enter chat rooms, otherwise it will break
    - If you join the room at a later date, you won't see messages from before you joined the room
    - chat log isn't really saved anywhere at the moment

- Stanley renamed app.py to main.py

## Pip Installs
- pip install flask
- pip install flask-wtf
- pip install flask-sqlalchemy
- pip install flask-migrate
- pip install flask-login
- pip install flask-socketio
- pip install gevent-websocket


## How to run
Most of these steps are followig the [mega tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).
1. Create and run your virtual environment
    1. python3 -m venv venv
2. Install all the dependencies using pip. There should be a section called ***Pip Installs***
3. Initialize the database and create all the necessary tables
    1. `flask db init`
    2. `flask db migrate -m "users table"`
    3. `flask db upgrade`
4. ~~Run with `flask run`~~ Run with `python main.py` (This is because running with `flask run` for some reason gives a warning about WebSockets although I havent run into any problems with it yet. This is just to be safe)