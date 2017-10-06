"""
Light

Acts as a single traffic light on a road, represents a lane
Turn - seperate turn signal
"""
from dependencies import *

class Light(threading.Thread):
    def __init__(self,id, turn):
        threading.Thread.__init__(self)
        self.id = id
        self.turn = turn
        self.stoprequest = threading.Event()

        self.state = 0
        if(turn):
            self.turn_state = 0
    """
    States for a traffic light

    -1 - Red
    0 - Yellow
    1 - Green
    """
    def set_state(state):
        self.state = state

    def set_turn(state):
        self.turn_state = state;

    def run(self):
        self.stoprequest.clear()
        while not self.stoprequest.isSet():
            time.sleep(1)
    def join(self, timeout=None):
        self.stoprequest.set()
        super(Intersection, self).join(timeout)
