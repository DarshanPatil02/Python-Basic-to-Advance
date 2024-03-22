# Read salary.txt 
# And return output as Darshan's salary is 100000

with open("H:/Python/Chapter 18/salary.txt",'r') as rf:
    with open("H:/Python/Chapter 18/Exercise.txt",'w') as wf:
        for line in rf.readlines():
            name,salary = line.split(',')
            wf.write(f"{name}'s Salary is {salary}")