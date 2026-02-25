# ***Dictionary***

# student = {True:"Vidhi",'age': 23,'courses':['Math','Hist']}
# student = {('name',10):"Vidhi",'age': 23,'courses':['Math','Hist']}
# student = {1:"Vidhi",'age': 23,'courses':['Math','Hist']}
student = {'name':"Vidhi",'age': 23,'courses':['Math','Hist']}
# print(student)
# print(student['phone'])
# print(student.get('phone','NOt Found'))
# print(student.get('name'))

# student['phone'] = '555-55556'
student['name'] = 'Aarohi'

student.update({'age':25,'city':'Pune'})

# del student['name']
# removed = student.pop('age')
# print(removed)

# print(len(student))
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student)

# for key in student:
#     print(key)

# for key , value in student.items():
#     print(key,value)

# student.clear()
# print(student)

# student = {
#     'name' : input("Enter Name: "),
#     'age' : int(input("Enter age: ")),
#     'marks' : int(input("Enter Marks: "))
# }

# student = {
#     'name' : 'Vidhi',
#     'age' : 25,
#     'marks' : 40
# }
# if student['marks'] < 40:
#     student["Status"] = "Fail"
# else:
#     student["Status"] = "Pass"

# print(student.keys())
# print(student.values())
# print(student)


# name = 'programming'
# count = {}                                    #Better way
# for ch in name:                               for ch in name:
#     if ch in count:                               count[ch] = count.get(ch,0) + 1
#         count[ch] +=1
#     else:
#         count[ch] = 1

# print(count)

# stock = {
#     'apple': 20,
#     'mango' : 10,
#     "kiwi" : 5
# }

# item = input("Item Name: ")
# quantity = int(input("Quantity to buy: "))

# if item in stock:
#     if quantity > stock[item]:
#         print("out of Stock")
#     else:
#         stock[item] -= quantity
#         print("Done")
# else:
#     print("Item not in stock")

users= {}
conti = True
while conti:
    print('''Add User - 1   View Users - 2   Exit - 3''')
    ans = int(input("Enter Choice Number: "))

    if ans == 1:
        name = input("Enter name: ")
        age = int(input("Enter Age: "))
        marks = int(input("Enter Marks: "))

        users.update({'name':name, 'age':age, 'marks':marks })
    elif ans == 2:
        print(users)
    else:
        conti = False
        print("Thank You!")