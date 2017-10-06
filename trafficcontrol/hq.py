"""
Control Panel

Helps run the simulation with a hypothetical road network

Example:
hq.py <input option>
nothing - randomly generate
0 - input prompt
1 - command line args
"""

#Imports
import random
import threading
import uuid
from objects import *
from queue import Queue
regions = []

#Generate
def randomly_generate():
    for r in range(1):
        intersections = []
        for i in range(random.randrange(5,10)):
            roads = []
            for ro in range(random.randrange(3,4)):
                lights = []
                for l in range(random.randrange(2,4)):
                    lights.append(light.Light(uuid.uuid4(), 0))
                roads.append(road.Road(uuid.uuid4(), lights ))
            intersections.append(intersection.Intersection(uuid.uuid4(), roads))
        regions.append(region.Region(uuid.uuid4(), intersections))

randomly_generate()
regions[0].start()
