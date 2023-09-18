import os
from pathlib import Path

basedir=Path(os.path.dirname(os.path.dirname(__file__)))

class Config:
    BROKER_CONNECTION_RETRY_ON_STARTUP=False
    @classmethod
    def init_app(cls,app):
        pass
