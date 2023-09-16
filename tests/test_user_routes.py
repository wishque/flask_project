from app import errors
from utils.response import error
def test_add_user(client):
    user={"username":"hello","password":"world"}
    response=client.post("/",json=user)
    assert response.json["code"]==1000
    response=client.post("/",json=user)
    e=errors.UserExist()
    assert response.status_code==200
    assert response.json==error(e.code,e.msg)

# def test_list_user(client):
#     response=client.get("/")
#     assert True

def test_login(client):
    user=dict(username="hello",password="worlda")
    response=client.post("/login",json=user)
    e=errors.AuthError()
    assert response.json==error(e.code,e.msg)
    response=client.post("/",json=user)
    assert response.json["code"]==1000