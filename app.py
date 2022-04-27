from cgi import test
from flask import Flask, render_template, request, redirect
import scrapers.daft_scraper as daft_scraper
import scrapers.pricePropertyRegister as ppr_scraper
import matcher as matcher
import time
import threading
import os

# def test_task():
#     while True:
#         print('daemon running')
#         # sleep for 1 day
#         time.sleep(24*60)
#         print('daemon finished sleeping')
#         # scrape_data()
        
# def scrape_data():
#     # daft_scraper()
#     # ppr_scraper()
#     print('scraping')
    
app = Flask(__name__)

@app.route("/")
def index():
    # thread = threading.Thread(target=test_task)
    # thread.daemon = True         # Daemonize 
    # thread.start()
    return render_template("index.html")

@app.route("/application", methods=["POST", "GET"])
def application():
    try:
        os.remove("templates/property_map.html")
    except Exception:
        pass

    if request.method == "POST":

        budget = request.form["budget"]   
        rooms= request.form["rooms"]
        bathrooms=request.form["bathrooms"]
        county=request.form["county_dropdown"]
        stakeholder=request.form["stakeholder_group"]

        matcher.match_data(budget, rooms, bathrooms, county, stakeholder)

        return redirect("/results")
        # return render_template("property_map.html")
    else:
        return render_template("application.html")

@app.route("/results", methods=["GET"])
def results():

    return render_template("property_map.html")

if __name__ == "__main__":
    app.run(debug=True)

