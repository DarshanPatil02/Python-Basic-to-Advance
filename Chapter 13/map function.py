number = [1,2,3,4]

def square(a):
    return a**2

square_numbers =  list(map(square,number))
print(square_numbers)

# or
print(list(map(lambda x:x**2, number)))

names = ['abc',"abcde","abcdefghij"]
length = list(map(len,names))
print(length)