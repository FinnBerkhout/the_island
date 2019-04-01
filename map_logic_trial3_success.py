from tkinter import *
window = Tk()

#variable is stored in the root object
x = 5
y = 5

def A_press():
    global x
    x += 1
    L['text'] = 'X:' + str(x)

def B_press():
    global x
    x -= 1
    L['text'] = 'X:' + str(x)

def C_press():
    global y
    y += 1
    M['text'] = 'Y:' + str(y)

def D_press():
    global y
    y -= 1
    M['text'] = 'Y:' + str(y)

def E_press():
    global x,y
    x = 5
    y = 5
    L['text'] = 'X:' + str(x)
    M['text'] = 'Y:' + str(y)
        
buttA = Button(window, text="North", command=A_press)
buttA.pack()

buttB = Button(window, text="South", command=B_press)
buttB.pack()

buttC = Button(window, text="East", command=C_press)
buttC.pack()

buttD = Button(window, text="West", command=D_press)
buttD.pack()

buttE = Button(window, text="Go Home", command=E_press)
buttE.pack()


L = Label(window, text="X:5")
L.pack()

M = Label(window, text="Y:5")
M.pack()


window.mainloop()
