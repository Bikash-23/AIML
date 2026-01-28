# Polymorphisom:: many forms; multiple function but same name
# Opetarot Overloading : ex- + => add and string_concatetion

# 1. function overriding
# class Employee:
#     def get_designation(self):
#         print("Designation = Employee")
# class Teacher(Employee):
#     def get_designation(self):
#         print("Designation = Teacher")

# t1 = Teacher()
# t1.get_designation()

# 2. Duck Typing
class Teacher():
    def get_designation(self):
        print("Designation = Teacher")
class Accountant():
    def get_designation(self):
        print("Designation = Accountant")

t1 = Teacher()
a1 = Accountant()
t1.get_designation()
a1.get_designation()

