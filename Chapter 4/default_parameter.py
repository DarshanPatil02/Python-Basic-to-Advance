# Default parameter

def user_info(first_name,last_name,age):
    print(f"Your first name is {first_name}")
    print(f"Your last name is {last_name}")
    print(f"Your age is {age}")

user_info("Darshan","Patil",22)

# By using Default parameter

def user_info(first_name,last_name,age=26):
    print(f"Your first name is {first_name}")
    print(f"Your last name is {last_name}")
    print(f"Your age is {age}")

user_info("Ravi","Jadhav")

user_info("Ravi","Jadhav",25)

