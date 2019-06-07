def add(a, b):
    return a + b


def square(c):
    return c * c


def cube(d):
    return d * d * d


result = cube(square(add(2, 2)))
print(result)