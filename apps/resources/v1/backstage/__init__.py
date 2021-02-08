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
from .backstage_account import ProfileView

api.add_resource(TokenView, '/tokens', endpoint='api_v1_backstage_tokens')
api.add_resource(BackstageRolesView, '/roles', endpoint='api_v1_backstage_roles')
api.add_resource(BackstageRoleView, '/roles/<int:r_id>', endpoint='api_v1_backstage_role')
api.add_resource(ProfileView, '/profile', endpoint='api_v1_backstage_profile')
