from game.casting.stone import Stone
from game.casting.player import Player

class Cast:
    
    def __init__(self):
        self.falling_objects = []
        self.player = ''
        

    def compare_locations(self):
        for object in self.falling_objects:
            if self.falling_objects[object.location.get_y()] == self.player.location.get_y():
                pass


    def create_stones(self, number):
        for _ in range(number):
            new_stone = Stone()

    def set_player(self, player):
        self.player = player
    def get_falling_objects(self):
        pass
    def get_player(self):
        pass
