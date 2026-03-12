from pydantic import BaseModel

class UserRegister(BaseModel):
    username:str
    password: str
    age: int

class Userlogin(BaseModel):
    username:str
    password:str