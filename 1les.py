# Import Flask class and helper functions from flask package
from flask import Flask, redirect, url_for


# Create Flask application object
# __name__ tells Flask where current file is located
app = Flask(__name__)


# Route for homepage "/"
# When user opens localhost:5000/
# this function runs
@app.route("/")
def home():

    # Return simple text response
    return "vishal"


# Dynamic route
# <name> means take value from URL
# Example:
# localhost:5000/rahul
# name = "rahul"
@app.route("/<name>")
def user(name):

    # f-string used to insert variable inside string
    return f"hello {name}"


# Route for /admin
@app.route("/admin")
def admin():

    # redirect() sends user to another route/page

    # url_for("home")
    # finds URL of function named "home"

    # So user visiting /admin
    # gets redirected to homepage "/"
    return redirect(url_for("home"))


# This condition checks:
# Is this file being run directly?

# If YES:
# start Flask server
if __name__ == "__main__":

    # app.run() starts local development server

    # debug=True:
    # automatically reloads server on code changes
    # and shows detailed errors
    app.run(debug=True)




# Create Flask application

# Flask() creates the web application/server

# Think of it like:
# "Hey Flask, start my website"

# app is just a variable name
# storing the Flask application object

# __name__ means:
# "current file name"

# Flask uses __name__ to know:
# - where this file is located
# - where templates folder is
# - where static folder is

# Example:
# if file name is app.py
# then __name__ becomes "__main__"
# when directly running the file

# app = Flask(__name__)




# VERY EASY REAL-LIFE ANALOGY

# Imagine Flask asks:

# "Which file is creating this website?"

# You answer:

# __name__

# So Flask can find:

# HTML templates
# CSS files
# project folders

# correctly.

# SECOND LINE
# if __name__ == "__main__":

# This confuses almost EVERY beginner initially.

# SUPER EASY EXPLANATION

# Python checks:

# "Is this file being run directly?"

# If YES:

# app.run()

# will execute.

# Example

# Suppose file name is:

# app.py

# You run:

# python app.py

# Then:

# __name__

# automatically becomes:

# "__main__"

# So condition becomes:

# if "__main__" == "__main__":

# TRUE ✅

# Therefore:

# app.run()

# starts Flask server.

# Why This Is Useful?

# Sometimes another file imports this file.

# Example:

# import app

# Now:

# __name__

# is NOT "__main__" anymore.

# So:

# app.run()

# does NOT start automatically.

# This prevents problems.