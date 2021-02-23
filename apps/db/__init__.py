from flask_sqlalchemy import SignallingSession, get_state
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import orm


class RoutingSession(SignallingSession):
    def get_bind(self, mapper=None, clause=None):
        state = get_state(self.app)

        if self._flushing:
            # 写操作 ,使用主数据库
            return state.db.get_engine(self.app)
        else:
            # 读操作, 使用从数据库
            # 目前还没有研究主从复制，就先不搞这个了
            # return state.db.get_engine(self.app, bind='slave')
            return state.db.get_engine(self.app, bind='slave')


class RoutingSQLAlchemy(SQLAlchemy):
    def create_session(self, options):
        return orm.sessionmaker(class_=RoutingSession, db=self, **options)


db = RoutingSQLAlchemy()
