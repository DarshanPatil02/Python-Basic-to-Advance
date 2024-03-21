# Generators
# As we already know iterator and iterables
# Let's revise them

l = [1,2,3,4] # iterable

iter1 = iter(l) # iterator function
print(next(iter1))
# iterable can be convert into iterators and can perform opeartion like loop
# Always in loop first iterable is converted into iterators and then loop is applied
l = [1,2,3,4] # iterable
for num in map(lambda x: x**2 ,l): # here map func is iterator so for loop not need to convert l(an iterable) into iterators 
    print(num)

# generators are iterators
"""
In Python, a generator is a function that returns an iterator that produces a sequence of values when iterated over.
Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once.
"""

