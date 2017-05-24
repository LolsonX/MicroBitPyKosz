from microbit import *
import radio

radio.on()
  
scissorsI = Image("90009:"
                 "09090:"
                 "00900:"
                 "09090:"
                 "99099")
                 
rockI = Image("00000:"
              "09990:"
              "09990:"
              "09990:"
              "00000")
                 
paperI = Image("99999:"
               "90009:"
               "90009:"
               "90009:"
               "99999")
possible_messages = ['paper', 'scissors', 'rock']
possible_images = [paperI, scissorsI, rockI]
choose = 0
while True:
   if (button_a.was_pressed()):
        choose+=1;
   elif (button_b.was_pressed()):
        choose-=1;
        
   if choose >2 :
        choose = 0
   if choose < 0:
        choose = 2
   display.show(possible_images[choose])
   