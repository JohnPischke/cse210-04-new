from game.casting.falling_object import Falling_Object

class Stone(Falling_Object):
    
    def __init__(self):
        super().__init__()
        self.color = (1,1,1)
        self.points = -1
        self.symbol = "O"

    def update(self):
        pass

    #symbol, color