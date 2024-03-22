# else and finally clause in exception handling
 
try:
    num=int(input("Enter number : "))
except ValueError: # Here we know that value error will come. if we didn't place ValueError still it will run but it is not best practice for coding, we should always know which error we are handling
    print("You didn't entered integer")
except:
    print("unexpected error....")

# loop
while True:
    try:
        num=int(input("Enter number : "))
        print(f"User input: {num}")
        break
    except ValueError: # Here we know that value error will come. if we didn't place ValueError still it will run but it is not best practice for coding, we should always know which error we are handling
        print("You didn't entered integer")
    except:
        print("unexpected error....")

# use of else --> it is not good practice to write more lines in try block
while True:
    try:
        num=int(input("Enter number : "))
    except ValueError: # Here we know that value error will come. if we didn't place ValueError still it will run but it is not best practice for coding, we should always know which error we are handling
        print("You didn't entered integer")
    except:
        print("unexpected error....")
    else: # else block run only when try block successfully runs
        print(f"User input: {num}")
        break

# use of finally--> It will run at any cost. If try command fail still it run and If try command success still it run        
while True:
    try:
        num=int(input("Enter number : "))
    except ValueError: # Here we know that value error will come. if we didn't place ValueError still it will run but it is not best practice for coding, we should always know which error we are handling
        print("You didn't entered integer")
    except:
        print("unexpected error....")
    else: # else block run only when try block successfully runs
        print(f"User input: {num}")
        break
    finally:
        print("Finally block runs............")
