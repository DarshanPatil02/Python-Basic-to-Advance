# Syntax
# if condition:
#   #code # if condition is true then this code will execute

age = int(input("Enter your age: "))
if age>=14:
    print("Your age is above 14")

# Pass
x = 18
if x>=18:
    pass


# Else Statement
age = int(input("Enter your age: "))
if age>=14:
    print("Your age is above 14")
else:
    print("Your age is less than 14")



# Check two condition at same time
# and, or
     
name = "abc"
age = 19

# And
if name=='abc' and age==19:
    print("Condition is True")
else:
    print("Condition is False")

if name=='abc' and age==25:
    print("Condition is True")
else:
    print("Condition is False")

# OR
    
if name=='abc' or age==19:
    print("Condition is True")
else:
    print("Condition is False")

if name=='xyz' or age==19:
    print("Condition is True")
else:
    print("Condition is False")