## Santosh Khadka
## CS Calc - main file
from tkinter import *

def clearInput():
    inputBox = Entry(root, text="", borderwidth=2)
    inputBox.grid(row=1, column=0, columnspan=5)

## Root needs to be created FIRST
root = Tk()

## Entry Box
inputBox = Entry(root, text="", borderwidth=2, width=70)

## Menu Bar
label_File = Label(root, text="File")
label_Edit = Label(root, text="Edit")
label_View = Label(root, text="View")
label_Tab = Label(root, text="Tab")
label_change1 = Label(root, text="CHANGE")

## Buttons: Digits 0-9, +x-%=, clear, x^2, x^3, 10^x, log, ln, n!, (), +/-, .,  
button_0 = Button(root, text="0", padx=40, pady=30)
button_1 = Button(root, text="1", padx=40, pady=30)
button_2 = Button(root, text="2", padx=40, pady=30)
button_3 = Button(root, text="3", padx=40, pady=30)
button_4 = Button(root, text="4", padx=40, pady=30)
button_5 = Button(root, text="5", padx=40, pady=30)
button_6 = Button(root, text="6", padx=40, pady=30)
button_7 = Button(root, text="7", padx=40, pady=30)
button_8 = Button(root, text="8", padx=40, pady=30)
button_9 = Button(root, text="9", padx=40, pady=30)

button_addi = Button(root, text="+", padx=40, pady=30)
button_mult = Button(root, text="x", padx=40, pady=30)
button_subt = Button(root, text="-", padx=40, pady=30)
button_divi = Button(root, text="%", padx=40, pady=30)

button_equal = Button(root, text="=", command=clearInput)

button_square = Button(root, text="x^2", padx=40, pady=30)
button_cube = Button(root, text="x^3", padx=40, pady=30)
button_10x = Button(root, text="10^x", padx=40, pady=30)
button_log = Button(root, text="log", padx=40, pady=30)
button_ln = Button(root, text="ln", padx=40, pady=30)
button_factorial = Button(root, text="n!", padx=40, pady=30)
button_POSorNEG = Button(root, text="+/-", padx=40, pady=30)

button_sin = Button(root, text="sin", padx=40, pady=30)
button_cos = Button(root, text="cos", padx=40, pady=30)
button_tan = Button(root, text="tan", padx=40, pady=30)
button_sec = Button(root, text="sec", padx=40, pady=30)
button_csc = Button(root, text="csc", padx=40, pady=30)
button_cot = Button(root, text="cot", padx=40, pady=30)

button_decimal = Button(root, text=".", padx=40, pady=30)
button_clear = Button(root, text="C", padx=40, pady=30, command=clearInput)
button_pi = Button(root, text="pi", padx=40, pady=30)
button_div = Button(root, text="div", padx=40, pady=30)
button_mod = Button(root, text="mod", padx=40, pady=30)

# Entry box grid
inputBox.grid(row=1, column=0, columnspan=5)

# Menu bar grid  
label_File.grid(row=0, column=0)
label_Edit.grid(row=0, column=1)
label_Tab.grid(row=0, column=2)
label_View.grid(row=0, column=3)
label_change1.grid(row=0, column=4)

# Buttons grid
button_7.grid(row=2, column=1)
button_8.grid(row=2, column=2)
button_9.grid(row=2, column=3)

button_4.grid(row=3, column=1)
button_5.grid(row=3, column=2)
button_6.grid(row=3, column=3)

button_1.grid(row=4, column=1)
button_2.grid(row=4, column=2)
button_3.grid(row=4, column=3)
button_0.grid(row=5, column=1)

button_divi.grid(row=2, column=4)
button_mult.grid(row=3, column=4)
button_subt.grid(row=4, column=4)

button_POSorNEG.grid(row=5, column=2)
button_equal.grid(row=5, column=3)
button_addi.grid(row=5, column=4)

#button_.grid(row=, column=)
#button_.grid(row=, column=)


## GUI program is constantly looping to check for changes - Loop created
root.mainloop()

