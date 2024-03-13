# list comprehension with if statement
ls = list(range(1,11))
print(ls)

even_numbers = [i for i in ls if i%2==0]
print(even_numbers)

odd_nums = [i for i in range(1,11) if i%2!=0]
print(odd_nums)