# try:
#     f = open('Test.txt')
#     if f.name == "Test.txt":
#         raise Exception
# except Exception as e:
#     print("Error!")
# else:
#     print(f.read())
#     f.close()
# finally:
#     print("Program Executed!")

#### Task 1

# while True:

#     try:
#         num1 = int(input("Enter First Number: "))
#         num2 = int(input("Enter Second Number: "))
#     except ValueError:
#         print("Invalid Value!")
#         break
#     else:
#         print("Calulator.")
#         print("1.Addition")
#         print("2.Subtraction")
#         print("3.Multiplication")
#         print("4.Division")
#         print("5.Exit")

#         choice = int(input("Enter Choice: "))

#         if choice == 1:
#             print("Addition is: ",num1+num2)
#         elif choice == 2:
#             print("Subtraction is: ",num1-num2)
#         elif choice == 3:
#             print("Multiplication is: ",num1*num2)
#         elif choice == 4:
#             try:
#                 divison = num1/num2
#             except ZeroDivisionError:
#                 print("Number can't be divided by zero.")
#             else:
#                 print("Division is: ",num1/num2)
#         elif choice == 5:
#             break
#         else:
#             print("Wrong choice Number.")
    
### Task 2

# def withdraw(balance,amount):
#     try:
#         if amount > balance:
#             raise ValueError
#     except ValueError:
#         return "Insufficient Balance."
#     else:
#         total = balance-amount
#         return f"Balance: {total}"


# amt = int(input("Enter Amount: "))
# bal = int(input("Enter Balance: "))

# print(withdraw(amt,bal))

#### Task 3
while True:
    try:
        age = int(input("Enter age: "))

        if age < 0 or age > 120:
            raise ValueError("Age out of valid range")

        break   # valid input → exit loop

    except ValueError as e:
        print(e)

