"""
Road Object

Contains multiple traffic lights, handles enter and leave around intersections

"""
from dependencies import *

class Road(threading.Thread):
    def __init__(self,id, lights):
        threading.Thread.__init__(self)
        self.id = id
        self.lights = lights
        self.light_q = []
        self.stoprequest = threading.Event()

        self.cars = 0
    def add_cars():
    	pass
    def run(self):
        # print('\t\t{} {}'.format(self.id, 'initiated'))
        # print("\t\tInititalizing lights...")
        self.stoprequest.clear()
        for l in range(len(self.lights)):
            self.light_q.append(queue.Queue())
            self.lights[l].road_q = self.light_q[l];
            self.lights[l].start()
        while not self.stoprequest.isSet():
            try:
                for l in range(len(self.lights)):
                    print(self.light_q[l].get())
            except queue.Empty:
                print("Empty")
    def verify(self):
        while(1):
            status = True
            for l in range(len(self.lights)):
                if not self.lights[l].isAlive():
                        status=False
            if status:
                return True
    def join(self, timeout=None):
        self.stoprequest.set()
        super(Intersection, self).join(timeout)
