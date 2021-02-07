from flask_sqlalchemy import BaseQuery

from apps.models import BackstageRole


def filter_roles(params: dict) -> BaseQuery:
    """搜索后台管理系统角色"""

    roles = BackstageRole.list()
    if params.get('name') is not None:
        roles = roles.filter(BackstageRole.name.contains(params['name']))
    return roles


def patch_role(params: dict, role):
    """更新角色"""

    _params = dict()
    for k, v in params:
        if v:
            _params[k] = v
    role.update(**_params)
    role.save()
