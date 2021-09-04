from blasteroids.lib.constants import ROCKET_EXPLOSION_SOUND_ID, ROCKET_PROJECTILE_ID, ROCKET_SALVO_EXPLOSION_SOUND_ID
import pygame
from .projectile import Projectile


class RocketProjectile(Projectile):
    def __init__(self, id, position, orientation, velocity, collision_radius, damage, projectile_id, owner, life_span):
        super(RocketProjectile, self).__init__(id, position, orientation, velocity, collision_radius, damage, projectile_id, owner)
        self.life_span = life_span
        self.created_at = pygame.time.get_ticks()

    def on_removed(self, world):
        if self.projectile_id == ROCKET_PROJECTILE_ID:
            world.create_sound_effect(ROCKET_EXPLOSION_SOUND_ID, self.position)
        else:
            world.create_sound_effect(ROCKET_SALVO_EXPLOSION_SOUND_ID, self.position)

    def update(self, world, delta_time):
        if pygame.time.get_ticks() - self.created_at > self.life_span:
            self.destroy()
        else:
            closest_ship = world.ship_closest_to(self.position, self.owner)
            if closest_ship:
                angle_to_closest_ship = -1 * self.orientation.angle_to(closest_ship.position - self.position)
                if angle_to_closest_ship < 0:
                    if angle_to_closest_ship < -180:
                        correction = 45
                    elif angle_to_closest_ship < -45:
                        correction = -45
                    else:
                        correction = angle_to_closest_ship
                else:
                    if angle_to_closest_ship > 180:
                        correction = -45
                    elif angle_to_closest_ship > 45:
                        correction = 45
                    else:
                        correction = angle_to_closest_ship
                self.velocity = self.velocity.rotate(-1 * delta_time * 2 * correction)
                self.orientation = self.velocity.normalize()
            self.position = self.position + delta_time * self.velocity

    def can_hit_projectile(self, other):
        if other.owner == self.owner:
            return False
        return other.can_be_hit_by('rocket')

    def can_be_hit_by(self, type):
        return type == 'laser' or type == 'rocket'
