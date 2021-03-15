import traceback

from flask import current_app
from flask import request
from werkzeug.exceptions import HTTPException

from apps.lib.tools import responses
from apps.lib.code_define import Code


def process_exception(error):
    """全局异常处理"""

    current_app.logger.error('start error'.center(40, '*'))
    current_app.logger.error(f'{request.method}, {request.path}'.center(60, '*'))
    current_app.logger.error(traceback.format_exc())
    if isinstance(error, HTTPException):
        current_app.logger.error('error is {} {} end.'.format(error.code, error.description))
        current_app.logger.error('end error'.center(40, '*'))
        return responses(status_code=error.code, code=Code.known_error.get('code'), message=error.description)
    current_app.logger.error('error is {} end.'.format(error))
    current_app.logger.error('end error'.center(40, '*'))
    return responses(status_code=400, code=Code.known_error.get('code'), message=f'{error}')
