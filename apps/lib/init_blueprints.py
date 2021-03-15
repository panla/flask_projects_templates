from apps.resources.v1.backstage import blueprint as v1_backstage_blueprint


def register_blueprints(app):
    """注册蓝图"""

    app.register_blueprint(v1_backstage_blueprint)
