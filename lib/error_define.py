class ErrorCode(object):

    success = {'status_code': 200, 'code': 10000, 'message': '请求成功'}
    success_201 = {'status_code': 201, 'code': 10000}
    success_204 = {'status_code': 204, 'code': 10000}
    patch_success = {'status_code': 201, 'code': 10000, 'message': '更新成功'}
    delete_success = {'status_code': 201, 'code': 10000, 'message': '删除成功'}
    create_success = {'status_code': 201, 'code': 10000, 'message': '创建成功'}

    not_known_error = {'status_code': 400, 'code': 20001, 'message': '未知错误'}
    login_expired = {'status_code': 401, 'code': 20002, 'message': '登录失效'}
    passwd_error = {'status_code': 400, 'code': 20003, 'message': '密码错误'}
    code_error = {'status_code': 400, 'code': 20004, 'message': '短信验证码错误'}
    not_exist = {'status_code': 404, 'code': 20005}
    need_code_passwd = {'status_code': 400, 'code': 20006, 'message': '登录需要短信验证码或密码'}
    token_decode_error = {'status_code': 401, 'code': 20007, 'message': '登录验证错误'}
    headers_need_x_token = {'status_code': 401, 'code': 20008, 'message': '请求头中需要X-TOKEN'}
