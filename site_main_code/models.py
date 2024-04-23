from site_main_code.database import get_password , regustration, get_by_name, get_by_cookie_name, get_user_name_password
from site_main_code import requests, API_key, link_API
# импортирование необходимых библиотек функций и переменных

# получение id пользователя по имени и паролю

def get_id_by_name(nickname: str, password: str):
    user_result = get_by_name(nickname, password)
    if user_result:
        return user_result
    else:
        return None

# создание пользователя с получением данных
def create_user(email: str, nickname: str, password: str):
    return regustration(email, nickname, password)

# получение никнейма и пароля пользователя
def name_and_password():
    return get_user_name_password()

# получение никнейма пользователя по id
def name_by_key():
    return get_by_cookie_name()

def get_password_by_email(email:str):
    password = get_password(email)
    if password is not None:
        return password
    else:
        return "Неверный адрес"
def get_all_tasks():
    return requests.get(f'{link_API}/{API_key}/questions').json()

def get_test(id_test):
    return requests.get(f'{link_API}/{API_key}/questions/{id_test}').json()