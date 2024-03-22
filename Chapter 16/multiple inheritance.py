# Multiple Inheritance

class A:
    def class_a_method(self):
        return "I'am just a class A method"
    
    def hello(self):
        return "Hello from class A"
        
class B:
    def class_b_method(self):
        return "I'am just a class B method"
    
    def hello(self):
        return "Hello from class B"
    
class C(A,B):
    pass

isinstance_c = C()
print(isinstance_c.class_a_method())
print(isinstance_c.class_b_method()) 
print(isinstance_c.hello())  # here class A and Class B also has hello function but as per method resolution it will A
print(help(isinstance_c))