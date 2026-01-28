# Attributes::
#     class -> belong to class -> common 
#     instance -> belong to object

class Student:
    college_name = "ABC college"
    PI = 3.1

    def __init__(self,name,cgpa):
        self.name= name
        self.cgpa = cgpa
        self.PI = 3.14 # heigher priority than class atrribute
        
stu1 = Student("Bikash",9.0)

print(stu1.college_name,stu1.name,stu1.cgpa,stu1.PI)