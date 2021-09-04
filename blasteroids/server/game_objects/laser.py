from blasteroids.lib.constants import LASER_HIT_SOUND_ID, LASER_PROJECTILE_ID
import pygame
from .projectile import Projectile


class Laser(Projectile):
    def __init__(self, id, position, orientation, speed, collision_radius, damage, owner, life_span):
        super(Laser, self).__init__(id, position, orientation, orientation.normalize() * speed, collision_radius, damage, LASER_PROJECTILE_ID, owner)
        self.life_span = life_span
        self.created_at = pygame.time.get_ticks()

    def update(self, world, delta_time):
        if pygame.time.get_ticks() - self.created_at > self.life_span:
            self.destroy()
        else:
            super(Laser, self).update(world, delta_time)

    def can_hit_projectile(self, other):
        if other == self.owner:
            return False
        return other.can_be_hit_by('laser')

    def can_be_hit_by(self, type):
        return False

    def apply_damage_to(self, other, world):
        world.create_sound_effect(LASER_HIT_SOUND_ID, self.position)
        super(Laser, self).apply_damage_to(other, world)
