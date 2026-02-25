def greet():
    pass

# def hello_function(greet,name='You'): #defalut value
#     return f'{greet}, {name}'

# print(hello_function('hiii'))
# print(hello_function('hiii','Vidhi'))

# courses = ['Math','Sci']
# data = {'name':'Vidhi','age': 22}

# def info(*args,**kwargs):
#     print(args)
#     print(kwargs)

# info(10,20,'Hiii')
# info(10,'Hiii' ,name= 'Patil',age = 25)
# info(courses, name= 'Patil',age = 25)
# info(courses, data)
# info(*courses, data)
# info(*courses, **data)
# info(courses, *data) # as there is only one * hence it only considers keys in tuple
# #info(**courses) # error - as courses is not a dict

# Example function-1

# month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]  # 0 is for indexing purpose

# def is_leap(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# def days_in_month(year,month):

#     if not 1 <= month <= 12:
#         return 'Invalid Month'
    
#     if  month == 2 and is_leap(year):
#         return 29
    
#     return month_days[month]

# print(is_leap(1600))
# print(days_in_month(1600,4))


# Example function- 2

# def is_even(num):
#     return num % 2 == 0

# print(is_even(4))

# print('Even Numbers:')
# for i in range(1,6):
#     if is_even(i):
#         print(i)

# Example function - 3

# def find_largest(a,b,c):
#     if a > b:
#         if a > c:
#             return a
#         else:
#             return c
#     else:
#         if b > c:
#             return b
#         else:
#             return c

# print(find_largest(10,100000,500))

# Example function - 4

# def password_Check(password):

#     length = len(password)
#     digit = any(ch.isalpha() for ch in password)
#     letter = any(ch.isdigit() for ch in password)

#     if length >= 8:
#         if digit and letter:
#             return "Strong"
#         else:
#             return 'Weak'
#     else:
#         return 'Weak'
    
# print(password_Check('Vidhi123'))

#Example function - 5

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def Divide(a,b):
    return a / b

num1 = int(input("Enter first Number: "))
num2 = int(input("Enter Second Number: "))

while True:
    print("Menu")
    print("1.Add \n 2.Subtact \n 3.Multiply \n 4.Divide")
    choice = int(input("Enter Choice Number: "))
    if choice == 1:
        print(add(num1,num2))
    elif choice == 2:
        print(subtract(num1, num2))
    elif choice == 3:
        print(multiply(num1,num2))
    elif choice == 4:
        print(Divide(num1,num2))
    else:
        print("Invalid Output")

    check = input("Do you want to Continue? Y/n: ")
    if check == 'n':
        break
    elif check == "Y":
        continue
    else:
        print('Invalid Output')
        break
