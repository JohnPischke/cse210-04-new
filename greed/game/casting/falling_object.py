
# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley



import random
from game.common.location import Location
from game.common.points import Points


class Falling_Object:
    
    def __init__(self):
        # sets up the location, the points the player has, velocity(speed that things move), the symbol(symbol that
        # will be displayed on the screen), text size, and the color of the symbol that will be displayed on the screen. 
        self.location = Location(random.randint(0,900), 0)
        self.points = 0
        self.velocity = 10
        self.symbol = 1
        self.text_size = 50
        self.color = (0,0,0)

    def fall_down(self):
        # causes the y value of the location of the object it is used on to decrease. 
        self.location.move(0,self.velocity) 
        pass

    def get_x(self):
        # returns the x value of the location of the object it is used on. 
        return self.location.get_x()
    
    def get_y(self):
        # returns the y value of the location of the object it is used on. 
        return self.location.get_y()

    def get_symbol(self):
        # returns the symbol/text of an object that is to be  displayed on the screen 
        return self.symbol
    
    def get_text_size(self):
        # returns the text size of the symbol/text of an object that is to be  displayed on the screen 
        return self.text_size
    
    def get_points(self):
        # ***
        # returns the points of an object
        # /***
        return self.points

    def get_color(self):
        # returns the color of the symbol/text of an object that is to be  displayed on the screen 
        return self.color

    

