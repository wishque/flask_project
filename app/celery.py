from flask import Flask
from celery import Celery,Task

def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    config={key.lower():value for key,value in app.config.items()}
    celery_app.config_from_object(config)
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app