import pygame
from pygame.math import Vector2
from .projectile import Projectile


class ProximityMineProjectile(Projectile):
    def __init__(self, owner, id, position, velocity, collision_radius, damage, detection_range, timer_duration, explosion_radius, explosion_damage):
        super(ProximityMineProjectile, self).__init__(owner, id, 'proximity_mine_projectile', position, Vector2(0, 1), velocity, collision_radius, damage)
        self.detection_range = detection_range
        self.timer_duration = timer_duration
        self.explosion_radius = explosion_radius
        self.explosion_damage = explosion_damage
        self.armed_at = None
        self.armed = False

    def _detonate(self, world):
        targets = world.all_objects_in_range(self.position, self.explosion_radius, self)
        for target in targets:
            target.take_damage(self.explosion_damage, world)

    def update(self, world, delta_time):
        super(ProximityMineProjectile, self).update(world, delta_time)
        if self.armed:
            if pygame.time.get_ticks() - self.armed_at > self.timer_duration:
                self._detonate(world)
                self.destroy()
        else:
            target = world.ship_closest_to(self.position, self.owner)
            if target:
                if self.position.distance_squared_to(target.position) < self.detection_range * self.detection_range:
                    self.armed = True
                    self.armed_at = pygame.time.get_ticks()

    def take_damage(self, damage, world):
        super(ProximityMineProjectile, self).take_damage(damage, world)
        self._detonate()

    def apply_damage_to(self, other, world):
        other.take_damage(self.damage, world)
        self._detonate(world)

    def can_hit_projectile(self, other):
        return other.can_be_hit_by('proximity_mine')

    def can_be_hit_by(self, type):
        return True
