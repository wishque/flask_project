from logger import logger
def init_app(app):
    app.register_error_handler(Exception,unhandled_exception)

def unhandled_exception(e:Exception):
    logger.exception(e)
    return "error"
