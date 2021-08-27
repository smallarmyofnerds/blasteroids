import pygame
from pygame.math import Vector2
from pygame.transform import rotozoom

UP = Vector2(0, -1)

class DrawableObject:
    def __init__(self, size):
        self.size = size

    def draw(self, surface, position, direction):
        pass

    def _scale_rotate_and_blit(self, sprite, surface, position, direction):
        scaled_sprite = pygame.transform.scale(sprite, self.size)
        angle = direction.angle_to(UP)
        rotated_sprite = rotozoom(scaled_sprite, angle, 1.0)
        rotated_sprite_size = Vector2(rotated_sprite.get_size())
        blit_position = position - rotated_sprite_size * 0.5
        surface.blit(rotated_sprite, blit_position)
