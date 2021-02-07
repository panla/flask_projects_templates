from flask_restful import fields

detail_info_fields = {
    'id': fields.Integer,
    'account_id': fields.Integer,
    'is_staff': fields.Boolean,
    'name': fields.String(attribute='account.name'),
    'nickname': fields.String(attribute='account.nickname'),
    'cellphone': fields.String(attribute='account.cellphone'),
    'role': fields.Nested({
        'id': fields.Integer,
        'name': fields.String,
        'desc': fields.String
    }),
    'permissions': fields.Raw
}
