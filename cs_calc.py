## Santosh Khadka
## CS Calc - main file
from tkinter import *

def clearInput():
    inputBox = Entry(root, text="", borderwidth=2)
    inputBox.grid(row=1, column=0, columnspan=5)

## Root needs to be created FIRST
root = Tk()

## Entry Box
inputBox = Entry(root, text="", borderwidth=2)

## Menu Bar
label_File = Label(root, text="File")
label_Edit = Label(root, text="Edit")
label_View = Label(root, text="View")
label_Tab = Label(root, text="Tab")
label_change1 = Label(root, text="CHANGE")

## Buttons: Digits 0-9, +x-%=, clear, x^2, x^3, 10^x, log, ln, n!, (), +/-, .,  
button_0 = Button(root, text="0")
button_1 = Button(root, text="1")
button_2 = Button(root, text="2")
button_3 = Button(root, text="3")
button_4 = Button(root, text="4")
button_5 = Button(root, text="5")
button_6 = Button(root, text="6")
button_7 = Button(root, text="7")
button_8 = Button(root, text="8")
button_9 = Button(root, text="9")

button_addi = Button(root, text="+")
button_mult = Button(root, text="x")
button_subt = Button(root, text="-")
button_divi = Button(root, text="%")

button_equal = Button(root, text="=", command=clearInput)

button_square = Button(root, text="x^2")
button_cube = Button(root, text="x^3")
button_10x = Button(root, text="10^x")
button_log = Button(root, text="log")
button_ln = Button(root, text="ln")
button_factorial = Button(root, text="n!")
button_POSorNEG = Button(root, text="+/-")

button_sin = Button(root, text="sin")
button_cos = Button(root, text="cos")
button_tan = Button(root, text="tan")
button_sec = Button(root, text="sec")
button_csc = Button(root, text="csc")
button_cot = Button(root, text="cot")

button_decimal = Button(root, text=".")
button_clear = Button(root, text="C", command=clearInput)
button_pi = Button(root, text="pi")
button_div = Button(root, text="div")
button_mod = Button(root, text="mod")

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

