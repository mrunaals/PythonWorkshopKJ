from Tkinter import *

#Window and Widgets

window=Tk()
#Create widget in between the code
def squar():
    #print("Success")
    print(e1_value.get())
    sqdata=int(e1_value.get())*2
    t1.insert(END,sqdata)

b1=Button(window,text="Execute",command=squar) # Dont pass () for function
#b1.pack()
b1.grid(row=0,column=0) # more control in widget position

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)  # Kind of textbox , textvariable
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20) #height=1,width=20
t1.grid(row=0,column=2)

window.mainloop()
