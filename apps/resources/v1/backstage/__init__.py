from flask import Blueprint
from flask_restful import Api

from lib.backstage.init_request import identify
from lib.backstage.init_request import after_req_logger_info

blueprint = Blueprint('backstage', __name__, url_prefix='/api/v1/backstage')
api = Api(blueprint)

blueprint.before_request(identify)
blueprint.after_request(after_req_logger_info)

from .token import TokenView
from .backstage_role import BackstageRolesView, BackstageRoleView

api.add_resource(TokenView, '/tokens')
api.add_resource(BackstageRolesView, '/roles')
api.add_resource(BackstageRoleView, '/roles/<int:r_id>')
