from werkzeug.security import generate_password_hash, check_password_hash

from apps.db import db
from apps.mixin.model import BaseModel, ModelMixin


class Account(BaseModel, ModelMixin):

    __tablename__ = 'accounts'
    __table_args__ = ({'comment': '账户表'})

    cellphone = db.Column(db.String(12), unique=True, nullable=False, comment='手机号')
    name = db.Column(db.String(50), nullable=False, server_default='', comment='姓名')
    nickname = db.Column(db.String(50), nullable=False, server_default='', comment='昵称')
    password_hash = db.Column(db.String(300), nullable=False, comment='密码加密')

    @property
    def password(self):
        raise Exception('不可查看密码')

    @password.setter
    def password(self, value: str):
        self.password_hash = generate_password_hash(value)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
