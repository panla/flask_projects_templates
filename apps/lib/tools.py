def responses(status_code=200, code=10000, message='', data=None):
    return {'code': code, 'message': message, 'data': data}, status_code
