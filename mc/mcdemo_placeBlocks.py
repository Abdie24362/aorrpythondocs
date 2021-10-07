#A. Rosario
#Build a house with a button
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def build():
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x+1, pos.y, pos.z+1, pos.x+7, pos.y+5, pos.z+6, 45)
    mc.setBlocks(pos.x+2, pos.y+1, pos.z+2, pos.x+6, pos.y+4, pos.z+5, 0)
    mc.setBlock(pos.x+4, pos.y+1, pos.z+1, 64)
    mc.setBlock(pos.x+4, pos.y+2, pos.z+1, 64)
    mc.setBlock(pos.x+2, pos.y+2, pos.z+1, 102)
    mc.setBlock(pos.x+6, pos.y+2, pos.z+1, 102)
    mc.setBlock(pos.x+2, pos.y+3, pos.z+1, 102)
    mc.setBlock(pos.x+6, pos.y+3, pos.z+1, 102)
while True:
    if GPIO.input(6) == GPIO.LOW :
        build()
        
