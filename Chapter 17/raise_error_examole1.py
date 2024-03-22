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

goat1 = Goat("Lambchop","kiko goat")
print(goat1.sound())
