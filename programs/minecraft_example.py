#A. Rosario Rodriguez
#Minecraft Code Example

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.postToChat("Hello")
playerPos = mc.player.getTilePos()
mc.postToChat(playerPos)