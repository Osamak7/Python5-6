from flask import Flask
from markupsafe import escape

app= Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> hello , world! </p>"

@app.route("/hello")
def hello2():
    return "<p> Hello , how are you ? </p>"

@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {escape(username)}" # escape viene utilizzato per evitare che nella route ci siano attacchi malevoli scritti(XSS)