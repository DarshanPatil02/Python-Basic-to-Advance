fruits1 = ["orange","apple","pear"]
fruits2 = ["banana","kiwi","apple"]
fruits3 = ["orange","apple","pear"]

print(fruits1==fruits2)  # False ---> Because list elements are not same

print(fruits1==fruits3)  # True ---> Because list elements are same

print(fruits1 is fruits3) # False ---> Because here list elements are same but there location in memory is different  

# Split method
# Convert string to list

user_info = "Darshan 22".split(" ")
print(user_info)

name,age = "Darshan 22".split(" ")
print(name,age)

# join method
# Convert list to string
user_info = ["Darshan", "22"]
print(user_info)

print(",".join(user_info))
