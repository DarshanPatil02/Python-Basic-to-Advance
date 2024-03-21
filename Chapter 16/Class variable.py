# Define a class Circle and define a function area and circumference inside it

class Circle:
    import math
    pi = math.pi  # this is class variable 
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return round(Circle.pi*self.radius**2,2)  # because of class variable it is call as Class_name.variable---> Circle.pi
    
    def circumference(self):
        import math
        return round(Circle.pi*self.radius*2,2)
    
c1 = Circle(5)
print(c1.radius)    
print(c1.area())
print(c1.circumference())

