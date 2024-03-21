# list vs generators
# Memory usage, time required
# When to use list, when to use generators

import time
t1 = time.time()
l = [i**2 for i in range(10000000)]  # 10 million
t2 = time.time()
print(f"Time taken to generate list l {t2-t1}")


t1 = time.time()
g = (i**2 for i in range(10000000))  # 10 million
t2 = time.time()
print(f"Time taken to generate generator g {t2-t1}")

# When to use list, when to use generators
# Ans: List is used when we need values in list again and again
# Ans: Generator is used when we not need values in generator again and again
