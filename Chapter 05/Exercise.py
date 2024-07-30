# Problem 1
# define a function which will take list containing numbers as input # and return list containing square of every elements

def square_of_numbers(list):
    squared_number = []
    for i in list:
        squared_number.append(i**2)
    return squared_number

numbers = list(range(1,11))

print(square_of_numbers(numbers))

# Problem 2
# define a function which will take list as a argument and this function #will return a reversed list
# Note you simply do this with reverse method or [-1]
# but try to do this with the help of append and return method

num = [1,2,3,4]
words = ["word1","word2","word3"]

def reverse(lists):
    lists.reverse()
    return lists

print(reverse(num))
print(reverse(words))

# OR
def reverse_list(list):
    return(list[::-1])

print(reverse_list(num))
print(reverse_list(words))

# OR
def reverse_list_2(list):
    reverse_list = []
    for i in range(1,(len(list)+1)):
        reverse_list.append(list[-i])
    return reverse_list

print(reverse_list_2(num))
print(reverse_list_2(words))

# OR 

def reverse_list_3(lists):
    reverse_list = []
    for i in range(len(lists)):
        popped_element = lists.pop()
        reverse_list.append(popped_element)
    return reverse_list

print(reverse_list_3(num))
print(reverse_list_3(words))

# Problem 3
# define a function that take list of words as argument and # return list with reverse of every element in that list
#example
#['abc', 'tuv', 'xyz'] -> ['cba', 'vut', 'zyx'] 

def reverse_element(lists):
    reverse_elements = []
    for i in range(len(lists)):
        var = lists[i][::-1]
        reverse_elements.append(var)
    return reverse_elements

elements = ['abc', 'tuv', 'xyz']
print(reverse_element(elements))

# OR 
def reverse_element(lists):
    reverse_elements = []
    for i in lists:
        reverse_elements.append(i[::-1])
    return reverse_elements

elements = ['abc', 'tuv', 'xyz']
print(reverse_element(elements))


# Problem 4
# filter odd even
# define a function
# input
# list ---> [1,2,3,4,5,6,7]
# ouput ----> [[1,3,5,7], [2,4,6]] 

def filter_odd_even(lists):
    even = []
    odd = []
    for i in range(len(lists)):
        if lists[i]%2==0:
            even.append(lists[i])
        else:
            odd.append(lists[i])
    return odd,even

numbers = [1,2,3,4,5,6,7]
filter_odd_even(numbers)

# OR

def filter_odd_even(lists):
    even = []
    odd = []
    for i in lists:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return odd,even

numbers = [1,2,3,4,5,6,7]
filter_odd_even(numbers)


# Problem 5
# common elements finder function
# define a functions which take 2 lists as input and return a list which contains common elements of both lists
# example
#input -> [1,2,5,8], [1,2,7,6]
#output [1,2]

def common_elements(l1,l2):
    common = []
    for i in l1:
        for j in l2:
            if i==j:
                common.append(i)
    return common

l1 = [1,2,5,8]
l2 = [1,2,7,6]
print(common_elements(l1,l2))

# OR

def common_finder(l1,l2):
    output = []
    for i in  l1:
        if i in l2:
            output.append(i)
    return output

l1 = [1,2,5,8]
l2 = [1,2,7,6]
print(common_finder(l1,l2))

# Problem 6
# function
# [1,2,3, [1,2], [3,4]], input
# type()

ls1 = [1,2,3, [1,2], [3,4]]

def sublist_counter(ls1):
    output = 0
    for i in ls1:
        if type(i)==list:
            output+=1
    return output

print(sublist_counter(ls1))

