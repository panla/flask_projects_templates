from sqlalchemy.orm import validates
from sqlalchemy import text

from apps.db import db
from apps.mixin.model import BaseModel, ModelMixin
from apps.mixin.model import UNSIGNED_SMALLINT


class ApiPermission(db.Model, ModelMixin):

    __tablename__ = 'api_permissions'
    __table_args__ = ({'comment': '接口权限表'})

    id = db.Column(UNSIGNED_SMALLINT, primary_key=True)
    endpoint = db.Column(db.String(300), nullable=False, unique=True, comment='endpoint')
    methods = db.Column(db.String(50), nullable=False, comment='请求方法,')
    is_delete = db.Column(db.Boolean, nullable=False, server_default=text('0'), comment='删除标志')
    name = db.Column(db.String(50), nullable=False, unique=True, comment='权限名称')
    parent_id = db.Column(UNSIGNED_SMALLINT, comment='父级权限')

    @validates('endpoint')
    def validate_endpoint(self, key, value):
        """校验权限名称"""

        if ApiPermission.query.filter(ApiPermission.id != self.id, ApiPermission.endpoint == value).first():
            raise Exception('该endpoint已存在')
        return value

    @validates('name')
    def validate_endpoint(self, key, value):
        """校验权限名称"""

        if ApiPermission.query.filter(ApiPermission.id != self.id, ApiPermission.name == value).first():
            raise Exception('该name已存在')
        return value

    @property
    def methods_(self):
        return self.methods.split(',')
