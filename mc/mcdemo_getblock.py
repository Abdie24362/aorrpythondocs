# A. Rosario
# Get Block

import time
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    time.sleep(1)
    if GPIO.input(6) == GPIO.LOW :
        pos = mc.player.getTilePos()
        print("Button 6 was pressed")
        blockBeneath = mc.getBlock(pos.x, pos.y - 1, pos.z)
        print(blockBeneath)
        if blockBeneath == 57:
            mc.player.setPos(pos.x, pos.y + 20, pos.z)
    
    
        
