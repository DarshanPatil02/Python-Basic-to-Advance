# loops in tuples
# tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# some function that you can use with tuples

mixed = (1,2,3,4.0)

# for loop in tuple
for i in mixed:
    print(i)

# tuple with one element   ---> syntax ----> tuple = (element,) ----> comma is important
nums = (1,)
words = ("word1",)
print(type(nums))
print(type(words))

# tuple without parenthesis
guitars = 'yamaha', "baton rouge", 'taylor'
print(guitars)
print(type(guitars))

# tuple unpacking
guitarists = ('Maneli Jamal', 'Eddie Van Der Meer', "Andrew Foy")
guitarists1,guitarists2,guitarists3 = (guitarists)
print(guitarists1, type(guitarists1))
print(guitarists2, type(guitarists2))
print(guitarists3, type(guitarists3))
