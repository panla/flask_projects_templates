from datetime import datetime

from flask import current_app
from flask import g
import jwt

from apps.models import Account
from lib.jwt_tools import encode_token
from lib.tools import responses


def authenticate(cellphone: str, code: str, passwd: str):
    """登录，获取token"""

    account = Account.get(cellphone=cellphone, is_delete=False)
    if account:
        if code:
            if current_app.redis.read(cellphone) != code:
                return responses(status_code=401, code=10001, message='手机短信验证码错误')
        elif passwd:
            if not account.verify_password(passwd):
                return responses(status_code=401, code=10001, message='账户密码错误')
        else:
            responses(status_code=401, code=10001, message='登录需要手机短信验证码或账户密码')
        token, login_at, login_expired_at = encode_token(account.id, 'accounts')
        account.login_at = login_at
        account.login_expired_at = login_expired_at
        account.save()

        data = {
            'token': token.decode(),
            'id': account.id
        }
        return responses(status_code=201, message='登录成功', data=data)
    return responses(status_code=404, code=10001, message='账户不存在')


def decode_auth_token(auth_token: str):
    """校验 token"""

    now = datetime.now().timestamp()
    payload = jwt.decode(auth_token, current_app.config.get('JWT_SECRET_KEY'), options={'verify_exp': True})
    if isinstance(payload, dict) and (
            payload.get('data') and payload.get('data').get('id') and payload.get('data').get('table') == 'accounts'):
        account = Account.get(id=payload['data']['id'], is_delete=False)
        if not account:
            return responses(status_code=401, code=10001, message='请重新登录')
        if payload['data']['login_expired_at'] + 5 < now:
            return responses(status_code=401, code=10001, message='登录过期，请重新登录')
        if payload['data']['login_at'] + 5 < account.login_at.timestamp():
            return responses(status_code=401, code=10001, message='登录失效，请重新登录')
        g.account = account
        return payload
    return responses(status_code=401, code=10001, message='登录验证错误，请重新登录')
