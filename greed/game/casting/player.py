from game.common.location import Location

class Player:
    
    def __init__(self, x, y):
        self._location = Location(x, y)


    def move_x(self, value):
        self._location.move(value.get_x(),0)

    
