from tkinter import *
from random import *

window = Tk()






y = 5
x = 5


a = StringVar()
b = StringVar()
c = StringVar()
d = StringVar()
e = StringVar()

a.set("north")
b.set("south")
c.set("East")
d.set("West")
e.set("Go home")



def A_press():
    global y
    L['text'] = "Y:" + str(y)
    
def B_press():
    pass

def C_press():
    pass

def D_press():
    pass

def E_press():
    pass


xaxis = Label(window,text = "5").place(x = 10,y= 122)

L = Label(window,text = "5" ).place(x = 10,y= 90)

buttA = Button(window,textvariable = a, command= A_press,).place(x = 10,y = 297)
buttB = Button(window,textvariable = b, command= B_press,).place(x = 10,y = 262)
buttC = Button(window,textvariable = c, command= C_press,).place(x = 10,y = 227)
buttD = Button(window,textvariable = d, command= D_press,).place(x = 10,y = 192)
buttE = Button(window,textvariable = e, command= E_press,).place(x = 10,y = 157)

window.mainloop()
