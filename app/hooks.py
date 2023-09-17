from flask import current_app 

def before_request_log():
    current_app.logger.error("before request log")

def after_request_log(response):
    current_app.logger.error("after request log")
    return response