#Define is palindrome function that take one word in string as input
# and return True if it is palindrome else return False
# palindrome word that reads same backwards as forwards:
#example
#is_palindrome("madam") -----> True
#is_palindrome("naman") -----> True
#is_palindrome("horse") -----> False

# logic (algorithm) 
# step 1-> reverse the string
# step 2-> compare reversed string with original string

def is_palindrome(string):
    if string==string[::-1]:
        return True
    return False

print(is_palindrome("madam"))
print(is_palindrome("naman"))
print(is_palindrome("horse"))

# Or


def is_palindrome_check(string):
    return (string==string[::-1])

print(is_palindrome_check("madam"))
print(is_palindrome_check("naman"))
print(is_palindrome_check("horse"))