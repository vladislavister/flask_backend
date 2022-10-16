from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api()


@app.route('/')
def hello_world():  # put application's code here
    return 'Use /users, /categories or /records'

from src import users
from src import categories
from src import records