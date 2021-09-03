from .weapon import Weapon
from ..proximity_mine_projectile import ProximityMineProjectile


class ProximityMineWeapon(Weapon):
    def __init__(self, collision_radius, damage, detection_range, timer_duration, explosion_radius, explosion_damage):
        self.collision_radius = collision_radius
        self.damage = damage
        self.detection_range = detection_range
        self.timer_duration = timer_duration
        self.explosion_radius = explosion_radius
        self.explosion_damage = explosion_damage
    
    def shoot(self, ship, world):
        world.create_projectile(ProximityMineProjectile(ship, None, ship.position, ship.velocity, self.collision_radius, self.damage, self.detection_range, self.timer_duration, self.explosion_radius, self.explosion_damage))
        ship.reset_weapon()
