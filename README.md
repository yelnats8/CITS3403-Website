# CITS3403-Website
This is a repository for the CITS3403 (Agile Web Development) project.

The website is **OmegeLUL**, a website inspired by **Omegle**. 

Users log in and match up for a one on one discussion with someone random who is also looking for a conversation. They will be put in a chat and be given a random prompt to get the conversation going.

The application is made using Flask.

The application itself contains 4 python files:
- chat.py
    - This file contains the socket programming that communicates between the server and the client
- forms.py
    - This file contains all of the user forms made using flask forms
- models.py
    - This file contains all the database table structure. Made using SQLAlchemy and SQLite
- routes.py
    - This file contains all the routes the users will take to navigate the website application

## Members
Emily   - 23476614

Miguel  - 22887893

Niketh  - 23262446

Stanley - 22915411



## Pip Installs
- pip install flask
- pip install flask-wtf
- pip install flask-sqlalchemy
- pip install flask-migrate
- pip install flask-login
- pip install flask-socketio
- pip install gevent-websocket


## How to run
### Running the Application
Most of these steps are followig the [mega tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).
1. Create and run your virtual environment
    1. python3 -m venv venv
2. Install all the dependencies using pip. There should be a section called ***Pip Installs*** and requirements.txt
3. Initialize the database and create all the necessary tables
    1. `flask db init`
    2. `flask db migrate`
    3. `flask db upgrade`
4. Run with `python main.py`


## Running Unit Tests
1. The unit tests require python's native unit testing API, pytest. Install pytest with `pip install pytest`
2. To run the unit tests, simply type `pytest` in the command line