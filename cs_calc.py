## Santosh Khadka
## CS Calc - main file
from tkinter import *

## Root needs to be created FIRST - Root Options
root = Tk()
root.title("CS Calculator")
# Icon
root.iconbitmap('cs_calc.ico')
# Window Size: root.geometry('500x600')
root.geometry()
# Stops windows size from being changeable
root.resizable(width=False, height=False)
#root.configure(bg = 'gray24')

## Width and Height for Buttons
#paddingx = 45; paddingy = 30
btnWidth=9
btnHeight=3

randomInt_min = 1
randomInt_max = 6

num1 = 0
num2 = 0
mathCheck = ''

# Colors
equalButtonnColor = 'spring green'
numberButtonColor = 'light goldenrod'
trigButtonColor = 'peach puff'
moreMathButtonColor = 'MediumPurple1'
basicMathButtonColor = 'LightSkyBlue1'
nonNumbersButtonColor = 'DarkOliveGreen1'

## Functions
# Clear Entry box
def clearEntryBox():
    inputBox.delete(0, END) 
# Input number
def writeNum(number):
    inputBox.insert(END, number) #(location, variable)
# Equal sign
def giveOutput():
    n2 = int(inputBox.get())
    clearEntryBox()

    if (mathCheck == '+'):
        inputBox.insert(0, num1 + n2) 
    elif(mathCheck == '-'):
        inputBox.insert(0, num1 - n2)
    elif(mathCheck == '*'):
        inputBox.insert(0, num1 * n2)
    elif(mathCheck == '/'):
        inputBox.insert(0, num1 / n2)
## 
## Mathematical Functions
def addFunct():
    global num1 
    global mathCheck
    num1 = int(inputBox.get())
    clearEntryBox()
    mathCheck = '+'
def subtFunct():
    global num1 
    global mathCheck
    num1 = int(inputBox.get())
    clearEntryBox()
    mathCheck = '-'
def multFunct():
    global num1 
    global mathCheck
    num1 = int(inputBox.get())
    clearEntryBox()
    mathCheck = '*'
def diviFunct():
    global num1 
    global mathCheck
    num1 = int(inputBox.get())
    clearEntryBox()
    mathCheck = '/'

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
button_0 = Button(root, bg=numberButtonColor, text="0", width=btnWidth, height=btnHeight, command=lambda: writeNum(0))
button_1 = Button(root, bg=numberButtonColor, text="1", width=btnWidth, height=btnHeight, command=lambda: writeNum(1))
button_2 = Button(root, bg=numberButtonColor, text="2", width=btnWidth, height=btnHeight, command=lambda: writeNum(2))
button_3 = Button(root, bg=numberButtonColor, text="3", width=btnWidth, height=btnHeight, command=lambda: writeNum(3))
button_4 = Button(root, bg=numberButtonColor, text="4", width=btnWidth, height=btnHeight, command=lambda: writeNum(4))
button_5 = Button(root, bg=numberButtonColor, text="5", width=btnWidth, height=btnHeight, command=lambda: writeNum(5))
button_6 = Button(root, bg=numberButtonColor, text="6", width=btnWidth, height=btnHeight, command=lambda: writeNum(6))
button_7 = Button(root, bg=numberButtonColor, text="7", width=btnWidth, height=btnHeight, command=lambda: writeNum(7))
button_8 = Button(root, bg=numberButtonColor, text="8", width=btnWidth, height=btnHeight, command=lambda: writeNum(8))
button_9 = Button(root, bg=numberButtonColor, text="9", width=btnWidth, height=btnHeight, command=lambda: writeNum(9))

button_addi = Button(root, bg=basicMathButtonColor, text="+", width=btnWidth, height=btnHeight, command=addFunct)
button_mult = Button(root, bg=basicMathButtonColor, text="*", width=btnWidth, height=btnHeight, command=multFunct)
button_subt = Button(root, bg=basicMathButtonColor, text="-", width=btnWidth, height=btnHeight, command=subtFunct)
button_divi = Button(root, bg=basicMathButtonColor, text="x/y", width=btnWidth, height=btnHeight, command=diviFunct)

# Equal (=) Button, Clear, BackOne, Decimal, Pi, RandomInt, POSorNEG
button_equal = Button(root, bg=equalButtonnColor, text="=", width=btnWidth, height=btnHeight+2, pady=14, command=giveOutput)
button_clear = Button(root, bg=nonNumbersButtonColor, text="CLEAR", width=btnWidth, height=btnHeight, command=clearEntryBox)
button_back1 = Button(root, bg=nonNumbersButtonColor, text="<-", width=btnWidth, height=btnHeight, command=clearEntryBox)
button_decimal = Button(root, bg=numberButtonColor, text=".", width=btnWidth, height=btnHeight, command=clearEntryBox)
button_pi = Button(root, bg=numberButtonColor, text="pi", width=btnWidth, height=btnHeight, command=clearEntryBox)
button_randomInt = Button(root, bg=nonNumbersButtonColor, text="RANDOM", width=btnWidth, height=btnHeight, command=clearEntryBox)
button_POSorNEG = Button(root, bg=basicMathButtonColor, text="+/-", width=btnWidth, height=btnHeight)

# More Math Buttons
button_square = Button(root, bg=moreMathButtonColor, text="x^2", width=btnWidth, height=btnHeight)
button_squareRoot= Button(root, bg=moreMathButtonColor, text="sqrRoot(x)", width=btnWidth, height=btnHeight)
button_cube = Button(root, bg=moreMathButtonColor, text="x^3", width=btnWidth, height=btnHeight)
button_10powerx = Button(root, bg=moreMathButtonColor, text="10^x", width=btnWidth, height=btnHeight)
button_log = Button(root, bg=moreMathButtonColor, text="log", width=btnWidth, height=btnHeight)
button_ln = Button(root, bg=moreMathButtonColor, text="ln", width=btnWidth, height=btnHeight)
button_factorial = Button(root, bg=moreMathButtonColor, text="n!", width=btnWidth, height=btnHeight)

button_sin = Button(root, bg=trigButtonColor, text="sin", width=btnWidth, height=btnHeight)
button_cos = Button(root, bg=trigButtonColor, text="cos", width=btnWidth, height=btnHeight)
button_tan = Button(root, bg=trigButtonColor, text="tan", width=btnWidth, height=btnHeight)
#button_sec = Button(root, text="sec", width=btnWidth, height=btnHeight)
#button_csc = Button(root, text="csc", width=btnWidth, height=btnHeight)
#button_cot = Button(root, text="cot", width=btnWidth, height=btnHeight)

button_div = Button(root, bg=moreMathButtonColor, text="div", width=btnWidth, height=btnHeight)
button_mod = Button(root, bg=moreMathButtonColor, text="mod", width=btnWidth, height=btnHeight)
button_xpowery = Button(root, bg=moreMathButtonColor, text="x^y", width=btnWidth, height=btnHeight)

## GRIDS
# Grid Template: button_name.grid(row=, column=)
# Menu bar grid  
label_File.grid(row=0, column=0)
label_Edit.grid(row=0, column=1)
label_Tab.grid(row=0, column=2)
label_View.grid(row=0, column=3)
label_change1.grid(row=0, column=4)

# Entry box grid 
inputBox.grid(ipady=20, row=1, column=0, columnspan=5)

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
button_xpowery.grid(row=3, column=0)
button_randomInt.grid(row=2, column=0)
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
button_sin.grid(row=3, column=1); button_cos.grid(row=3, column=2); button_tan.grid(row=3, column=3)
button_pi.grid(row=2, column=1)
button_factorial.grid(row=2, column=2)
button_clear.grid(row=2, column=3)
button_10powerx.grid(row=4, column=1)
button_div.grid(row=4, column=2)
button_mod.grid(row=4, column=3)

#button_.grid(row=, column=)


## GUI program is constantly looping to check for changes - Loop created
root.mainloop()

def main():
    return