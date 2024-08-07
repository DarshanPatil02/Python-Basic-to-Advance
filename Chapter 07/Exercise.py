# define a function that takes a number (n)
# return a dictionary that contains cube of number from 1 to n
#e.g.: cube_finder(3)
#output = {1:1,2:8,3:27}

def cube_finder(n):
    cube_dict = {}
    for i in range(1,n+1):
        cube_dict[i]=(i**3)
    return cube_dict

print(cube_finder(3))

# Word Counter
def word_counter(name):
    dt = {}
    for i in name:
        count = name.count(i)
        dt[i]=count
    return dt            

print(word_counter("Darshan Patil"))

# Print the following dict in vertical line
user_info ={}

name = input('What is your name? ')
age = int(input("What is your age? "))
fav_movie= input("Which are your favourite movie seperated by comma? ").split(',')
fav_songs= input("Which are your favourite songs seperated by comma? ").split(',')

user_info['name']=name
user_info['age']=age
user_info['fav_movie']=fav_movie
user_info['fav_songs']=fav_songs

for i,j in user_info.items():
    print(i,":" ,j)
