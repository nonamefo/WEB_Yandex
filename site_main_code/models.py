from site_main_code.database import regustration, get_by_name, get_by_cookie_name, get_user_name_password
from site_main_code import requests, API_key, link_API
# импортирование необходимых библиотек функций и переменных

# получение id пользователя по имени и паролю
def get_id_by_name(nickname: str, password: str):
    return get_by_name(nickname, password)

# создание пользователя с получением данных
def create_user(email: str, nickname: str, password: str):
    return regustration(email, nickname, password)


def name_and_password():
    return get_user_name_password()


def name_by_key():
    return get_by_cookie_name()


def get_all_tasks():
    return requests.get(f'{link_API}/{API_key}/questions').json()

def get_test(id_test):
    return requests.get(f'{link_API}/{API_key}/questions/{id_test}').json()