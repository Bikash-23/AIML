# Inheritance:: Reusing attributes & methods from Parent(Base) class. 

# class Employee:
#     start_time = "10am"
#     end_time = "5pm"

#     def change_time(self,new_end_time):
#         self.end_time = new_end_time
# class Teacher(Employee):
#     def __init__(self,subject):
#         self.subject= subject
# t1 = Teacher("Physics")
# t1.change_time("7pm")

# class AdminStaf(Employee):
#     def __init__(self,role):
#         self.role = role
# class Accountant(AdminStaf):
#     def __init__(self, salary,role):
#         super().__init__(role)
#         self.salry= salary
# staf1 = AdminStaf("Manager")
# print(staf1.role,t1.subject,t1.start_time,t1.end_time)

# inheritance:: 1.single level(Employee -> Teacher)  
# 2. multi level(Employee -> AdminStuff -> Accountant)
# 3.multiple inheritance

# acc1 = Accountant(25000,"CA")
# print(acc1.role,acc1.salry,acc1.start_time)

class Tech:
    def __init__(self,salary):
        self.salary = salary
class Student:
    def __init__(self,gpa):
        self.gpa = gpa
class TA(Tech,Student):
    def __init__(self, salary,gpa,name):
        super().__init__(salary)
        Student.__init__(self,gpa)
        self.name = name

ta1= TA(15000,9.3,"Bikash")

print(ta1.name,ta1.gpa,ta1.salary)