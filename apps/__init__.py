from flask import Flask

from lib.init_app import init_app
from lib.init_logger import set_logger_handle
from lib.init_extension import init_extension
from lib.init_redis import init_redis
from apps.models import *


def create_app(config_file):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    init_app(app)
    set_logger_handle(app)

    init_extension(app)
    init_redis(app)

    return app
