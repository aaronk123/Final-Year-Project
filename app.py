from cgi import test
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def hello_world():

    return render_template("index.html")

@app.route("/application", methods=["POST", "GET"])
def login():

    if request.method == "POST":
        salary = request.form["salary"]
        age = request.form["age"]
        print(salary)
        print(age)
        return redirect("/results")

    else:
        return render_template("application.html")

@app.route("/results", methods=["GET"])
def results():

    return "<p>results page</p>"

if __name__ == "__main__":
    app.run(debug=True)
#https://python-adv-web-apps.readthedocs.io/en/latest/flask_forms.html#configure-the-form