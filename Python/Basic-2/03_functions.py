# function:: block of statement that perform a specific task
# function::
#     definition
#     fun call

# function type:
#     build-in:: print(),input(),type(),range()
#     user-define:: sum(),avg()

# def printHello():
#     print("Hello")

# printHello()

# def sum(a,b):
#     s = a+b
#     return s

# print(sum(5,2))

# def avg(a,b,c):
#     a = (a+b+c)/3
#     return a
# print(avg(1,2,3))

# set defult value 
# defult value added at the end
# def avg(a,b ,c=1):
#     a = (a+b+c)/3
#     return a
# print(avg(2,3))
# print(avg(2,3,5))

def factorial(n):
    for i in range(1,n):
        n*=i
    return n
print(factorial(5))

# ----------lambda-function-----------

# avg = lambda a,b,c: (a+b+c)/3
# print(avg(1,2,3))

