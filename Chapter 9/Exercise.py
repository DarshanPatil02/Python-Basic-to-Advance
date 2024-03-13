# Problem 1
# define a function that takes alist of String 
# Return a list containing reverese of string in list

def reverse_list(ls):
    reverse = [i[::-1] for i in ls]
    return reverse

print(reverse_list(["abc","tuv","xyz"]))

# Problem 2
# num to string
# define a function which take a list containing any datatypes and return int and float in str format

def find_numbers(lst):
    return [str(i) for i in lst if (type(i)==int or type(i)==float)]
    
l1 = [True, False, [1,2,3],1,2.6,8]
print(find_numbers(l1))
