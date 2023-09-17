from flask import current_app 

def init_app(app):
    app.before_request(before_request_log)
    app.after_request(after_request_log)

def before_request_log():
    current_app.logger.info("before request log")

def after_request_log(response):
    current_app.logger.info("after request log")
    return response