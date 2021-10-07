# A. Rosario
# Places a randomly colored wool block
'''
Set up program for MC and two buttons
Create a 'counter' variable that starts at 0
Create a list of blockdata numbers for different numbers for differetn color wool
Define a function called placeNext
    -it takes one argument called direction
    -it changes the counter by adding the direction argument
    -place a wool block of the color from the list where the indec matches the counter variable.
    -if the counter is out of bounds of the index, reset it
In a forever loop:
    -if the first button was pressed, placeNext(1)
    -if the second button was pressed, placeNext(-1)
'''
import time
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

counter = 0
woolColors = [6, 5, 10, 14, 15, 0]
def placeNext(direction):
    global counter
    pos = mc.player.getTilePos()
    counter += direction
    mc.setBlock(pos.x, pos.y, pos.z-1, 35, woolColors[counter])
    if counter > 5:
        counter = 0
    if counter < 0:
        counter = 5
while True:
    time.sleep(1)
    if GPIO.input(6) == GPIO.LOW :
        placeNext(1)
    if GPIO.input(13) == GPIO.LOW :
        placeNext(-1)
