from flask import Flask, request, render_template, make_response
from flask_sqlalchemy import SQLAlchemy
from site_main_code import database

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)





from site_main_code import database, server
