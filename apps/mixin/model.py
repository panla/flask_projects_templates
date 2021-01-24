from flask import current_app
from sqlalchemy import func
from sqlalchemy import text

from apps.db import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now(), comment='创建时间')
    updated_at = db.Column(
        db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), comment='更新时间')
    is_delete = db.Column(db.Boolean, server_default=text('0'), comment='删除标志')

    @property
    def created_time(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')

    @property
    def updated_time(self):
        return self.updated_at.strftime('%Y-%m-%d %H:%M:%S')


def db_session_commit():
    try:
        db.session.commit()
    except Exception as exc:
        db.session.rollback()
        current_app.logger.error(exc)


class ModelMixin(object):
    __slots__ = {}

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

    def add(self):
        # 添加数据

        db.session.add(self)

    def update(self, **kwargs):
        # 修改数据

        required_commit = False
        for k, v in kwargs.items():
            if hasattr(self, k) and getattr(self, k) != v:
                required_commit = True
                setattr(self, k, v)
        if required_commit:
            db_session_commit()
        return required_commit

    def to_json(self, excludes=None, selects=None):
        # 返回json格式数据，序列化

        if not hasattr(self, '__table__'):
            raise AssertionError(
                '<%r> does not have attribute for __table__' % self)
        elif selects:
            return {i: getattr(self, i) for i in selects}
        elif excludes:
            return {i.name: getattr(self, i.name)
                    for i in self.__table__.columns if i.name not in excludes}
        else:
            return {i.name: getattr(self, i.name)
                    for i in self.__table__.columns}

    @classmethod
    def get(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def list(cls, **kwargs):
        return cls.query.filter_by(**kwargs)
