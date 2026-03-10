import json

def load_users():
    try:
        with open("users_data.json", "r") as rf:
            content = json.load(rf)
    except FileNotFoundError:
        print("File Not Found. Creating new file.")
        return {}
    return content


def save_users(data):
    with open("users_data.json", "w") as f:
        json.dump(data, f, indent=2)


def user_exists(username, content):
    return username in content


def register_user():

    username = input("Enter Username: ")

    if username.strip() == "":
        print("Username Cannot be Empty.")
        return

    password = input("Enter Password: ")

    if len(password) < 6:
        print("Password must be at least 6 characters long.")
        return

    try:
        age = int(input("Enter Age: "))
    except ValueError:
        print("Enter integer input.")
        return

    if age <= 0 or age > 150:
        print("Enter Valid age between 1 to 150")
        return

    content = load_users()

    if user_exists(username, content):
        print("Username already exists.")
        return

    content[username] = {"password": password, "age": age}

    save_users(content)

    print("User Registered Successfully.")


def login_user(username, password):

    content = load_users()

    if username in content and content[username]["password"] == password:
        print("Login Successful.")
    else:
        print("User Not Found or Wrong Password.")


def view_users():

    content = load_users()

    if not content:
        print("No Users Found.")
        return

    for person in content:
        print(person)


def main_menu():
    print("\n1. Register User")
    print("2. Login User")
    print("3. View All Users")
    print("4. Exit")


while True:
    main_menu()

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("\nInvalid Input , Enter Number.")
        continue

    if choice == 1:
        register_user()

    elif choice == 2:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        login_user(username, password)

    elif choice == 3:
        view_users()

    elif choice == 4:
        print("\nThank You.")
        break

    else:
        print("Invalid Choice Number.")