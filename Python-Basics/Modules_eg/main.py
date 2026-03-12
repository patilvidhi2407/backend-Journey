from services.user_manager import UserManager

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


# import sys
# import random
# import datetime
# print(sys.path)
# print(random.__file__)

# num = random.choice([1,2,3])
# print(num)

# print(datetime.date.today())