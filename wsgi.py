from app import create_app
import os

app=create_app(os.environ.get("FLASK_CONFIG") or "default")

celery_app=app.extensions["celery"]
celery_app.autodiscover_tasks(["app.user"])