
numbers = list(range (1,10))

print(numbers)

numbers = list(range(1,10,2))

print(numbers)

numbers = list(range(2,100,2))

print(numbers)

import time
import random

for i in range(5):
    print("Hello")

wait_time = random.randint(1, 60)
time.sleep(wait_time)
