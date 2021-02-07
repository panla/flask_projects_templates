from datetime import datetime

from flask import current_app
import jwt


def encode_token(account_id: int, table: str):
    login_at = datetime.now()
    login_expired_at = login_at + current_app.config.get('TOKEN_EXP_DELTA')
    login_at_timestamp = login_at.timestamp()
    login_expired_at_timestamp = login_expired_at.timestamp()

    try:
        payload = {
            'exp': login_expired_at_timestamp,
            'iat': login_at_timestamp,
            'iss': 'ken',
            'data': {
                'id': account_id,
                'login_at': login_at_timestamp,
                'login_expired_at': login_expired_at_timestamp,
                'table': table
            }
        }
        token = jwt.encode(payload, current_app.config.get('JWT_SECRET_KEY'), algorithm='HS256')
        return token, login_at, login_expired_at
    except Exception as exc:
        current_app.logger.error(exc)
        return None
