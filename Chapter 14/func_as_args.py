l = [1,2,3,4]
print(list(map(lambda a: a**2, l)))
# map in build function use

def my_name(func,l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list

def my_map2(func,l):
    return [func(item) for item in l]
# my_map2 in created function we use

print(my_map2(lambda a: a**2, l))