# Print vs return  -> The print command can be used just about anywhere in a Python program to output information to the console. The return statement can only be used in functions.
# Return give output in function we need to print it

def add_three(a,b,c):
    return a+b+c

print(add_three(12,15,20))

def add_three(a,b,c):
    print(a+b+c)
          
add_three(12,15,20)

