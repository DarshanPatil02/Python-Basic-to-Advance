# raise_error_example2

class Mobile:
    def __init__(self,name):
        self.name =name

class Mobile_Store:
    def __init__(self):
        self.mobiles = []
        
    def add_mobiles(self,new_mobile):
        self.mobiles.append(new_mobile)

oneplus = Mobile("Oneplus 9 Pro")
samsung = "Samsung galaxy s8"
mobo_store = Mobile_Store()

print(mobo_store.mobiles) # here we getting empty list
# Adding new phone
mobo_store.add_mobiles(samsung)
print(mobo_store.mobiles) # here we getting list with 1 element 
# here element is one string but we want object only in mobile class like oneplus
# So we can do it isinstance

class Mobile:
    def __init__(self,name):
        self.name = name
    
class Mobile_Store:
    def __init__(self):
        self.mobiles = []

    def add_mobiles(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError("New mobile should be object of Mobile class")


oneplus = Mobile("Oneplus 10 Pro")
samsung = "Samsung galaxy s12"
mobile_store = Mobile_Store()

print(mobile_store.mobiles) # here we getting empty list
# Adding new phone
mobile_store.add_mobiles(oneplus)
mobile_store.add_mobiles(samsung) # here custom error will raise
mobo_phone = mobo_store.mobiles
print(mobile_store.mobiles[0].name) 
