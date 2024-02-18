from flask import Flask, request, render_template, make_response
import sqlite3

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

from site_main_code import db, server
