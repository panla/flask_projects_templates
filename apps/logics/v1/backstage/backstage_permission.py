from flask import current_app
from flask_restful import marshal

from apps.models import ApiPermission
from apps.entities.v1.backstage.backstage_permission import permission_fields


def build_permissions(permissions) -> list:
    results = []
    for permission in permissions:
        children = ApiPermission.list(parent_id=permission.id, is_delete=False)
        permission = marshal(permission, permission_fields)
        if children.first():
            children = marshal(list(children), permission_fields)
            permission['children'] = children
            results.append(permission)
    return results
