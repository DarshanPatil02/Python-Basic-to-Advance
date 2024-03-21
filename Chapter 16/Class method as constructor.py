# Class method as constructor
class Person():
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    @classmethod
    def from_string(cls,string):
        f_name,l_name,age = string.split(",")
        return cls(f_name,l_name,age)
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above_18(self):
        if self.age>18:
            return "Yes"
        return "No"

# Normal way to add attributes
p1 = Person("David","Warner",45)
p2 = Person("Rohit","Sharma",42)

# Our own way to add attributes by using function define by us ---> "from string"
p3 = Person.from_string("Sachin, Tendulkar, 15")

print(p3.first_name)