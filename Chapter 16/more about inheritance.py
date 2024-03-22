# Can we derive more than 1 class from base class ?
# multilevel inheritance
# method resolution order
# method overriding
# isinstance() issubclass()

# Can we derive more than 1 class from base class ?
# Ans: Yes


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

# Smartphone which is first class
class Smart_Phone(Phone):  
    def __init__(self,brand,model_name,price,ram,rom, android_version):
        super().__init__(brand,model_name,price)
        self.ram = ram 
        self.rom = rom
        self.android = android_version
    
Smart_Phone1 = Smart_Phone("Oneplus",12,65000,'16GB',"256GB",12)
print(Smart_Phone1.full_name(), f"and price is {Smart_Phone1._price}")

# Smartphone_2 which is second class
class Smart_Phone_2(Phone):  
    def __init__(self,brand,model_name,price,ram,rom, android_version,rear_camera,back_camera):
        super().__init__(brand,model_name,price)
        self.ram = ram 
        self.rom = rom
        self.android = android_version
        self.rear_camera = rear_camera
        self.back_camera = back_camera

Smart_Phone2 = Smart_Phone_2("Oneplus",12,65000,'16GB',"256GB",12,'64MP',"108MP")
print(Smart_Phone2.full_name(), f"and price is {Smart_Phone1._price} and having rear and back camera {Smart_Phone2.rear_camera} and {Smart_Phone2.back_camera} respectively")

# multilevel inheritance
class FlagshipPhone(Smart_Phone):
    def __init__(self, brand, model_name, price, ram, rom, android_version,rear_camera,back_camera,OS):
        super().__init__(brand, model_name, price, ram, rom, android_version)
        self.rear_camera = rear_camera
        self.back_camera = back_camera
        self.OS = OS

        
FlagshipPhone1 = FlagshipPhone("Oneplus",12,65000,'16GB',"256GB",12,'64MP',"108MP","Oxygen")
print(f"This is Flagship Phone {FlagshipPhone1.full_name()} and price is {FlagshipPhone1._price} and having rear and back camera {FlagshipPhone1.rear_camera} and {FlagshipPhone1.back_camera} respectively and Operating system is {FlagshipPhone1.OS}")


# method resolution order
print(FlagshipPhone1.full_name())
# Every class has method resolution
print(help(FlagshipPhone1)) # In output we can see method resolution which means  that what is flow of our code
"""
Method resolution order:
 |      FlagshipPhone
 |      Smart_Phone
 |      Phone
 |      builtins.object
 |"""
# In this FlashipPhone1 case python first call FlagshipPhone then it call Smart_Phone and 
# then Phone and builtins.object are already in python to create class


# Method override
class FlagshipPhone(Smart_Phone):
    def __init__(self, brand, model_name, price, ram, rom, android_version,rear_camera,back_camera,OS):
        super().__init__(brand, model_name, price, ram, rom, android_version)
        self.rear_camera = rear_camera
        self.back_camera = back_camera
        self.OS = OS
    
    def full_name(self): # this function override Phone.full_name function
        return f"This is Flagship Phone {FlagshipPhone1.full_name()} and price is {FlagshipPhone1._price} and Operating system is {FlagshipPhone1.OS}"

        
FlagshipPhone2 = FlagshipPhone("Oneplus",12,65000,'16GB',"256GB",12,'64MP',"108MP","Oxygen")
print(FlagshipPhone2.full_name())

# isinstance() issubclass() ----> These are two bulit-in function
# isinstance  ---> Check wheather this object/instance belongs to this class or not
# Syntax ---> It will take 2 arguement, 1-->object and 2-->class
Oneplus_10 = Smart_Phone("Oneplus",10,45000,'8GB',"128GB",9)
print(isinstance(Oneplus_10,Smart_Phone)) # --> o/p True because Oneplus_10 belongs to Smart_Phone class
print(isinstance(Oneplus_10,FlagshipPhone)) # --> o/p False because Oneplus_10 not belongs to FlagshipPhone class

Oneplus_12 = FlagshipPhone("Oneplus",12,65000,'16GB',"256GB",12,'64MP',"108MP","Oxygen")
print(isinstance(Oneplus_12,FlagshipPhone)) # --> o/p True because Oneplus_12 belongs to FlagshipPhone class
print(isinstance(Oneplus_12,Smart_Phone)) # --> o/p True because Oneplus_12 belongs to Smart_Phone class which is parent class of FlagshipPhone class

# issubclass
# Check wheather first argument class is subclass of second arguement
print(issubclass(Smart_Phone,Phone)) #--> True because Smart_Phone is subclass of phone
print(issubclass(Smart_Phone,FlagshipPhone)) #--> False because Smart_Phone is not subclass of FlagshipPhone, FlagshipPhone is subclass of Smart_phone
print(issubclass(FlagshipPhone,Smart_Phone)) #--> False because Smart_Phone is not subclass of FlagshipPhone, FlagshipPhone is subclass of Smart_phone
