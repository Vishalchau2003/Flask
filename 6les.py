# Import required Flask modules/functions
from flask import Flask, url_for, redirect, session, request, flash, render_template

# Import timedelta to set session expiry time
from datetime import timedelta


# Create Flask application object
app = Flask(__name__)


# Secret key is required for sessions and flash messages
# Flask uses it to securely sign session cookies
app.secret_key = "hello"


# Set session lifetime to 10 minutes
# After 10 minutes session expires automatically
app.permanent_session_lifetime = timedelta(minutes=10)



# Route for home page
@app.route("/")

# Function that runs when user visits "/"
def home():

    # Render index.html page
    return render_template("index.html")



# Route for login page
# methods=["POST","GET"] allows both:
# GET -> open page
# POST -> submit form data
@app.route("/login", methods=["POST", "GET"])

# Login function
def login():

    # Check if form was submitted
    if request.method == "POST":

        # Get value entered in textbox having name="nm"
        user = request.form["nm"]

        # Make session permanent
        # So it follows permanent_session_lifetime
        session.permanent = True

        # Store username inside session
        # Data remains available between pages
        session["user"] = user

        # Create flash message
        # "info" is category/type of message
        flash("You have been logged in", "info")

        # Redirect user to /user route
        return redirect(url_for("user"))

    else:

        # Check if user already logged in
        if "user" in session:

            # Show flash message
            flash("You have been alredy logged in", "info")

            # Redirect to user page
            return redirect(url_for("user"))

        # If not logged in, open login page
        return render_template("login.html")



# Route for logout
@app.route("/logout")

# Logout function
def logout():

    # Remove "user" from session
    # None prevents error if key doesn't exist
    session.pop("user", None)

    # Flash logout message
    flash("You have been logged out", "info")

    # Redirect to login page
    return redirect(url_for("login"))



# Route for user page
@app.route("/user")

# User function
def user():

    # Check if user exists in session
    if "user" in session:

        # Get username from session
        user = session["user"]

        # Open user.html
        # Send variable usr=user to HTML
        return render_template("user.html", usr=user)

    else:

        # If user not logged in
        flash("you are not logged in")

        # Redirect to login page
        return redirect(url_for("login"))



# Runs app only when this file is executed directly
if __name__ == "__main__":

    # Start Flask server in debug mode
    # debug=True auto reloads app after code changes
    app.run(debug=True)





#     After flash() you usually:

# redirect/render a page
# that page must contain get_flashed_messages()
# Example
# app.py
# flash("Login Successful!")
# return redirect(url_for("user"))

# This means:

# message stored temporarily
# next page will be /user

# So:

# user.html
# OR
# base.html

# must contain:

# {% with messages = get_flashed_messages() %}

# otherwise message will never appear.

# Flow
# flash()
#    ↓
# message stored in session temporarily
#    ↓
# redirect/render next page
#    ↓
# next page reads message
#    ↓
# message displayed
#    ↓
# message deleted automatically