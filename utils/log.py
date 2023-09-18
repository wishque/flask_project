from logging import Filter
from flask import g
from celery import Task
import os
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter

class RequestIDFilter(Filter):
    """
    Log filter to inject the current request id of the request under `log_record.request_id`
    """

    def filter(self, log_record):
        log_record.request_id = g.request_id
        return log_record

# app.logger.setLevel(cls.LOG_LEVEL)
# os.makedirs(cls.LOG_PATH,exist_ok=True)
# handler=TimedRotatingFileHandler(cls.LOG_PATH/"app.log",when="W0")
# formatter=Formatter("%(asctime)s|%(levelname)s|%(filename)s line %(lineno)d|%(request_id)s - %(message)s","%Y-%m-%d %H:%M:%S")
# handler.setFormatter(formatter)
# handler.addFilter(RequestIDFilter())
# app.logger.handlers.clear()
# app.logger.addHandler(handler)
