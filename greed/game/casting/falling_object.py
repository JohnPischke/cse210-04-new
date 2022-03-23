import random
from game.common.location import Location
from game.common.points import Points

class Falling_Object:
    
    def __init__(self):
        self.location = Location(random.randint(0,900), 600)
        self.points = Points()
        self.velocity = 1
        self.symbol = 1

    def fall(self):
        pass

    def delete(self):
        pass
