from .models import User
from app import db
from app.common.auth import auth
from app import errors

def add_user(username,password):
    user=User.query.filter(User.username==username).first()
    if user:
        raise errors.UserExist()
    user=User()
    user.username=username
    user.password=password
    db.session.add(user)
    db.session.commit()
    data={
        "username":user.username
    }
    return data


def get_user_list():
    result=User.query.all()
    return [user.username for user in result]

def login(username,password):
    user=User.query.filter(User.username==username).first()
    if user is None or not user.check_password(password):
        raise errors.AuthError()
    return "this is token"