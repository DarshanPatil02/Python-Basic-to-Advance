# define generator function
# take one number as arguement
# generate a sequence of even numbers from 1 to number

def even_num(n):
    for i in range(2,n+1,2):
        yield i

even_numbers = even_num(10)
for i in even_numbers:
    print(i)

for i in even_numbers:
    print(i)

for i in even_numbers:
    print(i)

