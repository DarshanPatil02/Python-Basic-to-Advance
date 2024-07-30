# list --> Ordered collection of Data
# You can store anything in lists like int,float, string

number = [2,6,8,9,25]
print(number)
print(type(number))

Words = ['John',"Tom","Lucy","Berlin"]
print(Words) 

mixed = [1,2,3,4,"Five",'Six', 6.5,7.8, None]
print(mixed)

# retrieve in list
print(mixed[2])

print(Words[2][2])

# Lists are mutable so we can change

print(mixed)  # Before
mixed[2]="Three"
print(mixed)  # after

words = ['John',"Tom","Lucy","Berlin"]
print(words[1][1:]) # obtain something in list element

