import requests
import json
from flask import Flask, render_template
from flask_session import Session
from tempfile import mkdtemp

# Configure flask application
app = Flask(__name__)

# GET request to API
response = requests.get("https://s3.amazonaws.com/open-to-cors/assignment.json")

responseString = response.text #string format
responseDict = json.loads(responseString) #convert to dict

#clean the dict
productsDict = responseDict["products"]

#sort the dict acc to int(popularity) in desc order
productsDictSorted = dict(sorted(productsDict.items(), key = lambda x : int(x[1]['popularity']), reverse = True))

#render template using flask and jinja2
@app.route("/")
def products():
  return render_template("index.html", productsDictSorted = productsDictSorted)


