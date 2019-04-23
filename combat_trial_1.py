from tkinter import *
from random import *
import time


############################
############################
from tkinter import Label

window = Tk()
window.title("combat trial 1")
window.configure(bg="black")
width = window.winfo_screenwidth() 
height = window.winfo_screenheight()
window.geometry('%sx%s' % (width//2, height//2))


############################
############################


UI_DELTA = 0.000001  # nanosecond scale iterative filter step size
UI_DEPTH = 10
ui_refreshes = []
last_refresh = time.time()
ui_delta = 0


PlayerHealth = 100
sword = StringVar()
swordATK = 5

EnemyHealth = " "
EnemyName = " "

InitializeAttack = 1
doesItAttack = randint(1, 5)

attackdelay = 1


############################
############################


class Enemy:

    def __init__(self, name, attack, health, tick_speed, agility, biome):

        self.attack = attack
        self.health = health
        self.biome = biome
        self.tick_speed = tick_speed
        self.name = name
        self.agility = agility

###############

    def set_enemy_stats(self):

        global EnemyHealth, EnemyName
        EnemyName = str(self.name)
        EnemyHealth = self.health
        enemy_health['text'] = "Health: " + str(EnemyHealth)
        enemy_name['text'] = str(EnemyName)

###############

    def damager(self):
        global PlayerHealth, doesItAttack, attackdelay, InitializeAttack

        if attackdelay != 0:
            attackdelay -= 1

        elif 2 < doesItAttack and PlayerHealth > 0 and attackdelay == 0:
            PlayerHealth = PlayerHealth - self.attack
            player_health['text'] = "Health: " + str(PlayerHealth)
            doesItAttack = randint(1, 5)
            
            if PlayerHealth <= 0:
                PlayerHealth = 0
                player_health['text'] = "Health: " + str(PlayerHealth)
                InitializeAttack = 1

            else:
                pass

        else:
            doesItAttack = randint(1, 5)

###############

    def tick(self):
        global last_refresh, ui_refreshes, last_refresh, ui_delta
        tick_speed_sec = self.tick_speed/1000

        # keep moving average of UI_REFRESH timing
        now = time.time()
        ui_refreshes.append(now - last_refresh)
        ui_refreshes = ui_refreshes[-UI_DEPTH:]
        ui_refresh = sum(ui_refreshes) / len(ui_refreshes)
        last_refresh = now

        # filter nanosecond scale timing oddities iteratively
        # both as they arise due to load and between various systems
        if float('%.5f' % ui_refresh) < tick_speed_sec:
            ui_delta += UI_DELTA
        if float('%.5f' % ui_refresh) > tick_speed_sec:
            ui_delta -= UI_DELTA

        self.damager()

        # set perfect UI_REFRESH timing
        pause = int(1000 *
                    min(tick_speed_sec, (
                        max(0, (
                            2 * tick_speed_sec - ui_refresh + ui_delta)))))

        window.after(pause, self.tick)
        

###############################################################
###############################################################

        
ent = Enemy("Ent", 19, 60, 4000, 15, 1)
creature = ent
doIAttack = randint(1, creature.agility)
###############################################################
###############################################################


class Weapons:

    def __init__(self, name, atkspeed, damage):

        self.name = name
        self.atkspeed = atkspeed
        self.damage = damage

#########################

    def weapontick(self):
        global last_refresh, ui_refreshes, last_refresh, ui_delta

        # keep moving average of UI_REFRESH timing
        now = time.time()
        ui_refreshes.append(now - last_refresh)
        ui_refreshes = ui_refreshes[-UI_DEPTH:]
        ui_refresh = sum(ui_refreshes) / len(ui_refreshes)
        last_refresh = now

        # filter nanosecond scale timing oddities iteratively
        # both as they arise due to load and between various systems

        if float('%.5f' % ui_refresh) < tick_speed_sec:
            ui_delta += UI_DELTA
        if float('%.5f' % ui_refresh) > tick_speed_sec:
            ui_delta -= UI_DELTA

        self.atk()

        # set perfect UI_REFRESH timing
        pause = int(1000 *
                    min(tick_speed_sec, (
                        max(0, (
                            2 * tick_speed_sec - ui_refresh + ui_delta)))))

        window.after(pause)
        
#########################
        
    def atk(self):
        global EnemyHealth, doesIAttack, InitializeAttack

        atk_recharge = self.atkspeed

        if atk_recharge != 0:
            atk_recharge = - 1
            print(atk_recharge)

        elif 2 < doesIAttack and EnemyHealth > 0 and atk_recharge == 0:
            EnemyHealth = EnemyHealth - self.damage
            enemy_health['text'] = "Health: " + str(EnemyHealth)
            doesIAttack = randint(1, 5)
            
            if EnemyHealth <= 0:
                EnemyHealth = 0
                enemy_health['text'] = "Health: " + str(EnemyHealth)
                InitializeAttack = 1

            else:
                pass

        else:
            doesIAttack = randint(1, 5)


###############################################################
###############################################################
copperShortSword = Weapons('Copper Short-Sword', 2, 5)

player_health = Label(window, text="Health: " + str(PlayerHealth), fg="white", bg="black")
player_health.place(relx=0.05, rely=0.1)

enemy_name = Label(window, text=str(EnemyName), fg="white", bg="black")
enemy_name.place(relx=0.85, rely=0.05)

enemy_health = Label(window, text="Health: " + str(EnemyHealth), fg="white", bg="black")
enemy_health.place(relx=0.85, rely=0.1)

creature.tick()
creature.set_enemy_stats()

mainloop()
