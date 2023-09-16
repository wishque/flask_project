from app import errors
from utils.response import error
from faker import Faker
from flask_sqlalchemy import SQLAlchemy
from flask.testing import FlaskClient
from app.user.models import User

def test_add_user(client:FlaskClient,faker:Faker):
    user=dict(username=faker.unique.name(),password=faker.password())
    response=client.post("/",json=user)
    assert response.json["code"]==1000

def test_add_exist_user(client:FlaskClient,faker:Faker,):
    user=dict(username=faker.unique.name(),password=faker.password())
    response=client.post("/",json=user)
    assert response.json["code"]==1000
    response=client.post("/",json=user)
    e=errors.UserExist()
    assert response.json==error(e.code,e.msg)


def test_login_failed(client:FlaskClient,faker:Faker):
    user=dict(username=faker.unique.name(),password=faker.password())
    response=client.post("/login",json=user)
    e=errors.AuthError()
    assert response.json==error(e.code,e.msg)

def test_login_success(client:FlaskClient,faker:Faker):
    user=dict(username=faker.unique.name(),password=faker.password())
    response=client.post("/",json=user)
    assert response.json["code"]==1000
    response=client.post("/login",json=user)
    assert response.json["code"]==1000