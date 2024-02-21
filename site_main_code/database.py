from site_main_code import *


# cmd to create a table
# from site_main_code import db, app
# app.app_context().push()
# db.create_all()

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(40))
    password = db.Column(db.String(40))
    email = db.Column(db.Text, nullable=True)


def regustration(email: str, nickname: str, password: str):
    article = Article(email=email, nickname=nickname, password=password)
    db.session.add(article)
    db.session.commit()
    return get_by_name(nickname, password)[1]


def get_by_name(nickname: str, password: str):
    users = Article.query.filter_by(nickname=nickname).all()
    lst = []
    for i in users:
        lst = [i.id] + [i.nickname] + [i.password]
    if lst[2] == password:
        return True, lst[0]
def get_user_name_password():
    id = request.cookies.get("user_id")
    print(id)

    users = Article.query.filter_by(id=id).all()
    lst = []
    for i in users:
        lst = [i.id] + [i.nickname] + [i.password]
    if len(lst) > 2:
        return lst[1], lst[2]
    else:
        return None

def get_by_cookie_name():
    id = request.cookies.get("user_id")
    print(id)

    users = Article.query.filter_by(id=id).all()
    lst = []
    for i in users:
        lst = [i.id] + [i.nickname] + [i.password]
    if len(lst) > 2:
        return lst[1]
    else:
        return None