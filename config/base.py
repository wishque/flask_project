import os
from pathlib import Path

basedir=Path(os.path.dirname(os.path.dirname(__file__)))

class Config:
    LOG_PATH= basedir / (os.environ.get("LOG_PATH") or "logs/")
    @classmethod
    def init_app(cls,app):
        pass