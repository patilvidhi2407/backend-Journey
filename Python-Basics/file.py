# First Way to open file ( Have to explicitly close the file)

# f = open('test.txt', 'r')
# print(f.read())
# print(f.name)
# print(f.mode)

# print(f.closed)
# print(f.close())

#Using context manager best mode

# with open('test.txt', 'r') as f:
#     f_content = f.read()
#     print(f_content)
    
# print(f.closed)

# with open('test.txt','r') as f:
    # f_data = f.readline()
    # print(f_data,end = '')
    # f_data = f.readline()
    # print(f_data)

    # f_data = f.readlines()
    # print(f_data)

    # for line in f:
    #     print(line,end='')

    # f_content = f.read(100)
    # print(f_content,end='')

    # f_content = f.read(100)
    # print(f_content)

    # size_to_read = 100
    # f_contents = f.read(size_to_read)
    # while len(f_contents) > 0:
    #     print(f_contents,end='')
    #     f_contents = f.read(size_to_read)

    # print(f.tell())

    # f_data = f.read(10)
    # print(f_data)
    # f.seek(10)
    # f_data = f.read(10)
    # print(f_data)

# with open('test2.txt','w') as f:
#     f.write('Hii Vidhi')
#     f.seek(0)
#     f.write("How?")

# with open('Test.txt','r') as rf:
#     with open('test_copy.txt','w')as wf:
#         for line in rf:
#             wf.write(line)


#### task 1

# file_name = input("Enter file name: ")

# try:
#     f = open(file_name , 'r')
#     print(f.read())
# except FileNotFoundError:
#     print("File Not Exists")

#### Task 2

# name = input("Enter name: ")
# age = int(input("Enter age: "))
# City = input("Enter City: ")

# with open("test2.txt" , "a") as f:
#     f.write(f"Name: {name} | Age: {age} | City: {City} \n")

# print("Data Submitted")

#### Task 3

# with open("test2.txt","r") as f:
#     count = 0
#     city_count = {}
#     for line in f:
#         count += 1  
#         edit = line.split('|')
#         city_name = edit[2].split(':')
#         city = city_name[1].strip()
#         if city in city_count:
#             city_count[city] += 1
#         else:
#             city_count[city] = 1
   
#     print("Total Entries: ",count)
#     print(city_count)        

#### Task 4

# condition = True

# while condition:
#     choice = int(input("1. Add Note: \n2. View Notes \n3.Exit \n"))
#     if choice == 1:
#         note = input("Give Note: ")
#         with open("test2.txt","a") as f:
#             f.write("\n" + note)
#     elif choice == 2:
#         with open("test2.txt","r") as r:
#             print(r.read())
#     elif choice == 3:
#         break
#     else:
#         print("Wrong Choice Number.")

#### Better Version

# while True:
#     print("1. Add Note")
#     print("2. View Notes")
#     print("3. Exit")

#     try:
#         choice = int(input("Enter choice: "))
#     except ValueError:
#         print("Please enter a number.")
#         continue

#     if choice == 1:
#         note = input("Give Note: ")
#         with open("test2.txt", "a") as f:
#             f.write(note + "\n")

#     elif choice == 2:
#         try:
#             with open("test2.txt", "r") as f:
#                 print(f.read())
#         except FileNotFoundError:
#             print("No notes found.")

#     elif choice == 3:
#         print("Exiting...")
#         break

#     else:
#         print("Wrong choice number.")


#### using Function

# def add_note():
#     note = input("Give Note: ")
#     with open("test2.txt", "a") as f:
#         f.write(note + "\n")
#     print("Note added successfully.")


# def view_notes():
#     try:
#         with open("test2.txt", "r") as f:
#             content = f.read()
#             if content.strip() == "":
#                 print("No notes found.")
#             else:
#                 print("\n--- Notes ---")
#                 print(content)
#     except FileNotFoundError:
#         print("No notes file found.")


# def show_menu():
#     print("\n1. Add Note")
#     print("2. View Notes")
#     print("3. Exit")


# def main():
#     while True:
#         show_menu()
#         try:
#             choice = int(input("Enter choice: "))
#         except ValueError:
#             print("Please enter a valid number.")
#             continue

#         if choice == 1:
#             add_note()
#         elif choice == 2:
#             view_notes()
#         elif choice == 3:
#             print("Exiting program...")
#             break
#         else:
#             print("Wrong choice number.")


# main()