import os
from flask import Flask
app = Flask(__name__, template_folder='./templates')
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'