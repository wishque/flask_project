from .base import Config
import os

class ProductionConfig(Config):
    DEBUG=False
    TESTING=False
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABSE_URI") 
    LOG_LEVEL=os.environ.get("LOG_LEVEL") or "INFO"

    @classmethod
    def init_app(cls,app):
        super().init_app(app)

