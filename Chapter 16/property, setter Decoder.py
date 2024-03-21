# We have discuss three problems in existing
# Now we will solve this problem using getter,setter decorator

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = price 
        self.complete_specification=f"{self.brand} {self.model_name} and price is {self._price}"
    
    def make_a_call(self,phone_number):
        print(f'Calling {phone_number}')

    def full_name(self):
        return f"{self.brand} {self.model_name}"

phone1 = Phone("Nokia",1.0,-1500) 

print(phone1.brand)
print(phone1.model_name)
phone1._price = -500
print(phone1._price)
print(phone1.complete_specification)

# In above class we have 3 problems
# 1) user can put price of phone as negative like (phone1 = Phone("Nokia",1.0,-1500) 
# 2) if user change price of phone it is seen in phone1.price but not seen in phone.complete specification
# 3) As user also change price of phone to negative like (phone1._price = -500)
# Solve the above problem

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)  # Solution of problem 1
        # OR 
        # if price<0:
        #     self._price=0
        # else:
        #     self._price = price            
    def complete_specification(self): # SOlution of problem 2 which is instead of creating it in first func make it seperate
        return f"{self.brand} {self.model_name}"

    # getter = property decorator and setter= setter
    @property # decorator    # Solution of problem 3. Here condition is first we need to use getter and then use setter
    def price(self):
        return self._price
    
    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)


    def make_a_call(self,phone_number):
        print(f'Calling {phone_number}')

    def full_name(self):
        return f"{self.brand} {self.model_name}"

phone1 = Phone("Nokia",1.0,-1500) 

print(phone1.brand)
print(phone1.model_name)
print(phone1._price)
phone1.price = -500
print(phone1._price)
print(phone1.complete_specification())

phone2 = Phone("Oneplus",11,60000) 

print(phone2.brand)
print(phone2.model_name)
print(phone2._price)
phone2.price = 65000
print(phone2._price)
print(phone2.complete_specification())
