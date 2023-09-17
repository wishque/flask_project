from .base import Config
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter
import os
from .base import basedir

class ProductionConfig(Config):
    DEBUG=False
    TESTING=False
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABSE_URI")  or "sqlite:///app.db"
    LOG_LEVEL=os.environ.get("LOG_LEVEL") or "INFO"
    LOG_PATH= basedir / (os.environ.get("LOG_PATH") or "logs/")

    @classmethod
    def init_app(cls,app):
        super().init_app(app)
        logger=logging.getLogger("app")
        os.makedirs(cls.LOG_PATH,exist_ok=True)
        handler=TimedRotatingFileHandler(cls.LOG_PATH/"app.log",when="W0")
        formatter=Formatter("%(asctime)s|%(message)s")
        handler.setFormatter(formatter)
        handler.setLevel(getattr(logging,cls.LOG_LEVEL))
        logger.addHandler(handler)

