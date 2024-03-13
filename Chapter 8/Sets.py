# Set datatypes
# Unordered collection of unique items

s = {1,2,3,4,5}
print(s)

s1 = {1,2,3,2}
print(s1)   # Not repeate 2

# Remove duplicates from list
l = [7, 2, 1, 1, 3, 4, 5, 10, 1, 5, 6, 8, 6, 3, 2, 1, 9, 7, 3, 1, 9, 1, 4, 2, 4]
print(l)

set1 = set(l)
l = list(set1)
print(l)