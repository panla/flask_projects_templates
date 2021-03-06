from flask_restful import Resource
from flask_restful import reqparse

from apps.lib.backstage.auth import authenticate


class TokenView(Resource):

    def post(self):
        """获取token"""

        parser = reqparse.RequestParser()
        parser.add_argument('cellphone', type=str, required=True, help='手机号')
        parser.add_argument('password', type=str, required=True, help='密码')
        params = parser.parse_args()
        return authenticate(cellphone=params['cellphone'], code='', passwd=params['password'])
