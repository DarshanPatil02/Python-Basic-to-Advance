class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name+" "+model_name
    
    def apply_discount(self,num):
        return self.price-((self.price*num)/100)
       

laptop1 = Laptop("HP","au114tx", 63000)
laptop2 = Laptop("Dell","bt185jp", 85000)

print(laptop1.price)
print(laptop1.apply_discount(40))

print(laptop2.price)
print(laptop2.apply_discount(40))
