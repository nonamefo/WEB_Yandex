import random
import os

from flask import Flask, render_template, request, make_response, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
import requests
import smtplib
from decouple import config

app = Flask(__name__)

os.environ['FLASK_ENV'] = 'production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['DEBUG'] = False
app.config['TESTING'] = False
app.config['PROPAGATE_EXCEPTIONS'] = None
app.config['SECRET_KEY'] = 'frog_and_rabit'
app.config['PERMANENT_SESSION_LIFETIME'] = None
app.config['USE_X_SENDFILE'] = False

db = SQLAlchemy(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
link_API = 'https://f720-94-29-124-153.ngrok-free.app'

try:
    API_key = requests.get(link_API + '/getapikey',
                           json={'login': '123', 'password': '321'}).json()['api_key']
except KeyError:
    requests.post(link_API + '/getapikey',
                  json={'login': '123', 'password': '321'}).json()
    API_key = requests.get(link_API + '/getapikey',
                           json={'login': '123', 'password': '321'}).json()['api_key']

from site_main_code import database, server, models
