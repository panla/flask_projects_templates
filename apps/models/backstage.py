from sqlalchemy.orm import validates
from sqlalchemy import text
from flask_sqlalchemy import BaseQuery

from apps.db import db
from apps.mixin.model import BaseModel, ModelMixin
from apps.mixin.model import UNSIGNED_BIGINTEGER, UNSIGNED_INTEGER, UNSIGNED_SMALLINT


class BackstageRole(db.Model, ModelMixin):

    __tablename__ = 'backstage_roles'
    __table_args__ = ({'comment': '后台管理系统角色表'})

    id = db.Column(UNSIGNED_INTEGER, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True, comment='角色名称')
    desc = db.Column(db.String(100), nullable=False, comment='角色描述')
    permissions_set = db.Column(db.String(500), nullable=False, comment='权限id,以,分割')
    is_delete = db.Column(db.Boolean, nullable=False, server_default=text('0'), comment='删除标志')

    @validates('name')
    def validate_name(self, key, value):
        """校验角色名称"""

        if BackstageRole.query.filter(BackstageRole.id != self.id, BackstageRole.name == value).first():
            raise Exception('该角色名称已存在')
        return value

    @property
    def permission_ids(self) -> list:
        """所拥有的权限id"""
        return self.permissions_set.split(',')

    @property
    def permissions(self) -> BaseQuery:
        """所拥有的权限"""
        from apps.models import ApiPermission

        _permission_ids = self.permissions_set.split(',')
        return ApiPermission.query.filter(ApiPermission.id.in_(_permission_ids), ApiPermission.is_delete.is_(False))

    @permissions.setter
    def permissions(self, value: list):
        self.permissions_set = ','.join(value)


class BackstageAccount(db.Model, ModelMixin):

    __tablename__ = 'backstage_accounts'
    __table_args__ = ({'comment': '后台管理系统账户表'})

    id = db.Column(UNSIGNED_BIGINTEGER, autoincrement=True, primary_key=True)
    account_id = db.Column(UNSIGNED_BIGINTEGER, unique=True, nullable=False, comment='统一账户')
    role_id = db.Column(UNSIGNED_INTEGER, index=True, nullable=False, comment='角色id')
    is_staff = db.Column(db.Boolean, nullable=False, server_default=text('0'), comment='是否是平台方账号')

    @property
    def role(self) -> BaseQuery:
        """所属角色"""

        return BackstageRole.get(id=self.role_id, is_delete=False)

    @property
    def account(self) -> BaseQuery:
        """统一账户"""

        from apps.models import Account
        return Account.get(id=self.account_id, is_delete=False)

    @property
    def permissions(self):
        from apps.logics.v1.backstage.backstage_permission import build_permissions

        if self.role and self.role.permissions:
            return build_permissions(self.role.permissions)
        return []
