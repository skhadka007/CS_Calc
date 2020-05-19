## Santosh Khadka
## testing out various features here

from tkinter import *

root = Tk()

## creating a label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is John Elder")

## using grid system
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

## putting onto screen - pack into the window only as big as the 'myLabel' needs
# myLabel.pack()

root.mainloop()
