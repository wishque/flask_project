from flask import Blueprint
from utils.request import request_data
from utils.response import success
from . import schemes
from . import services

bp=Blueprint("user",__name__)

@bp.route("/",methods=["POST"])
def add_user():
    user=schemes.UserScheme()
    args=user.load(request_data())
    data=services.add_user(**args)
    return success(data)

@bp.route("/",methods=["GET"])
def list_user():
    return success(services.get_user_list())

@bp.route("/login",methods=["POST"])
def login():
    params=request_data()
    username=params.get("username")
    password=params.get("password")
    result=services.login(username,password)
    return success(result)

