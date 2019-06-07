from tkinter import *

root = Tk()


def dosomething():
    print("You have clicked here")


button1 = Button(root, text='click here', command=dosomething, bg='red', fg='green')

button1.pack()

root.mainloop()

