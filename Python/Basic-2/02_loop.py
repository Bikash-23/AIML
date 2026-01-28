# loop:
#     while loop
#     for loop

# -------------while-loop------------------------

# i = 0
# while(i <5):
#     print("Hello")
#     i+=1

# num = 0
# while(num<5):
#     print(num+1)
#     num+=1

# num = 5
# while(num>0):
#     print(num)
#     num-=1

# number = int(input("Enter Num: "))

# i = 1
# while(i<=10):
#     print(number*i)
#     i+=1

# ---------------------break-continue--------------

# break :: terminate loop 
# continue :: to skip current iteration

# i = 1
# while(i<=10):
#     if(i%6 == 0):
#         break
#     print(i)
#     i+=1
# print('outside loop i:',i)

# i = 0
# while(i<10):
#     i+=1
#     if(i%6 == 0):
#         print('This time i:',i) #print the continue part number
#         continue
#     print(i) # skip due to continue
# print("outside loop i:",i) # outside loop 


# num = 0
# while(num<10):
#     num+=1
#     if(num % 2 == 0):
#         continue
#     print("Odd:",num)


# ----------------for-loop--------------------------

# in :: member operator

sting = "hello"

# if 'x' in sting:
#     print("o have in string")
# else:
#     print("haven't exist")

# for var in sting:
#     print(var)

# range(start, stop , step) :: start & step are optional and have defult value of 0 and +=1
# range(n) :: 0 to n-1 

# for i in range(5):
#     print(i)

# for i in range(1,10,2): 
#     print(i)



word = "artificial intelligence"

# count the number of i's
# count = 0
# for ch in word:
#    if(ch == 'i'):
#       count+=1

# print(count)

# count vowel
# count = 0
# for ch in word:
#    if(ch == 'a' or ch == 'e' or ch == 'i' or ch =='o' or ch =='u'):
#       count+=1

# print(count)

# sum of n natural number

n = int(input("Enter Number:"))
# sum = 0
# for i in range(1,n+1):
#     sum+=i

# print("SUM: ",sum)

sum = (n*(n+1))/2
print("SUM: ",sum)
