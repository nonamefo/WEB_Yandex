from site_main_code import *


def regestor(nickname, email, password):

    # Проверяем существование таблицы users в базе данных
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    table_exists = cursor.fetchall()

    if not table_exists:  # Если таблицы не существует, создаем её
        cursor.execute('''CREATE TABLE users
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nickname TEXT,
                          email TEXT,
                          password TEXT)''')
        conn.commit()

    # Записываем данные пользователя в базу данных
    cursor.execute("INSERT INTO users (nickname, email, password) VALUES (?, ?, ?)", (nickname, email, password))
    conn.commit()

    conn.close()

def check_login(nickname, password):


    cursor.execute("SELECT * FROM users WHERE nickname=? AND password=?", (nickname, password))
    user = cursor.fetchone()

    conn.close()

    return user


def find_user_by_id(user_id):


    # Поиск пользователя по его идентификатору
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = cursor.fetchone()

    conn.close()

    return user