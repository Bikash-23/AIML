# OOPS Pillars
# 1. Encapsulation
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism

# Encapsulation:: Wrapping data & function into single unit ; 
# data hiding :: public(inside class+outside class),
# protected(class+subclass) , private(inside the class)

class BankAccount:
    def __init__(self,name,balance,accno):
        self.name  = name #public
        self._balance = balance #Protected
        self.__accno = accno #private
    def get_accno(self): #getter
        return self.__accno
    def change_accno(self,newAccNo): #setter
        self.__accno = newAccNo

acc1 = BankAccount("Ravi Kisan",100000,232323)

print(acc1.name)
# print(acc1.get_accno())
# acc1.change_accno(171717)
# print(acc1.get_accno())
# print(acc1._BankAccount__accno) #another way to get private info
# print(acc1._balance) #another way to get protected info

# in python ,data hiding is by convension not stricly applicable in python there is no true protected or private 