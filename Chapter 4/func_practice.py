# function Practice

def last_char(name):
    return name[-1]

print(last_char("Darshan"))


def odd_even(num):
    num = int(num)
    if num%2==0:
        return ("Number is even")
    else:
        return ("Number is odd")

print(odd_even(25))

# OR based in DRY (Don't Repeate Yourself) principle

def odd_even_check(num):
    num = int(num)
    if num%2==0:
        return ("Number is even")
    return ("Number is odd")

print(odd_even_check(26))

# OR

def is_even(num):
    if num%2==0:
        return True
    return False

print(is_even(26))

# OR

def is_even_check(num):
    return(num%2==0)


print(is_even_check(26))

# If we pass blank function still if we want output function can return

def blank_function():
    return ("Yes it's return output")

print(blank_function())