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

# Create your first generator with generator function
# We can generate generrators using generator function or generator comprehension

# Generator function
def num(n):
    for i in range(1,n+1):
        yield i

numbers = num(10)    

for i in numbers: # In generators as we know it generates number at ones and return it at once only
    print(i)

for i in numbers: # If we again run loop there will be blank output
    print(i)

# Generator Comprehension

square = (num**2 for num in range(1,11)) # instead of square brackets in list comprehension use parenthesis '()'
print(square)
for i in square:
    print(i)

square = (num**2 for num in range(1,11)) # instead of square brackets in list comprehension use parenthesis '()'
print(next(square))
print(next(square))
print(next(square))