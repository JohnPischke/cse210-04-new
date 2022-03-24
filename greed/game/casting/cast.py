from game.casting.stone import Stone
from game.casting.gem import Gem
from game.casting.player import Player
import random

class Cast:
    
    def __init__(self):
        self.falling_objects = []
        self.player = Player(0,0)
        self.points_total = 0
        

    def compare(self):
        for object in self.falling_objects:
            object_y = object.location.get_y()
            if object_y == self.player.get_y():
                print("compare")


    def create_stones(self, number):
        for _ in range(number):
            x = random.randint(0,1)
            if x == 0:
                new_stone = Stone()
            if x == 1:
                new_stone = Gem()
            self.falling_objects.append(new_stone)

    def set_player(self, player):
        self.player = player

    def get_cast(self):
        return self.falling_objects

    def get_player(self):
        return self.player
