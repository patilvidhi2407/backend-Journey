# list = [10 , 3.14 , True , 'Vidhi']
list_2 = ['Hindi','English']

nums = [30,90,70,10]
# list.insert(0,list_2)
# list.append(110)
# list.extend(['my_name',"his_name"])
# list.remove(list_2)
# value = list.pop()
# print(value)
# list.pop()
# list.reverse()
# list.sort()
# nums.sort(reverse=True)
# sorted = sorted(nums)
# print(nums)
# print(sorted)
# print(len(list))

# print(sum(nums))
# print(nums.index(10))
# print(10 in list)
# for index,item in enumerate(list,start = 1):
#     print(index,item)

# list_str = '-'.join(list_2)
# print(list_str)

# new_list = list_str.split('-')
# print(new_list)

# empty_list = []
# empty_list = list()

# print(empty_list)

marks = [30,50,90,70,60,20]
print("Highest Marks: ",max(marks))
print("Lowest Marks: ",min(marks))

average = sum(marks) / len(marks)
print(average)

count = 0
for num in marks:
    if num >= 40:
        count+=1
print(count)