from logger import logger
from app.errors import ApiError
from utils.response import error
def init_app(app):
    app.register_error_handler(Exception,unhandled_exception)
    app.register_error_handler(ApiError,api_error)


def unhandled_exception(e:Exception):
    logger.exception(e)
    return error(1050,"服务器开小差了")

def api_error(e:ApiError):
    return error(e.code,e.msg)
