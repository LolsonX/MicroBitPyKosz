from microbit import *
import music
while True:
    display.scroll(str(int(pin0.read_analog())*(3.3/1023)))
    