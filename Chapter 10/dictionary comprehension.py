# dictionary comprehension
# Square = {1:1,2:4,3:9}
square = {num:num**2 for num in range(1,5)}
print(square)

square1 = {f"Square of {num} is":num**2 for num in range(1,5)}
print(square1)

for k,v in square1.items():
    print(k, v)

string = "Darshan"    
word_count = {i:string.count(i) for i in string}
print(word_count)

odd_even = {i:("Even" if i%2==0 else "odd") for i in range(1,11)}
print(odd_even)

