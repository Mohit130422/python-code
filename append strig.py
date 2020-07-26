"""a=str(12)
b=str(8)
c=str(2019)
d=a+"/"+b+"/"+c
print(type(d))
print(d)"""

"""#get value from option menu
import tkinter as tk
from tkinter import messagebox
dt=""
def show(x):
    print(x)
    global dt
    dt=dt+str(x)+"/"
    messagebox.showinfo('selected value: ',str(x))

root=tk.Tk()
options=tk.StringVar()
menu=tk.OptionMenu(root,options,'delhi','aligarh','mathura',command=show)
menu.pack()
options.set('delhi')
root.mainloop()
print("dt=",dt)"""

from tkinter import *


def select():
    select = "Your are select the option:" + str(radio.get())
    label.configure(text=select)


top = Tk()
top.geometry("300x150")
radio = StringVar()
lab = Label(text="Favourite programming language:")
lab.pack()

r1 = Radiobutton(top, text="Male", variable=radio, value="Male", command=select)
r1.pack(anchor=W)

r2 = Radiobutton(top, text="Female", variable=radio, value="female", command=select)
r2.pack(anchor=W)

label = Label(top)
label.pack()
top.mainloop()
