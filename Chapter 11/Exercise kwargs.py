# function
# list, reverse = True

def func(l,**kwargs):
    if kwargs.get("reverse_str")==True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]


names = ["darshan","patil"]
print(func(names))

print(func(names, reverse_str=True))