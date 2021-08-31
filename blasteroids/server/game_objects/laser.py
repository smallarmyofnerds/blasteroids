import pygame
from .projectile import Projectile


class Laser(Projectile):
    def __init__(self, owner, id, position, orientation, speed, collision_radius, damage, life_span):
        super(Laser, self).__init__(owner, id, 'laser', position, orientation, orientation.normalize() * speed, collision_radius, damage)
        self.life_span = life_span
        self.created_at = pygame.time.get_ticks()

    def update(self, world, delta_time):
        if pygame.time.get_ticks() - self.created_at > self.life_span:
            self.destroy()
        else:
            super(Laser, self).update(world, delta_time)
