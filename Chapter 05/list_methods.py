fruits = ["orange","apple","pear","banana","kiwi","apple","banana"]

if "apple" in fruits:
    print("apple is present")
else:
    print("apple is not present")


# Some common methods in list
# count
# sort method
# sorted function
# reversed
# clear
# copy
# index method
    
print(fruits.count("apple"))

fruits.sort() # sort ascending order
print(fruits)

fruits.sort(reverse=True) #sort descending order
print(fruits)

number=[3,5,1,9,10]
number.sort()
print(number)

# Sorted  ---> used to sort number without affecting original one
fruits = ["orange","apple","pear","banana","kiwi","apple","banana"]
print(sorted(fruits))
print(fruits)  # --->  original list doesn't affected

print(sorted(fruits, reverse=True))

number=[3,5,1,9,10]
print(number) # before clear
number.clear()
print(number) # after clear

number=[3,5,1,9,10]
number_copy = number.copy()
print(number_copy)

number_copy[1]=12
print(number_copy) #---> Copy changes according to command
print(number) #---> Original list remains same

# index method
numbers = [2,8,6,9,7,3,12]
print(numbers.index(8))

numbers = [2,8,6,9,7,3,12,6,85,52]
print(numbers.index(6)) # syntax index.(number to  find, from index position (default = 0))
print(numbers.index(6,3)) # syntax index.(number to  find, from index position)
print(numbers.index(6,3,10)) # syntax index.(number to  find, from index position,end index)

