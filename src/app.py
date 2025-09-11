from flask import Flask
from rich.logging import RichHandler

app = Flask(__name__)
app.logger.handlers = [RichHandler()]

with open("version.txt") as version_file:
    version_txt = version_file.read().strip().splitlines()

VERSION = "-".join(version_txt)

from .routes import *  # noqa: E402, F403
from .routes import api_router  # noqa: E402

app.register_blueprint(api_router)
