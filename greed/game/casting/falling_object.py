
# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley



import random
from game.common.location import Location

 

# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley


class Falling_Object:
    
    def __init__(self):
        self.location = Location(random.randint(0,900), 0)
        self.points = 0
        self.velocity = 10
        self.symbol = 1
        self.text_size = 50
        self.color = (0,0,0)

    def fall_down(self):
        self.location.move(0,self.velocity) 
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

    def get_color(self):
        return self.color

    

    #font size