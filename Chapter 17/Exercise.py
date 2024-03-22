# Make a function "divide"
# divide (a,b)
# print(divide(4,2))  ==> # 2
# print(divide(4,0))  ==> # please don't divide by zero (Zero division error)
# print(divide('4',2))  ==> # please input numbers only

def divide(num1,num2):
        try:
            return (num1/num2)
        except ZeroDivisionError:
            print("Please don't divide by zero")
        except TypeError:
            print("Please input numbers only")
        
print(divide(2,5))
print(divide(4,2))
print(divide(4,0))
print(divide('4',2))

def divide(num1,num2):
        try:
            return (num1/num2)
        except ZeroDivisionError as z:
            return z
        except TypeError as t:
             return t
        except:
             return "Unexpected error"
        
print(divide(2,5))
print(divide(4,2))
print(divide(4,0))
print(divide('4',2))