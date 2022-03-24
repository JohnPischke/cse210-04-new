import random
from game.common.location import Location
from game.common.points import Points

class Falling_Object:
    
    def __init__(self):
        self.location = Location(random.randint(0,900), 600)
        self.points = 0
        self.velocity = -1
        self.symbol = 1
        self.text_size = 1

    def fall(self):
        self.location = Location.move(0, self.velocity)
        pass

    def get_x(self):
        return self.location.get_x()
    
    def get_y(self):
        return self.location.get_y()

    def get_symbol(self):
        return self.symbol
    
    def get_text_size(self):
        return self.text_size
    
    def get_points(self):
        return self.points

    

    #font size