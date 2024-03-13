# list comprehension with if statement
ls = list(range(1,11))
print(ls)

even_numbers = [i for i in ls if i%2==0]
print(even_numbers)

odd_nums = [i for i in range(1,11) if i%2!=0]
print(odd_nums)

# list comprehension if else
# get an output from a list if number inside list is even make it double and if number is odd make it negative

ls = list(range(1,11))
output = [i*2 if i%2==0 else -i for i in ls]
print(output)