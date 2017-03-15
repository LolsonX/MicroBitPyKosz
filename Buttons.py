from microbit import *

while True:
    display.clear()
    sleep(100)
    if (button_a.is_pressed() and not button_b.is_pressed()):
        display.scroll("Button A is pressed")
    elif (not button_a.is_pressed() and button_b.is_pressed()):
        display.scroll("Button B is pressed")
    elif button_a.is_pressed() and button_b.is_pressed():
        display.scroll("Both are pressed")
    else:
        display.scroll("Press any button")
