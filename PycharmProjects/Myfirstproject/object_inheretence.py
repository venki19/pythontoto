class Computer:

    def __init__(self, ram, memory, processor):
        self.ram = ram
        self.memory = memory
        self.processor = processor

    def getspecs(self):
        print('Please enter details')
        self.ram = input("Enter ram size")
        self.memory = input("Enter memory")
        self.processor = input("Enter processor")

    def displayspecs(self):
        print('Here are the specs of the computer')
        print('ram size is :'+self.ram, 'memory is :'+self.memory, 'processor is :'+self.processor)

class Desktop(Computer):
    def __init__(self, casecolour):
        self.casecolour = casecolour

    def getcasecolour(self):
        self.casecolour = input("Enter case colour")

    def putcasecolour(self):
        print('The case colour is :'+self.casecolour)

class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight

    def getweight(self):
        self.weight = input("Enter weight")

    def putweight(self):
        print('The weight is :'+self.weight)

comp = Laptop('');
comp1 = Desktop('');

comp.getspecs()
comp.getweight()
comp1.getcasecolour()
comp.displayspecs()
comp.putweight()
comp1.putcasecolour()
