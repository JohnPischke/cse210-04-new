
# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley



from game.common.location import Location

class Player:
    
    def __init__(self, x, y):
        self._location = Location(x, y)
        self._symbol = "#"
        self._text_size = 50
        self._color = (0,255,255)
        

    def get_x(self):
        return self._location.get_x()

    def get_y(self):
        return self._location.get_y()

    def get_symbol(self):
        return self._symbol

    def get_text_size(self):
        return self._text_size

    def get_color(self):
        return self._color

    def move_x(self, value):
        self._location.move(value.get_x(),0)

    
