from site_main_code import *
from site_main_code.models import *


@app.context_processor
def inject_message():
    return dict(name_by_key=name_by_key())

@app.context_processor
def inject_message():
    return dict(name=name_and_password())


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template("home.html")


@app.route('/user_page')
def user_page():
    return render_template('user_page.html')


@app.route('/answer', methods=["POST"])
def answer_test():
    return render_template("error.html")


@app.route('/logout')
def logout():
    res = make_response(render_template('logout.html'))
    res.set_cookie('user_id', request.cookies.get('user_id'), max_age=0)
    return res


@app.route('/authorise', methods=['POST'])
def autorise():
    if request.method == "POST":
        try:
            email = request.form["email"]
            print(email)
            name = request.form["nickname"]
            print(name)
            password = request.form["password"]
            print(password)
            res = make_response(render_template("acept_login.html"))
            res.set_cookie('user_id', f'{get_info_by_email(email=email, nickname=name, password=password)}',
                           max_age=60 * 60 * 24 * 365 * 2)
            return res
        except Exception as ex:
            print(ex)
            return render_template("error.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        try:

            name = request.form["nickname"]
            password = request.form["password"]

            name, id = get_info_by_name(nickname=name, password=password)

            if id is not False:
                res = make_response(render_template("acept_login.html"))
                res.set_cookie('user_id', f'{id}', max_age=60 * 60 * 24 * 365 * 2)
                return res
        except Exception as ex:
            return render_template("error.html")

    else:
        return render_template("login.html")


@app.route('/regester')
def regester():
    return render_template('regestor.html')


@app.route('/about_us')
def about_us():
    return render_template("about_us.html")


@app.route('/error')
def error():
    return render_template('error.html')


@app.route('/test', methods=["POST"])
def test_te():
    name = request.form.get('name')
    word = request.form.get('word')
    return f"{name} + {word}"


@app.route('/tests/<num>')
def tests(num):
    return render_template("super_tesks.html", lst=open(f"{num}").readlines())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
