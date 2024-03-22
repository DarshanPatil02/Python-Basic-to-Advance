# special method/ magic method/ dunder method
# operator overloading
# polymorphism
"""
The word "polymorphism" means "many forms", and in programming it refers to 
methods/functions/operators with the same name that can be executed on many objects or classes.
"""
# E.g:- len function in python can used with list, str, tuple, dict ---> this is called as polymorphism

class Phone: # base class/ parent class
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = price 
    
    def phone_name(self):
        return f"{self.brand} {self.model_name}"
l = [1,2,3]
print(l) # while we print list l it show a well formed list list is also an class in python

my_phone = Phone("Nokia",2.0, 1500)
print(my_phone) # but while we print my_phone which is also a class but not show good readable o/p it just show class and location

# To make our phone class like list class by using dunder method
 
class Phone: # base class/ parent class
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price 
    
    def phone_name(self):
        return f"{self.brand} {self.model_name}"
    
    # two dender method are used for good o/p
    # 1) str and 2) repr(representation)
    # You can put any dender method str is used by normal user while repr is used by python developer

    def __str__(self) -> str:
        return f"{self.brand} {self.model_name} and price is {self._price}"
    
    def __repr__(self) -> str:
        return f"Phone ('{self.brand}', '{self.model_name}', '{self._price}')"
    
    def __len__(self):
        return(len(self.phone_name))
    
    # overloading
    def __add__(self,other):
        return self.price+other.price

my_phone1 = Phone("Nokia",2.0, 1500) # by default it will call first which is str
print(my_phone.__repr__()) 
my_phone2 = Phone("Nokia",5.0, 2500) # by default it will call first which is str

print(my_phone1+my_phone2)