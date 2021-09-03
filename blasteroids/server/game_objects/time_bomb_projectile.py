import pygame
from pygame.math import Vector2
from .projectile import Projectile


class TimeBombProjectile(Projectile):
    def __init__(self, owner, id, position, velocity, collision_radius, damage, timer_duration, explosion_radius, explosion_damage):
        super(TimeBombProjectile, self).__init__(owner, id, 'time_bomb_projectile', position, Vector2(0, 1), velocity, collision_radius, damage)
        self.timer_duration = timer_duration
        self.explosion_radius = explosion_radius
        self.explosion_damage = explosion_damage
        self.created_at = pygame.time.get_ticks()

    def _detonate(self, world):
        targets = world.all_objects_in_range(self.position, self.explosion_radius)
        for target in targets:
            target.take_damage(self.explosion_damage)

    def update(self, world, delta_time):
        if pygame.time.get_ticks() - self.created_at > self.timer_duration:
            self._detonate(world)
            self.destroy()
        else:
            super(TimeBombProjectile, self).update(world, delta_time)

    def apply_damage_to(self, other, world):
        other.take_damage(self.damage)
        self._detonate(world)