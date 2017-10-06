"""
Intersections

Contains multiple roads, stored as (N, S, E, W)
"""
from dependencies import *

class Intersection(threading.Thread):
    def __init__(self,id,roads):
        threading.Thread.__init__(self)
        self.id = id
        self.roads = roads
        self.stoprequest = threading.Event()
        self.road_q = []

    #Threading
    def run(self):
        self.stoprequest.clear()
        for r in range(len(self.roads)):
            self.road_q.append(queue.Queue())
            self.roads[r].int_q = self.road_q[r];
            self.roads[r].start()
        while not self.stoprequest.isSet():
            try:
                for r in range(len(self.roads)):
                    print(self.road_q[r].get())
            except queue.Empty:
                print("Empty")
    def verify(self):
        while(1):
            status = True
            for r in range(len(self.roads)):
                if not self.roads[r].isAlive() or not self.roads[r].verify():
                        status=False
            if status:
                return True
    def join(self, timeout=None):
        self.stoprequest.set()
        super(Intersection, self).join(timeout)

    def enter_intersection():
        pass
