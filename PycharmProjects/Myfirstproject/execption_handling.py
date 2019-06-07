def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("This is dive by zero error")
        return 0


x = float(input("Please Enter value a"))
y = float(input("please Enter value b"))
result = divide(x, y)
print(result)