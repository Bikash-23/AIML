# Question-1
# class BankAccount:
#     def __init__(self,account_number,owner_name,balance):
#         self.account_number = account_number
#         self.owner_name = owner_name
#         self.balance = balance
#     def deposite(self,depo):
#         self.balance += depo
#         return self.balance
#     def withdraw(self,withd):
#         self.balance -=withd
#     def check_balnce(self):
#         return self.balance
    
# ac1 = BankAccount(2121,"Bikash",10000)
# # print(ac1.balance)
# # print(ac1.deposite(100))
# ac1.withdraw(100)
# ac1.deposite(500)
# print(ac1.check_balnce())

# Question-2
# class Book:
#     def __init__(self,title,author,list_of_reviews = None):
#         self.title = title
#         self.author = author
#         self.list_of_reviews = list_of_reviews if list_of_reviews else []
#     def add_review(self,newReview):
#         self.list_of_reviews.append(newReview)
#     def count_reviews(self):
#         return len(self.list_of_reviews)
#     def display_reviews(self):
#         for i in self.list_of_reviews:
#             print(i)

# b1 = Book("Hello","Bikash Pari",["ravi","raja","ramu"])
# print(b1.count_reviews())
# b1.display_reviews()
# b1.add_review("bik")
# print(b1.author, b1.title)
# b1.display_reviews()

# Question-3
# class Student:
#     def __init__(self, name, roll_no, marks):
#         self.set_name(name)
#         self.set_roll_no(roll_no)
#         self.set_marks(marks)

#     def get_name(self):  # getter
#         return self._name

#     def set_name(self, name):  # setter
#         if name.strip() == "":
#             raise ValueError("Name can't be empty")
#         self._name = name

#     def get_roll_no(self):
#         return self._roll_no

#     def set_roll_no(self, roll_no):
#         if roll_no < 1 or roll_no > 100:
#             raise ValueError("Roll number must be between 1 and 100")
#         self._roll_no = roll_no  # fixed typo

#     def get_marks(self):
#         return self._marks

#     def set_marks(self, marks):
#         if marks < 0:
#             raise ValueError("Marks can't be negative!")
#         self._marks = marks


# # Object creation outside the class
# s1 = Student("Bikash", 67, 100)
# # print(s1.get_name())   
# # print(s1.get_roll_no())  
# # print(s1.get_marks())    

# # s1.set_name("bik")
# # print(s1.get_name())  

# Question-4
# class Shape:
#     def area(self):
#         pass
# class Circle(Shape):
#     def area(self):
#         print("Circle area")
# class Rectangle(Shape):
#     def area(self):
#         print("Rectangle Area")
# class Triangle(Shape):
#     def area(self):
#         print("Triangle Area")  

# c1 = Circle()
# c1.area()
# r1= Rectangle()
# r1.area()
# t1 = Triangle()
# t1.area()

# Question-5
# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
# class Bike(Vehicle):
#     def engine_cc(self,cc):
#         self.cc = cc
#         print(self.cc)
# class Car(Vehicle):
#     def no_seat(self,seat):
#         self.seat = seat
#         print(self.seat)
# b1 = Bike("honda","sine_sp")
# b1.engine_cc("125cc")
# c1 = Car("BMW","123_3")
# c1.no_seat(6)

# Question-6
# class Employee:
#     def calculate_salary(self,salary):
#         pass
# class Intern(Employee):
#     def calculate_salary(self,salary):
#         print(f"Intern Salary:{salary}")
# class FullTimeEmployee(Employee):
#     def calculate_salary(self,salary):
#         print(f"FullTimeEmployee Salary:{salary}")
# class ContractEmployee(Employee):
#     def calculate_salary(self,salary):
#         print(f"ContractEmployee salary:{salary}")

# i1 =Intern()
# i1.calculate_salary(10000)
# fte1 = FullTimeEmployee()
# fte1.calculate_salary(300000)
# ce1 = ContractEmployee()
# ce1.calculate_salary(50000)

# Question-7
# class Person:
#     def __init__(self,name,age = None,address=None):
#         self.name = name
#         self.age = age
#         self.address = address
#     def dispaly(self):
#         print("Name:",self.name)
#         if self.age is not None:
#             print("Age:",self.age)
#         if self.address is not None:
#             print("Address:",self.address)
#         print("----------------")
    
# p1  = Person("Biaksh")
# p1.dispaly()
# p2 = Person("Bikash",22)
# p2.dispaly()
# p3 = Person("Bikash",22,"Kolkata")
# p3.dispaly()

# Question-8
# class Player:
#     player_count = 0
#     def __init__(self,name,level):
#         self.name = name
#         self.level = level
#         Player.player_count +=1

# p1 =Player("Bikash","jr.")
# p2 =Player("Ravi","jr.")
# p3 =Player("ray","sr.")
# p4 =Player("kk","sr.")
# print(p1.name)
# print(p1.player_count)

# Question-9
# class Herbivore:
#     def info(self):
#         print("Hervivore")
# class Carnivore:
#     def info(self):
#         print("Carnivore")  
# class Omnivore:
#     def info(self):
#         print("Omnivore")
# class Bear(Herbivore,Carnivore,Omnivore):
#     def __init__(self):
#         print("Bear!")
#         # Herbivore.info(self)
#         # Carnivore.info(self)
#         # Omnivore.info(self)

# b1 = Bear()
# b1.info()

# Question-10