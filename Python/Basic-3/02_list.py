# Lists:: mutable sequence of value 

mark = [99,89,100,65,92]
# print(mark)
# print(len(mark))
# mark[2] = 92
# print(mark[2])
# print(type(mark))

# ---------slicing-------

# print(mark[2:5])
# print(mark[2:len(mark)])
# print(mark[2:])
# print(mark[-4:-1])

# -----------Methods----------
# list.append(val) :: add one element at the end 
# list.insert(idx,val) :: insert element at idx 
# list.sort() :: arranges in increaing order
# list.reverse() :: reverse order

# mark.append(45)
# print(mark)

# mark.insert(3,67)
# print(mark)

# mark.sort()
# mark.sort(reverse=True)
# print(mark)

# mark.reverse()
# print(mark)

# -----------loop-----------
# for val in mark:
#     print(val)
idx = 0
for val in mark:
    if(val == 100):
        print(idx)
        break
    idx+=1