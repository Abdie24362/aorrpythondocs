# A. Rosario
# MC Multilists

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#Make a line of wool colors
woolLine = [13, 12, 8, 7, 1]
#Make a Grid of wool colors
'''
# Exclamation mark
woolGrid = [[15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],
            [15, 0, 0, 15, 15, 14, 15, 15, 0, 0, 15],
            [15, 0, 15, 15, 15, 15, 15, 15, 15, 0, 15],
            [15, 0, 15, 15, 15, 14, 15, 15, 15, 0, 15],
            [15, 0, 15, 15, 15, 14, 15, 15, 15, 0, 15],
            [15, 0, 15, 15, 15, 14, 15, 15, 15, 0, 15],
            [15, 0, 0, 15, 15, 14, 15, 15, 0, 0, 15],
            [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]]
'''
'''
#Question Mark
woolGrid = [[15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],
            [15, 0, 0, 15, 15, 14, 15, 15, 0, 0, 15],
            [15, 0, 15, 15, 15, 15, 15, 15, 15, 0, 15],
            [15, 0, 15, 15, 15, 14, 15, 15, 15, 0, 15],
            [15, 0, 15, 15, 15, 15, 14, 15, 15, 0, 15],
            [15, 0, 15, 15, 14, 15, 14, 15, 15, 0, 15],
            [15, 0, 0, 15, 14, 14, 14, 15, 0, 0, 15],
            [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]]
'''
woolGrid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 15, 15, 15, 15, 15, 15, 15, 15, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0],
            [0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0],
            [0, 0, 0, 15, 0, 0, 0, 15, 0, 0, 15, 0, 0, 0, 15, 0, 0, 0],
            [0, 0, 15, 15, 15, 0, 0, 15, 0, 0, 15, 0, 0, 15, 15, 15, 0, 0],
            [0, 15, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 14, 14, 14, 15, 0]]
#Get my position
pos = mc.player.getTilePos()
'''
#This loop will place a line of wool
for i, wool in enumerate(woolLine):
    print(str(i) + ' is the color ' + str(wool))
    mc.setBlock(pos.x + i, pos.y , pos.z, 35, wool)
'''
#This will print a grid of wool blocks
for i, row in enumerate(woolGrid):
    print(row)
    for j, col in enumerate(row):
        print(col)
        mc.setBlock(pos.x + j, pos.y + i, pos.z, 35, col)