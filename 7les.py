# from flask import Flask, url_for, redirect, session, request, flash, render_template
# from datetime import timedelta

# app = Flask(__name__)

# app.secret_key = "hello"
# app.permanent_session_lifetime = timedelta(minutes=10)


# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route("/login", methods=["POST", "GET"])
# def login():

#     if request.method == "POST":
#         user = request.form["nm"]
#         session.permanent = True
#         session["user"] = user

#         flash("You have been logged in", "info")

#         return redirect(url_for("user"))

#     else:

#         if "user" in session:

#             flash("You have been alredy logged in", "info")

#             return redirect(url_for("user"))

#         return render_template("login.html")
    

# @app.route("/user",methods=["POST","GET"])
# def user():
#     email=None
#     if "user" in session:
#         user = session["user"]

#         if request.method=="POST":
#             email=request.form["email"]
#             session["email"]=email
#             flash("email was saved")
#         else:
#             if "email" in session:
#                 email=session["email"]

#         return render_template("user2.html", email=email)
            

#     else:
#         flash("you are not logged in")
#         return redirect(url_for("login"))
    
# @app.route("/logout")
# def logout():

#     session.pop("user", None)
#     flash("You have been logged out", "info")
#     session.pop("email",None)

#     return redirect(url_for("login"))



# if __name__ == "__main__":

#     app.run(debug=True)


















from flask import Flask, url_for, redirect, session, request, flash, render_template
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=10)

app.config['SQLAlchemy_DATABASE_URI']='sqlite://users.sqlite3'
app.config['SQLAlchemy_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)


class users(db.Model):
    _id=db.Columns("id",db.Integers,primary_key=True)
    name=db.Columns(db.String(100))
    email=db.Columns(db.String(100))

    def __init__(self,name,email):
        self.name=name
        self.email=email
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():

    if request.method == "POST":
        user = request.form["nm"]
        session.permanent = True
        session["user"] = user

        flash("You have been logged in", "info")

        return redirect(url_for("user"))

    else:

        if "user" in session:

            flash("You have been alredy logged in", "info")

            return redirect(url_for("user"))

        return render_template("login.html")
    

@app.route("/user",methods=["POST","GET"])
def user():
    email=None
    if "user" in session:
        user = session["user"]

        if request.method=="POST":
            email=request.form["email"]
            session["email"]=email
            flash("email was saved")
        else:
            if "email" in session:
                email=session["email"]

        return render_template("user2.html", email=email)
            

    else:
        flash("you are not logged in")
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():

    session.pop("user", None)
    flash("You have been logged out", "info")
    session.pop("email",None)

    return redirect(url_for("login"))



if __name__ == "__main__":
    db.createall()
    app.run(debug=True)






# # Configure database location
# # SQLALCHEMY_DATABASE_URI tells Flask where the database is stored

# # sqlite:///users.sqlite3
# # sqlite   -> database type
# # ///      -> means database file is in current project folder
# # users.sqlite3 -> database file name

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'


# # Disable modification tracking
# # Flask-SQLAlchemy tracks every object change by default
# # That tracking uses extra memory
# # False improves performance and removes warning message

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# # Create SQLAlchemy object
# # This connects Flask app with SQLAlchemy
# # SQLAlchemy helps Python talk to database using Python code instead of raw SQL

# db = SQLAlchemy(app)


# # Create a table/model named "users"
# # db.Model means this class will become a database table

# class users(db.Model):


#     # Create ID column

#     # _id -> Python variable name
#     # "id" -> actual database column name

#     # db.Integer -> only integer values allowed

#     # primary_key=True means:
#     # - Every row must have unique ID
#     # - Cannot contain duplicate values
#     # - Used to identify each row uniquely

#     _id = db.Column("id", db.Integer, primary_key=True)


#     # Create name column

#     # db.String(100) means:
#     # Store text/string
#     # Maximum length = 100 characters

#     name = db.Column(db.String(100))


#     # Create email column

#     # Also stores string/text data
#     # Maximum length = 100 characters

#     email = db.Column(db.String(100))


#     # Constructor function
#     # Runs automatically whenever object is created

#     def __init__(self, name, email):


#         # Store passed name inside object

#         self.name = name


#         # Store passed email inside object

#         self.email = email