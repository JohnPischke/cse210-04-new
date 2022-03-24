from game.casting.falling_object import Falling_Object

class Gem(Falling_Object):
    
    def __init__(self):
        super().__init__()
        self.color = (2,2,2)
        self.points = 1
        self.symbol = "*"
       

    def update(self):
        pass

    def get_color(self):
        return self.color
    


    #symbol, color