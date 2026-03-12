import json
from models.user import User as u


class UserManager:

    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        try:
            with open("data/user_data.json", "r") as rf:
                data = json.load(rf)

            users = []

            for username, info in data.items():
                info_dict = {
                    "username": username,
                    "password": info["password"],
                    "age": info["age"]
                }

                new_user = u.from_dict(info_dict)
                users.append(new_user)

            return users

        except FileNotFoundError:
            return []

    def save_users(self):

        data = {}

        for user in self.users:
            new_dict = user.to_dict()

            data[new_dict["username"]] = {
                "password": new_dict["password"],
                "age": new_dict["age"]
            }

        with open("data/user_data.json", "w") as wf:
            json.dump(data, wf, indent=4)

    def register_user(self, username, password, age):

        # check if username already exists
        for user in self.users:
            if user.username == username:
                return {"message": "User already exists"}

        new_user = u(username, password, age)

        self.users.append(new_user)

        self.save_users()

        return {"message": "User registered successfully"}

    def login_user(self, username, password):

        for user in self.users:

            if user.username == username:

                if user.check_password(password):
                    return {"message": "Login successful"}

                else:
                    return {"message": "Wrong password"}

        return {"message": "User not found"}

    def view_users(self):

        if not self.users:
            return []

        result = []

        for user in self.users:
            result.append(user.to_dict())

        return result