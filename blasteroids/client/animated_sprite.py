from .drawable_object import DrawableObject
import pygame

class AnimatedSprite(DrawableObject):
    def __init__(self, sprite_list, size, ticks_per_frame):
        super(AnimatedSprite, self).__init__(size)
        self.sprite_list = sprite_list
        self.ticks_per_frame = ticks_per_frame
        self.counter = 0
        self.max_counts = len(sprite_list) * ticks_per_frame
    
    def draw(self, surface, position, direction):
        self.counter = (self.counter + 1) % self.max_counts
        self._scale_rotate_and_blit(self.sprite_list[self.counter // self.ticks_per_frame], surface, position, direction)