# Exception handling
# try except else finally

age1 = int(input("Enter your age: "))
if age1>=18:
    print( "You can play this game")
else:
    print("You can't play this game")

# This is a good code not showing error but if we put age in word like seven then it will raise error
# because of above simple reason we our code not run. We don't want this
# So the above problem is solved by try except else finally

try:
    age2 = int(input("Enter your age: "))
except:
    print("Invalid input please enter in digit")
if age2>=18:  # It will show name error
    print( "You can play this game")
else:
    print("You can't play this game")

# OR (In above code if else show error)

try:
    age = int(input("Enter your age: "))
    if age>=18:
        print( "You can play this game")
    else:
        print("You can't play this game")
except:
    print("Invalid input please enter in digit")

# Still in above code there is one problem that is code stop with not giving required output
# We want to run code till correct input not entered
    
while True:
    try:
        age_of_player=int(input("Enter your age: "))
        break
    except ValueError: # Here we know that value error will come. if we didn't place ValueError still it will run but it is not best practice for coding, we should always know which error we are handling
        print("Maybe you entered string insted of number, try again")
    except:
        print("unexpected error....")
if age_of_player>=18:
        print( "You can play this game")
else:
    print("You can't play this game")