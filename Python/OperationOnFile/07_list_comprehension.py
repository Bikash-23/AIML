squares = []
# for i in range(6):
#     squares.append(i*i)

# print(squares)

# ----------list_comprehensions----------
# sq =[i*i for i in range(6)]
# print(sq)

sq =[i*i for i in range(6) if i%2 != 0]
print(sq)

# nums = [-2,-3,-4,3,4,-2]
# nums = [0 if val<0 else val for val in nums]
# print(nums)

