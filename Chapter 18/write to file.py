# how to write in file
# r --> read
# w --> write
# a --> write
# r+ --> we can read our file and we also write our file and it does not create file like 'w' and 'r' mode 

# w, a function also able to create file in directory if file not exist 

with open("H:/Python/Chapter 18/file.txt", 'w') as f: # w is used to overwrite (Inside file content will delete and new will add)
    f.write("hello friends")

with open("H:/Python/Chapter 18/file.txt", 'a') as f: # a is used to extend or append in file
    f.write("\nHear we are learning how to write in file using python")

for line in open("H:/Python/Chapter 18/file.txt",'r'):
    print(line)

with open("H:/Python/Chapter 18/file.txt",'r+') as f:
    f.write("Here we are using r+ function")

for line in open("H:/Python/Chapter 18/file.txt"): # 'r+' it overwrite on all previous content in file 
    print(line)
# 'r+' it overwrite on all previous content in file. To avoid this we can use seek method first to change curser position
    
with open("H:/Python/Chapter 18/file.txt",'r+') as f:
    f.seek(len(f.read())) # pass curser at end line
    f.write("\nHello friend!\n Welcome to my github repo\n")
    
for line in open("H:/Python/Chapter 18/file.txt"):  
        print(line)


