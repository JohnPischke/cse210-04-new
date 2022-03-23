
class Location:
    
    def __init__(self, x, y):
        self._point_x = x
        self._point_y = y

    def move(self, x, y):
        self._point_x += x
        self._point_y += y
        return (self._point_x, self._point_y)

#    def set(self, x, y):
#        self._point_x = x
#        self._point_y = y
#        return (self._point_x, self._point_y)