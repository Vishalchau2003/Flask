# # Import Flask class to create the web application
# # Import redirect to move user from one route/page to another
# # Import url_for to generate URL of a function(route)
# from flask import Flask, redirect, url_for


# # Create a Flask application object
# # __name__ tells Flask where this file is located
# app = Flask(__name__)


# # @app.route("/") means:
# # When user opens the main/home URL -> "/"
# # this function will run
# @app.route("/")

# # Function for home page
# def home():

#     # Whatever we return will be shown in browser
#     return "Hello from hell"


# # Dynamic route
# # <name> means Flask will take value from URL
# # Example:
# # /vishal
# # /rahul
# # /anything
# @app.route("/<name>")

# # Function receives that value as parameter
# def user(name):

#     # f-string used to insert variable inside string
#     # If URL is /vishal
#     # Output -> hello vishal
#     return f"hello {name}"


# # Route for admin page
# @app.route("/admin")

# # Function for admin route
# def admin():

#     # redirect() sends user to another route/page

#     # url_for("user", name="vishal")
#     # creates URL for user() function

#     # It becomes:
#     # /vishal

#     # So opening /admin redirects to /vishal
#     return redirect(url_for("user", name="vishal"))


# # This condition checks:
# # Is this file being run directly?

# # If yes -> run Flask server
# # If imported into another file -> don't run server
# if __name__ == "__main__":

#     # Starts Flask development server
#     app.run()















# # Import Flask class to create the web application
# # Import render_template to display HTML files
# from flask import Flask, render_template


# # Create Flask application object
# # __name__ helps Flask know the location of current file
# app = Flask(__name__)


# # Route for home page "/"
# # When user opens localhost:5000/
# # this function will execute
# @app.route("/")

# # Function for home page
# def home():

#     # render_template() is used to open an HTML file

#     # "index.html"
#     # Flask will search this file inside a folder named "templates"

#     # content="Vishi"
#     # Sending variable named 'content' to HTML

#     # r="vishie"
#     # Sending another variable named 'r' to HTML

#     # These values can be used inside HTML like:
#     # {{ content }}
#     # {{ r }}

#     return render_template(
#         "index.html",
#         content="Vishi",
#         r="vishie"
#     )


# # Checks whether this file is run directly
# # If true, Flask server starts
# if __name__ == "__main__":

#     # Start Flask development server
#     app.run()













# from flask import Flask,render_template
# app=Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# if __name__=="__main__":
#     app.run() 










from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",content=["vishie","vishi","shibal"])

if __name__=="__main__":
    app.run() 