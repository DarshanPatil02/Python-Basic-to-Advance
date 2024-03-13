# List comprehension
# with the help of list comprhension we can create of list in one line

# Create a list of square from 1 to 10
square = []
for i in range(1,11):
    square.append(i**2)
print(square)

# By using list comprehension
square_2 = [i**2 for i in range(1,11)]
print(square_2)

# create a list of negative number from 1 to 10
negative = []
for i in range(1,11):
    negative.append(-i)

print(negative)

# By using list comprehension
negative_1 = [-i for i in range(1,11)]
print(negative_1)

# take a input of certain name and obtain their first letter as output
names = ["Darshan","Rohit","Mohit","Punit"]
first_letter = [i[0] for i in names]
print(first_letter)
