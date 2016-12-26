#import tkinter
#Author: Prashant Nair
#tkdocs.com for documentation
#Python3 is import  Tkinter

#load all for our case

from Tkinter import *

#Window and Widgets

window=Tk()
#Create widget in between the code

b1=Button(window,text="Execute")
#b1.pack()
b1.grid(row=0,column=0) # more control in widget position

e1=Entry(window)  # Kind of textbox
e1.grid(row=0,column=1)

t1=Text(window) #height=1,width=20
t1.grid(row=0,column=2)

window.mainloop()
