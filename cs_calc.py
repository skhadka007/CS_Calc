3## Santosh Khadka
## CS Calc - main file
from tkinter import *

## Width and Height for Buttons
#paddingx = 45; paddingy = 30
btnWidth=9; btnHeight=2
randomInt_min = 1; randomInt_max = 6

def clearInput():
    inputBox = Entry(root, text="", borderwidth=2, width=59)
    inputBox.grid(row=1, column=0, columnspan=5)

## Root needs to be created FIRST
root = Tk()

## Entry Box
inputBox = Entry(root, text="", borderwidth=2, width=59) #width=70

## Menu Bar
label_File = Label(root, text="File")
label_Edit = Label(root, text="Edit")
label_View = Label(root, text="View")
label_Tab = Label(root, text="Tab")
label_change1 = Label(root, text="    ")

# Button template
#button_ = Button(root, text="", width=btnWidth, height=btnHeight)

## Buttons: Digits 0-9, +x-%=, clear, x^2, x^3, 10^x, log, ln, n!, (), +/-, ., etc.
# Numerical Buttons
button_0 = Button(root, text="0", width=btnWidth, height=btnHeight)
button_1 = Button(root, text="1", width=btnWidth, height=btnHeight)
button_2 = Button(root, text="2", width=btnWidth, height=btnHeight)
button_3 = Button(root, text="3", width=btnWidth, height=btnHeight)
button_4 = Button(root, text="4", width=btnWidth, height=btnHeight)
button_5 = Button(root, text="5", width=btnWidth, height=btnHeight)
button_6 = Button(root, text="6", width=btnWidth, height=btnHeight)
button_7 = Button(root, text="7", width=btnWidth, height=btnHeight)
button_8 = Button(root, text="8", width=btnWidth, height=btnHeight)
button_9 = Button(root, text="9", width=btnWidth, height=btnHeight)

button_addi = Button(root, text="+", width=btnWidth, height=btnHeight)
button_mult = Button(root, text="*", width=btnWidth, height=btnHeight)
button_subt = Button(root, text="-", width=btnWidth, height=btnHeight)
button_divi = Button(root, text="%", width=btnWidth, height=btnHeight)

# Equal (=) Button, Clear, BackOne, Decimal, Pi, RandomInt
button_equal = Button(root, text="=", width=btnWidth, height=btnHeight+3, command=clearInput)
button_clear = Button(root, text="CLEAR", width=btnWidth, height=btnHeight, command=clearInput)
button_back1 = Button(root,text="<-", width=btnWidth, height=btnHeight, command=clearInput)
button_decimal = Button(root, text=".", width=btnWidth, height=btnHeight, command=clearInput)
button_pi = Button(root, text="pi", width=btnWidth, height=btnHeight, command=clearInput)
button_randomInt = Button(root, text="RANDOM", width=btnWidth, height=btnHeight, command=clearInput)

# More Math Buttons
button_square = Button(root, text="x^2", width=btnWidth, height=btnHeight)
button_squareRoot= Button(root, text="sqrRoot(x)", width=btnWidth, height=btnHeight)
button_cube = Button(root, text="x^3", width=btnWidth, height=btnHeight)
button_10powerx = Button(root, text="10^x", width=btnWidth, height=btnHeight)
button_log = Button(root, text="log", width=btnWidth, height=btnHeight)
button_ln = Button(root, text="ln", width=btnWidth, height=btnHeight)
button_factorial = Button(root, text="n!", width=btnWidth, height=btnHeight)
button_POSorNEG = Button(root, text="+/-", width=btnWidth, height=btnHeight)

button_sin = Button(root, text="sin", width=btnWidth, height=btnHeight)
button_cos = Button(root, text="cos", width=btnWidth, height=btnHeight)
button_tan = Button(root, text="tan", width=btnWidth, height=btnHeight)
#button_sec = Button(root, text="sec", width=btnWidth, height=btnHeight)
#button_csc = Button(root, text="csc", width=btnWidth, height=btnHeight)
#button_cot = Button(root, text="cot", width=btnWidth, height=btnHeight)

button_div = Button(root, text="div", width=btnWidth, height=btnHeight)
button_mod = Button(root, text="mod", width=btnWidth, height=btnHeight)
button_xpowery = Button(root, text="x^y", width=btnWidth, height=btnHeight)

## GRIDS
# Grid Template: button_name.grid(row=, column=)
# Menu bar grid  
label_File.grid(row=0, column=0)
label_Edit.grid(row=0, column=1)
label_Tab.grid(row=0, column=2)
label_View.grid(row=0, column=3)
label_change1.grid(row=0, column=4)

# Entry box grid
inputBox.grid(row=1, column=0, columnspan=5)

# Number Buttons grid AND +/- '.'
button_7.grid(row=5, column=1)
button_8.grid(row=5, column=2)
button_9.grid(row=5, column=3)

button_4.grid(row=6, column=1)
button_5.grid(row=6, column=2)
button_6.grid(row=6, column=3)

button_1.grid(row=7, column=1)
button_2.grid(row=7, column=2)
button_3.grid(row=7, column=3)

button_0.grid(row=8, column=1)

button_POSorNEG.grid(row=8, column=2)
button_decimal.grid(row=8, column=3)

# Grid for Column 0(first): xpowery, randInt, sqrRoot, x^2(square), x^3(cube), log, ln
button_xpowery.grid(row=2, column=0)
button_randomInt.grid(row=3, column=0)
button_squareRoot.grid(row=4, column=0)
button_square.grid(row=5, column=0)
button_cube.grid(row=6, column=0)
button_log.grid(row=7, column=0)
button_ln.grid(row=8, column=0)

# Grid for Column 4(last): BackOne, division, multiplication, addition, subtraction, EQUAL
button_back1.grid(row=2, column=4)
button_divi.grid(row=3, column=4)
button_mult.grid(row=4, column=4)
button_addi.grid(row=5, column=4)
button_subt.grid(row=6, column=4)
button_equal.grid(row=7, column=4, rowspan=2)

# sin, cos, tan, pi, n!(factorial), clear, 10^x, div, mod - grid
button_sin.grid(row=2, column=1); button_cos.grid(row=2, column=2); button_tan.grid(row=2, column=3)
button_pi.grid(row=3, column=1)
button_factorial.grid(row=3, column=2)
button_clear.grid(row=3, column=3)
button_10powerx.grid(row=4, column=1)
button_div.grid(row=4, column=2)
button_mod.grid(row=4, column=3)

#button_.grid(row=, column=)


## GUI program is constantly looping to check for changes - Loop created
root.mainloop()

