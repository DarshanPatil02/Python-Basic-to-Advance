# in keyword in set and for loop 

s = {"a",'b','c'}
# in keyword to check if item is present or not in set
if "a" in s:
    print("Present")
else:
    print("Not Present")

# for loop in set
for item in s:
    print(item)

#set math
s1 = {1,2,3,4}
s2 = {3,4,5,6}

# Union
union_Set =s1 | s2
print(union_Set)

# Intersection
intersection_set = s1 & s2
print(intersection_set)
