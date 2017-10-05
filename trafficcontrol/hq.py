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
import sys
import random
import os
import threading
import time
from objects import *
regions = None

#Generate
def randomly_generate():
    ran = [random.randrange(1, 3), random.randrange(20,40)]
    regions = [region.Region( [ intersection.Intersection( [ road.Road( [ light.Light( bool(random.getrandbits(1)) ) for l in range(random.randrange(2,4)) ] ) for ro in range(random.randrange(3,4)) ] ) for i in range(ran[1]) ] ) for r in range(ran[0]) ]
def input_prompt():
    ran = [ input("number of regions "), input("number of intersections "), input("number of roads "), input("number of lights ") ]
    regions = [region.Region( [ intersection.Intersection( [ road.Road( [ light.Light( bool(random.getrandbits(1)) ) for l in ran[3] ] ) for ro in ran[2] ] ) for i in range(ran[1]) ] ) for r in range(ran[0]) ]
def command_args(args):
    ran = [ sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]]

if len(sys.argv)>1:
    if sys.argv[1] == "0":
        input_prompt()
    elif sys.argv[1] == "1":
        command_args(sys.argv[2:])
else:
    pass
    # randomly_generate()

class countThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("Starting " + self.name)
        while(1):
            print("hello" + str(self.counter))
            time.sleep(1)

# def count( threadName):
#       count = 0
#       count++1;
#       sleep(1)
#       print(threadName + " " + str(count))
# thread -> intersection
thread1 = countThread(1, "Thread-1", 1)
thread2 = countThread(2, "Thread-2", 2)
thread3 = countThread(3, "Thread-3", 3)
thread4 = countThread(4, "Thread-4", 4)
thread5 = countThread(5, "Thread-5", 5)
thread6 = countThread(6, "Thread-6", 6)
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()

# thread1.join()
# thread2.join()
#Run Model
