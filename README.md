Подготовка к запуску проекта:
необходимо создать файл .env и поместить в него две переменные email_password и email_sender.
В них должен храниться пароль от почты настроенный для работы со стороними приложениями и адрес этой же электронной почты соответственно.
После чего небоходимо подключить API с заданиями.
Для этого небходимо прописать путь к ней в переменной link_API в файле __init__ который в свою очередь находиться в дериктории site_main_code.
После чего скрипты сами запросят API ключ. Либо пропишите его сами в переменной API_key она в том же файле что и link_API