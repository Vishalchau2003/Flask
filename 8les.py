# Import Flask class and useful functions from flask package

# Flask -> used to create Flask application
# url_for -> generates URL dynamically
# redirect -> redirects user to another route/page
# session -> stores user data temporarily
# request -> gets form data from user/browser
# flash -> shows temporary popup/messages
# render_template -> renders HTML files

from flask import Flask, url_for, redirect, session, request, flash, render_template


# Import timedelta
# Used for setting session expiration time

from datetime import timedelta


# Import SQLAlchemy
# SQLAlchemy is ORM (Object Relational Mapper)

# It lets us use Python code instead of writing SQL queries manually

from flask_sqlalchemy import SQLAlchemy


# Create Flask app object

app = Flask(__name__)


# Secret key used for session security

app.secret_key = "hello"


# Session lifetime
# User stays logged in for 10 minutes

app.permanent_session_lifetime = timedelta(minutes=10)


# Configure database location

# sqlite:///users.sqlite3

# sqlite -> database type
# /// -> database file is in current project folder
# users.sqlite3 -> database filename

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'


# Disable modification tracking
# Saves memory and removes warning

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Connect SQLAlchemy with Flask app

db = SQLAlchemy(app)


# Create database table/model

class users(db.Model):


    # Create ID column

    # "id" -> actual database column name

    # db.Integer -> integer datatype

    # primary_key=True ->
    # Every row gets unique ID

    _id = db.Column("id", db.Integer, primary_key=True)


    # Create name column

    # db.String(100)
    # Stores text up to 100 characters

    name = db.Column(db.String(100))


    # Create email column

    email = db.Column(db.String(100))


    # Constructor function

    # Runs automatically when object is created

    def __init__(self, name, email):


        # Store name inside object

        self.name = name


        # Store email inside object

        self.email = email


# Home route

@app.route("/")


# Function runs when user visits "/"

def home():


    # Render index.html page

    return render_template("index.html")


# Login route

# methods=["POST","GET"]

# GET -> open page
# POST -> submit form data

@app.route("/login", methods=["POST", "GET"])

def login():


    # Check if form submitted

    if request.method == "POST":


        # Get data from textbox having name="nm"

        user = request.form["nm"]


        # Make session permanent

        session.permanent = True


        # Store username inside session

        session["user"] = user


        # Search database for user

        # filter_by(name=user)
        # means WHERE name = user

        # first()
        # gets first matching row

        found_user = users.query.filter_by(name=user).first()


        # If user already exists

        if found_user:


            # Store email in session

            session["email"] = found_user.email


        # If user does not exist

        else:


            # Create new user object

            usr = users(user, "")


            # Add user into database

            db.session.add(usr)


            # Save changes permanently

            db.session.commit()


        # Show flash message

        flash("You have been logged in", "info")


        # Redirect to /user page

        return redirect(url_for("user"))


    # If request method is GET

    else:


        # Check if already logged in

        if "user" in session:


            # Show message

            flash("You have been alredy logged in", "info")


            # Redirect to user page

            return redirect(url_for("user"))


        # Open login page

        return render_template("login.html")


# User route

@app.route("/user", methods=["POST", "GET"])

def user():


    # Initially email is empty

    email = None


    # Check if user logged in

    if "user" in session:


        # Get username from session

        user = session["user"]


        # If form submitted

        if request.method == "POST":


            # Get email entered in form

            email = request.form["email"]


            # Store email inside session

            session["email"] = email


            # Find current user in database

            found_user = users.query.filter_by(name=user).first()


            # Update email in database

            found_user.email = email


            # Save updated changes

            db.session.commit()


            # Show flash message

            flash("email was saved")


        # If request method is GET

        else:


            # Check if email exists in session

            if "email" in session:


                # Get email from session

                email = session["email"]


        # Open user2.html page

        # Send email variable to HTML

        return render_template("user2.html", email=email)


    # If user not logged in

    else:


        # Show message

        flash("you are not logged in")


        # Redirect to login page

        return redirect(url_for("login"))


# View route

@app.route("/view")

def view():


    # users.query.all()

    # Get ALL rows from database

    # Send all data to view.html

    return render_template("view.html", values=users.query.all())


# Logout route

@app.route("/logout")

def logout():


    # Remove user from session

    session.pop("user", None)


    # Remove email from session

    session.pop("email", None)


    # Show logout message

    flash("You have been logged out", "info")


    # Redirect to login page

    return redirect(url_for("login"))


# Run application

if __name__ == "__main__":


    # Create database tables

    # Runs only if tables don't exist

    with app.app_context():

        db.create_all()


    # Start Flask server

    app.run(debug=True)