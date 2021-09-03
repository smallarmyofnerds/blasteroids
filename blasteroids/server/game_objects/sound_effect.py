from pygame import Vector2
from blasteroids.server.game_objects.game_object import GameObject


class SoundEffect(GameObject):
    def __init__(self, id, position, name):
        super(SoundEffect, self).__init__(id, name, position, Vector2(0, 1), Vector2(0, 0))
        self.has_happened = False
    
    def update(self, world, delta_time):
        if self.has_happened:
            self.destroy()
        else:
            self.has_happened = True
