from app import errors
def test_add_user(client):
    user={"username":"hello","password":"world"}
    response=client.post("/",json=user)
    assert response.status_code==200
    response=client.post("/",json=user)
    assert response.status_code==200
    assert response.json["code"]==errors.USER_EXIST

def test_list_user(client):
    response=client.get("/")
    print(response.data)
    assert True