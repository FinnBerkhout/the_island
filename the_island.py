from tkinter import *
from random import *
#######################################
window = Tk()
window.title("The Island")
window.configure(bg = "black")
width = window.winfo_screenwidth() 
height = window.winfo_screenheight()
window.geometry('%sx%s' % (width, height))
########################################
hunger = StringVar()
thirst = StringVar()
health = StringVar()
energy = StringVar()
Inventory = StringVar()
TEXT = StringVar()
AXE = StringVar()
PICKAXE = StringVar()
SWORD = StringVar()
Op_A = StringVar()
Op_B = StringVar()
Op_C = StringVar()
Op_D = StringVar()
Op_E = StringVar()
Op_F = StringVar()
AXE.set('Flint Axe')

place_counter = 1

#######################################
def opa():
    global TEXT,place_counter,AXE,PICKAXE,SWORD
    
    if place_counter == 1:
        TEXT.set("As you run away from the sound you look behind to catch a glimpse of what happened while you're doing it you run into a wall,but its not a wall its a door. The door opens and light seeps through illuminating the room you're in. you look behind you just in time to see a small mouse go through a crack in the wall you see what the mouse knocked over… its a book.")
        place_counter = 2
        Op_A.set("Option A: Leave")
        Op_B.set("Option B: Read the book")
                 
    elif place_counter == 2:
        TEXT.set("You Stand up and make your way through the door, As your eyes adjust to the light you see lush forests and some beautiful grasslands. But as you look further you notice sand and water. You’re on an island and you’re alone, with nobody. You slowly come to realize that nobody will come and save you so this will be your home for the next… you realise that you probably won’t be leaving here alive...  ")
        place_counter = 4
        Op_A.set("Option A: Go back inside")
        Op_B.set("Option B: Explore")

    elif place_counter == 3:
        place_counter = 5
        TEXT.set("You pick up the book and open it. It’s blank. You go to put it down again but then all of a sudden, a note falls out, it says: Where am I, who am I, what is this place, who put me here. Is there anyone else?  Why do I exist?The bottom of the note is marked with a cross.You sit the book down neatly back where it came from. Something beside it glints in the light it a flint axe.Next you?")
        AXE.set('Flint Axe')
        Op_A.set('Option A:go outside')
        Op_B.set('Option B:look more closly at this area')
        Op_C.set('Option C: search a different part of the house')
##                 
def opb():
    global TEXT,place_counter,AXE,PICKAXE,SWORD
                 
    if place_counter == 1:
        TEXT.set("While you stumble towards the object you trip over a pile of wood falling flat of your face… there’s a gust of wind and and a door creaks open. You stand up wondering what made that noise. As light floods the room exposing the contents, you see what made the noise, a book.")
        place_counter = 3
        Op_A.set("Option A: Read the book")
        Op_B.set("Option B: forget about the book for now")      
    elif place_counter == 2:
        TEXT.set("You Decide to read the book that has fallen over before venturing outside. As you open the book a note falls out. It Reads:Where am I, who am I, what is this place, who put me here. Is there anyone else?  Why do I exist?The bottom of the note is marked with a cross... You notice a small shimmer of light in the corner where the book came from it’s a small flint axe it’s slightly blunt, but it will do for now.Now you decide to?")
        place_counter = 5
        Op_A.set('Option A:go outside')
        Op_B.set('Option B:look more closly at this area')
        Op_C.set('Option C: search a different part of the house')
        AXE.set('Flint Axe')
        

    elif place_counter == 3:
        place_counter = 7
        TEXT.set('You Stand up and make your way through the door, as your eyes adjust to the light you see lush forests and some beautiful grasslands. But as you look further you notice sand and water. You’re on an island and you’re alone, with nobody. You slowly come to realize that nobody will come and save you so this will be your home for the next… you realise that you probably won’t be leaving here alive... You step down onto the grass and look behind you. You see the rickety house, it looks like it was thrown together in a hurry and then whoever made it tried to fix it up, it’s very very old and battered. You look down next to you and you see a crude stone pickaxe and a dull short sword that looks like its made of copper.')
        Op_A.set('Option A: Explore the island')
        Op_B.set('Option B:go back inside to see if you can find anything new')
        Op_C.set('Option C: look at the outside of the house')
        PICKAXE.set('Stone pickaxe')
        SWORD.set('copper short-sword')
##
def opc():
    global TEXT,place_counter,AXE,PICKAXE,SWORD
    if place_counter == 1:
        TEXT.set("You wake up... With no memory of who you are,where you've been or where you are now. you start to get up... BANG something falls to the floor on your right and a creature scuttles away. What do you do?")



##    
def opd():
    global TEXT,place_counter,AXE,PICKAXE,SWORD
    if place_counter == 1:
        TEXT.set("You wake up... With no memory of who you are,where you've been or where you are now. you start to get up... BANG something falls to the floor on your right and a creature scuttles away. What do you do?")
        place_counter = 1

    elif place_counter == 2:
        TEXT.set("You Decide to read the book that has fallen over before venturing outside. As you open the book a note falls out. It Reads:Where am I, who am I, what is this place, who put me here. Is there anyone else?  Why do I exist?The bottom of the note is marked with a cross. You notice a small shimmer of light in the corner where the book came from it’s a small flint axe it’s slightly blunt, but it will do for now.Now you decide to?")
        place_counter = 2



##
def ope():
    global TEXT,place_counter,AXE,PICKAXE,SWORD
    if place_counter == 1:
        TEXT.set("You wake up... With no memory of who you are,where you've been or where you are now. you start to get up... BANG something falls to the floor on your right and a creature scuttles away. What do you do?")
        place_counter = 1

    elif place_counter == 2:
        TEXT.set("You Decide to read the book that has fallen over before venturing outside. As you open the book a note falls out. It Reads:Where am I, who am I, what is this place, who put me here. Is there anyone else?  Why do I exist?The bottom of the note is marked with a cross. You notice a small shimmer of light in the corner where the book came from it’s a small flint axe it’s slightly blunt, but it will do for now.Now you decide to?")
        place_counter = 2



##
def opf():
    global TEXT,place_counter,AXE,PICKAXE,SWORD
    if place_counter == 1:
        TEXT.set("You wake up... With no memory of who you are,where you've been or where you are now. you start to get up... BANG something falls to the floor on your right and a creature scuttles away. What do you do?")
        place_counter = 1

    elif place_counter == 2:
        TEXT.set("You Decide to read the book that has fallen over before venturing outside. As you open the book a note falls out. It Reads:Where am I, who am I, what is this place, who put me here. Is there anyone else?  Why do I exist?The bottom of the note is marked with a cross. You notice a small shimmer of light in the corner where the book came from it’s a small flint axe it’s slightly blunt, but it will do for now.Now you decide to?")
        place_counter = 2








###########################################################################
def destroy(): 
    global health, thrist, energy, hunger, TEXT, Inventory, AXE, PICKAXE, SWORD
 
    TEXT.set("You wake up... With no memory of who you are,where you've been or where you are now. you start to get up... BANG something falls to the floor on your right and a creature scuttles away. What do you do?")
    health.set('Health 100')
    thirst.set('Thirst 10')
    energy.set('Energy 50')
    hunger.set('Hunger 25')
    Inventory.set('Inventory:')
    Op_A.set('Option A:run away')
    Op_B.set('Option B:Investigate')
    Op_C.set('Option C: none')
    Op_D.set('Option D: none')
    Op_E.set('Option E: none')
    Op_F.set('Option F: none')

    
    OP_A = Button(window, textvariable =  Op_A ,bg = "black",command = opa, fg = 'white', font = 'times 11').place(x = 10,y = 122)
    OP_B = Button(window, textvariable =  Op_B ,bg = "black",command = opb, fg = 'white', font = 'times 11').place(x = 10,y = 157)
    OP_C = Button(window, textvariable =  Op_C ,bg = "black",command = opc, fg = 'white', font = 'times 11').place(x = 10,y = 192)
    OP_D = Button(window, textvariable =  Op_D ,bg = "black",command = opd, fg = 'white', font = 'times 11').place(x = 10,y = 227)
    OP_E = Button(window, textvariable =  Op_E ,bg = "black",command = ope, fg = 'white', font = 'times 11').place(x = 10,y = 262)
    OP_F = Button(window, textvariable =  Op_F ,bg = "black",command = opf, fg = 'white', font = 'times 11').place(x = 10,y = 297)


    health = Label(window, textvariable =  health, bg = "black", fg = "white",font = "times 10").place(x = 10, y = 10)
    energy = Label(window, textvariable =  energy, bg = "black", fg = "white",font = "times 10").place(x = 10, y = 31)
    hunger = Label(window, textvariable =  hunger, bg = "black", fg = "white",font = "times 10").place(x = 10, y = 52)
    thrist = Label(window, textvariable =  thirst, bg = "black", fg = "white",font = "times 10").place(x = 10, y = 73)
    inventory = Label(window, textvariable = Inventory, bg = "black", fg = "white",font = "times 12").place(x = 10, y = 375)
    pickaxe = Label(window, textvariable = PICKAXE , bg = "black", fg = "white",font = "times 10").place(x = 10, y = 399)
    axe = Label(window, textvariable =  AXE , bg = "black", fg = "white",font = "times 10").place(x = 10, y = 421)
    sword = Label(window, textvariable = SWORD, bg = "black", fg = "white",font = "times 10").place(x = 10, y = 443)
    scenario = Label(window, textvariable = TEXT,borderwidth = 1,wraplength = 250, relief = "solid", bg="black", fg="white",font = "times 10").place(x = 1000, y = 10)
    

    list = window.grid_slaves()
    for l in list:
        l.destroy()





            
############################################################################################################################################################

title = Label(window, text='THE ISLAND', font = " times 20", bg = "black", fg = "white").grid(padx = 510,pady = 15)
start = Button(window, text='Start',command=destroy, bg = "black",font = " times 20", fg = "white", ).grid(padx = 500,pady = 1)
intructions = Label(window, text= "The Island is a survival game that requires you to survive for 40 days on a small island, foraging and hunting for food, finding water, and fighting the mighty beasts that roam the island, good luck and have fun.", font = " times", bg = "black",wraplength = 300, fg = "white").grid(padx = 510,pady = 15)


    





















window.mainloop()
