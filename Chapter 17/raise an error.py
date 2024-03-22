# raise error
# NotImplementedError
# also called as Abstract error in Java

def add(a,b):
    return a+b
print(add(2,5))

# In above example if we pass string then it will not add then it will join
print(add('2','5'))
# But we don't want this, so therefore we raise a custom error

def add(a,b):
    if (type(a)==int and type(b)==int):
        return a+b
    raise TypeError("Oops! You pass wrong datatype to function")
print(add(2,5))
print(add('2','5'))

