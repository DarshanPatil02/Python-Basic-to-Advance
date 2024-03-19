# advance min() and max() function

numbers = [1,2,4,5,7]
print(max(numbers))
print(min(numbers))

names = ['Rohit','Darshan','Ajay']
def func(item):
    return len(item)

print(max(names, key=func))
print(min(names, key=func))

# By using lambda function
names = ['Rohit','Darshan','Ajay']
print(max(names, key= lambda x: len(x)))
print(min(names,key=lambda x:len(x)))

students = [
    {'name':'Darshan', 'score':95, 'age':21},
    {'name':'Rohit', 'score':90, 'age':18},
    {'name':'Ajay', 'score':87, 'age':25}
]

print(max(students, key=lambda item: item.get('score'))['name'])

students1 = {
    'Darshan': {'score':95, 'age':21},
    'Rohit': {'score':90, 'age':18},
    'Ajay': {'score':87, 'age':25}
}

print(max(students1, key= lambda item: students1[item]['score']))

