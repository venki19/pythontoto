

product = {"apple":20, "banana":30, "orange":50}

accept = input("please enter product")

if(accept in product):
    print(product.get(accept))

else:
    print("product not available")


newlist = list(range(1, 100))

for x in newlist:

     if x % 2 != 0 :
         print(x)