# Create a laptop class with attributes like brand name, model name, price
# Create two objects/ instance of your laptop class

class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name+" "+model_name


laptop1 = Laptop("HP","au114tx", 63000)
laptop2 = Laptop("Dell","bt185jp", 85000)

print(laptop1.model_name)
print(laptop2.price)
print(laptop1.laptop_name)

# OR  (Insted of self used laptop)
class Laptop:
    def __init__(laptop,brand_name,model_name,price):
        laptop.brand_name = brand_name
        laptop.model_name = model_name
        laptop.price = price
        laptop.laptop_name = brand_name+" "+model_name
        

laptop1 = Laptop("HP","au114tx", 63000)
laptop2 = Laptop("Dell","bt185jp", 85000)

print(laptop1.model_name)
print(laptop2.price)
print(laptop1.laptop_name)