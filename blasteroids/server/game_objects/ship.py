import pygame
from .destroyable_game_object import DestroyableGameObject


class Ship(DestroyableGameObject):
    def __init__(self, position, orientation, player):
        super(Ship, self).__init__(position, orientation, pygame.Vector2(0, 0), pygame.Vector2(0, 0))
        self.player = player

    def destroy(self, remove_object, world):
        super(Ship, self).destroy(remove_object, world)
        world.remove_player(self.player)
