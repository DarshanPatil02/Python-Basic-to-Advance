class Phone: # base class/ parent class
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = price 
        self.complete_specification=f"{self.brand} {self.model_name} and price is {self._price}"
    
    def make_a_call(self,phone_number):
        print(f'Calling {phone_number}')

    def full_name(self):
        return f"{self.brand} {self.model_name}"

# Smartphone
class Smart_Phone:
    def __init__(self,brand,model_name,price,ram,rom, android_version):
        self.brand = brand
        self.model_name = model_name
        self._price = price
        self.ram = ram 
        self.rom = rom
        self.android = android_version
    
    def make_a_call(self,phone_number):
        print(f'Calling {phone_number}')

    def full_name(self):
        return f"{self.brand} {self.model_name}"


phone1 = Phone("Nokia", 1.0,1500)
Smart_Phone1 = Smart_Phone("Oneplus","12",65000,"12GB",'256GB',14)
print(phone1.full_name())
print(Smart_Phone1.full_name())

# In above case we need to write our code again and agian for phone also and smartphone alse
# So can we do that, those specification are in phone we not need to write. This is done by inheritance

class Phone: # base class/ parent class
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = price 
        self.complete_specification=f"{self.brand} {self.model_name} and price is {self._price}"
    
    def make_a_call(self,phone_number):
        print(f'Calling {phone_number}')

    def full_name(self):
        return f"{self.brand} {self.model_name}"

# Smartphone 
class Smart_Phone(Phone):  # By adding parent class here  #This is child class/Derived class
    def __init__(self,brand,model_name,price,ram,rom, android_version):
        # To add all data from parent we can done by two ways
        # First way Uncommon way
        # Phone.__init__(self,brand,model_name,price)
        # Second Way common way
        super().__init__(brand,model_name,price)
        self.ram = ram 
        self.rom = rom
        self.android = android_version
    
phone1 = Phone("Nokia", 1.0,1500)
Smart_Phone1 = Smart_Phone("Oneplus",12,65000,'16GB',"256GB",12)
print(phone1.full_name())
print(Smart_Phone1.full_name(), f"and price is {Smart_Phone1._price}")

