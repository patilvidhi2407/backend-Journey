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