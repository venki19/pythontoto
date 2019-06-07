class students:

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def getdate(self):
        print("Accepting date")
        self.name = input("Enter name")
        self.contact = input("Enter contact")

    def putdata(self):
        print("The name is : "+self.name, "the contact is : "+self.contact)


class science_students(students):

    def __init__(self, age):
        self.age = age

    # def age(self):
      #  self.age = input("Enter age")

    def science(self):
        print('I am a science student & my age is : '+self.age)


venki = science_students("20")
# venki.age()
venki.science()
venki.getdate()
venki.putdata()