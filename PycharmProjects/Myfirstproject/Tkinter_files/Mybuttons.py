from tkinter import *


class Mybuttons:

    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()


        self.printbutton = Button(frame, text="Click Here", command=self.printmessage)
        self.printbutton.pack()

        self.quitbutton = Button(frame, text="Exit", command=frame.quit)
        self.quitbutton.pack(side=LEFT)


    def printmessage(self):
        print("Button clicked")

root = Tk()

b = Mybuttons(root)

root.mainloop()

