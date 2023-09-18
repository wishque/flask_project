from flask import current_app,request
from flask import g
from uuid import uuid4
import time

def init_app(app):
    app.before_request(add_request_id)
    app.before_request(before_request_log)
    app.after_request(after_request_log)

def before_request_log():
    current_app.logger.info(f"Recive Request: {request.method} {request.path}.")

def add_request_id():
    g.request_id=uuid4()
    g.start_time=time.time()

def after_request_log(response):
    cost=time.time()-g.start_time
    current_app.logger.info(f"Respond in {cost:.4f}s: {response.status}.")
    return response