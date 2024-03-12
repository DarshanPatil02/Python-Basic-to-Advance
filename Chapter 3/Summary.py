# if Statement

name = "Darshan"
if name=="Darshan":
    print("Your name is Darshan")
else:
    print("You are not Darshan")

# OR
    
name = "Dhiraj"
if name=="Dhiraj" or name=="dhiraj":
    print("Your name is Dhiraj")
else:
    print("You are not Dhiraj")

# AND
    
name = "Dhiraj"
if name=="Dhiraj" and name=="dhiraj":
    print("Your name is Dhiraj")
else:
    print("You are not Dhiraj")


# WHile
    
i=0
while i<=10:
    print(f"Hello World! {i}")
    i+=1

# for loop

for i in range(1,10):
    print(i)

# for with break
 for i in range(0,11):
    if i==5:
        break
    print(i)

# for with continue
for i in range(1,11):
    if i==5:
        continue
    print(i)

# loop with string

for i in "Darshan":
    print(i)

# range function with step

for i in range(1,10,2):
    print(i)