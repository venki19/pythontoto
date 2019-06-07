
class students:

 # define the attributes.

     def __init__(self, name, contact):
         self.name = name
         self.contact = contact

     def getdata(self):
         print("Accepting data")
         self.name = input("Enter name")
         self.contact = input("Enter contact")

     def putdata(self):
         print('The name is :'+self.name, 'The is contact is :'+self.contact)


venki = students("blank", 0)
venki.getdata()
venki.putdata()