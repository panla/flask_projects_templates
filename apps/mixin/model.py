from flask import current_app
from sqlalchemy import text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, SMALLINT, TINYINT

from apps.db import db

UNSIGNED_BIGINTEGER = BIGINT(unsigned=True)
UNSIGNED_INTEGER = INTEGER(unsigned=True)
UNSIGNED_SMALLINT = SMALLINT(unsigned=True)
UNSIGNED_TINYINT = TINYINT(unsigned=True)


def db_session_commit():
    try:
        db.session.commit()
    except Exception as exc:
        db.session.rollback()
        current_app.logger.error(exc)


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(UNSIGNED_BIGINTEGER, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='创建时间')
    updated_at = db.Column(
        db.DateTime, nullable=False,
        server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), comment='更新时间'
        )
    is_delete = db.Column(db.Boolean, nullable=False, server_default=text('0'), comment='删除标志')

    @property
    def created_time(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')

    @property
    def updated_time(self):
        return self.updated_at.strftime('%Y-%m-%d %H:%M:%S')


class ModelMixin(object):

    __slots__ = ()

    def __init__(self, **kwargs):
        pass

    def save(self):
        # 保存数据

        db.session.add(self)
        db_session_commit()
        return self

    def delete(self, commit=True):
        # 删除数据

        db.session.delete(self)
        if commit:
            db_session_commit()

    def update(self, **kwargs):
        # 修改数据

        commit = False
        for k, v in kwargs.items():
            if hasattr(self, k) and getattr(self, k) != v:
                commit = True
                setattr(self, k, v)
        if commit:
            db_session_commit()
        return commit

    def to_json(self, excludes=None, selects=None):
        # 返回json格式数据，序列化

        if not hasattr(self, '__table__'):
            raise AssertionError('<%r> does not have attribute for __table__' % self)
        elif selects:
            return {i: getattr(self, i) for i in selects}
        elif excludes:
            return {i.name: getattr(self, i.name) for i in self.__table__.columns if i.name not in excludes}
        else:
            return {i.name: getattr(self, i.name) for i in self.__table__.columns}

    @classmethod
    def get(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def list(cls, **kwargs):
        return cls.query.filter_by(**kwargs)
