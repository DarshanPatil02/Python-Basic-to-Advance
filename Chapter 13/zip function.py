# Zip function

user_id = ["user1","user2","user3"]
names = ['Rohit','Mohit',"Vinit"]

print(list(zip(user_id,names)))

user_id = ["user1","user2"]
names = ['Rohit','Mohit',"Vinit"]

print(list(zip(user_id,names)))

examples = [("a",1),("b",2)]
print(dict(examples))

user_id = ["user1","user2","user3"]
names = ['Rohit','Mohit',"Vinit"]
last_name = ['Sharma',"Modi","Shah"]
print(list(zip(user_id,names,last_name)))


# Zip unpacking
l = [(1,2),(3,4),(5,6),(7,8)]
l1,l2 = list(zip(*l))
print(l1)
print(l2)

# Find max from tuple pairs
new_list = []
for pair in zip(l1,l2):
    new_list.append(max(pair))
    
print(new_list)
