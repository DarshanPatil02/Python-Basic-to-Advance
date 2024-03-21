# Instance or object
# Method

l = [1,2,3,4] # l is instance
l.pop() # pop is method

class Person():
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above_18(self):
        if self.age>18:
            return "Yes"
        return "No"

p1 = Person("David","Warner",45)
p2 = Person("Rohit","Sharma",42)
p3 = Person("Sachin", "Tendulkar", 15)

print(p1.full_name())
print(p2.full_name())

print(p1.is_above_18())
print(p3.is_above_18())