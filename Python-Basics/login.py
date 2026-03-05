
def Register():
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
    
    with open('users.txt','a') as f:
        f.write(f'{username}|{password}|{age}\n')
        print("\nRegister Successfully!")

    return 


def login():
    
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    found = False

    try: 
        with open("users.txt",'r') as rf:

            for line in rf:
                line = line.strip()
                data = line.split('|')

                if data[0] == username and data[1] == password:
                    found = True
                    break

    except FileNotFoundError:
        print("File Doest Not Exists!")
        return

    if found:
        print("\nLogin Successful.")
        return 
    else:
        print("\nUser Not Found!")
        return 


def view():
    print("\nBelow is the list of users.\n")
    with open('users.txt' ,'r') as file:

        for line in file:
            print(line,end="")

    print("\nDone!!!!")
    return 


while True:
    print("\n1. Register User")
    print("2. Login User")
    print("3. View All Users")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("\nInvalid Input , Enter Number.")
        continue

    if choice == 1:
        Register()
    elif choice == 2:
        login()
    elif choice == 3:
        view()
    elif choice == 4:
        print("\nThank You.")
        break
    else:
        print("Invalid Choice Number.")