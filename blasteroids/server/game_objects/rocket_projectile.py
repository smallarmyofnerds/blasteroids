import pygame
from .projectile import Projectile


class RocketProjectile(Projectile):
    def __init__(self, owner, id, position, orientation, speed, collision_radius, damage, life_span, name):
        super(RocketProjectile, self).__init__(owner, id, name, position, orientation, orientation.normalize() * speed, collision_radius, damage)
        self.speed = speed
        self.life_span = life_span
        self.created_at = pygame.time.get_ticks()

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
                self.orientation = self.orientation.rotate(-1 * delta_time * 2 * correction)
                self.velocity = self.orientation.normalize() * self.speed
            self.position = self.position + delta_time * self.velocity

    def can_hit_projectile(self, other):
        if other.owner == self.owner:
            return False
        return other.can_be_hit_by('rocket')

    def can_be_hit_by(self, type):
        return type == 'laser' or type == 'rocket'
