from flask_restful import reqparse
from flask_restful import inputs
from flask_restful import fields

filter_parser = reqparse.RequestParser()
filter_parser.add_argument('page', type=inputs.positive, required=False, default=1, help='页数，正整数')
filter_parser.add_argument('pagesize', type=inputs.int_range(1, 20), required=False, help='每页数量，(1, 20)')
filter_parser.add_argument('name', type=str, required=False, help='角色名称，模糊搜索，字符串')

create_parser = reqparse.RequestParser()
create_parser.add_argument('name', type=str, required=True, help='角色名称')
create_parser.add_argument('desc', type=str, required=True, help='角色描述')
create_parser.add_argument('permissions', type=inputs.positive, action='append', required=True, help='权限id，数组')

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('name', type=str, required=False, help='角色名称')
patch_parser.add_argument('desc', type=str, required=False, help='角色描述')
patch_parser.add_argument('permissions', type=inputs.positive, action='append', required=False, help='权限id，数组')

role_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'desc': fields.String,
    'is_delete': fields.Boolean
}
