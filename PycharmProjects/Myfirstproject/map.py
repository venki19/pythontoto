def add(x):
    return x+2

numbers = (10, 20, 30, 40, 60)

result = list(map(add, numbers))

print(result)


result1 = list(map(lambda x:x*2, numbers))

print(result1)