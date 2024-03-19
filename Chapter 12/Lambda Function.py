# lambda function (anonymous function)

def add(a,b):
    return a+b
print(add(2,6))

add_2 = lambda a,b: a+b
print(add_2(2,5))

# mostly lambda function is not assigned to variable
# It is mostly used with build in functions like map, reduce, filter

multipy=lambda a,b : a*b
print(multipy(12,4)) 

# lambda function practice
is_even = lambda a: a%2==0
print(is_even(5))

# last char 
last_char = lambda word: word[-1] 
print(last_char("Darshan"))

# lambda with if else

func = lambda x : True if len(x)>5 else False
print(func("Darshan"))

# or
func1=lambda x: len(x)>5
print(func1("Monday`"))