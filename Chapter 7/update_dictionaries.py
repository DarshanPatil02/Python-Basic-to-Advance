user_info = {
    "name":'Darshan',
    "age": 22,
    "fav_movie": ['coco', 'kimi no na wa'],
    "fav_tunes":['awakening, fairy tale']
}
print(user_info)

more_info = {"State":"Maharashtra","hobbies":["coding","reading","playing"]}

# update
user_info.update(more_info)
print(user_info)

# update also update previous data
more_info = {"name":"Darshan Patil","State":"Maharashtra","hobbies":["coding","reading","playing"]}
print(user_info)
user_info.update(more_info)
print(user_info)


