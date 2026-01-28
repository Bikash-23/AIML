# Question-1
# str = input("Enter Name: ")
# is_palindrome = True
# for idx in range(0,len(str)//2):
#     if str[idx] != str[len(str)-1-idx]:
#         is_palindrome = False
#         break
    
# if is_palindrome:
#     print("Palindrome!")
# else:
#     print("Not Palindrome!")

# Question-2
# list = [1,2,3,4,5,6,7]
# sum = 0
# for i in range(len(list)):
#     sum+= list[i]
# print(sum)

# Question-3
# list1= [1,2,7]
# list2=[2,4,5]

# for i in range(len(list2)):
#     list1.append(list2[i])
# list1.sort()
# print(list1)

# Question-4
# num = (1,2,3,4,5,6)
# odd = []
# even = []
# for i in range (len(num)):
#     if(num[i] %2 == 0):
#         even.append(num[i])
#     else:
#        odd.append(num[i])
# print(even)
# print(odd)

# Question-5
# student ={
#     "Bikash": 67,
#     "Ravi":98,
#     "Ram":45
# }
# while True:
#     key = input("Enter Key:").upper()
#     if(key == "A"):
#         name = input("Enter Name:")
#         marks = int(input("Enetr Marks:"))
#         student[name] = marks
#     elif(key == "B"):
#         name = input("Enter Name for Update Marks:")
#         if name in student:
#          marks = int(input("Enetr Marks:"))
#          student[name] = marks
#         else:
#             print("Student not found!")

#     elif(key == "C"):
#         name = input("Enetr name for search:")
#         if name in student:
#             print(f"{name} : student{name}")
#         else:
#             print("Student not found!")
#     elif(key == "D"):
#         if not student:
#             print("No student in record")
#         else:
#             for name,marks in student.items():
#                 print(name,":",marks)
#     else:
#         if key == "E":
#             print("Exit...")
#             break
    
# Question-6
# words = ["apple","banana","kiwi","cherry","mango"]

# fruits= {}

# for i in range (len(words)):
#     fruits[words[i]] = len(words[i])

# print(fruits)

# Question-7
# str = input("Enetr String:")
# count = 0
# for i in range (len(str)):
#     if (str[i] == " "):
#       count+=1
# print(count)

# Question-8
# list1 = [1,2,3,4]
# list2 = [5,6,3,7,8]

# set1 =set(list1)
# set2 = set(list2)

# if set1.intersection(set2) :
#     print("share common element!")
# else:
#     print("No common element!")

# Question-9
# list1 = [1,2,2,3,4,5,6,5,4,7]
# seen = set()
# duplicate = set()

# for i in list1:
#     if i in seen:
#         duplicate.add(i)
#     else:
#         seen.add(i)

# print(duplicate)

# Question-10
s = input("Enter String: ")

unique_chars = set()

for ch in s:
    if s.count(ch) == 1:   # appears only once
        unique_chars.add(ch)

print("Unique characters:", unique_chars)
print(len(unique_chars))