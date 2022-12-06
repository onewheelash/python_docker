from flask import Flask
app = Flask(__name__)

app.route('/')
def hello_world():
    return 'Hello, Docker!'


# to test the app
#cd /path/to/python-docker
#source .venv/bin/activate
#(.venv) $ python3 -m flask run


#to setup Flask
#cd /path/to/python-docker
#python3 -m venv .venv
#source .venv/bin/activate
#(.venv) $ python3 -m pip install Flask
#(.venv) $ python3 -m pip freeze > requirements.txt
#(.venv) $ touch app.py