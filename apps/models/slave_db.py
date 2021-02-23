from sqlalchemy import text
from sqlalchemy import UniqueConstraint

from apps.db import db
from apps.mixin.model import ModelMixin
from apps.mixin.model import UNSIGNED_SMALLINT


class ApiPermission(db.Model, ModelMixin):

    __tablename__ = 'api_permissions'
    __bind_key__ = 'slave'

    id = db.Column(UNSIGNED_SMALLINT, primary_key=True)
    endpoint = db.Column(db.String(300), index=True, comment='endpoint')
    method = db.Column(db.String(10), nullable=False, comment='请求方法')
    is_delete = db.Column(db.Boolean, nullable=False, server_default=text('0'), comment='删除标志')
    name = db.Column(db.String(50), nullable=False, unique=True, comment='权限名称')
    parent_id = db.Column(UNSIGNED_SMALLINT, comment='父级权限')
    desc = db.Column(db.String(100), comment='描述简介')
    url = db.Column(db.String(200), comment='页面url')

    __table_args__ = (
        UniqueConstraint('endpoint', 'method'),
        {'comment': '接口权限表', 'useexisting': True}
    )