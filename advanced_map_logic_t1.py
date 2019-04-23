from tkinter import *
from random import *
window = Tk()
width = window.winfo_screenwidth() 
height = window.winfo_screenheight()
window.geometry('%sx%s' % (width, height))

placeDES = StringVar()

y = 4
x = 4
starter = 1
destype = randint(0, 3)

placeDES.set("""you decide to head out on a journey.
there is a glint in your eye, a glint full of hope and wonder you gaze out on the forests and grasslands
""")


def a_press():
    global x
    x += 1
    L['text'] = 'X:' + str(x)
    locator()


def b_press():
    global x
    x -= 1
    L['text'] = 'X:' + str(x)
    locator()


def c_press():
    global y
    
    y += 1
    M['text'] = 'Y:' + str(y)
    locator()


def d_press():
    global y
    y -= 1
    M['text'] = 'Y:' + str(y)
    locator()


def e_press():
    global x, y
    x = 4
    y = 4
    L['text'] = 'X:' + str(x)
    M['text'] = 'Y:' + str(y)
    locator()


def locator():
    global destype
    if x >= 2 and x <= 5 and y >= 2 and y <= 3:
        if destype == 0:
            placeDES.set("You step out onto a grassland, green hills rolling out as far as the eye can, see you awe at the beauty of the place. you're hit with a wave of sadness as this is your prison cell, not a haven, it is the chamber that will spend the rest of your sad lonely days in.")
            destype = randint(0, 3)
    
        if destype == 1:
            placeDES.set("You look forth onto a sea of grass, as the waves of wind roll past the silky touch of the grass strokes your leg. The rabbits bound joyfully through the grass and the bees fly from flower to flower humming there own little tune.")
            destype = randint(0, 3)
                
        if destype == 2:
            placeDES.set("      You're in a grassland:                                  The sway of the grass entices you to move forward, its a sea, and it's never ending. you feel as if you could lie down and fall asleep on the long, soft grass. something in the distance hisses and you realise that the placid place could become a war zone at any moment.")
            destype = randint(0, 3)

        if destype == 3:
            placeDES.set("")
            destype = randint(0, 3)


placeID = Label(window, textvariable=placeDES, fg="black", wrap=250)
placeID.place(relx=0.1, rely=0.1)
buttA = Button(window, text="East", command=a_press)
buttA.pack()

buttB = Button(window, text="West", command=b_press)
buttB.pack()

buttC = Button(window, text="North", command=c_press)
buttC.pack()

buttD = Button(window, text="South", command=d_press)
buttD.pack()

buttE = Button(window, text="Go Home", command=e_press)
buttE.pack()


L = Label(window, text="X:4")
L.pack()

M = Label(window, text="Y:4")
M.pack()


window.mainloop()
