from .base import Config,basedir
import os 

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=f'sqlite:///{basedir/"debug.db"}'