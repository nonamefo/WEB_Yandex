from flask import render_template, Flask, request

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/', methods=['POST'])
def login():
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
            return render_template("error_text.html")


@app.route('/enter')
def enter():
    return render_template("entry.html")


@app.route('/regester')
def regester():
    return render_template('regestor.html')


if __name__ == '__main__':
    app.run(debug=True)
