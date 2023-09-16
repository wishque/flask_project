from .models import User
from app import db
from app.common.auth import auth

def add_user(username,password):
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