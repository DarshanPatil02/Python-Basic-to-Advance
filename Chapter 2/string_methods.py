# String Method

name = "Darshan Patil"

# 1. Len Function
print(len(name))

#2. Lower Function
print(name.lower())

#3. Upper Function
print(name.upper())

#4. Title Method
print(name.title())

#5. Count Method
print(name.count('a'))

#6. Space remove
name = "        Darshan        "
dots = ".................."
print(name+dots)

# Remove space from left side
print(name.lstrip()+dots)

# Remove space from right side
print(name.rstrip()+dots)

# Remove space from both side
print(name.strip()+dots)


# Remove space in between 
name = "    Dars    han     "
print(name.replace(" ",""))

# Replace function

string = "She is beautful and she is good dancer"
print(string.replace(" ","_"))

# Replace for certain number of times
print(string.replace("is","was",1)) # first 'is' is replced by "was"


# find Method
string = "She is beautful and she is good dancer"
print(string.find("is"))

# Find second 'is'
# Syntax string.find("what to find", postion from where to find)

is_pos1=string.find('is')
is_pos2=string.find('is',is_pos1+1)
print(is_pos2)


# center method -- Expected output== **Darshan**
# Syntax --> string.center(length expected, expected extension)

name = "Darshan"
print(name.center(11,'*'))

user_name = input("Enter your name:")
print (user_name.center(len(user_name)+8,"*"))
