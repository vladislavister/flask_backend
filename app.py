from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api()


@app.route('/user')
def hello_world():  # put application's code here
    return 'Hello World!'

from src import users