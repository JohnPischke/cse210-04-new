from game.casting.stone import Stone
from game.casting.player import Player

class Cast:
    
    def __init__(self):
        self.falling_objects = []
        self.player = ''

    def compare_locations(self):
        pass

    def create_stones(self, number):
        for _ in range(number):
            new_stone = Stone()

    def set_player(self, player):
        self.player = player
