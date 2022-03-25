from game.casting.stone import Stone
from game.casting.gem import Gem
from game.casting.player import Player
import random

 

# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley


class Cast:
    
    def __init__(self):
        self.falling_objects = []
        self.player = Player(500,600)
        self.points_total = 0
        

    def compare(self):
        index = -1
        for object in self.falling_objects:
            index += 1
            object_y = object.location.get_y()
            object_x = object.location.get_x()
            object_points = object.get_points()
            if object_y == self.player.get_y():
                if object_x >= self.player.get_x() - self.player.get_text_size()/2 and object_x <= self.player.get_x() + self.player.get_text_size()/2:
                    self.points_total += object_points
                    del self.falling_objects[index]


    def create_stones(self, number):
        if len(self.falling_objects) < 300:

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

    def get_points_total(self):
        return self.points_total

    def fall(self):
        index = -1
        for object in self.falling_objects:
            index += 1
            object.fall_down()
            if object.location.get_y() >= 600:
               # self.falling_objects.remove(index)
               del self.falling_objects[index]
        