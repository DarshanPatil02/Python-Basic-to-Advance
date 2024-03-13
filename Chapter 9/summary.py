# List comprehension summary
Square = [i**2 for i in range(1,11)]
print(Square)

# if condition in list comprehension
print([i for i in range(1,11) if i%2==0])

# if else condition in list comprehension
print([i**2 if i%2!=0 else -i for i in range(1,11)])

# Nested list by list comprehension
print([[i for i in range(1,4)] for j in range(3)])

