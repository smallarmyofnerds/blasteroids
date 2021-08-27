import pygame
from .destroyable_game_object import DestroyableGameObject


class Projectile(DestroyableGameObject):
    def __init__(self, position, orientation, damage):
        super(Projectile, self).__init__(position, orientation, pygame.Vector2(0, 0), pygame.Vector2(0, 0), damage)
