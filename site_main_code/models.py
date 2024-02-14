from site_main_code import *


class User():
    pass


def name_by_key():
    if request.cookies.get('foo') == '1':
        return "Всеволод Бари"
    if request.cookies.get('foo') == '2':
        return "Antony"
