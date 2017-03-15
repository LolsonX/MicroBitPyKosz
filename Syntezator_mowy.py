#Dalek voice

from microbit import *
import speech
import random

dalekWords = ["Hej,", "WHERE, IS, DOCTOR,", "ALARM", "BOMB,", "BOOOM", "HI!, MY, NAME, IS, DALEK,"]
numberOfDalekWords = len(dalekWords)

display.show(Image.HAPPY)

while True:
    speech.say(dalekWords[random.randrange(numberOfDalekWords)],
    pitch=128, speed=128, mouth=128, throat=128)
    sleep(2000)