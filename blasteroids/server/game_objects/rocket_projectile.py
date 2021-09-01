import pygame
from .projectile import Projectile


class RocketProjectile(Projectile):
    def __init__(self, owner, id, position, orientation, speed, collision_radius, damage, life_span):
        super(RocketProjectile, self).__init__(owner, id, 'rocket_projectile', position, orientation, orientation.normalize() * speed, collision_radius, damage)
        self.life_span = life_span
        self.created_at = pygame.time.get_ticks()

    def update(self, world, delta_time):
        if pygame.time.get_ticks() - self.created_at > self.life_span:
            self.destroy()
        else:
            super(RocketProjectile, self).update(world, delta_time)
