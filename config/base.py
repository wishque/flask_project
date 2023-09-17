import os
from pathlib import Path

basedir=Path(os.path.dirname(os.path.dirname(__file__)))

class Config:
    @staticmethod
    def init_app(app):
        pass