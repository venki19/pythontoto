
newlist = (1, 3, 4, 8, 14, 17, 21, 25)

evenlist = list(filter(lambda x: x % 2 == 0, newlist))

oddlist = list(filter(lambda x: x % 2 != 0, newlist))

print(evenlist)

print(oddlist) 