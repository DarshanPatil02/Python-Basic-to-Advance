# While loop

# Print Hello world! as per user requirement

user_input = int(input("Enter number: "))
i=1
while i<=user_input:
        print("Hello Wolrd!", i)
        i+=1

# Sum certain number by while loop
 
user_input = int(input("Enter number: "))
total = 0
i = 0
while i <= user_input:
        total+=i
        i+=1
print(f"Sum of 1 to {user_input} is {total}")


# for loops

for i in range(10):
        print("Hello World!")


total=0
for i in range(0,11):
        total+=i
print(total)


# ask user to input a number containing more than one digit
# example I 1256
# calculate 1+2+5+6 and print
# algorithm (method to solve problem in human language)
# ask input in string, i.e don't change string to int
# example - "1256"
# pick string character one by one and change to int
# int(example[0]) + int(example[1]) .... go upto len(example)\

user_input = input("Enter number: ")
total=0
for i in range(0,len(user_input)):
        total+=int(user_input[i])
print(f"The sum of {user_input} is {total}")


# ask a user for name
# print count of each words
# output:
# D:1
# a:3
# r:1
# s:1
# h:1
# n:1
#  :1
# P:1
# t:1
# i:1
# l:1


name = input("Enter your name: ")
temp_var = ''

for i in range(0,len(name)):
        if name[i] not in temp_var:
                temp_var+=name[i]
                print(f"{name[i]}:{name.count(name[i])}")

# Break and Continue keyword

# 1 to 10 print
for i in range(1,11):
        if i==5:
                break
        print(i)
         
# Continue
# 1 to 10 print but not 5

for i in range(1,11):
        if i==5:
                continue
        print(i)

# Step in range
# Synatx --> range(start,end,step)
        
for i in range(1,100,2):
        print(i)

for i in range(20,0,-2):
        print(i)


# Loops is string
for i in "Darshan":
        print(i)

# Sum of number digits
total=0
number = input("Enter Number here:")
for i in number:
        total+=int(i)
print(total)
