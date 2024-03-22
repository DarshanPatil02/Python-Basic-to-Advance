import pdb # import pdb module
# module python file contains usefull classes and functions wrote
# by developer.


# According to wikipedia -- Debugging is the process of finding and resolving defects or problems within a computer program
# that prevent correct operation of computer software or a system.

# Why debugging
# 1.) our program is not running and causing unexpected errors.
# 2.) our program is working fine but not working the same way we want

# Steps for debugging
#1.) set trace
#2.) execute code Line by Line

pdb.set_trace() # it is used to track error
# It works as line by line means it runs 1st line after that enter l to check which line is running. 
# Then enter n for next line. Repeate steps till error found
name = input("Please enter your name: ")
age = input("Please enter your age: ")
print(f"Hello {name} your are is {age}")
new_age = age+5 # at this line it will show "TypeError: can only concatenate str (not "int") to str" and we found error
print(f"Hello {name} your are will be {new_age} after 5 years")

# Resloved my mistake
pdb.set_trace() 
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
print(f"Hello {name} your are is {age}")
new_age = age+5 
print(f"Hello {name} your are will be {new_age} after 5 years")
