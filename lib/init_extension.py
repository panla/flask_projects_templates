from flask import current_app
from flask_migrate import Migrate

from common.redis_client import RedisClient
from apps.db import db


def init_db(app):
    db.init_app(app)


def init_migrate(app):
    migrate = Migrate()
    migrate.init_app(db=db, app=app)


def init_redis(app):
    """集成Redis"""

    try:
        redis = RedisClient(
            app.config['REDIS_HOST'], app.config['REDIS_PORT'], app.config['REDIS_DB'],
            app.config['REDIS_PWD'], app.config.get('REDIS_EXPIRE')
            )
        redis.init_app(app)
    except Exception as exc:
        current_app.logger.error(exc)
