from flask import current_app
from flask import g

from apps.models import BackstageRole
from lib.error_define import ErrorCode
from lib.tools import responses


def admin_access_required(role_lis: list):
    def required(func):
        def decorator(*args, **kwargs):
            roles = BackstageRole.query.filter(BackstageRole.name.in_(role_lis)).all()
            if (g.b_account.role not in roles) or (not g.b_account.is_stff):
                return responses(**ErrorCode.no_access)
            return func(*args, **kwargs)
        return decorator
    return required


def staff_access_required():
    def required(func):
        def decorator(*args, **kwargs):
            if not g.b_account.is_stff:
                return responses(**ErrorCode.no_access)
            return func(*args, **kwargs)
        return decorator
    return required
