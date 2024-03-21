# How to create a class
# What is class
# what is init method, constructor
# What are attributes, instance variable
# How to create our object

class Person:
    def __init__(self, first_name,last_name,age):  # __init__ is method to constructor class and 
                                                   # it is syntax and self is call and it is must to call object
                                                   # self represents object
        #instance variable
        print("init method / constructor get called")
        self.first_name = first_name #instance variable
        self.last_name = last_name  #instance variable
        self.age = age  #instance variable

p1 = Person("Darshan","patil", 21)
p2 = Person("Ajit","Kapoor", 19)

print(p1.first_name)
print(p2.first_name)