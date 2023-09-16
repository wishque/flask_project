from app.common.models import BaseModel
from werkzeug.security import generate_password_hash,check_password_hash
from app import db

class User(BaseModel):
    username=db.Column(db.String(64),unique=True)
    password_hash=db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute.")
    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)
    
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
