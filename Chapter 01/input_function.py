a = "My name is"
b = "Darshan"
print(a+" "+b)

age = input("Enter your age:")
my_age_is="My age is:"
print(my_age_is+age)

number_1 = int(input("Enter your number: "))
number_2 = int(input("Enter your number: "))
print("Sum of Number1 and Number2 is", number_1+number_2)

name,age = "Darshan","22"
print(f"My name is {name} and my age is {age}")

x=y=z=1
print(x+y+z)


name,age = input("Enter your name and age ").split()
print(f"My name is {name} and my age is {age}")


# String Formatting

name = "Darshan"
age = "22"

print("Hello {} my age is {}".format(name,age))
# OR
print(f"Hello {name} my age is {age}")
