from tkinter import *

master = Tk()

var = StringVar(master)
var.set("No-one")

drop=OptionMenu(master,var,"one","two","three")
drop.pack()

drop.place(x=300,y=300)
master.mainloop()