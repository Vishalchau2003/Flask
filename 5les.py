# Import required Flask modules
# Flask -> creates the web app
# redirect -> redirects user to another route
# url_for -> generates URL of a route
# render_template -> loads HTML files
# request -> handles form data and requests
# session -> stores user data temporarily
from flask import Flask, redirect, url_for, render_template, request, session

# Import timedelta to set session expiry time
from datetime import timedelta


# Create Flask application
app = Flask(__name__)


# Secret key is required for sessions
# Flask uses this key to encrypt/sign session data
app.secret_key = "vis"


# Set session lifetime to 5 days
# After 5 days session expires automatically
app.permanent_session_lifetime = timedelta(days=5)


# Route for home page
@app.route("/")
def home():

    # Load index.html page
    return render_template("index.html")


# Route for login page
# Supports both GET and POST methods
@app.route("/login", methods=["POST", "GET"])
def login():

    # Check if form is submitted
    if request.method == "POST":

        # Get value from input field whose name="nm"
        user = request.form["nm"]

        # Store username in session
        # Session acts like temporary storage
        session["user"] = user

        # Redirect user to /user route
        return redirect(url_for("user"))

    else:

        # If user already exists in session
        # directly redirect to user page
        if "user" in session:

            return redirect(url_for("user"))

        # Otherwise open login page
        return render_template("login.html")


# Route for user page
@app.route("/user")
def user():

    # Check if user exists in session
    if "user" in session:

        # Retrieve username from session
        user = session["user"]

        # Display username on browser
        return f"<h1>{user}</h1>"

    else:

        # If user not logged in
        # redirect to login page
        return redirect(url_for("login"))


# Route for logout
@app.route("/logout")
def logout():

    # Remove user from session
    # None prevents error if user key doesn't exist
    session.pop("user", None)

    # Redirect user back to login page
    return redirect(url_for("login"))


# Run Flask application
if __name__ == "__main__":

    # debug=True automatically reloads server
    # and shows detailed errors
    app.run(debug=True)
