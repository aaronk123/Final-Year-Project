from cgi import test
from flask import Flask, render_template, request, redirect
import scrapers.daft_scraper as daft_scraper
import scrapers.pricePropertyRegister as ppr_scraper
import time
import threading

def test_task():
    while True:
        print('daemon running')
        #sleep for 1 day
        # time.sleep(24*60)
        # print('daemon finished sleeping')
        # scrape_data()
        
def scrape_data():
    daft_scraper()
    ppr_scraper()

app = Flask(__name__)

@app.route("/")
def hello_world():
    thread = threading.Thread(target=test_task)
    thread.daemon = True         # Daemonize 
    thread.start()
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
    app.run(debug=True, threaded=True)

#https://python-adv-web-apps.readthedocs.io/en/latest/flask_forms.html#configure-the-form