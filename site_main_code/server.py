import random

from site_main_code import *
from site_main_code.models import *


@app.context_processor
def inject_message():
    return dict(name_by_key=name_by_key())


@app.route('/', methods=['POST', 'GET'])
@app.route('/home')
@app.route('/home_page')
@app.route('/main_page')
def home():
    if request.method == "POST":
        return render_template("home.html", title='Home page')
    else:
        return render_template("home.html", title='Home page')

@app.route('/user_page')
def user_page():
    return render_template('user_page.html')


@app.route('/answer', methods=["POST"])
def answer_test():
    return render_template("error.html")

@app.route('/logout')
def logout():
    res = make_response(render_template('logout.html'))
    res.set_cookie('foo', request.cookies.get('foo'), max_age=0)
    return res

@app.route('/pass_sucses',methods=['POST'])
def pass_sucses():
    if request.method == "POST":
        db = ['ggg']
        try:
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]
            if (name is not None) and (email is not None) and (password is not None):
                return render_template("acept_entrense.html")

        except KeyError:
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
        except Exception as ex:
            return render_template("error.html")
    else:
        return render_template("home.html", title='Home page')


@app.route('/enter')
def enter():
    return render_template("entry.html")


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
