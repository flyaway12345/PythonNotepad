from tkinter.constants import END, LEFT
from tkinter.filedialog import *
import tkinter as tk

def saveFile():
    new_file = asksaveasfile(mode = 'w',filetype = [('text files', '.txt')])
    if new_file is None:
        return
    text = str(textField.get(1.0, END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode = 'r', filetype = [('text files', '*.txt')])
    if file is not None:
        content = file.read()
    textField.insert(INSERT, content)

def clearFile():
    textField.delete(1.0, END)

canvas = tk.Tk() 
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg = "white")
topButtonSection = Frame(canvas)
topButtonSection.pack(padx = 10,pady = 5, anchor = 'nw')

openButton = Button(canvas, text="Open",bg ="white", command = openFile)
openButton.pack(in_ = topButtonSection, side=LEFT)

saveButton = Button(canvas, text="Save",bg ="white", command = saveFile)
saveButton.pack(in_ = topButtonSection, side=LEFT)

clearButton = Button(canvas, text="Clear",bg ="white", command = clearFile)
clearButton.pack(in_ = topButtonSection, side=LEFT)

exitButton = Button(canvas, text="Exit",bg ="white", command = exit)
exitButton.pack(in_ = topButtonSection, side=LEFT)

textField = Text(canvas,wrap = WORD, bg = "#F9DDA4", font = ("Arial",15))
textField.pack(padx =10,pady =5, expand = TRUE, fill = BOTH)

canvas.mainloop()