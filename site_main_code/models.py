from site_main_code.database import regustration, get_by_name, get_by_cookie_name, get_user_name_password
from site_main_code import requests, API_key ,link_API


def get_info_by_name(nickname: str, password: str):
    return get_by_name(nickname, password)


def get_info_by_email(email: str, nickname: str, password: str):
    return regustration(email, nickname, password)





def get_all_tasks():
    return requests.get(f'{link_API}/{API_key}/questions').json()

def get_test(id_test):
    return requests.get(f'{link_API}/{API_key}/questions/{id_test}').json()


def name_and_password():
    return get_user_name_password()


def name_by_key():
    return get_by_cookie_name()
