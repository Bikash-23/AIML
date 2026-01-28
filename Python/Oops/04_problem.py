class Product:
    count = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product.count+=1

    @staticmethod
    def cal_discount(price,percentage):
        final_price = price -(price*percentage/100)
        return final_price   
    
laptop = Product("Laptop",40000)
phone = Product("Phone",15000)
prn = Product("Pen",10)

print(laptop.name)
print(Product.count)
res = laptop.cal_discount(laptop.price,10)
print(res)
