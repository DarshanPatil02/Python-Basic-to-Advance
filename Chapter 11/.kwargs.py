# kwargs (keyword arguement)
# **kwargs (double star operators)

# kwargs as a parameter
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))

print(func(first_name="Darshan",last_name="Patil" ))

# Unpacking dictionaries

d = {
    "name":'Darshan',
    "age": 22,
    "fav_movie": ['coco', 'kimi no na wa'],
    "fav_tunes":['awakening, fairy tale']
}

def function_dict(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")

print(function_dict(**d))

