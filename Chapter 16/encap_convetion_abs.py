# Encapsulation: Bundling data and methods into a single unit, hiding internal state from the outside world.
# Abstraction: Hiding complex implementation details and exposing only essential features.
# Some special naming convention:---->_name to tell this is private variable
# Name Magling: Compiler technique to create unique names (like __name) for entities, typically used to avoid naming conflicts in namespaces or classes.
# __name__ ==> dunder/magic methods

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = price # to tell this is private variable to avoid conflict but it is changeable
    
    def make_a_call(self,phone_number):
        print(f'Calling {phone_number}')

    def full_name(self):
        return f"{self.brand} {self.model_name}"

phone1 = Phone("Nokia",1.0,1500)
phone2 = Phone("Samsung","J7",1500)

print(phone1._price)  

# Name Magling example
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.__price = price # name magling, Python automatically change it's name
    
    def make_a_call(self,phone_number):
        print(f'Calling {phone_number}')

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
phone1 = Phone("Nokia",1.0,2500)
phone2 = Phone("Samsung","J7",25000)

#print(phone1.__price)  # It is showing error even we given this name
print(phone1.__dict__)  # In this you can see new name decided by python
print(phone1._Phone__price)
