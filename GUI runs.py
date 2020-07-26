#GUI runs
from tkinter import *
window=Tk()
window.title("Welcome to my_python_world")
window.geometry('350x200')
lbl = Label(window,text="Hello world")
lbl.grid(column=0,row=0)
txt=Entry(window,width=10)
txt.grid(column=1,row=0)
def clicked():
    lbl.configure(text="Button was clicked!!")
btn = Button(window,text="click me" ,command=clicked)
btn.grid(column=2,row=0)
window.mainloop()
