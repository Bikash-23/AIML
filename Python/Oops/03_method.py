# Method::
#     isinstance => it parameter is self ; access the class & instance attribute
#     class => it parameter is cls ; only get the class atrribute ; have decorater : @classmethod
#     static => no copalsary paremeter ; can't access the instance and class attribute ; decoretor : @staticmethod

class Computer:
    ram_type = "SSD"

    def __init__(self,ram,storage):
        self.ram= ram
        self.storage = storage

    @classmethod    
    def get_storage_type(cls):
        print(f"Storae Type: {cls.ram_type}")

    def print_info(self):
        print(f"RAM:{self.ram} & RAM_Storage : {self.storage} & Type: {self.ram_type}")

    @staticmethod
    def calc_discount(price,discount):
        final_price = price - ((discount * price) / 100)
        print(f"Final Price :{final_price}")
lap1 = Computer("16gb","512gb")
# lap1.print_info()
# lap1.get_storage_type()
# Computer.get_storage_type()

lap1.calc_discount(50000,10)

