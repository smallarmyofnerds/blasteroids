from .weapon import Weapon
from ..time_bomb_projectile import TimeBombProjectile


class TimeBombWeapon(Weapon):
    def __init__(self, collision_radius, damage, timer_duration, explosion_radius, explosion_damage):
        self.collision_radius = collision_radius
        self.damage = damage
        self.timer_duration = timer_duration
        self.explosion_radius = explosion_radius
        self.explosion_damage = explosion_damage
    
    def shoot(self, ship, world):
        world.create_projectile(TimeBombProjectile(ship, None, ship.position, ship.velocity, self.collision_radius, self.damage, self.timer_duration, self.explosion_radius, self.explosion_damage))
        world.create_sound_effect('time_bomb_shot', ship.position)
        ship.reset_weapon()
