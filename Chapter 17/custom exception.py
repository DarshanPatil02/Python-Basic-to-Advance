# python custom exceptions
# Q - Why custom exceptions
# A - To increase readability of code

# Example

def validate(name):
    if len(name)<8:
        raise ValueError("Name is too short")
    
username="Darshan"
validate(username)
print(f"hello {username}")

# Instead of ValueError we want other like NametooshortError

class NametooshortError(ValueError):
    pass

def validate(name):
    if len(name)<8:
        raise NametooshortError("Name is too short") # here we have to define NametooshortError class first

username=input("Enter your name: ")
validate(username)
print(f"hello {username}")
