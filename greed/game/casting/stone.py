
# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley



from game.casting.falling_object import Falling_Object

class Stone(Falling_Object):
    
    def __init__(self):
        super().__init__()
        self.color = (255,64,64)
        self.points = -1
        self.symbol = "O"

    def update(self):
        pass

    #symbol, color