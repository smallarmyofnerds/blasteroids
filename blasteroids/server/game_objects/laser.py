import pygame
from .projectile import Projectile


class Laser(Projectile):
    def __init__(self, config, owner, id, position, orientation, velocity, damage):
        super(Laser, self).__init__(owner, id, 'laser', position, orientation, velocity, config.laser_radius, damage)
        self.created_at = pygame.time.get_ticks()

    def update(self, world, delta_time):
        if pygame.time.get_ticks() - self.created_at > 500:
            self.destroy()
        else:
            super(Laser, self).update(world, delta_time)
