from .base import Config
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter
import os
from .base import basedir
from utils.log import RequestIDFilter
from flask import Flask


class ProductionConfig(Config):
    DEBUG=False
    TESTING=False

    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABSE_URI")  or f"sqlite:///{basedir/'app.db'}"

    BROKER_URL='redis://localhost:6379/0'
    RESULT_BACKEND='redis://localhost:6379/1'

    LOG_LEVEL=os.environ.get("LOG_LEVEL") or "INFO"
    LOG_PATH= basedir / (os.environ.get("LOG_PATH") or "logs/")

    ECHO=False

    @classmethod
    def init_app(cls,app:Flask):
        super().init_app(app)

        app.logger.setLevel(cls.LOG_LEVEL)
        os.makedirs(cls.LOG_PATH,exist_ok=True)
        handler=TimedRotatingFileHandler(cls.LOG_PATH/"app.log",when="W0")
        formatter=Formatter("%(asctime)s|%(levelname)s|%(filename)s line %(lineno)d|%(request_id)s - %(message)s","%Y-%m-%d %H:%M:%S")
        handler.setFormatter(formatter)
        handler.addFilter(RequestIDFilter())
        app.logger.handlers.clear()
        app.logger.addHandler(handler)
