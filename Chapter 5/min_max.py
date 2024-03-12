numbers = [6,60,2]
print(min(numbers))
print(max(numbers))

# Create a function which gives difference between minimum and maximum number in list

def min_max_diff(ls):
    diff = max(ls) - min(ls)
    return diff

print(min_max_diff(numbers))