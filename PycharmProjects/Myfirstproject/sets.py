numbers = {1, 2, 4, 6, 8, 9}

numbers.add(3)
numbers.remove(6)
print(numbers)


# Union of sets : displays all the contents of both a & b with ut duplicates

seta = {1, 2, 3, 4, 5}
setb = {4, 5, 6, 7, 8}

print(seta | setb)

# inter section on sets : displays only which are common entries in both sets

print(seta & setb)

# difference operation

print(seta - setb)