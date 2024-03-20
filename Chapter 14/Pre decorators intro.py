# You should have a complete understading of functions
# first class function/ closures
# then finally we will learn about decorators

def squares(a):
    return a**2

s = squares
print(s(7))
print(s.__name__)
print(squares.__name__)
print(s)
print(squares)