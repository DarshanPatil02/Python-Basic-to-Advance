'''
In decorators practice we have seen in last example that in case 
where we have to pass only int in function so we make a decorator function that identify input is correct or not
but i case if we need to pass 'str' or any other datatype we need to create again other decorator func
to avoid this we will do decorator with arguement 
'''

from functools import wraps

def only_datatype_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper_func(*args,**kwargs):
            if [type(i)==data_type for i in args]:
                return function(*args,**kwargs)
            print("Invalid arguement")
        return wrapper_func
    return decorator

@only_datatype_allow(str)
def string_join(*args):
    string=''
    for arg in args:
        string+=arg
    return string

print(string_join("abc","efg","ijk","mno"))

