from flask import request
from flask import make_response


def init_cross(app):
    app.before_request(cross_domain_access_before)
    app.after_request(cross_domain_access_after)


def cross_domain_access_before():
    """在请求前，设置路由跨域请求"""

    if request.method == 'OPTIONS':
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Max-Age'] = 24 * 60 * 60
        response.headers['Access-Control-Allow-Methods'] = "GET, POST, DELETE, PATCH"
        return response


def cross_domain_access_after(response):
    """在请求后，设置返回headers头"""

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
