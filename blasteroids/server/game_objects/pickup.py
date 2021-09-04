import random
from pygame import Vector2
import pygame
from .physical_object import PhysicalGameObject


class Pickup(PhysicalGameObject):
    def __init__(self, id, position, pickup_id, lifespan):
        super(Pickup, self).__init__(id, position, Vector2(0, 1), Vector2(0, 1).rotate(random.random() * 360.0) * random.random() * 40, 10, 0, 0)
        self.pickup_id = pickup_id
        self.lifespan = lifespan
        self.created_at = pygame.time.get_ticks()

    def update(self, world, delta_time):
        if pygame.time.get_ticks() - self.created_at > self.lifespan:
            self.destroy()
        else:
            super(Pickup, self).update(world, delta_time)

    def apply_pickup_to(self, ship, world):
        pass
