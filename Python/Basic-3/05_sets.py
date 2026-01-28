# Sets:: collecton of unique elements
# sets:: mutable & unorded but element in sets:: immutable

# set1 = {1,2,3,2,2,4}
# set1.add(5)
# print(set1)
# print(type(set1))

# set2 = {}
# print(type(set2))

# set3 = set()
# print(type(set3))

# ----------method----------

# s.add(val)::add a val
# s.remove(val) :: remove Val
# s.clear() :: empties the set    
# s.pop() :: remove a random Val
# s.union(set2) :: return new Union
# s.intersection(set2) :: return new intersection

set1= {1,2,2,3,5,4}
# set1.add(6)
# set1.remove(2)
# set1.pop()
# print(set1)

set2 = {4,5,6,7,8,9}
# print(set1.union(set2))
print(set1.intersection(set2))