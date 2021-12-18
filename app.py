import requests
import json
from flask import Flask, render_template, session, request, flash, redirect
from flask_session import Session
from helpers import login_required
from tempfile import mkdtemp
import random
import string

from helpers import login_required

# Configure flask application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def gen_id():
    code = ''.join(random.choices(string.digits, k = 5))    
    return code

# Login User
@app.route("/login", methods=["GET", "POST"])
def login():
  # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
      if request.form.get("password") != "SmartServTest@123":
        flash("Incorrect password.", category="message")
        return redirect("/login")
      else:
        # Remember which user has logged in
        uniqueSessionId = gen_id()
        session["user_id"] = uniqueSessionId

        flash("Log In successful.", category="message")
        # Redirect user to home page
        return redirect("/")

    else:
      return render_template("login.html")

# main page
@app.route("/")
@login_required
def products():
  # GET request to API
  response = requests.get("https://s3.amazonaws.com/open-to-cors/assignment.json")

  responseString = response.text #string format
  responseDict = json.loads(responseString) #convert to dict

  #clean the dict
  productsDict = responseDict["products"]

  #sort the dict acc to int(popularity) in desc order
  productsDictSorted = dict(sorted(productsDict.items(), key = lambda x : int(x[1]['popularity']), reverse = True))
  
  return render_template("index.html", productsDictSorted = productsDictSorted)

# log user out
@app.route("/logout")
@login_required
def logout():
  # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


if __name__ == "__main__":
    app.run()