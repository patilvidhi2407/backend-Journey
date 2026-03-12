import json
from models import user as u

class UserManager:

    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        try:
            with open("Modules_eg/data/users.json", "r") as rf:
                data = json.load(rf)

            users = []
            for username, info in data.items():
                info_dict = {"username": username,"password":info["password"],"age" : info["age"]}
                new_user = u.User.from_dict(info_dict)
                users.append(new_user)
            return users

        except FileNotFoundError:
            return []

    def save_users(self):
        data = {}

        for user in self.users:
            new_dict = user.to_dict()
            data[new_dict["username"]] = { "password": new_dict["password"], "age": new_dict["age"] }


        with open("Modules_eg/data/users.json", "w") as wf:
            json.dump(data, wf, indent=4)


    def register_user(self):
        username = input("Enter Username: ")

        for user in self.users:
            if user.username == username:
                print("User already exists.")
                return

        password = input("Enter Password: ")
        age = int(input("Enter Age: "))

        new_user = u.User(username, password, age)

        self.users.append(new_user) 

        self.save_users()

        print("User Registered Successfully.")

    def login_user(self, username, password):
        found = False
        for user in self.users:
            if user.username == username:
                found = True
                break

        if not found:
            print("User Not found")
            return

        for user in self.users:
            if user.username == username:
                if user.check_password(password):
                    print("Login Successful.")
                else:
                    print("Wrong Password.")
        return

    def view_users(self):

        if not self.users:
            print("No users found.")
            return

        for user in self.users:
            print(user.display())
        return
