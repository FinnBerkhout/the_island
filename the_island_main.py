from tkinter import *
#######################################
window = Tk()
window.title("The Island")
window.configure(bg="black")
width = window.winfo_screenwidth() 
height = window.winfo_screenheight()
window.geometry('%sx%s' % (width, height))
########################################
Hunger = int(25)
Thirst = int(30)
Health = int(100)
Energy = int(30)
Inventory = StringVar()
TEXT = StringVar()
AXE = StringVar()
AxeHarvest = 0

PICKAXE = StringVar()
PickStoneHarvest = 0
PickOreHarvest = 0

SWORD = StringVar()
SwordAtk = 0
Op_A = "Option A: "
Op_B = "Option B: "
Op_C = "Option C: "
Op_D = "Option D: "
Op_E = "Option E: "
Op_F = "Option F: "
ButtonAText = StringVar()
ButtonBText = StringVar()
ButtonCText = StringVar()
ButtonDText = StringVar()
ButtonEText = StringVar()
ButtonFText = StringVar()

place_counter = 1
#######################################


def opa():
    global TEXT, place_counter, AXE, PICKAXE, SWORD
    if place_counter == 1:
        TEXT.set("As you run away from the sound you look behind to catch a glimpse of what happened while you're doing it you run into a wall,but its not a wall its a door. The door opens and light seeps through illuminating the room you're in. you look behind you just in time to see a small mouse go through a crack in the wall you see what the mouse knocked over… its a book.")
        place_counter = 2
        ButtonAText.set(Op_A + "leave")
        ButtonBText.set(Op_B + "Stay and read the book.")
    elif place_counter == 2:
        TEXT.set("You Stand up and make your way through the door, As your eyes adjust to the light you see lush forests and some beautiful grasslands. But as you look further you notice sand and water. You’re on an island and you’re alone, with nobody. You slowly come to realize that nobody will come and save you so this will be your home for the next… you realise that you probably won’t be leaving here alive...  ")
        place_counter = 4
        ButtonAText.set(Op_A + "Go back inside")
        ButtonBText.set(Op_B + "Explore")

    elif place_counter == 3:
        place_counter = 5
        TEXT.set("You pick up the book and open it. It’s blank. You go to put it down again but then all of a sudden, a note falls out, it says: Where am I, who am I, what is this place, who put me here. Is there anyone else?  Why do I exist?The bottom of the note is marked with a cross.You sit the book down neatly back where it came from. Something beside it glints in the light it a flint axe.Next you?")
        AXE.set('Flint Axe')
        ButtonAText.set(Op_A + 'outside')
        ButtonBText.set(Op_B + 'look more closly at this area')
        ButtonCText.set(Op_C + 'search a different part of the house')

    elif place_counter == 4:
        pass

    elif place_counter == 5:
        pass

    elif place_counter == 6:
        pass

    elif place_counter == 7:
        pass

    else:
        pass

    if free_mode == 1:
        pass


##                 
def opb():
    global TEXT, place_counter, AXE, PICKAXE, SWORD
    if place_counter == 1:
        TEXT.set("While you stumble towards the object you trip over a pile of wood falling flat of your face… there’s a gust of wind and and a door creaks open. You stand up wondering what made that noise. As light floods the room exposing the contents, you see what made the noise, a book.")
        place_counter = 3
        ButtonAText.set(Op_A + "Read the book")
        ButtonBText.set(Op_B + "forget about the book for now")      
    elif place_counter == 2:
        TEXT.set("You Decide to read the book that has fallen over before venturing outside. As you open the book a note falls out. It Reads:Where am I, who am I, what is this place, who put me here. Is there anyone else?  Why do I exist?The bottom of the note is marked with a cross... You notice a small shimmer of light in the corner where the book came from it’s a small flint axe it’s slightly blunt, but it will do for now.Now you decide to?")
        place_counter = 5
        ButtonAText.set('Option A:go outside')
        ButtonBText.set('Option B:look more closly at this area')
        ButtonCText.set('Option C: search a different part of the house')

    elif place_counter == 3:
        place_counter = 7
        TEXT.set('You Stand up and make your way through the door, as your eyes adjust to the light you see lush forests and some beautiful grasslands. But as you look further you notice sand and water. You’re on an island and you’re alone, with nobody. You slowly come to realize that nobody will come and save you so this will be your home for the next… you realise that you probably won’t be leaving here alive... You step down onto the grass and look behind you. You see the rickety house, it looks like it was thrown together in a hurry and then whoever made it tried to fix it up, it’s very very old and battered. You look down next to you and you see a crude stone pickaxe and a dull short sword that looks like its made of copper.')
        ButtonAText.set('Option A: Explore the island')
        ButtonBText.set('Option B:go back inside to see if you can find anything new')
        ButtonCText.set('Option C: look at the outside of the house')
        PICKAXE.set('Stone pickaxe')
        SWORD.set('copper short-sword')

    elif place_counter == 4:
        pass    

    elif place_counter == 5:
        pass

    elif place_counter == 6:
        pass

    elif place_counter == 7:
        pass
        
##
def opc():
    global TEXT,place_counter,AXE,PICKAXE,SWORD

    if place_counter == 1:
        pass

    elif place_counter == 2:
        pass

    elif place_counter == 3:
        pass

    elif place_counter == 4:
        pass

    elif place_counter == 5:
        pass

    elif place_counter == 6:
        pass

    elif place_counter == 7:
        global free_mode
        pass
        
##    
def opd():
    global TEXT,place_counter,AXE,PICKAXE,SWORD
    if place_counter == 1:
        TEXT.set("You wake up... With no memory of who you are,where you've been or where you are now. you start to get up... BANG something falls to the floor on your right and a creature scuttles away. What do you do?")
        place_counter = 1

    elif place_counter == 2:
        passs


    elif place_counter == 3:
        pass

    elif place_counter == 4:
        pass
        
    elif place_counter == 5:
        pass


    elif place_counter == 6:
        pass


    elif place_counter == 7:
        global free_mode
        pass

##
def ope():
    global TEXT,place_counter,AXE,PICKAXE,SWORD
    if place_counter == 1:
        pass

    elif place_counter == 2:
        pass


    elif place_counter == 3:
        pass

    elif place_counter == 4:
        pass

    elif place_counter == 5:
        pass


    elif place_counter == 6:
        pass


    elif place_counter == 7:
        global free_mode
        pass

##
def opf():
    global TEXT,place_counter,AXE,PICKAXE,SWORD
    
    if place_counter == 1:
        pass

    elif place_counter == 2:
        pass


    elif place_counter == 3:
        pass

    elif place_counter == 4:
        pass

    elif place_counter == 5:
        pass


    elif place_counter == 6:
        pass


    elif place_counter == 7:
        global free_mode
        pass






###########################################################################
def destroy(): 
    global Health, Thrist, Energy, Hunger, TEXT, Inventory, AXE, PICKAXE, SWORD
 
    TEXT.set("You wake up... With no memory of who you are,where you've been or where you are now. you start to get up... BANG something falls to the floor on your right and a creature scuttles away. What do you do?")

    health = Label(window, text = '', bg = "black", fg = "white",font = "times 10")
    energy = Label(window, text = '', bg = "black", fg = "white",font = "times 10")
    hunger = Label(window, text = '', bg = "black", fg = "white",font = "times 10")
    thirst = Label(window, text = '', bg = "black", fg = "white",font = "times 10")

    health.place(x = 10, y = 10)
    energy.place(x = 10, y = 31)
    hunger.place(x = 10, y = 52)
    thirst.place(x = 10, y = 73)

    
    health["text"] = "Health: " + str(Health)
    thirst["text"] = 'Thirst: ' + str(Thirst)
    energy["text"] = 'Energy: ' + str(Energy)
    hunger["text"] = 'Hunger: ' + str(Hunger)
    
    #Op_A.set(('Option A: ', ButtonAText))
    #Op_B.set(('Option B: ', ButtonBText))
    #Op_C.set(('Option C: ', ButtonCText))
    #Op_D.set(('Option D: ', ButtonDText))
    #Op_E.set(('Option E: ', ButtonEText))
    #Op_F.set(('Option F: ', ButtonFText))

    Inventory.set('Inventory:')
    ButtonAText.set(Op_A + "Run away")
    ButtonBText.set(Op_B + "Investigate")

    OP_A = Button(window, textvariable =  ButtonAText ,bg = "black",command = opa, fg = 'white', font = 'times 11')
    OP_B = Button(window, textvariable =  ButtonBText ,bg = "black",command = opb, fg = 'white', font = 'times 11')
    OP_C = Button(window, textvariable =  ButtonCText ,bg = "black",command = opb, fg = 'white', font = 'times 11')
    OP_D = Button(window, textvariable =  ButtonDText ,bg = "black",command = opd, fg = 'white', font = 'times 11')
    OP_E = Button(window, textvariable =  ButtonEText , bg = "black",command = ope, fg = 'white', font = 'times 11')
    OP_F = Button(window, textvariable =  ButtonFText ,bg = "black",command = opf, fg = 'white', font = 'times 11')

    ButtonAText.set(Op_A + "Run away")
    ButtonBText.set(Op_B + "Investigate")
    

    OP_A.place(x = 10,y = 122)
    OP_B.place(x = 10,y = 157)
    OP_C.place(x = 10,y = 192)
    OP_D.place(x = 10,y = 227)
    OP_E.place(x = 10,y = 262)
    OP_F.place(x = 10,y = 297)

    inventory = Label(window, textvariable = Inventory, bg = "black", fg = "white",font = "times 12")
    pickaxe = Label(window, textvariable = PICKAXE , bg = "black", fg = "white",font = "times 10")
    axe = Label(window, textvariable =  AXE , bg = "black", fg = "white",font = "times 10")
    sword = Label(window, textvariable = SWORD, bg = "black", fg = "white",font = "times 10")
    scenario = Label(window, textvariable = TEXT,borderwidth = 1,wraplength = 250, relief = "solid", bg="black", fg="white",font = "times 10")

    inventory.place(x = 10, y = 375)
    pickaxe.place(x = 10, y = 399)
    axe.place(x = 10, y = 421)
    sword.place(x = 10, y = 443)
    scenario.place(x = 1000, y = 10)

    list = window.grid_slaves()
    for l in list:
        l.destroy()

            
############################################################################################################################################################

title = Label(window, text='The Island', font = " times 20", bg = "black", fg = "white")
start = Button(window, text='Start',command=destroy, bg = "black",font = " times 20", fg = "white", )
intructions = Label(window, text= "The Island is a survival game that requires you to survive for 40 days on a small island, foraging and hunting for food, finding water, and fighting the mighty beasts that roam the island, good luck and have fun.", font = " times", bg = "black",wraplength = 300, fg = "white")

title.grid(padx = 510,pady = 15)
start.grid(padx = 500,pady = 1)
intructions.grid(padx=510,pady = 15)

window.mainloop()
