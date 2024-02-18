from site_main_code import *


class User():
    pass


def name_by_key(nickname=None, email=None, password=None, id=None):
    if email is not None:
        db.regestor(nickname=nickname, email=email, password=password)
    elif nickname is not None:
        db.check_login(nickname=nickname, password=password)
    elif id is not None:
        db.find_user_by_id(user_id=id)
    else:
        print('<eufufufufuf')
