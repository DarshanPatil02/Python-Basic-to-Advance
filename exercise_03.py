# EXERCISE, NUMBER GUESSING GAME
# Make a variable, like winning_number and assign any number to it.
# Ask user to guess a number .
# if user guessed correctly then print "YOU WIN !!!!"
# if user didn't guessed correctly then :
# if user guessed lower than actual number then print "too low"
# if user guessed higher than actual number then print "too high"

# google "how to generate random number in python to generate random
# winning number

import numpy as np
user_input = int(input("Enter number between 1 to 100 here: "))
winning_number = np.random.randint(1,100)
if user_input==winning_number:
    print("YOU WIN !!!!")
if user_input<winning_number:
    print("too low")
else:
    print("too high")
print(f"Winning number is {winning_number} and your number is {user_input}")


# EXERCISE WATER COCO
# Ask user's name and age
# If user's name start with ('a' or 'A') and age is above 10 then
# Print 'you can watch coco movie'
# Else print 'sorry, you cannot watch coco'

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

if user_name.lower()[0]=='a' and user_age>=10:
    print('you can watch coco movie')
else:
    print ('sorry, you cannot watch coco')


# if elif else statement
    
# Show ticket pricing
# 1 to 3 (free)
# 4 to 10 (150)
# 11 and 60 (250)
# 60 and above (200)
    
user_age = int(input("Enter your age: "))
if user_age<=0:
    print("Please enter valid age")
elif 0<user_age<=3:
    print("You got free ticket")
elif 3<user_age<=10:
    print("Pay Rs 150")
elif 10<user_age<=60:
    print("Pay Rs 250")
else:
    print("You pay Rs 200")

# exercise one of three
# sum of n natural numbers
# ask a user for natural number(n)
# print total from 1 to n


user_input = int(input("Enter number: "))
total = 0
i = 0
while i <= user_input:
        total+=i
        i+=1
print(f"Sum of 1 to {user_input} is {total}")


# ask user to input a number containing more than one digit
# example I 1256
# calculate 1+2+5+6 and print
# algorithm (method to solve problem in human language)
# ask input in string, i.e don't change string to int
# example - "1256"
# pick string character one by one and change to int
# int(example[0]) + int(example[1]) .... go upto len(example)\

user_input = input("Enter number: ")
total = 0
i=0
while i <len(user_input):
    total+=(int(user_input[i]))
    i+=1
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
i=0
while i < len(name):
    if name[i] not in temp_var:
        temp_var+=name[i]
        print(f"{name[i]}:{name.count(name[i])}" )
    i+=1
    