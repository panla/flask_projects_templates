from common.redis_tools import RedisClient


def init_redis(app):
    """集成Redis"""

    try:
        app.redis = RedisClient(
            app.config['REDIS_HOST'], app.config['REDIS_PORT'], app.config['REDIS_DB'],
            app.config['REDIS_PWD'], app.config.get('REDIS_EXPIRE')
            )
    except Exception as exc:
        current_app.logger.error(exc)
