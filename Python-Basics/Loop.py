nums = (1,2,3,4,5)

# for num in nums:
#     if(num == 3):
#         break
#     print(num)
    
# for num in nums:
#     if(num == 3):
#         print("Got It!")
#         continue
#     print(num)

# for num in nums:
#     for letter in 'abc':
#         print (letter)
#     print(num)

# for i in range(9,11):
#     print(i)

x = 1
# while x < 10:
#     if x == 5:
#         break
#     print(x)
#     x+=1

# while x < 10:
#     print(x)
#     x += 1

# sum of first 10 number

# n = int(input("Enter value of n: "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)

# for i in range(1,11):
#     for n in range(1,11):
#         t = i * n
#         print(f'{i} * {n} = {t}')
#     print("\n")


# n= 0
# while n < 3:
#     password = input("Enter Password: ")
#     if password == "Vidhi":
#         print("Success")
#         break
#     elif n == 2:
#         print("Account Locked !")
#     else:
#         print("Try Again")
#     n += 1

count = 0

for i in range(1,101):
    if i % 2 == 0:
        count+=1
        print(i)
print(count)
