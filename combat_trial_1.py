from tkinter import *
from random import *
import time

############################
############################

window = Tk()
window.title("combat trial 1")
window.configure(bg = "black")
width = window.winfo_screenwidth() 
height = window.winfo_screenheight()
window.geometry('%sx%s' % (width//2, height//2))

############################
############################
UI_DELTA = 0.000001 # nanosecond scale iterative filter step size
UI_DEPTH = 10 # depth of ui_refreshes moving average
ui_refreshes = []
last_refresh = time.time()
ui_delta = 0

PlayerHealth = 100
sword = StringVar()
swordATK = 5

doesItAttack = randint(1,5)
doIAttack = randint(1,5)


############################
############################


class enemy:

    
    def __init__(self,name, attack, health, defence,tick_speed, biome):

        self.attack = attack
        self.health = health
        self.defence = defence
        self.biome = biome
        self.tick_speed = tick_speed
         
###############


    def animate(self):
        global last_refresh, ui_refreshes, last_refresh, ui_delta
        tick_speed_SEC = self.tick_speed/1000

          
        # keep moving average of UI_REFRESH timing
        now = time.time()
        ui_refreshes.append(now - last_refresh)
        ui_refreshes = ui_refreshes[-UI_DEPTH:]
        ui_refresh = sum(ui_refreshes) / len(ui_refreshes)
        last_refresh = now

        # filter nanosecond scale timing oddities iteratively
        # both as they arise due to load and between various systems
        refresh_error = abs(tick_speed_SEC-ui_refresh)
        if float('%.5f' % ui_refresh) < (tick_speed_SEC):
            ui_delta += UI_DELTA
        if float('%.5f' % ui_refresh) > (tick_speed_SEC):
            ui_delta -= UI_DELTA

        # do whatever your loop does
        # note this must take less time than your refresh rate!!
        ##    print(  int(time.time()),
        ##            ('%.6f' % ui_refresh),
        ##            ('%.6f' % refresh_error),
        ##            ('%.4f' % round(ui_refresh, 4)),
        ##            int(1000*round(ui_refresh, 4)))
        hw()

        # set perfect UI_REFRESH timing
        pause = int(1000 *
                    min(tick_speed_SEC, (
                        max(0, (
                            2 * tick_speed_SEC - ui_refresh + ui_delta)))))

        window.after(pause, self.animate)

        

    def damager(self):
        global PlayerHealth,doesItAttack
        if 2 < doesItAttack:
            PlayerHealth = PlayerHealth - self.attack
            doesItAttack = randint(1,5)
            player_health['text'] = str(PlayerHealth)
            print(doesItAttack)
            print(str(PlayerHealth))


        else:
            print(doesItAttack)
            doesItAttack = randint(1,5)

        
            

###############
   

def hw():
    number = randint(0,5)
    comparer =randint(0,5)
    print (comparer,number)
    if comparer == number:
        print('they are equal')
        number = randint(0,5)
        comparer =randint(0,5)

    else:
        print("they are'nt")
        number = randint(0,5)
        comparer =randint(0,5)
    





###############################################################
###############################################################
class weapons:

    def __init__(self,Name,AtkSpeed,Damage):

        self.Name = Name
        self.AtkSpeed = AtkSpeed
        self.Damage = Damage

    def tick(self):
        threading.Timer(AtkSpeed,Atk).start()
        Atk

    def Atk(self):
        pass
        
    


            
    
                
player_health = Label(window,text = str(PlayerHealth),fg = "white",bg = "black")
player_health.place(relx = 0.05, rely = 0.1)



ent = enemy("Ent",20,60,5,300,1)

creature = ent

creature.animate()









window.after(0, animate)            
mainloop()














