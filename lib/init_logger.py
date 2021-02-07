import os
import logging
import traceback
from logging.handlers import TimedRotatingFileHandler

from flask import current_app
from flask import request
from werkzeug.exceptions import HTTPException

from lib.tools import responses


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


def process_exception(error):
    """全局异常处理"""

    current_app.logger.error('start error'.center(40, '*'))
    current_app.logger.error(f'{request.method}, {request.path}'.center(60, '*'))
    if isinstance(error, HTTPException):
        current_app.logger.error('error is {} {} end.'.format(error.code, error.description))
        current_app.logger.error(traceback.format_exc())
        current_app.logger.error('end error'.center(40, '*'))
        return responses(status_code=error.code, code=10200, message=error.description)
    current_app.logger.error('error is {} end.'.format(error))
    current_app.logger.error('end error'.center(40, '*'))
    return responses(status_code=400, code=10200, message=f'{error}')
