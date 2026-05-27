# Import Blueprint and render_template from Flask
#
# Blueprint:
# Used to create a separate module/section of the Flask app
#
# render_template:
# Used to render HTML files
from flask import Blueprint, render_template


# Create a Blueprint object
#
# "second"
# -> name of blueprint
#
# __name__
# -> tells Flask the current file location
#
# static_folder="static"
# -> Flask will look for CSS/images/js inside:
#    admin/static
#
# template_folder="templates"
# -> Flask will look for HTML files inside:
#    admin/templates
second = Blueprint(
    "second",
    __name__,
    static_folder="static",
    template_folder="templates"
)


# If user opens:
# http://127.0.0.1:5000/home
#
# then home() function will run
@second.route("/home")


# Create another route:
# /
#
# If user opens:
# http://127.0.0.1:5000/
#
# then same home() function will run
#
# Multiple routes can point to same function
@second.route("/")


# Function that handles both routes
def home():

    # Render home.html file
    #
    # Flask searches:
    # templates/home.html
    #
    # and sends HTML page to browser
    return render_template("home.html")


# Create route:
# /test
#
# If user opens:
# http://127.0.0.1:5000/test
#
# this function runs
@second.route("/test")


# Function for /test route
def test():

    # Return simple HTML heading
    return "<h1>test</h1>"














# You typed:
# /admin

# Flask looks for:

# /admin/

# which exists from:

# @second.route("/")
# To open /home

# You must type:

# /admin/home

# because Flask created:

# /admin + /home

# ↓

# /admin/home
# Easy Visual
# Blueprint
# url_prefix="/admin"

# adds:

# /admin

# before EVERY route.

# Route 1
# @second.route("/")

# becomes:

# /admin/
# Route 2
# @second.route("/home")

# becomes:

# /admin/home
# Important Thing

# "/" inside blueprint means:

# default/home route of blueprint