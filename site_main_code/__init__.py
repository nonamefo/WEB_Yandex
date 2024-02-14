from flask import Flask, request, render_template, make_response
from flask_login import LoginManager

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
db = 'база данных'

from site_main_code import db, server
