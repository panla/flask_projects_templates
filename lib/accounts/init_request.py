from flask import request
from flask import current_app
from flask import g

from lib.accounts.auth import decode_auth_token
from lib.tools import responses
from lib.error_define import ErrorCode


def identify():
    """在请求前，用户鉴权"""

    if request.path in ['/api/v1/accounts/tokens', '/api/v1/accounts', '/api/v1/accounts/codes']:
        return None

    header_token = request.headers.get('X-TOKEN')
    if header_token:
        payload = decode_auth_token(header_token)
        if isinstance(payload, dict) and payload.get('data') and payload.get('data').get('id'):
            return None
        return responses(**ErrorCode.token_decode_error)
    return responses(**ErrorCode.headers_need_x_token)


def after_req_logger_info(response):
    """打印日志信息"""

    current_app.logger.info('start request'.center(40, '*'))
    if hasattr(g, 'account'):
        cellphone = g.account.cellphone
        current_app.logger.info(f'Account.id = {g.account.id} Account.cellphone = {cellphone} end.')
    current_app.logger.info('{} {}'.format(request.method, request.url))
    if request.json:
        current_app.logger.info(request.json)
    current_app.logger.info('end request'.center(40, '*'))
    return response
