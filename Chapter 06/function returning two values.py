# function returning two values in the form of tuple
def func(num1,num2):
    add = num1+num2
    multiply = num1*num2
    return add, multiply

print(func(5,12)) # It return two values in the form of tuple

# to obtain that values individually
addition,multiplication = func(5,12)
print(addition)
print(multiplication)
