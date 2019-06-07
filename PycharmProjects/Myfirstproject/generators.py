
def function():
    counter = 0
    while counter < 5:
        yield counter
        counter += 1


for x in function():
        print(x)


def even_number(x):

    for i in range(x):
        if x % 2 == 0:
            yield i 


print(list(even_number(20)))
