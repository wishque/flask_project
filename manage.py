from app import create_app
import os
from logger import logger

app=create_app(os.environ.get("FLASK_CONFIG") or "default")