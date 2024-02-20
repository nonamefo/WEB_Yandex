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

    def __repr__(self):
        return '<User %r>' % (self.nickname)




def name_by_key(nickname=None, email=None, password=None, id=None):
    if email is not None:
        db.regestor(nickname=nickname, email=email, password=password)
    elif nickname is not None:
        db.check_login(nickname=nickname, password=password)
    elif id is not None:
        db.find_user_by_id(user_id=id)
    else:
        print('<eufufufufuf')


