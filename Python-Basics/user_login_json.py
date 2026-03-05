import json

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
    
    data = {
        "name": username,
        "age" : age,
        "password": password
    }

    try:
        with open("users_data.json") as f:
            content = json.load(f)
            # print(content)  #content is a list
    except FileNotFoundError:
        users = []
        users.append(data)
    else:
        content.append(data)

        with open("users_data.json","w") as f:
            json.dump(content,f,indent=2)

    return
            
    

def login():
    
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    found = False

    try: 
        with open("users_data.json",'r') as rf:

            data = json.load(rf)

            for item in data:
                if item['name'] == username and item['password'] == password:
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

    with open('users_data.json' ,'r') as file:
        content = json.load(file)
        
        for item in content:        # to print new dictionary on new line
            print(item)
            
    # print(json.dumps(content,indent=2))  to print key , value pair like this on new line
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