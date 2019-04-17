import time
import tkinter as tk
from random import*

tick_speed = 100 # your preferred refresh rate in milleseconds
UI_DELTA = 0.000001 # nanosecond scale iterative filter step size
UI_DEPTH = 10 # depth of ui_refreshes moving average

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
    

def animate():

    global last_refresh, ui_refreshes, last_refresh, ui_delta

      
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
    master.after(pause, animate)


tick_speed_SEC = tick_speed/1000
ui_refreshes = []
last_refresh = time.time()
ui_delta = 0
master = tk.Tk()
master.after(0, animate)
master.mainloop()
