import pytest 
from pytest import MonkeyPatch
from flask import Flask
from app import create_app, db as db
from app.common.auth import auth


@pytest.fixture(scope="session")
def app():
    app=create_app("testing")

    with app.app_context():
        db.create_all() 

        yield app

        db.drop_all()

@pytest.fixture(scope="function",autouse=True)
def disable_auth(monkeypatch:MonkeyPatch):
    monkeypatch.setattr(auth,"verify_token_callback",lambda x: True)

@pytest.fixture(scope="session")
def client(app:Flask):
    client=app.test_client()
    return client
