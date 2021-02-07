from functools import wraps

from flask import current_app
from flask import g

from apps.models import BackstageRole


def super_admin_user_required(realm=None):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            if g.b_account.role != BackstageRole.get(name='超级管理员'):
                raise Exception('this backstage account is not a super admin user')
            return fn(*args, **kwargs)
        return decorator
    return wrapper


def admin_user_two_required(realm=None):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            roles = BackstageRole.query.filter(BackstageRole.name.in_(['超级管理员', '二级管理员'])).all()
            if g.b_account.role not in roles:
                raise Exception('this backstage account is not a admin user')
            return fn(*args, **kwargs)
        return decorator
    return wrapper


def admin_user_three_required(realm=None):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            roles = BackstageRole.query.filter(BackstageRole.name.in_(['超级管理员', '二级管理员', '三级管理员'])).all()
            if g.b_account.role not in roles:
                raise Exception('this backstage account is not a admin user')
            return fn(*args, **kwargs)
        return decorator
    return wrapper


def staff_user_required(realm=None):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            if not g.b_account.is_stff:
                raise Exception('this backstage account is not a staff user')
            return fn(*args, **kwargs)
        return decorator
    return wrapper
