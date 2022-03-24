from game.casting.stone import Stone
from game.casting.gem import Gem
from game.casting.player import Player
import random

class Cast:
    
    def __init__(self):
        self.falling_objects = []
        self.player = Player(0,0)
        

    def compare_locations(self):
        for object in self.falling_objects:
            if self.falling_objects[object.location.get_y()] == self.player.location.get_y():
                pass


    def create_stones(self, number):
        x = random.uniform(0,1)
        for _ in range(number):
            if x == 0:
                new_stone = Stone()
            else:
                new_stone = Gem()
            self.falling_objects.append(new_stone)

    def set_player(self, player):
        self.player = player

    def get_cast(self):
        return self.falling_objects

    def get_player(self):
        return self.player
