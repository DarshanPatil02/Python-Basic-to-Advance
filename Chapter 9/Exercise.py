# define a function that takes alist of String 
# Return a list containing reverese of string in list

def reverse_list(ls):
    reverse = [i[::-1] for i in ls]
    return reverse

print(reverse_list(["abc","tuv","xyz"]))
