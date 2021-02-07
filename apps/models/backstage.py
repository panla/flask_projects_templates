from sqlalchemy.orm import validates
from sqlalchemy import text
from flask_sqlalchemy import BaseQuery

from apps.db import db
from apps.mixin.model import BaseModel, ModelMixin
from apps.mixin.model import UNSIGNED_BIGINTEGER, UNSIGNED_SMALLINT


class BackstagePermission(db.Model, ModelMixin):

    __tablename__ = 'backstage_permissions'
    __table_args__ = ({'comment': '后台管理系统页面权限表'})

    id = db.Column(UNSIGNED_SMALLINT, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False, comment='权限名称')
    desc = db.Column(db.String(100), nullable=False, comment='权限描述')
    parent_id = db.Column(UNSIGNED_SMALLINT, comment='父级权限')
    is_delete = db.Column(db.Boolean, nullable=False, server_default=text('0'), comment='删除标志')

    @validates('name')
    def validate_name(self, key, value):
        """校验权限名称"""

        if BackstagePermission.query.filter(
                BackstagePermission.id != self.id, BackstagePermission.name == value).first():
            raise Exception('该权限名称已存在')


class BackstageRole(db.Model, ModelMixin):

    __tablename__ = 'backstage_roles'
    __table_args__ = ({'comment': '后台管理系统角色表'})

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True, comment='角色名称')
    desc = db.Column(db.String(100), nullable=False, comment='角色描述')
    permissions_set = db.Column(db.String(200), nullable=False, comment='权限id,以,分割')
    is_delete = db.Column(db.Boolean, nullable=False, server_default=text('0'), comment='删除标志')

    @validates('name')
    def validate_name(self, key, value):
        """校验角色名称"""

        if BackstageRole.query.filter(BackstageRole.id != self.id, BackstageRole.name == value).first():
            raise Exception('该角色名称已存在')

    @property
    def permission_ids(self) -> list:
        """所拥有的权限id"""
        return self.permissions_set.split(',')

    @property
    def permissions(self) -> BaseQuery:
        """所拥有的权限"""

        _permission_ids = self.permissions_set.split(',')
        return BackstagePermission.query.filter(
            BackstagePermission.id.in_(_permission_ids), BackstagePermission.is_delete.is_(False))


class BackstageAccount(db.Model, ModelMixin):

    __tablename__ = 'backstage_accounts'
    __table_args__ = ({'comment': '后台管理系统账户表'})

    id = db.Column(UNSIGNED_BIGINTEGER, autoincrement=True, primary_key=True)
    account_id = db.Column(UNSIGNED_BIGINTEGER, unique=True, nullable=False, comment='统一账户')
    role_id = db.Column(db.Integer, nullable=False, comment='角色id')
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
