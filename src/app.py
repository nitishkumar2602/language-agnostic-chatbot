from flask import Flask

app = Flask(__name__)
VERSION = "1.0.0"

from .routes import *  # noqa: E402, F401
