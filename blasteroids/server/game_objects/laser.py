import pygame
from .projectile import Projectile


class Laser(Projectile):
    def __init__(self, config, id, position, orientation, velocity, damage):
        super(Laser, self).__init__(id, 'laser', position, orientation, velocity, config.laser_radius, damage)
        self.created_at = pygame.time.get_ticks()

    def _update(self, world, delta_time):
        if pygame.time.get_ticks() - self.created_at > 500:
            self.destroy(world)
