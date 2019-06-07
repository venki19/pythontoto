file = open("demo.txt", "w")
file.write("this is a new line")
file.close()

file = open("demo.txt", "r")
print(file.read())
file.close()

file = open("demo.txt", "a")
file.write("This is the second line entered")
file.close()
