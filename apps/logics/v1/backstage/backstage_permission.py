from flask_restful import marshal

from apps.models import BackstagePermission
from apps.entities.v1.backstage.backstage_permission import permission_fields


def build_permissions(permissions) -> list:
    results = []
    for permission in permissions:
        children = BackstagePermission.list(parent_id=permission.id)
        children = marshal(list(children), permission_fields)
        permission = marshal(permission, permission_fields)
        permission['children'] = children
        results.append(permission)
    return results
