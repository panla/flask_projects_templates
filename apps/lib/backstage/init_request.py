from flask import request
from flask import current_app
from flask import g

from apps.lib.backstage.auth import decode_auth_token
from apps.lib.tools import responses
from apps.lib.code_define import Code


def identify():
    """在请求前，用户鉴权"""

    if request.path in ['/api/v1/backstage/tokens', '/api/v1/backstage/codes']:
        return None

    header_token = request.headers.get('X-TOKEN')
    if header_token:
        payload = decode_auth_token(header_token)
        if isinstance(payload, dict) and payload.get('data') and payload.get('data').get('id'):
            return None
        return responses(**Code.token_decode_error)
    return responses(**Code.headers_need_x_token)


def after_req_logger_info(response):
    """打印日志信息"""

    current_app.logger.info('start request'.center(40, '*'))
    current_app.logger.info('{} {}'.format(request.method, request.url))
    if hasattr(g, 'account') and hasattr(g, 'b_account'):
        account_id = g.account.id
        b_account_id = g.b_account.id
        phone = g.account.cellphone
        current_app.logger.info(f'Account.id={account_id} BAccount.id={b_account_id} Account.cellphone={phone} end.')
    if request.json:
        current_app.logger.info(request.json)
    current_app.logger.info('end request'.center(40, '*'))
    return response
