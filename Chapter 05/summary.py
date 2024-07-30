# List cahpter summary
# List is a data structure that can holda any type of Data

# Create a list
word = ["word1","word2"]

# You can store anything inside list
mixed = [1,2,3,[4,5,6],"seven",8.0,None]

# List is a ordered collection of items
print(mixed[0]) # output = [1]
print(mixed[3]) # Output = [4,5,6]

# Add data to our list
# append method
mixed.append(10)
print(mixed)

mixed.append([10,20,30])
print(mixed)

# Extend
mixed.extend([10,20,30])
print(mixed)

# join two list
l1=[10,20,30]
l2=[40,50,60]
l = l1+l2
print(l)

# Insert
mixed.insert(1,25)
print(mixed)

# Remove data from list
popped=mixed.pop() # remove last item
popped=mixed.pop(1) # remove item at last position

# Remove
mixed.remove("seven")
print(mixed)

# del statement
print(mixed)
del mixed[2]
print(mixed)

# loop in list
for i in mixed:
    print(i)