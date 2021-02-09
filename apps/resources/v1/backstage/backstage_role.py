from flask import current_app

from flask_restful import marshal
from flask_restful import Resource

from apps.models import BackstageRole
from lib.tools import responses
from lib.code_define import Code
from apps.entities.v1.backstage.backstage_role import filter_parser, create_parser, patch_parser
from apps.entities.v1.backstage.backstage_role import role_fields
from apps.logics.v1.backstage.backstage_role import filter_roles, patch_role
from apps.logics.v1.backstage.backstage_permission import build_permissions


class BackstageRolesView(Resource):

    def get(self):
        """后台管理系统角色列表"""

        params = filter_parser.parse_args()
        roles = filter_roles(params)
        total = roles.count()
        roles = roles.order_by(BackstageRole.id.desc())
        roles = roles.paginate(params['page'], params['pagesize'] or total).items
        roles = marshal(list(roles), role_fields)
        return responses(data={'total': total, 'roles': roles})

    def post(self):
        """后台管理系统角色创建"""

        params = create_parser.parse_args()
        role = BackstageRole(**params).save()
        return responses(data={'id': role.id}, **Code.create_success)


class BackstageRoleView(Resource):

    def get(self, r_id):
        """角色详情"""

        role = BackstageRole.get(id=r_id)
        if role:
            permissions = build_permissions(role.permissions)
            role = marshal(role, role_fields)
            role['permissions'] = permissions
            return responses(data=role)
        return responses(message='该角色不存在', **Code.not_exist)

    def delete(self, r_id):
        """更新角色删除状态"""

        role = BackstageRole.get(id=r_id)
        if role:
            if not role.is_delete:
                role.is_delete = True
            else:
                role.is_delete = False
            role.save()
            return responses(**Code.delete_success)
        return responses(message='该角色不存在', **Code.not_exist)

    def patch(self, r_id):
        """更新角色"""

        params = patch_parser.parse_args()
        role = BackstageRole.get(id=r_id)
        if role:
            patch_role(params, role)
            return responses(**Code.patch_success)
        return responses(message='该角色不存在', **Code.not_exist)
