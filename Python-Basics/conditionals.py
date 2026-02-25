# language = "C++"

# if language == "Python":
#     print("Language is Python")
# elif language == "java":
#     print("language is Java")
# elif language == "JavaScript":
#     print("Language is JavaScript")
# else:
#     print("No match")

# a = [1,2,3]
# # b = [1,2,3]
# b = a

# print(id(a))
# print(id(b))

# # print(id(a) == id(b))
# print(a is b)

# condition = False / None / 0 / 0.0 / '' / [] / () / {}

# if condition:
#     print('Evaluates as True')
# else:
#     print('Evaluates as False')

num1, num2, num3 = map(int,input("Enter 3 numbers: ").split())

if num1 < num2:
    if num2 > num3:
        print("Max: " , num2)
    else:
        print("Max: " , num3)
else:
    if num1 > num3:
        print("Max: " , num1)
    else:
        print("Max:" ,num3)