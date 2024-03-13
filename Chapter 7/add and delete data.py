# add and delete data
user_info = {
    "name":'Darshan',
    "age": 22,
    "fav_movie": ['coco', 'kimi no na wa'],
    "fav_tunes":['awakening, fairy tale']
}
print(user_info)

# how to add data
user_info["fav_song"]=["song1","song2"]
print(user_info)

# how to delete data
popped_items = user_info.pop("fav_tunes")
print(f"popped items is {popped_items}")
print(user_info)

# popitem method
popped_item = user_info.popitem()
print(popped_item)
print(user_info)