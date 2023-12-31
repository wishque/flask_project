from .base import Config,basedir
import os 

class DevelopmentConfig(Config):
    DEBUG=True

    SQLALCHEMY_DATABASE_URI=f'sqlite:///{basedir/"debug.db"}'

    BROKER_URL='redis://localhost:6379/0'
    RESULT_BACKEND='redis://localhost:6379/1'