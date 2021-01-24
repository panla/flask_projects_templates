from flask_migrate import Migrate

from apps.db import db


def init_extension(app):
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(db=db, app=app)
