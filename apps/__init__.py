from flask import Flask

from lib.init_cross import init_cross
from lib.init_logger import set_logger_handle
from lib.init_exception import process_exception
from lib.init_extension import init_db
from lib.init_extension import init_migrate
from lib.init_extension import init_redis
from lib.init_blueprints import register_blueprints
from apps.models import *


def create_app(config_file):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    set_logger_handle(app)
    init_cross(app)
    init_db(app)
    init_migrate(app)
    init_redis(app)
    register_blueprints(app)

    app.register_error_handler(Exception, process_exception)

    return app
