import pytest 
from pytest import MonkeyPatch
from flask import Flask
from app import create_app, db as _db
from app.common.auth import auth
import random
from flask_sqlalchemy import SQLAlchemy


@pytest.fixture(scope="function")
def app():
    app=create_app("testing")

    with app.app_context():
        _db.create_all() 

        yield app

        _db.drop_all()

@pytest.fixture(scope="function")
def client(app:Flask):
    client=app.test_client()
    return client

@pytest.fixture(scope="session")
def db():
    return _db

@pytest.fixture(scope="function",autouse=True)
def disable_auth(monkeypatch:MonkeyPatch):
    monkeypatch.setattr(auth,"verify_token_callback",lambda x: True)

# @pytest.fixture(scope="function",autouse=True)
# def disable_db_commit(db:SQLAlchemy,monkeypatch:MonkeyPatch):
#     session=db.session
#     monkeypatch.setattr(session,"commit",db.session.flush)

@pytest.fixture(scope='session', autouse=True)
def faker_session_locale():
    return ['zh_CN']

@pytest.fixture(scope='session', autouse=True)
def faker_seed():
    return random.randint(0,10**10)
