from mcpi.minecraft import Minecraft
from sense_hat import SenseHat
import mcpi.block as block

sense = SenseHat()
mc = Minecraft.create()

block_colors = {
    0: (0, 0, 0),
    1: (100, 100, 100),
    2: (0, 255, 0),
    3: (51,43,0),
    8: (0, 0, 255),
    9: (0, 0, 255),
    10: (255, 85, 0),
    11: (255, 85, 0),
    12: (255, 235, 205),
    13: (80, 80, 80),
    14: (153, 102, 0),
    15: (200, 200, 200),
    16: (50, 50, 50),
    17: (51, 17, 0),
    18: (0, 155, 0),
    20: (150, 150, 255),
    24: (255, 235, 205),
    37: (255, 255, 35),
    56: (100, 100, 255),
    57: (100, 100, 255),
    73: (255, 0, 0),
}


while True:
    diamond_found = False
    x, y, z = mc.player.getPos()
    for row in range(-4, 4):
        for col in range(-4, 4):
            block = mc.getBlock(x+col, y-1, z+row)
            if block in block_colors:
                block_color = block_colors[block]
                sense.set_pixel(col+4, row+4, block_color)
            else:
                sense.set_pixel(col+4, row+4, (0, 0, 0))
    for event in sense.stick.get_events():
        if event.direction == "middle" and event.action == "pressed":
            mc.postToChat("Searching for diamonds...")
            for row in range(-1, 2):
                for col in range(-1, 2):
                    for block in range(30):
                        if mc.getBlock(x+col, -65+block, z+row) == 56:
                            diamond_found = True
                            sense.set_pixel(col+4, row+4, (220, 220, 255))
                            mc.postToChat("Diamond found! Go to x:{} y:{} z:{}".format(x+col, -65+block, z+row))
                            break
            if not diamond_found:
                mc.postToChat("No diamonds found. Keep searching.")

