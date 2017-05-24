from microbit import *
display.off()
while True:
    if button_a.is_pressed():
        pin0.write_digital(1)
        pin0.set_analog_period(400000)
    elif button_b.is_pressed():
        pin0.write_analog(0)
    