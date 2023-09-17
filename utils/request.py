from flask import request
def request_data():
    if request.method in ["PUT","POST"]:
        if hasattr(request,"json") and request.json:
            return request.get_json()
    return request.form
