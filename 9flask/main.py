
from flask import Flask, render_template, url_for


# Import the blueprint object named 'second'
# from the file second.py inside admin folder
from admin.second import second

app = Flask(__name__)


# Register the blueprint with the main Flask app
# url_prefix="" means:
# no prefix will be added before blueprint routes
# Example:
# @second.route("/home")
# becomes simply:
# /home
app.register_blueprint(second, url_prefix="")

@app.route("/")
def test():

    return "<h1>Test</h1>"


if __name__ == "__main__":

   
    app.run(debug=True)










# You are basically learning how Flask projects become modular using Blueprints and how Python imports work.

# Right now your project changed from:

# single file flask app

# to:

# multi-file structured flask app

# Let's understand EVERYTHING step by step.

# 1. Earlier Simple Flask App

# Initially you probably had:

# main.py
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Home"

# if __name__ == "__main__":
#     app.run(debug=True)

# Everything was inside ONE file.

# This works for small projects only.

# 2. Problem With Big Projects

# Suppose project becomes large:

# You may have:

# admin panel
# user panel
# authentication
# dashboard
# APIs

# If all routes stay in one file:

# main.py = 5000 lines 😭

# Very messy.

# So Flask provides:

# BLUEPRINTS
# 3. What Is Blueprint?

# Blueprint means:

# A separate section/module of your app

# Example:

# admin routes
# user routes
# auth routes

# Each can live in separate files.

# 4. Your Structure Now

# You created:

# 9flask/
# │
# ├── main.py
# │
# ├── admin/
# │   ├── __init__.py
# │   ├── second.py
# │   ├── templates/
# │   │    ├── home.html
# │   │    └── base.html
# │   └── static/

# This is now modular Flask architecture.

# 5. What main.py Does
# main.py
# from flask import Flask
# from admin.second import second

# app = Flask(__name__)

# app.register_blueprint(second, url_prefix="/admin")

# This file:

# creates Flask app
# imports blueprint
# attaches blueprint to app
# 6. Understanding This Import
# from admin.second import second

# Means:

# STEP 1

# Go inside folder:

# admin
# STEP 2

# Find file:

# second.py
# STEP 3

# Import variable:

# second

# from that file.

# 7. Why __init__.py Needed

# You created:

# admin/__init__.py

# This tells Python:

# "admin is a package/folder that can be imported"

# Without this:

# from admin.second import second

# fails.

# 8. What Happens Inside second.py
# second.py
# second = Blueprint(
#     "second",
#     __name__,
#     static_folder="static",
#     template_folder="templates"
# )

# This creates a blueprint object.

# Think:

# Blueprint = mini flask app
# 9. Routes Inside Blueprint
# @second.route("/")
# def home():

# NOT:

# @app.route("/")

# because routes belong to blueprint now.

# 10. Blueprint Registration

# This line:

# app.register_blueprint(second, url_prefix="/admin")

# means:

# Attach all blueprint routes under /admin
# 11. URL Formation

# Inside blueprint:

# @second.route("/")

# Combined with:

# url_prefix="/admin"

# becomes:

# /admin/

# Another:

# @second.route("/home")

# becomes:

# /admin/home
# 12. Why Template Error Happened

# You wrote:

# template_folder="template"

# But actual folder was:

# templates

# Flask searched:

# admin/template/home.html

# which does not exist.

# After fixing:

# template_folder="templates"

# Flask searches correctly:

# admin/templates/home.html
# 13. How Flask Finds Templates

# This line:

# render_template("home.html")

# means:

# Find home.html inside template folder

# Since blueprint has:

# template_folder="templates"

# Flask checks:

# admin/templates/home.html
# 14. Why Static Folder Mentioned
# static_folder="static"

# means:

# CSS/images/js are inside admin/static
# 15. Whole Flow

# When browser opens:

# http://127.0.0.1:5000/admin/home

# Flow becomes:

# STEP 1

# Flask app receives request.

# STEP 2

# Sees:

# /admin

# belongs to blueprint.

# STEP 3

# Blueprint checks:

# @second.route("/home")

# matched.

# STEP 4

# Runs:

# home()
# STEP 5

# Calls:

# render_template("home.html")
# STEP 6

# Flask searches:

# admin/templates/home.html
# STEP 7

# HTML sent to browser.

# 16. Why This Structure Is Powerful

# Now you can create:

# admin/
# user/
# auth/
# api/
# dashboard/

# Each with:

# own routes
# own templates
# own static files

# Very scalable.

# 17. Big Companies Use Similar Structure

# Projects in:

# Instagram
# Netflix
# Spotify

# also split apps/modules similarly.

# Not same Flask structure necessarily, but same concept:

# modular architecture