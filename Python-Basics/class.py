# class Employee:
    
#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + "." + last + "@gmail.com"

#     def fullname(self):
#         return f"{self.first} {self.last}"

# emp1 = Employee("John","Smith",5000)
# emp2 = Employee("Test","User",8000)

# emp1.first = "John"           instead of doin this manually we can use init
# emp1.last = "Smith"       
# emp1.pay = 5000

# print(emp1.first)
# print(emp1.pay)
# print(emp2.email)

# print(emp1.fullname())  #or
# print(Employee.fullname(emp2))


class User:

    def __init__(self,username,password,age):

        self.username = username
        self.password = password
        self.age = age

    def display_info(self):
        return f"Username: {self.username} | Age: {self.age}"
    
    def check_password(self,entered_password):
        return self.password == entered_password
    

user1 = User("Vidhi","Vidhi1234",22)
user2 = User("Aarohi","1234567",40)

password = input("Enter password:")

print(user2.check_password(password))
        
# print(user1.display_info())
# print(user2.display_info())