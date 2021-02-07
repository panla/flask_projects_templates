from sqlalchemy.orm import validates
from sqlalchemy import text

from apps.db import db
from apps.mixin.model import BaseModel, ModelMixin
from apps.mixin.model import UNSIGNED_SMALLINT


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
        if BackstagePermission.query.filter(
                BackstagePermission.id != self.id, BackstagePermission.name == value).first():
            raise Exception('该权限名称已存在')


class BackstageRole(db.Model, ModelMixin):

    __tablename__ = 'backstage_roles'
    __table_args__ = ({'comment': '后台管理系统角色表'})

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True, comment='角色名称')
    permissions_set = db.Column(db.String(200), nullable=False, comment='权限id,以,分割')
    is_delete = db.Column(db.Boolean, nullable=False, server_default=text('0'), comment='删除标志')

    @validates('name')
    def validate_name(self, key, value):
        if BackstageRole.query.filter(BackstageRole.id != self.id, BackstageRole.name == value).first():
            raise Exception('该角色名称已存在')
