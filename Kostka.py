# Add your Python code here. E.g.
from microbit import *
import random

wybor = 2

possible = []
while True:
    licznik = 0
    wybor += button_a.get_presses()
    wybor -= button_b.get_presses()
    if wybor < 2:
        wybor = 2
    elif wybor > 200:
        wybor = 200
    display.scroll(str(wybor))
    
    if pin0.is_touched():
        for i in range(1, wybor+1):
            possible.append(str(i))
        while True:
            if accelerometer.was_gesture("shake"):
                display.scroll(random.choice(possible))
                sleep(3000)
                display.clear()
            if button_a.is_pressed():
                wybor -=1
                break
                
        
