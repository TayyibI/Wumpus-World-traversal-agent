import wumpus
import random

GRID_SIZE = 5
width = 6
pit_count=1
wumpus_count=1
blocks = set()
wumpus_location = {(1,2)}

gold = {(2,4)}
pits = {(2,3)}
wumpus_location = {(2,2)}
initial_location = (1,1)

for x in range(width+1):  #border
    blocks.add((0, x))
    blocks.add((x, 0))
    blocks.add((width,x))
    blocks.add((x, width))


while pit_count != 0:
    x = random.randint(1, GRID_SIZE)
    y = random.randint(1, GRID_SIZE)
    if (x, y) != (1, 1):
        pit_count = pit_count -1
        pits = {(x,y)}


while wumpus_count != 0:
    x = random.randint(1, GRID_SIZE)
    y = random.randint(1, GRID_SIZE)
    if (x, y) not in pits and (x, y) != (1, 1):
        wumpus_count = wumpus_count -1
        wumpus_location = {(x,y)}


    x = random.randint(1, GRID_SIZE)
    y = random.randint(1, GRID_SIZE)
    if (x, y) not in pits and (x, y) not in wumpus_location and (x, y) != (1, 1):
        gold = {(x,y)}

initial_location = (1, 1)
'''
gold = {(2,4)}
pits = {(3,2)}

wumpus_location = {(3,1)}
initial_location = (1,1)
'''
world1 = wumpus.WumpusWorld(blocks = blocks, gold = gold, wumpus = wumpus_location, pits = pits, initial_location = initial_location)





