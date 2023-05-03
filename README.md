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
4. Run with `flask run`