from .development import DevelopmentConfig
from .testing import TestingConfig
from .production import ProductionConfig

from .base import basedir

config={
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "production":ProductionConfig,

    "default":DevelopmentConfig,
}