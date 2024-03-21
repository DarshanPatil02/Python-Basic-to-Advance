# Define a function which gives how much time required to run a function
import time
from functools import wraps

def calculate_time(any_function):
    @wraps(any_function)
    def wrapper_func(*args,**kwargs):
        print(f"Executing...{any_function.__name__}")
        t1 = time.time()
        returned_value = any_function(*args,**kwargs)
        t2=time.time()
        t = t2-t1
        print(f"This function took {t} sec to run")
        return returned_value
    return wrapper_func

@calculate_time
def square_finder(n):
    l = [f"Square of {i} is {i**2}" for i in range(1,n+1)]
    for i in l:
        print( i)
print(square_finder(1000))
