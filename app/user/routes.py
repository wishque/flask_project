from flask import Blueprint
from utils.request import request_data
from . import services

bp=Blueprint("user",__name__)

@bp.route("/",methods=["POST"])
def add_user():
    params=request_data()
    username=params.get("username")
    password=params.get("password")
    data=services.add_user(username,password)
    return data

@bp.route("/",methods=["GET"])
def list_user():
    return services.get_user_list()

