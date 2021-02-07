from flask import Blueprint
from flask_restful import Api

from lib.accounts.init_request import identify
from lib.accounts.init_request import after_req_logger_info

blueprint = Blueprint('accounts', __name__, url_prefix='/api/v1/accounts')
api = Api(blueprint)

blueprint.before_request(identify)
blueprint.after_request(after_req_logger_info)
