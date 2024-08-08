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

s = {1,2,3}
s.add(4)
print(s)

s.remove(3)  # if something not present in set want to remove gives error so go to discard
print(s)

print(s)
s.discard(5)
print(s)


s.clear() # to clear sets
print(s)

# Copy
s = {1,2,3,4,5,6,7,8,9}
s1 = s.copy() 
print(s1)

# What can store in sets?
# int, float, str,bool  but not list, dict
# But 1 and True can't be at a time in sets or vice versa 0 and False can't be at a time in sets
s = {1,22.6,8.5,True,"string"}
print(s)

p = {0,False,12.5,5}
print(p)

