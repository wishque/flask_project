from flask_httpauth import HTTPTokenAuth

auth=HTTPTokenAuth()

@auth.verify_token
def verify_token(token):
    if not token:
        raise Exception
    
    user=None
    if user is None:
        raise Exception

    return user