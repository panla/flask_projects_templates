from apps.lib.init_cross import init_cross
from apps.lib.init_logger import set_logger_handle
from apps.lib.init_exception import process_exception
from apps.lib.init_extension import init_db
from apps.lib.init_extension import init_migrate
from apps.lib.init_extension import init_redis
from apps.lib.init_blueprints import register_blueprints


def init_app(app):
    set_logger_handle(app)
    init_cross(app)
    init_db(app)
    init_migrate(app)
    init_redis(app)
    register_blueprints(app)
    app.register_error_handler(Exception, process_exception)
    return app
