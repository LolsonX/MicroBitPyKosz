from microbit import *
import music
pin0.write_analog(0)
while True:
 
    while round(pin0.read_analog()*(3.3/1023),2) == 1.7:
        display.show(Image.HAPPY)
        sleep(1)
    display.show(" ")
    