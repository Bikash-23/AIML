'''
Type Conversion - >(compactible)
int -> float
float -> int
int -> bool
srting -> int(not everytime) : possible t&c -> 'abc123' -> int not possible but "123" -> int(123) possible'''

# -> Type conversion (implicit -> done by Python interpreter) :: ex_ float+int

# a= 10
# b= 2
# print(type(a/b))

ans1 = 5 +10.0
print(ans1)

# -> casting -> explicit:: not automatic

ans2 = int(5 +10.0)
print(ans2)

print(type(int("123")))

val1 = 0
val2 = 5
print(bool(val1) , bool(val2))
print(int(False), float(True))