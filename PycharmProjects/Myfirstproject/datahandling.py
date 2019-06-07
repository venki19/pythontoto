class increment:
    __hiddenvarieable = 0


    def add(self, increment1):
        self.__hiddenvarieable += increment1
        print(self.__hiddenvarieable)


objectone = increment()
objectone.add(10)



