# readfile
# open function
# read method
# seek method
# tell method
# readline method
# readlines method
# close method
# name, close

f = open("H:\\Python\\Chapter 18\\Good thoughts.txt") # open function

print(f"cursor position - {f.tell()}") # tell method

print(f.read())  # read method
print(f"cursor position - {f.tell()}")

# seek method
print(f"cursor position before seek - {f.tell()}")
print(f.seek(7)) # To place the cursor at required position
print(f"cursor position after seek - {f.tell()}")

# close method
f.close()

# Again
f = open("H:\\Python\\Chapter 18\\Good thoughts.txt") # open function
print(f.readline())  # readline method --> read only one line
print(f.readline(), end="") # to avoid line spacing use end = ""
print(f.readline())
print(f.readline())
f.close()

# readlines
f = open("H:\\Python\\Chapter 18\\Good thoughts.txt") 
lines = f.readlines()
print(lines)
for i in lines:
    print(i)

# name to get name of file
print(f.name)
# closed to check file close or not
print(f.closed)
f.close()
print(f.closed)

# We can read files like this also
f = open("H:\\Python\\Chapter 18\\Good thoughts.txt") 
for line in f:
    print(line)

for line in f.readlines()[:2]:
    print(line)
f.close()
