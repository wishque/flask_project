from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

db=SQLAlchemy()
migrate=Migrate()

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)

    from app import error_handler
    error_handler.init_app(app)

    from app import hooks
    hooks.init_app(app)

    from app.user.routes import bp as user_bp
    app.register_blueprint(user_bp)

    return app

    

