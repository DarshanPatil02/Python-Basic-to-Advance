# In part 1 if we pass follwing argument then it show error

def decorator_function(any_function):
    def wrapper_function():
        print("This is awesome function")
        any_function()
    return wrapper_function

@decorator_function
def function1():
    print(f"This is function 1")
function1()


# But if pass following command then function will show error

def decorator_function(any_function):
    def wrapper_function():
        print("This is awesome function")
        any_function()
    return wrapper_function

@decorator_function
def function1(num):
    print(f"This is function 1 with number {num}")
function1(3)


# Then follow this syntax
def decorator_function(any_function):
    def wrapper_function(*args,**kwargs): # by adding *args and **kwargs
        print("This is awesome function")
        return any_function(*args,**kwargs) # Here also same changes and also return the function
    return wrapper_function

@decorator_function
def function1(num):
    print(f"This is function 1 with number {num}")
function1(3)

# Example 2
def decorator_function(any_function):
    def wrapper_function(*args,**kwargs): # by adding *args and **kwargs
        print("This is awesome function")
        return any_function(*args,**kwargs) # Here also same changes and also return the function
    return wrapper_function

@decorator_function
def function1(a,b):
    return a+b
function1(3,2)

