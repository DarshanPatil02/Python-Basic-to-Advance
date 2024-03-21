# Static method in class is a function in class which not requied self or class arguments
# It is seperate but it is link with class by some logic

class Person():
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    # Static Method
    @ staticmethod
    def static_func():
        print("Hello this is static function!!")
        
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

print(Person.static_func())