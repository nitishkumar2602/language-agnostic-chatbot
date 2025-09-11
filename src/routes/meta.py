from ..app import app
from ..app import VERSION
from flask import jsonify, render_template

@app.get("/")
def read_root():
    return render_template("home.jinja")