from flask import request, render_template

from site_main_code import app


@app.route('/', methods=['POST', 'GET'])
@app.route('/home')
@app.route('/home_page')
@app.route('/main_page')
def home():
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]
            print(name, email, password)
            return render_template("home.html")
        except KeyError:
            try:
                name = request.form["name"]
                password = request.form["password"]
                print(name, password)
                return render_template("home.html")
            except Exception as ex:
                return render_template("error.html")
        except Exception as ex:
            return render_template("error.html")
    else:
        return render_template("home.html", title="Дом милый дом")


@app.route('/tests/<num>')
def tests(num):
    return render_template("super_tesks.html", lst=open(f"{num}").readlines())


@app.route('/answer', methods=["POST"])
def answer_test():
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]
            print(name, email, password)
            return render_template("home.html")
        except KeyError:
            try:
                name = request.form["name"]
                password = request.form["password"]
                print(name, password)
                return render_template("home.html")
            except Exception as ex:
                return render_template("error.html")
        except Exception as ex:
            return render_template("error.html")
    else:
        return render_template("home.html", title="Дом милый дом")


@app.route('/enter')
def enter():
    return render_template("entry.html")


@app.route('/test', methods=["POST"])
def test_te():
    name = request.form.get('name')
    word = request.form.get('word')
    return f"{name} + {word}"
@app.route('/regester')
def regester():
    return render_template('regestor.html')


@app.route('/about_us')
def about_us():
    return render_template("about_us.html")


@app.route('/error')
def error():
    return render_template('error.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
