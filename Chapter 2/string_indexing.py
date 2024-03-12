#string indexing

language="python"

#position (index number)

# p = 0, -6
# y = 1, -5
# t = 2, -4
# h = 3, -3
# o = 4, -2
# n = 5, -1

print(language[2])
print(language[-1])

#Slicing/ Selecting sub sequence
# Syntax - (start argument: stop argument -1)

print(language[2:4])
print(language[2:])
print(language[:5])

# String step argument
# Syntax - (start argument: stop argument -1 :step)

print(language[0:5:2])
print(language[::3])
print(language[::-1])