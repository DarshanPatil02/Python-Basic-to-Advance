# define a function
# input
# num, iterable(tuple, list)containing numbers as args
# example
# nums [1,2,3] to power(3, "nums)
# output
# list ---> [1, 8, 27) 1
# if user didn't pass any args then give a user a message That you didn't pass args
# else
# return list

# NOTE use list comprehension

def power_num (num,*args):
    if args:
        return ([i**num for i in args])
    else:
        return ("you didn't pass args")


numbers = [1,2,3]
print(power_num(3,*numbers))

print(power_num(3))