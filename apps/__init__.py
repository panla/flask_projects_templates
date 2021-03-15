from flask import Flask

from apps.lib.init_app import init_app
from apps.models import *


def create_app(config_file):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    app = init_app(app)

    return app
