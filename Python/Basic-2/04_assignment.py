# Question-1
# salary = int(input("Enter Salary: "))
# if(salary <30000):
#     tax = salary*.05
# elif(salary >=30000 and salary<70000):
#     tax= salary*.15
# else:
#     tax = salary*.25

# print(tax)

# Question-2
# a = int(input("Enter Num 1: "))
# b = int(input("Enter Num 2: "))
# for i in range(a,b+1):
#     if(i%2 == 0):
#         print(i)

# Question-3
# n =int(input("Enter Number:"))
# temp = n
# count = 0
# while(temp>0):
#    digit = temp/10
#    temp = temp//10
#    count+=1
# print(count)

# temp= n
# while(count>0):
#    digit = temp//(10**(count-1))
#    print(digit)
#    temp = temp%(10**(count-1))
#    count-=1

# Question-4
# def count_num(n):
#     temp = n
#     count = 0
#     while(temp>0):
#         digit = temp/10
#         temp=temp//10
#         count+=1
#     return count
# print(count_num(312))

# Question-5
# def sum_digit(n):
#     sum= 0
#     while n>0:
#         i = n%10
#         n = n//10
#         sum +=i
#     return sum
# print(sum_digit(315))

# Question-6
# for i in range(1,101):
#     if(i%3 == 0 and i%5 == 0):
#         print(i)

#Question-7
# while True:
#     num = (input("Enter Number:"))
#     if num == "Quit":
#         print("Terminate...")
#         break
#     Num = int(num)
#     if(Num>=0):
#         print("Possitive")
#     else:
#         print("Negative")

#Question-8
# def calculator(a,b,s):
#     if(s == '+'):
#         return a+b
#     elif(s=='-'):
#         return a-b
#     elif(s=='*'):
#         return a*b
#     elif(s=='/' and b !=0):
#         return a/b
#     else:
#         return "error"
    
# print(calculator(2,2,"@"))

# Question-9
# def is_prime(n):
#     for i in range(2,n):
#         if(n%i == 0):
#             return False
#             break
#         return True

# print(is_prime(12))

# Question-10

num= int(input("Enter Number:"))
while True:
    guess = int(input("Enter Guess:"))
    if(num<guess):
        print("Too High")
    elif(num==guess):
        print("Correct Guess")
        break
    else:
        print("Too Low")