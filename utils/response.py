def success(data):
    return {"code":1000,"msg":"成功","data":data}

def error(code,msg):
    return {"code":code,"msg":msg,"data":None}