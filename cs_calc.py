## Santosh Khadka
## CS Calc - main file
from tkinter import *

## Root needs to be created FIRST
root = Tk()

## create the object/widget first then set it into the window
label_File = Label(root, text="File")
label_Edit = Label(root, text="Edit")
label_View = Label(root, text="View")
label_Tab = Label(root, text="Tab")

label_File.grid(row=0, column=0)
label_Edit.grid(row=0, column=1)
label_Tab.grid(row=0, column=2)
label_View.grid(row=0, column=3)


## GUI program is constantly looping to check for changes - so create loop
root.mainloop()

