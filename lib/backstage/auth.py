from datetime import datetime

from flask import current_app
from flask import g
import jwt

from apps.models import Account, BackstageAccount
from lib.jwt_tools import encode_token
from lib.tools import responses
from lib.response_code_define import ResponseCode


def authenticate(cellphone: str, code: str, passwd: str):
    """登录，获取token"""

    account = Account.get(cellphone=cellphone, is_delete=False)
    if account:
        b_account = BackstageAccount.get(account_id=account.id)
        if not b_account:
            return responses(message='该账号不是后台管理系统账号', **ResponseCode.not_exist)
        if not b_account.role:
            return responses(message='该账户的角色不存在', **ResponseCode.not_exist)
        if code:
            if current_app.redis.read(cellphone) != code:
                return responses(**ResponseCode.code_error)
        elif passwd:
            if not account.verify_password(passwd):
                return responses(**ResponseCode.passwd_error)
        else:
            responses(**ResponseCode.need_code_passwd)
        token, login_at, login_expired_at = encode_token(account.id, 'accounts')
        account.login_at = login_at
        account.login_expired_at = login_expired_at
        account.save()

        data = {
            'token': token,
            'account_id': account.id,
            'backstage_account_id': b_account.id
        }
        return responses(data=data, **ResponseCode.success_201)
    return responses(message='账户不存在', **ResponseCode.not_exist)


def decode_auth_token(auth_token: str):
    """校验 token"""

    now = datetime.now().timestamp()
    jwt_secret_key = current_app.config.get('JWT_SECRET_KEY')
    payload = jwt.decode(auth_token, jwt_secret_key, algorithms='HS256', options={'verify_exp': True})
    if isinstance(payload, dict) and (
            payload.get('data') and payload.get('data').get('id') and payload.get('data').get('table') == 'accounts'):
        account = Account.get(id=payload['data']['id'], is_delete=False)
        b_account = BackstageAccount.get(account_id=account.id)
        if not b_account:
            return responses(message='该账号不是后台管理系统账号', **ResponseCode.not_exist)
        if not b_account.role:
            return responses(message='该账户的角色不存在', **ResponseCode.not_exist)
        if not account:
            return responses(message='请重新登录', **ResponseCode.not_exist)
        if payload['data']['login_expired_at'] + 5 < now:
            return responses(**ResponseCode.login_expired)
        if payload['data']['login_at'] + 5 < account.login_at.timestamp():
            return responses(**ResponseCode.login_expired)
        g.account = account
        g.b_account = b_account
        return payload
    return responses(**ResponseCode.token_decode_error)
