from cgi import test
from flask import Flask, render_template, request, redirect
import main as test_script

app = Flask(__name__)

@app.route("/")
def hello_world():
    #test_script.hello()
    #test_script.daft_scraper()
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


#https://python-adv-web-apps.readthedocs.io/en/latest/flask_forms.html#configure-the-form