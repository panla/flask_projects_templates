from flask import g
from flask_restful import Resource
from flask_restful import marshal

from apps.lib.tools import responses
from apps.entities.v1.backstage.backstage_account import detail_info_fields


class ProfileView(Resource):

    def get(self):
        """获取当前用户的信息"""

        b_account = g.b_account
        data = marshal(b_account, detail_info_fields)
        return responses(data=data)
