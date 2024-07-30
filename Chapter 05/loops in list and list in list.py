fruits = ["orange","apple","pear","banana","kiwi","apple","banana"]

# for loop

for fruit in fruits:
    print(fruit)

# While loop
i = 0
while i in range(len(fruits)):
    print(fruits[i])
    i+=1

# list inside list

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(len(matrix))

print(matrix[0])

# for loop inside for loop

for sublist in matrix:
    for i in sublist:
        print(i)

# obtain 5 in matrix
print(matrix[1][1])