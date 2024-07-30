# common  method to delete data from list
fruits = ["orange","apple","pear","Banana","Kiwi"]

# pop method

fruits.pop() # delete last element if pass blank
print(fruits)

fruits.pop(1) # delete element whose index is given
print(fruits)

#del
del fruits[1] # delete element whose index is given
print(fruits)

# remove
fruits.remove("Banana")
print(fruits)