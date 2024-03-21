# Class method
# Difference between class method and instance method


class Person:
    count_att = 0 # class variable/class attributes
    def __init__(self,f_name,l_name,age):
        Person.count_att+=1
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
    
    @classmethod # In-bulit decorator in class
    def count_instances(cls): # class method and instance method (insted of self used class as first attribute)
        return f"You have create {cls.count_att} instances of {cls.__name__} class"

p1 = Person("Rohit","Sharma", 42)
p2 = Person("Surya","Yadav", 38)

print(Person.count_instances())