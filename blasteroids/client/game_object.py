import pygame
from .spacegame_utils import wrap_to_world

class GameObject:
    def __init__(self, position, direction, velocity, size):
        self.position = position
        self.direction = direction
        self.velocity = velocity
        self.size = size

    def draw(self, screen):
        pass

    def move(self, world_size):
        self.position = wrap_to_world(self.position + self.velocity, world_size)

    def collides_with(self, other):
        return pygame.sprite.spritecollide(self.mask, other.mask, False, pygame.sprite.collide.mask())