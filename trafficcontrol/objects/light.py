"""
Light

Acts as a single traffic light on a road, represents a lane
"""

class Light:
    def __init__(self, turn):
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