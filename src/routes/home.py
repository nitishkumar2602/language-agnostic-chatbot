from flask import render_template

from ..app import app

__all__ = ("index",)


@app.get("/")
@app.get("/home/")
@app.get("/index/")
def index():
    return render_template("index.jinja")
