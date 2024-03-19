# Enumerated Function
# We use enumerated function with for loop to track position of our item in iterable 

# How we do this without enumerated function
names = ["abc","xyz","Darshan"]
# Expected Output
"""
0 --abc
1 --xyz
2 --Darshan
"""
pos=0
for i in names:
    print(f"{pos} --- {i}")
    pos+=1

# With enumerated function
for position,name in enumerate(names):
    print (f"{position} --- {name}")

# Define a function that takes two arguement
# 1.) string containing list
# 2.) string that want to find in and this function will return the index of string in your list
# and if the string is not present return -1
    
def position_finder(ls,target):
    for pos,string in enumerate(ls):
        if string==target:
            return pos
    return -1
        
ls = ["abc","xyz","Darshan"]
print(position_finder(ls, "Darshan"))

print(position_finder(ls, "abc1"))
 