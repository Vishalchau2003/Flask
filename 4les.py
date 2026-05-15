# Import required things from Flask

from flask import Flask, redirect, url_for, render_template, request

# Flask       -> Main Flask class used to create the web app
# redirect    -> Used to move user to another route/page
# url_for     -> Generates URL for a function name
# render_template -> Used to open HTML files from templates folder
# request     -> Used to get data sent from browser/forms



# Create Flask application object
app = Flask(__name__)

# __name__ tells Flask where this file is located
# Flask uses it to find templates, static files etc.



# Route for homepage "/"
@app.route("/")

# Function that runs when user opens homepage
def home():

    # Opens index.html file from templates folder
    return render_template("index.html")



# Route for "/login"
# methods=["POST", "GET"] means this route accepts both GET and POST requests

@app.route("/login", methods=["POST", "GET"])

def login():

    # Check if form data was submitted using POST method
    if request.method == "POST":

        # Get data from form input whose name="nm"
        # Example:
        # <input type="text" name="nm">

        user = request.form["nm"]

        # Redirect user to user page
        # url_for("user", usr=user)
        # creates URL like:
        # /Vishal

        return redirect(url_for("user", usr=user))

    else:

        # If method is GET
        # show login.html page

        return render_template("login.html")



# Dynamic route
# Whatever comes after "/" becomes value of usr

@app.route("/<usr>")

def user(usr):

    # Display username inside h1 heading

    return f"<h1>{usr}</h1>"



# This condition checks:
# "Is this file being run directly?"

if __name__ == "__main__":

    # Start Flask server

    # debug=True means:
    # 1. Auto reload when code changes
    # 2. Shows detailed error messages

    app.run(debug=True)