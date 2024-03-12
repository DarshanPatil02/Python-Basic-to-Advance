# generate list with range function
# something more about pop function
# pass list to a function

list = []
for i in range(11):
    list.append(i)
print(list)

# Or 
number_list = list(range(11))
print(number_list)

# something more about pop function
print(number_list.pop())
popped_item = number_list.pop(2)
print(popped_item)

# pass list to a function
number_list = list(range(1,11))
def negative_list(list):
    negative=[]
    for i in list:
        negative.append(-i)
    return negative

negative_list(number_list)