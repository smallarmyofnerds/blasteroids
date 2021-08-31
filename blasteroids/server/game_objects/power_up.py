import pygame
from .physical_object import PhysicalGameObject


class PowerUp(PhysicalGameObject):
    def __init__(self, id, position, orientation, name):
        super(PowerUp, self).__init__(id, position, orientation)
        self.name = name
