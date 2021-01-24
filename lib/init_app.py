from flask import request
from flask import make_response
from flask import current_app
from werkzeug.exceptions import HTTPException

from lib.tools import responses


def init_app(app):
    app.before_request(cross_domain_access_before)
    app.after_request(cross_domain_access_after)
    app.register_error_handler(Exception, process_exception)


def cross_domain_access_before():
    """在请求前，设置路由跨域请求"""

    if request.method == 'OPTIONS':
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Max-Age'] = 24 * 60 * 60
        response.headers['Access-Control-Allow-Methods'] = "GET, POST, DELETE, PATCH"
        return response


def cross_domain_access_after(response):
    """在请求后，设置返回headers头"""

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response


def process_exception(error):
    current_app.logger.error(f'error {request.method}, {request.path} error'.center(60, '*'))
    if isinstance(error, HTTPException):
        current_app.logger.error('error is {} {} end.'.format(error.code, error.description))
        current_app.logger.error('error'.center(40, '*'))
        return responses(status_code=error.code, code=10200, message=error.description)
    current_app.logger.error('error is {} end.'.format(error))
    current_app.logger.error('error'.center(40, '*'))
    return responses(status_code=400, code=10200, message=f'{error}')
