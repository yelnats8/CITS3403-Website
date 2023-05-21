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
    - This file contains all the database table structure. Made using SQLAlchemy and SQLite as the language
- routes.py
    - This file contains all the routes the users will take to navigate the website application

The prompts are stored in a json file called `prompts.json`. We modify this file to change the prompts

## Members
Emily   - 23476614

Miguel  - 22887893

Niketh  - 23262446

Stanley - 22915411


## How to run
### Running the Application
Most of these steps are followig the [mega tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).
1. Create and run your virtual environment
2. Install all the dependencies using pip. There should be a section called ***Pip Installs*** and requirements.txt
3. Initialize the database and create all the necessary tables
    1. `flask db init`
    2. `flask db migrate`
    3. `flask db upgrade`
4. Run with `python main.py`

## Progress Log
#### **(1/05/2023)** 
- Miguel has added a basic user login logout system by following the mega tutorial. If you haven't already, please have a look at it. Stanley is working on a chat feature, building on top of the code. Stanley is following [this tutorial](https://www.youtube.com/watch?v=mkXdvs8H7TA)

#### **(7/05/2023)**
- Stanley has finally finished at least a functional yet super fragile chat. You can create and join chat rooms from the home page. Creating a chat room will automatically generate you a 4 letter room code where you can join. To join a chat room, just input the room code.
    - ~~chat as of now is super fragile, you can break it by putting in a room code that doesn't exist~~
    - You have to be logged in to enter chat rooms, otherwise it will break
    - ~~If you join the room at a later date, you won't see messages from before you joined the room~~
    - ~~chat log isn't really saved anywhere at the moment~~

- Stanley renamed app.py to main.py

#### **(19/05/2023)**
- Chat function now has its own database and can load previous chats when you join the room. However the formatting is a bit  off

#### **(20/5/2023)**
- We underestimated how big the project would be and are now paying the consequences. See git log graph *log.txt* for complete timeline.

## Pip Installs
- pip install flask
- pip install flask-wtf
- pip install flask-sqlalchemy
- pip install flask-migrate
- pip install flask-login
- pip install flask-socketio
- pip install gevent-websocket
- pip install pytest

there is a more detailed view in requirements.txt