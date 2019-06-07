from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename

class menudiaplay:

    def __init__(self):
        self.exit = exit

    def function1(self):
     print("Menu is clicked")


    def openfile(self):
      name = askopenfilename()
      print(name)

    def function3(self):
       print("Undo is done")

    def exitfunc(self):
        self.exit = tkinter.messagebox.askquestion("Question", "Really want to exit")
        if self.exit == 'yes':
            self.root.destroy()
        else:
            print("Hello welcome back")


    root = Tk()

    mymenu = Menu(root)
    root.config(menu=mymenu)

    filesubmenu = Menu(mymenu)

    mymenu.add_cascade(label="File", menu=filesubmenu)

    filesubmenu.add_cascade(label="New Project", command=function1)
    filesubmenu.add_cascade(label="New", command=function1)
    filesubmenu.add_cascade(label="open File", command=askopenfilename)
    filesubmenu.add_cascade(label="Power save Mode", command=function1)
    filesubmenu.add_cascade(label="Exit", command=exitfunc)

    editsubmenu = Menu(mymenu)

    mymenu.add_cascade(label="Edit", menu=editsubmenu)

    editsubmenu.add_cascade(label="Undo", command=function3)

    toolbar = Frame(root, bg="light pink")
    insertbutton = Button(toolbar, text="Insert Files", command=function1)
    insertbutton.pack(side=LEFT, padx=2, pady=3)

    printbuttopn = Button(toolbar, text="Print", command=function1)
    printbuttopn.pack(side=LEFT, padx=2, pady=3)

    toolbar.pack(side=TOP, fill=X)

    status = Label(root, text="This is the status", bd=1, relief=SUNKEN, anchor=W)
    status.pack(side=BOTTOM, fill=X)

    root.mainloop()


b = menudiaplay()