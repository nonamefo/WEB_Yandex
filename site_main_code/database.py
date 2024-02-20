from site_main_code import *
from site_main_code.models import Article

def regestration_or_login():
    try:
        email = request.form["email"]
        nickname = request.form["nickname"]
        password = request.form["password"]
        article = Article(title=nickname, nickname=nickname, password=password)
    except Exception:
        email = ''
        nickname = request.form["nickname"]
        password = request.form["password"]
        article = Article(nickname=nickname, password=password)
