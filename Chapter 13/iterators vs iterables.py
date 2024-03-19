numbers = [1,2,3,4] # iterables
squares=list(map(lambda a:a**2, numbers)) # iterators
print(squares)

for i in squares:
    print(i)

iter_number = iter(numbers)
print(list(iter_number))
print(next(iter_number))