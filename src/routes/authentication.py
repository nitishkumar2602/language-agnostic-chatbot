from flask import render_template

from ..app import app

__all__ = ("register", "login", "login_post", "register_post")


@app.get("/login-register/")
def register():
    return render_template("login-register.jinja", active_tab="register")


@app.get("/login-register/")
def login():
    return render_template("login-register.jinja", active_tab="login")


@app.post("/authentication-login/")
def login_post():
    return "Login POST endpoint"


@app.post("/authentication-register/")
def register_post():
    return "Register POST endpoint"
