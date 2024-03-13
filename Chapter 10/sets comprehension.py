# set comprehension

s = {i**2 for i in range(11)}
print(s)

import random
numbers = [random.randint(1,10) for _ in range(25)]
print(numbers)

s1 = {i  for i in [random.randint(1,10) for _ in range(6)]}
print(s1)

names = ("Mohit","Rohit","Vinit","Punit","Ankit","Pandit")
word_initial = {name[0] for name in names}
print(word_initial)