class ApiError(Exception):
    code=None
    msg=None

class UserExist(ApiError):
    code=1001
    msg="用户已存在"

class AuthError(ApiError):
    code=1002
    msg="登陆失败"