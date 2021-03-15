import os
import logging
from logging.handlers import TimedRotatingFileHandler


def set_logger_handle(app):
    """配置 logger handle"""

    log_level = app.config.get('LOG_LEVEL').upper() or 'DEBUG'

    logfile_path = app.config.get('LOG_PATH')
    os.makedirs(os.path.dirname(logfile_path), exist_ok=True)

    file_handler = TimedRotatingFileHandler(logfile_path, 'midnight')
    file_handler.setLevel(level=log_level)
    file_handler.setFormatter(
        logging.Formatter('[%(asctime)s>] [%(levelname)s] <-%(filename)s-line %(lineno)d>  %(message)s')
    )
    app.logger.addHandler(file_handler)
    app.logger.setLevel(level=log_level)
