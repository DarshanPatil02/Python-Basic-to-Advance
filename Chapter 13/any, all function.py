# any, all function

number1 = [2,4,6,8,10]
number2 = [1,2,3,4,5,6]

evens1 = []
for num in number1:
    evens1.append(num%2==0)

print(evens1)

evens2 = []
for num in number2:
    evens2.append(num%2==0)
print(evens2)

# all function is used to check all values in list are True or not
print(all([True,True,True,True,True]))

print(all([nums%2==0 for nums in number1]))
print(all([nums%2==0 for nums in number2]))

# any function is used to check any values in list are True or not 
print(any([nums%2==0 for nums in number1]))
print(any([nums%2==0 for nums in number2]))
