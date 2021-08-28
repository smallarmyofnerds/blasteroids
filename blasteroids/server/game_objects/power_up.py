import pygame
from .destroyable_game_object import DestroyableGameObject


class PowerUp(DestroyableGameObject):
    def __init__(self, id, position, orientation, name):
        super(PowerUp, self).__init__(id, position, orientation)
        self.name = name
