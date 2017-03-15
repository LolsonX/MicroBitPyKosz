from microbit import *

if "__main__" != __name__:
    quit(1)

man0 = Image(
    "00900:"
    "99999:"
    "00900:"
    "09090:"
    "90009")
    
man1 = Image(
    "00900:"
    "09990:"
    "90909:"
    "09090:"
    "09090")
    
man2 = Image(
    "00900:"
    "99999:"
    "00900:"
    "09090:"
    "90009")
    
man3 = Image(
    "90909:"
    "09990:"
    "00900:"
    "09090:"
    "09090")
    
    
man = [man0, man1, man2, man3]
display.show(man, loop = True, delay=100)