# raise error
# NotImplementedError
# also called as Abstract error in Java

def add(a,b):
    return a+b
print(add(2,5))

# In above example if we pass string then it will not add then it will join
print(add('2','5'))
# But we don't want this, so therefore we raise a custom error

def add(a,b):
    if (type(a)==int and type(b)==int):
        return a+b
    raise TypeError("Oops! You pass wrong datatype to function")
print(add(2,5))
print(add('2','5'))

# Example1
# Notimplemented error
# abstract method

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        return "This is animal sound"

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

doggy = Dog("bonny",'pug')
print(doggy.sound())

# Case 1: if we change animal sound to "meao meao"
class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        return "meao meao"

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

doggy = Dog("bonny",'pug')
print(doggy.sound()) # o/p is meao meao
# But this is wrong. Here we want that whatever subclasses from animal should define sound otherwise raise error

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        raise NotImplementedError("You have to define this method in subclasses")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    
    def sound(self):
        return "bhow bhow"

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return "meao meao"

class Goat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

doggy = Dog("bonny",'pug')
print(doggy.sound())

goat1 = Goat("Lily","goat_breed")
print(goat1.sound())
