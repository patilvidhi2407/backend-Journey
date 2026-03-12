from fastapi import FastAPI
from services.user_manager import UserManager
from schemas.user_schema import UserRegister, Userlogin

manager = UserManager()

app = FastAPI()

users = []

# @app.post("/register")
# def register(username: str, password: str, age: int):
#     manager.register_user(username, password, age)
#     return {"message": "User registered successfully"}

@app.post("/register")
def register(user: UserRegister):
    manager.register_user(user.username, user.password, user.age)
    return {"message": "User registered successfully"}

@app.get("/users")
def get_users():
    return manager.view_users()

@app.post("/login")
def login(user: Userlogin):
    result = manager.login_user(user.username,user.password)
    return result
    