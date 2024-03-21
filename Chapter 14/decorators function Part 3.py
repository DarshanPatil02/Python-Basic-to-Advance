def decorator_function1(any_function):
    def wrapper_function(*args,**kwargs):
        """This is wrapper function"""
        print("This is awesome function")
        return any_function(*args,**kwargs)
    return wrapper_function

@decorator_function1
def add(a,b):
    """This is add function"""
    return a+b

print(add.__doc__,"\n",add.__name__) # Actually it is add function but shown wrapper function 
# To tackle this problem use following solution

from functools import wraps
def decorator_function_2(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        """This is wrapper function"""
        print("This is awesome function")
        return any_function()
    return wrapper_function

def add_numbers(a,b):
    """This is add function"""
    return a+b

print(add_numbers.__doc__)
print(add_numbers.__name__)