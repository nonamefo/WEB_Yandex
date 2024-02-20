from site_main_code import *


# cmd to create a table
# from site_main_code import app
# app.app_context().push()
# db.create_all()

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(40))
    password = db.Column(db.String(40))
    email = db.Column(db.Text, nullable=True)


def regustration_or_login():
    try:
        email = request.form["email"]
        nickname = request.form["nickname"]
        password = request.form["password"]
        article = Article(email=email, nickname=nickname, password=password)
        db.session.add(article)
        db.session.commit()
        print(email, nickname, password)
        return 1
    except Exception:
        email = ''
        nickname = request.form["nickname"]
        password = request.form["password"]
