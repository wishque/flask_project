from app import create_app
import os

flask_app=create_app(os.environ.get("FLASK_CONFIG") or "default")

celery_app=flask_app.extensions["celery"]
celery_app.autodiscover_tasks(["celery_app.user"])