# *operators
# *args

def total_in_x(x,*args): # in this case first x is as parameter and remaining are tuple
    total=x
    for i in args:
        total+=i
    return total

total_in_x(5,1,2,3,4,5)

# args as arguement

def multiply_function(*args):
    multiply=1
    for i in args:
        multiply*=i
    return multiply

# lets create a list nums
nums = [2,5,6]
# if we pass list to function it will return an unexpected output i.e., list
print(multiply_function(nums))
# to get a required output put a command as follow
print(multiply_function(*nums)) # it will unpack list given

# function with all parameters
# PADK
def all_par_func(name,*args,last_name="unknown",**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

print(all_par_func("Darshan",(1,2,3),a="Joy",b="fun"))