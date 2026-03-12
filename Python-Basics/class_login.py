# import json

# class User:

#     def __init__(self, username, password, age):
#         self.username = username
#         self.password = password
#         self.age = age

#     def display(self):
#         return f"Username: {self.username} | Age: {self.age}"

#     def check_password(self, entered_password):
#         return self.password == entered_password

#     def to_dict(self):
#         return {
#         "username": self.username,
#         "password": self.password,
#         "age": self.age
#         }

#     def from_dict(data):
#         return User(
#         data["username"],
#         data["password"],
#         data["age"]
#         )
        

# class UserManager:

#     def __init__(self):
#         self.users = self.load_users()

#     def load_users(self):
#         try:
#             with open("users_data.json", "r") as rf:
#                 data = json.load(rf)

#             users = {}
#             for username, info in data.items():
#                 # users[username] = User(username, info["password"], info["age"])
#                 users[username] = User.from_dict(info)

#             return users

#         except FileNotFoundError:
#             return {}

#     def save_users(self):
#         data = {}

#         for username, user in self.users.items():
#             data[username] = {
#                 "password": user.password,
#                 "age": user.age
#             }

#         with open("users_data.json", "w") as wf:
#             json.dump(data, wf, indent=4)

#     def register_user(self):
#         username = input("Enter Username: ")

#         if username in self.users:
#             print("User already exists.")
#             return

#         password = input("Enter Password: ")
#         age = int(input("Enter Age: "))

#         new_user = User(username, password, age)

#         self.users[username] = new_user

#         self.save_users()

#         print("User Registered Successfully.")

#     def login_user(self, username, password):

#         if username not in self.users:
#             print("User not found.")
#             return

#         user = self.users[username]

#         if user.check_password(password):
#             print("Login Successful.")
#         else:
#             print("Wrong Password.")

#     def view_users(self):

#         if not self.users:
#             print("No users found.")
#             return

#         for user in self.users.values():
#             print(user.display())


# def main_menu():

#     manager = UserManager()

#     while True:

#         print("\n1. Register User")
#         print("2. Login User")
#         print("3. View All Users")
#         print("4. Exit")

#         try:
#             choice = int(input("Enter choice: "))
#         except ValueError:
#             print("Invalid input.")
#             continue

#         if choice == 1:
#             manager.register_user()

#         elif choice == 2:
#             username = input("Enter Username: ")
#             password = input("Enter Password: ")
#             manager.login_user(username, password)

#         elif choice == 3:
#             manager.view_users()

#         elif choice == 4:
#             print("Thank You.")
#             break

#         else:
#             print("Invalid Choice.")


# main_menu()



###  Using Json -> Dictionary -> User Object
#    User objects → dictionaries → JSON 

import json

class User:

    def __init__(self, username, password, age):
        self.username = username
        self.password = password
        self.age = age

    def display(self):
        return f"Username: {self.username} | Age: {self.age}"

    def check_password(self, entered_password):
        return self.password == entered_password

    def to_dict(self):
        return {
        "username": self.username,
        "password": self.password,
        "age": self.age
        }

    @staticmethod
    def from_dict(data):
        return User(
        data["username"],
        data["password"],
        data["age"]
        )
        

class UserManager:

    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        try:
            with open("users_data.json", "r") as rf:
                data = json.load(rf)

            users = []
            for username, info in data.items():
                info_dict = {"username": username,"password":info["password"],"age" : info["age"]}
                new_user = User.from_dict(info_dict)
                users.append(new_user)
            return users

        except FileNotFoundError:
            return []

    def save_users(self):
        data = {}

        for user in self.users:
            new_dict = user.to_dict()
            data[new_dict["username"]] = { "password": new_dict["password"], "age": new_dict["age"] }


        with open("users_data.json", "w") as wf:
            json.dump(data, wf, indent=4)


    def register_user(self):
        username = input("Enter Username: ")

        for user in self.users:
            if user.username == username:
                print("User already exists.")
                return

        password = input("Enter Password: ")
        age = int(input("Enter Age: "))

        new_user = User(username, password, age)

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


def main_menu():

    manager = UserManager()

    while True:

        print("\n1. Register User")
        print("2. Login User")
        print("3. View All Users")
        print("4. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == 1:
            manager.register_user()

        elif choice == 2:
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            manager.login_user(username, password)

        elif choice == 3:
            manager.view_users()

        elif choice == 4:
            print("Thank You.")
            break

        else:
            print("Invalid Choice.")


main_menu()