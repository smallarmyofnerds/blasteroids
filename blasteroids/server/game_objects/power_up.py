from pygame import Vector2
import pygame
from .physical_object import PhysicalGameObject


class PowerUp(PhysicalGameObject):
    def __init__(self, id, name, position, lifespan):
        super(PowerUp, self).__init__(id, name, position, Vector2(0, 1), Vector2(0, 0), 10, 0, 0)
        self.lifespan = lifespan
        self.created_at = pygame.time.get_ticks()

    def update(self, world, delta_time):
        if pygame.time.get_ticks() - self.created_at > self.lifespan:
            self.destroy()
        else:
            super(PowerUp, self).update(world, delta_time)

    def apply_power_up_to(self, ship):
        pass
