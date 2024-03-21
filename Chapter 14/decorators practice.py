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