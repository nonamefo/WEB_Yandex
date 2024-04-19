from site_main_code import *
from site_main_code.models import *


@app.context_processor
def inject_message():
    return dict(
        name_by_key=name_by_key(),
        get_test=get_test,
        get_all_tasks=get_all_tasks(),
        link_API=link_API,
        zip=zip,
    )


@app.route('/', methods=['POST', 'GET'])
@app.route('/home')
def home():
    return render_template("home.html", title='Home page')


@app.route('/user_page')
def user_page():
    return render_template('user_page.html')


@app.route('/answer', methods=["POST"])
def answer_test():
    return render_template("error.html")


@app.route('/login', methods=['POST', 'GET'])
# @cache.cached(timeout=300)
def login():
    if request.method == "POST":
        try:
            name = request.form["nickname"]
            password = request.form["password"]

            name, id = get_id_by_name(nickname=name, password=password)

            if id is not False:
                res = make_response(render_template("acept_login.html"))
                res.set_cookie('user_id', f'{id}', max_age=60 * 60 * 24 * 365 * 2)
                return res
        except Exception as ex:
            return render_template("error.html")

    else:
        return render_template("login.html")


@app.route('/logout')
# @cache.cached(timeout=300)
def logout():
    res = make_response(render_template('logout.html'))
    res.set_cookie('foo', request.cookies.get('foo'), max_age=0)
    return res


@app.route('/pass_sucses', methods=['POST'])
# @cache.cached(timeout=300)
def pass_sucses():
    if request.method == "POST":
        try:
            name = request.form["name"]
            password = request.form["password"]
            if (name in db) and (password in db):
                res = make_response(render_template("acept_entrense.html"))
                res.set_cookie('foo', f'{random.randint(1, 2)}', max_age=60 * 60 * 24 * 365 * 2)
                return res
            else:
                return render_template("error.html")
        except Exception as ex:
            return render_template("error.html")
    else:
        return render_template("home.html", title='Home page')


@app.route('/enter')
# @cache.cached(timeout=300)
def enter():
    return render_template("entry.html")


@app.route('/regester', methods=['POST'])
@app.route('/regester', methods=['GET'])
@cache.cached(timeout=300)
def regester():
    if request.method == 'GET':
        return render_template('regestor.html')
    if request.method == 'POST':
        try:
            name = request.form["nickname"]
            email = request.form["email"]
            password = request.form["password"]
        except:
            return redirect('/error')
        create_user(nickname=name, email=email, password=password)
        name, id = get_info_by_name(nickname=name, password=password)

        if id is not False:
            res = make_response(render_template("acept_login.html"))
            res.set_cookie('user_id', f'{id}', max_age=60 * 60 * 24 * 365 * 2)
            return res
        return redirect('/error')


@app.route('/about_us')
# @cache.cached(timeout=300)
def about_us():
    return render_template("about_us.html")


@app.route('/error')
# @cache.cached(timeout=300)
def error():
    return render_template('error.html')


@app.route('/test', methods=["POST"])
def test_te():
    name = request.form.get('name')
    word = request.form.get('word')
    return f"{name} + {word}"


@app.route('/tests/<id>', methods=['GET'])
def tests(id):
    if request.method == "GET":
        data = get_test(id)
        return render_template('tests.html', data=data)





@app.route('/check/<int:id>', methods=['POST'])
def check(id):
    if request.method == "POST":
        user_data = request.form.values()
        data = get_test(id)
        return render_template('tests.html', data=data, user_data=user_data)


@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Неверный запрос'}), 400


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({'error': 'Требуется аутентификация'}), 401


@app.errorhandler(403)
def forbidden(error):
    return jsonify({'error': 'Отказано в доступе'}), 403


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'error': 'Страница не найдена'}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'error': 'Метод не разрешен'}), 405


@app.errorhandler(408)
def request_timeout(error):
    return jsonify({'error': 'Таймаут запроса'}), 408


@app.errorhandler(409)
def conflict(error):
    return jsonify({'error': 'Конфликт'}), 409


@app.errorhandler(410)
def gone(error):
    return jsonify({'error': 'Ресурс удален'}), 410


@app.errorhandler(414)
def uri_too_long(error):
    return jsonify({'error': 'URI слишком длинный'}), 414


@app.errorhandler(415)
def unsupported_media_type(error):
    return jsonify({'error': 'Неподдерживаемый тип медиа'}), 415


@app.errorhandler(417)
def expectation_failed(error):
    return jsonify({'error': 'Ожидание не выполнено'}), 417


@app.errorhandler(418)
def im_a_teapot(error):
    return jsonify({'error': 'Я - чайник'}), 418


@app.errorhandler(422)
def unprocessable_entity(error):
    return jsonify({'error': 'Необрабатываемая сущность'}), 422


@app.errorhandler(429)
def too_many_requests(error):
    return jsonify({'error': 'Слишком много запросов. Попробуйте позже'}), 429


@app.errorhandler(451)
def unavailable_for_legal_reasons(error):
    return jsonify({'error': 'Недоступно по юридическим причинам'}), 451


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Внутренняя ошибка сервера'}), 500


@app.errorhandler(501)
def not_implemented(error):
    return jsonify({'error': 'Не реализовано'}), 501


@app.errorhandler(503)
def service_unavailable(error):
    return jsonify({'error': 'Сервис временно недоступен'}), 503


@app.errorhandler(504)
def gateway_timeout(error):
    return jsonify({'error': 'Время ожидания истекло'}), 504


@app.errorhandler(505)
def http_version_not_supported(error):
    return jsonify({'error': 'HTTP версия не поддерживается'}), 505
