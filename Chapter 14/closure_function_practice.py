# function returning function practice
# It is also called closure function

def to_power(x): # power digit
    def calc_power(n):  # number to power
        return n**x
    return calc_power
cube = to_power(3)
print(cube(5))

square = to_power(2)
print(square(3))