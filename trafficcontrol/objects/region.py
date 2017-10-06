"""
Regions

Contains multiple intersections, controls traffic waves
"""
from dependencies import *

class Region(threading.Thread):
    def __init__(self,id,intersections):
        threading.Thread.__init__(self)
        self.id = id
        self.intersections = intersections
        self.int_q = []
        self.stoprequest = threading.Event()

    #Threading
    def run(self):
        self.stoprequest.clear()
        print('{} {}'.format(self.id, 'initiated'))
        for i in tqdm(range(len(self.intersections))):
            self.int_q.append(queue.Queue())
            self.intersections[i].region_q = self.int_q[i];
            self.intersections[i].start()
        self.verify()
        while not self.stoprequest.isSet():
            try:
                for i in range(len(self.intersections)):
                    print(self.int_q[i].get())
            except queue.Empty:
                print("Empty")
    def verify(self):
        while(1):
            status = True
            for i in range(len(self.intersections)):
                if not self.intersections[i].isAlive() or not self.intersections[i].verify():
                        status=False
            if status:
                print("Connections verified.")
                return True
    def join(self, timeout=None):
        self.stoprequest.set()
        super(Region, self).join(timeout)
