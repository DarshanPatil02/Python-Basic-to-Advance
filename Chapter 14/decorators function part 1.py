# Decoraters - enhance the functionality of other function
# used for decorator

def decorator_func(any_function):
    def wrapper_function():
        print("This is awesome function")
        any_function()
    return wrapper_function

# Below function print "func 1" but i also want that it should print "This is awesome function"
def func1():
    print("This is function 1")

def func2():
    print("This is function 2")
# first assign variable
v1 = decorator_func(func1)
print(v1())

# Use decorated function without using above style
def decorator_function(any_function):
    def wrapper_function():
        print("This is awesome function")
        any_function()
    return wrapper_function

@decorator_function
def function1():
    print("This is function 1")

@decorator_func
def function2():
    print("This is function 2")

print(function1())
print(function2())