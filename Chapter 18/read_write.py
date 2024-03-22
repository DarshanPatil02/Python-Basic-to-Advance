# file read and write at a time
# Suppose i want to read file Chapter 18/Good thoughts.txt and write it in Chapter 18/file1.txt

with open("Chapter 18/Good thoughts.txt",'r') as rf:
    with open("Chapter 18/file1.txt",'w') as wf:
        wf.write(rf.read())

# OR 
with open("Chapter 18/Good thoughts.txt",'r') as rf:
    with open("Chapter 18/file1.txt",'w') as wf:
        for i in rf.readlines()[:2]:
            wf.write(i)
