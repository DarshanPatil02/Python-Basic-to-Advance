# with block it not only used for reading or open it is used for many purpose
# with block is also called context manager...

with open("Chapter 18\Good thoughts.txt") as f:
    for line in f:
        print(line) 

print(f.closed)