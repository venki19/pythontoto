from tkinter import *

root = Tk()

label1 = Label(root, text="First Name", bg="red", fg="white")
label2 = Label(root, text="Last Name", bg="blue", fg="green")


label1.pack(fill=X)
label2.pack(side=LEFT, fill=Y)

root.mainloop()