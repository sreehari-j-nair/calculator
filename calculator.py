from tkinter import *

window = Tk()
window.title("Simple Calculator")

screen=Entry(window, width=45, borderwidth=7)
screen.grid(row=0, column=0, columnspan=3)

def button_click(number):
    current = screen.get()
    screen.delete(0,END)
    screen.insert(0, str(current)+str(number))

def button_clear():
    screen.delete(0,END)

def button_addition():
    firstnumber = screen.get()
    global  fnum
    global a
    a="addition"
    fnum = int(firstnumber)
    screen.delete(0,END)

def button_subtraction():
    firstnumber = screen.get()
    global  fnum
    global a
    a="subtraction"
    fnum = int(firstnumber)
    screen.delete(0,END)

def button_multiplication():
    firstnumber = screen.get()
    global  fnum
    global a
    a="multiplication"
    fnum = int(firstnumber)
    screen.delete(0,END)

def button_division():
    firstnumber = screen.get()
    global  fnum
    global a
    a="division"
    fnum = int(firstnumber)
    screen.delete(0,END)

def button_equalize():
    secondnumber = screen.get()
    screen.delete(0,END)

    if a=="addition" :
        screen.insert(0, fnum + int(secondnumber))

    if a=="subtraction" :
        screen.insert(0, fnum - int(secondnumber))

    if a=="multiplication" :
        screen.insert(0, fnum * int(secondnumber))

    if a=="division" :
        screen.insert(0, fnum / int(secondnumber))


button1=Button(window, text="1", padx=40, pady=20, command= lambda:button_click(1))
button2=Button(window, text="2", padx=40, pady=20, command= lambda: button_click(2))
button3=Button(window, text="3", padx=40, pady=20, command= lambda: button_click(3))
button4=Button(window, text="4", padx=40, pady=20,command= lambda: button_click(4))
button5=Button(window, text="5", padx=40, pady=20, command= lambda: button_click(5))
button6=Button(window, text="6", padx=40, pady=20, command= lambda: button_click(6))
button7=Button(window, text="7", padx=40, pady=20, command= lambda: button_click(7))
button8=Button(window, text="8", padx=40, pady=20, command= lambda: button_click(8))
button9=Button(window, text="9", padx=40, pady=20, command= lambda:button_click(9))
button0=Button(window, text="0", padx=40, pady=20, command= lambda:button_click(0))
button_add=Button(window, text="+",padx=39,pady=20, command=button_addition)
button_equal=Button(window, text="=",padx=134,pady=20, command= button_equalize)
button_clear=Button(window, text="Clear", padx=30,pady=20,command= button_clear)
button_subtract=Button(window, text="-",padx=40,pady=20, command=button_subtraction)
button_multiply=Button(window, text="*",padx=40,pady=20, command=button_multiplication)
button_divide=Button(window, text="%",padx=38,pady=20, command=button_division)


button1.grid(row=3,column=2)
button2.grid(row=3,column=1)
button3.grid(row=3,column=0)

button4.grid(row=2,column=2)
button5.grid(row=2,column=1)
button6.grid(row=2,column=0)

button7.grid(row=1,column=2)
button8.grid(row=1,column=1)
button9.grid(row=1,column=0)

button0.grid(row=4,column=1)
button_add.grid(row=4,column=0)
button_equal.grid(row=6,column=0,columnspan=3)
button_clear.grid(row=5,column=1)
button_subtract.grid(row=4,column=2)
button_multiply.grid(row=5,column=0)
button_divide.grid(row=5,column=2)

window.mainloop()
