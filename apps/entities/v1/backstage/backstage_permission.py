from flask_restful import fields

permission_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'desc': fields.String,
    'url': fields.String,
    'endpoint': fields.String,
    'method': fields.String,
    'parent_id': fields.Integer
}
