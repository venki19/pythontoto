from tkinter import *
import parser
import sys

root = Tk()
root.title('Calculator')
#root.config(bg="Gray")
#root.geometry("250x160+300+300")
i = 0


def get_variables(num):
    global i
    display.insert(i, num)
    i += 1


def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")


def factorial():
    complete_string = display.get()
    number = int(complete_string)
    fact = 1
    counter = number
    try:
        while counter > 0:
            fact = fact*counter
            counter -= 1
        clear_all()
        display.insert(0, fact)
    except Exception:
        clear_all()
        display.insert(0, "Error")

def get_operator(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i+=length

def clear_all():
    display.delete(0, END)


def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()

root.columnconfigure(0, pad=3)
root.columnconfigure(1, pad=3)
root.columnconfigure(2, pad=3)
root.columnconfigure(3, pad=3)
root.columnconfigure(4, pad=3)

root.rowconfigure(0, pad=3)
root.rowconfigure(1, pad=3)
root.rowconfigure(2, pad=3)
root.rowconfigure(3, pad=3)

# adding the input field
display = Entry(root, justify=LEFT, width=23, font="Times 16 bold")
display.grid(row=0, column=0, columnspan=8, padx=30, pady=30, sticky=W+E)


# adding buttons to the calculator
one = Button(root, text='1', command=lambda: get_variables(1), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="orange").grid(row=2, column=0)
Button(root, text='2', command=lambda: get_variables(2), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="orange").grid(row=2, column=1)
Button(root, text='3', command=lambda: get_variables(3), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="orange").grid(row=2, column=2)

Button(root, text='4', command=lambda: get_variables(4), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="orange").grid(row=3, column=0)
Button(root, text='5', command=lambda: get_variables(5), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="orange").grid(row=3, column=1)
Button(root, text='6', command=lambda: get_variables(6), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="orange").grid(row=3, column=2)

Button(root, text='7', command=lambda: get_variables(7), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="orange").grid(row=4, column=0)
Button(root, text='8', command=lambda: get_variables(8), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="orange").grid(row=4, column=1)
Button(root, text='9', command=lambda: get_variables(9), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="orange").grid(row=4, column=2)

# adding other buttons to the calculator
Button(root, text='AC', command=lambda: clear_all(), font=("Calibri", 12), foreground="RED", height =2,width=4,padx=10, pady = 10, bg="Green").grid(row=5, column=0)
Button(root, text='0', command=lambda: get_variables(0), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="orange").grid(row=5, column=1)
Button(root, text='=', command=lambda: calculate(), font=("Calibri", 12), foreground="RED", height =2,width=4,padx=10, pady = 10, bg="Green").grid(row=5, column=2)

Button(root, text='+', command=lambda: get_operator("+"), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="Blue").grid(row=2, column=3)
Button(root, text='-', command=lambda: get_operator("-"), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="Blue").grid(row=3, column=3)
Button(root, text='*', command=lambda: get_operator("*"), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="Blue").grid(row=4, column=3)
Button(root, text='/', command=lambda: get_operator("/"), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="Blue").grid(row=5, column=3)

# adding new operations
Button(root, text='pi', command=lambda: get_operator("*3.14"), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="grey").grid(row=2, column=4)
Button(root, text='%', command=lambda: get_operator("%"), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="grey").grid(row=3, column=4)
Button(root, text='(', command=lambda: get_operator("("), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="grey").grid(row=4, column=4)
Button(root, text='exp', command=lambda: get_operator("**"), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="grey").grid(row=5, column=4)

Button(root, text='<-', command=lambda: undo(), font=("Calibri",12), foreground="RED", height =2,width=4,padx=10, pady = 10, bg="Green").grid(row=2, column=5)
Button(root, text='X!', command=lambda: factorial(), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="Light Blue").grid(row=3, column=5)
Button(root, text=')', command=lambda: get_operator(")"), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="Light Blue").grid(row=4, column=5)
Button(root, text='^X', command=lambda: get_operator("**2"), font=("Calibri",12), height =2,width=4,padx=10, pady = 10, bg="Light Blue").grid(row=5, column=5)

root.mainloop()
