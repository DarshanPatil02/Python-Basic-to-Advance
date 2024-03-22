# csv file can be read by reader and DictReader in csv module
# Read csv file by reader
from csv import reader
with open("Chapter 19/tips.csv",'r') as rf:
    csv_reader = reader(rf) # it is an iterator
    print(csv_reader)
    for i in csv_reader:
        print(i)

# here you can see that our first heading is printing but we don't want it.
with open("Chapter 19/tips.csv",'r') as rf:
    csv_reader = reader(rf) # it is an iterator
    next(csv_reader)
    print(csv_reader)
    for i in csv_reader:
        print(i)

# Read csv file by DictWriter
# It will o/p oreded dict
from csv import DictReader
with open("Chapter 19/tips.csv",'r') as f:
    csv_reader = DictReader(f) # it is an iterator
    for row in csv_reader:
        print(row)
        print(row['time'])
    
# Read csv file seperated by |
from csv import DictReader
with open("Chapter 19/tips 1.csv",'r') as f:
    csv_reader = DictReader(f,delimiter='|') # it is an iterator
    for row in csv_reader:
        print(row['total_bill'])
    