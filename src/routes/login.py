from ..app import app
from flask import render_template

@app.route("/login", methods=["GET"])
@app.route("/register", methods=["GET"])
def login():
    return render_template("login-register.jinja")


@app.route("/login", methods=["POST"])
def login_post():
    return "Login POST endpoint"


@app.route("/register", methods=["POST"])
def register_post():
    return "Register POST endpoint"