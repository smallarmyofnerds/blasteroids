import pygame
from .projectile import Projectile


class Laser(Projectile):
    def __init__(self, id, position, orientation, velocity, damage):
        super(Laser, self).__init__(id, 'laser', position, orientation, velocity, damage)
        self.created_at = pygame.time.get_ticks()

    def update(self, world, delta_time):
        if pygame.time.get_ticks() - self.created_at > 500:
            self.destroy(world)
        else:
            super(Laser, self).update(world, delta_time)
