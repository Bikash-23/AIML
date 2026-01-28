# Tuples:: immtable sequence of values

num = (1,2,3,4,5,2)
# print(num)
# print(type(num))
# print(len(num))
# print(num[2])
# print(num[:])
# print(num[:2])
# print(num[2:])
# print(num[1:3])


# single value tuple is invalid
# tup = (1)
# print(type(tup))

# to print single value tuples
# tup= (1,)
# print(type(tup))
# print(tup)

# -----------method--------
sum = 0
for ele in num:
    sum +=ele
print(sum)

print(num.index(2))
print(num.count(2))