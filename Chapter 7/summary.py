# Summary of dictionary chapter
#Q. what are dictionaries
#A. unordered collections of data in key value pair.

d = {"name": "Darshan",
     'Age':22}

print(d)
# OR
d = dict(name="Darshan",age=22)
print(d)

# How to acces data from dict
print(d['name'])

# Add data in empty dict
empty_dict = {}
empty_dict['Fruit1']="apple"
empty_dict['Fruit2']="orange"
empty_dict['Fruit3']="mango"

print(empty_dict)

# Check existance of values inside dict
if 'name' in d:
    print("present")
else:
    print("not present")

# How to iterate over dict
for i,j in d.items():
    print(i,":",j)

# to print all keys
for i in d:
    print(i)

# to print all values
for i in d.values():
    print(i)

# most common dict methods
# to access a key or check existance
print(d.get('name'))

# Q. Why we use get
# A. To get rid of error
# E.g: 
print(d.get("names"))

# To delete items
# pop ---> takes one arguement which takes keyword

popped = d.pop("name")
print(popped)

# Popped_item ---> remove any key from dict
d = {
    "name":'Darshan',
    "age": 22,
    "fav_movie": ['coco', 'kimi no na wa'],
    "fav_tunes":['awakening, fairy tale']
}

popped_item = d.popitem()
print(popped_item)
print(d)