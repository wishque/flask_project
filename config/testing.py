from .base import Config
class  TestingConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI="sqlite://"
    BROKER_URL='redis://localhost:6379/0'
    RESULT_BACKEND='redis://localhost:6379/1'
