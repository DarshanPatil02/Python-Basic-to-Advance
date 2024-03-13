# dictionaries intro

#Q - why we use dictionaries?
#A - Because of limitations of lists, lists are not enough to represent real data
# Example --

user = ['Darshan', 22, ['coco', 'kimi no na wa'], ['awakening, fairy tale']] 

# this list contains user name, age, fav movies, fav tunes
# you can do this but this is not a good way to do this.
#Q. what are dictionaries
#A. unordered collections of data in key value pair.
# how to create dictionaries

user = {"name": 'Darshan', "age": 22}
print(user) 
print(type(user))

# Second method to create dict
user_info = dict(name='Darshan',age= 22,fav_movie= ['coco', 'kimi no na wa'], fav_song=['awakening, fairy tale'])
print(user_info)
print(type(user_info))

# Dict does not repeate same key again it update same key with new values
dt = {"name":'Darshan',"age": 22,"age":35}
print(dt)
dt = {"name":'Darshan',"age": 35,"age":22}
print(dt)

# how to access data from dictionaries
# Note - There is no indexing because of unordered collection of data
print(user_info["name"])
print(user_info['age'])


# Which type of data a dictionary can store?
# Anything ---> Number,strings, list, dict

# How to add data to empty dictionary
users_info = {
    "user1":{"name":"John","age":25},
    "user2":{"name":"Tom","age":28},
    "user3":{"name":"Rock","age":23}
}  

print(users_info)
print(users_info["user1"])

# How to add data to empty dictionary
user_info2 ={}
user_info2['name']="Darshan"
user_info2["age"]=22
print(user_info2)