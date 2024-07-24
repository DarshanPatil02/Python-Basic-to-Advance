# Q. Ask user to input 3 number and you have to print averageof three numbers
n1=input("Enter No. 1: ")
n2=input("Enter No. 2: ")
n3=input("Enter No. 3: ")
print(f"Average of three numbers is: {(int(n1)+int(n2)+int(n3)/3)}")
# OR
n1,n2,n3=input("Enter 3 numbers here: ").split(",")
Avg=(int(n1)+int(n2)+int(n3))/3
print(f"Average of three numbers is {Avg}")


# Q. Ask user name and print it in reverse order
user_name=input("Please enter your name: ")
print(user_name[::-1])

# Q. Take two comma seperate input from user 
# 1) user's name
# 2) a single character
# Output: 
# 1) user's name length
# 2) count the single character user inputted in user's name

user_name_input, user_letter = input("Enter your name and letter: ").split(",")
print(len(user_name_input.strip()))
print(user_name_input.strip().lower().count(user_letter.strip().lower()))
