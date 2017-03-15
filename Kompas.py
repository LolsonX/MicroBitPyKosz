from microbit import *

while not compass.is_calibrated():
    compass.clear_calibration()
    compass.calibrate()
 
while True:
    sleep(100)
    needle = ((15-compass.heading()) //30) %12
    display.show(Image.ALL_CLOCKS[needle])