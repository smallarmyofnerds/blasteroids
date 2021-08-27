import pygame
from pygame.math import Vector2
from pygame.transform import rotozoom

UP = Vector2(0, 1)

class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = None
        self.camera_position = Vector2(0, 0)
        self.screen_bottom_left = Vector2(0, 0)

    def init(self):
        self.surface = pygame.display.set_mode((self.width, self.height))

    def reset(self):
        self.surface.fill((0, 0, 0))

    def move_camera_to(self, position):
        self.camera_position = position
        self.screen_bottom_left.x = position.x - 0.5 * self.width
        self.screen_bottom_left.y = position.y - 0.5 * self.height

    def _world_to_viewport(self, position):
        viewport_position = position - self.screen_bottom_left
        viewport_position.y = self.height - viewport_position.y
        return viewport_position

    def draw_sprite(self, sprite, position, orientation):
        angle = orientation.angle_to(UP)
        rotated_sprite = rotozoom(sprite, angle, 1.0)
        rotated_sprite_rect = rotated_sprite.get_rect()
        rotated_sprite_rect.center = self._world_to_viewport(position)
        self.surface.blit(rotated_sprite, rotated_sprite_rect)
