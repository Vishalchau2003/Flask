from flask import Flask,render_template,url_for

app=Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

if __name__=="__main__":
    app.run(debug=True)



# The static folder in Flask is used to store files that do NOT change dynamically.

# These are called static files.

# Examples of Static Files
# File Type	Example
# CSS	style.css
# Images	logo.png, image.jpg
# JavaScript	script.js
# Videos	video.mp4
# Fonts	.ttf, .woff



# Why NOT Put CSS Inside templates?

# Because:

# templates/

# is only for HTML/Jinja files.

# Flask renders templates dynamically.

# But CSS/images are not rendered dynamically.

# They are directly served to browser.

# So Flask separates them.