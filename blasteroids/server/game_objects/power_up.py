from pygame import Vector2
from .physical_object import PhysicalGameObject


class PowerUp(PhysicalGameObject):
    def __init__(self, id, name, position):
        super(PowerUp, self).__init__(id, name, position, Vector2(0, 1), Vector2(0, 0), 10, 0, 0)
