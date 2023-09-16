from logger import logger

def before_request_log():
    logger.error("before request log")

def after_request_log(response):
    logger.error("after request log")
    return response