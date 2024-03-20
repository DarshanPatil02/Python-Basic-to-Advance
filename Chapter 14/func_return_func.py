# function return function

def outer_func():
    def inner_func():
        print("Print inside function")
    return inner_func

func = outer_func()
print(func())

def outer_func1():
    def inner_func1():
        print("Print inside function")
    return inner_func1()

func1 = outer_func1()
print(func1)

def outer_func2(msg):
    def inner_func2():
        print(f"Message is {msg}")
    return inner_func2 

func2 = outer_func2('Hello Guys!!!')
print(func2())
