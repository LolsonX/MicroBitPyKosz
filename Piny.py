from microbit import *

while True:
    display.clear()
    display.scroll("Analog value: {}".format(pin0.read_analog()))
    display.clear()
    display.scroll("Digital value: {}".format(pin0.read_digital()))
    display.clear()
    sleep(5000)
