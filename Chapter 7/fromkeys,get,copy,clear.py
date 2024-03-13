# fromkeys  ---> if we want to set same values for multiple keys

d = {'name':"unknown",'age':'unknown'}
print(d)

# By using fromkeys
d1 = dict.fromkeys(["name",'age','height'],'unknown')
print(d1)

d2 = dict.fromkeys(("name",'age','height'),'unknown')
print(d2)

d3 = dict.fromkeys("abc",'unknown')
print(d3)

d4 = dict.fromkeys(range(1,11),'unknown')
print(d4)

d5 = dict.fromkeys(("name","age"),('unknown',"known"))
print(d5)


# get method
user_info = {
    "name":'Darshan',
    "age": 22
}
print(user_info['name']) #--> output as "Darshan"
print(user_info['names']) #--> no output raise error because it doesn't have names key

print(user_info.get("name")) #--> output as "Darshan"
print(user_info.get('names')) #--> output is none, not raise error even it doesn't have names key

# Some more about get
dt = {
    "name":'Darshan',
    "age": 22}
print(dt.get("name","not found!"))
print(dt.get("names","not found!")) # insted of None it returns not found!


if d.get('name'):
    print("present")
else:
    print("Not present")


# Clear ---> to clear dict
d.clear()
print(d)

# copy  ---> to create copy of originl
user_info1 = user_info.copy()
print(user_info1.pop("name"))
print(user_info1)
print(user_info)

# if we do like user_info1=user_info then if we do changes in one it will reflect in other
user_info = {
    "name":'Darshan',
    "age": 22,
}
user_info1 = user_info
print(user_info1.pop("name"))
print(user_info1)
print(user_info)
