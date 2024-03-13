# in keyword and iteration
user_info = {
    "name":'Darshan',
    "age": 22,
    "fav_movie": ['coco', 'kimi no na wa'],
    "fav_song":['awakening, fairy tale']
}
print(user_info)

# Check if key exist in dictionary
if "name" in user_info:
    print("present")
else:
    print("Not Present")

if "names" in user_info:
    print("present")
else:
    print("Not Present")


# Check if values exist in dictionary
if "Darshan" in user_info.values():
    print("present")
else:
    print("Not Present")

if 22 in user_info.values():
    print("present")
else:
    print("Not Present")

# loops in dictionary
for i in user_info:
    print(i)  # to print keys

for i in user_info.values():
    print(i)  # to print values

# key methods and values method
print(user_info.keys())
print(user_info.values())

# items
dict_items = user_info.items()
print(dict_items)

for key,value in user_info.items():
    print(f"key is {key} and value is {value}")