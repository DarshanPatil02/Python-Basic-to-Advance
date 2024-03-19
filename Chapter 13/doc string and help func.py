# what are doc string
# how to write doc string
# how to see doc string
# What is help function

# Doc string are written in triple quotes
def add(a,b):
    """This function takes 2 numbers and return their sum."""
    return a+b

print(add.__doc__)

# len, max, min, sum, sorted
print(len.__doc__)
print(sum.__doc__)

# help function
print(help(sum))