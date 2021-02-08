from flask import current_app

from flask_restful import marshal
from flask_restful import Resource

from apps.models import BackstageRole
from lib.tools import responses
from lib.error_define import ErrorCode
from lib.backstage.permission import admin_access_required, staff_access_required
from apps.entities.v1.backstage.backstage_role import filter_parser, create_parser, patch_parser
from apps.entities.v1.backstage.backstage_role import role_fields
from apps.logics.v1.backstage.backstage_role import filter_roles, patch_role
from apps.logics.v1.backstage.backstage_permission import build_permissions


class BackstageRolesView(Resource):

    @staff_access_required()
    def get(self):
        """后台管理系统角色列表"""

        params = filter_parser.parse_args()
        roles = filter_roles(params)
        total = roles.count()
        roles = roles.order_by(BackstageRole.id.desc())
        roles = roles.paginate(params['page'], params['pagesize'] or total).items
        roles = marshal(list(roles), role_fields)
        return responses(data={'total': total, 'roles': roles})

    @admin_access_required(['超级管理员', '二级管理员', '三级管理员'])
    def post(self):
        """后台管理系统角色创建"""

        params = create_parser.parse_args()
        role = BackstageRole(**params).save()
        return responses(data={'id': role.id}, **ErrorCode.create_success)


class BackstageRoleView(Resource):

    @staff_access_required()
    def get(self, r_id):
        """角色详情"""

        role = BackstageRole.get(id=r_id)
        if role:
            permissions = build_permissions(role.permissions)
            current_app.logger.debug(permissions)
            role = marshal(role, role_fields)
            role['permissions'] = permissions
            return responses(data=role)
        return responses(message='该角色不存在', **ErrorCode.not_exist)

    @admin_access_required(['超级管理员'])
    def delete(self, r_id):
        """更新角色删除状态"""

        role = BackstageRole.get(id=r_id)
        if role:
            if not role.is_delete:
                role.is_delete = True
            else:
                role.is_delete = False
            role.save()
            return responses(**ErrorCode.delete_success)
        return responses(message='该角色不存在', **ErrorCode.not_exist)

    @admin_access_required(['超级管理员'])
    def patch(self, r_id):
        """更新角色"""

        params = patch_parser.parse_args()
        role = BackstageRole.get(id=r_id)
        if role:
            patch_role(params, role)
            return responses(**ErrorCode.patch_success)
        return responses(message='该角色不存在', **ErrorCode.not_exist)
