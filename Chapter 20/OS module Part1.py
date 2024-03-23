import os
# to get current working directory
print(os.getcwd())

# to change current working directory
os.chdir("H:/Python/Chapter 20")

# If i want to create new folder in cwd
os.makedirs("New Folder")

# If we want to check is any folder is present or not
print(os.path.exists("New Folder")) 

# How to create file
open("Text_file.txt",'a').close() # if file already exist then it will not show error

# To get files present in folder
print(os.listdir())

# if we want to get file names with location then we use
for item in os.listdir(r"H:\Python"):
    path = os.path.join("H:\Python"+'\\'+item)
    print(path)

# Suppose we want to know folder as well as files present inside folder
file_iter = os.walk("H:\Python") 
print(file_iter) # It is an iterator
for Current_path, folder_names, file_names in file_iter:
    print(f"Current Path : {Current_path}")
    print(f"folders_name : {folder_names}")
    print(f"file_names : {file_names}")

# Suppose we have to delete some folder
import shutil
shutil.rmtree("H:/Python/Chapter 20/New Folder") # It will permanently delete this file
# shutle.copy and shutle.move are some function for copy files and move files resp.

