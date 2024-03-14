# *operators
# *args

def all_total(*args):
    total = 0
    for i in args:
        total+=i
    return(total)

print(all_total(1,2,5,7,8))


# *args with normal parameters

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