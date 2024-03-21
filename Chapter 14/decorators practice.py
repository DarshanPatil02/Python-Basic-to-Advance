# define a function which takes 2 number as input and return output as
# Output --->
# You are calling a add function
# This function takes two numbers as parameters and return their sum

from functools import wraps
def decorated_func(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):     
        print(f"You are calling {any_function.__name__} function")
        print(any_function.__doc__)
        return any_function(*args,**kwargs)
    return wrapper_function

@decorated_func
def add(a,b):
    """This function takes two numbers as parameters and return their sum"""
    return a+b

print(add(12,5))

@decorated_func
def multiply(a,b):
    """This function takes two numbers as parameters and return their product"""
    return a*b

print(multiply(4,3))

# Decorator practice
#case 1
def add_all(*args):
    total=0
    for i in args:
        total+=i
    return total
print(add_all(1,2,3,4,5,6)) # It is not showing error but if
print(add_all(1,2,3,4,5,6,[5,6,8])) # It is showing error

# So create a decorator function that only takes int datatype

def int_only(function):
    def wrapper_func(*args,**kwargs):
        data_type = []
        for arg in args:
            data_type.append(type(arg)==int)
        if all(data_type):
                return function(*args,**kwargs)
        else:
            print("Invalid arguement")
    return wrapper_func

@int_only
def add_all(*args):
    total=0
    for i in args:
        total+=i
    return total
print(add_all(1,2,3,4,5,6)) # It is not showing error but if
print(add_all(1,2,3,4,5,6,[5,6,8])) # It is showing error

# OR 
def int_only(function):
    def wrapper_func(*args,**kwargs):
        if all([type(arg)==int for arg in args]):
                return function(*args,**kwargs)
        print("Invalid arguement")
    return wrapper_func

@int_only
def add_all(*args):
    total=0
    for i in args:
        total+=i
    return total
print(add_all(1,2,3,4,5,6)) # It is not showing error but if
print(add_all(1,2,3,4,5,6,[5,6,8])) # It is showing error

