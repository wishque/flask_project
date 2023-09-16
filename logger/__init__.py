import logging
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter
from config import basedir
import os

logger=logging.getLogger("app")
handler=TimedRotatingFileHandler(os.path.join(basedir,"logs/app.log"),when="W0")
formatter=Formatter("%(asctime)s|%(message)s")
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)
logger.addHandler(handler)